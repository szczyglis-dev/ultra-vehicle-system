# Limb handles and transfers API

Read [the system explanation](../Scripting/Handles.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [AnchorHandle](Handles.md#anchorhandle)
- [AnchorHandleMode](Handles.md#anchorhandlemode)
- [ControlHandle](Handles.md#controlhandle)
- [GearLeverHandle](Handles.md#gearleverhandle)
- [GearPaddleHandle](Handles.md#gearpaddlehandle)
- [HandleActionSource](Handles.md#handleactionsource)
- [HandleAnimatorBinding](Handles.md#handleanimatorbinding)
- [HandleContactContext](Handles.md#handlecontactcontext)
- [HandleContactSource](Handles.md#handlecontactsource)
- [HandleController](Handles.md#handlecontroller)
- [HandleCurlAxis](Handles.md#handlecurlaxis)
- [HandleFinger](Handles.md#handlefinger)
- [HandleFingerPosition](Handles.md#handlefingerposition)
- [HandleFingerSegment](Handles.md#handlefingersegment)
- [HandleHandPose](Handles.md#handlehandpose)
- [HandleHandPosition](Handles.md#handlehandposition)
- [HandleHandPositionProfile](Handles.md#handlehandpositionprofile)
- [HandleHandSide](Handles.md#handlehandside)
- [HandleInput](Handles.md#handleinput)
- [HandleLimbs](Handles.md#handlelimbs)
- [HandlePoseSettings](Handles.md#handleposesettings)
- [HandleThumbAim](Handles.md#handlethumbaim)
- [HandleUse](Handles.md#handleuse)
- [HandleUsePhase](Handles.md#handleusephase)
- [HandleUseSettings](Handles.md#handleusesettings)
- [HandleValueContext](Handles.md#handlevaluecontext)
- [IHandle](Handles.md#ihandle)
- [JoystickHandle](Handles.md#joystickhandle)
- [MotorcycleHandle](Handles.md#motorcyclehandle)
- [PedalFootMode](Handles.md#pedalfootmode)
- [PedalHandle](Handles.md#pedalhandle)
- [RotaryHandle](Handles.md#rotaryhandle)
- [SteeringWheelHandle](Handles.md#steeringwheelhandle)
- [SteeringWheelHandle.RimSample](Handles.md#steeringwheelhandlerimsample)
- [SteeringWheelHandle.SteeringGripMode](Handles.md#steeringwheelhandlesteeringgripmode)
- [SwitchHandle](Handles.md#switchhandle)
- [ThrottleHandle](Handles.md#throttlehandle)
- [HandleControlMode](Handles.md#handlecontrolmode)
- [HandleAnimatorController](Handles.md#handleanimatorcontroller)
- [HandleAnimationEvents](Handles.md#handleanimationevents)
- [VehicleHandle](Handles.md#vehiclehandle)
- [YokeHandle](Handles.md#yokehandle)

## AnchorHandle

**Runtime/World/Passengers/IK/Handle/AnchorHandle.cs**

Exposes authored hand/foot anchors without control animation.

**Inherits / implements:** [VehicleHandle](Handles.md#vehiclehandle).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform anchor` | Authored palm/ankle contact. Keep it on the stationary grip frame for ClosureChange. |
| `public float closedDistance` | Distance in metres giving full closure at multiplier 1; default 0.03. |
| `public Vector3 closureAngles` | Additional base/middle/tip flexion in degrees; default (20, 35, 25). Thumb excluded. |
| `public float closureMultiplier` | Nonnegative multiplier before clamping closure to 0–1; default 1. |
| `public Transform controlAnchor` | Moving control contact used by ClosureChange. |
| `public float ControlClosure { get; }` | Clamped distance-based closure. Returns zero outside ClosureChange, with missing anchors or invalid distance range/multiplier. |
| `public bool followAnchorRotation` | True by default. False keeps the initial resolved orientation relative to the vehicle while following anchor position; affects resolved hand/foot contacts, not raw GetAnchor. |
| `public AnchorHandleMode mode` | Follow by default; ClosureChange measures distance to controlAnchor for additional four-finger flexion. |
| `public float openDistance` | World-space distance in metres giving zero closure; default 0.06. Must exceed closedDistance. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override Transform GetAnchor(PassengerBodyPart part)` | Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part. | `part` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact `Transform`, or `null` under the availability conditions described here. |

## AnchorHandleMode

**Runtime/World/Passengers/IK/Handle/AnchorHandle.cs**

Selects how an anchored contact uses its control transform.

### Values

- `Follow`: normal anchor following.
- `ClosureChange`: adds four-finger flexion from the distance between the palm anchor and moving control anchor; requires Adaptive Grip.

## ControlHandle

**Runtime/World/Passengers/IK/Handle/ControlHandle.cs**

Shared IK contact for an animated control. Inherits AnchorHandle; supplies limb permissions, palm/finger poses and a reference to the controlling animator. It never moves the control model.

**Inherits / implements:** `AnchorHandle`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public ControlAnimator animator` | Visual controller paired with this IK contact. Its InteractionValue is observed for generic contact value events; the handle never writes control geometry. |

## GearLeverHandle

**Runtime/World/Passengers/IK/Handle/GearLeverHandle.cs**

IK-only palm contact on a gear lever. Inherits ControlHandle; default authoring selects the right hand.

**Inherits / implements:** `ControlHandle`.

## GearPaddleHandle

**Runtime/World/Passengers/IK/Handle/GearPaddleHandle.cs**

IK-only palm contact on a moving gear paddle. Inherits ControlHandle; choose allowed limb, occupant and reach/return timing here.

**Inherits / implements:** `ControlHandle`.

## HandleActionSource

**Runtime/World/Passengers/IK/Handle/Core/HandleUseSettings.cs**

Automatic request source: value events, absolute command magnitude or resolved service-brake demand.

Values: `ValueChange`, `Command`, `ServiceBrake`.

## HandleAnimatorBinding

**Runtime/World/Passengers/IK/Handle/Core/HandleAnimatorBinding.cs**

See [custom animation and IK](../HandleAnimation.md) for setup, event timing and worked examples.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Animator animator` | Optional output Animator; application still chooses states/layers. |
| `public string changingParameter` | Optional Bool parameter receiving IsValueChanging. |
| `public string contactParameter` | Optional Bool parameter receiving the last sampled seat/part contact state. Normal LateUpdate reads the previous late contact sample. |
| `public Transform contactTransform` | Optional fingertip/palm frame registered during Apply, after ordinary seat Update tracking. Null keeps automatic humanoid mapping or your explicit registration. |
| `public bool drivePoseWeights` | Write the four channel weights to the resolved handle each Apply; default true. Turn off for an observation-only binding. |
| `public bool driveTargetOverride` | Write targetOverride when true; default false. Null clears the override only while this option is enabled. |
| `public float fingerWeight` | Package grip/finger pose blend against incoming finger rotations. Default 1; 0 leaves fingers to animation. Independent of arm IK. |
| `public VehicleHandle handle` | Optional explicit source handle; if empty use the selected seat limb handle. |
| `public PassengerBodyPart part` | Hand/foot controlled by this binding; default RightHand. |
| `public float physicalWeight` | Native physical palm support weight, default 1. Zero releases the locked palm and clears its support drives; does not disable anatomy, other limb motors or arbitrary transform supports. |
| `public float positionWeight` | Position IK blend against incoming animated upper/lower limb rotations. Default 1; 0 leaves animated limb rotations intact. |
| `public VehicleHandle ResolvedHandle { get; }` | Explicit handle, otherwise the selected seat limb handle, otherwise null. |
| `public float rotationWeight` | Independent wrist/ankle rotation blend. Default 1; 0 preserves its incoming local rotation under the blended parent. |
| `public PassengerSeat seat` | Occupied seat used to resolve the limb handle and identify manual contact reports. |
| `public Transform targetOverride` | Optional final world-space IK target. On HandleAnimatorBinding it is written only when driveTargetOverride is enabled; null restores native target selection. |
| `public string valueParameter` | Optional Float parameter receiving InteractionValue.x; blank, absent or wrong-type parameters are ignored. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void Apply()` | Applies configured weights/target and optional Animator outputs. Runs at execution order 90 before ordinary HumanoidPassenger IK (100). Missing/disabled handles are ignored. | — |
| `public void BeginControlChange()` | Animation Event relay to the resolved handle BeginValueChange. | — |
| `public void ContactEnter()` | Animation Event relay: chooses Manual contact mode and reports touching for the current seat/part. | — |
| `public void ContactExit()` | Animation Event relay: chooses Manual contact mode and reports not touching. | — |
| `public void EndControlChange()` | Animation Event relay to the resolved handle EndValueChange. | — |
| `public void SetControlValue(float value)` | Animation Event relay to SetAnimationValue(float). This reports a signal; use the concrete control API to command a switch/vehicle. | — |
| `public void SetFingerWeight(float value)` | Animation Event convenience method: sets the clamped fingerWeight. | — |
| `public void SetIKWeight(float value)` | Animation Event convenience method: sets both positionWeight and rotationWeight to the clamped value. | — |

## HandleContactContext

**Runtime/World/Passengers/IK/Handle/Core/HandleInteraction.cs**

See [custom animation and IK](../HandleAnimation.md) for setup, event timing and worked examples.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public readonly Transform Contact` | Registered bone, palm frame or application contact transform; may be null for Manual mode. |
| `public readonly float Distance` | World distance in metres, or positive infinity when geometry is unavailable. |
| `public readonly VehicleHandle Handle` | Original source handle. |
| `public readonly bool IsManual` | Whether this snapshot used Manual contact reports. |
| `public readonly bool IsTouching` | Sampled contact state; false on Ended. |
| `public readonly PassengerBodyPart Part` | Tracked hand or foot. |
| `public readonly PassengerBody Passenger` | Original tracked occupant, retained on release notifications. |
| `public readonly PassengerSeat Seat` | Original tracked seat. |
| `public readonly Transform Target` | Resolved final handle target at sample time; may be null. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public HandleContactContext(VehicleHandle handle, PassengerSeat seat, PassengerBody passenger, PassengerBodyPart part, Transform contact, Transform target, float distance, bool touching, bool manual)` | Creates a read-only snapshot from the supplied sample fields; does not perform an interaction. | — |

## HandleContactSource

**Runtime/World/Passengers/IK/Handle/Core/HandleInteraction.cs**

See [custom animation and IK](../HandleAnimation.md) for setup, event timing and worked examples.

### Values

- `Automatic`
- `Manual`

## HandleController

**Runtime/World/Passengers/IK/Handle/Core/HandleController.cs**

Per-vehicle handle registry and exclusive limb scheduler. The vehicle advances it once before passenger TireFeedback. See [runtime handover](../Scripting/Handles.md#runtime-handover) for admission, timing and cleanup.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<HandleUse> Finished` | After completion or cancellation has released ownership and restored any owned binding. Payload is the ended token. |
| `public event Action<HandleUse> Started` | After a token owns its limb. Payload is the new token. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public IReadOnlyList<VehicleHandle> All { get; }` | Read-only registered handle snapshot, excluding transient adapters and nested vehicles. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void CancelHandle(VehicleHandle handle)` | Cancel active uses targeting or returning to the specified handle. | — |
| `public void CancelAll()` | Immediately cancel every active token, blocking reentrant acquisition from cancellation callbacks. | — |
| `public void CancelSeat(PassengerSeat seat)` | Immediately cancel tokens for one seat. Blocks reentrant acquisition during cleanup. | — |
| `public VehicleHandle Current(PassengerSeat seat, PassengerBodyPart limb)` | Returns the requested destination while a token owns the limb; otherwise its configured handle. May be null for direct anchors. | — |
| `public VehicleHandle Get(string id)` | Exact ID lookup; null for missing or duplicate IDs. Disabled registered handles remain discoverable. | — |
| `public HandleUse GetUse(PassengerSeat seat, PassengerBodyPart limb)` | Returns the active ownership token for this seat and limb, otherwise null. | — |
| `public void Refresh()` | Cancel active work and rebuild handle discovery, IDs, subscriptions and priority order. Call after adding/removing handles or editing IDs/priorities. | — |
| `public HandleUse TryAcquire(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target)` | Admit persistent application-driven target ownership; returns null on refusal. Cancel the returned token to restore the home binding. | — |
| `public HandleUse TryAcquire(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, bool forceIK)` | Persistent ownership with an optional temporary IK override. Can force IK on the existing home handle. | `forceIK` borrows IK for this limb until the token ends. |
| `public HandleUse TryReachAndHold(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, bool forceIK)` | Timed reach and hold with an optional temporary IK override. | Return or cancel the token to release ownership. |
| `public HandleUse TryUse(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, bool forceIK, Action onArrival = null)` | Out-and-back reach with an optional temporary IK override. | Invokes the callback on arrival; restores the binding on return. |
| `public HandleUse TryAcquireAnimator(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target)` | Admit persistent ownership with Animator mode. Cancel restores mode only if it is still Animator. | — |
| `public bool TryGet(string id, out VehicleHandle handle)` | Exact case-sensitive ID lookup. Returns false for missing, blank/unregistered or duplicate IDs. | — |
| `public HandleUse TryReachAndHold(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target)` | Reach using outbound timing, then retain ownership until Return or Cancel. Returns null if unavailable. | — |
| `public HandleUse TryUse(PassengerSeat seat, PassengerBodyPart limb, string id, Action onArrival = null)` | Admit an out-and-back reach or return null. Explicit-limb overloads require that limb; the target-only overload uses preferred/fallback settings. Callback runs once on arrival. | — |
| `public HandleUse TryUse(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, Action onArrival = null)` | Admit an out-and-back reach or return null. Explicit-limb overloads require that limb; the target-only overload uses preferred/fallback settings. Callback runs once on arrival. | — |
| `public HandleUse TryUse(PassengerSeat seat, VehicleHandle target, Action onArrival = null)` | Admit an out-and-back reach or return null. Explicit-limb overloads require that limb; the target-only overload uses preferred/fallback settings. Callback runs once on arrival. | — |

## HandleCurlAxis

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

Values: `Default`, `X`, `Y`, `Z`. The hand-level selector applies to the four fingers. The thumb selector defines its Base hinge; Middle/Tip transform this axis through their saved neutral frames. Axis evaluation runs in preview and gameplay; Closure helper values do not. See [Curl axis selection](../HandPositions.md#curl-axis-selection).

## HandleFinger

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

Typed finger selection independent of rig bone names.

Values: `Thumb`, `Index`, `Middle`, `Ring`, `Little`.

## HandleFingerPosition

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

See [Reusable hand positions](../HandPositions.md) for authoring, preview, copy/paste and shared assets.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Vector3 baseRotation` | Additional calibrated base XYZ rotation. |
| `public float closure` | Saved per-finger editor helper value. Auto-apply closure gates pose changes; gameplay ignores this value. |
| `public Vector3 curlAngles` | Signed base/middle/tip flexion degrees, bounded by anatomy. |
| `public HandleCurlAxis curlAxis` | Thumb Base hinge selector; Default is mirrored Base Z. Middle/Tip derive local axes from their neutral rotations relative to Base. Non-thumb fingers use the hand-level axis. |
| `public Vector3 middleRotation` | Additional calibrated middle XYZ rotation. |
| `public float surfaceFit` | Blend from authored curl to adaptive surface fit. |
| `public Vector3 tipRotation` | Additional calibrated tip XYZ rotation. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public HandleFingerPosition Copy()` | Independent copy of this finger configuration. | — |
| `public Vector3 Rotation(HandleFingerSegment segment)` | Typed lookup of the base/middle/tip rotation; rejects invalid enum values. | — |
| `public Vector3 Rotation(int segment)` | Returns base, middle or tip rotation for segment 0, 1 or 2. | — |
| `public void SetRotation(HandleFingerSegment segment, Vector3 rotation)` | Sets a joint rotation in calibrated bone-local XYZ degrees; rejects invalid enum values. | — |

## HandleFingerSegment

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

Typed selection of a finger joint rotation.

Values: `Base`, `Middle`, `Tip`.

## HandleHandPose

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

See [Reusable hand positions](../HandPositions.md) for authoring, preview, copy/paste and shared assets.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float closure` | Saved four-finger editor helper value, excluding the thumb. Auto-apply closure gates pose changes; gameplay ignores this value. |
| `public bool constrainThumbToRim` | Enables wheel pinch contact constraints. |
| `public HandleCurlAxis curlAxis` | Curl axis for the four non-thumb fingers; Default uses their calibrated axes. Explicit axes use saved neutral bone frames. |
| `public HandleFingerPosition index` | Index configuration. |
| `public HandleFingerPosition little` | Little-finger configuration. |
| `public float maximumFingerSpeed` | Maximum finger rotation speed for pose changes within one bound handle, degrees per second. Cross-handle transitions use Finger Blend Duration. |
| `public HandleFingerPosition middle` | Middle-finger configuration. |
| `public Vector3 position` | Palm offset in anchor-local metres. |
| `public HandleFingerPosition ring` | Ring-finger configuration. |
| `public Vector3 rotation` | Additional anchor-local XYZ degrees. |
| `public HandleFingerPosition thumb` | Thumb configuration. |
| `public HandleThumbAim thumbAim` | Surface fit, palm-forward or index-direction aiming. |
| `public float thumbAimLimit` | Maximum calibrated base aim in degrees. |
| `public float thumbBaseCone` | Surface-fitting thumb base cone limit. |
| `public float thumbDepthRatio` | Minimum depth ratio for constrained rim aiming. |
| `public float thumbInwardAngle` | Optional aim correction towards wheel centre. |
| `public float thumbInwardRatio` | Minimum inward ratio for constrained rim aiming. |
| `public float thumbOppositionLimit` | Surface-fitting thumb opposition limit. |
| `public float thumbSpreadLimit` | Surface-fitting thumb spread limit. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public HandleHandPose Copy()` | Deep copy including all five finger configurations. | — |
| `public HandleFingerPosition Finger(HandleFinger finger)` | Typed finger lookup; invalid enum values throw ArgumentOutOfRangeException. | — |
| `public HandleFingerPosition Finger(string digit)` | Returns the configured Thumb, Index, Middle or Ring finger; other names use Little. | — |
| `public void SetFinger(HandleFinger finger, HandleFingerPosition position)` | Replaces the chosen finger configuration; rejects null and invalid enum values. | — |

## HandleHandPosition

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

See [Reusable hand positions](../HandPositions.md) for authoring, preview, copy/paste and shared assets.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool autoApplyClosure` | Local editor-helper policy, default true; a linked preset supplies its own policy. Disabled Closure edits save only the slider value. Ignored by gameplay. |
| `public HandleHandPose left` | Local left-hand settings. |
| `public string name` | Display name in position selectors. |
| `public HandleHandPositionProfile preset` | Shared asset supplying left/right data and the Auto-apply closure policy. |
| `public HandleHandPose right` | Local right-hand settings. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public HandleHandPosition Copy()` | Deep resolved-value copy, including the resolved Auto-apply closure policy, with independent left/right/finger objects and no preset link. | — |
| `public HandleHandPose Hand(bool leftHand)` | Returns the resolved local/shared hand data. | — |
| `public HandleHandPose Hand(HandleHandSide side)` | Resolved hand data, using the optional shared preset. Invalid enum values throw ArgumentOutOfRangeException. | — |
| `public void SetHand(HandleHandSide side, HandleHandPose pose)` | Replaces the resolved side in local data or the linked preset; rejects null. | — |

## HandleHandPositionProfile

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPositionProfile.cs**

See [Reusable hand positions](../HandPositions.md) for authoring, preview, copy/paste and shared assets.

**Inherits / implements:** `ScriptableObject`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool autoApplyClosure` | Shared editor-helper policy, default true. Disabled Closure sliders change only their saved helper values; enabling does not reapply them. |
| `public HandleHandPose left` | Shared left-hand configuration. |
| `public HandleHandPose right` | Shared right-hand configuration. |

## HandleHandSide

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

Typed hand selection for pose access and per-hand overrides.

Values: `Left`, `Right`.

## HandleInput

**Runtime/World/Passengers/IK/Handle/Core/HandleInput.cs**

Defines the allowed handle input choices used by this topic.

### Values

- `Brake`
- `Throttle`
- `Clutch`
- `Steering`
- `Pitch`
- `Roll`
- `Yaw`
- `Lift`
- `Strafe`
- `Handbrake`

## HandleLimbs

**Runtime/World/Passengers/IK/Handle/Core/HandleUseSettings.cs**

Allowed limb flags used by controller admission and seat target resolution.

Values: `None = 0`, `LeftHand = 1`, `RightHand = 2`, `LeftFoot = 4`, `RightFoot = 8`, `Hands = 3`, `Feet = 12`, `All = 15`.

## HandlePoseSettings

**Runtime/World/Passengers/IK/Handle/Core/HandleInteraction.cs**

Shared pose and contact settings. Defaults preserve existing automatic behavior.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float contactAngle` | Maximum world rotation difference in degrees, default 180 (no angular restriction). Uses the registered contact frame and final target. |
| `public float contactDistance` | Automatic contact entry distance in world metres, default 0.03. |
| `public HandleContactSource contactSource` | Automatic geometric distance/angle detection (default), or Manual reports from an Animation Event/application. |
| `public float fingerWeight` | Package grip/finger pose blend against incoming finger rotations. Default 1; 0 leaves fingers to animation. Independent of arm IK. |
| `public float physicalWeight` | Native physical palm support weight, default 1. Zero releases the locked palm and clears its support drives; does not disable anatomy, other limb motors or arbitrary transform supports. |
| `public float positionWeight` | Position IK blend against incoming animated upper/lower limb rotations. Default 1; 0 leaves animated limb rotations intact. |
| `public float releaseDistance` | Automatic release distance in world metres, default 0.05, clamped to at least contactDistance. |
| `public float rotationWeight` | Independent wrist/ankle rotation blend. Default 1; 0 preserves its incoming local rotation under the blended parent. |
| `public Transform targetOverride` | Optional final world-space IK target. On HandleAnimatorBinding it is written only when driveTargetOverride is enabled; null restores native target selection. |

## HandleThumbAim

**Runtime/World/Passengers/IK/Handle/Core/HandleHandPosition.cs**

Thumb direction policy: `SurfaceFit`, `PalmForward`, `IndexDirection`.

## HandleUse

**Runtime/World/Passengers/IK/Handle/Core/HandleUse.cs**

Single ownership token returned by the controller. It is never reused. Arrival commits once; completion follows return. Cancellation restores only bindings still owned by this token.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action Arrived` | After binding the destination and running the arrival callback. Persistent acquisitions do not emit this event. |
| `public event Action Cancelled` | After cancellation has released ownership. An already committed action is not undone. |
| `public event Action Completed` | After the return completes and the home binding is restored. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool ForcesIK { get; }` | Whether this token requested temporary limb IK. |
| `public bool IsActive { get; }` | See the runtime handover contract and action settings described above. |
| `public PassengerBodyPart Limb { get; internal set; }` | See the runtime handover contract and action settings described above. |
| `public HandleUsePhase Phase { get; internal set; }` | See the runtime handover contract and action settings described above. |
| `public PassengerSeat Seat { get; internal set; }` | See the runtime handover contract and action settings described above. |
| `public VehicleHandle Target { get; internal set; }` | See the runtime handover contract and action settings described above. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public bool BeginAnimation()` | Give a held destination to Animator ownership after IK arrival. Returns false unless the active token still owns its original occupant/binding in Holding. Prepares physical humanoid limb animation. Return subsequently restores IK and performs the timed home trip. | No arguments; true on handover. |
| `public bool BeginAnimation(bool keepHandOnTarget)` | Begin a held gesture with whole-limb ownership when false, or retain hand IK/physical support and animate fingers only when true. The latter requires a humanoid hand. Returns false if the token, occupant or binding is no longer eligible. Return/cancellation restores finger ownership. | `keepHandOnTarget`: choose finger-only animation on the held target. |
| `public void Cancel()` | Idempotent immediate cancellation. Never restores a newer foreign binding. | — |
| `public void Return()` | Release persistent/automatic holding and request a timed return. For an outbound trip, return follows arrival. | — |

## HandleUsePhase

**Runtime/World/Passengers/IK/Handle/Core/HandleUseSettings.cs**

Observable request phase. Completed and Cancelled are terminal states.

Values: `Releasing`, `Outbound`, `Holding`, `ReturnReleasing`, `Returning`, `Completed`, `Cancelled`.

## HandleUseSettings

**Runtime/World/Passengers/IK/Handle/Core/HandleUseSettings.cs**

Destination action and travel policy. Explicit requests use the timing fields even when useOnAction is false.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool allowOtherLimbs` | See the runtime handover contract and action settings described above. |
| `public bool allowUnsupportedDeparture` | False by default. Allows this request to bypass the source handle's minimum-attachment rule. Other limbs are not cancelled. |
| `public HandleInput input` | See the runtime handover contract and action settings described above. |
| `public bool interruptLowerPriority` | False by default. Allows a strictly higher-priority timed request to interrupt another timed request on the same seat limb, preserving its original home destination. Persistent and Animator ownership remain protected. |
| `public float liftHeight` | See the runtime handover contract and action settings described above. |
| `public PassengerBodyPart preferredLimb` | See the runtime handover contract and action settings described above. |
| `public int priority` | Higher automatic requests are attempted first; interruption also requires interruptLowerPriority. |
| `public float releaseDuration` | See the runtime handover contract and action settings described above. |
| `public float releaseThreshold` | See the runtime handover contract and action settings described above. |
| `public float returnDelay` | See the runtime handover contract and action settings described above. |
| `public float returnDuration` | Return travel duration in seconds, independent of outbound travel. |
| `public PassengerSeat seat` | See the runtime handover contract and action settings described above. |
| `public HandleActionSource source` | See the runtime handover contract and action settings described above. |
| `public float threshold` | See the runtime handover contract and action settings described above. |
| `public float travelDuration` | Outbound travel duration in seconds (Inspector: Outbound Duration). |
| `public bool useOnAction` | See the runtime handover contract and action settings described above. |

## HandleValueContext

**Runtime/World/Passengers/IK/Handle/Core/HandleInteraction.cs**

See [custom animation and IK](../HandleAnimation.md) for setup, event timing and worked examples.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public readonly float DeltaTime` | Sample interval in seconds; explicit Begin/End report zero. |
| `public readonly VehicleHandle Handle` | Original source handle. |
| `public readonly bool IsChanging` | True for start/progress, false for stop. |
| `public readonly Vector3 PreviousValue` | Previous observed vector (explicit Begin/End use the current sampled value). |
| `public readonly Vector3 Value` | Current sampled vector in source-specific units. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public HandleValueContext(VehicleHandle handle, Vector3 value, Vector3 previousValue, float deltaTime, bool changing)` | Creates a read-only snapshot from the supplied sample fields; does not perform an interaction. | — |

## IHandle

**Runtime/World/Passengers/IK/Handle/VehicleHandle.cs**

Common contact, preparation, binding and input contract.

| Control API | Meaning |
| --- | --- |
| `HandleControlMode ControlMode { get; set; }` / `SetControlMode(HandleControlMode mode)` | Select ownership for this handle; cancels its active requests on a change. |
| `bool UsesIK`, `bool UsesAnimator` | Whether the selected mode enables each built-in path. |
| `HandleAnimatorController animatorController` | Handle-owned Animator configuration and gesture events. |
| `bool IsAnimationBusy` | Whether this handle's gesture still owns an active request, including its return. |
| `bool TryBeginInteraction()` / `void BeginInteraction()` | Start the configured gesture; the bool method reports admission failure. Custom mode leaves startup to your code. |
| `void CancelInteraction()` | Cancel the handle-owned gesture. |
| `void ReceiveAnimationEvent(string signal)` | Direct named-signal entry point, also called by the relay. |
| `void ApplyAnimatorController()` | Apply live mode/Animator settings; normally called by the handle's Update. |
| `event Action<HandleControlMode> ControlModeChanged` | Notification after the handle mode changes. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames. | `part` — Selected body-part enum or part configuration, as declared. `ik` — Mapped humanoid limb/frame helper for this character. `animator` — Character Animator providing mapped bones/animation context. |
| `Transform GetAnchor(PassengerBodyPart part)` | Returns the stable contact transform for a supported body part, or `null` when unavailable/unsupported. | `part` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact `Transform`, or `null` under the availability conditions described here. |
| `float HandContact(bool left)` | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Normalized fraction in 0–1. |
| `bool HandDriven(bool left)` | Reports whether the selected hand should receive physical target guidance. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `bool HandSteering(bool left)` | Reports whether the selected hand participates in steering support. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `void Prepare()` | Prepares reusable contact geometry or handle initialization without entering a seat. | No arguments; no returned value. |
| `void SetInput(Command command, float deltaTime)` | IK-only input hook for application-owned contact targets, such as an aiming hand. Instrument motion belongs to a separate animator. | — |

## JoystickHandle

**Runtime/World/Passengers/IK/Handle/JoystickHandle.cs**

Joystick grip and steering-contact geometry. Inherits SteeringWheelHandle; pitch/roll model motion belongs to SteeringStickAnimator.

**Inherits / implements:** `SteeringWheelHandle`.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public JoystickHandle()` | Declared defaults for this handle; explicit prefab settings take precedence. | — |

## MotorcycleHandle

**Runtime/World/Passengers/IK/Handle/MotorcycleHandle.cs**

Supplies fixed left/right contacts with prepared finger poses.

**Inherits / implements:** [VehicleHandle](Handles.md#vehiclehandle).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override float GripDiameter { get; }` | Resolved cylindrical grip diameter in metres, full width rather than radius. |
| `public float gripLength` | Grip length in metres in the owning system's space. Initial value: `.11f`. |
| `public float gripRadius` | Tube radius in local metres. Grip centres stay fixed; the editor updates the palm contacts and prepares the fingers. |
| `public virtual bool IsPrepared { get; }` | Whether fixed motorcycle hand/finger preparation is available. |
| `public Transform leftGrip` | Centre of the left grip. Local X runs along the tube; local Y points from the palm towards the tube centre. |
| `public Transform rightGrip` | Assign the right grip reference used by MotorcycleHandle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames. | `part` — Selected body-part enum or part configuration, as declared. `ik` — Mapped humanoid limb/frame helper for this character. `animator` — Character Animator providing mapped bones/animation context. |
| `public override Transform GetAnchor(PassengerBodyPart part)` | Returns the prepared left/right grip target for the requested hand. | `part` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact `Transform`, or `null` under the availability conditions described here. |

## PedalFootMode

**Runtime/World/Passengers/IK/Handle/PedalHandle.cs**

Values: `Press`, `Rotation`. Press follows the moving contact; Rotation keeps an ankle pivot while pitching the foot.

- `Press`
- `Rotation`

## PedalHandle

**Runtime/World/Passengers/IK/Handle/PedalHandle.cs**

IK-only pedal contact. Press follows the moving contact; Rotation keeps the ankle fixed and aims the foot towards the pedal. Input and travel settings belong to PedalAnimator.

**Inherits / implements:** `ControlHandle`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform ankleAnchor` | Fixed ankle position and reference frame for Rotation. Local Z points towards the toes, X is the pitch axis. |
| `public PedalFootMode footMode` | Press (default) follows the pedal contact; Rotation pivots the foot at a fixed ankle. |
| `public override bool RequiresFootRotation { get; }` | True in Rotation mode; enables the existing IK and physical ankle rotation drives. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override Transform GetAnchor(PassengerBodyPart part)` | Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part. | — |
| `public PedalHandle()` | Declared defaults for this handle; explicit prefab settings take precedence. | — |
| `public override void Prepare()` | Initializes the contact or synchronizes its initial state without requesting a limb. | — |
| `public virtual bool TryGetFootPose(out Vector3 position, out Quaternion rotation)` | Resolves fixed ankle position and foot pitch from Ankle Anchor and Contact Anchor without creating a target. | — |

## RotaryHandle

**Runtime/World/Passengers/IK/Handle/RotaryHandle.cs**

IK palm contact for a rotary knob or hand lever. Inherits ControlHandle. Set its anchor on the moving grip; configure value and motion on the animator.

**Inherits / implements:** `ControlHandle`.

## SteeringWheelHandle

**Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs**

Describes steering contacts, surface geometry and hand participation.

**Inherits / implements:** [VehicleHandle](Handles.md#vehiclehandle).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool allowHandRegrip` | Allow automatic hand repositioning and column support while steering. Disable for fixed handlebar grips. |
| `public bool authoredTargets` | Keep manually authored palm anchors instead of regenerating wheel-rim contacts. Use for control sticks. |
| `public Vector3 center` | Steering-wheel rim centre in the handle's local space. |
| `public RimSample[] customRim` | Optional closed centerline for flat-bottomed or irregular wheels. At least three samples. |
| `public virtual int GeometrySignature { get; }` | Hash of geometry inputs used to detect a changed steering surface. |
| `public SteeringGripMode gripMode` | Selects the grip mode policy for this configuration. Options: `BothHands`, `LeftHand`, `RightHand`, `Released`. Initial value: `SteeringGripMode.BothHands`. |
| `public virtual bool HasCustomRim { get; }` | True when at least three custom rim centerline samples are configured. |
| `public float leftAngle` | Left angle in degrees, relative to the owning mechanism's reference frame. Initial value: `180`. |
| `public Transform leftTarget` | Assign the left target reference used by SteeringWheelHandle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public int pinchHandPosition` | Index of the thumb/index pinch configuration. |
| `public int pressureHandPosition` | Index of the palm-pressure configuration. |
| `public SteeringHandRegripSettings regrip` | Configuration for regrip. Expand this field; its settings are described under SteeringHandRegripSettings. Initial value: `new SteeringHandRegripSettings()`. |
| `public bool reverseApproach` | The wheel-local direction away from the driver is +Z. Reverse for a backwards pivot. |
| `public float rightAngle` | Right angle in degrees, relative to the owning mechanism's reference frame. |
| `public Transform rightTarget` | Assign the right target reference used by SteeringWheelHandle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float rimRadius` | Rim radius in metres in the owning system's space. Initial value: `.1744f`. |
| `public bool showFingerContacts` | When checked, show finger contacts is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public bool stickGrip` | Fit fingers and thumb around Grip Diameter at the authored palm anchors. |
| `public float tubeDepthRadius` | Fore/aft tube radius. Zero uses a circular section equal to Tube Radius. |
| `public float tubeRadius` | Radius of the rim tube, not its diameter. |
| `public bool useAnchorStartPosition` | Start from the assigned palm anchors and retain their position and rotation offsets while allowing regrip. Takes precedence over `authoredTargets` and skips automatic reach adjustment. |
| `public bool varyGripWithSteering` | Select or blend the saved pressure/pinch poses while steering; no runtime closure factor is applied. |
| `public virtual float WorldScale { get; }` | Absolute steering-control world X scale used by the uniform-scale geometry model. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool AllowsHand(bool left)` | Checks enabled state and the configured left/right grip-mode permission. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames. | `part` — Selected body-part enum or part configuration, as declared. `ik` — Mapped humanoid limb/frame helper for this character. `animator` — Character Animator providing mapped bones/animation context. |
| `public virtual Vector3 Centerline(float angle)` | Evaluates the steering-rim centerline at an angular coordinate in the wheel's local frame. | `angle` — Angular coordinate in degrees for this geometry operation. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation. |
| `public override Transform GetAnchor(PassengerBodyPart part)` | Returns `leftTarget`/`rightTarget` only for an allowed corresponding hand; unsupported limbs or disallowed hands return `null`. | `part` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact `Transform`, or `null` under the availability conditions described here. |
| `public virtual void GetContactFrame(float angle, out Vector3 point, out Quaternion rotation)` | Returns a world-space contact point/orientation at an angular coordinate around the steering rim. | `angle` — Angular coordinate in degrees for this geometry operation. `point` — Geometry point in the declared coordinate frame. `rotation` — Requested/output orientation in the declared frame. |
| `public virtual void GetPalmContactFrame(float angle, float pressure, out Vector3 point, out Quaternion rotation)` | Returns a world palm-contact frame including the requested pressure adjustment. | `angle` — Angular coordinate in degrees for this geometry operation. `pressure` — Normalized palm pressure. `point` — Geometry point in the declared coordinate frame. `rotation` — Requested/output orientation in the declared frame. |
| `public override float HandContact(bool left)` | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Normalized fraction in 0–1. |
| `public override bool HandDriven(bool left)` | Reports whether the selected hand should receive physical target guidance. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual bool HandPinch(bool left)` | Reports whether the selected hand uses the pinch gesture. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public override bool HandSteering(bool left)` | Reports whether the selected hand participates in steering support. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual float PalmPressure(bool left)` | Returns normalized palm-pressure presentation for the selected hand. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Normalized fraction in 0–1. |
| `public override void Prepare()` | Prepares reusable contact geometry or handle initialization without entering a seat. | No arguments; no returned value. |
| `public virtual float RadiusAt(float angle)` | Returns the steering-rim tube radius at the supplied angular coordinate. | `angle` — Angular coordinate in degrees for this geometry operation. **Returns:** Surface distance/radius in the unit and frame described by this operation. |
| `public override void ResolveHandPositions(bool left, out HandleHandPose primary, out HandleHandPose secondary, out float blend)` | Selects the configured grip/pinch and blends the pressure configuration using current steering contact demand. | — |
| `public virtual void SetGripMode(SteeringGripMode mode)` | Chooses both hands, left only, right only or released steering-grip permission. | `mode` — Mode, interpreted by this operation in the declared type. |
| `public virtual void SetHandContact(bool left, float contact)` | Sets normalized physical contact participation for one hand; finger pose is independent of contact. | `left` selects the hand; `contact` is clamped to 0–1. |
| `public virtual void SetHandControl(bool left, bool driven, bool steering)` | Selects physical-guidance and steering-support participation independently for one hand. | `left` — `true` selects the left hand; `false` selects the right. `driven` — Whether physical hand guidance is enabled. `steering` — Normalized steering input, or bool steering participation when declared bool. |
| `public virtual void SetHandPinch(bool left, bool value)` | Enables/disables the selected hand's pinch gesture. | `left` — `true` selects the left hand; `false` selects the right. `value` — Requested bool state for this operation. |
| `public virtual void SetHandPinch(bool left, float amount)` | Sets a clamped 0–1 Pinch-to-Wrapped blend. Zero uses normal grip/pressure selection; one uses the saved Pinch pose. | `left` selects the hand; `amount` is the pinch weight. |
| `public virtual void SetPalmPressure(bool left, float value)` | Sets the blend towards the authored pressure hand position; the calibrated palm contact stays unchanged. | `left` — `true` selects the left hand; `false` selects the right. `value` — Normalized value clamped to 0–1 by this control. |
| `public virtual float SignedDistance(Vector3 worldPoint)` | Returns signed world-space distance to the steering tube surface; positive means outside. | `worldPoint` — World-space target/sample point. **Returns:** Surface distance/radius in the unit and frame described by this operation. |
| `public virtual float SignedDistanceLocal(Vector3 point)` | Evaluates a wheel-local point against the steering tube and returns scaled surface distance. | `point` — Geometry point in the declared coordinate frame. **Returns:** Surface distance/radius in the unit and frame described by this operation. |
| `public SteeringWheelHandle()` | Declared defaults for this handle; explicit prefab settings take precedence. | — |
| `public override bool Supports(PassengerBodyPart part)` | Whether Allowed limbs and any specialized geometry policy permit this limb. | — |
| `public virtual void UpdateTargets()` | Updates steering palm targets from current geometry without changing seat occupancy. | No arguments; no returned value. |

## SteeringWheelHandle.RimSample

**Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs**

Value data for rim sample; its fields are listed below.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Vector3 position` | World-space position used by the current contact or motion sample. |
| `public float radius` | Physical radius in metres; use half the outside diameter of the represented shape. |

## SteeringWheelHandle.SteeringGripMode

**Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs**

Defines the allowed steering grip mode choices used by this topic.

### Values

- `BothHands`
- `LeftHand`
- `RightHand`
- `Released`

## SwitchHandle

**Runtime/World/Passengers/IK/Handle/SwitchHandle.cs**

IK-only hand contact for a switch. Inherits ControlHandle. Detents, events and motion belong to SwitchAnimator.

**Inherits / implements:** `ControlHandle`.

## ThrottleHandle

**Runtime/World/Passengers/IK/Handle/ThrottleHandle.cs**

IK-only contact for a throttle grip. Inherits ControlHandle; all geometry and value writes belong to ThrottleAnimator.

**Inherits / implements:** `ControlHandle`.

## HandleControlMode

`IK`, `AnimatorIK` (Inspector: Animator + IK), `Animator`, `Custom`. This selects the handle's limb/animation ownership independently of the passenger controller. See [configuration tutorial](../HandleAnimation.md#tutorial-handle-owned-animator).

## HandleAnimatorController

Configure through **[Handle] > Animator controller**. The seat supplies the current passenger and active seated Animator unless an explicit Animator is assigned. `controller`, `valueMask`, `mask` and `contactMask` are Edit Mode authoring inputs for the mask Apply button. Runtime layer ownership uses names and valid indices; changing controller or disabling the owner restores a previously owned weight when it has not been changed externally.

| Member | Meaning |
| --- | --- |
| `seat`, `limb`, `animator` | Occupant, selected hand/foot and optional explicit character Animator. |
| `steeringSource`, `valueSource` | Optional normalized wheel angle or `IInteriorValueSource`; otherwise reads Interaction Value X. |
| `valueParameter`, `valueMultiplier`, `valueOffset` | Animator float output and linear remapping. |
| `changingParameter`, `contactParameter` | Optional Animator bool outputs. |
| `valueLayer`, `valueLayerWeight`, `valueMask` | Continuous overlay settings. |
| `trigger`, `layer`, `mask`, `layerWeight` | Full gesture trigger and overlay. |
| `contactTrigger`, `contactLayer`, `contactMask` | Contact/finger clip after an IK reach. |
| `animateInIKMode` | Enables an authored contact/gesture clip for an IK handle. |
| `enterBlend`, `returnBlend` | Gesture overlay blend durations in seconds. |
| `animationEvents`, `commitTime`, `duration`, `timeout` | Clip-event or elapsed-time completion, and cancellation timeout. |
| `startedEvent`, `inMoveEvent`, `reachedEvent`, `completedEvent`, `cancelledEvent` | Exact string arguments accepted from the clip relay. |
| `Started`, `InMove`, `Reached`, `Completed`, `Cancelled` | C# `Action` events for the current gesture. Started fires once on admission; Reached commits once; Completed follows successful return. |
| `onStarted`, `onInMove`, `onReached`, `onCompleted`, `onCancelled` | Matching Inspector UnityEvents; C# event fires before its Inspector counterpart. |

## HandleAnimationEvents

Place on the character Animator's GameObject. `HandleAnimationEvent(string signal)` routes a configured name to active handle gestures. The optional `handles` array declares fixed receivers. Active requests register automatically, so no per-request Inspector rewiring is required. Physical passengers forward events from their seated animation source. Receivers ignore signals while no gesture is active; use distinct event names for gestures that can run concurrently.

## VehicleHandle

**Runtime/World/Passengers/IK/Handle/VehicleHandle.cs**

Common contact, preparation, binding and input contract.

| Control API | Meaning |
| --- | --- |
| `HandleControlMode ControlMode { get; set; }` / `SetControlMode(HandleControlMode mode)` | Select ownership for this handle; cancels its active requests on a change. |
| `bool UsesIK`, `bool UsesAnimator` | Whether the selected mode enables each built-in path. |
| `HandleAnimatorController animatorController` | Handle-owned Animator configuration and gesture events. |
| `bool IsAnimationBusy` | Whether this handle's gesture still owns an active request, including its return. |
| `bool TryBeginInteraction()` / `void BeginInteraction()` | Start the configured gesture; the bool method reports admission failure. Custom mode leaves startup to your code. |
| `void CancelInteraction()` | Cancel the handle-owned gesture. |
| `void ReceiveAnimationEvent(string signal)` | Direct named-signal entry point, also called by the relay. |
| `void ApplyAnimatorController()` | Apply live mode/Animator settings; normally called by the handle's Update. |
| `event Action<HandleControlMode> ControlModeChanged` | Notification after the handle mode changes. |


**Inherits / implements:** `MonoBehaviour`, `IHandle`.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<HandleContactContext> ContactEnded` | Once when contact is lost or released (including exit/disable/rebinding). Payload retains the original occupant identity. |
| `public event Action<HandleContactContext> ContactStarted` | Once on a not-touching to touching transition; C# event runs before the matching UnityEvent. |
| `public event Action<HandleContactContext> ContactUpdated` | Once per contact sample while touching, including its start sample. Payload identifies handle, seat, occupant, part and target. |
| `public UnityEvent<HandleContactContext> onContactEnded` | Inspector-configurable counterpart of ContactEnded. Runs after the C# event for the same phase. |
| `public UnityEvent<HandleContactContext> onContactStarted` | Inspector-configurable counterpart of ContactStarted. Runs after the C# event for the same phase. |
| `public UnityEvent<HandleContactContext> onContactUpdated` | Inspector-configurable counterpart of ContactUpdated. Runs after the C# event for the same phase. |
| `public UnityEvent<HandleValueContext> onValueChangeStarted` | Inspector-configurable counterpart of ValueChangeStarted. Runs after the C# event for the same phase. |
| `public UnityEvent<HandleValueContext> onValueChangeStopped` | Inspector-configurable counterpart of ValueChangeStopped. Runs after the C# event for the same phase. |
| `public UnityEvent<HandleValueContext> onValueChanging` | Inspector-configurable counterpart of ValueChanging. Runs after the C# event for the same phase. |
| `public event Action<HandleValueContext> ValueChangeStarted` | Once when a significant value change or explicit BeginValueChange starts activity. |
| `public event Action<HandleValueContext> ValueChangeStopped` | Once when the value settles for valueStopDelay, explicit EndValueChange runs or the handle is disabled/destroyed. |
| `public event Action<HandleValueContext> ValueChanging` | Each active changed/manual sample; does not imply contact or commit a gameplay action. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool adaptiveGrip` | Fit fingers around this handle. Applies to hands only; foot anchors are unaffected. |
| `public HandleLimbs allowedLimbs` | Flags selecting the hands/feet allowed to use this handle. |
| `public float angularDamper` | Damping for angular damper. Higher values oppose relative motion more strongly. Initial value: `20`. |
| `public float angularSpring` | Restoring stiffness for angular spring. Higher values resist displacement more strongly. Initial value: `500`. |
| `public Vector3 animationValue` | Vector signal writable by animation/Timeline/application code. Its meaning and units belong to the application. |
| `public int defaultHandPosition` | Index of the normal grip configuration. |
| `public float fingerBlendDuration` | Seconds to blend displayed finger rotations from the previous handle to this handle after rebind. Default 0.12; zero opts out. Controller travel retains the current pose. Initial seating and editor previews apply immediately. |
| `public float gripDiameter` | Grip diameter in metres in the palm anchor's local space. The cylinder runs along anchor X, with its centre towards +Y from the palm contact. |
| `public virtual float GripDiameter { get; }` | Resolved cylindrical grip diameter in metres, full width rather than radius. |
| `public int HandPositionCount { get; }` | Number of positions, initializing handle-type defaults when the list is empty. |
| `public HandleHandPosition[] handPositions` | Named local/shared configurations. Empty older data is initialized from type-specific defaults. |
| `public string id` | Unique, case-sensitive ID used by EngineAudio's runtime API. |
| `public virtual int InputOrder { get; }` | Input-consumption priority among handles; higher values consume after dependencies. |
| `public Vector3 InteractionValue { get; }` | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics. |
| `public bool IsValueChanging { get; }` | Whether generic value activity is currently running. |
| `public HandlePoseSettings leftFootPose` | Independent left-foot pose, target and contact settings. Finger weight is unused for feet. |
| `public HandlePoseSettings leftHandPose` | Independent left-hand pose, target and contact settings. Weights default to one. |
| `public float maximumPalmForce` | Force/torque budget for maximum palm force; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `90`. |
| `public float maximumTorque` | Force/torque budget for maximum torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `25`. |
| `public int minimumAttachments` | Minimum other held limbs left on this source before borrowing one, evaluated separately for each seat. |
| `public bool observeRotation` | Observe local Euler degrees (true, default) or local position units (false). Euler values wrap at 360 degrees. |
| `public float positionDamper` | Damping for position damper. Higher values oppose relative motion more strongly. Initial value: `60`. |
| `public float positionSpring` | Restoring stiffness for position spring. Higher values resist displacement more strongly. Initial value: `2000`. |
| `public virtual bool RequiresFootRotation { get; }` | Defaults to false. Rotating pedals return true; selector and pedal transfer handles forward their selected handle's requirement. |
| `public HandlePoseSettings rightFootPose` | Independent right-foot pose, target and contact settings. Finger weight is unused for feet. |
| `public HandlePoseSettings rightHandPose` | Independent right-hand pose, target and contact settings. Weights default to one. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public HandleUseSettings use` | Automatic action policy and explicit/automatic transfer timing for this destination. |
| `public bool useAnimationValue` | Observe animationValue instead of the built-in/transform value source; default false. |
| `public float valueChangeThreshold` | Euclidean change threshold in source-value units, default 0.0001. Small changes accumulate against the last significant sample. |
| `public float valueStopDelay` | Seconds without significant change before automatic Stop; default 0.08. Explicit manual activity ends through EndValueChange. |
| `public Transform valueTransform` | Optional externally animated transform to observe when useAnimationValue is false; otherwise use the concrete handle source. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void BeginValueChange()` | Starts explicit value activity, emitting Started only when idle. Constant-value samples still emit progress until EndValueChange. | — |
| `public virtual void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames. | — |
| `public void ClearHandPositionOverride(HandleHandSide side)` | Restores normal selection and wheel pressure/pinch blending for that hand. | — |
| `public void EndValueChange()` | Ends manual/automatic activity and emits Stopped once if active. Safe when idle. | — |
| `public void EnsureHandPositions()` | Initializes missing configurations with the defaults for the handle type; existing local or shared poses remain unchanged. | — |
| `public abstract Transform GetAnchor(PassengerBodyPart part)` | Returns the stable contact transform for a supported body part, or `null` when unavailable/unsupported. | — |
| `public HandleFingerPosition GetFingerPosition(int positionIndex, HandleHandSide side, HandleFinger finger)` | Typed access to one finger of one configured hand. | — |
| `public virtual Transform GetHandAnchor(PassengerBodyPart part)` | Returns the configured palm target with pose offsets. Feet keep the raw anchor; source geometry remains on GetAnchor. | — |
| `public HandleHandPose GetHandPose(int positionIndex, HandleHandSide side)` | Resolved local/shared hand data; edits to shared data affect all handles linked to that asset. | — |
| `public HandleHandPosition GetHandPosition(int index)` | Strict indexed lookup; invalid indices throw ArgumentOutOfRangeException. HandPosition(int) remains the clamped lookup. | — |
| `public HandleHandPosition GetHandPosition(string name)` | Named lookup; a missing name throws KeyNotFoundException. | — |
| `public int GetHandPositionOverride(HandleHandSide side)` | Returns the explicit position index, or -1 for automatic selection. | — |
| `public HandlePoseSettings GetPoseSettings(PassengerBodyPart part)` | Returns the live settings for this body part; lazily restores a null settings object. Invalid enum throws ArgumentOutOfRangeException. | — |
| `public virtual float HandContact(bool left)` | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released. | — |
| `public virtual bool HandDriven(bool left)` | Reports whether the selected hand should receive physical target guidance. | — |
| `public HandleHandPosition HandPosition(int index)` | Returns a position, clamping the index to the available list. | — |
| `public virtual bool HandSteering(bool left)` | Reports whether the selected hand participates in steering support. | — |
| `public HandleHandPosition MakeHandPositionLocal(int index)` | Replaces the entry with a deep local copy of its resolved values, detaching any shared asset. | — |
| `public virtual void Prepare()` | Initializes the contact or synchronizes its initial state without requesting a limb. | — |
| `public void ReleaseContact(PassengerSeat seat, PassengerBodyPart part)` | Releases one tracked pair and emits Ended once if touching. Safe when untracked. | — |
| `public bool ReportContact(PassengerSeat seat, PassengerBodyPart part, bool touching)` | Records touching/not-touching for the current occupant. Select Manual contactSource to use the report; events are emitted when SampleContact runs. No geometric contact required in Manual mode. | — |
| `public virtual void ResetHandle()` | Resets local handle state through the common extensible handle contract. | — |
| `public virtual void ResolveHandPositions(bool left, out HandleHandPose primary, out HandleHandPose secondary, out float blend)` | Resolves local or shared left/right configurations and their blend. Base handles use their normal grip; wheels select pinch or blend pressure. | — |
| `public void ResolveHandPositions(HandleHandSide side, out HandleHandPose primary, out HandleHandPose secondary, out float blend)` | Typed access to the current configuration sources and blend; dispatches to the handle-specific resolver. | — |
| `public void SampleContact(PassengerSeat seat, PassengerBodyPart part)` | Samples one tracked seat/part and emits contact transitions plus progress while touching. Seats call this after ordinary posing and rigid supports; custom pipelines can call it explicitly. | — |
| `public void SampleInteraction(float deltaTime)` | Samples the current source and advances generic activity using finite nonnegative seconds. The first sample establishes a silent baseline. Built-in handles call it in LateUpdate. | — |
| `public void SetAnimationValue(float value)` | Selects the explicit animation signal and stores a finite scalar X/vector. Invalid values are ignored. Sampling emits events; no mechanical action is performed. | — |
| `public void SetAnimationValue(Vector3 value)` | Selects the explicit animation signal and stores a finite scalar X/vector. Invalid values are ignored. Sampling emits events; no mechanical action is performed. | — |
| `public void SetDefaultHandPosition(int index)` | Sets the normal grip index with strict index validation. | — |
| `public void SetFingerPosition(int positionIndex, HandleHandSide side, HandleFinger finger, HandleFingerPosition position)` | Replaces one finger in the resolved hand; rejects null. | — |
| `public void SetHandPose(int positionIndex, HandleHandSide side, HandleHandPose pose)` | Replaces resolved hand data, including the shared asset when linked; rejects null. | — |
| `public void SetHandPositionOverride(HandleHandSide side, int index)` | Temporarily forces that hand to use one configured pose with no automatic gesture blend. Does not replace contact geometry, steering ownership or physics. Not serialized. | — |
| `public virtual void SetInput(Command command, float deltaTime)` | IK-only input hook for application-owned contact targets, such as an aiming hand. Instrument motion belongs to a separate animator. | — |
| `public void SetPoseTarget(PassengerBodyPart part, Transform target)` | Sets a final world-space target override for this part. Null returns to the handle contact target. | — |
| `public void SetPoseWeights(PassengerBodyPart part, float position, float rotation, float fingers)` | Sets position, rotation and finger weights independently. Values clamp to 0–1; non-finite values become zero. No re-entry/rebind required. | — |
| `public virtual bool Supports(PassengerBodyPart part)` | Whether Allowed limbs and any specialized geometry policy permit this limb. | — |
| `public bool TrackContact(PassengerSeat seat, PassengerBodyPart part, Transform contact)` | Registers a contact transform for the current occupant and limb. Returns false for inactive/transitioning/empty seats or a limb bound to another handle. Built-in humanoids register their mapped bones/palm contacts automatically. | — |
| `public bool TryGetContactState(PassengerSeat seat, PassengerBodyPart part, out HandleContactContext state)` | Returns the last sampled snapshot for the current occupant, or false/default when unavailable; false-contact snapshots remain valid while tracked. | — |
| `public bool TryGetHandPosition(string name, out HandleHandPosition position)` | Finds the first exact, case-sensitive position name. Returns false and null for missing/empty names. | — |

## YokeHandle

**Runtime/World/Passengers/IK/Handle/YokeHandle.cs**

Describes steering contacts, surface geometry and hand participation.

**Inherits / implements:** [SteeringWheelHandle](Handles.md#steeringwheelhandle).
