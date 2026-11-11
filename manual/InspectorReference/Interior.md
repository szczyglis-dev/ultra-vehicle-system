# Interior controls and instruments

[Back to the complete Inspector reference](../InspectorReference.md).

In the controller’s Interior group, **Animators** animate cockpit controls/instruments and connect data sources; **Handles** connect controls to passenger hand/foot grips and IK targets. Both groups include short descriptions and header tooltips.

| Component or data block | Settings declared here |
| --- | --- |
| [AircraftHud](#aircrafthud) | 5 |
| [AnchoredControlAnimator](#anchoredcontrolanimator) | 7 |
| [AnchoredRotation](#anchoredrotation) | 4 |
| [CarHud](#carhud) | 6 |
| [ClutchSource](#clutchsource) | 0 |
| [CommandValueSource](#commandvaluesource) | 1 |
| [ControlAnimator](#controlanimator) | 4 |
| [ControlInteraction](#controlinteraction) | 20 |
| [ControlInteractionAnimationEvents](#controlinteractionanimationevents) | 1 |
| [EngineRpmSource](#enginerpmsource) | 1 |
| [GasSource](#gassource) | 2 |
| [GearLeverAnimator](#gearleveranimator) | 8 |
| [GearLeverPosition](#gearleverposition) | 3 |
| [GearPaddleAnimator](#gearpaddleanimator) | 7 |
| [GearShiftAnimator](#gearshiftanimator) | 3 |
| [GearShiftDirection](#gearshiftdirection) | 0 |
| [HandbrakeSource](#handbrakesource) | 0 |
| [HandleMotion](#handlemotion) | 7 |
| [IGearShiftAnimator](#igearshiftanimator) | 0 |
| [IndicatorSwitchBinding](#indicatorswitchbinding) | 3 |
| [InstrumentNeedle](#instrumentneedle) | 0 |
| [InteriorDataSourceAttribute](#interiordatasourceattribute) | 0 |
| [InteriorModule](#interiormodule) | 0 |
| [InteriorValueSource](#interiorvaluesource) | 0 |
| [PedalAnimator](#pedalanimator) | 8 |
| [PitchSource](#pitchsource) | 0 |
| [ProfileSwitchBinding](#profileswitchbinding) | 5 |
| [RearMirror](#rearmirror) | 14 |
| [RearMirrors](#rearmirrors) | 4 |
| [RollSource](#rollsource) | 1 |
| [RotaryAnimator](#rotaryanimator) | 9 |
| [ServiceBrakeSource](#servicebrakesource) | 1 |
| [SpeedValueSource](#speedvaluesource) | 3 |
| [SteeringSource](#steeringsource) | 1 |
| [SteeringStickAnimator](#steeringstickanimator) | 14 |
| [SteeringWheelAnimator](#steeringwheelanimator) | 8 |
| [SwitchAnimator](#switchanimator) | 8 |
| [SwitchPosition](#switchposition) | 0 |
| [ThrottleAnimator](#throttleanimator) | 8 |
| [TwistThrottleAnimator](#twistthrottleanimator) | 0 |
| [VehicleHandleAnimator](#vehiclehandleanimator) | 1 |
| [VehicleValueSource](#vehiclevaluesource) | 1 |
| [YokeAnimator](#yokeanimator) | 6 |

## AircraftHud

Configuration/implementation type for aircraft hud within cockpit instruments and bindings.

**Source:** `Runtime/Interior/Render/AircraftHud.cs`. Component / asset.

**Inherited settings:** [InteriorModule](Interior.md#interiormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `cockpitSurface` | `Renderer` | Screen mesh receiving the flight-display texture through its material property block. Assign the display face rather than the whole cockpit renderer when possible. | `None / unassigned` | Aircraft Hud > Cockpit Surface |
| `customTexture` | `Texture` | Fixed texture displayed instead of drawing the generated flight HUD. Leave empty to show live vehicle readouts. | `None / unassigned` | Aircraft Hud > Custom Texture |
| `refreshRate` | `float` | Maximum times per second the generated flight display redraws. Lower values save work but make readout changes less smooth. | `15`; Range: 1 to 30 | Aircraft Hud > Refresh Rate |
| `textureProperty` | `string` | Shader texture slot on the cockpit screen that receives the HUD image. Use the exact property name exposed by the screen material's shader. | `"_BaseMap"` | Aircraft Hud > Texture Property |
| `vehicle` | `VehicleController` ([fields](Controller.md#vehiclecontroller)) | Aircraft supplying speed, attitude and other flight readouts. If empty, the display initially binds to a VehicleController in its parent hierarchy. | `None / unassigned` | Aircraft Hud > Vehicle |

## AnchoredControlAnimator

**Source:** `Runtime/Interior/Animators/AnchoredControlAnimator.cs`. Component configuration.

**Inherited settings:** `ControlAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `motion` | `AnchoredRotation` | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. | Anchored Control Animator > Motion |
| `onValueChanged` | `UnityEvent<float>` | After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request. | Anchored Control Animator > Signals and callbacks > On Value Changed |
| `pressDuration` | `float` | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier. | Anchored Control Animator > Press Duration |
| `pressedAngle` | `float` | Pedal angle in degrees at displayed value one. | Anchored Control Animator > Pressed Angle |
| `releasedAngle` | `float` | Pedal angle in degrees at displayed value zero. | Anchored Control Animator > Released Angle |
| `releaseDuration` | `float` | Seconds to fade after releasing the request; zero stops immediately. | Anchored Control Animator > Release Duration |

**AnchoredControlAnimator data source:** `dataSource` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

## AnchoredRotation

Preserves a neutral pose relative to an independent pivot frame.

**Source:** `Runtime/Interior/Controls/AnchoredRotation.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `anchor` | `Transform` | Fixed transform defining the rotation centre and axes. It cannot be the moving mesh or its child, otherwise the hinge would move with the part. | `None / unassigned` | [Control animator] > Motion > Anchor |
| `localAxis` | `Vector3` | Hinge direction in Anchor's local coordinates. The mesh rotates around this axis through the anchor position, even if its imported pivot is elsewhere. | `Vector3.right` | [Control animator] > Motion > Local Axis |
| `movingPart` | `Transform` | Mesh rotated around the independent anchor, retaining its captured offset from the hinge. Its own imported pivot does not have to lie on the hinge. | `None / unassigned` | [Control animator] > Motion > Moving Part |



| Setting | Type | Description | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `reverse` | `bool` | Mirror motion around the neutral pose without changing input or travel limits. | `false` | [Control animator] > Motion > Reverse |

## CarHud

Configuration/implementation type for car hud within cockpit instruments and bindings.

**Source:** `Runtime/Interior/Render/CarHud.cs`. Component / asset.

**Inherited settings:** [InteriorModule](Interior.md#interiormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `cockpitSurface` | `Renderer` | Dashboard screen renderer receiving the display texture. The configured Texture Property must exist in its material's shader. | `None / unassigned` | Car Hud > Cockpit Surface |
| `customTexture` | `Texture` | Texture replacing the generated dashboard readout. Leave empty for live speed, fuel and warning indicators. | `None / unassigned` | Car Hud > Custom Texture |
| `refreshRate` | `float` | Maximum dashboard image redraws per second. Reduce for cheaper small screens; increase for smoother live needles/readouts. | `10`; Range: 1 to 30 | Car Hud > Refresh Rate |
| `speedUnit` | `SpeedUnit` | Unit used for the dashboard's speed readout. Switching between km/h, mph and m/s changes the numbers, not the vehicle's physical speed. Options: `Kph`, `Mph`, `MetresPerSecond`. | `SpeedUnit.Kph` | Car Hud > Speed Unit |
| `textureProperty` | `string` | Shader texture slot receiving the generated dashboard image or Custom Texture. A wrong property name leaves the screen material unchanged. | `"_BaseMap"` | Car Hud > Texture Property |
| `vehicle` | `VehicleController` ([fields](Controller.md#vehiclecontroller)) | Vehicle supplying speed, fuel, lights and assist indicators to the dashboard screen. If empty, the display initially finds a parent VehicleController. | `None / unassigned` | Car Hud > Vehicle |

## ClutchSource

**Source:** `Runtime/Interior/Controls/Source/ClutchSource.cs`. Samples Command.Clutch (0..1).

| Field | Type | Meaning |
| --- | --- | --- |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## CommandValueSource

**Source:** `Runtime/Interior/Controls/Source/CommandValueSource.cs`. Samples a selected Command channel, without resolved actuator mapping.

| Field | Type | Meaning |
| --- | --- | --- |
| `input` | `HandleInput` | Command channel to sample through HandleCommandInput. |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## ControlAnimator

**Source:** `Runtime/Interior/Animators/ControlAnimator.cs`. Shared control presentation base. It references an optional IK handle, coordinates real limb arrival and owns Wait For Handle / Fake Sync Handle Motion. It does not act as an IK target.

**Inherited settings:** `VehicleHandleAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `fakeSyncHandleMotion` | `bool` | Default false. Outbound reach uses the contact pose captured before visual motion; after arrival it follows the live anchor. | [Control animator] > IK contact > Fake Sync Handle Motion |
| `handle` | `VehicleHandle` | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion. | [Control animator] > IK contact > Handle |
| `showGizmos` | `bool` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. | Control Animator > Show Gizmos |
| `waitForHandle` | `bool` | Default true. Wait for the real palm/foot within 2.5 cm after transit, plus finger blending for hands. Mechanics remain immediate; steering is excluded. | [Control animator] > IK contact > Wait For Handle |

## ControlInteraction

`Started`, `Commit`, `Completed` and `Cancelled`

**Source:** `Runtime/Interior/Controls/ControlInteraction.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `animationEvents` | `bool` | Use Animation Events to call Commit and Complete instead of elapsed time. | `false` | Control Interaction > Animation Events |
| `animationLayer` | `string` | Optional layer name temporarily enabled for the gesture. Empty preserves controller weights. Put the gesture trigger transition on that layer. | `""` | Control Interaction > Animation Layer |
| `animationLayerWeight` | `float` | Temporary weight of Animation Layer. Completion/cancellation restores its previous weight unless another system changed it. | `1`; Range: 0–1 | Control Interaction > Animation Layer Weight |
| `animationEnterBlend` | `float` | Seconds used to fade from the underlying pose into an Animator gesture. Zero applies immediately. | `0.2`; Min: 0 | Control Interaction > Animation Enter Blend |
| `animationReturnBlend` | `float` | Seconds used to fade a completed Animator gesture back to the underlying pose. Zero restores immediately; cancellation restores immediately. | `0.2`; Min: 0 | Control Interaction > Animation Return Blend |
| `animator` | `Animator` | Optional override. Otherwise use the current occupant's SeatedAnimator. | `None / unassigned` | Control Interaction > Animator |
| `commitTime` | `float` | Seconds from animation start until the control action is committed when timed commit is used. Set it to the moment the hand visibly presses or moves the control. | `.25`; Minimum: 0 | Control Interaction > Commit Time |
| `customDriver` | `MonoBehaviour` | A MonoBehaviour implementing IControlInteractionDriver. | `None / unassigned` | Control Interaction > Custom Driver |
| `duration` | `float` | Total timed animation interaction length in seconds. After both this duration and Commit Time have elapsed, the sequence can complete and restore hand control. | `.7`; Minimum: 0 | Control Interaction > Duration |
| `hand` | `PassengerBodyPart` | Hand used for the interaction. Choose LeftHand or RightHand; foot selections are not accepted by this hand-interaction sequence. Options: `LeftHand`, `RightHand`, `LeftFoot`, `RightFoot`. | `PassengerBodyPart.LeftHand` | Control Interaction > Hand |
| `keepHandOnTargetWhileAnimating` | `bool` | IK then Animator: retain the hand target and existing IK/physical arm support while a layer masked to fingers performs the press. Ignored by other interaction modes. Captured when the request begins. | `false` | Control Interaction > Keep Hand On Target While Animating |
| `mode` | `ControlInteractionMode` | Immediate commits the control action at once. IK first transfers a hand to Target. Animator uses an animation and its timing/events. Custom delegates the sequence to the assigned interaction handler. Options: `Immediate`, `IK`, `Animator`, `Custom`, `IKThenAnimator`. | `ControlInteractionMode.IK` | Control Interaction > Mode |
| `onCancelled` | `UnityEvent` | After an active interaction is cancelled. No payload; committed gameplay is not rolled back. | `No listeners` | Control Interaction > On Cancelled |
| `onCommit` | `UnityEvent` | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks. | `No listeners` | Control Interaction > On Commit |
| `onCompleted` | `UnityEvent` | After the interaction completes. No payload; completion commits first if still needed. | `No listeners` | Control Interaction > On Completed |
| `onStarted` | `UnityEvent` | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately. | `No listeners` | Control Interaction > On Started |
| `seat` | `PassengerSeat` ([fields](World.md#passengerseat)) | Seat containing the character who operates this control. IK, Animator and Custom modes require an eligible occupant; Immediate can work without one. | `None / unassigned` | Control Interaction > Seat |
| `target` | `VehicleHandle` ([fields](World.md#vehiclehandle)) | Handle the character reaches for before the control action is committed in IK mode. Its contact pose determines where the hand goes. | `None / unassigned` | Control Interaction > Target |
| `timeout` | `float` | Cancels an unfinished Animator or Custom action, including missing animation events. Zero disables timeout. | `5`; Minimum: 0 | Control Interaction > Timeout |
| `trigger` | `string` | Exact Animator trigger parameter name used to start an Animator-mode interaction. It must exist as a trigger in the assigned animation controller. | `"Interact"` | Control Interaction > Trigger |

## ControlInteractionAnimationEvents

Relays Animator events to the active interaction.

**Source:** `Runtime/Interior/Controls/ControlInteractionAnimationEvents.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `interaction` | `ControlInteraction` ([fields](Interior.md#controlinteraction)) | Active interaction receiving commit, complete and cancel events from this animation clip. Put this relay on the object receiving the clip's Animation Events. | `None / unassigned` | Control Interaction Animation Events > Interaction |

## EngineRpmSource

Configuration/implementation type for engine rpm source within cockpit instruments and bindings.

**Source:** `Runtime/Interior/Controls/Source/EngineRpmSource.cs`. Component / asset.

**Inherited settings:** [InteriorValueSource](Interior.md#interiorvaluesource). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `engine` | `Engine` ([fields](Engine.md#engine)) | Engine whose current RPM is returned to the bound gauge or control. A missing or disabled engine returns zero. | `None / unassigned` | Engine Rpm Source > Engine |

## GasSource

**Source:** `Runtime/Interior/Controls/Source/GasSource.cs`. Samples DriveDemand or raw throttle demand. Optional magnitude supports reverse propulsion and motorcycle twist grips.

| Field | Type | Meaning |
| --- | --- | --- |
| `absoluteValue` | `bool` | Return the magnitude, including reverse propulsion; disable to retain the signed source value. |
| `useResolvedDemand` | `bool` | Read resolved signed DriveDemand when true; otherwise Command.Throttle. |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## GearLeverAnimator

**Source:** `Runtime/Interior/Animators/GearLeverAnimator.cs`. Component configuration.

**Inherited settings:** `ControlAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Contact transform used for IK. Parent it to the moving grip; it is separate from the animator hinge/pivot anchor. | Gear Lever Animator > Anchor |
| `downshiftDelay` | `float` | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. | Gear Lever Animator > Downshift Delay |
| `engine` | `Engine` | Assign the engine Engine component/asset used by Propulsion. | Gear Lever Animator > Engine |
| `gearbox` | `Gearbox` | Assign the gearbox Gearbox component/asset used by CommercialAudio. | Gear Lever Animator > Gearbox |
| `mode` | `GearLeverMotionMode` | Rotation or Translation. | Gear Lever Animator > Mode |
| `movingPart` | `Transform` | `Transform` whose pose this mapper owns; keep imported-mesh offsets on its child. | Gear Lever Animator > Moving Part |
| `positions` | `GearLeverPosition[]` | Unique signed gear numbers and their absolute poses. Defaults include R, N and gears 1–6. | Gear Lever Animator > Positions |
| `shiftDuration` | `float` | Visual lever travel duration in seconds; independent of gearbox torque transfer. Initial value: `.18f`. | Gear Lever Animator > Shift Duration |

## GearLeverPosition

**Source:** `Runtime/Interior/Animators/GearLeverAnimator.cs`. Serializable position entry.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `gear` | `int` | -1 = R, 0 = N, positive = forward gear. Duplicates and numbers below -1 are invalid. | Gear Lever Position > Gear |
| `position` | `Vector3` | Absolute local offset relative to Anchor, used in Translation mode. | Gear Lever Position > Position |
| `rotation` | `Vector3` | Absolute Euler degrees relative to Anchor, used in Rotation mode. | Gear Lever Position > Rotation |

## GearPaddleAnimator

**Source:** `Runtime/Interior/Animators/GearPaddleAnimator.cs`. Receives accepted gear changes through IGearShiftAnimator, coalesces downshifts, then reaches, presses and releases the paddle. Link a GearPaddleHandle for the intended hand.

**Inherited settings:** `ControlAnimator`, `IGearShiftAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `direction` | `GearShiftDirection` | Selects the direction policy for this configuration. Options: `Both`, `Up`, `Down`. | Gear Paddle Animator > Direction |
| `downshiftDelay` | `float` | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. | Gear Paddle Animator > Downshift Delay |
| `motion` | `AnchoredRotation` | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. | Gear Paddle Animator > Motion |
| `onPressed` | `UnityEvent` | Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction. | Gear Paddle Animator > Signals and callbacks > On Pressed |
| `pressDuration` | `float` | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier. | Gear Paddle Animator > Press Duration |
| `pressedAngle` | `float` | Pedal angle in degrees at displayed value one. | Gear Paddle Animator > Pressed Angle |
| `returnDuration` | `float` | Return travel duration in seconds, independent of outbound travel. | Gear Paddle Animator > Return Duration |

## GearShiftAnimator

**Source:** `Runtime/Interior/Animators/GearShiftAnimator.cs`. Component configuration.

**Inherited settings:** `VehicleHandleAnimator`.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `animators` | `MonoBehaviour[]` | Visual gear controls implementing IGearShiftAnimator. Assign the paddle animators; do not assign their IK handles. | Gear Shift Animator > Animators |
| `engine` | `Engine` | Assign the engine Engine component/asset used by Propulsion. | Gear Shift Animator > Engine |
| `gearbox` | `Gearbox` | Assign the gearbox Gearbox component/asset used by CommercialAudio. | Gear Shift Animator > Gearbox |

## GearShiftDirection

**Source:** `Runtime/Interior/Animators/GearPaddleAnimator.cs`. Component configuration.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## HandbrakeSource

**Source:** `Runtime/Interior/Controls/Source/HandbrakeSource.cs`. Samples Command.Handbrake as 0 or 1.

| Field | Type | Meaning |
| --- | --- | --- |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## HandleMotion

**Source:** `Runtime/Interior/Animators/HandleMotion.cs`. Reusable geometry mapping for animator-owned rotation or translation in an independent anchor frame. It is not an IK contact.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Independent hinge and local axis frame outside Moving Part. Preserves the authored neutral mesh offset; translation distances are metres regardless of anchor scale. | `None / unassigned` |
| `localAxis` | `Vector3` | Local axis around which the configured motion or operation takes place. Initial value: `Vector3.forward`. | [Control animator] > Motion > Local Axis |
| `maximum` | `float` | Offset at normalized value one; values may be signed/reversed to match model direction. | [Control animator] > Motion > Maximum |
| `minimum` | `float` | Offset at normalized value zero: degrees in rotation mode, local distance in translation mode. | [Control animator] > Motion > Minimum |
| `mode` | `AircraftControlMotionMode` | Chooses rotation (degrees) or translation (local distance) for minimum/maximum/offset. | [Control animator] > Motion > Mode |
| `movingPart` | `Transform` | `Transform` whose pose this mapper owns; keep imported-mesh offsets on its child. | [Control animator] > Motion > Moving Part |



| Setting | Type | Description | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `reverse` | `bool` | Mirror motion around the neutral pose without changing input or travel limits. | `false` | [Control animator] > Motion > Reverse |

## IGearShiftAnimator

**Source:** `Runtime/Interior/Animators/IGearShiftAnimator.cs`. Presentation contract for accepted gear changes. Implement it on visual gear controls; IK handles do not consume gearbox events.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## IndicatorSwitchBinding

**Source:** `Runtime/Interior/Controls/IndicatorSwitchBinding.cs`. Component configuration.

**Inherited settings:** `MonoBehaviour`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `leftPosition` | `SwitchPosition` | Selects the left position policy for this configuration. Options: `Negative`, `Neutral`, `Positive`. Initial value: `SwitchPosition.Negative`. | Indicator Switch Binding > Left Position |
| `lights` | `Lights` | Assign the lights Lights component/asset used by IndicatorAudio. | Indicator Switch Binding > Lights |
| `switchAnimator` | `SwitchAnimator` | Switch animator for this control. | Indicator Switch Binding > Switch Animator |

## InstrumentNeedle

Specializes value-driven rotation for instruments.

**Source:** `Runtime/Interior/Controls/InstrumentNeedle.cs`. Component / asset.

**Inherited settings:** [RotaryAnimator](Interior.md#rotaryanimator). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## InteriorDataSourceAttribute

**Source:** `Runtime/Interior/Controls/Source/InteriorDataSourceAttribute.cs`. Marks an Inspector component field as an IInteriorValueSource consumer. The editor picker accepts application MonoBehaviours implementing the interface.

## InteriorModule

Configuration/implementation type for interior module within cockpit instruments and bindings.

**Source:** `Runtime/Interior/Core/InteriorModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [VehicleModule](Common.md#vehiclemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## InteriorValueSource

Base adapter for an `IInteriorValueSource` value producer.

**Source:** `Runtime/Interior/Controls/Source/InteriorValueSource.cs`. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## PedalAnimator

**Source:** `Runtime/Interior/Animators/PedalAnimator.cs`. Samples resolved propulsion/service braking or an explicit command axis, and animates pedal travel. Its paired PedalHandle owns foot/ankle contact geometry.

**Inherited settings:** `ControlAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `absoluteInput` | `bool` | Use absolute input for signed propulsion/reverse commands. | Pedal Animator > Absolute Input |
| `motion` | `AnchoredRotation` | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. | Pedal Animator > Motion |
| `onValueChanged` | `UnityEvent<float>` | After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request. | Pedal Animator > Signals and callbacks > On Value Changed |
| `pressDuration` | `float` | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier. | Pedal Animator > Press Duration |
| `pressedAngle` | `float` | Pedal angle in degrees at displayed value one. | Pedal Animator > Pressed Angle |
| `releasedAngle` | `float` | Pedal angle in degrees at displayed value zero. | Pedal Animator > Released Angle |
| `releaseDuration` | `float` | Seconds to fade after releasing the request; zero stops immediately. | Pedal Animator > Release Duration |

**PedalAnimator data source:** `dataSource` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

## PitchSource

**Source:** `Runtime/Interior/Controls/Source/PitchSource.cs`. Samples normalized Command.Pitch (-1..1).

| Field | Type | Meaning |
| --- | --- | --- |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## ProfileSwitchBinding

**Source:** `Runtime/Interior/Controls/ProfileSwitchBinding.cs`. Component configuration.

**Inherited settings:** `MonoBehaviour`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `offProfileId` | `string` | Registration ID requested by the off position; defaults to drive. | Profile Switch Binding > Off Profile ID |
| `onProfileId` | `string` | Registration ID requested by the on position; defaults to hover. | Profile Switch Binding > On Profile ID |
| `profileSwitcher` | `ProfileSwitcher` | Assign the profile switcher ProfileSwitcher component/asset used by ProfileSwitchBinding. | Profile Switch Binding > Profile Switcher |
| `switchAnimator` | `SwitchAnimator` | Switch animator for this control. | Profile Switch Binding > Switch Animator |
| `vehicle` | `VehicleController` | Assign the vehicle VehicleController component/asset used by Audio. | Profile Switch Binding > Vehicle |

## RearMirror

Configuration/implementation type for rear mirror within cockpit instruments and bindings.

**Source:** `Runtime/Interior/Render/RearMirrors.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `active` | `bool` | Allows this individual mirror to render while the mirror system is enabled and the surface is visible. Turn off to stop updates for this mirror only. | `true` | Rear Mirror > Active |
| `aspectRatio` | `float` | Width divided by height for an automatically created mirror texture. At 2, the texture is twice as wide as high. Match this to the mirror screen shape. | `1.8`; Range: .5f to 3 | Rear Mirror > Aspect Ratio |
| `camera` | `Camera` | Dedicated camera looking behind the vehicle for this mirror. RearMirrors renders it manually to a texture, so do not use the main driving camera here. | `None / unassigned` | Rear Mirror > Camera |
| `cullingMask` | `LayerMask` | Layers visible in this mirror's reflection. Exclude UI, helpers or costly geometry that should not appear behind the vehicle. | `~0` | Rear Mirror > Culling Mask |
| `farClip` | `float` | Mirror camera's far clipping distance, in metres. | `120`; Minimum: 1 | Rear Mirror > Far Clip |
| `fieldOfView` | `float` | Vertical view angle in degrees of this mirror camera. Increase to show a wider rear area, at the cost of making objects look smaller. | `55`; Range: 10 to 150 | Rear Mirror > Field Of View |
| `flipHorizontally` | `bool` | Flips the displayed camera image left-to-right. Enable when the mirror should present a mirrored view instead of a rear-facing camera feed. | `true` | Rear Mirror > Flip Horizontally |
| `maximumViewDistance` | `float` | Observer-to-mirror distance in metres beyond which this mirror stops updating. Lower values save rendering work when the camera is far from the vehicle. | `25`; Minimum: 1 | Rear Mirror > Maximum View Distance |
| `nearClip` | `float` | Mirror camera's near clipping distance, in metres. | `.1`; Minimum: .01f | Rear Mirror > Near Clip |
| `refreshRate` | `float` | Maximum mirror updates per second. Reduce to save rendering work; frame budget, visibility and distance can further lower the actual rate. | `20`; Range: 1 to 60 | Rear Mirror > Refresh Rate |
| `resolution` | `int` | Width in pixels of an automatically created mirror texture. Higher values sharpen the reflection but increase rendering and texture memory; an assigned Texture keeps its own size. | `256`; Range: 64 to 2048 | Rear Mirror > Resolution |
| `surface` | `Renderer` | Mirror-face renderer that displays this entry's camera image. Its visibility, layer and distance from the observer decide whether a render is needed. | `None / unassigned` | Rear Mirror > Surface |
| `texture` | `RenderTexture` | Optional existing render texture receiving the mirror image. If empty, the system creates one using Resolution and Aspect Ratio. | `None / unassigned` | Rear Mirror > Texture |
| `textureProperty` | `string` | Exact shader property name receiving this mirror's render texture, such as the material's main texture slot. It must match the shader used by Surface. | `"_BaseMap"` | Rear Mirror > Texture Property |

## RearMirrors

Owns mirror eligibility, camera rendering and generated textures.

**Source:** `Runtime/Interior/Render/RearMirrors.cs`. Component / asset.

**Inherited settings:** [InteriorModule](Interior.md#interiormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `maximumRendersPerFrame` | `int` | Maximum mirror-camera renders in one frame. Lower this to spread updates across frames and reduce frame spikes; higher values update more mirrors together. | `2`; Range: 1 to 8 | Rear Mirrors > Maximum Renders Per Frame |
| `mirrors` | `List<RearMirror>` ([fields](Interior.md#rearmirror)) | Mirror screens and their dedicated cameras. Add one entry per independently rendered mirror; each can have its own resolution and refresh limits. | `Empty list` | Rear Mirrors > Mirrors |
| `mirrorsEnabled` | `bool` | Master switch for updating all mirror cameras. Individual entries still need Active enabled and must pass visibility/distance checks. | `true` | Rear Mirrors > Mirrors Enabled |
| `observer` | `Camera` | Camera used to decide whether mirror surfaces are visible and close enough to update. If empty, Camera.main is used. | `None / unassigned` | Rear Mirrors > Observer |

## RollSource

**Source:** `Runtime/Interior/Controls/Source/RollSource.cs`. Samples normalized roll (-1..1), optionally displaying resolved wheel steering while taxiing.

| Field | Type | Meaning |
| --- | --- | --- |
| `useGroundSteering` | `bool` | Use resolved SteeringNormalized while an airplane is on the ground; otherwise return Command.Roll. |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## RotaryAnimator

**Source:** `Runtime/Interior/Animators/RotaryAnimator.cs`. Displays a bounded value as rotation, optionally following an IInteriorValueSource. Link a RotaryHandle when an occupant needs to touch the knob.

**Inherited settings:** `ControlAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `dataSource` | `MonoBehaviour` | Optional component implementing `IInteriorValueSource`; leave empty for API or `UnityEvents` control. | Rotary Animator > Data Source |
| `maximumAngle` | `float` | Upper rotation angle in degrees for the configured motion. Initial value: `135`. | Rotary Animator > Maximum Angle |
| `maximumValue` | `float` | Upper input/value endpoint mapped to the motion or instrument range. Initial value: `1`. | Rotary Animator > Maximum Value |
| `minimumAngle` | `float` | Lower rotation angle in degrees for the configured motion. Initial value: `-135`. | Rotary Animator > Minimum Angle |
| `minimumValue` | `float` | Lower input/value endpoint mapped to the motion or instrument range. | Rotary Animator > Minimum Value |
| `motion` | `AnchoredRotation` | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. | Rotary Animator > Motion |
| `onValueChanged` | `UnityEvent<float>` | After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request. | Rotary Animator > Signals and callbacks > On Value Changed |
| `response` | `float` | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: `18`. | Rotary Animator > Response |

| `value` | `float` | `0` | Requested value in configured units. An assigned Data Source replaces it each frame. |

## ServiceBrakeSource

**Source:** `Runtime/Interior/Controls/Source/ServiceBrakeSource.cs`. Samples resolved service braking or raw Command.ServiceBrake (0..1).

| Field | Type | Meaning |
| --- | --- | --- |
| `useResolvedBrake` | `bool` | Read resolved ServiceBrake when true; otherwise Command.ServiceBrake. |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## SpeedValueSource

Configuration/implementation type for speed value source within cockpit instruments and bindings.

**Source:** `Runtime/Interior/Controls/Source/SpeedValueSource.cs`. Component / asset.

**Inherited settings:** [InteriorValueSource](Interior.md#interiorvaluesource). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `signed` | `bool` | Preserves forward/reverse sign in the speed readout instead of returning speed magnitude. | `false` | Speed Value Source > Signed |
| `speedUnit` | `SpeedUnit` | Output unit; defaults to Kph. Changing this does not alter vehicle physics. For a signed SpeedValueSource, reverse motion remains negative. Options: `Kph`, `Mph`, `MetresPerSecond`. | `SpeedUnit.Kph` | Speed Value Source > Speed Unit |
| `vehicle` | `VehicleController` ([fields](Controller.md#vehiclecontroller)) | Vehicle whose speed is read for a gauge or display. Signed chooses forward/reverse speed; Speed Unit determines the returned units. | `None / unassigned` | Speed Value Source > Vehicle |

## SteeringSource

**Source:** `Runtime/Interior/Controls/Source/SteeringSource.cs`. Samples normalized resolved steering (-1..1), with Hover command steering support.

| Field | Type | Meaning |
| --- | --- | --- |
| `useResolvedSteering` | `bool` | Read SteeringNormalized when true, except Hover which uses Command.Steering. False always reads Command.Steering. |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## SteeringStickAnimator

**Source:** `Runtime/Interior/Animators/SteeringStickAnimator.cs`. Owns joystick pitch/roll model motion and taxi steering presentation. JoystickHandle supplies only the hand contacts.

**Inherited settings:** `SteeringWheelAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `controlResponse` | `float` | Visual pitch and airborne roll response per second. Taxi roll follows wheel steering directly. | Steering Stick Animator > Control Response |
| `driverSeat` | `PassengerSeat` | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator. | Steering Stick Animator > Driver Seat |
| `handle` | `JoystickHandle` | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion. | [Control animator] > IK contact > Handle |
| `leftHandRest` | `Transform` | Independent left-hand palm target, in cabin space. Reserved through the steering hand API. | Steering Stick Animator > Left Hand Rest |
| `localPitchAxis` | `Vector3` | Direction vector defining local pitch axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: `Vector3.right`. | Steering Stick Animator > Local Pitch Axis |
| `localRollAxis` | `Vector3` | Local axis used to apply roll input to the handle or stick. Initial value: `Vector3.forward`. | Steering Stick Animator > Local Roll Axis |
| `maximumPitch` | `float` | Pitch attitude limit in the assisted profile. Aerobatic profiles use angular rates instead. | Steering Stick Animator > Maximum Pitch |
| `maximumRoll` | `float` | Upper local roll angle in degrees. Initial value: `6`. | Steering Stick Animator > Maximum Roll |
| `maximumRollOffset` | `float` | Maximum roll offset for this control. | Steering Stick Animator > Maximum Roll Offset |
| `minimumRoll` | `float` | Lower local roll angle in degrees. Initial value: `-6`. | Steering Stick Animator > Minimum Roll |
| `motion` | `HandleMotion` | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. | Steering Stick Animator > Motion |
| `rotationPivot` | `Transform` | Floor/base pivot. Place the stick mesh and its grip targets below this transform. | Steering Stick Animator > Rotation Pivot |
| `throttle` | `ThrottleAnimator` | Assign the throttle ThrottleAnimator component/asset used by SteeringStickAnimator. | Steering Stick Animator > Throttle |

**SteeringStickAnimator data source:** `pitchSource` — Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source.

## SteeringWheelAnimator

**Source:** `Runtime/Interior/Animators/SteeringWheelAnimator.cs`. Component configuration.

**Inherited settings:** `VehicleHandleAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `boatSteeringResponse` | `float` | Boat helm rendering response per second. Zero follows the resolved rudder immediately. | Steering Wheel Animator > Boat Steering Response |
| `invert` | `bool` | Reverses the sign of the assigned control input before applying control-surface motion. | Steering Wheel Animator > Invert |
| `localRotationAxis` | `Vector3` | Direction vector defining local rotation axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: `Vector3.forward`. | Steering Wheel Animator > Local Rotation Axis |
| `overrideSteeringAngle` | `bool` | Use this animator’s visual full-lock angle instead of the vehicle’s shared steering-wheel angle. Default false; does not change physical wheel steering. | Steering Wheel Animator > Override Steering Angle |
| `steeringAngleAtFullLock` | `float` | Degrees from neutral to full lock on either side when override is enabled. Default 35; nonnegative. | Steering Wheel Animator > Steering Angle At Full Lock |
| `steeringWheel` | `Transform` | Assign the steering wheel reference used by SteeringWheelAnimator. Leave unassigned only when this feature is optional or the component can resolve it automatically. | Steering Wheel Animator > Steering Wheel |
| `vehicle` | `VehicleController` | Assign the vehicle VehicleController component/asset used by Audio. | Steering Wheel Animator > Vehicle |
| `anchor` | `Transform` | Optional independent steering-wheel hinge and local axis frame. Empty keeps the original rest-local rotation. | `None / unassigned` |

**SteeringWheelAnimator data source:** `dataSource` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

## SwitchAnimator

**Source:** `Runtime/Interior/Animators/SwitchAnimator.cs`. Owns binary or three-position detents, requested/actual state, visual travel and switch events. It references a SwitchHandle for optional limb reach synchronization.

**Inherited settings:** `ControlAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `initiallyOn` | `bool` | Initial binary request used by first preparation. | Switch Animator > Initially On |
| `initialPosition` | `SwitchPosition` | Initial three-position detent used by first preparation. | Switch Animator > Initial Position |
| `motion` | `HandleMotion` | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. | Switch Animator > Motion |
| `neutralOffset` | `float` | Middle-detent geometry offset in degrees or local distance, according to motion.mode. | Switch Animator > Neutral Offset |
| `onPositionChanged` | `UnityEvent<SwitchPosition>` | After a changed switch detent request. Payload: `SwitchPosition`; silent immediate synchronization does not invoke it. | Switch Animator > Signals and callbacks > On Position Changed |
| `onValueChanged` | `UnityEvent<bool>` | After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request. | Switch Animator > Signals and callbacks > On Value Changed |
| `threePosition` | `bool` | Enables Negative/Neutral/Positive detents; without it Negative requests throw. | Switch Animator > Three Position |
| `transitionDuration` | `float` | Seconds for visible detent travel; settlement events follow that travel. | Switch Animator > Transition Duration |

## SwitchPosition

**Source:** `Runtime/Interior/Animators/SwitchAnimator.cs`. Component configuration.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## ThrottleAnimator

**Source:** `Runtime/Interior/Animators/ThrottleAnimator.cs`. Owns throttle grip geometry and displayed throttle, including optional external presentation. The paired ThrottleHandle contains only IK contact and grip settings.

**Inherited settings:** `ControlAnimator`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `driverSeat` | `PassengerSeat` | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator. | Throttle Animator > Driver Seat |
| `externalValue` | `float` | Externally supplied throttle/control value used when the selected input mode requests external control. | Throttle Animator > External Value |
| `motion` | `HandleMotion` | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. | Throttle Animator > Motion |
| `response` | `float` | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: `5`. | Throttle Animator > Response |
| `useExternalValue` | `bool` | Uses explicit cockpit presentation instead of following vehicle throttle. | Throttle Animator > Use External Value |
| `useLeftHand` | `bool` | Uses the driver's left hand rather than the right for this control. | Throttle Animator > Use Left Hand |
| `vehicle` | `VehicleController` | Assign the vehicle VehicleController component/asset used by Audio. | Throttle Animator > Vehicle |

**ThrottleAnimator data source:** `dataSource` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

## TwistThrottleAnimator

**Source:** `Runtime/Interior/Animators/TwistThrottleAnimator.cs`. Inherits [AnchoredControlAnimator](#anchoredcontrolanimator).

Rotates the grip from resolved DriveDemand. Motion, angle, timing, preview and event settings are inherited.


### Limb motion synchronization

Control animators, switches, pedals and rotary controls expose `waitForHandle` (default true) and `fakeSyncHandleMotion` (default false). Assign `handle` to the corresponding IK contact on each ControlAnimator. Waiting uses actual limb contact within 2.5 cm after controller arrival, plus finger blending for hands, without a timeout bypass. Fake sync freezes only the outbound contact in the vehicle frame and follows the live contact after arrival. The steering wheel is excluded. See [the handle synchronization guide](../Scripting/Handles.md#synchronizing-control-motion-with-limb-arrival) for mode combinations and lifecycle behavior.

No additional Inspector settings are declared on this type.

## VehicleHandleAnimator

**Source:** `Runtime/Interior/Animators/VehicleHandleAnimator.cs`. Shared base for instrument geometry ownership. Set Automatic Motion off when an external Animator or Timeline owns the model.

**Inherited settings:** `VehicleModule`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `automaticMotion` | `bool` | Default true. Allows this animator to write model transforms; disable when an external animation system owns the visible control. | Vehicle Handle Animator > Automatic Motion |

## VehicleValueSource

**Source:** `Runtime/Interior/Controls/Source/VehicleValueSource.cs`. Base for reusable vehicle presentation sources. It stores an optional vehicle and falls back to the nearest parent vehicle. Sources are read by consumers and never drive the vehicle.

| Field | Type | Meaning |
| --- | --- | --- |
| `vehicle` | `VehicleController` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |

## YokeAnimator

Configuration/implementation type for yoke animator within cockpit instruments and bindings.

**Source:** `Runtime/Interior/Animators/YokeAnimator.cs`. Component / asset.

**Inherited settings:** [SteeringWheelAnimator](Interior.md#steeringwheelanimator). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `controlResponse` | `float` | Visual control response per second, shared by roll and pitch. | `1.5`; Minimum: .1f | Yoke Animator > Control Response |
| `localPitchTravelAxis` | `Vector3` | Direction the yoke slides for pitch commands, in the slider parent's local coordinates. Usually forward/back along the steering column. | `Vector3.forward` | Yoke Animator > Local Pitch Travel Axis |
| `pitchSlide` | `Transform` | Sliding column, with the rotating yoke below it. Leave empty to slide the yoke itself. | `None / unassigned` | Yoke Animator > Pitch Slide |
| `pitchTravel` | `float` | Maximum yoke slide in metres from neutral for full pitch input in either direction. Increase for a longer push/pull stroke. | `.035`; Minimum: 0 | Yoke Animator > Pitch Travel |

**YokeAnimator data source:** `pitchSource` — Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source.


| Setting | Type | Description | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `reversePitch` | `bool` | Reverse column translation independently of steering-wheel Invert. | `false` | Yoke Animator > Reverse Pitch |
| `pitchAnchor` | `Transform` | Optional independent column translation direction frame outside the slider. Local Pitch Travel Axis uses its local axes; Pitch Travel is in metres. | `None / unassigned` |
