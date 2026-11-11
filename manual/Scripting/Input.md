# Command sampling and input ownership

The input system translates a player, AI or external producer into one `Command` for a vehicle tick. The command describes intent; engine, brakes and steering then resolve that intent into mechanical outputs. A keyboard adapter, an Input System adapter and a network adapter can therefore share the same vehicle mechanics.

The integration has two boundaries: a producer fills a command, and `VehicleController` samples the currently selected `IVehicleInput`. Input ownership belongs to the application. Installing several adapters does not define which player, AI or replay should control the vehicle.

## Keyboard configuration and gating

Each keyboard adapter serializes `enableControls` with a default of `true`. Continuous reads and one-shot polling honor it. Disabling releases held axes and pending commands, blocks the optional `ActionInput` fallback and resets the drive steering ramp or retained airplane throttle. The component itself stays enabled, so the same provider can remain assigned while controls are temporarily blocked.

Keyboard keys are serialized `Key` fields, with `Key.None` meaning unbound. `KeyboardDriveInput.gearKeys` and `alternateGearKeys` map indices to requested gears; they can be configured independently. Each profile-specific action has its own field, including actions that happen to share a default key. The public `ignitionKey`, `profileKey` and `airplaneBrakeKey` fields configure ignition, profile selection and airplane braking.

The Inspector groups key fields under the initially collapsed **Keyboard bindings** foldout. Non-binding tuning and custom subclass fields remain visible. Edge-triggered actions are still latched in `Update()` and consumed by `ReadCommand()` once; changing bindings does not change the physics sampling contract. See [Keyboard setup](../Input.md#keyboard-bindings).

## Implementation map

| Class | Responsibility |
| --- | --- |
| `Command` | Defines axes, action requests and analog/digital channel metadata. |
| `InputBuffer` | Buffers axes and pending one-shot actions for fixed-step consumption. |
| `ExternalController` | Provides the buffered command API for external control. |
| `DirectController` / `IDirectInput` | Optionally replaces physical driving with authoritative world-pose input while updating presentation from measured motion. |
| `ActionInput` | Reads configured Unity Input System actions. |
| `InputGate` | Selects an input source for the active registered driving profile. |
| `VehicleController` | Selects `inputSource`, samples commands and publishes resolved state. |

For adapter setup, see [Input](../Input.md).

For complete custom providers, see [Writing your own input source](../Input.md#writing-your-own-input-source). Start with the ready-to-drive keyboard (W/S, A/D) or analog gamepad example; both read the device themselves. The fuller providers also cover UI/device setters, one-shot buffering and per-channel analog/digital flags.

## Sampling contract

Render frames and physics ticks do not occur at the same rate. Buffer an action pressed between physics ticks so it survives until the next read, then consume it once. A held axis has different semantics: it remains valid until the producer changes or clears it. Repeating a gear-up action as if it were a held axis can produce several shifts from one button press.

`SubmitCommand` is appropriate when one producer owns the complete command. Partial producers should agree on composition before submission: replacing a command also replaces metadata and can erase another producer's pending request. Use `ClearControls()` at handover boundaries so a retained throttle or queued action cannot leak to the next owner.

`VehicleController` calls the selected enabled `IVehicleInput` once per fixed tick. Continuous axes remain until the provider changes/clears them. One-shot gear, lighting, ignition and profile requests must be consumed once.

`InputBuffer` retains pending commands. `SubmitCommand` replaces the entire pending command and its channel masks; `SetAxes` changes the axis subset. `ReadCommand` sanitizes/clamps values and consumes actions. `ClearControls` releases all held values and queued actions.

`InputBuffer` clears on focus loss and disable. `ExternalController` retains commands on focus loss and clears on disable. Neither component implements transport, AI decisions or ownership arbitration.

For a working AI integration, see [Implementing an AI driver](../Input.md#implementing-an-ai-driver): follow a target, brake near it, and visit waypoints. The guide includes complete scripts and Inspector setup.

For authoritative position/rotation input instead of driving forces, see [Direct pose control](../Input.md#direct-pose-control-for-ai-and-scripted-traffic). Select DirectController in the same Input Source slot, enable its flag, and submit world poses.

## External controller and runtime ownership

The example below treats external control as a session. It captures the previous provider, clears stale external values and restores the previous provider only if it still owns the slot. That final check matters when another possession system has legitimately taken control in the meantime.

Call `Drive` from the system that produces commands, not from a second vehicle simulation. Releasing the session clears the external buffer even if ownership has already changed, so taking control again starts from released controls.

Attach this component outside the vehicle's inactive hierarchy if it must control possession independently. Assign an enabled `ExternalController` owned by the vehicle. Call `TakeControl`, submit `Drive` commands from your producer, and `ReleaseControl` when done.

**Example: `ExternalInputSession.cs`**

<!-- example: ExternalInputSession.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class ExternalInputSession : MonoBehaviour
    {
        public VehicleController vehicle;
        public ExternalController external;
        private MonoBehaviour previous;
        private bool ownsInput;

        public void TakeControl()
        {
            if (ownsInput || !vehicle || !external || !external.isActiveAndEnabled) return;
            previous = vehicle.inputSource;
            external.ClearControls();
            vehicle.SetInputSource(external);
            ownsInput = true;
        }

        public void Drive(float throttle, float steering, float brake)
        {
            if (ownsInput && vehicle && vehicle.inputSource == external)
                external.SetAnalogAxes(throttle, steering, brake);
        }

        public void ReleaseControl()
        {
            if (!ownsInput) return;
            if (external) external.ClearControls();
            if (vehicle && vehicle.inputSource == external)
                vehicle.SetInputSource(previous ? previous : null);
            ownsInput = false;
        }

        private void OnDisable() => ReleaseControl();
    }
}
```

Only the selected provider is read by `VehicleController`, but other enabled keyboard/demo scripts may have their own side effects. Disable or coordinate those at the application possession boundary. Feed producer data before the controller's fixed tick when it must affect that tick.

## Progressive keyboard braking and analog controllers

Channel metadata tells mechanics whether an axis already represents a proportional control. A trigger at 25% should remain a proportional brake request; a keyboard key may need a ramp from released to full braking. Marking a digital source as analog bypasses shaping that the driver might expect, while marking an analog pedal as digital can apply unwanted smoothing.

Keep units at the input boundary normalized. Vehicle speed, wheel torque and steering-column degrees are outputs or mechanic settings, not substitutes for command axes. Use the steering conversion API when a physical steering device reports column angle, then submit the resulting input according to the adapter's channel convention.

`AnalogControls` takes precedence over `DigitalControls` for a channel. `SetAnalogAxes` marks all channels analog. Analog pedal/steering channels bypass the associated digital shaping: progressive brake ramp, engine throttle smoothing and digital steering assistance. Input Action processors still apply.

Signed throttle allows direction-based driving; independent positive throttle/brake pedals use the selected direction and may overlap. The clutch range is zero connected to one disconnected. Boat steering retains analog magnitude; digital/unspecified steering uses the profile's slew times.

## Input Action lifecycle

With `PlayerInput`, the adapter resolves references through that player's action asset and leaves action enabling to `PlayerInput`. Otherwise it enables referenced actions unless configured not to. Shared references are retained until their last owner releases them; actions enabled externally stay enabled. Refresh bindings after editing action references at runtime.

## Aircraft keyboard policy

`KeyboardFlightInput` retains aircraft throttle, rather than using W/S as throttle. Its wheel-brake binding also controls the retained-throttle brake policy. Configure that adapter or replace it when using another cockpit convention. Independent analog throttle/brake behavior belongs to `ActionInput` and the command metadata, not keyboard polling.

## Runtime keyboard configuration

All four adapters inherit `KeyboardInput`. `SetControlsEnabled(false)` immediately clears pending actions, steering state and any retained airplane throttle, and pauses the adapter's analog fallback. `SetControlsEnabled(true)` resumes input on subsequent updates. `SetEnabled(false)` is also available through the module API to disable the component itself.

Use `TrySetBinding(nameof(KeyboardDriveInput.forwardKey), Key.UpArrow)` to change an action, and `TryGetBinding` to read it. Pass a gear index for the `gearKeys` and `alternateGearKeys` arrays. `Key.None` unbinds an action. Invalid names, field types, keys and array indices return `false`; bindings are not resized automatically. `ResetBindings()` restores built-in defaults. Rebinding and resetting clear retained controls, so release and press one-shot action keys again after changing them. Changes made in Play Mode are session-local; save them through your game's settings system if needed.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed input and commands API](../API/Input.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### ActionInput

[ActionInput](../API/Input.md#actioninput) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void RefreshBindings()` | Re-resolves Input System action references, including the selected `PlayerInput` action asset. |
| `public virtual void UseAsVehicleInput()` | Selects this action adapter as the vehicle's current input source. |
| `public static Command MergeHover(Command keyboard, Command analog)` | Combines hover-related adapter input into the current command. |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |

### Command

[Command](../API/Input.md#command) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public bool IsAnalog(InputChannels channel)` | Checks whether the specified command channel is marked as an analog input. |
| `public bool IsDigital(InputChannels channel)` | Checks whether the specified command channel is marked as a digital input. |

### DirectController

[DirectController](../API/Input.md#directcontroller) documents the mode flags and inherited buffered command API.

| Method | Role |
| --- | --- |
| `public virtual bool SetPose(Vector3 position, Quaternion rotation)` | Store a validated world-pose request. |
| `public virtual void ClearPose()` | Clear the stored pose and hold current placement without a target. |
| `public virtual void SetDirectControl(bool value)` | Switch pose versus ordinary command control at the next fixed tick. |
| `public virtual Pose ReadPose(Pose currentPose, float deltaTime)` | Sample the independent target or stored pose. |
| `public virtual void UseAsVehicleInput()` | Select this source on its parent vehicle. |

### IDirectInput

[IDirectInput](../API/Input.md#idirectinput) defines optional direct ownership alongside IVehicleInput.

| Method | Role |
| --- | --- |
| `Pose ReadPose(Pose currentPose, float deltaTime)` | Return the next world pose for the supplied fixed timestep. |

### InputBuffer

[InputBuffer](../API/Input.md#inputbuffer) gives the full declared contract.

- `public virtual void ClearControls()` — // Release all held controls and queued actions, e.g. when AI/network ownership changes.
- `public virtual Command ReadCommand()` — // Returns the current continuous controls and consumes queued one-shot actions so they cannot repeat on later // physics ticks.
- `public virtual void ResetInput()` — Clears held input and pending one-shot requests for a vehicle reset.
- `public virtual void SelectGear(int gear)` — // Queues an explicit gear request; the active gearbox applies its direction and over-rev guards.
- `public virtual void SetAnalogAxes(float throttle, float steering, float brake = 0, bool handbrake = false)` — Current set analog axes.
- `public virtual void SetAxes(float throttle, float steering, float brake = 0, bool handbrake = false)` — Current set axes.
- `public virtual void SetBurnout(bool held)` — Current set burnout.
- `public virtual void SetClutch(float pedal)` — Current set clutch.
- `public virtual void SetFlightAxes(float pitch, float roll, float yaw, float lift)` — Current set flight axes.
- `public virtual void SetHorn(bool held)` — Current set horn.
- `public virtual void SetIndicators(IndicatorState state)` — Current set indicators.
- `public virtual void SetNitro(bool held)` — Current set nitro.
- `public virtual void SetStrafe(float strafe)` — Current set strafe.
- `public virtual void SetWheelLift(bool held)` — Current set wheel lift.
- `public virtual void ShiftGear(int direction)` — // Queues a single upward or downward shift, reducing the supplied direction to its sign.
- `public virtual void SubmitCommand(Command command)` — // Replace the complete pending command, including one-shot actions. ReadCommand consumes actions once.
- `public virtual void ToggleGearbox()` — // Queues a transmission-mode cycle for the next command sample.
- `public virtual void ToggleHazards()` — // Queues one hazard-light toggle for the next command sample.
- `public virtual void ToggleHeadlights()` — // Queues one low-beam toggle without reading or changing a physical light directly.
- `public virtual void ToggleHighBeams()` — // Queues one high-beam toggle for the lighting module.
- `public virtual void ToggleIgnition()` — // Queues one ignition toggle; reading the command consumes it once.
- `public virtual void ToggleLeftIndicator()` — // Queues one left-indicator toggle for the next command sample.
- `public virtual void ToggleProfile()` — // Queues one drive-profile toggle for the next command sample.
- `public virtual void ToggleRightIndicator()` — // Queues one right-indicator toggle for the next command sample.

### InputGate

[InputGate](../API/Input.md#inputgate) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Rebinds `ConfigurationChanged` on the current owner, resolves `ProfileSwitcher` and refreshes input permissions. |
| `public virtual void Refresh()` | Re-evaluates the input gate's configured permission and target input availability. |

### InputGate.Route

[InputGate.Route](../API/Input.md#inputgateroute) gives the full declared contract.

| Event / callback | Role |
| --- | --- |
| `public UnityEvent selected` | Inspector callback when this controller route is selected; no payload. |

### IVehicleInput

[IVehicleInput](../API/Input.md#ivehicleinput) gives the full declared contract.

| Method | Role |
| --- | --- |
| `Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |

### IVehicleInputReset

[IVehicleInputReset](../API/Input.md#ivehicleinputreset) gives the full declared contract.

- `void ResetInput()` — Clears held input and pending one-shot requests for a vehicle reset.

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### KeyboardBoatInput

[KeyboardBoatInput](../API/Input.md#keyboardboatinput) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |

- **KeyboardBoatInput** — `public override void ResetBindings()` — Restores default bindings and clears retained controls.

### KeyboardDriveInput

[KeyboardDriveInput](../API/Input.md#keyboarddriveinput) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void CycleHeadlights()` | Queues the next low/high/off state through the normal one-shot command path. |
| `public virtual float AdvanceSteering(float target, float deltaTime)` | Advances keyboard steering shaping for elapsed time rather than reading a separate mechanical steering state. |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |

- **KeyboardDriveInput** — `public override void ResetBindings()` — Restores default bindings and clears retained controls.

### KeyboardFlightInput

[KeyboardFlightInput](../API/Input.md#keyboardflightinput) gives the full declared contract.

- `public virtual Command ReadCommand()` — // Returns the current continuous controls and consumes queued one-shot actions so they cannot repeat on later // physics ticks.
- `public override void ResetBindings()` — Current reset bindings.
- `public virtual void ResetControls()` — Current reset controls.
- `public virtual void ResetInput()` — Clears held input and pending one-shot requests for a vehicle reset.

### KeyboardInput

- **KeyboardInput** — `public abstract void ResetBindings()` — Restores all keyboard bindings to the built-in defaults and clears retained controls. Other tuning values remain unchanged.
- **KeyboardInput** — `public virtual void SetControlsEnabled(bool value)` — Enables or pauses this component's controls. Keyboard inputs clear queued actions, axes and retained aircraft throttle when disabled; Cameras restores its original camera lens when paused.
- **KeyboardInput** — `public virtual bool TryGetBinding(string action, out Key key, int index = -1)` — Reads a binding using the same field-name/index rules. Returns false for an invalid lookup and writes Key.None.
- **KeyboardInput** — `public virtual bool TrySetBinding(string action, Key key, int index = -1)` — Sets a Key field by its exact serialized name, or a Key[] element using index. Returns false for unknown names, wrong types, invalid keys or indices. Key.None unbinds the action. Clears retained controls on success.

### KeyboardSubmarineInput

[KeyboardSubmarineInput](../API/Input.md#keyboardsubmarineinput) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |

- **KeyboardSubmarineInput** — `public override void ResetBindings()` — Restores default bindings and clears retained controls.

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
