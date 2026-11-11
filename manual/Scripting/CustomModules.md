# Custom modules

This tutorial adds a small custom downforce mechanic, installs it through the vehicle Inspector and optionally exposes it through Unity's component and Tools menus. Keep your code in your game's Assets folder or runtime assembly so package updates preserve it. The example uses the `UltraVehicleSystem` namespace from the `UltraVehicleSystem.Runtime` assembly.

## Choose what to inherit

For a mechanic called once per vehicle fixed tick, inherit the category base matching its responsibility: `ControllerModule`, `DriveModule`, `EffectsModule`, `EngineModule`, `ExteriorModule`, `InteriorModule`, `PhysicsModule` or `WorldModule`. Each supplies the category interface used by the Inspector. Deriving directly from `VehicleModule` leaves you without a category-specific interface for the Add module menu; use a category base for this tutorial.

`Category` chooses the responsibility group. `Phase` chooses the dependency barrier; `ExecutionOrder` chooses priority among peers within the phase/category. The example adds a chassis force, so it uses `PhysicsModule` in the `Assistance` phase. It does not replace the engine or the drive profile.

Some extension points have a different owner: derive from `AudioModule` and implement `RenderAudio` for a sound channel, `CameraModule` for a `Cameras`-owned view, or `PassengerBehaviour` and implement `StepBehaviour` for a seat behavior. Their nested owners advance them; adding an independent `FixedUpdate` does not integrate them correctly. To change an existing algorithm, derive from that implementation and override its narrow virtual operation instead. To introduce a movement family, create a `DriveProfile`.

## Create the runtime component

Save the following as `Assets/MyGame/Vehicles/CustomDownforce.cs`. If this folder uses an asmdef, reference `UltraVehicleSystem.Runtime`. Keep this class public, concrete and outside an Editor folder. The filename must match the component class name.

The example applies `acceleration` in m/s², rather than a force in newtons. It acts only above a configured speed while at least one native wheel is grounded. A flying vehicle with no contact wheels therefore receives no force from this example.

<!-- example: CustomDownforce.cs -->
```csharp
using UltraVehicleSystem;
using UnityEngine;

namespace MyGame.Vehicles
{
    [DisallowMultipleComponent]
    [AddComponentMenu("My Game/Vehicles/Custom Downforce")]
    [ModuleSetup(IncludeInFull = false)]
    public class CustomDownforce : PhysicsModule
    {
        [Min(0)] public float acceleration = 2f;
        [Min(0)] public float minimumSpeedKph = 40f;

        public override ExecutionPhase Phase => ExecutionPhase.Assistance;
        public override int ExecutionOrder => 200;
        public override bool SupportsDirectControl => false;

        public override void Configure(VehicleController vehicle)
        {
            base.Configure(vehicle);
            acceleration = Mathf.Max(0f, acceleration);
            minimumSpeedKph = Mathf.Max(0f, minimumSpeedKph);
        }

        public override void Step(VehicleController vehicle, Command command, float deltaTime)
        {
            if (!vehicle.Body || vehicle.SpeedKph < minimumSpeedKph) return;

            bool grounded = false;
            foreach (var wheel in vehicle.Wheels)
                if (wheel.Grounded) { grounded = true; break; }
            if (!grounded) return;

            vehicle.Body.AddForce(-vehicle.transform.up * acceleration,
                ForceMode.Acceleration);
        }
    }
}
```

`Configure` is repeatable setup, including during editor configuration and for registered disabled modules. Validate values and resolve/cache dependencies there. Do not spawn another resource or subscribe again on every call. `Step` receives the owning vehicle, the same sampled `Command` as the other mechanics, and the fixed timestep in seconds. Use `deltaTime` for your own rates/integration; `AddForce` already participates in Unity's physics integration, so this `acceleration` is not multiplied by `deltaTime`.

`SupportsProfile` can reject drive profiles your mechanic does not support. `SupportsDirectControl` is separate: force mechanics should not run while a direct input source owns the vehicle pose. Leave the category's default behavior or override it deliberately. If your module owns subscriptions, loops or generated resources, release them on disable/destroy and preserve base cleanup when overriding a built-in lifecycle method.

## Choose Phase and ExecutionOrder

The two overrides in the example select different levels of the schedule. `public` keeps the inherited properties accessible, `override` replaces their virtual getters, and `=>` returns the value whenever the getter is read. `Phase => ExecutionPhase.Assistance` places the mechanic in the Assistance barrier. `ExecutionOrder => 200` assigns a local priority inside its category and phase. The number is an ordering key, not a timestep, frequency, delay or Unity script execution order.

The controller compares three levels, in this order: `Phase`, category position in `vehicle.categoryExecutionOrder`, then `EffectiveExecutionOrder` inside that category. Lower local numbers run first. An order of `200` cannot move an Assistance mechanic before a Contact mechanic, and it cannot move a Physics mechanic before an Engine mechanic in the same phase when Engine is the earlier category.

### All execution phases, in tick order

| Position | Phase | Purpose / when to use | Built-in examples |
| --- | --- | --- | --- |
| 1 | `Contact` | Prepare wheel support, geometry and early assistance settings. Use for data later wheel/drivetrain stages need. | `Suspension`, `ContactEnvelope`, `DrivingAssists`, `AirplaneGroundContact`, `LandingGear`, `LandingGearSuspension` |
| 2 | `Transmission` | Resolve transmission selection before brake, clutch and engine work. | `Transmission` |
| 3 | `Braking` | Resolve service/handbrake demand before propulsion. | `Brakes` |
| 4 | `TrailerBraking` | Propagate towing brake demand after the towing vehicle resolves braking. | `Trailer` |
| 5 | `Clutch` | Resolve clutch coupling and related shift-control work before power. | `Clutch`, `GearShiftAnimator` |
| 6 | `Power` | Resolve burnout/boost/fuel and engine output before axle torque distribution. | `Burnout`, `Nitro`, `FuelTank`, `Engine` |
| 7 | `Differential` | Distribute resolved engine torque to the driven wheels. | `Differential` |
| 8 | `Steering` | Resolve steering angles before the drive strategy. | `Steering` |
| 9 | `Drive` | Execute the active drive profile using resolved drivetrain and steering state. | `Drive` |
| 10 | `Friction` | Resolve contact grip and native tire friction before later assists. | `Friction` |
| 11 | `Assistance` | Run general mechanics and assistance that need the earlier drivetrain/contact results. This is the Module default; many components inherit it. | `TractionControl`, tutorial `CustomDownforce` |
| 12 | `Suspension` | Apply later suspension assistance. Native spring/support preparation already runs in Contact. | `AntiRoll` |
| 13 | `Balance` | Apply balancing assistance after suspension-related mechanics. | `MotorcycleBalance` |
| 14 | `Presentation` | Advance scheduled control/part presentation before passenger feedback. This is still a fixed-tick phase. | `SteeringWheelAnimator`, `AircraftControlSurfaces`, `Lights` |
| 15 | `Coasting` | Resolve low-speed wheel contact-release assistance after the main mechanics. | `Coasting` |
| 16 | `Parking` | Resolve parking-hold behavior after drive/coasting decisions. | `ParkingHold` |
| 17 | `WheelDynamics` | Apply final wheel rotational behavior, including airborne losses. | `WheelDynamics` |
| 18 | `Feedback` | Advance handles and passenger/contact feedback. Handles run at the start of this phase; controller telemetry publication follows the entire schedule. | `Passengers`, `WaterInteraction`, `Events`, `TireFeedback` |
| 19 | `Collision` | Run supplemental tire collision processing after the preceding mechanic stages. This is not a replacement for Unity collision callbacks. | `TireCollision` |

Choose the phase from the dependency your code needs, not from the numeric order of another component. In particular, `Suspension` the component runs in `Contact`; `ExecutionPhase.Suspension` is the later barrier used by `AntiRoll`. Similarly, changing an animator to a phase after `Feedback` would make its new pose unavailable to passenger work earlier in that tick. These barriers order UVS callbacks; they do not reschedule Unity native physics or render-frame callbacks.

### Default category priority inside each phase

The default `vehicle.categoryExecutionOrder` is the sequence below. It is independent of the declaration order of `ModuleCategory` and of the alphabetical documentation catalog. The position is only relevant when two modules are in the same phase; categories are revisited for each phase rather than run once as eight complete blocks.

| Position | Category | Typical responsibility |
| --- | --- | --- |
| 1 | `Controller` | Command adapters and profile selection |
| 2 | `Engine` | Engine, gearbox, clutch, fuel and torque allocation |
| 3 | `Drive` | Drive strategy, wheel steering/brakes and suspension |
| 4 | `Physics` | Contact/grip, damage and supplemental wheel physics |
| 5 | `World` | Passengers, towing, weapons, cameras and water |
| 6 | `Interior` | Cockpit controls and readouts |
| 7 | `Exterior` | Bodywork, gear, lights and visible equipment |
| 8 | `Effects` | TireFeedback, audio and visual effects |

Change the controller category order when an intentional dependency spans categories within one phase. Duplicate categories are kept once; omitted categories are appended, so omitting a category does not disable it. Do not rely on local `ExecutionOrder` to cross a category boundary.

### Built-in Phase and ExecutionOrder defaults by category

The common `VehicleModule` defaults are `Phase = ExecutionPhase.Assistance` and `ExecutionOrder = 700`. All eight category bases inherit these values unless a more specialized base or component overrides them. A category has a position in the controller list, not a reserved numeric band of module priorities. The following tables list concrete built-ins and their inherited or overridden property values; Inspector overrides and subclasses can change their effective local priority.

#### Controller defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `Assistance` | 700 | `ActionInput`, `DirectController`, `ExternalController`, `InputBuffer`, `InputGate`, `KeyboardBoatInput`, `KeyboardDriveInput`, `KeyboardFlightInput`, `KeyboardSubmarineInput`, `ProfileSwitcher` |

#### Engine defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `Transmission` | 100 | `Transmission` |
| `Clutch` | 250 | `Clutch` |
| `Power` | 250 | `Nitro` |
| `Power` | 290 | `FuelTank` |
| `Power` | 300 | `Engine` |
| `Differential` | 350 | `Differential` |
| `Assistance` | 550 | `TractionControl` |
| `Assistance` | 700 | `AutomaticGearbox`, `ManualGearbox` |

#### Drive defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `Contact` | 50 | `Suspension` |
| `Contact` | 90 | `ContactEnvelope` |
| `Contact` | 700 | `DrivingAssists` |
| `Braking` | 200 | `Brakes` |
| `Power` | 240 | `Burnout` |
| `Steering` | 400 | `Steering` |
| `Drive` | 450 | `Drive` |
| `Assistance` | 700 | `Tracks` |
| `Suspension` | 600 | `AntiRoll` |
| `Balance` | 650 | `MotorcycleBalance` |
| `Parking` | 860 | `ParkingHold` |

#### Physics defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `Contact` | 60 | `AirplaneGroundContact` |
| `Friction` | 500 | `Friction` |
| `Assistance` | 700 | `Damage`, `VehicleMeshDeformation` |
| `Coasting` | 850 | `Coasting` |
| `WheelDynamics` | 870 | `WheelDynamics` |
| `Collision` | 950 | `TireCollision` |

#### World defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `TrailerBraking` | 210 | `Trailer` |
| `Assistance` | 700 | `Cameras`, `Coupler`, `InteriorCamera`, `ObjectDropper`, `OrbitCamera`, `RocketLauncher`, `WeaponBarrel` |
| `Feedback` | 50 | `BalanceRider`, `SteeringHandRegrip` |
| `Feedback` | 700 | `Passengers`, `WaterInteraction` |

#### Interior defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `Clutch` | 700 | `GearShiftAnimator` |
| `Assistance` | 700 | `AircraftHud`, `CarHud`, `RearMirrors` |
| `Presentation` | 700 | `AnchoredControlAnimator`, `GearLeverAnimator`, `GearPaddleAnimator`, `InstrumentNeedle`, `PedalAnimator`, `RotaryAnimator`, `SteeringStickAnimator`, `SteeringWheelAnimator`, `SwitchAnimator`, `ThrottleAnimator`, `TwistThrottleAnimator`, `YokeAnimator` |

#### Exterior defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `Contact` | 35 | `LandingGearSuspension` |
| `Contact` | 40 | `LandingGear` |
| `Assistance` | 700 | `Body`, `HoverVisuals`, `MovingPart`, `Propulsion`, `TrackVisuals`, `Wipers` |
| `Presentation` | 700 | `AircraftControlSurfaces` |
| `Presentation` | 800 | `Lights` |

#### Effects defaults

| Phase | Default ExecutionOrder | Components |
| --- | --- | --- |
| `Assistance` | 700 | `Audio`, `BoatWaterAudio`, `BoatWaterParticles`, `BrakeAudio`, `CommercialAudio`, `DamageAudio`, `EngineAudio`, `EventAudio`, `ExhaustSmoke`, `HornAudio`, `IndicatorAudio`, `PropulsionJets`, `Skidmarks`, `SwitchAudio`, `TireAudio`, `TireSmoke`, `WeaponEffects`, `WeaponRecoil` |
| `Feedback` | 700 | `Events` |
| `Feedback` | 900 | `TireFeedback` |

These are scheduling-property defaults, not a promise that every component performs its main work in top-level `Step`. Input is read before the scheduled phases. `Engine` advances the selected gearbox through its own simulation contract; the gearbox components inherit `Assistance`/`700` without moving their actual gearbox algorithm there. `AudioModule` channels render through `Audio`; `CameraModule` views render through `Cameras`. `PassengerBehaviour` components inherit `Feedback`/`50`, but `Passengers` owns their `StepPassenger`/`StepBehaviour` sequence and their top-level `Step` is sealed and empty. Geometry-only helpers do not have a controller `ExecutionOrder`.

### What 200 means for CustomDownforce

`CustomDownforce` inherits `PhysicsModule`, chooses `Assistance`, and uses local order `200`. Within `Physics/Assistance` it runs before `Damage` and `VehicleMeshDeformation`, which inherit `700`. However, `TractionControl` is `Engine/Assistance` with order `550`, so it still runs before `CustomDownforce` under the default category sequence. This compares their scheduled slots; collision damage routing and mesh upload retain their own callback timing. The smaller number does not overtake the earlier category. All Contact, Power, Drive and Friction stages have also already finished.

There is no special requirement to use `200`; it is a deliberate example priority with room for another `Physics/Assistance` module at `100` or `300`. Use the inherited `700` if no relative local dependency matters. If your custom Physics mechanic must run before downforce in the same phase, choose a smaller local number. If it must prepare contact data before power resolution, choose `Contact` and then decide its order relative to the other `Physics/Contact` work. Merely changing `200` to `0` while keeping `Assistance` cannot establish that dependency.

### Inspector overrides, ties and runtime changes

`ExecutionOrder` is the implementation default. `EffectiveExecutionOrder` returns `localExecutionOrder` when `overrideExecutionOrder` is true, otherwise it returns `ExecutionOrder`. Enable the Inspector order override and set a local number to tune an existing instance without creating a subclass. This changes only its place inside its category and phase; it does not change `Phase`. With the override disabled, the stored local value of `0` is not an active priority override.

Equal effective orders retain registry order in the current category snapshot. Discovery establishes that registry order; explicit registration can insert a component according to its default order or a supplied index. If a dependency matters, give the components distinct local priorities instead of relying on hierarchy/discovery ties. Module lookup order is separate from execution order.

After editing `vehicle.categoryExecutionOrder`, `overrideExecutionOrder` or `localExecutionOrder` from code, call `vehicle.RefreshModuleOrder()`. A custom runtime change to a getter-backed `ExecutionOrder` also needs this refresh because the category order is cached. `Phase` is read while building each tick's phase lists; changing it during a tick takes effect on the next tick. Applying vehicle configuration and registration changes also rebuild scheduling. `RefreshModuleOrder()` rebuilds ordering without configuring wheels or resetting simulation. Use Unity script execution order only for independent Unity callbacks such as `Update()`/`LateUpdate()`; it cannot change these internal phase barriers.

## Find it in Add module

1. Wait for Unity compilation to finish with no errors, then select a vehicle with `VehicleController`.
2. Open its **Add module** menu and choose **Custom > Physics > Custom Downforce**. Custom is selected because the class lives outside the package runtime assembly; Physics comes from `PhysicsModule`; Custom Downforce is the readable class name.
3. Set Acceleration and Minimum Speed Kph, then apply vehicle configuration. Test a supported wheeled vehicle above and below the threshold. Compare enabled/disabled behavior under the same input and ground conditions.

No package registry edit is needed. The Inspector searches loaded concrete public types and recognizes their category contracts. `AddComponentMenu` does not rename or move this Inspector entry. Special bases use dedicated paths, such as Custom > Effects > Audio, Custom > World > Cameras, Custom > World > Passengers and Custom > Interior > Animators/Handles.

`ModuleSetup(IncludeInFull = false)` keeps this tutorial component out of automatic full setup while retaining the explicit Add module choice. `EnabledByDefault = false` changes the initial enabled flag during full setup; it does not force every manually added component to start disabled. An empty `AddComponentMenu` hides a type from the controller menu unless `ModuleSetup(ModuleOnly = true)` opts it back in. These attributes are optional policies, not a registration requirement.

## Add Component and runtime installation

The `AddComponentMenu` attribute above adds **My Game > Vehicles > Custom Downforce** to Unity's ordinary Add Component menu. After adding through that menu, discover/register the component with its owning controller and apply configuration. Attaching a `MonoBehaviour` alone is separate from membership in the UVS schedule.

For an already attached instance, use `vehicle.RegisterModule(instance)`. Registration configures a newly registered instance and adds it to the next applicable schedule. For a new root component, `vehicle.AddModule<CustomDownforce>()` creates and registers it; the helper does not suppress duplicate creation, so first check for the intended existing instance. If setup values must be assigned before `Configure`, create the component, assign those values, then register that instance.

For a hierarchy assembled from several components, `vehicle.ConnectAvailableModules()` discovers owned children and fills missing compatible module references. Assign geometry and application-specific assets yourself, then call `vehicle.TryApplyConfiguration(out error)` and handle a `false` result. Discovery stops at a nested controller. Put a child module under the intended vehicle and transfer ownership explicitly if it moves to another vehicle.

## Add an optional Tools entry

`AddComponentMenu` does not generate a new Tools command. The package's built-in Tools entries are explicitly declared editor commands. Add your own Editor script; do not edit the package's `ComponentMenu` file.

Save the following as `Assets/MyGame/Vehicles/Editor/CustomDownforceMenu.cs`. If you use asmdefs, place it in an Editor-only assembly referencing your game runtime assembly and `UltraVehicleSystem.Runtime`. Select the vehicle root, then use **Tools > UltraVehicleSystem > Add Component > Custom > Custom Downforce**. This command reuses an existing component on that root, supports Undo, connects the vehicle and reports configuration errors. Runtime spawning should use the runtime API above.

<!-- example: CustomDownforceMenu.cs -->
```csharp
using UltraVehicleSystem;
using UnityEditor;
using UnityEngine;

namespace MyGame.Vehicles.Editor
{
    public static class CustomDownforceMenu
    {
        private const string Path =
            "Tools/UltraVehicleSystem/Add Component/Custom/Custom Downforce";

        [MenuItem(Path)]
        private static void Add()
        {
            var vehicle = Selection.activeGameObject.GetComponent<VehicleController>();
            Undo.IncrementCurrentGroup();
            int group = Undo.GetCurrentGroup();
            Undo.SetCurrentGroupName("Add Custom Downforce");
            try
            {
                Undo.RegisterFullObjectHierarchyUndo(vehicle.gameObject,
                    "Add Custom Downforce");
                var module = vehicle.GetComponent<CustomDownforce>();
                if (!module) module = Undo.AddComponent<CustomDownforce>(vehicle.gameObject);

                vehicle.ConnectAvailableModules();
                if (!vehicle.TryApplyConfiguration(out var error))
                    Debug.LogError(error, vehicle);

                foreach (var component in vehicle.GetComponentsInChildren<Component>(true))
                {
                    if (!component) continue;
                    EditorUtility.SetDirty(component);
                    if (PrefabUtility.IsPartOfPrefabInstance(component))
                        PrefabUtility.RecordPrefabInstancePropertyModifications(component);
                }
                EditorGUIUtility.PingObject(module);
            }
            finally { Undo.CollapseUndoOperations(group); }
        }

        [MenuItem(Path, true)]
        private static bool Validate()
            => !Application.isPlaying && Selection.activeGameObject &&
               Selection.activeGameObject.GetComponent<VehicleController>();
    }
}
```

Keep `UnityEditor` references in the Editor file. The runtime component must compile into a player build without an editor assembly dependency. This Tools example is specific to the root force module; audio, camera, passenger and handle additions must also establish their own nested owner and bindings.

## Follow the module flow

1. Unity creates/enables the component using its normal `Awake`/`OnEnable` lifecycle. Those callbacks do not mean UVS registration/configuration has already happened.
2. Controller initialization/discovery or explicit registration establishes membership. Controller-driven `Configure` prepares the module; `Configured` notifies observers when that setup finishes. Reconfiguration can happen later.
3. Each controller `FixedUpdate` samples input and clears transient actuators. It schedules the module in its phase/category/local order, subject to active/enabled, profile and direct-control checks.
4. `Step` executes once when eligible, then the controller publishes that module's `Stepped` event. After all phases, it builds telemetry and publishes `AfterPhysicsStep`. The module receives an automatic `UVS.Module.CustomDownforce` profiler scope when profiling is enabled.
5. `SetEnabled(false)` disables scheduled execution and invokes Unity disable cleanup. `UnregisterModule` only removes registry membership; it does not disable independent `Update`/`LateUpdate` callbacks. Disable/remove the old component and update consumers when replacing it.

Use an ordinary `Update` for per-frame UI and `LateUpdate` for final presentation when needed, with an explicit transform owner/order. Do not call `Step` again from `FixedUpdate`. Changes to registry/order during a running tick affect the next tick. After editing execution ordering, use `RefreshModuleOrder`; after changing wheel/module configuration, apply configuration.

## If it does not appear or run

For a missing menu type, check compilation, public/concrete visibility, filename/runtime assembly, category inheritance and inherited `AddComponentMenu`/`ModuleSetup` policy. A class in the package assembly appears under Base, while application code appears under Custom. A plain `MonoBehaviour` helper is not automatically a category module.

For a visible component with no `Step`, check registry membership, vehicle ownership and validation, enabled state, profile support and direct-control mode. For no visible force, check speed, native ground support and the configured `acceleration`. Use the automatic module scope and a custom `ProfilerMarker` to inspect execution; do not rely on per-tick logging for performance measurements.

Continue with [`VehicleModule` lifecycle](Modules.md), [Architecture](../Architecture.md) and [Profiling and debugging](ProfilingAndDebugging.md).
