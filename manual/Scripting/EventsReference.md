# Events reference

Public notifications grouped by the class that declares them. Each class has its own table with the event/callback, argument types and the point at which it fires. Events follow declaration order within each class; the class sections are ordered by name.

`C#` means subscribe with `+=` / `-=`. `Inspector` means a UnityEvent field, connected in the Inspector or with `AddListener` / `RemoveListener`. Arguments are shown in delegate order; `—` means no arguments. Read current state when first subscribing rather than expecting an initial notification.

Inherited events are listed once on their declaring base class: Module lifecycle events also apply to derived modules. Profiles and helper classes are included where they expose events. Inspector callbacks nested in settings identify their invoking component below.

## Runtime classes

### AircraftControlSurfaces

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ControlsChanged` | C# | `Vector3` | When displayed pitch/roll/yaw controls change; Vector3 components carry those presentation values. |
| `FlapsChanged` | C# | `float` | When the normalized flap presentation request changes. |
| `AirbrakeChanged` | C# | `float` | When the normalized airbrake presentation request changes. |
| `ExternalControlChanged` | C# | `bool` | When aircraft surface presentation changes external/follow-vehicle ownership. |

Details: [AircraftControlSurfaces API](../API/Aircraft.md#aircraftcontrolsurfaces).

### AircraftHud

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Changed` | C# | `Telemetry` | After the HUD receives an updated reading. |

Details: [AircraftHud API](../API/Interior.md#aircrafthud).

### AnchoredControlAnimator

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `onValueChanged` | Inspector | `float` | After the animated control value changes (0–1), including reset to the released value. |

Details: [AnchoredControlAnimator API](../API/Interior.md#anchoredcontrolanimator).

### BoatProfile

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `SinkingChanged` | C# | `bool` | Raised once when sinking is started or stopped. The argument is the new sinking state; repeated requests for the same state do not raise another event. |

Details: [BoatProfile API](../API/Boat.md#boatprofile).

### Brakes

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ServiceBrakeChanged` | C# | `float` | When resolved service-brake demand changes (0–1). |
| `HandbrakeChanged` | C# | `bool` | When the resolved handbrake state changes; bool reports the new state. |
| `BrakingChanged` | C# | `bool` | Moving service-brake activity changes; payload is active/inactive. Owned by Brakes, independent of TireFeedback. |

Details: [Brakes API](../API/DriveDynamics.md#brakes).

### Burnout

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `BurnoutStarted` | C# | — | Assistance begins. |
| `BurnoutStopped` | C# | — | Assistance ends, including reset/disable. |
| `StateChanged` | C# | `bool` | Reports transitions into and out of active assistance. |

Details: [Burnout API](../API/DriveDynamics.md#burnout).

### Cameras

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `CameraChanged` | C# | `Camera` | After Attach changes the assigned camera or Detach releases it; payload is the new camera or null. Inspector field edits do not raise this API event. |
| `ModeChanged` | C# | `ViewMode` | After SetView or Attach changes the view; payload is the new mode. |

Details: [Cameras API](../API/Camera.md#cameras).

### CarHud

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Changed` | C# | `Telemetry` | After the HUD receives an updated reading. |

Details: [CarHud API](../API/Interior.md#carhud).

### Clutch

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `EngagementChanged` | C# | `float` | When resolved clutch engagement changes (0–1); distinct from pedal travel. |
| `AutomaticChanged` | C# | `bool` | When automatic clutch assistance selection changes. |

Details: [Clutch API](../API/DriveDynamics.md#clutch).

### ControlInteraction

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `onStarted` | Inspector | — | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately. |
| `onCommit` | Inspector | — | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks. |
| `onCompleted` | Inspector | — | After the interaction completes. No payload; completion commits first if still needed. |
| `onCancelled` | Inspector | — | After an active interaction is cancelled. No payload; committed gameplay is not rolled back. |

Details: [ControlInteraction API](../API/Interactions.md#controlinteraction).

### Coupler

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Attached` | C# | `Trailer` | After coupler admission creates the relationship. |
| `Detached` | C# | `Trailer` | After explicit detachment/cleanup of this hitch relationship. |

Details: [Coupler API](../API/Towing.md#coupler).

### Damage

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Hit` | C# | `DamageHit` | When a damage hit is accepted. |
| `DeformationRequested` | C# | `DamageHit, float` | Accepted hit and radius before part detachment; optional deformation receivers process it synchronously. |
| `EffectsCleared` | C# | — | Requests clearing optional impact presentation. |
| `FullyRepaired` | C# | — | After a full repair pass and effect cleanup; it does not guarantee destroyed objects were recreated. |
| `PartsChanged` | C# | — | Reports that the damage boundary list has been refreshed. |

Details: [Damage API](../API/Damage.md#damage).

### DamagePart

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Restored` | C# | `DamagePart` | After full remount/state/mesh repair; incremental Repair(amount) does not emit this event. |
| `Detached` | C# | `DamagePart` | After a damage part detaches. |
| `Damaged` | C# | `DamagePart, float` | After the part accepts damage. |
| `Repaired` | C# | `DamagePart, float` | After damage is actually removed. |

Details: [DamagePart API](../API/Damage.md#damagepart).

### DrivingAssists

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `TractionControlChanged` | C# | `bool` | When `DrivingAssists` changes its coordinated traction-control choice. |
| `StabilityControlChanged` | C# | `bool` | When `DrivingAssists` changes its stability-assistance choice. |

Details: [DrivingAssists API](../API/DriveDynamics.md#drivingassists).

### DroppableObject

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Dropped` | C# | `DroppableObject` | After this payload detaches and inherits motion. |

Details: [DroppableObject API](../API/Weapons.md#droppableobject).

### Engine

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `EngineStateChanged` | C# | `bool` | After engine running state changes. |
| `GearChanged` | C# | `int` | When Engine observes a changed gearbox gear during Step; the initial gear sample is silent. |
| `ActiveGearboxChanged` | C# | `Gearbox` | Reports a change of effective gearbox identity, including removal or disable. Read ActiveGearbox when first subscribing. |

Details: [Engine API](../API/DriveDynamics.md#engine).

### EventAudio

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Played` | C# | `EffectEvent, AudioClip` | When `EventAudio` plays a resolved event clip. |

Details: [EventAudio API](../API/Audio.md#eventaudio).

### Events

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Raised` | C# | `EffectEvent` | When the adapter translates a typed source notification or an integration publishes a custom effect. |

Details: [Events API](../API/Events.md#events).

### FuelTank

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `FuelChanged` | C# | `float` | After fuel quantity changes; the value is current litres, not the transfer amount. |
| `Emptied` | C# | — | On the transition to empty fuel. |
| `Refuelled` | C# | — | After an actual increase in fuel, including `SetFuel`. No payload; query quantity if needed. |

Details: [FuelTank API](../API/Interior.md#fueltank).

### Gearbox

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `GearChanged` | C# | `int` | After gear selection/synchronization changes the signed gear: reverse -1, neutral 0, forward positive. |
| `ShiftStarted` | C# | `int` | When an accepted selection starts its shift interval. |
| `ShiftCompleted` | C# | `int` | When that shift interval completes; a zero-duration shift can complete immediately. |

Details: [Gearbox API](../API/DriveDynamics.md#gearbox).

### GearPaddleAnimator

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `onPressed` | Inspector | — | Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction. |

Details: [GearPaddleAnimator API](../API/Interior.md#gearpaddleanimator).

### HandleController

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Started` | C# | `HandleUse` | After a token owns its limb. Payload is the new token. |
| `Finished` | C# | `HandleUse` | After completion or cancellation has released ownership and restored any owned binding. Payload is the ended token. |

Details: [HandleController API](../API/Handles.md#handlecontroller).

### HandleUse

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Arrived` | C# | — | After binding the destination and running the arrival callback. Persistent acquisitions do not emit this event. |
| `Completed` | C# | — | After the return completes and the home binding is restored. |
| `Cancelled` | C# | — | After cancellation has released ownership. An already committed action is not undone. |

Details: [HandleUse API](../API/Handles.md#handleuse).

### HumanoidPassenger

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `BeforeSeatedIK` | C# | `HumanoidPassenger` | Immediately before seated IK work. |
| `AfterSeatedIK` | C# | `HumanoidPassenger` | Immediately after seated IK work. |

Details: [HumanoidPassenger API](../API/PassengerControllers.md#humanoidpassenger).

### InputGate.Route

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `selected` | Inspector | — | InputGate selects the route matching the active profile, after assigning its input source. |

Details: [InputGate.Route API](../API/Input.md#inputgateroute).

### IPartMotionSource

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `MotionOccurred` | C# | `PartMotionEvent` | Reports the corresponding source state change. |
| `MotionAudioStopped` | C# | — | Reports the corresponding source state change. |

Details: [IPartMotionSource API](../API/MovingParts.md#ipartmotionsource).

### LandingGear

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `StateChanged` | C# | `LandingGearState` | When deployment sequencing changes `LandingGearState`. |

Details: [LandingGear API](../API/Aircraft.md#landinggear).

### LightChannel

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `LitChanged` | C# | `bool` | When a `LightChannel`'s actual lit output changes. |

Details: [LightChannel API](../API/Lights.md#lightchannel).

### Lights

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `IndicatorPhaseChanged` | C# | `bool` | When the shared flashing output phase changes. |
| `BeamModeChanged` | C# | `BeamMode` | When requested beam mode changes. |
| `IndicatorsChanged` | C# | `IndicatorState` | When requested direction/hazard state changes. |

Details: [Lights API](../API/Lights.md#lights).

### MovingPart

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `OpeningStarted` | C# | — | Once before an opening operation moves the pose. No payload; interruptions never imply completion. |
| `OpeningCompleted` | C# | — | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
| `ClosingStarted` | C# | — | Once before a closing operation moves the pose. |
| `ClosingCompleted` | C# | — | Once after the actual pose reaches the requested closing target. |
| `Moved` | C# | `MovingPart` | After moving-part pose changes. |
| `MotionEnabledChanged` | C# | `bool` | When moving-part motion availability changes. |
| `MotionOccurred` | C# | `PartMotionEvent` | Reports an admitted movement phase to optional presentation receivers. |
| `MotionAudioStopped` | C# | — | Requests stopping movement audio after interruption or disable. |

Details: [MovingPart API](../API/MovingParts.md#movingpart).

### Nitro

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `NitroStarted` | C# | — | Effective boost begins. |
| `NitroStopped` | C# | — | Effective boost ends, including reset/disable. |
| `AmountChanged` | C# | `float` | Reports actual remaining charge after a change; payload is charge units. |
| `BoostStateChanged` | C# | `bool` | Reports transitions into/out of resolved boost; payload is the active flag. |
| `Depleted` | C# | — | Raised once when positive charge reaches zero. |
| `OutputStateChanged` | C# | `bool` | Reports a change of the propulsion-output session. Receivers can be absent without affecting boost. |

Details: [Nitro API](../API/DriveDynamics.md#nitro).

### ObjectDropper

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Dropped` | C# | `ObjectDropper, DroppableObject` | After the dropper releases a payload; includes the dropper and released object. |
| `DroppingEnabledChanged` | C# | `bool` | When dropper availability changes. |

Details: [ObjectDropper API](../API/Weapons.md#objectdropper).

### PartMotionEvents

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `openingStarted` | Inspector | — | VehicleBodyPart or MovingPart starts opening; follows its OpeningStarted C# event. |
| `openingCompleted` | Inspector | — | VehicleBodyPart or MovingPart reaches its open target; follows OpeningCompleted, not an interrupted operation. |
| `closingStarted` | Inspector | — | VehicleBodyPart or MovingPart starts closing; follows its ClosingStarted C# event. |
| `closingCompleted` | Inspector | — | VehicleBodyPart or MovingPart reaches its closed target; follows ClosingCompleted. |

Details: [PartMotionEvents API](../API/MovingParts.md#partmotionevents).

### PassengerAccess

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `StateChanged` | C# | `PassengerAccess, AccessState` | When access sequencing changes. |
| `Finished` | C# | `PassengerAccess, bool` | When an access attempt ends; the bool reports success. Check occupancy after cancellation/handover. |
| `BeforeEnter` | C# | `PassengerSeatContext` | After reservation succeeds, before collision preparation, door requests and entry motion. |
| `AfterEnter` | C# | `PassengerSeatContext` | After the entire entry sequence succeeds and its reservation/Target are cleared. |
| `BeforeExit` | C# | `PassengerSeatContext` | Before collision preparation, door requests and exit motion; occupancy is still retained. |
| `AfterExit` | C# | `PassengerSeatContext` | After the entire exit sequence succeeds and its reservation/Target are cleared. |
| `Cancelled` | C# | `PassengerSeatContext` | After a prepared/started sequence is cancelled and reservation/Target cleared; context retains original identities. |
| `EnterBegin` | C# | `PassengerSeatContext` | Once an admitted entry starts in Opening, after Before checks; seat reservation is held. |
| `EnterInProgress` | C# | `PassengerAccessProgress` | After each entry motion sample in Moving, starting at zero; progress one is not whole-sequence completion. |
| `EnterFinished` | C# | `PassengerSeatContext` | Only after the entire entry succeeds, including the required door state and reservation/Target cleanup. |
| `EnterCancelled` | C# | `PassengerSeatContext` | After a reserved entry is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. |
| `ExitBegin` | C# | `PassengerSeatContext` | Once an admitted exit starts in Opening, after Before checks; seat reservation is held. |
| `ExitInProgress` | C# | `PassengerAccessProgress` | After each exit motion sample in Moving, starting at zero; progress one is not whole-sequence completion. |
| `ExitFinished` | C# | `PassengerSeatContext` | Only after the entire exit succeeds, including the required door state and reservation/Target cleanup. |
| `ExitCancelled` | C# | `PassengerSeatContext` | After a reserved exit is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. |
| `started` | Inspector | — | Inspector callback when access sequencing starts; no payload. |
| `completed` | Inspector | — | Inspector callback when access succeeds; no payload. |
| `cancelled` | Inspector | — | Inspector callback when access is cancelled; no payload. |
| `onEnterBegin` | Inspector | — | Counterpart of `EnterBegin`; no arguments. |
| `onEnterInProgress` | Inspector | `float` | Counterpart of `EnterInProgress`; normalized motion time 0..1. |
| `onEnterFinish` | Inspector | — | Counterpart of `EnterFinished`; no arguments. |
| `onEnterCancelled` | Inspector | — | Counterpart of `EnterCancelled`; no arguments. |
| `onExitBegin` | Inspector | — | Counterpart of `ExitBegin`; no arguments. |
| `onExitInProgress` | Inspector | `float` | Counterpart of `ExitInProgress`; normalized motion time 0..1. |
| `onExitFinish` | Inspector | — | Counterpart of `ExitFinished`; no arguments. |
| `onExitCancelled` | Inspector | — | Counterpart of `ExitCancelled`; no arguments. |

Details: [PassengerAccess API](../API/PassengerAccess.md#passengeraccess).

### Passengers

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Entered` | C# | `PassengerSeat, PassengerBody` | After a body acquires a seat; includes both the seat and occupant. |
| `Exited` | C# | `PassengerSeat, PassengerBody, PassengerExitReason` | After occupancy is released; includes seat, former occupant and exit reason. |
| `BeforeEnter` | C# | `PassengerSeatContext` | Forwards the validated seat entry boundary before occupancy/controller assignment. |
| `AfterEnter` | C# | `PassengerSeatContext` | After successful attachment and entry notifications; carries the seat/passenger context. |
| `BeforeExit` | C# | `PassengerSeatContext` | Before an occupied seat detaches its passenger, including ejection and lifecycle cleanup. |
| `AfterExit` | C# | `PassengerSeatContext` | After detachment and exit notifications; before an ejection adds its velocity change. |
| `BeforeEject` | C# | `PassengerSeatContext` | Before a seat starts ejection detachment; occupancy is still retained. |
| `AfterEject` | C# | `PassengerSeatContext` | After seat ejection and its built-in velocity change. |
| `onBeforeEnter` | Inspector | `PassengerSeatContext` | Before an occupant acquires any seat on this vehicle. |
| `onEntered` | Inspector | `PassengerSeat, PassengerBody` | After an occupant acquires a seat; includes both seat and passenger. |
| `onBeforeExit` | Inspector | `PassengerSeatContext` | Before occupancy ends on any seat, including ejection or disable. |
| `onExited` | Inspector | `PassengerSeat, PassengerBody, PassengerExitReason` | After occupancy ends; includes seat, passenger and reason. |
| `onBeforeEject` | Inspector | `PassengerSeatContext` | Before any seat ejects its occupant. |
| `onEjected` | Inspector | `PassengerSeatContext` | After a successful ejection, including its optional impulse. |

Details: [Passengers API](../API/PassengerControllers.md#passengers).

### PassengerSeat

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ControllerChanged` | C# | `PassengerSeat, PassengerControllerType, PassengerControllerType` | After a successful controller handover; does not synthesize another entry or exit. |
| `Entered` | C# | `PassengerBody` | After this seat acquires its occupant. |
| `ResetRequested` | C# | `PassengerBody` | When a custom occupant receives a vehicle-reset request; the application performs its reset. |
| `Exited` | C# | `PassengerBody, PassengerExitReason` | After this seat releases occupancy; includes former occupant and exit reason. |
| `BeforeEnter` | C# | `PassengerSeatContext` | After admission checks, before occupancy/controller assignment; the seat is still empty. |
| `AfterEnter` | C# | `PassengerSeatContext` | After successful attachment and Entered notifications. |
| `BeforeExit` | C# | `PassengerSeatContext` | Before detachment while still occupied; includes exit, ejection, disable and destruction. |
| `AfterExit` | C# | `PassengerSeatContext` | After detachment and Exited notifications; an ejection velocity change happens afterward. |
| `BeforeEject` | C# | `PassengerSeatContext` | Before ejection detaches the still-seated occupant. |
| `AfterEject` | C# | `PassengerSeatContext` | After ejection detachment and built-in velocity change; custom controllers own their physics. |
| `onBeforeEnter` | Inspector | `PassengerBody` | Before seat occupancy is acquired. The request is validated again after observers return. |
| `onEntered` | Inspector | `PassengerBody` | After the passenger acquires this seat. |
| `onBeforeExit` | Inspector | `PassengerBody` | Before seat occupancy is released, including ejection and disable paths. |
| `onExited` | Inspector | `PassengerBody, PassengerExitReason` | After occupancy ends. Includes the released passenger and the exit reason. |
| `onBeforeEject` | Inspector | `PassengerBody` | Before ejection releases occupancy or applies its impulse. |
| `onEjected` | Inspector | `PassengerBody` | After successful ejection and its optional impulse. |
| `onControllerChanged` | Inspector | `PassengerControllerType` | After the seat switches to a different passenger controller. |
| `onResetRequested` | Inspector | `PassengerBody` | When a custom occupant is asked to reset its seated pose. |
| `onLimbReleased` | Inspector | `PassengerBodyPart` | Invoked once when an individual hand or foot enters damage-released state. |
| `onHandsReleased` | Inspector | `PassengerBody` | Once when both hands have entered the damage-released state. |
| `onFeetReleased` | Inspector | `PassengerBody` | Once when both feet have entered the damage-released state. |

Details: [PassengerSeat API](../API/PassengerControllers.md#passengerseat).

### PedalAnimator

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `onValueChanged` | Inspector | `float` | After displayed pedal travel changes (0–1), including immediate positioning and reset. |

Details: [PedalAnimator API](../API/Interior.md#pedalanimator).

### ProfileSwitcher

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ProfileChanged` | C# | `DriveProfile` | After configuring an accepted target profile; an animated transition may still be in progress. |
| `ProfilesChanged` | C# | — | After successful registration, removal or list replacement. Does not imply a strategy change. |
| `TransitionStarted` | C# | — | After target configuration and animated-route initialization; immediate switches do not emit it. |
| `TransitionBegan` | C# | `ProfileTransition, string, string` | Admitted transition component, source profile ID and destination profile ID. |
| `TransitionAudioStopped` | C# | — | Requests stopping transition presentation. |
| `TransitionProgressed` | C# | `float` | During animation, with normalized progress. |
| `TransitionCompleted` | C# | — | After animated transition completion, contact restoration and final presentation. |
| `TransitionInterrupted` | C# | — | On disable during a transition, after finalizing the selected target and presentation. |
| `started` | Inspector | — | Inspector callback when an animated route starts. |
| `progressed` | Inspector | `float` | Inspector callback with normalized animation progress. |
| `completed` | Inspector | — | Inspector callback after animated route completion. |

Details: [ProfileSwitcher API](../API/DriveProfiles.md#profileswitcher).

### Propulsion

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `SpeedChanged` | C# | `float` | When visual propulsion spool changes (0 stopped to 1 full speed); not RPM, mechanical thrust or individual shaft speed. |

Details: [Propulsion API](../API/Aircraft.md#propulsion).

### PropulsionJets

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `JetsEnabledChanged` | C# | `bool` | When jet presentation availability changes. |

Details: [PropulsionJets API](../API/Presentation.md#propulsionjets).

### RearMirrors

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `MirrorsEnabledChanged` | C# | `bool` | When whole-system mirror eligibility changes. |
| `MirrorEnabledChanged` | C# | `int, bool` | When one mirror's eligibility changes. |

Details: [RearMirrors API](../API/Interior.md#rearmirrors).

### Rocket

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Exploded` | C# | `Rocket, Vector3` | At the rocket's explosion boundary. |

Details: [Rocket API](../API/Weapons.md#rocket).

### RocketLauncher

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `TriggerChanged` | C# | `bool` | When held trigger intent changes. |
| `FiringEnabledChanged` | C# | `bool` | When weapon firing availability changes. |
| `Fired` | C# | `RocketLauncher, Rocket` | After an admitted shot launches a rocket; holding the trigger alone is not a shot. |

Details: [RocketLauncher API](../API/Weapons.md#rocketlauncher).

### RotaryAnimator

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ValueChanged` | C# | `float` | When SetValue changes the requested value in configured units; does not wait for visible rotation to settle. |
| `onValueChanged` | Inspector | `float` | After the requested rotary value changes, in configured units; follows ValueChanged and does not wait for settling. |

Details: [RotaryAnimator API](../API/Interior.md#rotaryanimator).

### SeatAccess

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `onEnterBegin` | Inspector | — | Invoked when an admitted enter operation begins for this access path. |
| `onEnterInProgress` | Inspector | `float` | Normalized enter motion progress (0..1). One does not imply door cleanup has finished. |
| `onEnterFinish` | Inspector | — | Invoked after the entire enter operation succeeds, including door cleanup. |
| `onEnterCancelled` | Inspector | — | Invoked when a reserved enter operation is cancelled or fails. Rejected requests do not invoke it. |
| `onExitBegin` | Inspector | — | Invoked when an admitted exit operation begins for this access path. |
| `onExitInProgress` | Inspector | `float` | Normalized exit motion progress (0..1). One does not imply door cleanup has finished. |
| `onExitFinish` | Inspector | — | Invoked after the entire exit operation succeeds, including door cleanup. |
| `onExitCancelled` | Inspector | — | Invoked when a reserved exit operation is cancelled or fails. Rejected requests do not invoke it. |

### Skidmarks

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Cleared` | C# | — | After skidmark history is cleared. |

Details: [Skidmarks API](../API/Presentation.md#skidmarks).

### Stabilization

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Overturned` | C# | `Telemetry` | Raised once when sustained tilt qualifies; carries the telemetry snapshot at that transition. |
| `Recovered` | C# | `Telemetry` | Raised once when tilt falls below the recovery threshold; carries the telemetry snapshot at that transition. |

Details: [Stabilization API](../API/CollisionsAndStabilization.md#stabilization).

### Steering

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `AngleChanged` | C# | `float` | When the resolved road-wheel angle changes, in degrees (not steering-column degrees). |

Details: [Steering API](../API/DriveDynamics.md#steering).

### Suspension

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Landed` | C# | `LandingEvent` | First upright wheel support after qualifying flight. Context includes height, air time, speed and impact data; assisted rebounds are marked. Independent of landing assistance. |
| `LandingCompleted` | C# | `LandingEvent` | First support from all operational wheel rays after Landed; may be the same step. This does not mean suspension motion has settled. |

Details: [Suspension API](../API/Suspension.md#suspension).

### SwitchAnimator

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ValueChanged` | C# | `bool` | When requested IsOn changes; negative and positive detents both count as on. Immediate synchronization is silent. |
| `Switched` | C# | `bool` | When motion settles; both negative and positive detents report true. |
| `PositionChanged` | C# | `SwitchPosition` | When the requested detent changes; distinguishes all three positions. |
| `PositionReached` | C# | `SwitchPosition` | When motion settles at the requested detent. |
| `onValueChanged` | Inspector | `bool` | After the binary IsOn request changes, following ValueChanged. Negative/positive detents both count as on; immediate synchronization is silent. |
| `onPositionChanged` | Inspector | `SwitchPosition` | After a changed detent request, following PositionChanged; immediate synchronization is silent. |

Details: [SwitchAnimator API](../API/Interior.md#switchanimator).

### ThrottleAnimator

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ValueChanged` | C# | `float` | When the displayed throttle value changes during Step, including smoothing toward its target. |

Details: [ThrottleAnimator API](../API/Interior.md#throttleanimator).

### TireFeedback

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Sampled` | C# | — | After TireFeedback updates its wheel/contact classification. No payload; read the component's current cached feedback. |
| `WheelGroundedChanged` | C# | `int, bool` | When feedback grounded state changes; arguments are wheel index and the new state. |
| `WheelSurfaceChanged` | C# | `int, TireSurfaceProfile` | When a wheel selects a different presentation surface; its profile can be null. |
| `SkiddingChanged` | C# | `bool` | When aggregate feedback skid state changes. |

Details: [TireFeedback API](../API/Events.md#tirefeedback).

### TireSmoke

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `WheelBurnoutChanged` | C# | `int, bool` | When indexed wheel burnout-smoke presentation changes. |
| `SmokeModeChanged` | C# | `TireSmokeMode` | After the smoke presentation mode changes. |

### TractionControl

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ActiveChanged` | C# | `bool` | When resolved traction-control intervention changes between active/inactive. |

Details: [TractionControl API](../API/DriveDynamics.md#tractioncontrol).

### Trailer

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ConnectionBroken` | C# | — | When a trailer's active hitch relationship breaks. |

Details: [Trailer API](../API/Towing.md#trailer).

### Transmission

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ModeChanged` | C# | `TransmissionMode` | After transmission mode changes and its gearbox connection is applied. |

Details: [Transmission API](../API/DriveDynamics.md#transmission).

### VehicleBodyPart

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `OpeningStarted` | C# | — | Once before an opening operation moves the pose. No payload; interruptions never imply completion. |
| `OpeningCompleted` | C# | — | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
| `ClosingStarted` | C# | — | Once before a closing operation moves the pose. |
| `ClosingCompleted` | C# | — | Once after the actual pose reaches the requested closing target. |
| `OpenChanged` | C# | `bool` | When the part's requested open state changes. |
| `PhysicsChanged` | C# | `bool` | When the part's `usePhysics` policy changes. |
| `Released` | C# | — | After the body part is released from vehicle-owned motion. |
| `MotionOccurred` | C# | `PartMotionEvent` | Reports an admitted movement phase to optional presentation receivers. |
| `MotionAudioStopped` | C# | — | Requests stopping movement audio after interruption or disable. |

Details: [VehicleBodyPart API](../API/Damage.md#vehiclebodypart).

### VehicleController

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Collided` | C# | `Collision` | During Unity collision entry; Collision is live callback data, so copy values before deferring work. |
| `ContactPersisted` | C# | `Collision` | During sustained native contact; copy values before retaining or deferring them. |
| `Impacted` | C# | `Impact` | After copying collision contact/velocity/impulse data; the Impact snapshot can be retained. |
| `AfterPhysicsStep` | C# | `Telemetry` | After the module pipeline and telemetry sampling; this is not a callback after native Physics.Simulate. |
| `Teleported` | C# | `Pose` | After world pose and occupants have been synchronized. |
| `CommandSampled` | C# | `Command` | After the selected provider is sampled. |
| `DriveProfileChanged` | C# | `DriveProfile` | After an immediate profile change is configured successfully. |
| `ConfigurationChanged` | C# | — | After validated wheel/module configuration is applied. |
| `WheelAvailabilityChanged` | C# | `int, bool` | After a wheel availability change; arguments are configured wheel index and new availability. |
| `InputSourceChanged` | C# | `MonoBehaviour` | After assigning input ownership. |
| `ModuleRegistered` | C# | `VehicleModule` | After registration/configuration. |
| `ModuleUnregistered` | C# | `VehicleModule` | After removal from future pipeline membership; independent callbacks may still need disabling. |
| `WheelAttachmentChanged` | C# | `Wheel, bool` | Forwards an owned Wheel attachment change after its per-wheel notification; bool is the new attached state. |
| `Repaired` | C# | — | After RepairAll finishes in-place repair and actuator cleanup; Teleport alone does not emit it. |

Details: [VehicleController API](../API/Core.md#vehiclecontroller).

### VehicleHandle

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ContactStarted` | C# | `HandleContactContext` | Once on a not-touching to touching transition; C# event runs before the matching UnityEvent. |
| `ContactUpdated` | C# | `HandleContactContext` | Once per contact sample while touching, including its start sample. Payload identifies handle, seat, occupant, part and target. |
| `ContactEnded` | C# | `HandleContactContext` | Once when contact is lost or released (including exit/disable/rebinding). Payload retains the original occupant identity. |
| `ValueChangeStarted` | C# | `HandleValueContext` | Once when a significant value change or explicit BeginValueChange starts activity. |
| `ValueChanging` | C# | `HandleValueContext` | Each active changed/manual sample; does not imply contact or commit a gameplay action. |
| `ValueChangeStopped` | C# | `HandleValueContext` | Once when the value settles for valueStopDelay, explicit EndValueChange runs or the handle is disabled/destroyed. |
| `onContactStarted` | Inspector | `HandleContactContext` | Inspector-configurable counterpart of ContactStarted. Runs after the C# event for the same phase. |
| `onContactUpdated` | Inspector | `HandleContactContext` | Inspector-configurable counterpart of ContactUpdated. Runs after the C# event for the same phase. |
| `onContactEnded` | Inspector | `HandleContactContext` | Inspector-configurable counterpart of ContactEnded. Runs after the C# event for the same phase. |
| `onValueChangeStarted` | Inspector | `HandleValueContext` | Inspector-configurable counterpart of ValueChangeStarted. Runs after the C# event for the same phase. |
| `onValueChanging` | Inspector | `HandleValueContext` | Inspector-configurable counterpart of ValueChanging. Runs after the C# event for the same phase. |
| `onValueChangeStopped` | Inspector | `HandleValueContext` | Inspector-configurable counterpart of ValueChangeStopped. Runs after the C# event for the same phase. |

Details: [VehicleHandle API](../API/Handles.md#vehiclehandle).

### VehicleMeshDeformation

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `DeformationChanged` | C# | — | After pending deformation geometry is uploaded. No payload; inspect owned geometry at this boundary. |
| `Restored` | C# | — | After deformable shape is restored to rest geometry. |

Details: [VehicleMeshDeformation API](../API/Damage.md#vehiclemeshdeformation).

### VehicleModule

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `EnabledChanged` | C# | `bool` | After `SetEnabled` changes the module flag. |
| `Configured` | C# | `VehicleController` | After controller-driven module configuration. |
| `Stepped` | C# | `VehicleController, Command, float` | After this registered module has stepped. |

Details: [VehicleModule API](../API/Modules.md#vehiclemodule).

### WaterInteraction

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `InteractionEnabledChanged` | C# | `bool` | When the master water-interaction gate changes. |
| `ProviderChanged` | C# | `WaterProvider` | When the assigned water provider changes; null means no assigned provider. |
| `SubmergedChanged` | C# | `bool` | When sampled body-center submergence changes. |

Details: [WaterInteraction API](../API/Water.md#waterinteraction).

### WeaponBarrel

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `TriggerChanged` | C# | `bool` | When held trigger intent changes. |
| `FiringEnabledChanged` | C# | `bool` | When weapon firing availability changes. |
| `Fired` | C# | `WeaponBarrel, MonoBehaviour` | After an admitted shot creates/releases its projectile or store. |

Details: [WeaponBarrel API](../API/Weapons.md#weaponbarrel).

### Wheel

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `AttachmentChanged` | C# | `Wheel, bool` | After attachment state and collider/actuator availability update; bool is the new attached state. |

Details: [Wheel API](../API/WheelContact.md#wheel).

### WheelLift

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `WheelLiftStarted` | C# | — | Assistance begins. |
| `WheelLiftStopped` | C# | — | Assistance ends after controlled lowering, or immediately on reset/disable/excessive tilt. |
| `StateChanged` | C# | `bool` | New assistance state. |

Details: [WheelLift API](../API/WheelLift.md#wheellift).

### Wipers

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `StrokeStarted` | C# | `bool` | When a wiper stroke starts. |
| `RunningChanged` | C# | `bool` | When the wiper running request changes. |
| `SpeedChanged` | C# | `float` | After `SetSpeed` changes requested wiper speed. |
| `Parked` | C# | — | When wipers reach their parked state. |
| `WiperStrokeStarted` | C# | `string, bool` | Reports entry ID and stroke direction: false for outward, true for return. Entries have independent phase clocks. |
| `WiperRunningChanged` | C# | `string, bool` | After an API changes an entry's effective running request; payload is its ID and new bool request. |
| `WiperSpeedChanged` | C# | `string, float` | After an API changes an entry's effective speed; payload is its ID and cycles per minute. |
| `WiperParked` | C# | `string` | When an entry reaches/is immediately placed at its parked pose; payload is its ID. |
| `StrokeAudioRequested` | C# | `Wiper, bool, float` | Specific wiper, stroke direction and resolved cycles per minute for optional audio. |
| `WiperRemoved` | C# | `Wiper` | Reports an entry removed from the mechanism so optional receivers can release its resources. |
| `AudioStopped` | C# | — | Requests stopping wiper audio. |
| `StrokeBatchStarted` | C# | — | Begins a mechanism tick; receivers can deduplicate shared voices within this batch. |

Details: [Wipers API](../API/Wipers.md#wipers).





### DamageFeedback

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Impacted` | C# | `DamageContact` | Accepted non-scrape cue. |
| `Scraped` | C# | `DamageContact` | Accepted sustained-contact sample; can run every physics step. |
| `Cleared` | C# | — | Contact history and presentation were cleared. |
| `Contacted` | C# | `DamageContact` | Any accepted presentation contact. |
| `TireImpacted` | C# | `DamageContact` | Accepted wheel strike, distinct from touchdown. |
| `TireLanded` | C# | `DamageContact` | Accepted wheel touchdown with landing strength/height. |
| `SuspensionMoved` | C# | `DamageContact` | Accepted suspension compression/landing cue. |
| `PartBroken` | C# | `DamageContact` | Accepted breakage presentation cue; not physical detachment itself. |
| `EffectsCleared` | C# | — | Custom effect leases were cleared. |
| `EffectPlayed` | C# | `DamageHit, DamageImpactProfile` | Custom pooled impact effect successfully started. |
| `onContact` | Inspector | `DamageContact` | Any accepted presentation contact. |
| `onImpact` | Inspector | `DamageContact` | Accepted non-scrape cue. |
| `onScrape` | Inspector | `DamageContact` | Accepted sustained-contact sample; can run every physics step. |
| `onTireImpact` | Inspector | `DamageContact` | Accepted wheel strike, distinct from touchdown. |
| `onTireLanding` | Inspector | `DamageContact` | Accepted wheel touchdown with landing strength/height. |
| `onSuspension` | Inspector | `DamageContact` | Accepted suspension compression/landing cue. |
| `onBreakage` | Inspector | `DamageContact` | Accepted breakage presentation cue; not physical detachment itself. |
| `onEffectPlayed` | Inspector | `DamageHit, DamageImpactProfile` | Custom pooled impact effect successfully started. |
| `onCleared` | Inspector | — | Contact history and presentation were cleared. |
| `onEffectsCleared` | Inspector | — | Custom effect leases were cleared. |
| `FallLanded` | C# | `DamageContact` | First qualifying height-fall ground contact, shared across body, attached panels and wheels. |
| `RolloverImpacted` | C# | `DamageContact` | One qualifying tilted/spinning ground strike. |
| `onFallLanding` | Inspector | `DamageContact` | Inspector equivalent of FallLanded. |
| `onRolloverImpact` | Inspector | `DamageContact` | Inspector equivalent of RolloverImpacted. |

Details: [Damage feedback API](../API/DamageFeedback.md#damagefeedback).

### DamageAudio

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Played` | C# | `DamageContact, AudioClip` | A one-shot started; includes the contact and actual clip. |
| `ScrapeStarted` | C# | `DamageContact, AudioClip` | A scrape lane became audible; contact and original loop clip. |
| `ScrapeStopped` | C# | `DamageContact, AudioClip` | A scrape lane faded/stopped, switched material/group or was cleared. |
| `DamagePlayed` | C# | `DamageHit, DamageImpactProfile, AudioClip` | A scripted hit sound started; includes the selected material profile. |
| `DetachmentPlayed` | C# | `DamagePart, AudioClip` | A named part detachment sound started. |
| `onPlayed` | Inspector | `DamageContact, AudioClip` | A one-shot started; includes the contact and actual clip. |
| `onDamagePlayed` | Inspector | `DamageHit, DamageImpactProfile, AudioClip` | A scripted hit sound started; includes the selected material profile. |
| `onDetachmentPlayed` | Inspector | `DamagePart, AudioClip` | A named part detachment sound started. |
| `onScrapeStarted` | Inspector | `DamageContact, AudioClip` | A scrape lane became audible; contact and original loop clip. |
| `onScrapeStopped` | Inspector | `DamageContact, AudioClip` | A scrape lane faded/stopped, switched material/group or was cleared. |

Details: [Damage feedback API](../API/DamageFeedback.md#damageaudio).

## Demo and example classes

### CameraRigDemo

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `ModeChanged` | C# | `ViewMode` | After a changed camera view mode is applied. |
| `TargetChanged` | C# | `Transform` | After retargeting the demo camera; null releases the target. |
| `PointerCaptureFilter` | C# query | `Vector2 → bool` | CanCaptureAt checks a screen position. Every invoked filter must allow capture; the first false vetoes it. This is not a state-change notification. |

### ProjectileDemo

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Impacted` | C# | `ProjectileDemo, ProjectileImpact` | Once on an accepted collision, after copying impact data and before application-owned hit handling. |

### VehicleSelectorDemo

| Event / callback | Kind | Arguments | When it fires / meaning |
| --- | --- | --- | --- |
| `Selected` | C# | `VehicleController` | After a valid selection updates input routing, camera target and HUD; selecting the same index can notify again. |
