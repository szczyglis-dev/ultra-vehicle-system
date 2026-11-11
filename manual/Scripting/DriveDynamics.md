# Engine, transmission and traction

The drivetrain turns a driving request into a bounded torque budget at the wheels. `Engine` produces power, a gearbox and clutch determine coupling, `Differential` distributes output and `TractionControl` limits what the available contact can transmit. Braking and steering remain separate mechanics coordinated by the same command pipeline.

This division gives each extension a clear scope. Change a torque curve in the engine, a selection rule in the gearbox, axle distribution in the differential or slip intervention in traction control. Writing wheel torque from an unrelated update loop bypasses those relationships and makes budgets difficult to preserve.

## Configure in the Inspector first

Build a [driving chassis](../Physics.md#inspector-quick-start-a-basic-driving-chassis), then configure [gearbox](../Gearbox.md#inspector-quick-start), [clutch](../Clutch.md#inspector-quick-start), [differential](../Differential.md#inspector-quick-start) and [traction control](../TractionControl.md#inspector-quick-start) through their Engine-category panels. Apply/save and test the ordinary drivetrain before replacing torque or selection policies in code.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `AutomaticGearbox` | Makes automatic shift decisions from operating conditions. |
| `Clutch` | Models coupling and finite rotational energy transfer. |
| `Differential` | Distributes driven axle torque. |
| `Engine` | Resolves running state, RPM and propulsion torque/power. |
| `Gearbox` | Shared validated selection, ratios and shift state. |
| `ManualGearbox` | Provides the manually selected gearbox implementation. |
| `TractionControl` | Limits propulsion according to contact capacity and slip. |
| `Transmission` | Selects Direct, Manual or Automatic transmission operation. |

For user setup, see [Gearbox](../Gearbox.md), [Clutch](../Clutch.md), [Differential](../Differential.md) and [Traction control](../TractionControl.md). Boat and track behavior have separate [references](README.md).


## Longitudinal direction

Set `Engine.invertDriveDirection` to reverse wheel torque and built-in longitudinal thrust without swapping input commands or selecting reverse gear. `Engine.DriveDirectionSign` exposes the polarity; `VehicleController.DriveDirectionSign` makes it available to custom drive profiles. `VehicleController.ForwardSpeed` reports velocity along that configured direction, so automatic direction changes and brake/reverse resolution retain their normal meaning. `Engine.OutputTorque` reports the signed output after inversion. Ignition, clutch energy, power limits and throttle magnitude retain their existing contracts.

This setting affects propulsion. It does not reorient model geometry, suspension, steering geometry or flight control axes. See [Physics](../Physics.md#reverse-longitudinal-propulsion).

## Changing steering layout

`Steering` prepares its steering-wheel list, per-wheel steering multipliers and tie-rod links when configured. Wheel contact, attachment, component availability and current wheel positions remain live. Change steering demand through normal commands; it needs no configuration refresh.

After deliberately editing `Wheel.steering`, `Wheel.steeringMultiplier`, steering/tie-rod membership or axle layout, call `steering.RefreshWheelBindings(vehicle)` once. It preserves the current actuator angle and clears native steer angles on wheels removed from steering. Changes made in the Play Mode Inspector need the same refresh. To preserve a layout across a later full vehicle reconfiguration, update the corresponding `vehicle.wheelSetup` definitions too.

**Example: `RearSteeringConfiguration.cs`**

<!-- example: RearSteeringConfiguration.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public sealed class RearSteeringConfiguration : MonoBehaviour
    {
        public VehicleController vehicle;
        public Steering steering;
        public int rearWheelIndex;
        public void EnableRearSteering(bool enabled)
        {
            if (!vehicle || !steering || rearWheelIndex < 0 ||
                rearWheelIndex >= vehicle.Wheels.Count ||
                rearWheelIndex >= vehicle.wheelSetup.Length) return;
            var wheel = vehicle.Wheels[rearWheelIndex];
            wheel.steering = enabled;
            wheel.steeringMultiplier = -.5f;
            vehicle.wheelSetup[rearWheelIndex].steer = enabled;
            vehicle.wheelSetup[rearWheelIndex].steeringMultiplier = -.5f;
            steering.RefreshWheelBindings(vehicle);
        }
    }
}
```

## Engine and Gearbox

Keep three quantities distinct: requested throttle, crank torque and torque arriving at a wheel. A gear ratio trades wheel speed for torque; it does not create engine power. Final drive and efficiency further affect transmitted output. The active coupling and intervention stages can reduce that output even when the driver requests full throttle.

For a combustion torque-curve extension, override `Engine.EvaluateCrankTorque(float rpm)`. That hook belongs to the gearbox combustion path. Direct drive uses `settings.motorTorque`, so changing the crank curve is not a universal replacement for both modes. Choose the extension point according to which path the vehicle actually runs.

The engine produces torque with RPM response, torque curve and configured power/acceleration limits. Direct drive uses the configured wheel torque budget. With a gearbox, positive ratios and final drive convert crank torque/speed; reverse direction is represented by selected gear. Efficiency and clutch coupling affect transmitted output.

`Gearbox` selection validates the gear range, direction speed and predicted redline. A higher forward gear with a taller ratio may reduce existing overspeed even if its predicted RPM still exceeds redline, allowing automatic shifting to resume after a Nitro lock is released. Downshifts and engagement from neutral remain redline-guarded. Shifts interrupt propulsion for the configured duration. `Synchronize` is a selector helper and does not replace validated driving requests.

Automatic forward shifting requires loaded driven-wheel contact. During low-RPM deceleration, downshifts bypass Minimum Gear Time and may skip intermediate gears to reach a suitable coupled RPM in one shift. At standstill this selects first gear as soon as any current shift completes. Upshifts remain sequential and retain the minimum dwell; direction changes, explicit commands, driver-controlled clutch, boost locks and over-rev protection keep their existing guards. Grounded RPM/road-speed evidence and hysteresis prevent airborne revving or a spinning tire from cycling through higher gears. Thrust also fades near the configured road-speed envelope; ratios alone do not define attainable top speed.

## Request a manual gear

A gameplay request should use the same selection validation as a player shift. The sample switches transmission mode, resolves `Engine.ActiveGearbox` and asks it to select the requested index. Passing the vehicle allows the gearbox to assess motion and predicted RPM rather than accepting a gear based on its numeric range alone.

Treat a `false` return as a rejected request. A UI may retain the currently selected gear and display a refusal; an AI may retry after reducing speed. Neither should repeatedly force internal state in order to bypass the safety rule.

Assign a configured vehicle and `Transmission`. Call `Select` from UI/AI. The example selects Manual, resolves the connected gearbox and honors its safety checks.

**Example: `ManualGearControl.cs`**

<!-- example: ManualGearControl.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class ManualGearControl : MonoBehaviour
    {
        public VehicleController vehicle;
        public Transmission transmission;

        public bool Select(int gear)
        {
            if (!vehicle || !transmission || !transmission.engine) return false;
            transmission.SetMode(TransmissionMode.Manual);
            var box = transmission.engine.ActiveGearbox;
            return box && box.TrySelectGear(gear, vehicle);
        }
    }
}
```

The call may fail while shifting or during unsafe direction/over-rev changes. Queue or retry according to the application input policy, rather than forcing `CurrentGear`.

## Clutch

The clutch is the controllable connection between the engine and gearbox. A closed connection lets engine rotation load the wheels and lets wheel motion influence engine RPM. An open connection allows the engine to rev without driving the axle. Partial connection limits transmitted torque rather than simply blending two displayed RPM values.

`SetAutomatic(bool)` chooses assistance ownership; `SetManualEngagement(float)` requests an engagement amount, whereas the command's clutch value represents pedal travel. Keep those opposite conventions visible in an adapter. `EngagementChanged` reports resolved coupling and is suitable for an instrument; it is not another input request.

For an application-driven launch, feed throttle and clutch through the selected input provider and let the normal power pipeline run. Change clutch configuration at a deliberate setup boundary. A replacement clutch must preserve the relationship between coupling, reflected wheel load and finite stored energy; independently assigning wheel RPM would bypass the native wheel's contact response.

Pedal travel and clutch engagement use opposite intuitions: the driver's pedal is fully pressed at `Command.Clutch = 1`, which disconnects the drivetrain. At zero the clutch is released toward connection. Use this convention consistently in physical pedals, input actions and replay data.

A rapid release can transfer stored flywheel energy in addition to current combustion output. This explains why a launch can briefly break traction without increasing sustained engine power. Tune the clutch capacity and engine rotational inertia together before using traction-control settings to hide an unrealistic launch response.

`Command.Clutch` is pedal travel: zero connected, one disconnected. Intermediate values control capacity. Automatic assistance can yield to a driver pedal; `engagementRate` smooths assistance, not a button release.

Flywheel energy uses engine rotational inertia and RPM. Release exchanges finite energy through clutch capacity and reflected wheel inertia; it can produce wheelspin. `allowLaunchWheelspin` controls whether that stored-energy share bypasses ordinary TCS suppression. `Engine` power limits still constrain sustained combustion torque.

Neutral and shifts disconnect coupling. Automatic forward shift decisions pause under driver-controlled slipping clutch. Idle support is present; stalls, temperature and wear are outside the model.

### Supply a clutch pedal from an external producer

This adapter writes only clutch travel into an already selected `ExternalController`. The producer supplies pedal position in 0–1, and disabling the adapter releases that pedal request. Input ownership is still managed by the application's possession/session layer; assigning a controller here does not automatically select it on the vehicle.

**Example: `ExternalClutchPedal.cs`**

<!-- example: ExternalClutchPedal.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class ExternalClutchPedal : MonoBehaviour
    {
        public ExternalController input;

        public void SetPedalTravel(float pressedFraction)
        {
            if (input) input.SetClutch(Mathf.Clamp01(pressedFraction));
        }

        private void OnDisable()
        {
            if (input) input.SetClutch(0);
        }
    }
}
```

Zero means the pedal is released, not fully disconnected. The clutch mechanic decides resolved engagement with its current assistance policy. Keep one producer for the clutch channel, since two adapters writing the same buffered value would simply replace each other's request.

## Differential

A differential decides how an axle shares the engine's available torque. It is most visible when its two wheels do not have equal support: one may be on ice, unloaded or travelling a longer path during a turn. It works within the propulsion budget; it does not create another engine or independently propel the vehicle.

Author an axle by selecting its two driven `WheelCollider` references. Use separate pairs for separate axles, avoid duplicate wheel membership, and keep those colliders owned by this vehicle. For an open axle, one low-traction wheel restricts useful torque at both sides. Limited slip biases distribution toward usable support. Locked behavior opposes relative shaft speed using a bounded coupling torque.

If implementing another axle policy, retain the total budget and separate coupling from service braking. Validate it with one wheel airborne, split grip, a tight turn and zero throttle. A result that looks correct on uniform straight ground can still introduce net braking or extra power in those cases.

`maximumLockTorque` limits the locked coupling. A finite coupling is important because a wheel pair can require different speeds during a turn. The model can oppose the difference without imposing an instantaneous identical RPM on both native wheels.

Unpaired wheels retain base drive-weight allocation. The differential does not add propulsion while service/handbraking and does not implement a center differential between complete axles.

## TractionControl

Traction control reduces propulsion when a driven tire cannot use the requested torque. It reads actual contact and slip rather than assuming that high throttle always means wheelspin. Its job is intervention within the engine/differential result; it does not replace the native tire force calculation.

Tune the desired slip response, reduction speed and recovery speed separately. Fast reduction can catch a launch, while excessively fast recovery can repeatedly reapply the torque that caused the slip. The contact-capacity bound remains relevant even when a minimum feedback scale allows some propulsion through the ordinary slip controller.

Use `SetTractionControlEnabled(bool)` to control the component directly. When `DrivingAssists` is installed and enabled, use its `SetTractionControl(bool)` action because that component owns synchronized assist settings. For telemetry, distinguish enabled configuration from current intervention. A custom strategy should preserve contact/load evidence and avoid manufacturing braking torque when limiting propulsion.

TCS uses native contact load, surface grip and contact-relative slip to bound each driven wheel's torque. Target slip, launch reference speed, reduction/recovery rates and minimum feedback scale control intervention. A separate contact-capacity limit can reduce torque below that minimum.

Cornering reserve uses measured load/motion rather than steering input alone. Locked-shaft coupling and the total propulsion-reduction budget prevent a cut from introducing unintended net braking. There is no extra tire force or direct RPM assignment.

## Signed direction requests

The signed keyboard convention brakes opposing movement before selecting reverse/forward propulsion. Reverse after a held stop requires release and a fresh near-stationary press. The slope-release grace permits a bounded small gravity roll; it does not add hill-hold force. Manual gear selection retains its own safety policy.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed engine and drivetrain API](../API/DriveDynamics.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### Brakes

[Brakes](../API/DriveDynamics.md#brakes) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController v)` | Resolves an Engine reference only when no explicit engine is assigned. |
| `public override void Step(VehicleController v, Command c, float dt)` | Resolves signed-pedal direction/braking policy, publishes actuator demand and applies service/handbrake torques. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<float> ServiceBrakeChanged` | When resolved service braking changes. Payload: normalized resolved brake demand. |
| `public event System.Action<bool> HandbrakeChanged` | When resolved handbrake state changes. Payload: bool. |
| `public event System.Action<bool> BrakingChanged` | Moving service-brake activity changes. Owned by Brakes; independent of TireFeedback. |

### Burnout

[Burnout](../API/DriveDynamics.md#burnout) gives the full declared contract.

- `public event System.Action BurnoutStarted` — Current burnout started.
- `public event System.Action BurnoutStopped` — Current burnout stopped.
- `public event System.Action<bool> StateChanged` — Current state changed.
- `public override void Configure(VehicleController vehicle)` — Binds the component to its configured owner and selected source.
- `public void ResetState()` — Current reset state.
- `public virtual void ResetVehicleState(VehicleResetReason reason)` — Clears transient state for the supplied reset reason without changing persistent configuration.
- `public void SetBurnout(bool held)` — Current set burnout.
- `public override void Step(VehicleController vehicle, Command command, float dt)` — Current step.

### Clutch

[Clutch](../API/DriveDynamics.md#clutch) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resolves the engine only when no explicit reference is assigned. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances manual/automatic coupling and publishes `EngagementChanged` after a resolved coupling change. |
| `public virtual void SetAutomatic(bool value)` | Chooses automatic clutch assistance rather than manual engagement ownership. |
| `public virtual void SetManualEngagement(float value)` | Requests normalized manual clutch coupling, distinct from clutch pedal travel. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<float> EngagementChanged` | When resolved clutch coupling changes. Payload: normalized engagement, distinct from pedal travel. |
| `public event System.Action<bool> AutomaticChanged` | When automatic clutch assistance selection changes. Payload: bool. |

### Differential

[Differential](../API/DriveDynamics.md#differential) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Step(VehicleController v, Command c, float dt)` | Distributes axle torque and bounded shaft coupling; skips adding propulsion while service/handbraking. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

### DrivingAssists

[DrivingAssists](../API/DriveDynamics.md#drivingassists) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Caches the vehicle and applies its coordinated assist choices. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Applies the coordinator's current traction/stability choices to its connected mechanics. |
| `public virtual void Apply()` | Writes coordinated traction/stability assist choices to the connected mechanics. Disabling the coordinator does not restore previous settings. |
| `public virtual void SetTractionControl(bool value)` | Changes the coordinated traction-control choice through `DrivingAssists`. |
| `public virtual void SetStabilityControl(bool value)` | Changes the coordinated stability-assistance choice. |
| `public virtual void SetAssistsEnabled(bool value)` | Applies the application's combined assist enable choice through `DrivingAssists`. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> TractionControlChanged` | When `DrivingAssists` changes its coordinated traction-control choice. Payload: bool. |
| `public event System.Action<bool> StabilityControlChanged` | When `DrivingAssists` changes its stability-assistance choice. Payload: bool. |

### Engine

[Engine](../API/DriveDynamics.md#engine) gives the full declared contract.

- `public event System.Action<Gearbox> ActiveGearboxChanged` — Reports a change of effective gearbox identity, including removal or disable. Read ActiveGearbox when first subscribing.
- `public event System.Action<bool> EngineStateChanged` — Current engine state changed.
- `public event System.Action<int> GearChanged` — Current gear changed.
- `public override void Configure(VehicleController vehicle)` — Binds the component to its configured owner and selected source.
- `public virtual void ResetState()` — // Clear mechanical state for a respawn while preserving the ignition switch.
- `public virtual void ResetVehicleState(VehicleResetReason reason)` — Clears transient state for the supplied reset reason without changing persistent configuration.
- `public virtual void SetEngineRunning(bool running)` — Current set engine running.
- `public virtual void StartEngine()` — Current start engine.
- `public override void Step(VehicleController v, Command c, float dt)` — Current step.
- `public virtual void StopEngine()` — // Turns ignition off and clears propulsion state without disabling the component or applying parking brakes.
- `public virtual void ToggleEngine()` — Current toggle engine.

### Gearbox

[Gearbox](../API/DriveDynamics.md#gearbox) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void ConfigureFor(VehicleController vehicle, Engine engine)` | Connects and prepares the gearbox for its vehicle and engine context. |
| `public virtual bool TrySelectGear(int gear, VehicleController vehicle)` | Selects a signed gear (-1 reverse, 0 neutral, positive forward). Rejects invalid/unchanged gears, an active shift, unsafe direction changes or unsafe over-rev. The vehicle overload verifies this is the engine's active gearbox; the numeric overload takes explicit speed/RPM evidence. |
| `public virtual bool TryShiftUp(VehicleController vehicle)` | Requests the next higher gear through the gearbox's validated selection path. |
| `public virtual bool TryShiftDown(VehicleController vehicle)` | Requests the next lower gear through the gearbox's validated selection path. |
| `public virtual void Simulate(VehicleController vehicle, Command command, float wheelRpm, float maxRpm, float dt)` | Advances gearbox shift/selection state for one mechanical timestep. |
| `public virtual bool TrySelectGear(int gear, float forwardSpeed, float wheelRpm, float maxRpm)` | Selects a signed gear (-1 reverse, 0 neutral, positive forward). Rejects invalid/unchanged gears, an active shift, unsafe direction changes or unsafe over-rev. The vehicle overload verifies this is the engine's active gearbox; the numeric overload takes explicit speed/RPM evidence. |
| `public virtual void Synchronize(int gear)` | Synchronizes the gear selector as an explicit helper. It does not replace `TrySelectGear` safety validation for driving input. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<int> GearChanged` | After accepted gear selection. Payload: signed gear index, with reverse -1, neutral 0 and forward gears positive. |
| `public event System.Action<int> ShiftStarted` | When an accepted selection starts its shift interval. Payload: selected gear index. |
| `public event System.Action<int> ShiftCompleted` | When that shift interval completes; a zero-duration shift can complete immediately. Payload: gear index. |

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### MotorcycleBalance

[MotorcycleBalance](../API/DriveDynamics.md#motorcyclebalance) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Measures wheelbase and prepares wheel/contact geometry for balance response. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Uses gravity, contact and steering evidence to apply bounded motorcycle lean/balance support. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

### Nitro

[Nitro](../API/DriveDynamics.md#nitro) gives the full declared contract.

- `public event Action<float> AmountChanged` — Current amount changed.
- `public event Action<bool> BoostStateChanged` — Current boost state changed.
- `public event Action Depleted` — Current depleted.
- `public event Action NitroStarted` — Current nitro started.
- `public event Action NitroStopped` — Current nitro stopped.
- `public event Action<bool> OutputStateChanged` — Reports a change of the propulsion-output session. Receivers can be absent without affecting boost.
- `public virtual float AddNitro(float value)` — Current add nitro.
- `public override void Configure(VehicleController vehicle)` — Binds the component to its configured owner and selected source.
- `public virtual void Refill()` — Current refill.
- `public virtual void ResetState(bool refill = false)` — Current reset state.
- `public virtual void ResetVehicleState(VehicleResetReason reason)` — Clears transient state for the supplied reset reason without changing persistent configuration.
- `public virtual void SetAmount(float value)` — Current set amount.
- `public virtual void SetBoost(bool held)` — Current set boost.
- `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Current step.

### ParkingHold

[ParkingHold](../API/DriveDynamics.md#parkinghold) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resolves the local Trailer used by detached-parking policy. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Adds bounded low-speed support while applicable parking/service braking is active; does nothing for a sleeping body. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

### Steering

[Steering](../API/DriveDynamics.md#steering) gives the full declared contract.

- `public virtual void RefreshWheelBindings(VehicleController vehicle)` — Rebuilds the steering layout and tie-rod bindings once, preserving the actuator angle.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Discovers owned steering tie rods and measures axle/wheel geometry for its steering model. |
| `public override void Step(VehicleController v, Command c, float dt)` | Advances steering response/native wheel angles, publishes the resolved actuator and emits `AngleChanged` on a change. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<float> AngleChanged` | When resolved road-wheel steering angle changes. Payload: angle in degrees, not column degrees. |

### TractionControl

[TractionControl](../API/DriveDynamics.md#tractioncontrol) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resets retained intervention feedback before later propulsion steps. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Limits wheel propulsion from contact/slip evidence and emits `ActiveChanged` when intervention state changes. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |
| `public virtual void SetTractionControlEnabled(bool value)` | Enables/disables this traction-control module through its module action. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> ActiveChanged` | When resolved traction-control intervention changes between active/inactive. Payload: bool; enabled configuration is a separate state. |

### Transmission

[Transmission](../API/DriveDynamics.md#transmission) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resolves missing engine/manual/automatic references and applies the selected transmission mode. |
| `public override void Step(VehicleController v, Command c, float dt)` | Consumes a transmission toggle or changed mode field and applies the selected Direct/Manual/Automatic implementation. |
| `public virtual void SetMode(TransmissionMode value)` | Changes transmission or camera mode through the declaring component's transition rules. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<TransmissionMode> ModeChanged` | After the declaring component's selected mode changes. Payload: its mode enum. |

### VehicleModule

[VehicleModule](../API/Modules.md#vehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void Configure(VehicleController vehicle)` | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
| `public virtual void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it. |
| `public virtual void SetEnabled(bool value)` | Changes module enabled state and publishes an actual requested-flag change. |
| `public virtual bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> EnabledChanged` | After `SetEnabled` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
| `public event System.Action<VehicleController> Configured` | After controller-driven module configuration. Payload: the owning `VehicleController`. |
| `public event System.Action<VehicleController, Command, float> Stepped` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds. |
