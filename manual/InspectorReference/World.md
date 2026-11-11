# Cameras, passengers, water, towing and weapons

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [AccessAnimationEvents](#accessanimationevents) | 0 |
| [AccessAnimationProfile](#accessanimationprofile) | 38 |
| [AccessMotion](#accessmotion) | 0 |
| [AdaptiveHandGrip](#adaptivehandgrip) | 9 |
| [AdaptiveHandGrip.Finger](#adaptivehandgripfinger) | 10 |
| [AnchorHandle](#anchorhandle) | 8 |
| [BalanceRider](#balancerider) | 33 |
| [CameraModule](#cameramodule) | 4 |
| [Cameras](#cameras) | 5 |
| [ControlHandle](#controlhandle) | 1 |
| [Coupler](#coupler) | 13 |
| [CustomPassengerBody](#custompassengerbody) | 0 |
| [DroppableObject](#droppableobject) | 3 |
| [GearLeverHandle](#gearleverhandle) | 0 |
| [GearPaddleHandle](#gearpaddlehandle) | 0 |
| [HandGrip](#handgrip) | 5 |
| [HandGrip.FingerPose](#handgripfingerpose) | 3 |
| [HandleAnimatorBinding](#handleanimatorbinding) | 15 |
| [HandleFingerPosition](#handlefingerposition) | 7 |
| [HandleHandPose](#handlehandpose) | 19 |
| [HandleHandPosition](#handlehandposition) | 5 |
| [HandleHandPositionProfile](#handlehandpositionprofile) | 3 |
| [HandlePoseSettings](#handleposesettings) | 9 |
| [HandleUseSettings](#handleusesettings) | 17 |
| [HumanoidAccessMotion](#humanoidaccessmotion) | 2 |
| [HumanoidIK](#humanoidik) | 16 |
| [HumanoidJointDefinition](#humanoidjointdefinition) | 5 |
| [HumanoidPassenger](#humanoidpassenger) | 18 |
| [InteriorCamera](#interiorcamera) | 6 |
| [JoystickHandle](#joystickhandle) | 0 |
| [MotorcycleHandle](#motorcyclehandle) | 4 |
| [ObjectDropper](#objectdropper) | 2 |
| [OrbitCamera](#orbitcamera) | 18 |
| [PassengerAccess](#passengeraccess) | 13 |
| [PassengerBehaviour](#passengerbehaviour) | 1 |
| [PassengerBody](#passengerbody) | 0 |
| [PassengerBodyPartConfig](#passengerbodypartconfig) | 7 |
| [PassengerFootConfig](#passengerfootconfig) | 11 |
| [PassengerGForceLimits](#passengergforcelimits) | 11 |
| [PassengerHandConfig](#passengerhandconfig) | 22 |
| [PassengerJointSupport](#passengerjointsupport) | 12 |
| [PassengerModule](#passengermodule) | 0 |
| [PassengerRestraints](#passengerrestraints) | 30 |
| [Passengers](#passengers) | 7 |
| [PassengerAnimatorLayers](#passengeranimatorlayers) | 3 |
| [PassengerAnimatorLayers.Layer](#passengeranimatorlayerslayer) | 4 |
| [PassengerSeat](#passengerseat) | 46 |
| [PassengerTransformSupport](#passengertransformsupport) | 14 |
| [PedalFootMode](#pedalfootmode) | 0 |
| [PedalHandle](#pedalhandle) | 2 |
| [RagdollCollisionHelper](#ragdollcollisionhelper) | 13 |
| [RagdollCollisionRelay](#ragdollcollisionrelay) | 0 |
| [Rocket](#rocket) | 23 |
| [RocketLauncher](#rocketlauncher) | 4 |
| [RotaryHandle](#rotaryhandle) | 0 |
| [SeatAccess](#seataccess) | 35 |
| [SteeringHandRegrip](#steeringhandregrip) | 2 |
| [SteeringHandRegripSettings](#steeringhandregripsettings) | 7 |
| [SteeringWheelHandle](#steeringwheelhandle) | 20 |
| [SteeringWheelHandle.RimSample](#steeringwheelhandlerimsample) | 2 |
| [SwitchHandle](#switchhandle) | 0 |
| [ThrottleHandle](#throttlehandle) | 0 |
| [Trailer](#trailer) | 5 |
| [VehicleHandle](#vehiclehandle) | 32 |
| [WaterInteraction](#waterinteraction) | 4 |
| [WaterProvider](#waterprovider) | 0 |
| [WaterSurfaceProfile](#watersurfaceprofile) | 12 |
| [WaterSurface](#watersurface) | 11 |
| [WeaponBarrel](#weaponbarrel) | 10 |
| [WorldModule](#worldmodule) | 0 |
| [RiderAnimationRule](#rideranimationrule) | 14 |
| [RiderAnimator](#rideranimator) | 8 |
| [RiderMotionState](#ridermotionstate) | 11 |
| [YokeHandle](#yokehandle) | 0 |

| [PassengerLimbDamageFeedback](#passengerlimbdamagefeedback) | 6 |

| [PassengerCollisionSurface](#passengercollisionsurface) | 3 |

## RiderMotionState

**Source:** `Runtime/World/Passengers/Riding/RiderMotionState.cs`. Nested configuration data.

| Field | Type | Purpose | Initial value |
| --- | --- | --- | --- |
| `seated` | `bool` | Rider motion state value; see the API reference. | `default` |
| `grounded` | `bool` | Rider motion state value; see the API reference. | `default` |
| `footPushing` | `bool` | Rider motion state value; see the API reference. | `default` |
| `reversing` | `bool` | Rider motion state value; see the API reference. | `default` |
| `leftFootPlanted` | `bool` | Rider motion state value; see the API reference. | `default` |
| `rightFootPlanted` | `bool` | Rider motion state value; see the API reference. | `default` |
| `speed` | `float` | Rider motion state value; see the API reference. | `default` |
| `steeringAngle` | `float` | Rider motion state value; see the API reference. | `default` |
| `leanAngle` | `float` | Rider motion state value; see the API reference. | `default` |
| `ridingBlend` | `float` | Rider motion state value; see the API reference. | `default` |
| `stepPhase` | `float` | Rider motion state value; see the API reference. | `default` |


## RiderAnimator

**Source:** `Runtime/World/Passengers/Riding/RiderAnimator.cs`. Component.

| Field | Type | Purpose | Initial value |
| --- | --- | --- | --- |
| `rider` | `BalanceRider` | Balance Rider supplying steering, lean, foot and occupancy signals. | `default` |
| `animator` | `Animator` | Optional explicit Animator. Empty follows the occupant's seated animation source, including ragdoll animation sampling. | `default` |
| `speedParameter` | `string` | Optional float parameter for forward speed in m/s. | `"RiderSpeed"` |
| `steeringParameter` | `string` | Optional signed steering angle float in degrees. | `"RiderSteeringAngle"` |
| `leanParameter` | `string` | Optional motorcycle lean float in degrees. | `"RiderLean"` |
| `feetParameter` | `string` | Optional feet Ground-to-Riding blend float from zero to one. | `"RiderFeetBlend"` |
| `phaseParameter` | `string` | Optional normalized alternating step phase float. | `"RiderStepPhase"` |
| `rules` | `RiderAnimationRule[]` | Independent conditions, angle bands, bools, triggers, state crossfades and custom callbacks. | `Array.Empty<RiderAnimationRule>()` |


## RiderAnimationRule

**Source:** `Runtime/World/Passengers/Riding/RiderAnimator.cs`. Nested configuration data.

| Field | Type | Purpose | Initial value |
| --- | --- | --- | --- |
| `condition` | `RiderMotionCondition` | Rider condition controlling this rule. Angle conditions use the signed range below. | `default` |
| `actionName` | `string` | Unique action name for a Custom condition. Control it with SetActionActive, PlayAction and StopAction. | `default` |
| `minimumAngle` | `float` | Inclusive minimum signed steering/lean angle in degrees. | `-180` |
| `maximumAngle` | `float` | Inclusive maximum signed steering/lean angle in degrees. | `180` |
| `angleHysteresis` | `float` | Extra degrees retained around an active angle range, preventing repeated events at its boundary. | `1` |
| `feetBlendThreshold` | `float` | Feet Raised is true above this blend; Feet Lowered below it. | `.5f` |
| `boolParameter` | `string` | Optional Animator bool held while the condition is active. | `default` |
| `enterTrigger` | `string` | Optional Animator trigger fired once when this condition begins. | `default` |
| `exitTrigger` | `string` | Optional Animator trigger fired once when this condition ends. | `default` |
| `state` | `string` | Optional full Animator state path crossfaded on entry. Empty leaves state selection to your controller. | `default` |
| `layer` | `int` | Animator layer for the optional state. | `default` |
| `fadeSeconds` | `float` | Crossfade duration in seconds for the optional state. | `.2f` |
| `onEntered` | `UnityEvent` | Condition began, including angle-range transitions. Can call custom animation code. | `new UnityEvent()` |
| `onExited` | `UnityEvent` | Condition ended or the occupant/binding was released. | `new UnityEvent()` |


## AccessAnimationEvents

Relays animation access markers into the sequence.

**Source:** `Runtime/World/Passengers/Access/AccessAnimationEvents.cs`. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## AccessAnimationProfile

Stores animation states, references and timing configuration.

**Source:** `Runtime/World/Passengers/Access/AccessAnimationProfile.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `completionTimeout` | `float` | Additional time allowed before an unfinished access operation is cancelled, in seconds. | `2`; Minimum: .1f | Access Animation Profile > Completion Timeout |
| `controller` | `RuntimeAnimatorController` | Animator controller containing the standing, seated, entry and exit states named below. The profile's bindings must match this controller for boarding animation to start. | `None / unassigned` | Access Animation Profile > Controller |
| `enterClip` | `AnimationClip` | Humanoid reference clip used to measure the entry trajectory. It must match the motion played by Enter State so placement correction follows the visible animation. | `None / unassigned` | Access Animation Profile > Enter Clip |
| `enterLeftFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` | Access Animation Profile > Enter Left Foot Contact |
| `enterPlacement` | `AnimationCurve` | Weight of the outside alignment during entry; fades before the character sits. | `AnimationCurve.EaseInOut(0, 1, .65, 0)` | Access Animation Profile > Enter Placement |
| `enterRange` | `Vector2` | Start and end of the usable entry motion as fractions of the reference clip, from 0 to 1. Trim idle frames so placement is calibrated over the actual boarding movement. | `new Vector2(0, 1)` | Access Animation Profile > Enter Range |
| `enterRightFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` | Access Animation Profile > Enter Right Foot Contact |
| `enterState` | `string` | Animator state path played while the character boards. Use the state containing the entry motion calibrated by Enter Clip and Enter Range. | `"Base Layer.Enter In"` | Access Animation Profile > Enter State |
| `enterTrigger` | `string` | Trigger parameter sent to the Animator to request the entry animation. The exact trigger name must exist in Controller. | `"EnterIn"` | Access Animation Profile > Enter Trigger |
| `exitBlendSeconds` | `float` | Blend from the current seated body and hand pose into the exit animation. Zero disables the blend. Ankle rotation remains animated. | `.2`; Minimum: 0 | Access Animation Profile > Exit Blend Seconds |
| `exitClip` | `AnimationClip` | Humanoid reference clip used to measure the exit trajectory. It must match Exit State so the character is aligned to the doorway and outside position. | `None / unassigned` | Access Animation Profile > Exit Clip |
| `exitLeftFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` | Access Animation Profile > Exit Left Foot Contact |
| `exitPlacement` | `AnimationCurve` | Outside-alignment weight over normalized exit progress: horizontal axis is progress, vertical axis is weight. Raise the curve earlier to move the character toward the outside placement sooner. | `AnimationCurve.EaseInOut(.2, 0, .85, 1)` | Access Animation Profile > Exit Placement |
| `exitRange` | `Vector2` | Start and end of the usable exit motion as fractions of the reference clip. The end must be greater than the start; use this to exclude unrelated frames. | `new Vector2(0, 1)` | Access Animation Profile > Exit Range |
| `exitRightFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` | Access Animation Profile > Exit Right Foot Contact |
| `exitState` | `string` | Animator state path played while leaving the seat. Use the state matching Exit Clip and Exit Range. | `"Base Layer.Enter Out"` | Access Animation Profile > Exit State |
| `exitTrigger` | `string` | Trigger parameter sent to request the exit animation. It must match the transition setup in Controller. | `"EnterOut"` | Access Animation Profile > Exit Trigger |
| `footBlendSeconds` | `float` | Seconds spent blending foot contact corrections on or off during access motion. Increase to soften foot placement changes; decrease for faster planting/release. | `.16`; Minimum: .01f | Access Animation Profile > Foot Blend Seconds |
| `handoverBlendSeconds` | `float` | Final seated blend on entry and positional support fade on exit. Exit rotations follow the Animator. Set zero to disable the additional blend. | `.2`; Minimum: 0 | Access Animation Profile > Handover Blend Seconds |
| `holdFeetWhileIdle` | `bool` | Disable when an application locomotion / ground IK system owns standing feet. | `true` | Access Animation Profile > Hold Feet While IDle |
| `horizontalScale` | `float` | Scales the horizontal part of the calibrated boarding trajectory. Increase to fit a wider cabin/longer step; vertical placement is adapted separately. | `1`; Range: .5f to 1.5f | Access Animation Profile > Horizontal Scale |
| `layer` | `int` | Animator layer index used to play and inspect boarding/exit states. | `0`; Minimum: 0 | Access Animation Profile > Layer |
| `manualFootContacts` | `bool` | Use foot-contact curves instead of automatic height/speed classification. | `false` | Access Animation Profile > Manual Foot Contacts |
| `plantHeight` | `float` | Maximum foot height above the reference ground, in metres, for considering it planted. Increase to accept more near-ground poses; too high can pin a foot that should be lifting. | `.06`; Minimum: .01f | Access Animation Profile > Plant Height |
| `plantSpeed` | `float` | Maximum foot speed in m/s for considering a near-ground foot planted. Lower values require it to be nearly still; higher values can hold feet during faster motion. | `.3`; Minimum: .01f | Access Animation Profile > Plant Speed |
| `playbackSpeed` | `float` | Playback speed multiplier for the boarding and exit motion. | `1`; Minimum: .01f | Access Animation Profile > Playback Speed |
| `releaseEntryFeet` | `float` | Normalized boarding progress after which standing foot plants are released. | `.65`; Range: 0 to 1 | Access Animation Profile > Release Entry Feet |
| `rootMotionRotationWeight` | `float` | Weight of extracted root turning. | `1; Range: 0 to 1` | Access Animation Profile > Root Motion Rotation Weight |
| `rootMotionScale` | `Vector3` | Local-axis scale of extracted root movement. The seat/outside anchors still define endpoints. | `Vector3.one` | Access Animation Profile > Root Motion Scale |
| `seatedClip` | `AnimationClip` | Humanoid reference clip used to measure the seated pose. Choose a pose matching the end of the boarding sequence and the seat's intended posture. | `None / unassigned` | Access Animation Profile > Seated Clip |
| `seatedState` | `string` | Animator state path for the seated pose reached at the end of entry. It supplies the animation-side pose before seated control takes over. | `"Base Layer.Seated"` | Access Animation Profile > Seated State |
| `seatPose` | `AnimationCurve` | Blend to the physical seat pose. Reach 1 before handing over to seat physics. | `AnimationCurve.EaseInOut(.72, 0, .94, 1)` | Access Animation Profile > Seat Pose |
| `standingClip` | `AnimationClip` | Humanoid reference clip used to measure the standing pose for spatial alignment. It calibrates placement; the Animator controller still owns actual playback. | `None / unassigned` | Access Animation Profile > Standing Clip |
| `standingState` | `string` | Full Animator state path used for the standing pose, including the layer name when needed. It must match the configured controller exactly. | `"Base Layer.Idle"` | Access Animation Profile > Standing State |
| `transitionAllowance` | `float` | Extra time allowance in seconds for Animator state transitions during access. | `.2`; Minimum: 0 | Access Animation Profile > Transition Allowance |
| `useAnimatorRootMotion` | `bool` | Extract translation/turning from Animator root motion; enable for unbaked Root Transform tracks. Disable for movement baked into pose. | `false` | Access Animation Profile > Use Animator Root Motion |
| `useFootIK` | `bool` | Stabilize grounded feet during access; disable to use the uncorrected animation. | `true` | Access Animation Profile > Use Foot IK |



| Setting | Type | Description | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `physicsBlendSeconds` | `float` | Seconds to fade the whole visible skeleton from the last entry animation pose into the live ragdoll. Physics runs immediately. Zero disables this visual blend. | `.2f` | Access Animation Profile > Physics Blend Seconds |

## AccessMotion

Replaceable character-motion adapter called by `PassengerAccess` during entry/exit.

**Source:** `Runtime/World/Passengers/Access/AccessMotion.cs`. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## AdaptiveHandGrip

Binds a character to a surface and applies fitted finger poses.

**Source:** `Runtime/World/Passengers/IK/AdaptiveHandGrip.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `digits` | `Finger[]` ([fields](World.md#adaptivehandgripfinger)) | Generated from Mecanim mapping or assigned explicitly for a custom skeleton. | `Empty list` | Adaptive Hand Grip > Digits |
| `iterations` | `int` | Finger/contact fitting iteration count. Higher values increase fitting work. | `6`; Range: 2 to 12 | Adaptive Hand Grip > Iterations |
| `leftHand` | `bool` | Selects the left hand for this grip configuration. | `false` | Adaptive Hand Grip > Left Hand |
| `palmThickness` | `float` | Palm clearance thickness in metres used when fitting the hand to the handle surface. | `.009`; Minimum: .001f | Adaptive Hand Grip > Palm Thickness |
| `poseRefitAngle` | `float` | Hand rotation change in degrees needed before recalculating finger fit, unless the position threshold is already exceeded. Lower values follow small movements more accurately but refit more often. | `2`; Minimum: 0 | Adaptive Hand Grip > Pose Refit Angle |
| `poseRefitDistance` | `float` | Ignore small physical wrist compliance instead of repeatedly re-optimizing finger curls. | `.003`; Minimum: 0 | Adaptive Hand Grip > Pose Refit Distance |
| `refitFingersPerFrame` | `int` | Maximum fingers whose contact fit is recalculated in one frame. Lower values spread the work but take more frames to finish a new grip; 5 can update the whole hand together. | `2`; Range: 1 to 5 | Adaptive Hand Grip > Refit Fingers Per Frame |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` | Adaptive Hand Grip > Show Gizmos |
| `wheel` | `SteeringWheelHandle` ([fields](World.md#steeringwheelhandle)) | Steering-wheel surface used to fit this hand's fingers around the rim. For non-wheel grips the general Handle reference supplies the contact instead. | `None / unassigned` | Adaptive Hand Grip > Wheel |

## AdaptiveHandGrip.Finger

[Grip solving](../API/GripSolving.md)

**Source:** `Runtime/World/Passengers/IK/AdaptiveHandGrip.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `bones` | `Transform[]` | Three finger bones in order from the palm toward the fingertip. The fitter rotates this chain to wrap the finger around the handle surface. | `new Transform[3]` | Adaptive Hand Grip > Bones |
| `flexionAxes` | `Vector3[]` | Local bending axes for the finger joints, in bone order. | `new Vector3[3]` | Adaptive Hand Grip > Flexion Axes |
| `maximumFlexion` | `Vector3` | Maximum finger-joint flexion angles in degrees for the proximal, intermediate and distal joints. | `new Vector3(85, 110, 80)` | Adaptive Hand Grip > Maximum Flexion |
| `name` | `string` | Readable finger label used to identify this calibration entry, such as Thumb or Index. Bone assignments and calibration determine the actual motion. | `None / unassigned` | Adaptive Hand Grip > Name |
| `openRotations` | `Quaternion[]` | Reference local rotations for the open finger joints, in bone order. | `new Quaternion[3]` | Adaptive Hand Grip > Open Rotations |
| `oppositionAxis` | `Vector3` | Local rotation axis used to move the thumb across the palm toward the grip. Set it to the thumb model's opposition direction rather than its curl axis. | `Zero-initialized Vector3` | Adaptive Hand Grip > Opposition Axis |
| `padRadius` | `float` | Radius in metres representing the finger pad around the sampled finger shape. A larger pad keeps the bones farther from the grip surface and avoids visible penetration. | `.006`; Minimum: .001f | Adaptive Hand Grip > Pad Radius |
| `spreadAxis` | `Vector3` | Local rotation axis used to spread or bring together this finger at its base. Calibrate it to the finger bone's actual orientation. | `Zero-initialized Vector3` | Adaptive Hand Grip > Spread Axis |
| `thumb` | `bool` | Uses thumb-specific opposition/spread fitting instead of ordinary finger bending. | `false` | Adaptive Hand Grip > Thumb |
| `tipOffset` | `Vector3` | Offset from the last finger bone to the fingertip in that bone's local coordinates. Set it at the visible tip so contact fitting uses the finger's real length. | `Zero-initialized Vector3` | Adaptive Hand Grip > Tip Offset |

## AnchorHandle

Exposes authored hand/foot anchors without control animation.

**Source:** `Runtime/World/Passengers/IK/Handle/AnchorHandle.cs`. Component / asset.

**Inherited settings:** [VehicleHandle](World.md#vehiclehandle). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `anchor` | `Transform` | Palm/ankle contact. Use a stationary grip frame for Closure Change. | `None / unassigned` | Anchor Handle > Anchor |
| `closedDistance` | `float` | Distance in metres at full additional closure when multiplier is 1. | `0.03`; minimum 0 | Anchor Handle > Behaviour > Closed Distance |
| `closureAngles` | `Vector3` | Additional base/middle/tip flexion in degrees for the four fingers; excludes thumb. | `(20, 35, 25)` | Anchor Handle > Behaviour > Closure Angles |
| `closureMultiplier` | `float` | Scales normalized closure before clamping to 0–1. | `1`; minimum 0 | Anchor Handle > Behaviour > Closure Multiplier |
| `controlAnchor` | `Transform` | Moving lever contact measured against Anchor in Closure Change. | `None / unassigned` | Anchor Handle > Behaviour > Control Anchor |
| `followAnchorRotation` | `bool` | When false, resolved contact rotation stays in the vehicle frame while position follows the anchor. | `true` | Anchor Handle > Behaviour > Follow Anchor Rotation |
| `mode` | `AnchorHandleMode` | Follow the anchor normally, or use ClosureChange to add four-finger flexion from control distance. Requires Adaptive Grip for finger closure. | `Follow` | Anchor Handle > Behaviour > Mode |
| `openDistance` | `float` | World-space distance in metres at zero additional closure. Must exceed Closed Distance. | `0.06`; minimum 0.0001 | Anchor Handle > Behaviour > Open Distance |

## BalanceRider

**Source:** `Runtime/World/Passengers/Seats/BalanceRider.cs`. Component.

| Field | Type | Purpose | Initial value |
| --- | --- | --- | --- |
| `ejectOnExternalImpact` | `bool` | Eject on a strong collision with an external dynamic body, regardless of which vehicle is controlled. | `true` |
| `minimumExternalImpactSpeed` | `float` | Minimum normal contact speed in m/s. | `4` |
| `minimumExternalImpactVelocityChange` | `float` | Minimum collision impulse divided by chassis mass, in m/s. Both thresholds must pass. | `1.5` |
| `externalImpactBalanceDuration` | `float` | Seconds to suspend MotorcycleBalance after impact ejection. Driver-ejection policy may keep it off longer. | `1.5` |
| `reverseMode` | `RiderReverseMode` | Reverse Gear keeps normal transmission behavior. Foot Pushing selects neutral and uses bounded human-effort wheel torque while an occupied driver can reach the ground. | `default` |
| `footReverseSpeed` | `float` | Maximum foot-propelled reverse speed in metres per second. | `1.3f` |
| `footPushTorque` | `float` | Total backward wheel torque in Nm representing the driver's foot pushes, independent of engine power. | `160` |
| `footReverseEngageSpeed` | `float` | Maximum ground speed in m/s for starting foot pushing. Sideways or backward coasting must finish braking first. | `.15f` |
| `footStepPeriod` | `float` | Maximum seconds for a full left/right pair of steps; shortens at higher reverse speed to keep planted feet within reach. Shared by physical targets and animation signals. | `1.2f` |
| `allowFootPushing` | `bool` | Let this occupied driver provide ground foot targets and provide foot propulsion in Foot Pushing mode with any wheel-driven profile. Passengers never propel the vehicle. | `true` |
| `pushFeet` | `RiderPushFeet` | Both alternates the feet. Left or Right lets a scooter keep the other foot on its riding/deck target. Disabled prevents foot propulsion. | `RiderPushFeet.Both` |
| `footStepDistance` | `float` | Recovery step distance in metres, relative to the ground pose. | `.35f` |
| `footStartBlendTime` | `float` | Seconds to blend from the current supported foot pose into the walking gait. Zero starts immediately. | `.12f` |
| `footMotionSmoothTime` | `float` | Seconds to smooth physical walking targets between steps and over changing terrain. Zero disables target smoothing. | `.06f` |
| `footGroundSmoothTime` | `float` | Seconds to smooth the shared wheel support plane on uneven ground, using existing wheel contacts. Zero disables smoothing. | `.08f` |
| `footStepHeight` | `float` | Foot lift in metres during the recovery part of each step. | `.1f` |
| `useWheelGroundPlane` | `bool` | Project walking targets onto the existing wheel support plane, without additional raycasts. | `true` |
| `footGroundClearance` | `float` | Ankle offset above the sampled ground plane in metres. | `.08f` |
| `motorcycleProfileOnly` | `bool` | Run this rider behaviour only while the vehicle uses MotorcycleProfile. Disable to use it with another drive profile. | `false` |
| `leftFootMode` | `RiderFootMode` | How each foot uses Ground/Riding poses. Unchanged leaves the Seat binding alone; Riding can follow a moving pedal or scooter deck anchor. | `default` |
| `rightFootMode` | `RiderFootMode` | Right-foot pose policy, independent of the left foot. Unchanged preserves the Seat binding. | `default` |
| `blendSource` | `RiderBlendSource` | Speed uses vehicle speed magnitude. Manual uses Manual Riding Blend, which your input/animation code can update. | `default` |
| `manualRidingBlend` | `float` | Requested transition from Ground (0) to Riding (1) when Blend Source is Manual. | `default` |
| `supportBalance` | `bool` | Apply bounded pelvis torque toward the seat-forward stance. Supports the rider only; does not balance the vehicle or animate bicycle pedalling. | `default` |
| `forwardLean` | `float` | Desired forward lean relative to the Seat frame. Positive leans forward; negative leans backward. | `default` |
| `steeringLean` | `float` | Additional rider lean into commanded steering at full input. Negative reverses lean direction. Zero disables turn lean. | `default` |
| `balanceSpring` | `float` | Pelvis support stiffness in Nm/rad. | `250` |
| `balanceDamper` | `float` | Damping relative to the chassis in Nm per rad/s. | `25` |
| `maximumBalanceTorque` | `float` | Maximum artificial pelvis torque in Nm. Zero applies no torque. | `120` |
| `leftFootGround` | `Transform` | Left-foot target used while stopped or moving slowly. | `default` |
| `rightFootGround` | `Transform` | Right-foot target used while stopped or moving slowly. | `default` |
| `leftFootRiding` | `Transform` | Left-foot target used in the riding pose. | `default` |
| `rightFootRiding` | `Transform` | Right-foot target used in the riding pose. | `default` |
| `liftStartsAtKph` | `float` | Speed in kilometres per hour at which the feet start blending from the ground pose to the riding pose. | `1` |
| `fullyRaisedAtKph` | `float` | Speed in kilometres per hour at which both feet reach the riding pose. | `8` |
| `blendSpeed` | `float` | Response of foot-target blending. Higher values move the targets more quickly. | `4` |
| `onMotionUpdated` | `UnityEvent<RiderMotionState>` | Current motion state after rider targets update. Suitable for custom animation integrations. | `new UnityEvent<RiderMotionState>()` |
| `onFootPushingChanged` | `UnityEvent<bool>` | Foot propulsion begins or stops; false is also published on disable or loss of occupancy. | `new UnityEvent<bool>()` |
| `onFootPlanted` | `UnityEvent<PassengerBodyPart>` | A foot starts its planted phase. The two feet alternate while pushing backward. | `new UnityEvent<PassengerBodyPart>()` |

## CameraModule

Base class for a Cameras submodule. Cameras renders its selected enabled submodule once per frame.

**Source:** `Runtime/World/Camera/CameraModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `active` | `bool` | Activate this view after assigning a camera. Inactive views never move the camera or change its lens. | `false` |
| `anchor` | `Transform` | Explicit position and rotation reference. If unassigned, the vehicle root is used. | `None / unassigned` |
| `requirePointerLock` | `bool` | Only read mouse movement while the cursor is locked. Your game controls cursor capture. | `false` |
| `sensitivity` | `float` | Degrees of camera look change per mouse-delta unit. Increase for faster mouse looking; decrease for finer aim around the same allowed view range. | `.15` |

## Cameras

Optional vehicle camera owner. It moves an explicitly assigned camera only while the selected submodule is Active. It releases ownership when inactive, detached or disabled.

**Source:** `Runtime/World/Camera/Cameras.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `customModule` | `CameraModule` ([fields](World.md#cameramodule)) | Selected custom CameraModule on this GameObject. Used when mode is Custom. | `None / unassigned` |
| `enableControls` | `bool` | Allows the camera system to process look/zoom input. Use SetControlsEnabled(false) from code to disable controls and clear pending input immediately. | `true` |
| `mode` | `ViewMode` | Orbit uses the exterior orbit module; Interior uses the cabin module; Custom uses Custom Module. Selecting a mode changes which module controls the assigned view camera. Options: `Orbit`, `Interior`, `Custom`. | `Orbit` |
| `readMouseInput` | `bool` | Reads mouse movement/scroll for look and zoom. Turn off when another input adapter calls the camera API, so mouse input is not also added. | `true` |
| `viewCamera` | `Camera` | Optional camera to control. Leave empty when using your own camera system. | `None / unassigned` |

## ControlHandle

**Source:** `Runtime/World/Passengers/IK/Handle/ControlHandle.cs`. Shared IK contact for an animated control. Inherits AnchorHandle; supplies limb permissions, palm/finger poses and a reference to the controlling animator. It never moves the control model.

**Inherited settings:** `AnchorHandle`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `animator` | `ControlAnimator` | Visual controller paired with this IK contact. Its InteractionValue is observed for generic contact value events; the handle never writes control geometry. | Control Handle > Animator |

## Coupler

Validates and owns one hitch relationship, joint and changed collision pairs.

**Source:** `Runtime/World/Towing/Coupler.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `allowJointBreak` | `bool` | Allow physical forces to break the hitch. Disable for an unbreakable connection. | `true` |
| `attachDistance` | `float` | Maximum separation in metres between the towing hitch and trailer hitch for attachment. Increase to allow coupling from farther away. | `1.2`; Minimum: .05f |
| `attachmentAlignmentTime` | `float` | Seconds to bring accepted nearby hitches together without an instantaneous correction impulse. | `1.5`; Minimum: .05f |
| `attachOnStart` | `bool` | Attach Initial Trailer at startup. Manual TryAttach remains available when disabled. | `true` |
| `breakForce` | `float` | Force in newtons above which the native hitch joint may break when Allow Joint Break is on. Increase for a stronger coupling; turn breaking off for an unbreakable joint. | `200000`; Minimum: 0 |
| `breakTorque` | `float` | Torque in N·m above which the hitch joint may break when Allow Joint Break is on. Lower values let severe twisting separate the trailer sooner. | `200000`; Minimum: 0 |
| `hitch` | `Transform` | World-space coupling point used to align the trailer connection. | `None / unassigned` |
| `initialTrailer` | `Trailer` ([fields](World.md#trailer)) | Trailer to attach at startup when Attach On Start is enabled. It must still satisfy hitch distance and normal attachment eligibility checks. | `None / unassigned` |
| `longitudinalDamper` | `float` | Fore/aft hitch damping in N·s/m. | `50000`; Minimum: 0 |
| `longitudinalSpring` | `float` | Fore/aft hitch stiffness in N/m. A compliant drawbar prevents parked tire constraints from fighting a perfectly rigid longitudinal lock. | `1000000`; Minimum: 1 |
| `pitchLimit` | `float` | Maximum hitch pitch articulation in degrees. | `30`; Range: 1 to 80 |
| `rollLimit` | `float` | Maximum hitch roll articulation in degrees. | `20`; Range: 1 to 80 |
| `vehicle` | `VehicleController` ([fields](Controller.md#vehiclecontroller)) | Towing vehicle whose Rigidbody receives the hitch connection and supplies commands to the trailer. If empty, the component looks on the same GameObject. | `None / unassigned` |

## CustomPassengerBody

Minimal body for application-owned Custom occupancy.

**Source:** `Runtime/World/Passengers/Bodies/CustomPassengerBody.cs`. Component / asset.

**Inherited settings:** [PassengerBody](World.md#passengerbody). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## DroppableObject

Detaches the actual payload and establishes released physics.

**Source:** `Runtime/World/Weapons/DroppableObject.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `inheritVelocity` | `bool` | Retains the carrier's point velocity when releasing this payload. | `true` |
| `localReleaseVelocity` | `Vector3` | Optional separation velocity in this object's local axes, in metres per second. | `Zero-initialized Vector3` |
| `mass` | `float` | Mass in kilograms of the released payload. It affects inertia and collision response after the object separates from its carrier. | `10`; Minimum: .01f |

## GearLeverHandle

**Source:** `Runtime/World/Passengers/IK/Handle/GearLeverHandle.cs`. IK-only palm contact on a gear lever. Inherits ControlHandle; default authoring selects the right hand.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## GearPaddleHandle

**Source:** `Runtime/World/Passengers/IK/Handle/GearPaddleHandle.cs`. IK-only palm contact on a moving gear paddle. Inherits ControlHandle; choose allowed limb, occupant and reach/return timing here.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## HandGrip

Stores character hand frames and fallback finger poses.

**Source:** `Runtime/World/Passengers/IK/HandGrip.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `angularDamper` | `float` | Damping of wrist rotation for an external grip. Increase to reduce wobble around the target palm orientation; ordinary handles can supply their own damping. | `35`; Minimum: 0 | Hand Grip > Angular Damper |
| `angularSpring` | `float` | Strength pulling an externally driven physical wrist toward the grip orientation. Higher values hold the palm angle more firmly; an ordinary VehicleHandle can supply its own wrist drive settings instead. | `1200`; Minimum: 0 | Hand Grip > Angular Spring |
| `contactPoint` | `Transform` | Palm-contact marker on the hand, separate from the wrist bone origin. Its position and orientation are aligned to the target grip so the palm touches the handle correctly. | `None / unassigned` | Hand Grip > Contact Point |
| `fingers` | `FingerPose[]` ([fields](World.md#handgripfingerpose)) | Finger-bone pose entries switched between relaxed and gripping rotations. Add each bone that should change when the hand grips or releases. | `Empty list` | Hand Grip > Fingers |
| `maximumTorque` | `float` | Maximum wrist-orientation torque in N·m for an external grip. Lower values let the palm yield under load even with a strong angular spring. | `250`; Minimum: 0 | Hand Grip > Maximum Torque |

## HandGrip.FingerPose

Value data for finger pose; its fields are listed below.

**Source:** `Runtime/World/Passengers/IK/HandGrip.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `bone` | `Transform` | Individual finger bone receiving the configured grip or relaxed local rotation. Add multiple entries to pose a full finger chain. | `None / unassigned` | Hand Grip > Bone |
| `gripRotation` | `Quaternion` | Bone's local rotation when the hand grips. Adjust each finger bone so the closed hand wraps around the intended control. | `Zero-initialized Quaternion` | Hand Grip > Grip Rotation |
| `relaxedRotation` | `Quaternion` | Bone's local rotation when the hand is not gripping. Set it to the finger's natural open/resting pose. | `Zero-initialized Quaternion` | Hand Grip > Relaxed Rotation |

## HandleAnimatorBinding

**Source:** `Runtime/World/Passengers/IK/Handle/Core/HandleAnimatorBinding.cs`. Component binding for animation/Timeline and handle feedback.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `animator` | `Animator` | Optional Animator receiving configured output parameters. | Unassigned | Handle Animator Binding > Animator |
| `changingParameter` | `string` | Optional Animator bool receiving IsValueChanging. | Unassigned | Handle Animator Binding > Changing Parameter |
| `contactParameter` | `string` | Optional Animator bool receiving this occupant last sampled contact state. | Unassigned | Handle Animator Binding > Contact Parameter |
| `contactTransform` | `Transform` | Application palm/fingertip frame overriding automatic contact tracking while this binding applies. | Unassigned | Handle Animator Binding > Contact Transform |
| `drivePoseWeights` | `bool` | Write configured pose weights to the resolved handle each Apply. | `true` | Handle Animator Binding > Drive Pose Weights |
| `driveTargetOverride` | `bool` | Write Target Override on Apply, including clearing it when unassigned. | `false` | Handle Animator Binding > Drive Target Override |
| `fingerWeight` | `float` | Finger overlay weight. | `1`; range 0–1 | Handle Animator Binding > Finger Weight |
| `handle` | `VehicleHandle` | Explicit handle; empty resolves the selected seat limb current handle, including transfers/selectors. | Unassigned | Handle Animator Binding > Handle |
| `part` | `PassengerBodyPart` | Seat limb controlled by this binding. | `RightHand` | Handle Animator Binding > Part |
| `physicalWeight` | `float` | Independent physical palm support weight. | `1`; range 0–1 | Handle Animator Binding > Physical Weight |
| `positionWeight` | `float` | Position overlay weight. | `1`; range 0–1 | Handle Animator Binding > Position Weight |
| `rotationWeight` | `float` | Rotation overlay weight. | `1`; range 0–1 | Handle Animator Binding > Rotation Weight |
| `seat` | `PassengerSeat` | Seat supplying the selected occupant/limb and contact state. | Unassigned | Handle Animator Binding > Seat |
| `targetOverride` | `Transform` | World-space pose target written when Drive Target Override is enabled. | Unassigned | Handle Animator Binding > Target Override |
| `valueParameter` | `string` | Optional Animator float receiving InteractionValue.x. | Unassigned | Handle Animator Binding > Value Parameter |

## HandleFingerPosition

| Setting | Type | Default | Description | Inspector path |
| --- | --- | --- | --- | --- |
| `baseRotation` / `middleRotation` / `tipRotation` | `Vector3` | Zero | Additional XYZ segment rotation; each axis has a degree slider. | Handle Finger Position > Base Rotation |
| `closure` | `float` | `1`; Range: 0–1 | Saved per-finger helper value. Auto-apply closure controls whether moving it rewrites the pose. Ignored by gameplay. | Handle Finger Position > Closure |
| `curlAngles` | `Vector3` | `(85, 110, 80)` | Signed base/middle/tip flexion about the selected axis, bounded anatomically; thumb Middle/Tip follow the Base hinge. | Handle Finger Position > Curl Angles |
| `curlAxis` | `HandleCurlAxis` | `Default` | Independent thumb Base hinge; Default uses mirrored Base Z. Middle/Tip derive axes through their neutral rotations. Non-thumb fingers use the hand-level selector. | Handle Finger Position > Curl Axis |
| `surfaceFit` | `float` | `1`; Range: 0–1 | Blend from authored curl to adaptive surface IK fit. | Handle Finger Position > Surface Fit |

## HandleHandPose

| Setting | Type | Default | Description | Inspector path |
| --- | --- | --- | --- | --- |
| `closure` | `float` | `1`; Range: 0–1 | Saved four-finger editor helper value; excludes the thumb. Applies pose changes only with Auto-apply closure enabled. Ignored by gameplay. | Handle Hand Pose > Closure |
| `constrainThumbToRim` | `bool` | `false` | Enable wheel pinch contact constraints. | Handle Hand Pose > Constrain Thumb To Rim |
| `curlAxis` | `HandleCurlAxis` | `Default` | Shared curl axis for the four non-thumb fingers: calibrated flexion by default or explicit X/Y/Z. | Handle Hand Pose > Curl Axis |
| `maximumFingerSpeed` | `float` | `300` | Maximum finger rotation speed for pose changes within one bound handle, degrees per second. Cross-handle transitions use Finger Blend Duration. | Handle Hand Pose > Maximum Finger Speed |
| `position` / `rotation` | `Vector3` | Zero | Anchor-local palm offset in metres and XYZ degrees; rotation has per-axis sliders. | Handle Hand Pose > Position |
| `thumb` / `index` / `middle` / `ring` / `little` | `HandleFingerPosition` | New finger | Five independently configurable fingers. | Handle Hand Pose > Thumb |
| `thumbAim` | `HandleThumbAim` | `SurfaceFit` | Surface fit, palm-forward or index-direction thumb aiming. | Handle Hand Pose > Thumb Aim |
| `thumbAimLimit` | `float` | `100`; Range: 0–180 | Maximum calibrated thumb base aim rotation. | Handle Hand Pose > Thumb Aim Limit |
| `thumbBaseCone` | `float` | `50` | Surface-fitting thumb base cone limit. | Handle Hand Pose > Thumb Base Cone |
| `thumbDepthRatio` / `thumbInwardRatio` | `float` | `.8` / `.25`; Range: 0–2 | Minimum thumb-tip distance ratios relative to rim depth/radius. | Handle Hand Pose > Thumb Depth Ratio |
| `thumbInwardAngle` | `float` | `0`; Range: 0–60 | Extra thumb aim towards wheel centre. | Handle Hand Pose > Thumb Inward Angle |
| `thumbOppositionLimit` | `float` | `12` | Surface-fitting thumb opposition limit. | Handle Hand Pose > Thumb Opposition Limit |
| `thumbSpreadLimit` | `float` | `5` | Surface-fitting thumb spread limit. | Handle Hand Pose > Thumb Spread Limit |

## HandleHandPosition

Reusable named position on every VehicleHandle. The Inspector supplies Copy/Paste, Save-as-asset and Make-local controls.

| Setting | Type | Default | Description | Inspector path |
| --- | --- | --- | --- | --- |
| `autoApplyClosure` | `bool` | `true` | Editor-only local setting. When false, Closure edits save only their own helper value. A linked preset supplies its own setting instead. | Handle Hand Position > Auto Apply Closure |
| `left` / `right` | `HandleHandPose` | New pose | Independent local hand data when no shared asset is assigned. | Handle Hand Position > Left |
| `name` | `string` | `Grip` | Display name in position selectors. | Handle Hand Position > Name |
| `preset` | `HandleHandPositionProfile` | Unassigned | Shared left/right data and Auto-apply closure setting. The Inspector labels shared hand sections with the position name. | Handle Hand Position > Preset |

## HandleHandPositionProfile

ScriptableObject created with **Create > UltraVehicleSystem > Controls > Hand Position Profile**. Its `left` and `right` HandleHandPose blocks are shared by every referencing handle; **Local** makes an independent copy. See [Reusable hand positions](../HandPositions.md).

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `autoApplyClosure` | `bool` | `true` | Shared editor-only checkbox below the preset information box. When false, Closure sliders save only their own helper values. | Handle Hand Position Profile > Auto Apply Closure |
| `left` | `Wheel` ([fields](Physics.md#wheel)) | Left Wheel on this axle. Its suspension compression is compared with Right to calculate the force opposing body roll. | `None / unassigned` | Handle Hand Position Profile > Left |
| `right` | `Wheel` ([fields](Physics.md#wheel)) | Right Wheel on this axle. Assign its matching left wheel in Left; both wheels must be operational and grounded for this axle's anti-roll force. | `None / unassigned` | Handle Hand Position Profile > Right |

## HandlePoseSettings

**Source:** `Runtime/World/Passengers/IK/Handle/Core/HandleInteraction.cs`. Referenced configuration block; expand its owning field.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `contactAngle` | `float` | Maximum orientation difference in degrees for automatic contact. | `180`; range 0–180 | [Handle component] > Limb IK, animation and contact > [limb] Pose > Contact Angle |
| `contactDistance` | `float` | Contact acquisition distance in metres. | `0.03`; minimum 0 | [Handle component] > Limb IK, animation and contact > [limb] Pose > Contact Distance |
| `contactSource` | `HandleContactSource` | Automatic samples contact distance/angle; Manual uses application-reported contact. | `Automatic` | [Handle component] > Limb IK, animation and contact > [limb] Pose > Contact Source |
| `fingerWeight` | `float` | Finger pose overlay weight. | `1`; range 0–1 | [Handle component] > Limb IK, animation and contact > [limb] Pose > Finger Weight |
| `physicalWeight` | `float` | Independent physical palm support weight. Zero releases the palm constraint while retaining ragdoll anatomy. | `1`; range 0–1 | [Handle component] > Limb IK, animation and contact > [limb] Pose > Physical Weight |
| `positionWeight` | `float` | Limb position overlay weight. | `1`; range 0–1 | [Handle component] > Limb IK, animation and contact > [limb] Pose > Position Weight |
| `releaseDistance` | `float` | Larger release distance adds hysteresis to contact events. | `0.05`; minimum 0 | [Handle component] > Limb IK, animation and contact > [limb] Pose > Release Distance |
| `rotationWeight` | `float` | Limb rotation overlay weight. | `1`; range 0–1 | [Handle component] > Limb IK, animation and contact > [limb] Pose > Rotation Weight |
| `targetOverride` | `Transform` | Optional final world-space IK target supplied by animation, Timeline or application code. | Unassigned | [Handle component] > Limb IK, animation and contact > [limb] Pose > Target Override |

## HandleUseSettings

**Source:** `Runtime/World/Passengers/IK/Handle/Core/HandleUseSettings.cs`. Referenced settings on every VehicleHandle.

| Setting | Meaning | Inspector path |
| --- | --- | --- |
| `allowOtherLimbs` | If the preferred limb is unavailable, try other allowed limbs in left hand, right hand, left foot, right foot order. | [Handle component] > Actions > Allow Other Limbs |
| `allowUnsupportedDeparture` | Default false. Allows departure even when the source would fall below Minimum Attachments. Independent of priority; does not cancel another limb's request. | [Handle component] > Actions > Allow Unsupported Departure |
| `input` | Command channel observed when Source is Command. Signed axes use their absolute magnitude. | [Handle component] > Actions > Input |
| `interruptLowerPriority` | Default false. Allows strictly higher-priority timed requests to interrupt timed ownership on the same limb; persistent and Animator ownership remain protected. | [Handle component] > Actions > Interrupt Lower Priority |
| `liftHeight` | Clearance arc height in metres along vehicle-local up during each trip. Zero follows a straight path. | [Handle component] > Actions > Lift Height |
| `preferredLimb` | First limb attempted for automatic actions and TryUse(seat, target). It must also be enabled in Allowed limbs. | [Handle component] > Actions > Preferred Limb |
| `priority` | Higher values try first for simultaneous automatic requests. Interruption additionally requires Interrupt Lower Priority. | [Handle component] > Actions > Priority |
| `releaseDuration` | Seconds used to release physical hand contact before each trip. Guidance remains active. | [Handle component] > Actions > Release Duration |
| `releaseThreshold` | Lower action release threshold used while this rule owns a token, preventing chatter near the activation point. | [Handle component] > Actions > Release Threshold |
| `returnDelay` | Seconds held at the destination after arrival or the last active automatic action before return starts. | [Handle component] > Actions > Return Delay |
| `returnDuration` | Seconds to return to the original handle or anchor. Independent of outbound travel; zero completes on the next controller step. | [Handle component] > Actions > Return Duration |
| `seat` | Explicit seat whose occupant may use this control. | [Handle component] > Actions > Seat |
| `source` | ValueChange observes handle value events; Command reads the selected command channel; ServiceBrake reads resolved service braking. | [Handle component] > Actions > Source |
| `threshold` | Action activation magnitude. Larger values require more input before requesting a limb. | [Handle component] > Actions > Threshold |
| `travelDuration` | Seconds to reach the handle (Outbound Duration). Independent of returnDuration; zero reaches the endpoint on the next controller step. | [Handle component] > Actions > Outbound Duration |
| `useOnAction` | Request the configured seat limb while this action is active. | [Handle component] > Actions > Use On Action |




## HumanoidAccessMotion

Character root component. **Humanoid Access Motion > Default Profile / Seated Pose Controller** are top-level fields. Assign this component to **Passenger Access > Motion**.

Built-in Animator-based humanoid access implementation.

**Source:** `Runtime/World/Passengers/Access/HumanoidAccessMotion.cs`. Component / asset.

**Inherited settings:** [AccessMotion](World.md#accessmotion). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `defaultProfile` | `AccessAnimationProfile` ([fields](World.md#accessanimationprofile)) | Fallback profile; a SeatAccess profile takes precedence for each request. | `None / unassigned` | Humanoid Access Motion > Default Profile |
| `seatedPoseController` | `RuntimeAnimatorController` | Optional controller sampled for the actual Animator/Animator + IK seated destination and restored after entry, including steering hands. Match the controller used after seating. Null retains the IK/reference target. | `None / unassigned` | Humanoid Access Motion > Seated Pose Controller |

## HumanoidIK

Bone mapping is at component top. **Humanoid IK > Match Target Rotation** is above **Auto-fill**, together with the other settings.

Uses character frames to resolve limb targets.

**Source:** `Runtime/World/Passengers/IK/HumanoidIK.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `leftElbowHint` | `Transform` | Left side: Optional marker choosing which way the elbow bends when reaching. Move it to the desired elbow side to avoid an unnatural arm fold. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Left Elbow Hint |
| `leftFoot` | `Transform` | Left side: Ankle/foot bone placed at the seat or pedal target. Its rotation can also follow the configured foot contact. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Left Foot |
| `leftHand` | `Transform` | Left side: Wrist/hand bone placed at the palm target. HandGrip can offset this bone so the visible palm, rather than the wrist origin, touches the control. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Left Hand |
| `leftLowerArm` | `Transform` | Left side: Forearm bone at the elbow; bends the arm so the wrist can reach its target within the joint limits. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Left Lower Arm |
| `leftLowerLeg` | `Transform` | Left side: Shin bone at the knee; bends the leg between the hip and the foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Left Lower Leg |
| `leftUpperArm` | `Transform` | Left side: Upper-arm bone at the shoulder; starts the two-bone arm solve toward the hand target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Left Upper Arm |
| `leftUpperLeg` | `Transform` | Left side: Thigh bone at the hip; starts the leg solve toward the configured foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Left Upper Leg |
| `matchTargetRotation` | `bool` | Also aligns solved hand/foot orientation with the target where that solver path supports it. Turn off when IK should reach the target position while retaining its existing end-bone orientation. | `false` | Humanoid IK > Match Target Rotation |
| `maximumForearmRoll` | `float` | Forearm roll for standalone IK without passenger anatomy. Passenger rigs use the saved elbow twist range instead. | `80`; Range: 0 to 90 | Humanoid IK > Maximum Forearm Roll |
| `rightElbowHint` | `Transform` | Right side: Optional marker choosing which way the elbow bends when reaching. Move it to the desired elbow side to avoid an unnatural arm fold. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Right Elbow Hint |
| `rightFoot` | `Transform` | Right side: Ankle/foot bone placed at the seat or pedal target. Its rotation can also follow the configured foot contact. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Right Foot |
| `rightHand` | `Transform` | Right side: Wrist/hand bone placed at the palm target. HandGrip can offset this bone so the visible palm, rather than the wrist origin, touches the control. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Right Hand |
| `rightLowerArm` | `Transform` | Right side: Forearm bone at the elbow; bends the arm so the wrist can reach its target within the joint limits. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Right Lower Arm |
| `rightLowerLeg` | `Transform` | Right side: Shin bone at the knee; bends the leg between the hip and the foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Right Lower Leg |
| `rightUpperArm` | `Transform` | Right side: Upper-arm bone at the shoulder; starts the two-bone arm solve toward the hand target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Right Upper Arm |
| `rightUpperLeg` | `Transform` | Right side: Thigh bone at the hip; starts the leg solve toward the configured foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` | Humanoid IK > Right Upper Leg |

## HumanoidJointDefinition

Saved native joint reference with neutral-frame/flexion metadata used by passenger physics and IK.

**Source:** `Runtime/World/Passengers/Physics/HumanoidJointLimits.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `connectedReferenceRotation` | `Quaternion` | Reference connected body rotation relative to the passenger root. | `Quaternion.identity` | Humanoid Passenger > Anatomical Joints > [Joint Id or Element N] > Connected Reference Rotation |
| `joint` | `ConfigurableJoint` | Saved `ConfigurableJoint` supplying native axes, anchors, connections and angular limits. | `None / unassigned` | Humanoid Passenger > Anatomical Joints > [Joint Id or Element N] > Joint |
| `jointId` | `string` | Unique, case-sensitive identifier used by HumanoidPassenger anatomical joint lookup/update APIs. Generated from the connected bones during authoring; freely editable. | `None / unassigned` | Humanoid Passenger > Anatomical Joints > [Joint Id or Element N] > Joint Id |
| `referenceFlexion` | `float` | Joint bend in degrees corresponding to the captured reference pose. The IK hinge solver uses this offset to interpret native joint limits correctly; it does not widen those limits. | `0` | Humanoid Passenger > Anatomical Joints > [Joint Id or Element N] > Reference Flexion |
| `referenceRotation` | `Quaternion` | Reference body rotation relative to the passenger root. | `Quaternion.identity` | Humanoid Passenger > Anatomical Joints > [Joint Id or Element N] > Reference Rotation |

## HumanoidPassenger

Character root component. **Humanoid Passenger > Free Ragdoll > [setting]** contains all free-ragdoll tuning fields. **Anatomical Joints > [Joint Id or Element N] > [setting]** names items from nonempty Joint Id. Existing assignments survive Auto-fill.

Connects humanoid rig, pose and physical passenger behavior.

**Source:** `Runtime/World/Passengers/Bodies/HumanoidPassenger.cs`. Component / asset.

**Inherited settings:** [PassengerBody](World.md#passengerbody). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `anatomicalJoints` | `HumanoidJointDefinition[]` ([fields](World.md#humanoidjointdefinition)) | Skeletal joint definitions used to read the body's actual axes, reference pose and bend limits. Edit physical limits on each referenced ConfigurableJoint; this list connects them to the passenger solver. | `System.Array.Empty<HumanoidJointDefinition>()` | Humanoid Passenger > Anatomical Joints |
| `animator` | `Animator` | Character Animator providing humanoid bone mapping and animated poses. A valid humanoid avatar lets setup locate the skeleton for IK and hand animation/physics transitions. | `None / unassigned` | Humanoid Passenger > Animator |
| `automaticSeatedIK` | `bool` | Apply the Animator + IK overlay in LateUpdate. Disable to call SolveSeatedIK from your own animation pipeline. | `true` | Humanoid Passenger > Automatic Seated IK |
| `exitCollisionClearance` | `float` | Keep the previous vehicle excluded until the departing character clears its combined collider bounds by this distance. Prevents animated kinematic limbs from blocking the doors/chassis. | `.25`; Minimum: 0 | Humanoid Passenger > Exit Collision Clearance |
| `freeRagdollAngularDamping` | `float` | Passive rotational damping while falling or lying down. Does not hold a pose or freeze bones. | `1.5`; Minimum: 0 | Humanoid Passenger > Free Ragdoll > Angular Damping |
| `freeRagdollCollisionDetection` | `CollisionDetectionMode` | Collision detection used by released ragdoll bodies. Continuous Dynamic prevents fast limbs from stepping through the ground before contact is resolved. The previous mode is restored on attachment. | `CollisionDetectionMode.ContinuousDynamic` | Humanoid Passenger > Free Ragdoll > Collision Detection |
| `freeRagdollInertiaScale` | `float` | Rotational inertia multiplier for released bones. Reduces abrupt limb rotation from ground impulses without changing body mass, gravity or linear momentum. Restored on attachment. | `4`; Minimum: 1 | Humanoid Passenger > Free Ragdoll > Inertia Scale |
| `freeRagdollJointDamping` | `float` | Passive damping of relative bone rotation. The pose spring stays zero, so joints never return to a riding/idle pose. | `1`; Minimum: 0 | Humanoid Passenger > Free Ragdoll > Joint Damping |
| `freeRagdollMaximumAngularSpeed` | `float` | Maximum angular speed in radians/second for released bones. Preserves lower per-body limits and restores the previous limit on attachment. | `18`; Minimum: 0.1 | Humanoid Passenger > Free Ragdoll > Maximum Angular Speed |
| `freeRagdollMaximumDampingTorque` | `float` | Maximum stabilizing torque in N·m for each free-ragdoll joint's relative-motion damping. Increase to resist violent limb spin more strongly; it does not pull the body back into a seated pose. | `20`; Minimum: 0 | Humanoid Passenger > Free Ragdoll > Maximum Damping Torque |
| `freeRagdollMaximumDepenetrationVelocity` | `float` | Maximum separation speed in m/s for overlapping free-ragdoll colliders. Caps abrupt push-out after contact while preserving ordinary flight and rolling velocity. Lower per-body limits are preserved, and previous limits return on attachment. | `3`; Minimum: 0.01 | Humanoid Passenger > Free Ragdoll > Maximum Depenetration Velocity |
| `freeRagdollPreprocessing` | `bool` | Enable joint preprocessing for free ragdolls. Leave off when impacts pin bones against the ground: preprocessing incompatible contact/joint constraints can sustain head oscillations. | `false` | Humanoid Passenger > Free Ragdoll > Preprocessing |
| `freeRagdollSolverIterations` | `int` | Minimum positional solver passes for a released ragdoll. Increase for more stable joint/contact solving at additional physics cost; higher per-body settings are preserved. | `24`; Minimum: 1 | Humanoid Passenger > Free Ragdoll > Solver Iterations |
| `freeRagdollSolverVelocityIterations` | `int` | Minimum velocity solver passes for a free ragdoll. Increase to improve impulse/velocity constraint solving at extra physics cost; this does not stiffen anatomical angle limits. | `8`; Minimum: 1 | Humanoid Passenger > Free Ragdoll > Solver Velocity Iterations |
| `ik` | `HumanoidIK` ([fields](World.md#humanoidik)) | Bone solver used to place hands and feet on seat targets. Setup finds an existing HumanoidIK or creates one for a valid humanoid Animator and maps its bones. | `None / unassigned` | Humanoid Passenger > Ik |
| `pelvis` | `Transform` | Pelvis bone used to place the character on the seat and attach physical seat support. Choose the skeleton's actual hip/pelvis transform. | `None / unassigned` | Humanoid Passenger > Pelvis |
| `physicalWhileSeated` | `bool` | Keeps the seated skeleton physically simulated rather than attaching it as a kinematic character. | `true` | Humanoid Passenger > Physical While Seated |
| `physicalAnimation` | `PassengerPhysicalAnimationSettings` | Contribution, ownership blend and bounded muscle drives for the composed Animator pose on physical limbs. See [layered physical animation](../HandleAnimation.md#layered-animation-on-a-physical-passenger). | Weight `1`, Blend Duration `.15` seconds | Humanoid Passenger > Physical Animation |
| `ragdollBodies` | `Rigidbody[]` | Rigidbodies belonging to this character's physical skeleton. Seating/release changes their physics state; setup discovers child rigidbodies when the list is empty. | `System.Array.Empty<Rigidbody>()` | Humanoid Passenger > Ragdoll Bodies |


### Physical animation settings

All non-weight numeric values have a minimum of zero. Weight is clamped to 0–1.

| Setting | Default | Inspector path |
| --- | --- | --- |
| Weight | 1 | Humanoid Passenger > Physical Animation > Weight |
| Blend Duration | .15 s | Humanoid Passenger > Physical Animation > Blend Duration |
| Position Spring / Position Damper / Maximum Force | 2200 / 80 / 100 N | Humanoid Passenger > Physical Animation > End position > [setting] |
| Rotation Spring / Rotation Damper / Maximum Torque | 900 / 45 / 80 N·m | Humanoid Passenger > Physical Animation > End rotation > [setting] |
| Joint Spring / Joint Damper / Maximum Joint Torque | 120 / 12 / 80 N·m | Humanoid Passenger > Physical Animation > Anatomical joint pose > [setting] |

## InteriorCamera

Exact cabin-anchor follow with bounded mouse look and configurable camera lens.

**Source:** `Runtime/World/Camera/InteriorCamera.cs`. Component / asset.

**Inherited settings:** [CameraModule](World.md#cameramodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `fieldOfView` | `float` | Vertical field of view in degrees while interior is active. The core restores the previous lens on release. | `72`; Range: 1 to 179 |
| `nearClipPlane` | `float` | Distance in metres below which geometry is clipped in the cockpit view. The 0.04 default keeps nearby dashboard parts visible; increasing it cuts away more nearby geometry. | `.04`; Minimum: .001f |
| `pitchLimits` | `Vector2` | Minimum/maximum up-down look angles in degrees relative to the cabin view. Tighten them to prevent looking through the roof or the driver's body. | `new Vector2(-55, 65)` |
| `positionOffset` | `Vector3` | Camera displacement in metres in the cabin anchor's local axes. Use it to place the driver's eye position without moving the anchor object. | `Zero-initialized Vector3` |
| `rotationOffset` | `Vector3` | Extra camera orientation in degrees relative to the cabin anchor. Use it to align the default view with the windshield or cockpit forward direction. | `Zero-initialized Vector3` |
| `yawLimits` | `Vector2` | Minimum/maximum left-right look angles in degrees around the cabin's default heading. Widen them to let the driver look farther sideways or behind. | `new Vector2(-180, 180)` |

## JoystickHandle

**Source:** `Runtime/World/Passengers/IK/Handle/JoystickHandle.cs`. Joystick grip and steering-contact geometry. Inherits SteeringWheelHandle; pitch/roll model motion belongs to SteeringStickAnimator.

**Inherited settings:** `SteeringWheelHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## MotorcycleHandle

Supplies fixed left/right contacts with prepared finger poses.

**Source:** `Runtime/World/Passengers/IK/Handle/MotorcycleHandle.cs`. Component / asset.

**Inherited settings:** [VehicleHandle](World.md#vehiclehandle). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `gripLength` | `float` | Length in metres of the cylindrical grip surface used for hand/finger fitting. Match the usable rubber grip rather than the full handlebar width. | `.11`; Minimum: .01f | Motorcycle Handle > Grip Length |
| `gripRadius` | `float` | Tube radius in local metres. Grip centres stay fixed; the editor updates the palm contacts and prepares the fingers. | `.025`; Minimum: .002f | Motorcycle Handle > Grip Radius |
| `leftGrip` | `Transform` | Centre of the left grip. Local X runs along the tube; local Y points from the palm towards the tube centre. | `None / unassigned` | Motorcycle Handle > Left Grip |
| `rightGrip` | `Transform` | Independent right-hand grip frame. Place and orient it on the throttle grip so each hand gets its own handlebar contact pose. | `None / unassigned` | Motorcycle Handle > Right Grip |

## ObjectDropper

Validates selected payload release and cooldown.

**Source:** `Runtime/World/Weapons/ObjectDropper.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `dropInterval` | `float` | Minimum seconds between accepted object releases. Increase to space drops farther apart; it does not change a released object's falling speed. | `.4`; Minimum: 0 |
| `droppingEnabled` | `bool` | Allows drop requests to release mounted objects. Turn off to keep the payload attached without clearing its configuration. | `true` |

## OrbitCamera

See [camera setup](../Cameras.md).

| Setting | Type | Description | Declared default |
| --- | --- | --- | --- |
| `distance` | `float` | Requested distance in metres from the focus point before obstacle avoidance. | `7` |
| `minimumDistance` | `float` | Nearest permitted user zoom distance in metres. | `1.5f` |
| `maximumDistance` | `float` | Farthest permitted user zoom distance in metres. | `65` |
| `focusOffset` | `Vector3` | Anchor-local focus offset in metres; aim the orbit at the desired part of the vehicle. | `new Vector3(0, 1.1f, 0)` |
| `initialYaw` | `float` | Initial yaw offset in degrees from the anchor heading when the view is reset. | `` |
| `initialPitch` | `float` | Initial orbit pitch offset in degrees when the view is reset. | `22` |
| `pitchLimits` | `Vector2` | Minimum and maximum orbit pitch angles in degrees. | `new Vector2(-5, 70)` |
| `zoomSensitivity` | `float` | Distance change per scroll input unit when adjusting user zoom. | `.6f` |
| `followResponse` | `float` | Response of orbit rotation and outward distance recovery. Higher values settle more quickly. | `12` |
| `avoidObstacles` | `bool` | Shorten the orbit when an enabled obstacle category blocks the view. Off by default; no obstruction casts run while disabled. | `` |
| `avoidGround` | `bool` | Treat Terrain and colliders beneath an enabled Orbit Camera Ground as obstacles when avoidance is enabled. | `true` |
| `avoidOtherObstacles` | `bool` | Also avoid ordinary scenery and unmarked props. Off by default; does not enable vehicles, passengers or Dynamic Obstacles. | `` |
| `avoidOtherVehicles` | `bool` | Also avoid other vehicles, including their attached parts. The followed vehicle and its own detached parts are always ignored. | `` |
| `obstructionRadius` | `float` | Radius in metres of the sphere swept between the focus and requested camera position. | `.2f` |
| `obstructionMask` | `LayerMask` | Layers tested by obstacle avoidance. Category switches still filter colliders inside this mask. | `~0` |
| `ignorePassengers` | `bool` | Exclude passenger bodies and ragdolls even when other obstacles are enabled. The followed vehicle's own passengers are always ignored. | `true` |
| `ignoreDynamicObstacles` | `bool` | Exclude props marked with Dynamic Obstacle even when other obstacles are enabled. | `true` |
| `gravityAlignedFocus` | `bool` | Keep the focus anchor's vehicle-local offset aligned with gravity instead of chassis pitch/roll. Prevents an overturn from moving the focus below the ground. | `` |

## PassengerAccess

Character root component. Assign **Passenger Access > Passenger / Motion**. All generic and directional UnityEvents are under **Passenger Access > Signals and callbacks** above Gizmos. See [built-in setup](../PassengerAccess.md#tutorial-built-in-humanoid-boarding).

Owns the entry/exit state machine, reservation and cancellation.

**Source:** `Runtime/World/Passengers/Access/PassengerAccess.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `cancelled` | `UnityEvent` | Event invoked when an active access operation is aborted. Use it to restore application UI or input state; it does not report successful boarding. | `No listeners` | Passenger Access > Cancelled |
| `completed` | `UnityEvent` | Event invoked after successful entry or exit. At this point the occupant/seat assignment has been updated, so gameplay can switch driving or walking controls. | `No listeners` | Passenger Access > Completed |
| `motion` | `AccessMotion` ([fields](World.md#accessmotion)) | Access-motion component that animates and aligns this character while boarding or leaving. The sequencer starts it after the door is ready and waits for its result before completing access. | `None / unassigned` | Passenger Access > Motion |
| `onEnterBegin` | `UnityEvent` | Once an admitted entry starts in Opening, after Before checks; seat reservation is held. | `No listeners` | Passenger Access > Signals and callbacks > On Enter Begin |
| `onEnterCancelled` | `UnityEvent` | After a reserved entry is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. | `No listeners` | Passenger Access > Signals and callbacks > On Enter Cancelled |
| `onEnterFinish` | `UnityEvent` | Only after the entire entry succeeds, including the required door state and reservation/Target cleanup. | `No listeners` | Passenger Access > Signals and callbacks > On Enter Finish |
| `onEnterInProgress` | `UnityEvent<float>` | After each entry motion sample in Moving, starting at zero; progress one is not whole-sequence completion. Dynamic float argument: normalized motion progress 0..1. | `No listeners` | Passenger Access > Signals and callbacks > On Enter In Progress |
| `onExitBegin` | `UnityEvent` | Once an admitted exit starts in Opening, after Before checks; seat reservation is held. | `No listeners` | Passenger Access > Signals and callbacks > On Exit Begin |
| `onExitCancelled` | `UnityEvent` | After a reserved exit is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. | `No listeners` | Passenger Access > Signals and callbacks > On Exit Cancelled |
| `onExitFinish` | `UnityEvent` | Only after the entire exit succeeds, including the required door state and reservation/Target cleanup. | `No listeners` | Passenger Access > Signals and callbacks > On Exit Finish |
| `onExitInProgress` | `UnityEvent<float>` | After each exit motion sample in Moving, starting at zero; progress one is not whole-sequence completion. Dynamic float argument: normalized motion progress 0..1. | `No listeners` | Passenger Access > Signals and callbacks > On Exit In Progress |
| `passenger` | `PassengerBody` ([fields](World.md#passengerbody)) | Character entering or leaving the vehicle. If empty, this component finds PassengerBody on the same GameObject; the referenced body is handed to the selected seat on entry. | `None / unassigned` | Passenger Access > Passenger |
| `started` | `UnityEvent` | Event invoked when an access request starts sequencing the door and character movement. Use it to block conflicting controls while entry/exit is in progress. | `No listeners` | Passenger Access > Started |

## PassengerBehaviour

Configuration/implementation type for passenger behaviour within seats, bodies and controller strategies.

**Source:** `Runtime/World/Passengers/Core/PassengerBehaviour.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [PassengerModule](World.md#passengermodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `seat` | `PassengerSeat` ([fields](World.md#passengerseat)) | Seat this behaviour operates on, such as the driver or rider seat. The behaviour runs only for a valid seat and a compatible vehicle. | `None / unassigned` | Passenger Behaviour > Seat |

## PassengerBody

Base character adapter used by seats and controller strategies.

**Source:** `Runtime/World/Passengers/Bodies/PassengerBody.cs`. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## PassengerBodyPartConfig

Inherited by each hand/foot. Path: **Passenger Seat > Hands, feet and head > [limb]**. Main Mode/Anchor/Handle and collision-release toggles are followed by **Advanced / Fine tuning**, **Damage feedback**, then **Release colliders**. Advanced does not contain either damage settings or the collider list.

Describes each limb's mode, target and support choices.

**Source:** `Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `damageFeedback` | `PassengerLimbDamageFeedback` | Independent Damage feedback group for this limb. | New settings instance | Passenger Seat > Hands, feet and head > [limb] > Damage feedback |
| `releaseColliders` | `PassengerCollisionSurface[]` | Selected surfaces for this Free limb, below Damage feedback. | Empty | Passenger Seat > Hands, feet and head > [limb] > Release colliders |
| `anchor` | `Transform` | Direct target transform used when no Handle is assigned. Its pose sets where this hand or foot reaches/rests; a handle supplies its own target instead. | `None / unassigned` | Passenger Seat > Hands, feet and head > [limb] > Anchor |
| `enableSelfCollidersOnRelease` | `bool` | Enable contacts between this Free limb and the ragdoll's own body. Neighboring skeletal bodies keep collisions disabled. | `false` | Passenger Seat > Hands, feet and head > [limb] > Enable Self Colliders On Release |
| `enableVehicleCollidersOnRelease` | `bool` | Enable contacts with the vehicle when this limb enters Free. The seat-wide setting also enables this for released limbs. | `false` | Passenger Seat > Hands, feet and head > [limb] > Enable Vehicle Colliders On Release |
| `handle` | `VehicleHandle` ([fields](World.md#vehiclehandle)) | Interactive grip or pedal supplying this limb's target and support settings. When assigned, it replaces the direct Anchor; a disabled handle supplies no valid target. | `None / unassigned` | Passenger Seat > Hands, feet and head > [limb] > Handle |
| `mode` | `PassengerBodyPartMode` | IKHandle places/supports the limb at its resolved target. Animator leaves it to character animation. Free releases target control so physical limbs can hang; free-arm options can still set an initial pose. Options: `IKHandle`, `Animator`, `Free`. | `IKHandle` | Passenger Seat > Hands, feet and head > [limb] > Mode |

## PassengerFootConfig

Path: **Passenger Seat > Hands, feet and head > Left Foot / Right Foot**. Pin To Anchor and release toggles are at limb top; other tuning is in **Advanced / Fine tuning**. Damage feedback and Release colliders follow it.

Per-foot mode, target and pinning/rotation configuration used by the seat.

**Source:** `Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [PassengerBodyPartConfig](World.md#passengerbodypartconfig). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `alignRotation` | `bool` | Guide the ankle orientation towards the authored target rotation, including moving pedals. Disabled by default. | `false` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Align Rotation |
| `damper` | `float` | Position damping for a spring-supported foot. Increase to reduce bouncing around the pedal/peg; it does not control ankle rotation. | `70`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Damper |
| `hold` | `bool` | Keeps a physical foot supported at its resolved target in IKHandle mode. Pin To Anchor can lock the position; otherwise spring/travel settings determine how much it yields. | `true` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Hold |
| `limitTravel` | `bool` | Adds a native distance limit around the foot target for spring-supported feet. Turn off to let the spring yield farther under load. Pin To Anchor overrides this with a locked foot position. | `false` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Limit Travel |
| `maximumAcceleration` | `float` | Foot-support force cap in m/s², multiplied by supported leg mass. A positive value enables mass-based support; zero uses the simpler default capped drive. Pin To Anchor overrides spring support. | `0`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Maximum Acceleration |
| `maximumRotationTorque` | `float` | Torque cap in N·m for foot-orientation support. Reduce to let the ankle twist under load; increase for a firmer sole orientation. | `25`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Maximum Rotation Torque |
| `pinToAnchor` | `bool` | Physically lock the foot position to its resolved anchor while Hold and IK Handle mode are enabled. Requires a physical seated passenger. Overrides spring and travel settings; ankle rotation remains free unless Align Rotation is enabled. | `false` | Passenger Seat > Hands, feet and head > [limb] > Pin To Anchor |
| `rotationDamper` | `float` | Damping of foot rotation around its target angle. Increase to reduce ankle wobble while Align Rotation is enabled. | `12`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rotation Damper |
| `rotationSpring` | `float` | Spring turning the physical foot toward the target orientation when Align Rotation is enabled. Increase to keep the sole aligned more firmly. | `160`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rotation Spring |
| `spring` | `float` | Position spring holding an unpinned foot at its target. Increase for firmer support under acceleration; Pin To Anchor locks position instead and overrides this spring. | `1200`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Spring |
| `travel` | `float` | Maximum positional slack in metres around the pinned foot target when travel limiting is enabled. | `.035`; Minimum: .001f | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Travel |

## PassengerGForceLimits

Path: **Passenger Seat > Settings > Force limits > [setting]**, the final Settings group.

Live settings in the **Passenger Seat > Settings > Force limits** foldout. See [G-force limits](../Seats.md#g-force-limits) for detection, timing and controller exclusions.

| Setting | Type | Default and constraints | Description | Inspector path |
| --- | --- | --- | --- | --- |
| `enabled` | `bool` | `true` | Enable transient protection for an occupied physical ragdoll. | Passenger Seat > Settings > Force limits > Enabled |
| `maximumJointSeparation` | `float` | `.025; minimum .001` | Maximum anatomical anchor separation while active, metres. Authored angular ranges are retained; soft limit springs are restored after protection. | Passenger Seat > Settings > Force limits > Maximum Joint Separation |
| `maximumRelativeAngularSpeed` | `float` | `360; minimum 1` | Maximum bone angular speed and rotation per physics step relative to the moving vehicle, based on the live pre-solve pose, degrees/second. | Passenger Seat > Settings > Force limits > Maximum Relative Angular Speed |
| `maximumRelativeSpeed` | `float` | `3; minimum .1` | Maximum dynamic bone speed relative to the local vehicle point velocity, m/s. | Passenger Seat > Settings > Force limits > Maximum Relative Speed |
| `maximumSeatDisplacement` | `float` | `.15; minimum .01` | Maximum pelvis displacement from the seated spine origin while active, metres. | Passenger Seat > Settings > Force limits > Maximum Seat Displacement |
| `minimumForce` | `float` | `0; minimum 0` | Optional minimum passenger inertial load in N, not vehicle contact force. Zero disables this additional test. | Passenger Seat > Settings > Force limits > Minimum Force |
| `minimumGForce` | `float` | `8; minimum 1` | Minimum gravity-compensated seat acceleration in standard G. | Passenger Seat > Settings > Force limits > Minimum Gforce |
| `minimumVelocityChange` | `float` | `1; minimum 0` | Minimum gravity-compensated change of seat velocity per physics step, m/s. | Passenger Seat > Settings > Force limits > Minimum Velocity Change |
| `monitorAfterPhysics` | `bool` | `true` | Observe overloads immediately after every physics solve, including wheel/suspension impulses without a body collision callback. Disable to retain pre-solve and collision-only detection; already active protection is still enforced after physics. | Passenger Seat > Settings > Force limits > Monitor After Physics |
| `protectConstraintFailure` | `bool` | `true` | Independently contain gross ragdoll failure above twice the relative speed limits or 125% of seat displacement; does not require a G/force spike. Main Enabled still applies. | Passenger Seat > Settings > Force limits > Protect Constraint Failure |
| `protectionTime` | `float` | `.15; minimum 0` | Minimum hold after an overload, at least one physics step; extended until relative bone motion settles. | Passenger Seat > Settings > Force limits > Protection Time |

## PassengerHandConfig

Path: **Passenger Seat > Hands, feet and head > Left Hand / Right Hand**. Fields not shown at the limb top are in **Advanced / Fine tuning**. Damage feedback and Release colliders are independent groups below Advanced.

Configuration/implementation type for passenger hand config within physical passengers and limb configuration.

**Source:** `Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [PassengerBodyPartConfig](World.md#passengerbodypartconfig). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `alignRestRotation` | `bool` | Let the physical resting wrist follow its anchor rotation with a bounded angular spring. Uses the calibrated palm frame when a HandGrip is present, otherwise the wrist frame. Reapply seated tuning after enabling; anchor rotation then updates live. | `false` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Align Rest Rotation |
| `animateThumb` | `bool` | Allow grip solvers to pose the thumb. Disable to keep its authored local pose across handle changes. | `true` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Animate Thumb |
| `damper` | `float` | Position damping for the basic held-hand support. Increase to reduce oscillation around the anchor; handle and relaxed-rest support can use separate damping. | `180`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Damper |
| `freeArmDamper` | `float` | Damping of relative arm-joint rotation in Free mode. It reduces flailing without pulling the arm back toward an anchor or fixed pose. | `3`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Free Arm Damper |
| `freeArmMaximumDampingTorque` | `float` | Maximum damping torque in N·m on a free arm. Higher values resist rapid limb rotation more strongly while still allowing the arm to hang. | `15`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Free Arm Maximum Damping Torque |
| `freeWristRotation` | `Vector3` | Reference wrist Euler rotation in degrees for the optional initialized free-arm pose. | `Zero-initialized Vector3` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Free Wrist Rotation |
| `hold` | `bool` | Keeps a physical hand supported at its resolved target while in IKHandle mode. Turn off to remove that support; handle/grip and relaxed-rest settings determine the support style. | `true` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Hold |
| `limitRestTravel` | `bool` | Bound wrist distance from the rest anchor using a native joint limit. Disable for force-limited spring support only, allowing the hand to yield under larger loads. Reapply seated tuning after editing. | `true` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Limit Rest Travel |
| `maximumRestForce` | `float` | Maximum force in newtons holding a relaxed-rest wrist at its anchor. Lower values let impacts pull the hand away more easily. | `80`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Maximum Rest Force |
| `maximumRestRotationTorque` | `float` | Maximum torque in N·m for relaxed-rest wrist alignment. Lower values let the palm rotate more freely under load. | `8`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Maximum Rest Rotation Torque |
| `palmContact` | `bool` | HandGrip calibration identifying the palm contact and finger poses for this hand. Use it when the wrist bone's origin does not coincide with the palm touching the control. | `false` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Palm Contact |
| `poseFreeArm` | `bool` | In Free mode, pose this arm toward its direct anchor once on entry, then let it hang. No car-to-hand support or angular position spring is created. Reapply seated tuning to change the initial pose. | `false` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Pose Free Arm |
| `relaxedRest` | `bool` | Soft support around a direct hand anchor, with weaker arm pose motors and free wrist rotation. Reapply seated tuning after editing. Handles and palm grips retain their own support. | `false` | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Relaxed Rest |
| `restArmDamper` | `float` | Damping of shoulder/elbow movement in the relaxed-rest arm. Increase to reduce flailing without making the wrist grip rigid. | `1.5`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Arm Damper |
| `restArmMaximumTorque` | `float` | Torque cap in N·m for the relaxed arm's pose spring and damping. Increase only if the arm support should resist stronger disturbances. | `15`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Arm Maximum Torque |
| `restArmSpring` | `float` | Weak angular pose spring on the relaxed arm's joints. Increase to retain the initial shoulder/elbow pose more firmly while the wrist rests at its anchor. | `6`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Arm Spring |
| `restDamper` | `float` | Damping of wrist movement around the direct rest anchor in Relaxed Rest. Increase to reduce bouncing or vibration while keeping the support soft. | `24`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Damper |
| `restRotationDamper` | `float` | Damping of wrist twisting around the relaxed-rest orientation. Increase to settle rotational wobble when rotation alignment is enabled. | `2`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Rotation Damper |
| `restRotationSpring` | `float` | Spring aligning a relaxed-rest wrist to the anchor rotation when Rest Align Rotation is on. Increase for firmer palm orientation; position support is configured separately. | `12`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Rotation Spring |
| `restSpring` | `float` | Spring pulling the wrist toward its direct rest anchor when Relaxed Rest is active. Increase for firmer support; it does not replace a VehicleHandle's grip spring. | `300`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Spring |
| `restTravel` | `float` | Allowed wrist displacement in metres from the relaxed-rest anchor when Limit Rest Travel is enabled. A larger value lets the resting hand wander farther under load. | `.12`; Minimum: .01f | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Rest Travel |
| `spring` | `float` | Position spring for a held hand using the basic seat-anchor support. Increase for a firmer attachment; relaxed-rest and VehicleHandle grip paths have their own spring settings. | `2200`; Minimum: 0 | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning > Spring |

## PassengerJointSupport

Path: **Passenger Seat > Custom supports > Joint Supports > [element] > [setting]**. Select Joint Id from the character’s Anatomical Joints mapping; the list supports +/− and drag reordering.

Serializable seat-owned support settings. Anatomical constraints remain active; these settings add forces rather than editing limits or creating another native joint.

**Source:** `Runtime/World/Passengers/Seats/PassengerJointSupport.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `active` | `bool` | Apply this additional support while this seat has an active physical ragdoll occupant. | `true` | Passenger Seat > Custom supports > Joint Supports > [item] > Active |
| `anchor` | `Transform` | Target pose, normally an empty Transform under the vehicle. No target means no support. | `None / unassigned` | Passenger Seat > Custom supports > Joint Supports > [item] > Anchor |
| `damper` | `float` | Damping in N per m/s of relative point velocity. Resists oscillation while allowing the target to move with the vehicle. | `30`; Minimum: 0 | Passenger Seat > Custom supports > Joint Supports > [item] > Damper |
| `holdRotation` | `bool` | Also align the joint body's orientation with the target. Leave off to hold only a point and retain anatomical angular freedom. | `false` | Passenger Seat > Custom supports > Joint Supports > [item] > Hold Rotation |
| `jointId` | `string` | Exact, case-sensitive Joint ID from the occupant's Anatomical Joints list. One support per ID in this seat. | `None / unassigned` | Passenger Seat > Custom supports > Joint Supports > [item] > Joint Id |
| `localOffset` | `Vector3` | Offset from the anatomical joint's anchor, in the joint body's local coordinates. Zero holds the joint pivot, for example the knee. | `Zero-initialized Vector3` | Passenger Seat > Custom supports > Joint Supports > [item] > Local Offset |
| `maximumForce` | `float` | Maximum total position support force in N, including damping. Zero disables position support. | `300`; Minimum: 0 | Passenger Seat > Custom supports > Joint Supports > [item] > Maximum Force |
| `maximumTorque` | `float` | Maximum total rotation support torque in Nm. Zero disables angular support. | `40`; Minimum: 0 | Passenger Seat > Custom supports > Joint Supports > [item] > Maximum Torque |
| `rotationDamper` | `float` | Angular damping in Nm per rad/s relative to the moving target. | `10`; Minimum: 0 | Passenger Seat > Custom supports > Joint Supports > [item] > Rotation Damper |
| `rotationOffset` | `Vector3` | Desired joint-body rotation relative to the anchor, in degrees. Used only when Hold Rotation is enabled. | `Zero-initialized Vector3` | Passenger Seat > Custom supports > Joint Supports > [item] > Rotation Offset |
| `rotationSpring` | `float` | Angular restoring torque in Nm per radian of orientation error. | `100`; Minimum: 0 | Passenger Seat > Custom supports > Joint Supports > [item] > Rotation Spring |
| `spring` | `float` | Position restoring force in N per metre of error. Higher values pull the joint pivot toward the target more strongly. | `500`; Minimum: 0 | Passenger Seat > Custom supports > Joint Supports > [item] > Spring |

## PassengerModule

Configuration/implementation type for passenger module within seats, bodies and controller strategies.

**Source:** `Runtime/World/Passengers/Core/PassengerModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## PassengerLimbDamageFeedback

**Path:** Passenger Seat > Hands, feet and head > [limb] > Damage feedback. Separate configuration on each of four limbs, below Advanced / Fine tuning.

| Setting | Type | Meaning | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `releaseOnCollision` | bool | Release only this limb on qualifying collision | false | Passenger Seat > Hands, feet and head > [limb] > Damage feedback > Release On Collision |
| `releaseOnSpin` | bool | Release only this limb on sustained gravity-relative tilt | false | Passenger Seat > Hands, feet and head > [limb] > Damage feedback > Release On Spin |
| `minimumCollisionForce` | float | Collision force threshold in N | 20000 | Passenger Seat > Hands, feet and head > [limb] > Damage feedback > Minimum Collision Force |
| `minimumCollisionSpeed` | float | Relative speed threshold in m/s | 3 | Passenger Seat > Hands, feet and head > [limb] > Damage feedback > Minimum Collision Speed |
| `minimumAngle` | float | Tilt threshold in degrees | 90 | Passenger Seat > Hands, feet and head > [limb] > Damage feedback > Minimum Angle |
| `tiltDelay` | float | Continuous over-threshold time in seconds | 0.1 | Passenger Seat > Hands, feet and head > [limb] > Damage feedback > Tilt Delay |

## PassengerCollisionSurface

**Paths:** Passenger Seat > Hands, feet and head > [limb] > Release colliders > Element; or Passenger Seat > Settings > Damage / Auto-eject > Eject colliders > Element.

| Setting | Type | Meaning | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `collider` | Collider | Existing cabin/door surface | None | [Release colliders or Eject colliders path] > [item] > Collider |
| `ignoreWorldCollisions` | bool | Surface ignores eligible world contacts | false | [Release colliders or Eject colliders path] > [item] > Ignore World Collisions |
| `ignoreVehicleCollisions` | bool | Surface ignores eligible vehicle contacts | false | [Release colliders or Eject colliders path] > [item] > Ignore Vehicle Collisions |

The same collider can be referenced in several lists; a checked policy takes precedence over unchecked copies. Lists have native add/remove/reorder plus a shared Copy colliders / Paste colliders / Reset colliders clipboard. Reset has no confirmation; Undo restores its contents. A limb list applies only to that Free limb, while Eject colliders applies to the whole detached passenger. These flags describe the listed surface's contact policies, not the character's broad collision flags.

## PassengerRestraints

Path: **Passenger Seat > Settings > Damage / Auto-eject** for ejection policy; **Passenger Seat > Settings > Fine Tuning** for other harness/constraint fields. Limb damage settings live on each limb instead of this class.

Stores harness, release, damping and ejection configuration.

**Source:** `Runtime/World/Passengers/Physics/PassengerRestraints.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `chestSupportStrength` | `float` | Scales chest support independently of the pelvis. Reapply seated tuning or re-enter the seat after editing. One preserves the original support. | `1`; Range: .25f to 4 | Passenger Seat > Settings > Fine Tuning > Chest Support Strength |
| `ejectionTiltDelay` | `float` | Time in seconds that the ejection tilt must be sustained before releasing the occupant. | `.1`; Minimum: 0 | Passenger Seat > Settings > Damage / Auto-eject > Ejection Tilt Delay |
| `ejectPassengerOnCollision` | `bool` | Whole occupant release after a sufficiently strong new contact. | `false` | Passenger Seat > Settings > Damage / Auto-eject > Eject Passenger On Collision |
| `ejectPassengerOnSpin` | `bool` | Whole occupant release after sustained roll/pitch tilt. | `true` | Passenger Seat > Settings > Damage / Auto-eject > Eject Passenger On Spin |
| `enablePassengerEjection` | `bool` | Allow the whole occupant to detach from the seat into a free ragdoll. Removes every hand, foot, pelvis and chest restraint. Independent of the limb-only options above. | `false` | Passenger Seat > Settings > Damage / Auto-eject > Enable Passenger Ejection |
| `harnessAngularDamper` | `float` | Mass-scaled damping resisting pelvis/chest rotation relative to the seated pose. Increase to reduce rocking without narrowing the allowed lean angles. | `3`; Minimum: 0 | Passenger Seat > Settings > Fine Tuning > Harness Angular Damper |
| `harnessAngularSpring` | `float` | Mass-scaled spring turning pelvis/chest back toward the captured seated orientation. Increase for a more upright, firmly held posture; reduce for freer torso movement. | `16`; Minimum: 0 | Passenger Seat > Settings > Fine Tuning > Harness Angular Spring |
| `harnessChestTravel` | `float` | Maximum chest displacement in metres from its support point when Limit Harness Travel is on. Increase to let the upper body sway farther independently of the pelvis. | `.06`; Minimum: .001f | Passenger Seat > Settings > Fine Tuning > Harness Chest Travel |
| `harnessDampingRatio` | `float` | Damping of the soft harness relative to its spring and supported mass. Around 1 settles without much bounce; lower values allow oscillation, higher values make the return more heavily damped. | `1`; Range: .5f to 1.5f | Passenger Seat > Settings > Fine Tuning > Harness Damping Ratio |
| `harnessForwardLean` | `float` | Seat-relative forward/backward angular travel in degrees around the captured seated pose. | `22`; Range: 5 to 40 | Passenger Seat > Settings > Fine Tuning > Harness Forward Lean |
| `harnessFrequency` | `float` | Natural frequency in Hz used to calculate soft-harness positional springs from supported mass. Increase for quicker, firmer pelvis/chest support; decrease for softer, slower movement. | `3`; Range: 1 to 5 | Passenger Seat > Settings > Fine Tuning > Harness Frequency |
| `harnessLimitDamperPerKg` | `float` | Mass-scaled damping at the harness's angular travel stops. Increase to reduce bounce when the occupant reaches a lean/twist limit. | `6`; Minimum: 0 | Passenger Seat > Settings > Fine Tuning > Harness Limit Damper Per Kg |
| `harnessLimitSpringPerKg` | `float` | Mass-scaled stiffness of the soft harness's angular travel stops. Increase to resist going beyond the lean/twist envelope more firmly. | `60`; Minimum: .1f | Passenger Seat > Settings > Fine Tuning > Harness Limit Spring Per Kg |
| `harnessMaximumAcceleration` | `float` | Force cap for soft harness support expressed as m/s² and multiplied by the supported mass. Increase to hold the occupant through stronger acceleration; reduce to let the support yield. | `80`; Minimum: 5 | Passenger Seat > Settings > Fine Tuning > Harness Maximum Acceleration |
| `harnessMaximumTorquePerKg` | `float` | Angular-support torque cap per kilogram of supported mass. Increase to let the soft harness hold torso orientation through stronger forces; this does not narrow the lean limits. | `8`; Minimum: 0 | Passenger Seat > Settings > Fine Tuning > Harness Maximum Torque Per Kg |
| `harnessSideLean` | `float` | Allowed side-to-side tilt in degrees around the captured seated pose. Increase to let the ragdoll lean sideways more before the soft limit pushes back. | `12`; Range: 5 to 30 | Passenger Seat > Settings > Fine Tuning > Harness Side Lean |
| `harnessTwist` | `float` | Seat-relative twist travel in degrees around the captured seated pose. | `28`; Range: 5 to 45 | Passenger Seat > Settings > Fine Tuning > Harness Twist |
| `limitHarnessTravel` | `bool` | Keep the pelvis inside Seat Travel and the chest inside Chest Travel using native joint limits. Angular sway stays physical. | `true` | Passenger Seat > Settings > Fine Tuning > Limit Harness Travel |
| `minimumEjectionAngle` | `float` | Gravity-relative tilt angle in degrees required for the spin/overturn ejection policy. | `90`; Range: 0 to 180 | Passenger Seat > Settings > Damage / Auto-eject > Minimum Ejection Angle |
| `minimumEjectionCollisionForce` | `float` | Minimum average contact force in N: impulse divided by the physics timestep. | `20000`; Minimum: 0 | Passenger Seat > Settings > Damage / Auto-eject > Minimum Ejection Collision Force |
| `minimumEjectionCollisionSpeed` | `float` | Minimum relative collision speed in m/s; force and speed thresholds must both be met. | `3`; Minimum: 0 | Passenger Seat > Settings > Damage / Auto-eject > Minimum Ejection Collision Speed |
| `passengerEjectionVelocity` | `Vector3` | Optional additional velocity in vehicle-local m/s. Existing ragdoll linear/angular motion is preserved. | `Zero-initialized Vector3` | Passenger Seat > Settings > Damage / Auto-eject > Passenger Ejection Velocity |
| `reseatEjectedOnReset` | `bool` | Allows vehicle reset to restore an eligible occupant previously ejected from this seat. | `true` | Passenger Seat > Settings > Damage / Auto-eject > Reseat Ejected On Reset |
| `seatDamper` | `float` | Damping on pelvis movement in the regular seat-support path. Increase to reduce bouncing. Soft Harness uses Harness Damping Ratio instead. | `1300`; Minimum: 0 | Passenger Seat > Settings > Fine Tuning > Seat Damper |
| `seatSpring` | `float` | Positional spring holding the pelvis to the seat in the regular support path. Higher values hold it more firmly; Soft Harness calculates its own mass-based spring from Harness Frequency instead. | `14000`; Minimum: 0 | Passenger Seat > Settings > Fine Tuning > Seat Spring |
| `seatTravel` | `float` | Maximum pelvis displacement in metres from its seat support point when linear travel is limited. A smaller value keeps the hips closer to the saddle or seat. | `.025`; Minimum: .001f | Passenger Seat > Settings > Fine Tuning > Seat Travel |
| `softHarness` | `bool` | Bounded native spring drives support pelvis and chest without bone pose overrides. Foot pins are configured separately on each foot. | `true` | Passenger Seat > Settings > Fine Tuning > Soft Harness |
| `solverIterations` | `int` | Minimum solver iterations on seated bones only. Zero preserves the body's setting; higher authored values are retained. Restored on release. | `12`; Range: 0 to 255 | Passenger Seat > Settings > Fine Tuning > Solver Iterations |
| `solverVelocityIterations` | `int` | Minimum velocity solver iterations while seated; higher per-body settings are preserved. | `4`; Range: 0 to 255 | Passenger Seat > Settings > Fine Tuning > Solver Velocity Iterations |
| `torsoSwayDegrees` | `float` | Angular freedom in degrees around the seated torso pose in the regular support path. Increase for more body sway; Soft Harness uses its separate side, forward and twist limits. | `12`; Range: 0 to 35 | Passenger Seat > Settings > Fine Tuning > Torso Sway Degrees |

## Passengers

Discovers owned handles and supplies input before seat work.

**Source:** `Runtime/World/Passengers/Core/Passengers.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `spawnOnStart` | `bool` | Lets enabled seats create/adopt their starting occupants when the vehicle starts. Each seat must also have Spawn On Start enabled; turn this off to populate seats through gameplay code. | `true` | Passengers > Spawn On Start |



| Setting | Type | Description | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `onBeforeEnter` | `UnityEvent<PassengerSeatContext>` | Before an occupant acquires any seat on this vehicle. | `new UnityEvent<PassengerSeatContext>()` | Passengers > Signals and callbacks > On Before Enter |
| `onEntered` | `UnityEvent<PassengerSeat, PassengerBody>` | After an occupant acquires a seat; includes both seat and passenger. | `new UnityEvent<PassengerSeat, PassengerBody>()` | Passengers > Signals and callbacks > On Entered |
| `onBeforeExit` | `UnityEvent<PassengerSeatContext>` | Before occupancy ends on any seat, including ejection or disable. | `new UnityEvent<PassengerSeatContext>()` | Passengers > Signals and callbacks > On Before Exit |
| `onExited` | `UnityEvent<PassengerSeat, PassengerBody, PassengerExitReason>` | After occupancy ends; includes seat, passenger and reason. | `new UnityEvent<PassengerSeat, PassengerBody, PassengerExitReason>()` | Passengers > Signals and callbacks > On Exited |
| `onBeforeEject` | `UnityEvent<PassengerSeatContext>` | Before any seat ejects its occupant. | `new UnityEvent<PassengerSeatContext>()` | Passengers > Signals and callbacks > On Before Eject |
| `onEjected` | `UnityEvent<PassengerSeatContext>` | After a successful ejection, including its optional impulse. | `new UnityEvent<PassengerSeatContext>()` | Passengers > Signals and callbacks > On Ejected |

## PassengerAnimatorLayers

Controls explicitly configured overlay weights for the current seat occupant. See [masked layer setup](../HandleAnimation.md#masked-animator-layers).

**Source:** `Runtime/World/Passengers/Controllers/PassengerAnimatorLayers.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `controller` | `RuntimeAnimatorController` | Authoring controller edited by Apply; does not replace the runtime controller. Animator Override Controllers resolve to their base for mask editing. | Unassigned | Passenger Animator Layers > Controller |
| `layers` | `List<Layer>` | Existing overlay names, masks and requested weights. | Empty | Passenger Animator Layers > Layers |
| `seat` | `PassengerSeat` | Seat supplying the current humanoid and its active animation source. Reset finds a seat on this GameObject. | Unassigned | Passenger Animator Layers > Seat |

## PassengerAnimatorLayers.Layer

**Source:** `Runtime/World/Passengers/Controllers/PassengerAnimatorLayers.cs`. Nested configuration data; add entries in the owning component.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `enabled` | `bool` | Apply the requested weight when on; mute the overlay when off. | `true` | Passenger Animator Layers > Enabled |
| `mask` | `AvatarMask` | Mask saved to the shared controller by Apply in Edit Mode. Null allows the whole body. Not a runtime mask setter. | Unassigned | Passenger Animator Layers > Mask |
| `name` | `string` | Existing overlay layer name; Inspector offers the selected controller's layers. Base Layer is excluded. | Unassigned | Passenger Animator Layers > Name |
| `weight` | `float` | Runtime blend weight and authoring default when enabled. | `1`; Range: 0..1 | Passenger Animator Layers > Weight |

## PassengerSeat

Full layout: **[Seat Inspector paths](../Seats.md#find-a-setting-in-the-seat-inspector)**. Main references are at component top; limb controls under **Hands, feet and head > [limb]**, collision/harness/force settings under **Settings**, extra bindings under **Custom supports**, and **Signals and callbacks** immediately above **Gizmos**.

`Entered`, `Exited`, `ControllerChanged` and custom `ResetRequested`

**Source:** `Runtime/World/Passengers/Seats/PassengerSeat.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `attachmentDamper` | `float` | Damping for main Spring support without physical seat restraints. | `20`; minimum 0 | Passenger Seat > Attachment Damper |
| `attachmentMode` | `PassengerAttachmentMode` | Independent main attachment policy: Spring retains controller support; Parent holds the seating origin at Spine Anchor. Other ragdoll bones keep simulating. | `Spring` | Passenger Seat > Attachment Mode |
| `attachmentSpring` | `float` | Main Spring support strength for occupants without physical seat restraints; does not retune ragdoll restraints. | `120`; minimum 0 | Passenger Seat > Attachment Spring |
| `body` | `PassengerBody` ([fields](World.md#passengerbody)) | Optional pre-placed body. Leave empty to spawn the prefab. | `None / unassigned` | Passenger Seat > Body |
| `bodyPrefab` | `PassengerBody` ([fields](World.md#passengerbody)) | Passenger prefab instantiated when this seat needs to spawn an occupant. It must contain the compatible PassengerBody implementation for the selected controller mode. | `None / unassigned` | Passenger Seat > Body Prefab |
| `customTypeId` | `string` | Application-defined type for Custom occupants; avoids changing the enum. | `None / unassigned` | Passenger Seat > Custom Type ID |
| `enableSelfCollidersOnRelease` | `bool` | Enable self contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. Neighboring skeletal bodies keep collisions disabled. | `false` | Passenger Seat > Settings > Colliders and collisions > Enable Self Colliders On Release |
| `enableVehicleCollidersOnRelease` | `bool` | Enable vehicle contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. | `false` | Passenger Seat > Settings > Colliders and collisions > Enable Vehicle Colliders On Release |
| `ejectColliders` | `PassengerCollisionSurface[]` | Whole-body surfaces under Passenger Seat > Settings > Damage / Auto-eject > Eject colliders. Each item has Collider and both ignore policies. | Empty | Passenger Seat > Settings > Damage / Auto-eject > Eject colliders |
| `excludeSelfCollisionsOnEnter` | `bool` | Exclude self contacts on entry and while held. Release options may restore them. Disable to keep self contacts enabled, including after regrip and reseating. Native joint collision settings still apply. | `true` | Passenger Seat > Settings > Colliders and collisions > Exclude Self Collisions On Enter |
| `excludeVehicleCollisionsOnEnter` | `bool` | Exclude contacts with the vehicle on entry and while held. Release options may restore them. Disable to keep vehicle contacts enabled, including after regrip and reseating. | `true` | Passenger Seat > Settings > Colliders and collisions > Exclude Vehicle Collisions On Enter |
| `exitAnchor` | `Transform` | Seat-associated exit placement marker available to passenger exit/reset workflows. For animated boarding, configure the detailed outside placement and clearance on SeatAccess as well. | `None / unassigned` | Passenger Seat > Exit Anchor |
| `gForceLimits` | `PassengerGForceLimits` ([fields](World.md#passengergforcelimits)) | Emergency overload detector and transient containment. Ordinary ragdoll motion remains unmodified below the activation thresholds. | New settings; enabled | Passenger Seat > Settings > Force limits |
| `headDamper` | `float` | Damping of the head's rotation relative to the vehicle, in N·m per rad/s. Increase to reduce nodding around the supported angle. | `20`; Minimum: 0 | Passenger Seat > Hands, feet and head > Head > Head Damper |
| `headPitch` | `float` | Head pitch relative to the seat's neutral forward pose, in degrees. Negative looks up; positive looks down. | `0`; Range: -60 to 60 | Passenger Seat > Hands, feet and head > Head > Head Pitch |
| `headSpring` | `float` | Strength of the optional ragdoll head support in N·m per radian of angle error. Increase to hold the chosen pitch more firmly; the neck's anatomical limits still apply. | `250`; Minimum: 0 | Passenger Seat > Hands, feet and head > Head > Head Spring |
| `holdHeadForward` | `bool` | Artificial spring support facing the seat's forward direction. Only affects an occupied, active Ragdoll Physics seat; stops on exit/ejection. | `false` | Passenger Seat > Hands, feet and head > Head > Hold Head Forward |
| `jointSupports` | `List<PassengerJointSupport>` ([fields](World.md#passengerjointsupport)) | Optional extra position/rotation springs resolved by the seated occupant's Anatomical Joint IDs. Active only with a physical Ragdoll Physics occupant; empty by default. | `Empty list` | Passenger Seat > Custom supports > Joint Supports |
| `leftFoot` | `PassengerFootConfig` ([fields](World.md#passengerfootconfig)) | Left foot's target, hold/pin and ankle alignment settings. Use them to place the foot on a pedal, peg or floor support. | `new PassengerFootConfig()` | Passenger Seat > Hands, feet and head > Left Foot |
| `leftHand` | `PassengerHandConfig` ([fields](World.md#passengerhandconfig)) | Left hand's control mode, target/grip and physical support. Expand to choose whether it holds a control, rests softly, follows animation or hangs free. | `new PassengerHandConfig()` | Passenger Seat > Hands, feet and head > Left Hand |
| `maximumHeadTorque` | `float` | Torque cap in N·m for artificial head support. A low cap lets the head yield under acceleration or impact even when Head Spring is high. | `80`; Minimum: 0 | Passenger Seat > Hands, feet and head > Head > Maximum Head Torque |
| `parentMakeKinematic` | `bool` | Parent mode makes only the held pelvis Rigidbody kinematic; other bones retain physics. | `true` | Passenger Seat > Parent Make Kinematic |
| `parentPositionOffset` | `Vector3` | Parent-mode position offset in Spine Anchor local metres. | `Vector3.zero` | Passenger Seat > Parent Position Offset |
| `parentRotationOffset` | `Vector3` | Parent-mode rotation offset in Spine Anchor local degrees. | `Vector3.zero` | Passenger Seat > Parent Rotation Offset |
| `parentWhileSeated` | `bool` | Places the occupant under the seat hierarchy while attached. This changes transform ownership; physical ragdoll support still comes from the selected passenger controller and restraints. | `true` | Passenger Seat > Parent While Seated |
| `passengerController` | `PassengerControllerType` | Ragdoll Physics uses the package physics/IK. Animator leaves animation to application code. Animator + IK overlays configured limb handles on application animation without ragdoll. Attach Only parents and positions the occupant without posing it. Custom only records occupancy; application code owns spawning, hierarchy, pose, animation and physics. Options: `RagdollPhysics`, `Animator`, `AnimatorIK`, `AttachOnly`, `Custom`. | `PassengerControllerType.RagdollPhysics` | Passenger Seat > Passenger Controller |
| `passengerType` | `PassengerType` | Category assigned to the seat's occupant: humanoid driver, humanoid passenger or application-defined Custom. Use Custom Type ID for your own category; this does not itself select the physics controller. Options: `HumanoidDriver`, `HumanoidPassenger`, `Custom`. | `PassengerType.HumanoidPassenger` | Passenger Seat > Passenger Type |
| `restraints` | `PassengerRestraints` ([fields](World.md#passengerrestraints)) | Pelvis/chest support, damping, release and ejection settings. Expand to configure each policy. | `new PassengerRestraints()` | Passenger Seat > Settings > Damage / Auto-eject or Fine Tuning (field-dependent) |
| `rightFoot` | `PassengerFootConfig` ([fields](World.md#passengerfootconfig)) | Right foot's target and physical support settings. Configure independently from the left foot for separate pedals or riding contacts. | `new PassengerFootConfig()` | Passenger Seat > Hands, feet and head > Right Foot |
| `rightHand` | `PassengerHandConfig` ([fields](World.md#passengerhandconfig)) | Right hand's control mode, target/grip and support. Configure independently so one hand can hold the wheel while the other operates a lever. | `new PassengerHandConfig()` | Passenger Seat > Hands, feet and head > Right Hand |
| `seatId` | `string` | Identifier used by application code to choose this seat. Use distinct values such as driver or rearLeft; it does not place the seat or automatically grant driver controls. | `"Passenger"` | Passenger Seat > Seat ID |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` | Passenger Seat > Show Gizmos |
| `spawnOnStart` | `bool` | Lets this seat spawn/adopt its starting occupant when the parent Passengers hub also allows startup spawning. Turn off for a seat that should begin empty. | `true` | Passenger Seat > Spawn On Start |
| `spineAnchor` | `Transform` | Pelvis / seated spine origin, facing forward, Y up. | `None / unassigned` | Passenger Seat > Spine Anchor |
| `transformSupports` | `List<PassengerTransformSupport>` | Independent Spring/Parent bone-to-anchor supports for any controller or physics state. Original hierarchy/local pose restore on release. Call RefreshTransformSupports after runtime edits; see [support settings](World.md#passengertransformsupport). | Empty list | Passenger Seat > Custom supports > Transform Supports |



| Setting | Type | Description | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `onBeforeEnter` | `UnityEvent<PassengerBody>` | Before seat occupancy is acquired. The request is validated again after observers return. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Before Enter |
| `onEntered` | `UnityEvent<PassengerBody>` | After the passenger acquires this seat. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Entered |
| `onBeforeExit` | `UnityEvent<PassengerBody>` | Before seat occupancy is released, including ejection and disable paths. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Before Exit |
| `onExited` | `UnityEvent<PassengerBody, PassengerExitReason>` | After occupancy ends. Includes the released passenger and the exit reason. | `new UnityEvent<PassengerBody, PassengerExitReason>()` | Passenger Seat > Signals and callbacks > On Exited |
| `onBeforeEject` | `UnityEvent<PassengerBody>` | Before ejection releases occupancy or applies its impulse. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Before Eject |
| `onEjected` | `UnityEvent<PassengerBody>` | After successful ejection and its optional impulse. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Ejected |
| `onControllerChanged` | `UnityEvent<PassengerControllerType>` | After the seat switches to a different passenger controller. | `new UnityEvent<PassengerControllerType>()` | Passenger Seat > Signals and callbacks > On Controller Changed |
| `onResetRequested` | `UnityEvent<PassengerBody>` | When a custom occupant is asked to reset its seated pose. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Reset Requested |
| `onLimbReleased` | `UnityEvent<PassengerBodyPart>` | Invoked once when an individual hand or foot enters damage-released state. | `new UnityEvent<PassengerBodyPart>()` | Passenger Seat > Signals and callbacks > On Limb Released |
| `onHandsReleased` | `UnityEvent<PassengerBody>` | Once when both hands have entered the damage-released state. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Hands Released |
| `onFeetReleased` | `UnityEvent<PassengerBody>` | Once when both feet have entered the damage-released state. | `new UnityEvent<PassengerBody>()` | Passenger Seat > Signals and callbacks > On Feet Released |

## PassengerTransformSupport

Path: **Passenger Seat > Custom supports > Transform Supports > [ID / Label or indexed element] > [setting]**. The list supports +/− and drag reordering.

**Source:** `Runtime/World/Passengers/Seats/PassengerTransformSupport.cs`. Referenced configuration block; expand its owning field.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `active` | `bool` | Enable this support entry. | `true` | Passenger Seat > Custom supports > Transform Supports > [item] > Active |
| `anchor` | `Transform` | Vehicle target outside the occupant hierarchy. | Unassigned | Passenger Seat > Custom supports > Transform Supports > [item] > Anchor |
| `bodyTransform` | `Transform` | Occupant root/bone/child from a pre-placed Body or Body Prefab; prefab references resolve on the spawned occupant. | Unassigned | Passenger Seat > Custom supports > Transform Supports > [item] > Body Transform |
| `damper` | `float` | Position support damping. | `20`; minimum 0 | Passenger Seat > Custom supports > Transform Supports > [item] > Damper |
| `followAnchorRotation` | `bool` | Follow live anchor rotation. False retains target world rotation captured on attach/refresh, with Preserve World Pose and Rotation Offset applied. | `true` | Passenger Seat > Custom supports > Transform Supports > [item] > Follow Anchor Rotation |
| `id` | `string` | Optional case-sensitive ID/label unique within this seat; empty permits transform-only lookup. | Unassigned | Passenger Seat > Custom supports > Transform Supports > [item] > ID |
| `makeKinematic` | `bool` | Parent only: temporarily make this transform Rigidbody kinematic, leaving other bones simulated. | `true` | Passenger Seat > Custom supports > Transform Supports > [item] > Make Kinematic |
| `mode` | `PassengerAttachmentMode` | Parent holds this transform; Spring uses position/rotation support. | `Parent` | Passenger Seat > Custom supports > Transform Supports > [item] > Mode |
| `positionOffset` | `Vector3` | Position offset in anchor-local metres. | `Vector3.zero` | Passenger Seat > Custom supports > Transform Supports > [item] > Position Offset |
| `preserveWorldPose` | `bool` | Capture current world pose relative to the anchor instead of snapping; offsets apply afterwards. | `false` | Passenger Seat > Custom supports > Transform Supports > [item] > Preserve World Pose |
| `rotationDamper` | `float` | Rotation support damping. | `20`; minimum 0 | Passenger Seat > Custom supports > Transform Supports > [item] > Rotation Damper |
| `rotationOffset` | `Vector3` | Rotation offset in anchor-local degrees. | `Vector3.zero` | Passenger Seat > Custom supports > Transform Supports > [item] > Rotation Offset |
| `rotationSpring` | `float` | Rotation support spring strength. | `120`; minimum 0 | Passenger Seat > Custom supports > Transform Supports > [item] > Rotation Spring |
| `spring` | `float` | Position support spring strength. | `120`; minimum 0 | Passenger Seat > Custom supports > Transform Supports > [item] > Spring |

## PedalFootMode

**Source:** `Runtime/World/Passengers/IK/Handle/PedalHandle.cs`. Component configuration.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## PedalHandle

**Source:** `Runtime/World/Passengers/IK/Handle/PedalHandle.cs`. IK-only pedal contact. Press follows the moving contact; Rotation keeps the ankle fixed and aims the foot towards the pedal. Input and travel settings belong to PedalAnimator.

**Inherited settings:** `ControlHandle`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `ankleAnchor` | `Transform` | Fixed ankle position and reference frame for Rotation. Local Z points towards the toes, X is the pitch axis. | Pedal Handle > Ankle Anchor |
| `footMode` | `PedalFootMode` | Press (default) follows the pedal contact; Rotation pivots the foot at a fixed ankle. | Pedal Handle > Foot Mode |

## RagdollCollisionHelper

Configuration/implementation type for ragdoll collision helper within physical passengers and limb configuration.

**Source:** `Runtime/World/Damage/RagdollCollisionHelper.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `disableJointProjection` | `bool` | Disables native joint projection on the activated ragdoll to avoid projection-driven impact corrections. | `true` |
| `maximumAngularSpeed` | `float` | Maximum bone angular speed in radians/second. | `18`; Minimum: .1f |
| `maximumBoneSpeed` | `float` | Free-flight bone speed cap in metres/second; moving contacts temporarily raise this budget. | `12`; Minimum: .1f |
| `maximumCarrySpeed` | `float` | Maximum retained carry speed after contact ends, plus 2 m/s slack. During contact, the budget permits the actual surface speed so the car cannot overtake a capped bone. Fades after release; never applies a force. | `18`; Minimum: 0 |
| `maximumContactVelocityChange` | `float` | Additional normal impulse budget beyond closing speed, in units of bone mass times this velocity change. | `4`; Minimum: .01f |
| `maximumDepenetrationSpeed` | `float` | Free-ragdoll overlap correction cap in metres/second. During a moving-body contact the cap is at least the surface speed, bounded at 12 m/s for this temporary increase; the upward launch cap still applies. | `3`; Minimum: .1f |
| `maximumUpwardSpeed` | `float` | Upward speed cap prevents launch impulses while allowing the body to climb a hood. | `5`; Minimum: .1f |
| `minimumImpactSpeed` | `float` | Minimum incoming normal speed of the contacting body and relative impact required to knock down a standing character. Idle animation touching a parked body is not an impact. | `.1`; Minimum: 0 |
| `ragdollCollisionDetection` | `CollisionDetectionMode` | Native collision detection mode used by the dynamic ragdoll. | `CollisionDetectionMode.ContinuousDynamic` |
| `useSpeculativeContacts` | `bool` | Speculative contacts while standing/animated. Dynamic ragdolls keep Ragdoll Collision Detection to avoid ghost contacts at rest and preserve vehicle panel sweeps. | `true` |
| `vehicleContactFriction` | `float` | Friction used for the helper's bounded contacts with external dynamic bodies. | `.45`; Range: 0 to 1 |
| `vehicleDamageScale` | `float` | Scales collision speed used for vehicle damage; normal environment collisions remain unchanged. | `.05`; Range: 0 to 1 |
| `vehicleResponse` | `float` | Inverse-mass/inertia response of the other dynamic body for this contact only. Zero makes the contact one-way. | `0`; Range: 0 to 1 |

## RagdollCollisionRelay

Configuration/implementation type for ragdoll collision relay within physical passengers and limb configuration.

**Source:** `Runtime/World/Damage/RagdollCollisionRelay.cs`. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## Rocket

Owns launched-rocket motor, collision and lifetime behavior.

**Source:** `Runtime/World/Weapons/Rocket.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `acceleration` | `float` | Motor acceleration in m/s² along the captured launch direction while the motor is burning. Increase for faster speed buildup; Burn Seconds sets how long thrust lasts. | `80`; Minimum: 0 |
| `applyExplosionForce` | `bool` | Apply explosion impulse to rigidbodies. Effects and Exploded notification are independent. | `true` |
| `burnSeconds` | `float` | Seconds the rocket motor produces thrust after launch. Zero disables the powered burn; a longer burn keeps accelerating the rocket for longer. | `3`; Minimum: 0 |
| `detonateOnCollision` | `bool` | Automatically detonate on contact. Explicit Detonate calls remain available. | `true` |
| `engineLoop` | `AudioClip` | Continuous motor recording played on the launched rocket during its powered burn. It follows the rocket rather than staying at the launcher. | `None / unassigned` |
| `exhaustAnchor` | `Transform` | Engine nozzle: local +Z points out of the exhaust. Optional; defaults to the launch direction reversed. | `None / unassigned` |
| `exhaustPrefab` | `ParticleSystem` | Particle effect attached to the launched rocket for motor exhaust. It follows the rocket while the motor burns. | `None / unassigned` |
| `explosionImpulse` | `float` | Explosion impulse passed to nearby rigidbodies, in N·s. Higher values throw objects harder; distance within Explosion Radius affects the applied impulse. | `80000`; Minimum: 0 |
| `explosionMask` | `LayerMask` | Layers eligible for this rocket's blast overlap query. | `~0` |
| `explosionPrefab` | `ParticleSystem` | Particle effect spawned at detonation. This controls the visible blast; physical blast impulse and radius are configured separately. | `None / unassigned` |
| `explosionRadius` | `float` | Blast radius in metres used to find nearby rigidbodies when explosion force is enabled. Increase to affect a wider area around detonation. | `12`; Minimum: 0 |
| `explosionSound` | `AudioClip` | One-shot played at the rocket's detonation point. It accompanies the explosion effect and remains separate from physical blast force. | `None / unassigned` |
| `explosionUpwardModifier` | `float` | Downward shift in metres of the effective blast origin used for force direction. Larger values make the explosion throw objects upward more strongly; the visual explosion remains at the hit point. | `.5`; Minimum: 0 |
| `inheritVehicleVelocity` | `bool` | Adds the launch point's vehicle velocity to the rocket's launch velocity. Enable so a rocket fired from a moving/rotating vehicle starts with that motion. | `true` |
| `launchDirection` | `Transform` | Optional transform whose forward axis aims the rocket at launch. If empty, the rocket object's own forward axis is used. | `None / unassigned` |
| `launchSound` | `AudioClip` | One-shot played when the rocket launches. Use it for the initial ignition or launch blast, separately from the sustained motor loop. | `None / unassigned` |
| `launchSpeed` | `float` | Initial forward launch speed in metres per second, before any inherited vehicle velocity. | `65`; Minimum: 0 |
| `lifetime` | `float` | Maximum seconds a launched rocket can remain in the scene. It is removed after this time even if it has not hit anything, preventing missed rockets from accumulating. | `12`; Minimum: .1f |
| `mass` | `float` | Rigidbody mass in kilograms of the launched rocket. It affects collision and impulse response; motor acceleration is configured separately. | `35`; Minimum: .01f |
| `useGravity` | `bool` | Enables gravity on the launched rocket's Rigidbody. Turn off for a rocket that should not drop under gravity after motor burnout. | `true` |


### Audio Settings groups

| Field | Type | Behavior |
| --- | --- | --- |
| `audioSettings` | `VehicleAudioSettings` | Reusable [VehicleAudioSettings](Effects.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `explosionAudioSettings` | `VehicleAudioSettings` | Reusable [VehicleAudioSettings](Effects.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `launchAudioSettings` | `VehicleAudioSettings` | Reusable [VehicleAudioSettings](Effects.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |

## RocketLauncher

Selects and launches configured mounted rocket stores.

**Source:** `Runtime/World/Weapons/RocketLauncher.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `automatic` | `bool` | Repeats firing while the firing request remains active; otherwise uses discrete launch requests. | `false` |
| `fireInterval` | `float` | Minimum seconds between rocket launches. Increase for a slower salvo; decrease to launch the remaining rockets more rapidly. | `.4`; Minimum: 0 |
| `firingEnabled` | `bool` | Allows this launcher to accept fire requests. Turn off to keep the rockets mounted and stop held-trigger firing. | `true` |
| `rockets` | `Rocket[]` ([fields](World.md#rocket)) | Mounted rockets available for launch, checked in list order. Fired or unavailable entries are skipped; each Rocket supplies its own motor and explosion settings. | `Empty list` |

## RotaryHandle

**Source:** `Runtime/World/Passengers/IK/Handle/RotaryHandle.cs`. IK palm contact for a rotary knob or hand lever. Inherits ControlHandle. Set its anchor on the moving grip; configure value and motion on the animator.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## SeatAccess

Main Seat / Door are at component top. Side, profiles, Outside and Doorway are under **Per-seat animation and side**. Other geometry/admission/door limits are under **Settings**. Directional events are under **Signals and callbacks** above **Gizmos**; **Select outside marker** is below Gizmos.

Describes the seat endpoint, outside marker, door and admission settings.

**Source:** `Runtime/World/Passengers/Access/SeatAccess.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `animationProfile` | `AccessAnimationProfile` ([fields](World.md#accessanimationprofile)) | Boarding animation calibration for this seat. Use it to select clips, state names and placement adaptation suitable for this cabin and approach side. | `None / unassigned` | Seat Access > Per-seat animation and side > Animation Profile |
| `clearanceHeight` | `float` | Height in metres of the exit-clearance capsule. Match it to the standing character so a low ceiling can block an unsafe exit. | `1.7`; Minimum: .5f | Seat Access > Settings > Clearance Height |
| `clearanceMask` | `LayerMask` | Layers tested when checking whether access space is blocked. | `~0` | Seat Access > Settings > Clearance Mask |
| `clearanceRadius` | `float` | Radius in metres of the standing-space capsule checked at the exit point. Increase to reserve more sideways space around the exiting character. | `.25`; Minimum: .1f | Seat Access > Settings > Clearance Radius |
| `closedDoorTolerance` | `float` | Allowed angle difference in degrees from fully closed when checking door completion. A small tolerance avoids waiting forever for a physical hinge to settle exactly at zero. | `3`; Range: 0 to 180 | Seat Access > Settings > Closed Door Tolerance |
| `door` | `VehicleBodyPart` ([fields](Exterior.md#vehiclebodypart)) | Optional door opened before entry/exit and checked against its target angle. Leave empty for an open vehicle with no door to wait for. | `None / unassigned` | Seat Access > Door |
| `doorTimeout` | `float` | Maximum time in seconds allowed for the door to reach the required access position. | `2`; Minimum: .1f | Seat Access > Settings > Door Timeout |
| `doorway` | `Transform` | Optional intermediate doorway marker for adapting the path between the outside position and the seated pose. Place it in the opening the character should pass through. | `None / unassigned` | Seat Access > Per-seat animation and side > Doorway |
| `duration` | `float` | Fallback access duration in seconds for the seat's entry/exit sequence. The assigned access-motion implementation may use calibrated clip timing instead. | `1.6`; Minimum: .1f | Seat Access > Settings > Duration |
| `groundProbeDistance` | `float` | Length in metres of the downward ray used to ground the outside position. It must reach from the raised probe origin to the expected terrain. | `5`; Minimum: .1f | Seat Access > Settings > Ground Probe Distance |
| `groundProbeHeight` | `float` | Height in metres above the outside point at which the downward ground ray starts. Increase when terrain beside the vehicle can lie above that point. | `2`; Minimum: .1f | Seat Access > Settings > Ground Probe Height |
| `interactionDistance` | `float` | Maximum character-to-outside-point distance in metres for starting entry. Increase to allow boarding from farther away; exit still checks its own free-space conditions. | `2`; Minimum: .1f | Seat Access > Settings > Interaction Distance |
| `maximumAngularSpeed` | `float` | Maximum vehicle angular speed in radians per second during entry/exit. | `.5`; Minimum: 0 | Seat Access > Settings > Maximum Angular Speed |
| `maximumGroundDrop` | `float` | Largest permitted downward projection from the authored outside point, in metres. | `2`; Minimum: 0 | Seat Access > Settings > Maximum Ground Drop |
| `maximumGroundRise` | `float` | Largest permitted upward projection from the authored outside point, in metres. | `.5`; Minimum: 0 | Seat Access > Settings > Maximum Ground Rise |
| `maximumSpeed` | `float` | Maximum vehicle point speed in m/s during entry/exit. | `.5`; Speed field; stored in m/s, displayed in the selected speed unit | Seat Access > Settings > Maximum Speed |
| `minimumGroundNormal` | `float` | Minimum upward ground normal for outside placement; 0.5 accepts slopes up to 60 degrees. | `.5`; Range: 0 to 1 | Seat Access > Settings > Minimum Ground Normal |
| `openDoorAnimationProfile` | `AccessAnimationProfile` ([fields](World.md#accessanimationprofile)) | Optional profile for a door already open at admission. Falls back to Animation Profile. The door remains open and clips need no door events. | `None / unassigned` | Seat Access > Per-seat animation and side > Open Door Animation Profile |
| `openDoorTolerance` | `float` | Allowed angle difference in degrees from the door's fully open angle before access may proceed. Increase to let boarding begin before the door reaches its exact stop. | `8`; Range: 0 to 180 | Seat Access > Settings > Open Door Tolerance |
| `outside` | `Transform` | Feet-level endpoint. Runtime never moves this transform. | `None / unassigned` | Seat Access > Per-seat animation and side > Outside |
| `outsideGroundClearance` | `float` | Height in metres added above the sampled ground for the outside standing point. A small positive value keeps the character from starting inside the floor. | `.02`; Minimum: 0 | Seat Access > Settings > Outside Ground Clearance |
| `projectOutsideToGround` | `bool` | Projects the outside access pose onto acceptable ground using the configured ground probe. | `true` | Seat Access > Settings > Project Outside To Ground |
| `seat` | `PassengerSeat` ([fields](World.md#passengerseat)) | Seat reached through this access route. It supplies the occupant, seated anchor and eligibility checks; if empty, the component looks on the same GameObject. | `None / unassigned` | Seat Access > Seat |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` | Seat Access > Show Gizmos |
| `side` | `AccessSide` | Descriptive side label; the assigned profile selects the actual clips and triggers. Options: `Left`, `Right`, `Custom`. | `Left` | Seat Access > Per-seat animation and side > Side |
| `standingOffset` | `Vector3` | Optional offset from Outside in this seat's local axes. | `Zero-initialized Vector3` | Seat Access > Settings > Standing Offset |
| `useOutsideRotation` | `bool` | Uses Outside's orientation when aligning the character beside the vehicle. Turn off when the access motion should derive its approach orientation without this authored rotation. | `true` | Seat Access > Settings > Use Outside Rotation |



| Setting | Type | Description | Default | Inspector path |
| --- | --- | --- | --- | --- |
| `onEnterBegin` | `UnityEvent` | Invoked when an admitted enter operation begins for this access path. | `new UnityEvent()` | Seat Access > Signals and callbacks > On Enter Begin |
| `onEnterInProgress` | `UnityEvent<float>` | Normalized enter motion progress (0..1). One does not imply door cleanup has finished. | `new UnityEvent<float>()` | Seat Access > Signals and callbacks > On Enter In Progress |
| `onEnterFinish` | `UnityEvent` | Invoked after the entire enter operation succeeds, including door cleanup. | `new UnityEvent()` | Seat Access > Signals and callbacks > On Enter Finish |
| `onEnterCancelled` | `UnityEvent` | Invoked when a reserved enter operation is cancelled or fails. Rejected requests do not invoke it. | `new UnityEvent()` | Seat Access > Signals and callbacks > On Enter Cancelled |
| `onExitBegin` | `UnityEvent` | Invoked when an admitted exit operation begins for this access path. | `new UnityEvent()` | Seat Access > Signals and callbacks > On Exit Begin |
| `onExitInProgress` | `UnityEvent<float>` | Normalized exit motion progress (0..1). One does not imply door cleanup has finished. | `new UnityEvent<float>()` | Seat Access > Signals and callbacks > On Exit In Progress |
| `onExitFinish` | `UnityEvent` | Invoked after the entire exit operation succeeds, including door cleanup. | `new UnityEvent()` | Seat Access > Signals and callbacks > On Exit Finish |
| `onExitCancelled` | `UnityEvent` | Invoked when a reserved exit operation is cancelled or fails. Rejected requests do not invoke it. | `new UnityEvent()` | Seat Access > Signals and callbacks > On Exit Cancelled |

## SteeringHandRegrip

Coordinates steering contacts, availability and external reservations.

**Source:** `Runtime/World/Passengers/IK/Regrip/SteeringHandRegrip.cs`. Component / asset.

**Inherited settings:** [PassengerBehaviour](World.md#passengerbehaviour). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `surface` | `SteeringWheelHandle` ([fields](World.md#steeringwheelhandle)) | SteeringWheelHandle describing the rim and palm contacts to regrip. It must describe the same wheel transform animated by Wheel Animator. | `None / unassigned` | Steering Hand Regrip > Surface |
| `wheelAnimator` | `SteeringWheelAnimator` ([fields](Interior.md#steeringwheelanimator)) | Animator supplying the wheel's actual displayed angle and steering demand. These values decide when a hand must release and catch a new part of the rim. | `None / unassigned` | Steering Hand Regrip > Wheel Animator |

## SteeringHandRegripSettings

Configuration/implementation type for steering hand regrip settings within grip fitting and steering ownership.

**Source:** `Runtime/World/Passengers/IK/Regrip/SteeringHandRegripSettings.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `guideAdjustmentSpeed` | `float` | Maximum guide grasp adjustment along the rim, in degrees per second. Wheel-following itself is never filtered. | `240`; Minimum: 30 | Steering Hand Regrip Settings > Guide Adjustment Speed |
| `leftRestAngle` | `float` | Lower rim angles for the relaxed thumb/index support; measured in the unturned wheel plane. | `250` | Steering Hand Regrip Settings > Left Rest Angle |
| `minimumHandSeparation` | `float` | Minimum angular spacing in degrees kept between hand contacts around the rim. | `75`; Range: 0 to 180 | Steering Hand Regrip Settings > Minimum Hand Separation |
| `palmReturnTime` | `float` | Minimum time for a full palm-pressure-to-wrapped-grip blend while the released wheel unwinds. | `.35`; Minimum: .1f | Steering Hand Regrip Settings > Palm Return Time |
| `reachAdjustment` | `float` | Search around each preferred angle for a reachable wrist pose. | `20`; Range: 0 to 35 | Steering Hand Regrip Settings > Reach Adjustment |
| `reachMargin` | `float` | Safety margin subtracted from the hand's measured arm reach, in metres. | `.012`; Minimum: 0 | Steering Hand Regrip Settings > Reach Margin |
| `rightRestAngle` | `float` | Right hand's preferred resting position around the rim, in degrees. The regrip planner uses it when returning that hand to its normal grip. | `290` | Steering Hand Regrip Settings > Right Rest Angle |

## SteeringWheelHandle

Describes steering contacts, surface geometry and hand participation.

**Source:** `Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs`. Component / asset.

**Inherited settings:** [VehicleHandle](World.md#vehiclehandle). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `allowHandRegrip` | `bool` | Allow automatic hand repositioning and column support while steering. Disable for fixed handlebar grips. | `true` | Steering Wheel Handle > Behaviour > Allow Hand Regrip |
| `authoredTargets` | `bool` | Keep manually authored palm anchors instead of regenerating wheel-rim contacts. Use for control sticks. | `false` | Steering Wheel Handle > Behaviour > Authored Targets |
| `center` | `Vector3` | Steering-wheel rim centre in the handle's local space. | `Zero-initialized Vector3` | Steering Wheel Handle > Behaviour > Center |
| `customRim` | `RimSample[]` ([fields](World.md#steeringwheelhandlerimsample)) | Optional closed centerline for flat-bottomed or irregular wheels. At least three samples. | `Empty list` | Steering Wheel Handle > Behaviour > Custom Rim |
| `gripMode` | `SteeringGripMode` | Chooses which hands may use this wheel: both, only left, only right, or neither. Released removes wheel targets without disabling the steering-wheel visual. Options: `BothHands`, `LeftHand`, `RightHand`, `Released`. | `SteeringGripMode.BothHands` | Steering Wheel Handle > Grip Mode |
| `leftAngle` | `float` | Left hand's contact angle around the wheel rim in degrees. Adjust to choose where that hand initially holds the wheel; regripping can move it during play. | `180`; Range: 0 to 360 | Steering Wheel Handle > Behaviour > Left Angle |
| `leftTarget` | `Transform` | Transform updated to the calculated left palm contact pose. One is created when empty; the passenger's left hand can use it as its reach target. | `None / unassigned` | Steering Wheel Handle > Left Target |
| `pinchHandPosition` | `int` | Hand Positions entry used for the thumb/index pinch. | `2`; Minimum: 0 | Steering Wheel Handle > Pinch Hand Position |
| `pressureHandPosition` | `int` | Hand Positions entry used for palm pressure, blended by the steering policy. | `1`; Minimum: 0 | Steering Wheel Handle > Pressure Hand Position |
| `regrip` | `SteeringHandRegripSettings` ([fields](World.md#steeringhandregripsettings)) | Timing and contact rules for lifting and repositioning hands during large steering-wheel turns. Expand to tune when each hand lets go and catches the rim again. | `new SteeringHandRegripSettings()` | Steering Wheel Handle > Behaviour > Regrip |
| `reverseApproach` | `bool` | The wheel-local direction away from the driver is +Z. Reverse for a backwards pivot. | `false` | Steering Wheel Handle > Behaviour > Reverse Approach |
| `rightAngle` | `float` | Right hand's contact angle around the wheel rim in degrees. Set independently from Left Angle for a natural two-hand starting grip. | `0`; Range: 0 to 360 | Steering Wheel Handle > Behaviour > Right Angle |
| `rightTarget` | `Transform` | Transform updated to the calculated right palm contact pose. One is created when empty; the passenger's right hand uses it when the grip mode permits. | `None / unassigned` | Steering Wheel Handle > Right Target |
| `rimRadius` | `float` | Distance in metres from the wheel centre to the centre of its rim tube. Match the visible rim so generated palm and finger contacts lie on it. | `.1744`; Minimum: .02f | Steering Wheel Handle > Behaviour > Rim Radius |
| `showFingerContacts` | `bool` | Draws finger contact guides in the Scene view for grip calibration. Turning it off hides these guides without disabling finger fitting. | `true` | Steering Wheel Handle > Show Finger Contacts |
| `stickGrip` | `bool` | Fit fingers and thumb around Grip Diameter at the authored palm anchors. | `false` | Steering Wheel Handle > Behaviour > Stick Grip |
| `tubeDepthRadius` | `float` | Fore/aft tube radius. Zero uses a circular section equal to Tube Radius. | `0`; Minimum: 0 | Steering Wheel Handle > Behaviour > Tube Depth Radius |
| `tubeRadius` | `float` | Radius of the rim tube, not its diameter. | `.016`; Minimum: .002f | Steering Wheel Handle > Behaviour > Tube Radius |
| `useAnchorStartPosition` | `bool` | Use assigned anchors as starting and return grips while allowing regrip. Preserves position and rotation offsets, skips reach adjustment, and takes precedence over Authored Targets. | `false` | Steering Wheel Handle > Behaviour > Use Anchor Start Position |
| `varyGripWithSteering` | `bool` | Select or blend the saved pressure/pinch poses while steering; no runtime closure factor is applied. | `true` | Steering Wheel Handle > Behaviour > Vary Grip With Steering |

## SteeringWheelHandle.RimSample

Value data for rim sample; its fields are listed below.

**Source:** `Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints | Inspector path |
| --- | --- | --- | --- | --- |
| `position` | `Vector3` | Point on the custom rim centreline in the steering-wheel transform's local coordinates. Order the points around the rim; the closed path replaces the normal circular rim. | `Zero-initialized Vector3` | Steering Wheel Handle > Position |
| `radius` | `float` | Rim tube radius in metres at this custom centreline point. It controls the thickness fingers fit around; it is separate from the overall steering-wheel radius. | `0`; Minimum: .001f | Steering Wheel Handle > Radius |

## SwitchHandle

**Source:** `Runtime/World/Passengers/IK/Handle/SwitchHandle.cs`. IK-only hand contact for a switch. Inherits ControlHandle. Detents, events and motion belong to SwitchAnimator.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## ThrottleHandle

**Source:** `Runtime/World/Passengers/IK/Handle/ThrottleHandle.cs`. IK-only contact for a throttle grip. Inherits ControlHandle; all geometry and value writes belong to ThrottleAnimator.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## Trailer

Stores the towed-body connection and brake-following behavior.

**Source:** `Runtime/World/Towing/Trailer.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `followHandbrake` | `bool` | Forward the towing vehicle's handbrake. Detached parking is controlled separately. | `true` |
| `followServiceBrake` | `bool` | Forward the towing vehicle's resolved service brake to this trailer. | `true` |
| `hitch` | `Transform` | World-space coupling point used to align the trailer connection. | `None / unassigned` |
| `parkWhenDetached` | `bool` | Applies the trailer's parking request while no towing vehicle is connected. Turn off if an uncoupled trailer should be free to roll. | `true` |
| `serviceBrakeMultiplier` | `float` | Multiplier for forwarded service braking; final demand is clamped to 0–1. | `1`; Minimum: 0 |

## VehicleHandle

**Control Mode** selects IK, Animator + IK, Animator or Custom independently of the seat. IK modes show limb pose/Hands settings. Animator modes show **Animator controller**, grouped into **Passenger and Animator**, **Continuous value**, **Gesture**, **IK contact clip**, **Animation Event names** and **Gesture signals and callbacks**. An IK handle can enable **Contact / gesture animation** to show its optional authored clip configuration. See [the tutorial](../HandleAnimation.md#tutorial-handle-owned-animator) for complete field paths and clip setup.


**Source:** `Runtime/World/Passengers/IK/Handle/VehicleHandle.cs`. Component configuration.

**Inherited settings:** `MonoBehaviour`, `IHandle`.

| Setting | Type | Meaning | Inspector path |
| --- | --- | --- | --- |
| `adaptiveGrip` | `bool` | Fit fingers around this handle. Applies to hands only; foot anchors are unaffected. | Vehicle Handle > Behaviour > Adaptive Grip |
| `allowedLimbs` | `HandleLimbs` | Flags selecting the hands/feet allowed to use this handle. | Vehicle Handle > Allowed Limbs |
| `angularDamper` | `float` | Damping for angular damper. Higher values oppose relative motion more strongly. Initial value: `20`. | Vehicle Handle > Angular Damper |
| `angularSpring` | `float` | Restoring stiffness for angular spring. Higher values resist displacement more strongly. Initial value: `500`. | Vehicle Handle > Angular Spring |
| `animationValue` | `Vector3` | Vector signal writable by animation/Timeline/application code. Its meaning and units belong to the application. | Vehicle Handle > Signals and callbacks > Animation Value |
| `defaultHandPosition` | `int` | Index of the normal grip configuration. | Vehicle Handle > Default Hand Position |
| `fingerBlendDuration` | `float` | Seconds to blend displayed finger rotations from the previous handle to this handle after rebind. Default 0.12; zero opts out. Controller travel retains the current pose. Initial seating and editor previews apply immediately. | Vehicle Handle > Behaviour > Finger Blend Duration |
| `gripDiameter` | `float` | Grip diameter in metres in the palm anchor's local space. The cylinder runs along anchor X, with its centre towards +Y from the palm contact. | Vehicle Handle > Behaviour > Grip Diameter |
| `handPositions` | `HandleHandPosition[]` | Named local/shared configurations. Empty older data is initialized from type-specific defaults. | Vehicle Handle > Hand Positions |
| `id` | `string` | Unique, case-sensitive ID used by EngineAudio's runtime API. | Vehicle Handle > ID |
| `leftFootPose` | `HandlePoseSettings` | Independent left-foot pose, target and contact settings. Finger weight is unused for feet. | Vehicle Handle > Limb IK, animation and contact > Left Foot Pose |
| `leftHandPose` | `HandlePoseSettings` | Independent left-hand pose, target and contact settings. Weights default to one. | Vehicle Handle > Limb IK, animation and contact > Left Hand Pose |
| `maximumPalmForce` | `float` | Force/torque budget for maximum palm force; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `90`. | Vehicle Handle > Maximum Palm Force |
| `maximumTorque` | `float` | Force/torque budget for maximum torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `25`. | Vehicle Handle > Maximum Torque |
| `minimumAttachments` | `int` | Minimum other held limbs left on this source before borrowing one, evaluated separately for each seat. | Vehicle Handle > Minimum Attachments |
| `observeRotation` | `bool` | Observe local Euler degrees (true, default) or local position units (false). Euler values wrap at 360 degrees. | Vehicle Handle > Signals and callbacks > Observe Rotation |
| `onContactEnded` | `UnityEvent<HandleContactContext>` | Inspector-configurable counterpart of ContactEnded. Runs after the C# event for the same phase. | Vehicle Handle > Signals and callbacks > On Contact Ended |
| `onContactStarted` | `UnityEvent<HandleContactContext>` | Inspector-configurable counterpart of ContactStarted. Runs after the C# event for the same phase. | Vehicle Handle > Signals and callbacks > On Contact Started |
| `onContactUpdated` | `UnityEvent<HandleContactContext>` | Inspector-configurable counterpart of ContactUpdated. Runs after the C# event for the same phase. | Vehicle Handle > Signals and callbacks > On Contact Updated |
| `onValueChangeStarted` | `UnityEvent<HandleValueContext>` | Inspector-configurable counterpart of ValueChangeStarted. Runs after the C# event for the same phase. | Vehicle Handle > Signals and callbacks > On Value Change Started |
| `onValueChangeStopped` | `UnityEvent<HandleValueContext>` | Inspector-configurable counterpart of ValueChangeStopped. Runs after the C# event for the same phase. | Vehicle Handle > Signals and callbacks > On Value Change Stopped |
| `onValueChanging` | `UnityEvent<HandleValueContext>` | Inspector-configurable counterpart of ValueChanging. Runs after the C# event for the same phase. | Vehicle Handle > Signals and callbacks > On Value Changing |
| `positionDamper` | `float` | Damping for position damper. Higher values oppose relative motion more strongly. Initial value: `60`. | Vehicle Handle > Position Damper |
| `positionSpring` | `float` | Restoring stiffness for position spring. Higher values resist displacement more strongly. Initial value: `2000`. | Vehicle Handle > Position Spring |
| `rightFootPose` | `HandlePoseSettings` | Independent right-foot pose, target and contact settings. Finger weight is unused for feet. | Vehicle Handle > Limb IK, animation and contact > Right Foot Pose |
| `rightHandPose` | `HandlePoseSettings` | Independent right-hand pose, target and contact settings. Weights default to one. | Vehicle Handle > Limb IK, animation and contact > Right Hand Pose |
| `showGizmos` | `bool` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. | Vehicle Handle > Show Gizmos |
| `use` | `HandleUseSettings` | Automatic action policy and explicit/automatic transfer timing for this destination. | Vehicle Handle > Actions |
| `useAnimationValue` | `bool` | Observe animationValue instead of the built-in/transform value source; default false. | Vehicle Handle > Signals and callbacks > Use Animation Value |
| `valueChangeThreshold` | `float` | Euclidean change threshold in source-value units, default 0.0001. Small changes accumulate against the last significant sample. | Vehicle Handle > Signals and callbacks > Value Change Threshold |
| `valueStopDelay` | `float` | Seconds without significant change before automatic Stop; default 0.08. Explicit manual activity ends through EndValueChange. | Vehicle Handle > Signals and callbacks > Value Stop Delay |
| `valueTransform` | `Transform` | Optional externally animated transform to observe when useAnimationValue is false; otherwise use the concrete handle source. | Vehicle Handle > Signals and callbacks > Value Transform |

## WaterInteraction

Connects vehicle water sampling and hull contact state.

**Source:** `Runtime/World/Water/WaterInteraction.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `hullHalfSize` | `Vector2` | Half-width / half-length in metres, shared by water audio and particle contact points. | `new Vector2(1, 2.5)` |
| `useProfileFallback` | `bool` | Allow the Boat profile's flat water when no explicit provider is assigned. | `true` |
| `waterInteractionEnabled` | `bool` | Master switch for water interaction: buoyancy, water audio and water particles. | `true` |
| `waterProvider` | `WaterProvider` ([fields](World.md#waterprovider)) | Explicit source of water height and motion samples for this vehicle. Assign it to use a particular water body instead of automatic provider selection. | `None / unassigned` |

## WaterProvider

Abstract sampling adapter and `WaterSample` data contract.

**Source:** `Runtime/World/Water/WaterProvider.cs`. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## WaterSurfaceProfile

Configuration/implementation type for water style within water sampling and movement.

**Source:** `Runtime/World/Water/WaterSurfaceProfile.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `deepColor` | `Color` | Water colour used for deeper-looking areas. Its alpha also participates in the material's transparency; it changes appearance, not physical depth. | `new Color(.025, .15, .34, 1)` |
| `depthAbsorption` | `float` | Strength of depth-based water-color absorption. | `.3`; Minimum: .01f |
| `foamColor` | `Color` | Tint and transparency of surface/shoreline foam drawn by the water material. It does not change separate foam particle systems. | `new Color(.7, .88, .87, 1)` |
| `reflectionStrength` | `float` | Multiplier for the water material's reflection contribution. | `.8`; Range: 0 to 1 |
| `rippleScale` | `float` | Spatial scale passed to the water shader for its small surface ripple pattern. It changes the visible pattern rather than the sampled buoyancy wave height. | `.055`; Minimum: .001f |
| `rippleStrength` | `float` | Visible small-ripple contribution to the water surface. | `.13`; Range: 0 to 1 |
| `roughness` | `float` | Shader roughness controlling how sharp the water's reflected highlights appear. Increase for softer, duller reflections; decrease for a smoother, glossier surface. | `.34`; Range: 0 to 1 |
| `shallowColor` | `Color` | Water colour used where the depth shader sees nearby ground. Use a lighter or clearer colour to make shallow shore areas distinct. | `new Color(.065, .32, .52, 1)` |
| `shorelineFoam` | `float` | Amount of depth/shoreline foam produced by the water shader. | `.55`; Range: 0 to 1 |
| `waveA` | `Vector4` | Direction X/Z, wavelength in metres, amplitude in metres. Shared by CPU sampling and shader. | `new Vector4(.85, .52, 22, .09)` |
| `waveB` | `Vector4` | Second wave: X/Z direction in the first two components, wavelength in metres in Z, and amplitude in metres in W. | `new Vector4(-.4, .92, 11, .045)` |
| `waveSpeed` | `float` | Multiplier for wave phase speed shared by CPU surface sampling and shader animation. | `.65`; Minimum: 0 |

## WaterSurface

Built-in water-surface provider implementation.

**Source:** `Runtime/World/Water/WaterSurface.cs`. Component / asset.

**Inherited settings:** [WaterProvider](World.md#waterprovider). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `animateWaves` | `bool` | Enables time-varying wave height and normal instead of a flat surface. | `true` |
| `depthEffectsEnabled` | `bool` | Uses existing camera depth if available; no camera/depth/opaque passes are requested by this component. | `true` |
| `generateGrid` | `bool` | Generate a bounded grid for vertex waves. Disable to retain your authored mesh. | `true` |
| `gridCellSize` | `float` | Grid-cell size in metres for the generated water mesh; smaller cells create a denser mesh. | `5`; Minimum: .5f |
| `materialOverride` | `Material` | Explicit water material; leave empty to retain the material authored on the renderer. | `None / unassigned` |
| `reflectionsEnabled` | `bool` | Allows the material's reflection contribution. Turn off to remove that appearance while keeping water sampling, waves and the surface itself active. | `true` |
| `renderSurface` | `bool` | Shows the water mesh while Water Enabled is on. Turn off for invisible water that still supplies physical water samples. | `true` |
| `size` | `Vector2` | Water surface width and length in metres. | `new Vector2(400, 640)` |
| `style` | `WaterSurfaceProfile` ([fields](World.md#watersurfaceprofile)) | Shared asset defining water colours, ripple appearance and other surface styling. Use it to keep several water surfaces visually consistent. | `None / unassigned` |
| `surfaceRenderer` | `MeshRenderer` | MeshRenderer used to display this water body's material. The component controls its visibility and material properties while active. | `None / unassigned` |
| `waterEnabled` | `bool` | Enables this water provider's sampling and visible surface. Turn off to make it unavailable to buoyancy/water-contact queries as well as hide its renderer. | `true` |

## WeaponBarrel

Owns muzzle aiming, trigger/cooldown admission and projectile initialization.

**Source:** `Runtime/World/Weapons/WeaponBarrel.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `fireMode` | `WeaponFireMode` | Single fires on a new trigger press; Automatic continues requesting shots while the trigger is held, respecting the reload interval. Options: `Single`, `Automatic`. | `Single` |
| `firingEnabled` | `bool` | Allows projectile creation when the weapon is ready. Turn off to block fire requests without disabling its aiming mechanism. | `true` |
| `impactImpulse` | `float` | Impact impulse in N·s passed to each spawned projectile. The projectile uses it to push the Rigidbody it hits; it does not set muzzle velocity or recoil. | `20000`; Minimum: 0 |
| `inheritVehicleVelocity` | `bool` | Adds the vehicle's velocity at the muzzle to the shot's initial velocity. This keeps shots consistent when the vehicle is moving or turning. | `true` |
| `movement` | `MovingPart` ([fields](Exterior.md#movingpart)) | MovingPart used to aim/elevate this barrel. Rotation input and aiming requests are forwarded to it; firing still uses the Muzzle transform's actual pose. | `None / unassigned` |
| `muzzle` | `Transform` | ProjectileDemo spawn point and firing direction. Place it at the barrel exit with local forward pointing along the shot. | `None / unassigned` |
| `muzzleSpeed` | `float` | Initial projectile speed at the muzzle in metres per second. | `110`; Minimum: .1f |
| `projectileLifetime` | `float` | Maximum seconds a spawned projectile can remain alive without a hit. Increase for long-range shots; decrease to remove missed projectiles sooner. | `12`; Minimum: .01f |
| `projectilePrefab` | `MonoBehaviour` | A prefab component implementing IWeaponProjectile. ProjectileDemo behavior belongs to your game. | `None / unassigned` |
| `shotsPerSecond` | `float` | Maximum firing cadence in shots per second. | `.4`; Minimum: .01f |

## WorldModule

Configuration/implementation type for world module within module lifecycle and scheduling.

**Source:** `Runtime/World/Core/WorldModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [VehicleModule](Common.md#vehiclemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## YokeHandle

Describes steering contacts, surface geometry and hand participation.

**Source:** `Runtime/World/Passengers/IK/Handle/YokeHandle.cs`. Component / asset.

**Inherited settings:** [SteeringWheelHandle](World.md#steeringwheelhandle). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

Orbit avoidance is off by default. Enable its master switch, then choose ground, ordinary obstacles and/or other vehicles; see [camera setup](../Cameras.md#optional-orbit-obstruction-avoidance).
