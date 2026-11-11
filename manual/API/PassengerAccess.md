# Animated access API

Read [the system explanation](../Scripting/PassengerAccess.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [AccessAnimationEvents](PassengerAccess.md#accessanimationevents)
- [AccessAnimationProfile](PassengerAccess.md#accessanimationprofile)
- [AccessMotion](PassengerAccess.md#accessmotion)
- [AccessSide](PassengerAccess.md#accessside)
- [AccessState](PassengerAccess.md#accessstate)
- [HumanoidAccessMotion](PassengerAccess.md#humanoidaccessmotion)
- [PassengerAccess](PassengerAccess.md#passengeraccess)
- [PassengerAccessProgress](PassengerAccess.md#passengeraccessprogress)
- [SeatAccess](PassengerAccess.md#seataccess)

## AccessAnimationEvents

**Runtime/World/Passengers/Access/AccessAnimationEvents.cs**

Relays animation access markers into the sequence.

**Inherits / implements:** `MonoBehaviour`.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void AccessCloseDoor()` | Delivers an animation marker requesting closure of the current access door. | No arguments; no returned value. |
| `public virtual void AccessOpenDoor()` | Delivers an animation marker requesting opening of the current access door. | No arguments; no returned value. |
| `public virtual void AccessWaitForOpenDoor()` | Optional clip marker holding access playback until the door reaches its open tolerance. A bounded Door Timeout cancels blocked doors; calibration sampling cannot operate this marker. | No arguments; no returned value. |

## AccessAnimationProfile

**Runtime/World/Passengers/Access/AccessAnimationProfile.cs**

Stores animation states, references and timing configuration.

**Inherits / implements:** `ScriptableObject`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float completionTimeout` | Additional time allowed before an unfinished access operation is cancelled, in seconds. |
| `public RuntimeAnimatorController controller` | Assign the controller reference used by AccessAnimationProfile. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public AnimationClip enterClip` | Assign the enter clip reference used by AccessAnimationProfile. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public AnimationCurve enterLeftFootContact` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. |
| `public AnimationCurve enterPlacement` | Weight of the outside alignment during entry; fades before the character sits. |
| `public Vector2 enterRange` | Lower/upper components defining the enter range range in the owning mechanism's units. Initial value: `new Vector2(0, 1)`. |
| `public AnimationCurve enterRightFootContact` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. |
| `public string enterState` | Text identifier/name for enter state. Keep it consistent with the referenced animation, profile or application setting. Initial value: `"Base Layer.Enter In"`. |
| `public string enterTrigger` | Text identifier/name for enter trigger. Keep it consistent with the referenced animation, profile or application setting. Initial value: `"EnterIn"`. |
| `public float exitBlendSeconds` | Seconds blending the live seated pose into the exit animation. Default 0.2; zero disables it. |
| `public AnimationClip exitClip` | Assign the exit clip reference used by AccessAnimationProfile. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public AnimationCurve exitLeftFootContact` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. |
| `public AnimationCurve exitPlacement` | Curve mapping the owning system's input to exit placement. Edit its keys to change the response shape. Initial value: `AnimationCurve.EaseInOut(.2f, 0, .85f, 1)`. |
| `public Vector2 exitRange` | Lower/upper components defining the exit range range in the owning mechanism's units. Initial value: `new Vector2(0, 1)`. |
| `public AnimationCurve exitRightFootContact` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. |
| `public string exitState` | Text identifier/name for exit state. Keep it consistent with the referenced animation, profile or application setting. Initial value: `"Base Layer.Enter Out"`. |
| `public string exitTrigger` | Text identifier/name for exit trigger. Keep it consistent with the referenced animation, profile or application setting. Initial value: `"EnterOut"`. |
| `public float footBlendSeconds` | Time in seconds used for foot blend seconds. Larger values make this phase/wait last longer. Initial value: `.16f`. |
| `public float handoverBlendSeconds` | Seconds for the final seated blend on entry and positional support fade on exit. Exit keeps Animator rotation. Default: 0.2; zero disables this additional blend. |
| `public virtual bool HasBindings { get; }` | Current has bindings predicate; read it instead of maintaining a second application flag. |
| `public bool holdFeetWhileIdle` | Disable when an application locomotion / ground IK system owns standing feet. |
| `public float horizontalScale` | Multiplier/fraction controlling horizontal scale. Increasing it increases this contribution relative to the unscaled value. Initial value: `1`. |
| `public int layer` | Animator layer index used to play and inspect boarding/exit states. |
| `public bool manualFootContacts` | Use foot-contact curves instead of automatic height/speed classification. |
| `public float plantHeight` | Plant height in metres in the owning system's space. Initial value: `.06f`. |
| `public float plantSpeed` | Foot-speed threshold used by planted-foot detection during access motion. Initial value: `.3f`. |
| `public float playbackSpeed` | Playback speed multiplier for the boarding and exit motion. Initial value: `1`. |
| `public float releaseEntryFeet` | Normalized boarding progress after which standing foot plants are released. |
| `public float rootMotionRotationWeight` | Weight of extracted root turning. |
| `public Vector3 rootMotionScale` | Local-axis scale of extracted root movement. The seat/outside anchors still define endpoints. |
| `public AnimationClip seatedClip` | Assign the seated clip reference used by AccessAnimationProfile. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public string seatedState` | Text identifier/name for seated state. Keep it consistent with the referenced animation, profile or application setting. Initial value: `"Base Layer.Seated"`. |
| `public AnimationCurve seatPose` | Blend to the physical seat pose. Reach 1 before handing over to seat physics. |
| `public AnimationClip standingClip` | Assign the standing clip reference used by AccessAnimationProfile. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public string standingState` | Text identifier/name for standing state. Keep it consistent with the referenced animation, profile or application setting. Initial value: `"Base Layer.Idle"`. |
| `public float transitionAllowance` | Extra time allowance in seconds for Animator state transitions during access. Initial value: `.2f`. |
| `public bool useAnimatorRootMotion` | Extract translation/turning from Animator root motion; enable for unbaked Root Transform tracks. Disable for movement baked into pose. |
| `public bool useFootIK` | Stabilize grounded feet during access; disable to use the uncorrected animation. |



| Declaration | Usage |
| --- | --- |
| `public float physicsBlendSeconds` | Seconds to fade the whole visible skeleton from the last entry animation pose into the live ragdoll. Physics runs immediately. Zero disables this visual blend. |

## AccessMotion

**Runtime/World/Passengers/Access/AccessMotion.cs**

Replaceable character-motion adapter called by `PassengerAccess` during entry/exit.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual float CompletionTimeout { get; }` | Additional seconds permitted after nominal motion duration before cancellation. |
| `public virtual bool IsComplete { get; }` | Current is complete predicate; read it instead of maintaining a second application flag. |
| `public virtual bool UsesAnimationDoorEvents { get; }` | Whether door requests must come from animation markers instead of timed fallback control. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public abstract bool Begin(SeatAccess access, PassengerBody passenger, bool entering)` | Attempts to begin character motion for the selected endpoint/body/direction. False rejects the adapter operation before successful motion ownership. | `access` — Access, interpreted by this operation in the declared type. `passenger` — Character body receiving motion/attachment. `entering` — `true` for entry motion; `false` for exit. **Returns:** `true` if the operation starts; `false` if admission fails. |
| `public virtual bool CanPlay(SeatAccess access, PassengerBody passenger, bool entering)` | Checks whether the motion adapter can play this access operation for the supplied body and direction. | `access` — Access, interpreted by this operation in the declared type. `passenger` — Character body receiving motion/attachment. `entering` — `true` for entry motion; `false` for exit. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public abstract void End(bool completed)` | Ends the motion adapter, using the completion flag to restore or hand over its owned state. | `completed` — `true` for successful motion completion; `false` for interruption/cleanup. |
| `public virtual float GetDuration(SeatAccess access, bool entering)` | Returns nominal access-motion duration for this endpoint and direction. | `access` — Access, interpreted by this operation in the declared type. `entering` — `true` for entry motion; `false` for exit. **Returns:** Computed float in the operation's documented unit/domain. |
| `public abstract void Sample(float normalizedTime)` | Receives normalized access progress from `PassengerAccess`; implement pose/motion sampling without choosing a new seat. | `normalizedTime` — Normalized access progress supplied by the owner. |

## AccessSide

**Runtime/World/Passengers/Access/SeatAccess.cs**

Defines the allowed access side choices used by this topic.

### Values

- `Left`
- `Right`
- `Custom`

## AccessState

**Runtime/World/Passengers/Access/PassengerAccess.cs**

Defines the allowed access state choices used by this topic.

### Values

- `Idle`
- `Opening`
- `Moving`
- `Closing`

## HumanoidAccessMotion

**Runtime/World/Passengers/Access/HumanoidAccessMotion.cs**

Built-in Animator-based humanoid access implementation.

**Inherits / implements:** [AccessMotion](PassengerAccess.md#accessmotion).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override float CompletionTimeout { get; }` | Additional seconds permitted after nominal motion duration before cancellation. |
| `public AccessAnimationProfile defaultProfile` | Fallback profile; a `SeatAccess` profile takes precedence for each request. |
| `public virtual AnimationClip enterClip { get; }` | Read-only/resolved enter clip for `HumanoidAccessMotion`. |
| `public virtual AnimationClip exitClip { get; }` | Read-only/resolved exit clip for `HumanoidAccessMotion`. |
| `public virtual AnimationClip idleClip { get; }` | Read-only/resolved idle clip for `HumanoidAccessMotion`. |
| `public override bool IsComplete { get; }` | Current is complete predicate; read it instead of maintaining a second application flag. |
| `public virtual Vector3 LeftFootLock { get; }` | Current left planted-foot support point in world space. |
| `public virtual bool LeftFootPlanted { get; }` | Read-only/resolved left foot planted for `HumanoidAccessMotion`. |
| `public virtual Vector3 RightFootLock { get; }` | Current right planted-foot support point in world space. |
| `public virtual bool RightFootPlanted { get; }` | Read-only/resolved right foot planted for `HumanoidAccessMotion`. |
| `public RuntimeAnimatorController seatedPoseController` | Optional controller sampled for the actual seated destination and restored after entry for Animator/Animator + IK passengers. Use the same controller as seated playback; default null retains the IK/reference target. |
| `public override bool UsesAnimationDoorEvents { get; }` | Whether door requests must come from animation markers instead of timed fallback control. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Begin(SeatAccess target, PassengerBody passenger, bool isEntering)` | Validates humanoid Animator, clips, mapped feet/pelvis and non-ragdoll state, then captures character/Animator state for access motion. | `target` — Configured target object/point; see declared type and owner. `passenger` — Character body receiving motion/attachment. `isEntering` — `true` for entry motion; `false` for exit. **Returns:** `true` if the operation starts; `false` if admission fails. |
| `public override bool CanPlay(SeatAccess target, PassengerBody passenger, bool isEntering)` | Checks whether the motion adapter can play this access operation for the supplied body and direction. | `target` — Configured target object/point; see declared type and owner. `passenger` — Character body receiving motion/attachment. `isEntering` — `true` for entry motion; `false` for exit. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual void Configure(AccessAnimationProfile profile)` | Selects the `AccessAnimationProfile` used by subsequent access motion. | `profile` — Movement/surface configuration, according to its declared type. |
| `public virtual float Duration(bool entering)` | Returns the built-in humanoid motion duration for the selected access direction/configuration. | `entering` — `true` for entry motion; `false` for exit. **Returns:** Computed float in the operation's documented unit/domain. |
| `public override void End(bool completed)` | Ends the motion adapter, using the completion flag to restore or hand over its owned state. | `completed` — `true` for successful motion completion; `false` for interruption/cleanup. |
| `public override float GetDuration(SeatAccess target, bool isEntering)` | Returns nominal access-motion duration for this endpoint and direction. | `target` — Configured target object/point; see declared type and owner. `isEntering` — `true` for entry motion; `false` for exit. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual void ReleaseIdleFeet()` | Releases temporary idle-foot ownership held during humanoid access motion. | No arguments; no returned value. |
| `public override void Sample(float normalizedTime)` | Evaluates the access motion or water style at the supplied normalized/world sample coordinates. | `normalizedTime` — Normalized access progress supplied by the owner. |

## PassengerAccess

**Runtime/World/Passengers/Access/PassengerAccess.cs**

Owns the entry/exit state machine, reservation and cancellation.

**Inherits / implements:** `MonoBehaviour`.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<PassengerSeatContext> AfterEnter` | After the complete entry sequence succeeds and the reservation/Target are cleared. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterExit` | After the complete exit sequence succeeds and the reservation/Target are cleared. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeEnter` | Before collision preparation, door requests and entry motion, after reservation succeeds. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeExit` | Before collision preparation, door requests and exit motion, while occupancy is retained. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> Cancelled` | After a started/prepared sequence is cancelled and the reservation/Target are cleared; context retains the original seat/passenger. Payload: immutable PassengerSeatContext. |
| `public UnityEvent cancelled` | Inspector callback when access is cancelled; no payload. |
| `public UnityEvent completed` | Inspector callback when access succeeds; no payload. |
| `public event Action<PassengerSeatContext> EnterBegin` | Once an admitted entry starts in Opening, after Before checks; seat reservation is held. |
| `public event Action<PassengerSeatContext> EnterCancelled` | After a reserved entry is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. |
| `public event Action<PassengerSeatContext> EnterFinished` | Only after the entire entry succeeds, including the required door state and reservation/Target cleanup. |
| `public event Action<PassengerAccessProgress> EnterInProgress` | After each entry motion sample in Moving, starting at zero; progress one is not whole-sequence completion. |
| `public event Action<PassengerSeatContext> ExitBegin` | Once an admitted exit starts in Opening, after Before checks; seat reservation is held. |
| `public event Action<PassengerSeatContext> ExitCancelled` | After a reserved exit is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. |
| `public event Action<PassengerSeatContext> ExitFinished` | Only after the entire exit succeeds, including the required door state and reservation/Target cleanup. |
| `public event Action<PassengerAccessProgress> ExitInProgress` | After each exit motion sample in Moving, starting at zero; progress one is not whole-sequence completion. |
| `public event Action<PassengerAccess, bool> Finished` | When an access attempt ends. Payload: `PassengerAccess` and success bool; inspect actual occupancy after cancellation/handover. |
| `public UnityEvent onEnterBegin` | Inspector counterpart of `EnterBegin`; no payload. |
| `public UnityEvent onEnterCancelled` | Inspector counterpart of `EnterCancelled`; no payload. |
| `public UnityEvent onEnterFinish` | Inspector counterpart of `EnterFinished`; no payload. |
| `public UnityEvent<float> onEnterInProgress` | Inspector counterpart of `EnterInProgress`; receives normalized motion time (0..1). |
| `public UnityEvent onExitBegin` | Inspector counterpart of `ExitBegin`; no payload. |
| `public UnityEvent onExitCancelled` | Inspector counterpart of `ExitCancelled`; no payload. |
| `public UnityEvent onExitFinish` | Inspector counterpart of `ExitFinished`; no payload. |
| `public UnityEvent<float> onExitInProgress` | Inspector counterpart of `ExitInProgress`; receives normalized motion time (0..1). |
| `public UnityEvent started` | Inspector callback when access sequencing starts; no payload. |
| `public event Action<PassengerAccess, AccessState> StateChanged` | When access sequencing changes. Payload: `PassengerAccess` and `AccessState`; seat occupancy may commit at a different boundary. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual bool IsBusy { get; }` | Current is busy predicate; read it instead of maintaining a second application flag. |
| `public virtual bool IsEntering { get; protected set; }` | True for entry, false for exit; retains the last direction while idle. |
| `public AccessMotion motion` | Motion adapter that owns the character pose during Moving; it is ended on success or cancellation. |
| `public PassengerBody passenger` | Assign the passenger PassengerBody component/asset used by PassengerAccess. |
| `public virtual AccessState State { get; protected set; }` | Current sequence phase: Idle, Opening, Moving or Closing. |
| `public virtual SeatAccess Target { get; protected set; }` | Current access endpoint; cleared before outcome callbacks. Use their captured context for the original seat. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void AnimationDoor(bool open)` | Routes an animation door request into the current passenger access sequence. | `open` — Requested open state. |
| `public virtual void Cancel()` | Unwinds this access attempt's motion/reservation and performs its state-specific occupancy cleanup. Already committed occupancy need not be undone. | No arguments; no returned value. |
| `public virtual bool TryEnter(SeatAccess access)` | Admits an asynchronous entry and reserves the endpoint/seat. True means started, not occupied/completed; observe Finished and actual seat occupancy. | `access` — Access, interpreted by this operation in the declared type. **Returns:** `true` when admitted; synchronous begin-listener cancellation returns `false`. Observe directional events for the eventual outcome. |
| `public virtual bool TryExit()` | Admits asynchronous departure. Seat release and motion completion occur at different boundaries; observe Finished for sequence outcome. | **Returns:** `true` when admitted; synchronous begin-listener cancellation returns `false`. Observe directional events for the eventual outcome. |

## PassengerAccessProgress

**Runtime/World/Passengers/Access/PassengerAccess.cs**

Immutable value snapshot sent by the directional motion-progress events. No per-sample heap allocation. Normalized motion time can remain at one while the adapter finishes blending or while the operation still waits for its door.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public PassengerSeatContext Context { get; }` | Original vehicle, passenger and seat identities captured at admission; retained after cleanup. |
| `public float Duration { get; }` | Nominal motion duration in seconds from the adapter; excludes extra completion/door waits. |
| `public float ElapsedTime { get; }` | Seconds elapsed in Moving, including holds/waits during that phase. |
| `public bool IsEntering { get; }` | True for entry; false for exit. |
| `public float NormalizedTime { get; }` | Nominal motion progress clamped to 0..1. Zero is sent after the initial motion sample. One is not a success notification. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public PassengerAccessProgress(PassengerSeatContext context, bool isEntering, float normalizedTime, float elapsedTime, float duration)` | Creates a value snapshot; clamps normalized time to 0..1 and elapsed/duration to nonnegative values. | `context` — Captured identities; `isEntering` — Direction; `normalizedTime` — Motion progress; `elapsedTime`, `duration` — Seconds. |

## SeatAccess

**Runtime/World/Passengers/Access/SeatAccess.cs**

Describes the seat endpoint, outside marker, door and admission settings.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public AccessAnimationProfile animationProfile` | Assign the animation profile AccessAnimationProfile component/asset used by SeatAccess. |
| `public float clearanceHeight` | Clearance height in metres in the owning system's space. Initial value: `1.7f`. |
| `public LayerMask clearanceMask` | Layers tested when checking whether access space is blocked. Initial value: `~0`. |
| `public float clearanceRadius` | Clearance radius in metres in the owning system's space. Initial value: `.25f`. |
| `public float closedDoorTolerance` | Threshold/tolerance for closed door tolerance. The corresponding action or transition is admitted only when its comparison condition is satisfied. Initial value: `3`. |
| `public VehicleBodyPart door` | Assign the door VehicleBodyPart component/asset used by SeatAccess. |
| `public virtual bool DoorAvailable { get; }` | Read-only/resolved door available for `SeatAccess`. |
| `public virtual bool DoorIsOpen { get; }` | Read-only/resolved door is open for `SeatAccess`. |
| `public float doorTimeout` | Maximum time in seconds allowed for the door to reach the required access position. Initial value: `2`. |
| `public Transform doorway` | Assign the doorway reference used by SeatAccess. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float duration` | Time in seconds over which this transition/action runs. Initial value: `1.6f`. |
| `public float groundProbeDistance` | Ground probe distance in metres in the owning system's space. Initial value: `5`. |
| `public float groundProbeHeight` | Ground probe height in metres in the owning system's space. Initial value: `2`. |
| `public float interactionDistance` | Interaction distance in metres in the owning system's space. Initial value: `2`. |
| `public float maximumAngularSpeed` | Maximum vehicle angular speed in radians per second during entry/exit. |
| `public float maximumGroundDrop` | Largest permitted downward projection from the authored outside point, in metres. |
| `public float maximumGroundRise` | Largest permitted upward projection from the authored outside point, in metres. |
| `public float maximumSpeed` | Maximum vehicle point speed in m/s during entry/exit. |
| `public float minimumGroundNormal` | Minimum upward ground normal for outside placement; 0.5 accepts slopes up to 60 degrees. |
| `public AccessAnimationProfile openDoorAnimationProfile` | Optional already-open-door variant; falls back to the standard profile. Previously open doors remain open and need no door markers. |
| `public float openDoorTolerance` | Threshold/tolerance for open door tolerance. The corresponding action or transition is admitted only when its comparison condition is satisfied. Initial value: `8`. |
| `public Transform outside` | Feet-level endpoint. Runtime never moves this transform. |
| `public float outsideGroundClearance` | Outside ground clearance in metres in the owning system's space. Initial value: `.02f`. |
| `public virtual Vector3 OutsidePosition { get; }` | Resolved outside position after optional support projection. |
| `public bool projectOutsideToGround` | Projects the outside access pose onto acceptable ground using the configured ground probe. Initial value: `true`. |
| `public PassengerSeat seat` | Assign the seat PassengerSeat component/asset used by SeatAccess. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public AccessSide side` | Descriptive side label; the assigned profile selects the actual clips and triggers. |
| `public Vector3 standingOffset` | Optional offset from Outside in this seat's local axes. |
| `public bool useOutsideRotation` | When checked, use outside rotation is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool CanContinue(PassengerBody passenger)` | Checks whether an admitted seat-access sequence can still continue. | `passenger` — Character body receiving motion/attachment. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual bool CanUse(PassengerBody passenger, bool entering)` | Checks whether a seat-access endpoint is currently usable by the supplied passenger. | `passenger` — Character body receiving motion/attachment. `entering` — `true` for entry motion; `false` for exit. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual bool DoorReady(bool open)` | Checks whether the configured door has reached the required access state. | `open` — Requested open state. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual bool IsExitClear(PassengerBody passenger)` | Checks the configured outside endpoint capsule for exit clearance; it does not plan a route. | `passenger` — Character body receiving motion/attachment. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual void RequestDoor(bool open)` | Requests the configured access door's required state for the current operation. | `open` — Requested open state. |


| Declaration | Usage |
| --- | --- |
| `public UnityEvent onEnterBegin` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<float> onEnterInProgress` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent onEnterFinish` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent onEnterCancelled` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent onExitBegin` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<float> onExitInProgress` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent onExitFinish` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent onExitCancelled` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
