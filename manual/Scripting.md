# Extend and integrate

To configure built-in systems, begin with [Basic Inspector workflow](InspectorConfiguration.md#basic-inspector-workflow) and the [Inspector-first guide index](Scripting/README.md#start-with-inspector-setup). Adding lights, suspension, clips, particles and ordinary model bindings does not require the custom implementation examples in this chapter.

Start with [Custom modules](Scripting/CustomModules.md) for a complete module tutorial, or [Profiling and debugging](Scripting/ProfilingAndDebugging.md) for captures and custom markers.

For km/h, mph or m/s authoring and readouts, see [Speed units](SpeedUnits.md).

Extend the package at the boundary that already owns the behavior you want to change. Public actions are the right tool for invoking existing behavior. A derived component changes an implementation. A capability interface lets consumers work with several implementations without knowing their concrete types.

The examples in this chapter show two common ways to customize the package: installing a new scheduled mechanic and replacing a narrow part of a built-in mechanic. Both preserve the surrounding vehicle lifecycle rather than copying the complete controller.

## Configuration and live state

Prepare the vehicle's layout and output settings before play. Steering wheel membership/multipliers and tie-rod links are prepared by `Steering.Configure`; lamp appearance/output references and registered audio sources' spatial settings are reused until explicitly refreshed. Inspector edits to those settings during Play Mode need the same refresh as a code edit.

Gameplay state stays live: commands, speed, wheel contact, wheel attachment/availability, brakes, gear selection, lamp requests/blinking, audio volume/pitch and listening contexts. Drive routing/weights remain available for runtime drivetrain control. Ordinary gameplay actions do not require reapplying configuration.

After a deliberate configuration change, call the relevant operation once:

| Changed configuration | Refresh operation |
| --- | --- |
| Steering wheel membership, steering multipliers, tie-rod links or axle layout | `steering.RefreshWheelBindings(vehicle)`; preserves the current steering actuator angle. |
| Lamp colors/intensity/emission, Light/Lens/Glow assignments or glow appearance | `lights.RefreshLightingConfiguration()`; a standalone channel has `channel.RefreshConfiguration()`. |
| Mixer/spatial blend, distances, rolloff, Doppler, spread or voice priority in one `VehicleAudioSettings` | `settings.RefreshConfiguration()`; applied at the next use of that settings block. |
| Spatial/routing edits across several channels of one Audio core | `audio.RefreshPlaybackConfiguration()`; configured sources update at their next use. |
| Authoritative `vehicle.wheelSetup` or a complete vehicle setup | `vehicle.ApplyConfiguration()`; reapplies wheel definitions and configures the modules. |

Refresh operations are configuration actions, not per-frame calls. See [steering](Scripting/DriveDynamics.md#changing-steering-layout), [lights](Scripting/Lights.md#changing-lamp-appearance) and [audio](Scripting/Audio.md#changing-spatial-audio-settings) for examples. Runtime-only Wheel edits are replaced by the authoritative `wheelSetup` values on the next full Apply Configuration; update those definitions too when the change should survive reconfiguration.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `VehicleModule` | Base registration/configuration/step contract for new mechanics. |
| `PhysicsModule` | Category base used by the downforce example. |
| `ModuleSetupAttribute` | Optional installation/menu policy for custom module types. |
| `VehicleController` | Public registration, lookup and reference-connection operations. |
| `Engine` | Provides the virtual crank-torque hook used by the replacement example. |
| `ModuleCatalog` | Discovers eligible module implementations for setup tooling. |

Part of the [Scripting Reference](Scripting/README.md). Namespace: `UltraVehicleSystem`; reference the runtime assembly from your project's asmdef.

## What is available directly on vehicle

In these examples, `vehicle` is an assigned `UltraVehicleSystem.VehicleController`. Assign it through your adapter's Inspector field, or use the owner passed to your module's `Configure(vehicle)` / `Step(vehicle, command, deltaTime)`. Use it as the entry point for shared state and registered mechanics; a property name does not automatically exist for every component type. C# identifiers are case-sensitive.

### Controllers and registries

| Entry point | Available operations and meaning |
| --- | --- |
| `vehicle.parts` | First registered `Body` module, or null. `Open(id)`, `Close(id)`, `Toggle(id)`, `GetPart(id)`, `OpenAll()`, `CloseAll()` and `SetPhysics(id, enabled)` operate on its body parts. |
| `vehicle.parts.parts` | Configured `VehicleBodyPart[]` on that Body module. Check `vehicle.parts` before accessing it. This does not list every MovingPart, gear or suspension helper. |
| `vehicle.parts.damageParts` | Configured damage-boundary array on the Body module; distinct from its movable body parts. |
| `vehicle.handles` | Per-vehicle `HandleController`: `Get(id)`, `TryGet(id, out handle)`, `All`, interaction requests such as `TryUse(...)`, and cancellation such as `CancelSeat(...)` / `CancelAll()`. |
| `vehicle.passengers` | First registered `Passengers` module, or null. Exposes occupant events, `TryEnter(body, seat)`, `TryExit(body)` and `ResetOccupants()`. |
| `vehicle.passengers.Seats` | Seat snapshot array. There is currently no `vehicle.seats` shortcut. Each Seats access clones the array: obtain it once for a UI/configuration operation, retain explicit seat references for repeated use, and reacquire after seat membership changes. `PassengerModules` also returns a copied array. |
| `vehicle.sensors` | Shared read-only live sensor state: sampled acceleration/velocity, attitude, gravity/G-force, ground clearance and last impact. Accessors do not issue a new ground ray; ground results depend on diagnostic ground sampling being enabled. |
| `vehicle.Wheels` | Runtime wheel collection exposed as `IReadOnlyList<Wheel>`. `vehicle.wheelSetup` is its authoring configuration; `vehicle.wheels` is the runtime array. |
| `vehicle.Modules` | Registered modules exposed as `IReadOnlyList<VehicleModule>`. Use registry operations for changes rather than directly editing the backing `vehicle.modules` array. |
| `vehicle.CategoryCores` / `GetCategoryCore(category)` | Category ownership and scheduling cores. Use module APIs for ordinary game actions. |

The optional `parts` and `passengers` shortcuts resolve through the module registry on each access. They include a registered disabled module, do not create a missing component and do not retain a stale cached reference after removal. A disabled module's own action methods still determine whether an operation can run. Cache the resolved reference within an operation when making several calls; resolve again when you need to observe runtime registration changes. For multiple implementations/providers, use `GetModules<T>` instead of assuming a shortcut selects all of them.

```csharp
// vehicle is an assigned VehicleController.
var bodyParts = vehicle.parts;
if (bodyParts)
{
    bodyParts.Open("LeftDoor");             // VehicleBodyPart > Part Id.
    var door = bodyParts.GetPart("LeftDoor");
}

var handle = vehicle.handles.Get("DashboardSwitch1"); // VehicleHandle > ID.
var passengers = vehicle.passengers;
if (passengers)
{
    var seatSnapshot = passengers.Seats;    // One array copy here, not each frame.
    // Use the selected PassengerSeat with passengers.TryEnter(body, seat).
}
```

For setup and complete interaction/boarding examples, see [Body-part actions](MovingParts.md), [Handles](Scripting/Handles.md), [Passenger access](Scripting/PassengerAccess.md) and [Passenger controllers](Scripting/PassengerControllers.md).

### Telemetry data versus telemetry settings

| Entry point | Meaning |
| --- | --- |
| `vehicle.Telemetry` | Latest completed physics-step snapshot (`Telemetry` value type): for example `SpeedKph`, `Rpm`, `Gear`, position, motion and enabled diagnostic sections. Reading it does not calculate another snapshot. |
| `vehicle.telemetry` | `TelemetrySettings` configuration, not the measured results. Flags: `controls`, `motion`, `body`, `powertrain`, `fuel`, `ground`, `wheelDetails`. Inspector: **Vehicle Controller > Setup > Telemetry**, below **Configuration**. Wheel details are off by default; the other optional groups are on by default. |
| `vehicle.Telemetry.HasSection(section)` | Checks whether an optional diagnostic section is present. Disabled sections contain default/empty data; do not interpret their zero values as a physical measurement. |
| `vehicle.AfterPhysicsStep` | Event delivering the completed snapshot after the mechanics pipeline. Prefer it when a consumer needs each finalized physics result. Subscribe/unsubscribe with the observer's lifecycle; see [Events and telemetry](Scripting/Events.md). |

```csharp
var snapshot = vehicle.Telemetry;
float speedKph = snapshot.SpeedKph;
if (snapshot.HasSection(TelemetrySections.Powertrain))
{
    float rpm = snapshot.Rpm;
}

// Optional diagnostic configuration; it does not enable/disable wheel mechanics.
vehicle.telemetry.wheelDetails = false;
```

The controller creates and publishes snapshots during physics processing. Before the first completed step, readings may still have their initial values. Changing telemetry settings affects subsequent samples. Core world pose, velocity, speed and timestamps remain available independently of the optional sections.

### Chassis, controls and state

| Entry point | Meaning |
| --- | --- |
| `vehicle.Body` | Root `Rigidbody`. This is distinct from the body-parts controller returned by `vehicle.parts`. |
| `vehicle.body` | Assigned visible-model `Transform`, not the root Rigidbody or the Body module. |
| `vehicle.SpeedKph`, `SpeedMph`, `GetSpeed(unit)` | Current speed in the requested units. `ForwardSpeed` is signed longitudinal speed; `Velocity` and `AngularVelocity` expose motion vectors. |
| `vehicle.Command` | Latest sampled input command. Supply player/AI/network input through an input provider rather than assigning this protected-set property. |
| `vehicle.DriveDemand`, `ServiceBrake` | Resolved propulsion demand and braking used by mechanics. |
| `vehicle.SteeringAngle`, `SteeringNormalized`, `SteeringWheelAngle` | Road-wheel steering state, normalized steering and logical column angle. Visual mesh inversion is separate. |
| `vehicle.IsDirectControl`, `ForcesReleased`, `IsMoving(...)`, `GetPointVelocity(point)` | Motion/control queries that respect the controller's current movement ownership. |
| `vehicle.settings`, `driveProfile`, `inputSource`, `wheelSetup` | Configuration/input references. Use their supported application APIs when changing them in runtime; editing a field alone does not necessarily reconnect or validate the configuration. |

### Other modules, actions and events

There are no universal `vehicle.engine`, `vehicle.audio` or `vehicle.seats` properties. Resolve installed modules and capability interfaces through `TryGetModule<T>(out module)`; pass `activeOnly: true` when the operation specifically requires an enabled provider. For repeated multi-provider queries, reuse a caller-owned `List<T>` with `GetModules<T>(list, activeOnly)`.

```csharp
if (vehicle.TryGetModule<Engine>(out var engine, activeOnly: true))
    engine.ToggleEngine();
```

The controller also exposes:

- Module lifecycle: `RegisterModule`, `UnregisterModule`, `AddModule<T>`, `SetModuleEnabled<T>` and `RefreshModuleOrder`. See [Module lifecycle](Scripting/Modules.md).
- Configuration/input: `ApplyConfiguration`, `TryApplyConfiguration`, `TrySetDriveProfile` and `SetInputSource`. See [Input](Scripting/Input.md) and [Drive profiles](Scripting/DriveProfiles.md).
- Vehicle operations: `Teleport`, `ResetVehicle`, `RepairPart`, `RepairAll`, `ReleaseAllForces` and `RestoreAllForces`. Use these entry points when their occupant/physics synchronization is required.
- Events: `AfterPhysicsStep`, `CommandSampled`, `Collided`, `Impacted`, `Teleported`, `ConfigurationChanged`, `DriveProfileChanged`, `InputSourceChanged`, `ModuleRegistered`, `ModuleUnregistered`, `WheelAvailabilityChanged`, `WheelAttachmentChanged` and `Repaired`. Use `Impacted` for a retainable impact snapshot; `Collided` carries the live Unity collision callback. See [Events reference](Scripting/EventsReference.md).

For exact signatures, arguments and all remaining properties, see [VehicleController API](API/Core.md#vehiclecontroller).

## Choose the smallest integration point

Start with the caller's need. If a UI button should start the engine, call its action; deriving an engine just to expose that button adds an unnecessary replacement. If an application needs a different torque calculation, a derived engine is appropriate. If several unrelated mechanics should expose a shared application reading, define a capability interface rather than inheriting them all from one concrete component.

Keep application-specific dependencies in adapters. A reusable vehicle mechanic should not discover the local player, UI canvas or network session itself. Pass a reference or feed commands/events across a small explicit boundary.

| Goal | Use |
| --- | --- |
| Trigger an existing behavior | Its public action or `UnityEvent` binding |
| Observe state | Typed events or telemetry snapshots |
| Supply controls | `IVehicleInput`, `InputBuffer` or `ExternalController` |
| Add a mechanic | A category `VehicleModule` subclass |
| Alter an existing mechanic | Its virtual operation in a derived component |
| Add a movement family | A serializable `DriveProfile` |
| Supply a hand/foot contact | `VehicleHandle` |
| Use another character framework | `PassengerBody`, a seat strategy or `AccessMotion` |
| Connect an ocean | `WaterProvider` |

Keep one owner for each responsibility. Replacing a mechanic requires updating explicit references and retiring the old implementation. Adding an observer does not.

## Add a mechanic

Choose a category base for responsibility and a phase for dependencies. The downforce below is an assistance force, so it does not need to replace wheel drive or steering. It reads the configured vehicle's speed and applies acceleration to the root `Rigidbody` through `Body`.

`ForceMode.Acceleration` makes this example's strength an acceleration rather than a force in newtons. The threshold is expressed in km/h because it compares with `SpeedKph`. State the same units in custom Inspector labels or tooltips so users do not have to infer them from implementation.

This component adds downforce in the Assistance phase. Add it through the controller's Custom module menu, or register an existing instance with `RegisterModule`. A category base supplies category membership; `Phase` and `ExecutionOrder` select scheduling.

**Example: `SpeedDownforce.cs`**

<!-- example: SpeedDownforce.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    [AddComponentMenu("My Game/Vehicles/Speed Downforce")]
    public class SpeedDownforce : PhysicsModule
    {
        [Min(0)] public float acceleration = 2;
        [Min(0)] public float minimumSpeedKph = 30;
        public override ExecutionPhase Phase => ExecutionPhase.Assistance;
        public override int ExecutionOrder => 100;

        public override void Step(VehicleController vehicle, Command command, float dt)
        {
            if (vehicle.SpeedKph >= minimumSpeedKph)
                vehicle.Body.AddForce(-vehicle.transform.up * acceleration,
                    ForceMode.Acceleration);
        }
    }
}
```

The controller calls `Step` once per physics tick. Do not call it again from your own `FixedUpdate`. Use `Configure` for owner-local references and persistent setup; it can run repeatedly, including in Edit Mode.

## Install your component on a vehicle, step by step

A script must first be a Unity component, then participate in the package's module contract, and finally belong to this vehicle's registered module set. The three installation paths below use the same `SpeedDownforce` example. Choose one path for each intended instance; they do not require separate implementations of the mechanic.

### 1. Prepare a discoverable module

1. Save the example as `SpeedDownforce.cs` in your application's runtime scripts, outside an `Editor` folder. Let Unity finish compiling and resolve compilation errors before adding it.
2. Keep the component class public, concrete and non-generic. The script filename should match the component class name so Unity can attach it normally.
3. Derive from a category base such as `PhysicsModule`, `DriveModule`, `EngineModule`, `InteriorModule`, `ExteriorModule`, `WorldModule`, `EffectsModule` or `ControllerModule`. Reference `UltraVehicleSystem.Runtime` if your application uses an asmdef.
4. Put repeatable setup in `Configure(vehicle)` and scheduled mechanic work in `Step(vehicle, command, deltaTime)`. Choose `Phase` and `ExecutionOrder` for dependencies; do not add a second `FixedUpdate` that runs the same work.
5. Keep the script in your own assembly. The controller's menu places types from the package runtime assembly under **Base** and types from other assemblies under **Custom**.

The category base matters beyond its name. For example, `PhysicsModule` implements `IPhysicsModule`; the Inspector uses that category interface to choose the menu group. Deriving only from `VehicleModule` and overriding `Category` does not supply the interface used by the menu. An ordinary `MonoBehaviour`, or a class that only implements `IVehicleModule` without deriving from `VehicleModule`, is not part of the controller's module discovery.

### 2. Add through the controller's Add module menu

1. Select the vehicle root that owns `VehicleController`.
2. Open **Modules**, then **Add module...**.
3. Choose **Custom → Physics → Speed Downforce** for the example above. The category comes from its module contract, and the displayed component name comes from the class name.
4. Edit the component's acceleration and minimum speed. The custom component appears in the controller's corresponding module category; use its selection control to inspect the actual component.
5. Click **Apply vehicle configuration** to apply setup and run registered module configuration. Fix any reported vehicle/wheel validation error before checking.

The menu creates the ordinary module on the root, then rediscovers vehicle modules so it is included in the controller's list. Audio channels and passenger behaviors have additional owner-specific authoring steps; use their dedicated technical chapters when extending those systems. The menu operation is distinct from the final configuration step.

`AddComponentMenu` controls Unity's regular **Add Component** menu. It does not define the controller's **Custom** path. A nonempty attribute, such as the one on `SpeedDownforce`, is optional for normal module discovery.

### 3. Add manually on the vehicle root

1. Select the same GameObject as `VehicleController`.
2. Use Unity's **Add Component** and select **My Game → Vehicles → Speed Downforce**, or drag `SpeedDownforce.cs` onto the object.
3. Return to the controller's **Modules** tab and click **Discover and order vehicle modules**.
4. Confirm that the instance appears under **Physics**, then set its configuration/references.
5. Click **Apply vehicle configuration**.

Discovery rebuilds the registry from the hierarchy; it does not call `Configure` on newly found modules. Applying configuration performs that setup. If you also need missing module/controller references filled, use the controller component's context menu **Connect available modules**, then apply configuration. Existing explicit references remain authoritative.

### 4. Add manually on a child object

1. Create a child beneath the vehicle, for example `Custom mechanics`.
2. Keep it beneath the intended `VehicleController`. Do not add a second controller to that branch unless it is a separate vehicle.
3. Add `SpeedDownforce` to the child using **Add Component** or by dragging its script.
4. On the main controller, run **Discover and order vehicle modules**, then **Apply vehicle configuration**.
5. Configure any geometry or local references on the child component. `Step` still receives the owning vehicle; use `vehicle.Body` for forces on the chassis rather than expecting a Rigidbody on that child.

This is useful for organizing mechanisms or placing a component beside its own geometry. A child placement does not require a different base class or another registration component. Discovery includes inactive children, but their modules do not step until their GameObjects and components are active/enabled.

## How the controller discovers and runs modules

There are two different searches. The Inspector searches compiled types to populate **Add module**. The runtime controller searches component instances already attached to its hierarchy. A type appearing in the menu does not mean an instance has been installed, and an installed instance does not have to be offered by that menu to be discoverable.

`DiscoverModules()` uses `GetComponentsInChildren<VehicleModule>(true)`: it includes the root and all inactive/active descendants. It keeps an instance only when its nearest parent `VehicleController`, including inactive parents, is this controller. A nested vehicle therefore owns its own branch; modules below it are excluded from the outer vehicle. Object names, hierarchy depth and the `AddComponentMenu` path do not determine ownership.

The controller orders discovered modules by effective local order and rebuilds category/phase scheduling. Startup `Awake` runs discovery followed by configuration, so components saved on the prefab are available without an application bootstrap script. The controller does not rescan the entire hierarchy every tick. A component added later through `GameObject.AddComponent` needs explicit registration or rediscovery.

| Operation | What it does | When to use it |
| --- | --- | --- |
| `DiscoverModules()` | Rebuilds membership from owned root/child instances and refreshes order; does not configure each found instance. | After assembling/reparenting a hierarchy or manually adding several components. |
| `RegisterModule(instance)` | Adds an existing instance, refreshes scheduling and immediately calls its `Configure` for this vehicle. An already registered instance is not added/configured again. | After creating one runtime component or explicitly installing an existing one. |
| `AddModule<T>()` | Creates `T` on the controller's own GameObject and registers/configures it. | A new root-level runtime mechanic. |
| `ConnectAvailableModules()` | Runs discovery and fills missing compatible module/controller references; can select an input provider if none is assigned. | Setup where installed components should find unassigned dependencies. |
| `TryApplyConfiguration(out error)` | Validates current vehicle setup, configures runtime wheels and all registered modules, and refreshes scheduling. | After changing setup that must be applied to native components or module caches. |
| `RefreshModuleOrder()` | Rebuilds scheduling without searching for components or applying configuration. | Ordering changes among already registered modules. |

Being discovered and being executed are separate conditions. The controller must be enabled and valid; a module must be active/enabled and support the selected profile. `SupportsProfile` controls movement compatibility. Registered disabled modules still receive configuration, so setup should tolerate disabled and Edit Mode use. Use the [module lifecycle reference](Scripting/Modules.md) for lookup, ordering and replacement details.

## Create and register a module from code

Call the following methods from your runtime spawn/setup flow after the vehicle itself is configured. Save the component beside `SpeedDownforce.cs` in the same example namespace. `InstallOnRoot` uses the combined controller API. `InstallOnChild` creates an owned child, sets its values, then registers that exact instance.

**Example: `CustomModuleInstallation.cs`**

<!-- example: CustomModuleInstallation.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class CustomModuleInstallation : MonoBehaviour
    {
        public VehicleController vehicle;

        public void InstallOnRoot()
        {
            if (!vehicle) return;
            vehicle.AddModule<SpeedDownforce>();
        }

        public void InstallOnChild()
        {
            if (!vehicle) return;
            var child = new GameObject("Custom downforce");
            child.transform.SetParent(vehicle.transform, false);
            var module = child.AddComponent<SpeedDownforce>();
            module.acceleration = 3;
            module.minimumSpeedKph = 40;
            vehicle.RegisterModule(module);
        }
    }
}
```

Each call intentionally adds an instance. If the feature should be unique, find the intended existing instance before creating another. If several components are assembled together, an alternative is to finish authoring them, run `ConnectAvailableModules()` and then `TryApplyConfiguration(out error)`. Do not assume `TryApplyConfiguration` will discover components that were never registered.

`RegisterModule` is an explicit low-level registry operation, not an ownership search. Keep registered instances under the intended controller just as in the child example. Moving an already registered component between vehicles needs an explicit handover: unregister it from the old controller, reparent it, then register/configure it on the new one.

## Menu visibility and installation policy

Most application modules need no metadata beyond a category base. Use `ModuleSetupAttribute` only when you want a specific setup policy. These choices are separate from discovery of components that already exist on the hierarchy.

| Declaration / condition | Effect |
| --- | --- |
| Public concrete category-module class in your runtime assembly | Eligible for normal Unity attachment and the controller's corresponding **Custom** category. |
| `[AddComponentMenu("My Game/Vehicles/Speed Downforce")]` | Gives Unity's regular **Add Component** a path; does not change the controller's Custom category/name. |
| `[AddComponentMenu("")]` | Hides the type from the controller menu unless `ModuleOnly = true` opts it back in. |
| `[ModuleSetup(ModuleOnly = true)]` | Allows a module hidden by an empty `AddComponentMenu` to appear in the controller menu. |
| `[ModuleSetup(IncludeInFull = false)]` | Excludes the type from automatic full setup/catalog installation; the Inspector's explicit **Add module** choice remains available. |
| `[ModuleSetup(EnabledByDefault = false)]` | Disables a newly installed instance in full setup. It does not make every manually/menu-created instance start disabled. |
| Abstract/open generic class, missing category interface or compilation/assembly problem | Not a usable normal Custom-menu entry; fix the type/assembly before checking hierarchy ownership. |

For a hidden optional module, `[ModuleSetup(ModuleOnly = true, IncludeInFull = false)]` combines manual controller-menu availability with exclusion from full setup. Do not add a registration list or modify package source just to make an ordinary custom module discoverable.

## When a component is missing

If the class is absent from **Add module → Custom**, check compilation, runtime assembly placement, its concrete category base and any inherited `AddComponentMenu`/`ModuleSetup` metadata. If an instance is absent from the controller's list, check that it derives from `VehicleModule`, belongs under this controller rather than a nested vehicle, and that discovery has run since it was added.

If the instance is listed but its `Step` does not run, check active/enabled state, `SupportsProfile`, controller validation errors and whether its system uses a nested scheduler. `VehicleHandle` is a passenger-owned helper, not a top-level `VehicleModule`: assign it through the seat/`Passengers` system and follow [Handles](Scripting/Handles.md). Audio channels and passenger modules likewise keep their owner-specific update contracts; do not add an independent tick to force them to run.

## Extend an existing operation

`virtual` marks a method or property as replaceable through inheritance. `override` supplies the derived implementation while preserving dispatch through a base-typed reference. `base` calls the inherited implementation explicitly; use it when adding behavior around the existing algorithm.

`sealed` prevents further inheritance of a class, or further overriding of a particular override. It is useful for fixed data/implementation contracts but is not an extension point. A public field is configurable data, not a virtual operation: hiding it in a subclass creates another field rather than changing what existing code reads.

The example below changes only crank-torque evaluation. It retains running-state handling, gearbox selection, clutch coupling and the rest of the engine lifecycle. This is easier to keep compatible than copying the entire engine into an application component.

Override a virtual operation and call base when retaining its work. This example scales the engine's evaluated crank torque without copying gearbox or clutch logic.

**Example: `LimitedTorqueEngine.cs`**

<!-- example: LimitedTorqueEngine.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class LimitedTorqueEngine : Engine
    {
        [Range(0, 1)] public float availablePower = 1;

        protected override float EvaluateCrankTorque(float rpm)
            => base.EvaluateCrankTorque(rpm) * availablePower;
    }
}
```

This hook affects gearbox combustion paths; Direct drive uses `Settings.motorTorque`. Use it in place of the configured `Engine` and update `Transmission`, audio and other explicit engine references. The [module reference](Scripting/Modules.md) explains registration, replacement and reference connection.

## Replacement contracts

Install a replacement as a handover, not as an additional writer. Resolve the old implementation's explicit consumers, retire its scheduled/independent work and point those consumers at the replacement. Registry lookup does not automatically rewrite fields already assigned to a component.

Before changing a virtual operation, inspect what its callers rely on: return values, accepted-state changes, event timing and resource cleanup. A subclass can preserve a method signature while breaking its behavioral contract. Check the application-facing behavior, especially rejected requests and disable/re-enable boundaries.

- Use `override`, rather than hiding an operation with `new`, for dispatch through built-in reference types.
- Preserve base lifecycle cleanup when extending a component. A full replacement owns any cleanup, state and validation it omits.
- Protected state setters and `Raise<EventName>` helpers support publishing replacement state. Calling a base action already publishes its own events.
- Public fields configure components; they are not override points. Extra fields in a runtime subtype do not automatically persist through an inline field serialized as its concrete base type.
- Specialized inspectors apply to subclasses. Additional serialized fields appear with the base inspector or its Custom fields area.

Fixed nested-scheduler entry points, value snapshots and private caches remain implementation contracts. See [Architecture](Architecture.md) for ownership boundaries.

## Follow a worked integration

Use [Events reference](Scripting/EventsReference.md) to find notifications by name, owner and firing boundary.

[Input handover](Scripting/Input.md), [profile creation](Scripting/DriveProfiles.md), [handle contacts](Scripting/Handles.md), [custom passengers](Scripting/PassengerControllers.md), [water adapter](Scripting/Water.md), [events and telemetry](Scripting/Events.md), [timed interactions](Scripting/Interactions.md) and [weapon control](Scripting/Weapons.md) each provide a complete component example.

## Profiling and debugging

See [Profiling and debugging](Scripting/ProfilingAndDebugging.md) for the capture workflow, built-in markers and a complete custom-marker example.
