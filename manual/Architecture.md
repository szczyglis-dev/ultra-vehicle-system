# Architecture and update ownership

The package is built around one vehicle owner and small components with separate responsibilities. `VehicleController` owns the root body, command sampling and module schedule. Modules contribute mechanics; strategies specialize movement or passenger behavior; presentation components consume resolved state.

Two structures help navigate the implementation: categories describe what a component is responsible for, while phases describe when its work runs. They are deliberately separate. A component's folder/category is not sufficient to determine its position relative to another mechanic.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `VehicleController` | Vehicle composition root, configuration boundary and fixed-step orchestration. |
| `IVehicleModule` | `VehicleModule` contracts, categories and the phase dependency sequence. |
| `VehicleModule` | Common component lifecycle and profile-compatibility behavior. |
| `CategoryCore` | Controller-owned schedule for one module category. |
| `Drive` | Nested owner of the current movement strategy. |
| `Passengers` | Nested owner of seats and passenger updates; vehicle.handles owns handle scheduling. |
| `Audio` | Nested owner of audio-channel rendering and routing. |

Part of the [Scripting Reference](Scripting/README.md).

Public types use `UltraVehicleSystem`; reference the `UltraVehicleSystem.Runtime` assembly from your integration. Runtime components do not depend on the demo assembly or a global player singleton.

Editor preparation, validation, component reset defaults, suspension preview scheduling and scene gizmo drawing live in `Editor` and compile into `UltraVehicleSystem.Editor`. Runtime components store the authored configuration and expose shared pose/geometry operations used during Play and editor previews.


## Vehicle composition

The hierarchy is an ownership boundary, not a requirement that every category have a dedicated `GameObject`. Modules can live on appropriate owned children. The controller's registry determines participation; helper components such as a blade or a hand target may instead be advanced by their local owner.

Use the tree below as a responsibility map. For a new feature, first locate the owner that should call it. A new optional mechanic usually belongs in the module pipeline; a new audio channel belongs under `Audio`; a new limb contact belongs under `Passengers`. Adding another independent Unity callback is not necessary for every new component.

A vehicle root owns a `VehicleController`, `Rigidbody`, body collider and registered modules. `WheelColliders` belong to that `Rigidbody`; child transforms can hold meshes, lights, controls, passengers and other modules. Discovery includes inactive children and stops at a nested `VehicleController`.

`wheelSetup` is the authored wheel configuration. `Wheels` exposes the controller-managed runtime adapters. `Wheel` visuals follow suspension/steering/spin; brake-caliper visuals follow suspension and steering without tire spin.

Logical organization, with representative components:

```text
VehicleController
|__ Controller
|   |__ Input (IVehicleInput)
|   |   |__ KeyboardDriveInput
|   |   |__ ActionInput
|   |   |__ InputBuffer / ExternalController
|   |__ InputGate
|   |__ ProfileSwitcher
|__ Physics
|   |__ Friction
|   |__ WheelDynamics
|   |__ TireCollision
|   |__ Damage
|   |__ VehicleMeshDeformation
|__ Drive
|   |__ Drive
|   |   |__ Selected DriveProfile
|   |__ Steering
|   |__ Brakes / ParkingHold
|   |__ Suspension / AntiRoll / ContactEnvelope
|   |__ MotorcycleBalance
|   |__ Tracks
|__ Engine
|   |__ Engine
|   |__ Transmission
|   |__ AutomaticGearbox / ManualGearbox
|   |__ Clutch
|   |__ Differential
|   |__ TractionControl
|   |__ FuelTank
|__ Interior
|   |__ SteeringWheelAnimator / YokeAnimator / SteeringStickAnimator
|   |__ ThrottleAnimator
|   |__ RearMirrors
|   |__ CarHud / AircraftHud
|__ Exterior
|   |__ Wipers
|   |__ Body
|   |   |__ VehicleBodyPart
|   |__ MovingPart
|   |__ Lights
|   |__ LandingGear
|   |   |__ LandingGearPart
|   |__ LandingGearSuspension
|   |__ Propulsion / HoverVisuals
|   |__ AircraftControlSurfaces
|   |__ TrackVisuals
|__ World
|   |__ Passengers
|   |   |__ PassengerSeat
|   |   |   |__ PassengerBody
|   |   |   |__ Passenger controller strategy
|   |   |__ VehicleHandle
|   |   |__ PassengerBehaviour
|   |__ Coupler / Trailer
|   |__ WaterInteraction
|   |__ WeaponBarrel / RocketLauncher / ObjectDropper
|__ Effects
    |__ Tires / TireFeedback
    |__ Events
    |__ Audio
    |   |__ EngineAudio
    |   |__ TireAudio
    |   |__ Other AudioModule channels
    |__ TireSmoke / ExhaustSmoke
    |__ Skidmarks
```

| Category | Extension base | Typical responsibilities |
| --- | --- | --- |
| Controller | `ControllerModule` | Input providers and profile/input routing |
| Physics | `PhysicsModule` | Wheel dynamics, friction, tire contact and damage |
| `Drive` | `DriveModule` | Pedals, steering, suspension and vehicle strategies |
| Engine | `EngineModule` | Engine, gearbox, clutch, differential and traction control |
| Interior | `InteriorModule` / `VehicleHandleAnimator` | Cockpit animators, displays and mirrors |
| Exterior | `ExteriorModule` | Body parts, lights, wipers, landing gear and vehicle presentation |
| World | `WorldModule` | `Passengers`, towing, water interaction and weapons |
| Effects | `EffectsModule` | Contact feedback, audio, particles and tire marks |

Each category has an `I<Category>VehicleModule` contract and a controller-owned `CategoryCore`. These cores are ordinary objects, not extra scene components.

## Command flow

`Command` is a value-type snapshot of driving intent. It carries normalized controls and action requests, without depending on a keyboard, player object or particular vehicle model. An input provider implements `IVehicleInput`; the controller reads the selected provider through `ReadCommand()` once per physics tick.

```text
Keyboard / Input Actions / AI / network / replay
                    |
                    v
Selected IVehicleInput.ReadCommand()
                    |
                    v
VehicleController.Command
  -> physical driving: optional Burnout command resolution
  -> CommandSampled notification and ignition request
  -> clear transient actuation
                    |
                    v
VehicleModule.Step(vehicle, command, fixedDeltaTime)
  transmission -> brakes -> clutch -> power -> steering/movement
  -> remaining physics and presentation phases
                    |
                    v
Resolved state, wheel actuation and module events
                    |
                    v
Telemetry snapshot -> AfterPhysicsStep
```

The module sequence above is abbreviated; the complete phase order is listed in [Physics pipeline](#physics-pipeline). Direct control has a separate motion branch, described below.

### Continuous controls and one-shot requests

| Command data | Meaning and lifetime |
| --- | --- |
| `Throttle`, `Steering`, `Pitch`, `Roll`, `Yaw`, `Lift`, `Strafe` | Signed demands in the range -1 to 1; the active movement profile determines how they are used |
| `Brake`, `Clutch` | Pedal amounts from 0 to 1; clutch zero couples the engine and one releases it |
| `Handbrake`, `Horn`, `Nitro`, `Burnout` | Held requests, supplied for every tick while active |
| `ToggleIgnition`, `ToggleProfile`, `ToggleTransmission`, light/indicator toggles | One-shot requests, consumed by the input provider when sampled |
| `Shift`, `RequestedGear`, `RequestedIndicators` | One-shot selections; zero `Shift` and null nullable selections mean no request. `RequestedGear = 0` explicitly requests neutral; -1 requests reverse |
| `AnalogControls`, `DigitalControls` | Per-channel input metadata used by mechanics to distinguish proportional input from button-driven input; analog takes precedence when both flags are set |

Input adapters retain short button presses until the next physics sample, so a render frame with no physics tick does not lose the action. A custom provider must implement the same contract: keep continuous values available, but return a queued one-shot action only once. Returning the same toggle on every tick repeatedly requests that action.

`InputBuffer` and `ExternalController` already implement this behavior. Select the source with `SetInputSource`, then use their axis/action methods or submit a complete command. `SubmitCommand` replaces the entire pending value, including pending actions; it does not append to an action queue. Release held controls with `ClearControls` when handing control to another producer. See [Input and commands](Scripting/Input.md) for integration examples.

### Example: submit a driving command

Add an `ExternalController` to the vehicle, then assign it and the vehicle to this component. Call `AccelerateAndShiftUp` from your application or UI. The command requests 60% throttle, a small right turn and one upward gear shift. The vehicle must already be configured with a running engine and a gearbox accepting manual shift requests.

<!-- example: CommandFlowExample.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

public sealed class CommandFlowExample : MonoBehaviour
{
    public VehicleController vehicle;
    public ExternalController input;

    public void AccelerateAndShiftUp()
    {
        if (!vehicle || !input || !input.isActiveAndEnabled) return;

        vehicle.SetInputSource(input);
        input.SubmitCommand(new Command(0.6f, 0.15f) {
            ServiceBrake = 0f,
            Shift = 1,
            AnalogControls = InputChannels.Throttle | InputChannels.Steering
        });
    }

    public void ReleaseControls()
    {
        if (input) input.ClearControls();
    }
}
```

On the next physics tick, `ReadCommand()` returns these values and consumes `Shift`. Later ticks retain throttle and steering until replaced or cleared; they do not repeat the shift. Call `ReleaseControls` to release the inputs; this does not actively brake or detach the selected input source. For continuous AI updates, use axis setters and queue shift requests only when needed, so replacing a complete pending command does not erase an unread action.

### Sampling and mechanical resolution

In physical driving, the controller reads the active source, or uses a default command when no enabled source is available. Optional `Burnout.ResolveDriveCommand` can adjust that sample before `CommandSampled` is published. The notification therefore describes the controller's sampled intent, including that adjustment; it is not a report of successful mechanical actions.

The controller handles `ToggleIgnition`, resets `ServiceBrake`, `DriveDemand`, `SteeringAngle` and transient wheel actuation, then passes the same command and timestep to scheduled modules. Each `Step` receives a copy of the struct. Changing that local copy does not change `VehicleController.Command` or the command seen by later modules. Modules communicate resolved results through the owning vehicle and their own state/events.

For example, `Brakes` resolves service braking and drive demand before power is calculated; clutch and gearbox state further constrain transmitted torque. Steering resolves the requested direction into an actual angle. A requested gear can be rejected by gearbox guards, and a held nitro request still depends on its module's eligibility rules. Read the accepted state or its event to determine the result.

The selected provider is sampled once, even if a module changes the profile or input route during the tick. The newly selected input source is read on the next tick. All modules in the current tick retain the sampled command; each still checks compatibility with the active drive profile before stepping.

### From resolved state to presentation

Use the state matching the feature: raw `Command` for an intentional input gesture, resolved `ServiceBrake` for actual brake demand, gearbox state/events for accepted gears, and contact/slip feedback for tire effects. Interior value sources can expose these readings to animators. The handle controller advances immediately before the Feedback phase, after control presentation has advanced, so passenger limb targets can follow the current controls. Audio channels render through their audio owner rather than sampling the input provider again.

At the end of the controller pipeline, `Telemetry` captures vehicle, engine and wheel readings and `AfterPhysicsStep` publishes that snapshot. Individual module events can occur earlier during their own step. Despite its name, `AfterPhysicsStep` marks completion of this controller's pipeline inside `FixedUpdate`; it does not mean Unity has already completed the subsequent native physics simulation.

### Direct control branch

When the selected input also implements active `IDirectInput`, `DirectVehicleMotion` takes chassis motion ownership. The controller skips Burnout command resolution, clears transient actuation, applies the direct motion step and derives service-brake/drive demand from its resulting command. It then publishes `CommandSampled`. Only modules supporting both the current profile and direct control advance. Telemetry uses the direct motion pose and velocity. Releasing direct control restores the captured Rigidbody mode; see [Input](Input.md) for the ownership contract.

## Physics pipeline

The controller advances enabled, profile-compatible modules in dependency order. In direct control, it also checks each module's `SupportsDirectControl` policy. Ordering is:

1. `ExecutionPhase` dependency barrier.
2. The controller's category order within that phase.
3. A module's effective local order within its category. Equal orders retain registration/discovery order.

Phases cover `Contact`, `Transmission`, Braking, `TrailerBraking`, `Clutch`, Power, `Differential`, `Steering`, `Drive`, `Friction`, Assistance, `Suspension`, Balance, Presentation, `Coasting`, Parking, `WheelDynamics`, `Feedback` and `Collision`. They are library execution barriers, independent of Unity's script-order settings. A local order cannot move an engine before its braking/clutch dependencies.

`AfterPhysicsStep` publishes the complete immutable telemetry snapshot after the pipeline. `Impact` copies collision data for deferred consumers; a live Unity `Collision` should only be used during its callback. Presentation reads actuator state, contact feedback and events rather than inferring physics from keyboard input.

## Membership and configuration

Registration and unregistration rebuild immutable membership/order snapshots. The current physics tick retains its captured snapshot; membership/order edits affect the next tick. A disabled or destroyed component is skipped when execution reaches it.

`Configure(vehicle)` may run repeatedly and in Edit Mode. Cache references and apply persistent settings there; do not assume a running simulation. `TryApplyConfiguration` validates wheels, applies persistent configuration and rebuilds ordering. `RefreshModuleOrder` only rebuilds scheduling, without reconfiguring wheels or resetting module state.

Use `RegisterModule`, `UnregisterModule`, `AddModule<T>` and `DiscoverModules` for membership. Unregistering removes physics-pipeline membership; disable an old component too when it owns frame callbacks, resources or subscriptions. Later discovery includes owned components again, so remove a retired component if it must not return.

## Nested owners

Nested ownership keeps specialized helpers from becoming unrelated top-level mechanics. An audio channel does not need to know category ordering, and a finger pose helper does not need to sample vehicle input. Its owner supplies the relevant context at the appropriate time.

When replacing an owner, inventory its local resources and children as well as its public methods. Scheduling replacement work without retiring old subscriptions or transform writers can leave two implementations active even though only one appears in the module registry.

- **`Audio`** owns its local `AudioModule` channels, rendering them once per frame. Channels own their generated audio sources; the core controls mixer/spatial settings. Core disable suspends all its channels.
- **`Passengers`** discovers seats and passenger behaviours. Vehicle Handles discovers and advances controls before the passenger core advances occupants. Each seat owns occupancy, per-limb bindings and a controller-strategy instance.
- **`Drive`** advances the selected serializable `DriveProfile`. Profiles contain configuration; simulation history lives on the vehicle's modules.

Do not tick a registered module, owned handle or audio channel a second time from another update loop. See [Seats](Seats.md), [Audio](Audio.md) and [Drive profiles](DriveProfiles.md).

## Extending a system

Derive from a category base for a new responsibility, or inherit a concrete built-in component for a compatible replacement. Public operations and state use virtual dispatch; protected lifecycle hooks and event publishers support custom implementations. Explicit assigned references remain authoritative. Registry lookup accepts classes and capability interfaces, with caller-owned lists for multiple providers.

The component authoring and ownership contracts are described in [Configuration](Configuration.md); lifecycle, inheritance, event and scheduling examples are in [Scripting](Scripting.md).

## What runs each tick, and where to attach your code

These are ordinary Unity components. `VehicleController.Awake()` initializes the vehicle; its `FixedUpdate()` owns the simulation pipeline. There is no controller-wide render-frame Update or LateUpdate dispatcher for modules.

1. Read the active input source once into `Command`, resolve direct-control/burnout handling and ignition requests, and clear transient brake, drive, steering and wheel actuator outputs.
2. Capture registered category membership and build phase lists. Membership/order changes made during a tick affect the next tick.
3. Run phases in this order: Contact, Transmission, Braking, TrailerBraking, Clutch, Power, Differential, Steering, Drive, Friction, Assistance, Suspension, Balance, Presentation, Coasting, Parking, WheelDynamics, Feedback, Collision. Handles step when the Feedback phase is reached.
4. Within each phase, call `Step(vehicle, command, deltaTime)` for eligible modules in category/local order, then notify their `Stepped` subscribers. Eligibility includes active/enabled state, profile support and direct-control support.
5. Sample sensors, construct the complete telemetry snapshot and publish `AfterPhysicsStep`. This is the end of controller work for that fixed tick; the event is not a callback after Unity's subsequent native physics simulation.

For a new mechanic, derive from the appropriate category base, implement `Configure` and `Step`, select `Phase`/`ExecutionOrder`, then register the instance. Use the supplied fixed `deltaTime`. Do not also call the same mechanic from your own `FixedUpdate`, which would execute it twice. Subscribe to `AfterPhysicsStep` for completed controller telemetry or a module's `Stepped` for that component's completion; unsubscribe when your observer is disabled.

For render-frame UI or animation, add an ordinary `MonoBehaviour.Update()` and read cached telemetry. For a camera or final visual adjustment, use `LateUpdate()` on your own component. Registration schedules only `Step`; Unity calls Update/LateUpdate independently, even on an unregistered component. Disabling/unregistering a module are different operations. Avoid competing writers on wheel, linkage, handle or camera transforms already owned by another component. When ordering against another frame callback matters, configure Unity script execution order or a clear explicit owner; category and Phase only order the vehicle's fixed-step schedule.

For all 19 phase descriptions, category priority, built-in per-category defaults and worked local-order comparisons, see [Custom modules: Phase and ExecutionOrder](Scripting/CustomModules.md#choose-phase-and-executionorder).


## Passenger access and handle responsibilities

Use `PassengerAccess` to coordinate entering and leaving a seat, including door opening, passenger movement and door closing. Occupancy and completion of the full access sequence are separate events; choose the event that matches your gameplay action.

To supply your own boarding animation, implement `AccessMotion`. To create a new control surface, derive from `VehicleHandle` and use its public pose, contact, value and interaction hooks. Use `HandleAnimatorBinding` to connect authored animations to a handle.

See [custom passenger access](Scripting/PassengerAccess.md) and [handle animation](HandleAnimation.md) for configuration and integration examples.
