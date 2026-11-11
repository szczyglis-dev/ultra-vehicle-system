# Input and commands API

Read [the system explanation](../Scripting/Input.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [ActionInput](Input.md#actioninput)
- [Command](Input.md#command)
- [ControllerCore](Input.md#controllercore)
- [ControllerModule](Input.md#controllermodule)
- [DirectController](Input.md#directcontroller)
- [ExternalController](Input.md#externalcontroller)
- [IDirectInput](Input.md#idirectinput)
- [InputBuffer](Input.md#inputbuffer)
- [InputChannels](Input.md#inputchannels)
- [InputGate.Route](Input.md#inputgateroute)
- [InputGate](Input.md#inputgate)
- [InputMode](Input.md#inputmode)
- [IVehicleInput](Input.md#ivehicleinput)
- [IVehicleInputReset](Input.md#ivehicleinputreset)
- [KeyboardBoatInput](Input.md#keyboardboatinput)
- [KeyboardDriveInput](Input.md#keyboarddriveinput)
- [KeyboardFlightInput](Input.md#keyboardflightinput)
- [KeyboardInput](Input.md#keyboardinput)
- [KeyboardSpaceshipInput](Input.md#keyboardspaceshipinput)
- [KeyboardSubmarineInput](Input.md#keyboardsubmarineinput)

## ActionInput

**Runtime/Controller/Input/ActionInput.cs**

Reads configured Unity Input System actions.

**Inherits / implements:** [ControllerModule](Input.md#controllermodule), [IVehicleInput](Input.md#ivehicleinput).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public InputActionReference brake` | Input System action used for brake. Assign the action from your input asset. |
| `public InputMode brakeMode` | Selects the brake mode policy for this configuration. Options: `Auto`, `Analog`, `Digital`. |
| `public InputActionReference burnout` | Optional Burnout InputAction reference, or a PlayerInput action named Burnout. No default gamepad button is reserved. |
| `public InputActionReference clutch` | Input System action used for clutch. Assign the action from your input asset. |
| `public bool enableReferencedActions` | Enable referenced actions while this adapter is active. Disable when `PlayerInput` owns their lifecycle. |
| `public InputActionReference forwardGear` | Input System action used for forward gear. Assign the action from your input asset. |
| `public InputActionReference handbrake` | Input System action used for handbrake. Assign the action from your input asset. |
| `public InputActionReference hazards` | Input System action used for hazards. Assign the action from your input asset. |
| `public InputActionReference headlights` | Input System action used for headlights. Assign the action from your input asset. |
| `public InputActionReference highBeams` | Input System action used for high beams. Assign the action from your input asset. |
| `public bool holdReverseUntilStopped` | Keep requesting reverse while negative throttle is held, without requiring a new press after stopping. Default `false`. |
| `public InputActionReference horn` | Held horn action. Defaults to gamepad east face button (B/Circle); supports explicit action references and PlayerInput. |
| `public InputActionReference ignition` | Input System action used for ignition. Assign the action from your input asset. |
| `public InputActionReference leftIndicator` | Input System action used for left indicator. Assign the action from your input asset. |
| `public InputActionReference lift` | Input System action used for lift. Assign the action from your input asset. |
| `public InputActionReference nitro` | Optional Nitro InputAction reference, or a PlayerInput action named Nitro. No default gamepad button is reserved. |
| `public InputActionReference pitch` | Input System action used for pitch. Assign the action from your input asset. |
| `public PlayerInput playerInput` | Optional PlayerInput component whose action asset and player context supply the configured input actions. |
| `public InputActionReference profile` | Input System action used for profile. Assign the action from your input asset. |
| `public InputActionReference reverseGear` | Input System action used for reverse gear. Assign the action from your input asset. |
| `public InputActionReference rightIndicator` | Input System action used for right indicator. Assign the action from your input asset. |
| `public InputActionReference roll` | Input System action used for roll. Assign the action from your input asset. |
| `public InputActionReference shiftDown` | Input System action used for shift down. Assign the action from your input asset. |
| `public InputActionReference shiftUp` | Input System action used for shift up. Assign the action from your input asset. |
| `public InputActionReference steering` | Input System action used for steering. Assign the action from your input asset. |
| `public InputMode steeringMode` | Selects the steering mode policy for this configuration. Options: `Auto`, `Analog`, `Digital`. |
| `public InputActionReference strafe` | Input System action used for strafe. Assign the action from your input asset. |
| `public InputActionReference throttle` | Input System action used for throttle. Assign the action from your input asset. |
| `public InputMode throttleMode` | Selects the throttle mode policy for this configuration. Options: `Auto`, `Analog`, `Digital`. |
| `public bool useDefaultGamepadBindings` | When checked, use default gamepad bindings is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public InputActionReference wheelLift` | Optional WheelLift reference or PlayerInput action named WheelLift. |
| `public InputActionReference yaw` | Input System action used for yaw. Assign the action from your input asset. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public static Command MergeHover(Command keyboard, Command analog)` | Combines hover-related adapter input into the current command. | `keyboard` — Keyboard, interpreted by this operation in the declared type. `analog` — Channel metadata choosing proportional behavior. **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
| `public virtual void RefreshBindings()` | Re-resolves Input System action references, including the selected `PlayerInput` action asset. | No arguments; no returned value. |
| `public virtual void UseAsVehicleInput()` | Selects this action adapter as the vehicle's current input source. | No arguments; no returned value. |

## Command

**Runtime/Core/Command.cs**

Value type carrying normalized driving axes, pending actions and analog/digital channel metadata.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public InputChannels AnalogControls` | Analog controls. |
| `public bool Burnout` | Held optional Drive burnout launch request; requires enabled Burnout settings. |
| `public float Clutch` | Pedal amount: 0 couples the engine, 1 releases the optional clutch. Clutch pedal amount: zero couples and one releases the engine. |
| `public InputChannels DigitalControls` | Digital controls. |
| `public bool Handbrake` | Handbrake. |
| `public bool HoldReverseRequest` | Held reverse intent for negative throttle; the drivetrain admits it only when safe. Default `false`. |
| `public bool Horn` | Held horn request; independent of ignition and consumed by HornAudio. |
| `public float Lift` | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one. |
| `public bool Nitro` | Held optional nitro request. Supply, throttle and engine/module eligibility still apply. |
| `public float Pitch` | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one. |
| `public int? RequestedGear` | One-shot gear selection; `null` leaves selection unchanged, zero is neutral and minus one is reverse. |
| `public IndicatorState? RequestedIndicators` | Requested indicators. |
| `public float Roll` | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one. |
| `public float ServiceBrake` | Normalized service-brake input from zero to one. |
| `public int Shift` | One-shot shift direction: minus one down, zero unchanged, plus one up. |
| `public float Steering` | Signed steering input from minus one to one. |
| `public float Strafe` | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one. |
| `public float Throttle` | Throttle. |
| `public bool ToggleHazards` | Toggle hazards. |
| `public bool ToggleHeadlights` | Toggle headlights. |
| `public bool ToggleHighBeams` | Toggle high beams. |
| `public bool ToggleIgnition` | Toggle ignition. |
| `public bool ToggleLeftIndicator` | Toggle left indicator. |
| `public bool ToggleProfile` | Toggle profile. |
| `public bool ToggleRightIndicator` | Toggle right indicator. |
| `public bool ToggleTransmission` | Toggle transmission. |
| `public bool WheelLift` | Held optional Physics WheelLift request. |
| `public float Yaw` | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public Command(float throttle, float steering)` | Constructs Command with the supplied initial state. | `throttle` — Normalized propulsion/throttle request. `steering` — Normalized steering input, or bool steering participation when declared bool. **Returns:** New instance initialized from the supplied arguments. |
| `public bool IsAnalog(InputChannels channel)` | Checks whether the specified command channel is marked as an analog input. | `channel` — Input/light channel selected by its enum. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public bool IsDigital(InputChannels channel)` | Checks whether the specified command channel is marked as a digital input. | `channel` — Input/light channel selected by its enum. **Returns:** `true` when the described condition holds; `false` otherwise. |

## ControllerCore

**Runtime/Controller/Core/ControllerCore.cs**

Configuration/implementation type for controller core within input and commands.

**Inherits / implements:** [CategoryCore](Modules.md#categorycore).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public ControllerCore()` | Constructs `ControllerCore` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## ControllerModule

**Runtime/Controller/Core/ControllerModule.cs**

Configuration/implementation type for controller module within input and commands.

**Inherits / implements:** [VehicleModule](Modules.md#vehiclemodule), [IControllerModule](Modules.md#icontrollermodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |

## DirectController

**Runtime/Controller/Input/DirectController.cs**

Replaceable buffered input source with optional direct world-pose control. See [the direct-mode guide](../Input.md#direct-pose-control-for-ai-and-scripted-traffic).

**Inherits / implements:** [ExternalController](Input.md#externalcontroller), [IDirectInput](Input.md#idirectinput).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool automaticSteering` | Infers normalized steering from heading change and signed travel. Turn off to use inherited SetAxes/SetAnalogAxes steering. |
| `public virtual bool AutomaticSteering { get; }` | Exposes steering inference policy through IDirectInput. |
| `public bool directControl` | Enables authoritative pose control when this source is selected. False preserves the inherited ExternalController command path. |
| `public virtual bool DirectControl { get; }` | Exposes the serialized flag through IDirectInput. |
| `public Transform poseTarget` | Optional independent transform supplying the desired world pose. Keep it outside the vehicle hierarchy; leave empty for SetPose. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ClearPose()` | Releases the stored pose request; without a Pose Target the vehicle holds its current applied pose. | No arguments or result. |
| `public virtual Pose ReadPose(Pose currentPose, float deltaTime)` | Samples an independent Pose Target, stored request or current pose, in that priority. | Current applied pose and fixed timestep. A vehicle-owned target is ignored. Returns world pose. |
| `public virtual void SetDirectControl(bool value)` | Changes the source flag, applied on the next vehicle fixed tick. | True for pose control; false for inherited buffered driving commands. |
| `public virtual bool SetPose(Vector3 position, Quaternion rotation)` | Stores an authoritative world pose until replaced or cleared. An assigned Pose Target takes precedence. | Position in world metres and quaternion rotation. Normalizes valid rotations; returns false for invalid values, retaining the last valid request. |
| `public virtual void UseAsVehicleInput()` | Assigns this source to the nearest parent VehicleController. | No arguments or result. |

## ExternalController

**Runtime/Controller/Input/ExternalController.cs**

Provides the buffered command API for external control.

**Inherits / implements:** [InputBuffer](Input.md#inputbuffer).

## IDirectInput

**Runtime/Controller/Input/DirectController.cs**

Optional authoritative world-pose capability for an input source. Existing IVehicleInput implementations remain physical command sources.

**Inherits / implements:** [IVehicleInput](Input.md#ivehicleinput).

### State and configuration

| Member | Meaning |
| --- | --- |
| `bool AutomaticSteering { get; }` | True estimates steering from path curvature; false uses the sampled Command.Steering, including at rest. |
| `bool DirectControl { get; }` | True selects pose ownership; false uses ordinary IVehicleInput commands. Only the selected, enabled source is considered. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `Pose ReadPose(Pose currentPose, float deltaTime)` | Supplies the next authoritative chassis pose once per direct-mode fixed tick. | Current applied pose and fixed timestep in seconds. Return world metres and a valid quaternion; invalid poses hold the previous pose. |

## InputBuffer

**Runtime/Controller/Input/InputBuffer.cs**

Buffers axes and pending one-shot actions for fixed-step consumption.

**Inherits / implements:** [ControllerModule](Input.md#controllermodule), [IVehicleInput](Input.md#ivehicleinput), [IVehicleInputReset](Input.md#ivehicleinputreset).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public InputChannels analogControls` | Mark analog axes to bypass digital shaping. `SetAnalogAxes` marks all channels for raw controller input. |
| `public InputChannels digitalControls` | Mark button-driven axes here to opt into keyboard assistance such as progressive braking. |
| `public bool holdReverseUntilStopped` | Keep requesting reverse while negative throttle is held, without requiring a new press after stopping. Default `false`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ClearControls()` | Clears retained axes, channel metadata and pending one-shot input actions. | No arguments; no returned value. |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
| `public virtual void ResetInput()` | Clears held input and pending one-shot requests for a vehicle reset. | — |
| `public virtual void SelectGear(int gear)` | Queues an explicit gear-selection action in the input buffer. | `gear` — Signed gear index: -1 reverse, 0 neutral, positive forward. |
| `public virtual void SetAnalogAxes(float throttle, float steering, float brake = 0, bool handbrake = false)` | Sets proportional driving axes and marks the corresponding channels analog. | `throttle` — Normalized propulsion/throttle request. `steering` — Normalized steering input, or bool steering participation when declared bool. `brake` — Normalized brake request. Default: `0`. |
| `public virtual void SetAxes(float throttle, float steering, float brake = 0, bool handbrake = false)` | Updates buffered drive-axis values and their input metadata without replacing all pending actions. | `throttle` — Normalized propulsion/throttle request. `steering` — Normalized steering input, or bool steering participation when declared bool. `brake` — Normalized brake request. Default: `0`. |
| `public virtual void SetBurnout(bool held)` | Stores a continuous Drive burnout request; false releases it. ClearControls releases both requests.  `held` — true while requested; false on release. | — |
| `public virtual void SetClutch(float pedal)` | Sets normalized clutch pedal travel: zero released/connected, one pressed/disconnected. | `pedal` — Selected pedal handle; `null` releases a usable foot destination. |
| `public virtual void SetFlightAxes(float pitch, float roll, float yaw, float lift)` | Updates buffered lift/pitch/roll/yaw-related axes using the declared channel metadata. | `pitch` — Normalized pitch input, or audio pitch multiplier in an audio operation. `roll` — Normalized roll input. `yaw` — Normalized yaw input. `lift` — Normalized vertical/lift request. |
| `public virtual void SetHorn(bool held)` | Stores a held horn request; false or ClearControls releases it. Repeated ReadCommand calls preserve it. | — |
| `public virtual void SetIndicators(IndicatorState state)` | Requests the selected direction/hazard indicator state. | `state` — State, interpreted by this operation in the declared type. |
| `public virtual void SetNitro(bool held)` | Stores a continuous Nitro request; false releases it. ReadCommand does not consume it as a one-shot.  `held` — true while requested; false on release. | — |
| `public virtual void SetStrafe(float strafe)` | Updates the buffered lateral movement axis. | `strafe` — Normalized lateral request. |
| `public virtual void SetWheelLift(bool held)` | Stores a continuous wheel-lift request; false releases it and ClearControls clears it. | — |
| `public virtual void ShiftGear(int direction)` | Queues a relative up/down gear action in the input buffer. | `direction` — Direction, interpreted by this operation in the declared type. |
| `public virtual void SubmitCommand(Command command)` | Replaces the pending buffered command, including its channel metadata and action flags. | `command` — Command sampled for this tick; use its channel metadata as well as axes. |
| `public virtual void ToggleGearbox()` | Queues a transmission-mode toggle in the input buffer. | No arguments; no returned value. |
| `public virtual void ToggleHazards()` | Queues a hazard-indicator toggle in the input buffer. | No arguments; no returned value. |
| `public virtual void ToggleHeadlights()` | Queues a headlight toggle in the input buffer. | No arguments; no returned value. |
| `public virtual void ToggleHighBeams()` | Queues a high-beam toggle in the input buffer. | No arguments; no returned value. |
| `public virtual void ToggleIgnition()` | Queues an ignition toggle for the next sampled command. | No arguments; no returned value. |
| `public virtual void ToggleLeftIndicator()` | Queues a left-indicator toggle for the next sampled command. | No arguments; no returned value. |
| `public virtual void ToggleProfile()` | Queues a movement-profile toggle for the next sampled command. | No arguments; no returned value. |
| `public virtual void ToggleRightIndicator()` | Queues a right-indicator toggle for the next sampled command. | No arguments; no returned value. |

## InputChannels

**Runtime/Core/Command.cs**

Defines the allowed input channels choices used by this topic.

### Values

- `None = 0`
- `Throttle = 1`
- `Steering = 2`
- `ServiceBrake = 4`
- `Clutch = 8`
- `Flight = 16`
- `All = Throttle \| Steering \| ServiceBrake \| Clutch \| Flight`

## InputGate

**Runtime/Controller/Input/InputGate.cs**

Controls permission to pass input to the vehicle.

**Inherits / implements:** [ControllerModule](Input.md#controllermodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Route[] routes` | Ordered routes configuration entries. Expand each item; see InputGate.Route for its individual settings. Initial value: `Array.Empty<Route>()`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Rebinds `ConfigurationChanged` on the current owner, resolves `ProfileSwitcher` and refreshes input permissions. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void Refresh()` | Re-evaluates the input gate's configured permission and target input availability. | No arguments; no returned value. |

## InputGate.Route

**Runtime/Controller/Input/InputGate.cs**

Controller routing configuration and its selection callback.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public UnityEvent selected` | Inspector callback when this controller route is selected; no payload. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public MonoBehaviour input` | Control channel or input provider used to drive this binding. |
| `public string profileId` | Case-sensitive registration ID in the vehicle ProfileSwitcher. Select this route when its registered profile becomes active. |

## InputMode

**Runtime/Controller/Input/ActionInput.cs**

Defines the allowed input mode choices used by this topic.

### Values

- `Auto`
- `Analog`
- `Digital`

## IVehicleInput

**Runtime/Core/Command.cs**

Input-provider contract sampled by the controller for one vehicle tick.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |

## IVehicleInputReset

**Runtime/Core/IVehicleResetHandler.cs**

Presentation or lifecycle contract for independent vehicle components.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void ResetInput()` | Clears held input and pending one-shot requests for a vehicle reset. | — |

## KeyboardBoatInput

**Runtime/Controller/Input/Samples/KeyboardBoatInput.cs**

Configuration/implementation type for keyboard boat input within input and commands.

**Inherits / implements:** [KeyboardInput](Input.md#keyboardinput), [IVehicleInput](Input.md#ivehicleinput).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public ActionInput analogInput` | Gamepad/joystick adapter. Created automatically if unassigned; custom Action references remain configurable. |
| `public Key burnoutKey` | Held Burnout request; on fixed-wing aircraft the accepted request increases native thrust. Initial value: `Key.LeftCtrl`. |
| `public Key forwardKey` | Configurable keyboard binding. Default: `Key.W`; `Key.None` leaves it unbound. |
| `public Key ignitionKey` | Keyboard binding for ignition. Choose None to leave the action unassigned. Initial value: `Key.I`. |
| `public Key nitroKey` | Held Nitro request, merged with analog input. Initial value: `Key.Enter`. |
| `public Key profileKey` | Keyboard binding for profile. Choose None to leave the action unassigned. Initial value: `Key.B`. |
| `public Key reverseKey` | Configurable keyboard binding. Default: `Key.S`; `Key.None` leaves it unbound. |
| `public Key steerLeftKey` | Configurable keyboard binding. Default: `Key.A`; `Key.None` leaves it unbound. |
| `public Key steerRightKey` | Configurable keyboard binding. Default: `Key.D`; `Key.None` leaves it unbound. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
| `public override void ResetBindings()` | Restores this adapter's default keys and clears retained controls. | No arguments; no returned value. |

## KeyboardDriveInput

**Runtime/Controller/Input/Samples/KeyboardDriveInput.cs**

Configuration/implementation type for keyboard drive input within input and commands.

**Inherits / implements:** [KeyboardInput](Input.md#keyboardinput), [IVehicleInput](Input.md#ivehicleinput).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Key[] alternateGearKeys` | Keys indexed by requested gear: index 0 is neutral; higher indices select forward gears. `Key.None` leaves an index unbound. |
| `public Key ascendAlternateKey` | Configurable keyboard binding. Default: `Key.RightShift`; `Key.None` leaves it unbound. |
| `public Key ascendKey` | Configurable keyboard binding. Default: `Key.LeftShift`; `Key.None` leaves it unbound. |
| `public Key burnoutKey` | Held burnout request key. Default LeftCtrl; effective only when Drive burnout is enabled. Camera navigation reserves keypad bindings only. |
| `public Key clutchKey` | Configurable keyboard binding. Default: `Key.LeftShift`; `Key.None` leaves it unbound. |
| `public Key descendKey` | Configurable keyboard binding. Default: `Key.LeftCtrl`; `Key.None` leaves it unbound. |
| `public Key forwardAlternateKey` | Configurable keyboard binding. Default: `Key.UpArrow`; `Key.None` leaves it unbound. |
| `public Key forwardKey` | Configurable keyboard binding. Default: `Key.W`; `Key.None` leaves it unbound. |
| `public Key[] gearKeys` | Keys indexed by requested gear: index 0 is neutral; higher indices select forward gears. `Key.None` leaves an index unbound. |
| `public Key handbrakeKey` | Configurable keyboard binding. Default: `Key.Space`; `Key.None` leaves it unbound. |
| `public Key hazardsKey` | Configurable keyboard binding. Default: `Key.V`; `Key.None` leaves it unbound. |
| `public bool cycleHeadlights` | Use the headlights key for low beams → high beams → off; ignore the separate high-beam key. Default: `true`. |
| `public Key headlightsKey` | Configurable keyboard binding. Default: `Key.L`; `Key.None` leaves it unbound. |
| `public Key highBeamsKey` | Configurable keyboard binding. Default: `Key.None`; `Key.None` leaves it unbound. |
| `public Key hornKey` | Held horn keyboard binding. Default Key.H; None disables it. |
| `public Key hoverBurnoutKey` | Burnout binding while HoverProfile is selected; avoids the Ctrl descent key. Initial value: `Key.C`. |
| `public Key ignitionKey` | Keyboard binding for ignition. Choose None to leave the action unassigned. Initial value: `Key.I`. |
| `public Key leftIndicatorKey` | Configurable keyboard binding. Default: `Key.J`; `Key.None` leaves it unbound. |
| `public Key nitroKey` | Held nitro request key. Default Enter; camera navigation reserves keypad bindings only. |
| `public virtual bool NumpadNavigationActive { get; set; }` | Reserves numeric keypad controls for camera movement rather than vehicle actions. |
| `public Key profileKey` | Keyboard binding for profile. Choose None to leave the action unassigned. Initial value: `Key.B`. |
| `public virtual bool ReserveVehicleSelectionDigits { get; set; }` | Configurable reserve vehicle selection digits for `KeyboardDriveInput`. |
| `public Key reverseAlternateKey` | Configurable keyboard binding. Default: `Key.DownArrow`; `Key.None` leaves it unbound. |
| `public Key reverseGearAlternateKey` | Configurable keyboard binding. Default: `Key.NumpadMinus`; `Key.None` leaves it unbound. |
| `public Key reverseGearKey` | Configurable keyboard binding. Default: `Key.Minus`; `Key.None` leaves it unbound. |
| `public Key reverseKey` | Configurable keyboard binding. Default: `Key.S`; `Key.None` leaves it unbound. |
| `public Key rightIndicatorKey` | Configurable keyboard binding. Default: `Key.K`; `Key.None` leaves it unbound. |
| `public Key shiftDownKey` | Configurable keyboard binding. Default: `Key.Q`; `Key.None` leaves it unbound. |
| `public Key shiftUpKey` | Configurable keyboard binding. Default: `Key.E`; `Key.None` leaves it unbound. |
| `public virtual float SmoothedSteering { get; }` | Read-only/resolved smoothed steering for `KeyboardDriveInput`. |
| `public float steeringReturnTime` | Time in seconds used for steering return time. Larger values make this phase/wait last longer. Initial value: `.12f`. |
| `public float steeringRiseTime` | Time in seconds used for steering rise time. Larger values make this phase/wait last longer. Initial value: `.25f`. |
| `public Key steerLeftAlternateKey` | Configurable keyboard binding. Default: `Key.LeftArrow`; `Key.None` leaves it unbound. |
| `public Key steerLeftKey` | Configurable keyboard binding. Default: `Key.A`; `Key.None` leaves it unbound. |
| `public Key steerRightAlternateKey` | Configurable keyboard binding. Default: `Key.RightArrow`; `Key.None` leaves it unbound. |
| `public Key steerRightKey` | Configurable keyboard binding. Default: `Key.D`; `Key.None` leaves it unbound. |
| `public Key strafeLeftKey` | Configurable keyboard binding. Default: `Key.Q`; `Key.None` leaves it unbound. |
| `public Key strafeRightKey` | Configurable keyboard binding. Default: `Key.E`; `Key.None` leaves it unbound. |
| `public Key transmissionKey` | Configurable keyboard binding. Default: `Key.T`; `Key.None` leaves it unbound. |
| `public Key wheelLiftKey` | Held WheelLift key on any supported vehicle with an enabled module. Initial value: `Key.Z`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void CycleHeadlights()` | Queues the next low/high/off state through the normal command path. | No arguments; no returned value. |
| `public virtual float AdvanceSteering(float target, float deltaTime)` | Advances keyboard steering shaping for elapsed time rather than reading a separate mechanical steering state. | `target` — Configured target object/point; see declared type and owner. `deltaTime` — Elapsed time in seconds supplied by the owning loop. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
| `public override void ResetBindings()` | Restores this adapter's default keys and clears retained controls. | No arguments; no returned value. |

## KeyboardFlightInput

**Runtime/Controller/Input/Samples/KeyboardFlightInput.cs**

Configuration/implementation type for keyboard flight input within input and commands.

**Inherits / implements:** [KeyboardInput](Input.md#keyboardinput), [IVehicleInput](Input.md#ivehicleinput), [IVehicleInputReset](Input.md#ivehicleinputreset).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Key airplaneBrakeKey` | Keyboard binding for airplane brake. Choose None to leave the action unassigned. Initial value: `Key.Space`. |
| `public float airplaneThrottle` | Initial persistent airplane throttle request, normalized from 0 to 1; throttle-up/down keys adjust it. |
| `public ActionInput analogInput` | Hover/airplane gamepad/joystick adapter. Created automatically if unassigned; custom Action references remain configurable. |
| `public Key ascendAlternateKey` | Configurable keyboard binding. Default: `Key.RightShift`; `Key.None` leaves it unbound. |
| `public Key ascendKey` | Configurable keyboard binding. Default: `Key.LeftShift`; `Key.None` leaves it unbound. |
| `public Key burnoutKey` | Held Burnout request; on fixed-wing aircraft the accepted request increases native thrust. Initial value: `Key.C`. |
| `public virtual bool CameraNavigationActive { get; set; }` | Configurable camera navigation active for `KeyboardFlightInput`. |
| `public Key descendKey` | Configurable keyboard binding. Default: `Key.LeftCtrl`; `Key.None` leaves it unbound. |
| `public Key forwardKey` | Configurable keyboard binding. Default: `Key.W`; `Key.None` leaves it unbound. |
| `public Key groundReverseKey` | Ground-only reverse key when the airplane profile enables Allow Ground Reverse. Default: `Key.Z`; clears retained forward throttle. |
| `public Key ignitionKey` | Configurable keyboard binding. Default: `Key.I`; `Key.None` leaves it unbound. |
| `public Key nitroKey` | Held Nitro request, merged with analog input. Initial value: `Key.RightAlt`. |
| `public Key parkingBrakeKey` | Configurable keyboard binding. Default: `Key.LeftAlt`; `Key.None` leaves it unbound. |
| `public Key pitchBackwardAlternateKey` | Configurable keyboard binding. Default: `Key.DownArrow`; `Key.None` leaves it unbound. |
| `public Key pitchBackwardKey` | Configurable keyboard binding. Default: `Key.S`; `Key.None` leaves it unbound. |
| `public Key pitchForwardAlternateKey` | Configurable keyboard binding. Default: `Key.UpArrow`; `Key.None` leaves it unbound. |
| `public Key pitchForwardKey` | Configurable keyboard binding. Default: `Key.W`; `Key.None` leaves it unbound. |
| `public Key profileKey` | Configurable keyboard binding. Default: `Key.B`; `Key.None` leaves it unbound. |
| `public Key reverseKey` | Configurable keyboard binding. Default: `Key.S`; `Key.None` leaves it unbound. |
| `public Key rollLeftKey` | Configurable keyboard binding. Default: `Key.A`; `Key.None` leaves it unbound. |
| `public Key rollRightKey` | Configurable keyboard binding. Default: `Key.D`; `Key.None` leaves it unbound. |
| `public Key steerLeftKey` | Configurable keyboard binding. Default: `Key.A`; `Key.None` leaves it unbound. |
| `public Key steerRightKey` | Configurable keyboard binding. Default: `Key.D`; `Key.None` leaves it unbound. |
| `public Key strafeLeftKey` | Configurable keyboard binding. Default: `Key.Q`; `Key.None` leaves it unbound. |
| `public Key strafeRightKey` | Configurable keyboard binding. Default: `Key.E`; `Key.None` leaves it unbound. |
| `public float throttleChangeRate` | Airplane throttle change per second while holding increase/decrease keys. |
| `public Key throttleDecreaseAlternateKey` | Configurable keyboard binding. Default: `Key.RightCtrl`; `Key.None` leaves it unbound. |
| `public Key throttleDecreaseKey` | Configurable keyboard binding. Default: `Key.LeftCtrl`; `Key.None` leaves it unbound. |
| `public Key throttleIncreaseAlternateKey` | Configurable keyboard binding. Default: `Key.RightShift`; `Key.None` leaves it unbound. |
| `public Key throttleIncreaseKey` | Configurable keyboard binding. Default: `Key.LeftShift`; `Key.None` leaves it unbound. |
| `public Key yawLeftKey` | Configurable keyboard binding. Default: `Key.Q`; `Key.None` leaves it unbound. |
| `public Key yawRightKey` | Configurable keyboard binding. Default: `Key.E`; `Key.None` leaves it unbound. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
| `public override void ResetBindings()` | Restores this adapter's default keys and clears retained controls. | No arguments; no returned value. |
| `public virtual void ResetControls()` | Clears the flight keyboard adapter's retained control state. | No arguments; no returned value. |
| `public virtual void ResetInput()` | Clears held input and pending one-shot requests for a vehicle reset. | — |

## KeyboardInput

**Runtime/Controller/Input/Samples/KeyboardInput.cs**

Shared runtime configuration API for the built-in keyboard inputs.

**Inherits / implements:** `ControllerModule`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual bool ControlsEnabled { get; }` | Current enableControls flag; component enable/disable remains independent. |
| `public bool enableControls` | Enables input processing. Use SetControlsEnabled(false) to clear pending controls immediately. |
| `public bool holdReverseUntilStopped` | Keep requesting reverse while negative throttle is held, without requiring a new press after stopping. Default `false`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public abstract void ResetBindings()` | Restores all keyboard bindings to the built-in defaults and clears retained controls. Other tuning values remain unchanged. | — |
| `public virtual void SetControlsEnabled(bool value)` | Enables or pauses this component's controls. Keyboard inputs clear queued actions, axes and retained aircraft throttle when disabled; Cameras restores its original camera lens when paused. | — |
| `public virtual bool TryGetBinding(string action, out Key key, int index = -1)` | Reads a binding using the same field-name/index rules. Returns false for an invalid lookup and writes Key.None. | — |
| `public virtual bool TrySetBinding(string action, Key key, int index = -1)` | Sets a Key field by its exact serialized name, or a Key[] element using index. Returns false for unknown names, wrong types, invalid keys or indices. Key.None unbinds the action. Clears retained controls on success. | — |

## KeyboardSpaceshipInput

**Runtime/Controller/Input/Samples/KeyboardSpaceshipInput.cs**

**Inherits / implements:** `KeyboardInput`, `IVehicleInput`.

| Member | Meaning |
| --- | --- |
| `public Key forwardKey` | Increase retained forward thrust, like airplane throttle. |
| `public Key reverseKey` | Decrease retained forward thrust to zero. |
| `public Key strafeLeftKey` | Left translation in the spacecraft frame. |
| `public Key strafeRightKey` | Right translation in the spacecraft frame. |
| `public Key ascendKey` | Upward translation in the spacecraft frame. |
| `public Key descendKey` | Downward translation in the spacecraft frame. |
| `public Key pitchUpKey` | Pitch the nose up. |
| `public Key pitchDownKey` | Pitch the nose down. |
| `public Key yawLeftKey` | Yaw left. |
| `public Key yawRightKey` | Yaw right. |
| `public Key rollLeftKey` | Roll left. |
| `public Key rollRightKey` | Roll right. |
| `public Key brakeKey` | Powered braking against world velocity. |
| `public Key nitroKey` | Optional propulsion boost. |
| `public Key burnoutKey` | Optional secondary propulsion boost. |
| `public Key ignitionKey` | Toggle ignition. |
| `public ActionInput analogInput` | Optional analog action adapter; unassigned creates one during startup. |
| `public float throttleChangeRate` | Retained throttle change per second. |
| `public float throttle` | Retained forward thrust, from zero to one. |
| `public Key backwardThrustKey` | Backward thrust without changing retained throttle. |
| `public bool CameraNavigationActive { get; set; }` | Allows an external application to reserve keyboard movement. The demo free-camera modes leave this false so vehicle controls stay active. |
| `public virtual Command ReadCommand()` | Reads current six-axis input and consumes latched ignition. |
| `public override void ResetBindings()` | Restores the default keyboard bindings. |

## KeyboardSubmarineInput

**Runtime/Controller/Input/Samples/KeyboardSubmarineInput.cs**

Configuration/implementation type for keyboard submarine input within input and commands.

**Inherits / implements:** [KeyboardInput](Input.md#keyboardinput), [IVehicleInput](Input.md#ivehicleinput).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public ActionInput analogInput` | Gamepad/joystick adapter. Created automatically if unassigned; custom Action references remain configurable. |
| `public Key ascendAlternateKey` | Configurable keyboard binding. Default: `Key.RightShift`; `Key.None` leaves it unbound. |
| `public Key ascendKey` | Configurable keyboard binding. Default: `Key.LeftShift`; `Key.None` leaves it unbound. |
| `public Key brakeKey` | Configurable keyboard binding. Default: `Key.Space`; `Key.None` leaves it unbound. |
| `public Key burnoutKey` | Held Burnout request; on fixed-wing aircraft the accepted request increases native thrust. Initial value: `Key.C`. |
| `public virtual bool CameraNavigationActive { get; set; }` | Configurable camera navigation active for `KeyboardSubmarineInput`. |
| `public Key descendAlternateKey` | Configurable keyboard binding. Default: `Key.RightCtrl`; `Key.None` leaves it unbound. |
| `public Key descendKey` | Configurable keyboard binding. Default: `Key.LeftCtrl`; `Key.None` leaves it unbound. |
| `public Key forwardKey` | Configurable keyboard binding. Default: `Key.W`; `Key.None` leaves it unbound. |
| `public Key ignitionKey` | Keyboard binding for ignition. Choose None to leave the action unassigned. Initial value: `Key.I`. |
| `public Key nitroKey` | Held Nitro request, merged with analog input. Initial value: `Key.Enter`. |
| `public Key pitchDownKey` | Configurable keyboard binding. Default: `Key.Z`; `Key.None` leaves it unbound. |
| `public Key pitchUpKey` | Configurable keyboard binding. Default: `Key.Q`; `Key.None` leaves it unbound. |
| `public Key profileKey` | Keyboard binding for profile. Choose None to leave the action unassigned. Initial value: `Key.B`. |
| `public Key reverseKey` | Configurable keyboard binding. Default: `Key.S`; `Key.None` leaves it unbound. |
| `public Key steerLeftKey` | Configurable keyboard binding. Default: `Key.A`; `Key.None` leaves it unbound. |
| `public Key steerRightKey` | Configurable keyboard binding. Default: `Key.D`; `Key.None` leaves it unbound. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual Command ReadCommand()` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
| `public override void ResetBindings()` | Restores this adapter's default keys and clears retained controls. | No arguments; no returned value. |
