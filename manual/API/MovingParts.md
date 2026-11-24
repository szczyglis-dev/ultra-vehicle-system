# General moving parts API

Read [the system explanation](../Scripting/MovingParts.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [ICustomPartMotion](MovingParts.md#icustompartmotion)
- [IPartMotionSource](MovingParts.md#ipartmotionsource)
- [MovingPart](MovingParts.md#movingpart)
- [MovingPartMotion](MovingParts.md#movingpartmotion)
- [MovingPartSpace](MovingParts.md#movingpartspace)
- [PartClipAnimation](MovingParts.md#partclipanimation)
- [PartMotionAudio](MovingParts.md#partmotionaudio)
- [PartMotionEvent](MovingParts.md#partmotionevent)
- [PartMotionEvents](MovingParts.md#partmotionevents)
- [PartMotionPlayback](MovingParts.md#partmotionplayback)
- [PartMotionSignals](MovingParts.md#partmotionsignals)
- [PartMotionStopReason](MovingParts.md#partmotionstopreason)
- [PedalDrive](MovingParts.md#pedaldrive)
- [SteeringPart](MovingParts.md#steeringpart)

## ICustomPartMotion

**Runtime/Contracts/Exterior/ICustomPartMotion.cs**

Custom pose owner called by the shared part-motion lifecycle. Report progress and completion through the supplied playback object.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void BeginMotion(PartMotionPlayback motion)` | Starts custom movement after a target is accepted. May report progress or complete synchronously. | — |
| `void StopMotion(PartMotionPlayback motion, PartMotionStopReason reason)` | Stops external movement with the supplied completion, stop or cancellation reason. | — |
| `void TickMotion(PartMotionPlayback motion, float deltaTime)` | Updates the active custom operation using elapsed seconds. | — |

## IPartMotionSource

**Runtime/Contracts/Exterior/IPartMotionSource.cs**

Presentation or lifecycle contract for independent vehicle components.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `event Action MotionAudioStopped` | Requests stopping movement audio after interruption or disable. |
| `event Action<PartMotionEvent> MotionOccurred` | Reports an admitted movement phase to optional presentation receivers. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `Transform AudioEmitter { get; }` | Transform used as the emitter for movement presentation. |

## MovingPart

**Runtime/Exterior/Parts/MovingPart.cs**

Owns rotation/translation requests, constraints and scheduled motion.

**Inherits / implements:** [ExteriorModule](Modules.md#exteriormodule), [IPartMotionSource](MovingParts.md#ipartmotionsource).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action ClosingCompleted` | Once after the actual pose reaches the requested closing target. No payload. |
| `public event System.Action ClosingStarted` | Once before a closing operation moves the pose. No payload. |
| `public event System.Action MotionAudioStopped` | Requests stopping movement audio after interruption or disable. |
| `public event System.Action<bool> MotionEnabledChanged` | Reports a changed movement request after pending motion is stopped when disabling. |
| `public event System.Action<PartMotionEvent> MotionOccurred` | Reports an admitted movement phase to optional presentation receivers. |
| `public event System.Action<MovingPart> Moved` | Reports this moving part after its actual pose changes. |
| `public event System.Action OpeningCompleted` | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
| `public event System.Action OpeningStarted` | Once before an opening operation moves the pose. No payload; interruptions never imply completion. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform anchor` | Optional independent pivot and axis frame for rotation and Part-space translation. Keeps the authored neutral pose; must remain outside the moving part hierarchy. |
| `public virtual float Angle { get; protected set; }` | Read-only/resolved angle for `MovingPart`. |
| `public Vector2 angleLimits` | Lower/upper components defining the angle limits range in the owning mechanism's units. Initial value: `new Vector2(-45, 45)`. |
| `public Transform AudioEmitter { get; }` | Transform used as the emitter for movement presentation. |
| `public AnimationCurve decreasingMotionCurve` | Normalized elapsed time to travel progress toward a lower angle/position. Independent of the increasing curve. Speed sets average travel speed; target changes restart from the current pose. Default: linear time-to-progress curve. |
| `public bool increasingIsOpening` | Increasing angle/position plays Opening Clips when true; reverse to swap clip roles. Default true. |
| `public AnimationCurve increasingMotionCurve` | Normalized elapsed time to travel progress toward a higher angle/position. Linear preserves constant speed; flatten near the end to slow down. Applies to fixed targets, not rate input or aiming. Default: linear time-to-progress curve. |
| `public virtual float Input { get; protected set; }` | Signed rate-control demand from minus one to one. |
| `public virtual bool IsClosing { get; }` | An accepted closing operation is pending; false after completion or cancellation. |
| `public virtual bool IsMoving { get; }` | Whether enabled rate/target movement remains possible at the configured speed and limits. |
| `public virtual bool IsOpening { get; }` | An accepted opening operation is pending; false after completion or cancellation. |
| `public bool limitRotation` | When checked, limit rotation is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public Vector3 localAxis` | Local axis around which the configured motion or operation takes place. Initial value: `Vector3.up`. |
| `public Vector3 localForward` | Local forward vector used by the part when resolving its directional motion. Initial value: `Vector3.forward`. |
| `public MovingPartMotion motion` | Anchor, axes and range describing the visible control's motion. Options: `Rotation`, `Translation`. |
| `public bool motionEnabled` | Enables motion behavior for this system. Initial value: `true`. |
| `public PartMotionEvents motionEvents` | Inspector UnityEvent callbacks for the same four operation notifications; also accessible through GetEvent. |
| `public virtual float NormalizedPosition { get; }` | Read-only/resolved normalized position for `MovingPart`. |
| `public Transform part` | Assign the part reference used by MovingPart. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public PartMotionPlayback playback` | Clip or custom motion implementation, plus lifecycle callbacks. Rotation/Translation still use the existing procedural path. |
| `public virtual float Position { get; protected set; }` | Current translation offset in metres relative to the moving part's captured neutral pose. |
| `public bool reverse` | Mirror motion around the neutral pose without changing input or travel limits. |
| `public bool showGizmos` | Show motion guides and the active pose owner in the Scene view. |
| `public PartMotionSignals Signals { get; }` | Notifications for requests, progress and operation termination. |
| `public float speed` | Angular rate in degrees per second; average travel speed for fixed targets with direction curves. Initial value: `35`. |
| `public virtual float TargetAngle { get; protected set; }` | Requested rotation angle before speed-limited travel, in degrees. |
| `public virtual float TargetPosition { get; protected set; }` | Read-only/resolved target position for `MovingPart`. |
| `public Transform translationAnchor` | Optional direction override for Anchor translation space; otherwise uses Anchor. Must remain outside the moving part hierarchy. |
| `public Vector3 translationDirectionAngles` | Additional Euler rotation of the travel axis in the selected coordinate space, in degrees. |
| `public Vector2 translationLimits` | Translation travel in metres, measured from the authored neutral pose. |
| `public MovingPartSpace translationSpace` | Selects the translation space policy for this configuration. Options: `Part`, `Parent`, `World`, `Anchor`. |
| `public float translationSpeed` | Translation rate in metres per second; average travel speed for fixed targets with direction curves. Initial value: `.2f`. |
| `public virtual Vector3 WorldPosition { get; }` | Read-only/resolved world position for `MovingPart`. |
| `public virtual Quaternion WorldRotation { get; }` | Read-only/resolved world rotation for `MovingPart`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void AimAt(Transform target)` | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. | — |
| `public virtual void AimAt(Vector3 worldPoint)` | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. | — |
| `public virtual void Cancel()` | Cancels active movement and releases its operation ownership. | — |
| `public virtual void CaptureNeutralPose()` | Replaces a moving part's neutral baseline and clears its previous motion requests. | — |
| `public virtual float ClampAngle(float angle)` | Returns the requested angle restricted by the moving part's configured angular policy. | — |
| `public virtual float ClampPosition(float value)` | Returns a translation offset restricted to the configured travel limits. | — |
| `public virtual void CompleteCustomMotion()` | Completes the current custom movement operation successfully. | — |
| `public override void Configure(VehicleController vehicle)` | Ensures its neutral pose is captured without recapturing every configuration. | — |
| `public virtual void GetRotationFrame(out Vector3 worldPivot, out Quaternion worldNeutralRotation)` | Returns the moving part's configured rotation pivot/orientation frame. | — |
| `public virtual void GetTranslationFrame(out Vector3 origin, out Vector3 direction)` | Returns the configured frame used to interpret translation travel. | — |
| `public virtual void ReportProgress(float normalizedValue)` | Reports actual normalized progress from a custom pose owner. | — |
| `public virtual void ReturnToNeutral()` | Requests movement toward the configured neutral pose within the part's limits. | — |
| `public virtual void SetAngle(float angle)` | Immediately applies a moving-part/geometry rotation in degrees. | — |
| `public virtual void SetInput(float input)` | Takes signed rate-input ownership for the configured rotation/translation mode; zero pauses rate travel. | — |
| `public virtual void SetMotionEnabled(bool value)` | Changes moving-part actuation availability and its notification state. | — |
| `public virtual void SetNormalizedPosition(float value)` | Maps a 0–1 fraction across the moving part's translation interval. | — |
| `public virtual void SetPosition(float value)` | Applies an immediate bounded translation offset in metres from the captured neutral pose. | — |
| `public virtual void SetTargetAngle(float angle, bool shortestPath = true)` | Requests smooth motion toward a bounded angle, optionally using shortest-arc policy. | — |
| `public virtual void SetTargetPosition(float value)` | Requests smooth motion toward a bounded translation offset. | — |
| `public virtual void StartMotion(float normalizedTarget)` | Requests movement to a normalized destination using the selected motion mode. | — |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances `Tick` using the controller's timestep; no second caller is needed while registered. | — |
| `public virtual void Stop()` | Clears moving-part rate, target and tracking requests at its current pose. | — |
| `public virtual void Tick(float deltaTime)` | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | — |

## MovingPartMotion

**Runtime/Exterior/Parts/MovingPart.cs**

Defines the allowed moving part motion choices used by this topic.

| Value | Meaning |
| --- | --- |
| Rotation | `Rotation` — Inspector display label for this mode. |
| Translation | `Translation` — Inspector display label for this mode. |
| Animation | `Animation` — Clip-sampled movement. |
| Custom | `Custom` — Application-owned movement through callbacks or a custom driver. |

## MovingPartSpace

**Runtime/Exterior/Parts/MovingPart.cs**

Defines the allowed moving part space choices used by this topic.

### Values

- `Part`
- `Parent`
- `World`
- `Anchor`

## PartClipAnimation

**Runtime/Exterior/Parts/Motion/PartClipAnimation.cs**

Samples a non-Legacy animation clip on an assigned Animator, with an optional separate closing clip.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Animator animator` | Animator whose hierarchy is sampled by the clip. |
| `public AnimationClip clip` | Primary non-Legacy clip for normalized part movement. |
| `public AnimationClip closingClip` | Optional forward-playing closing clip; otherwise the primary clip is sampled backwards. |
| `public float duration` | Full-trip duration in seconds; zero uses the selected clip length. |
| `public bool IsConfigured { get; }` | Whether the primary clip has been assigned. |
| `public bool IsPrepared { get; }` | Whether clip playback resources have been prepared. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public bool CanSample(bool opening)` | Validates clip/Animator compatibility before allocating or evaluating playback resources. | — |
| `public void Dispose()` | Releases the prepared animation graph. | — |
| `public float Duration(bool opening)` | Returns the configured duration or selected opening/closing clip length. | — |
| `public bool Sample(float value, bool opening)` | Maps opening/closing progress into the selected clip without changing the serialized clip assignment. | — |
| `public void SetClipOverride(AnimationClip value)` | Per-operation clips (for example selected gear poses) never overwrite the serialized shared clip, so runtime reconfiguration and Inspector authoring agree. | — |

## PartMotionAudio

**Runtime/Exterior/Parts/PartMotionAudio.cs**

Four cue clip lists and optional independent settings overrides. The Audio Settings group configures shared playback; individual cues can override it.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip[] closingClips` | Random clips for ClosingStarted. Empty lists remain silent and create no sources. |
| `public AudioSettingsOverride closingCompleted` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip[] closingCompletedClips` | Random clips for actual closing arrival; separate from the closing request/start cue. |
| `public AudioSettingsOverride closingStarted` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip[] openingClips` | Random clips for OpeningStarted. Null entries are skipped. |
| `public AudioSettingsOverride openingCompleted` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip[] openingCompletedClips` | Random clips for actual opening arrival; separate from the opening request/start cue. |
| `public AudioSettingsOverride openingStarted` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public AudioClip[] GetClips(PartMotionEvent motionEvent)` | Returns the selected cue’s clip array by reference. Invalid event values throw ArgumentOutOfRangeException. | — |
| `public VehicleAudioSettings GetSettings(PartMotionEvent motionEvent)` | Returns the selected cue override when Override Settings is enabled, otherwise returns the shared audioSettings instance. Invalid enum values throw ArgumentOutOfRangeException. | — |
| `public void SetClips(PartMotionEvent motionEvent, params AudioClip[] clips)` | Replaces the selected clip array; null becomes an empty array. Invalid event values throw ArgumentOutOfRangeException. | — |

## PartMotionEvent

**Runtime/Exterior/Parts/PartMotionEvents.cs**

Identifies one of the four start/arrival cues; does not represent a continuous motor loop.

### Values

- `OpeningStarted`
- `OpeningCompleted`
- `ClosingStarted`
- `ClosingCompleted`

## PartMotionEvents

**Runtime/Exterior/Parts/PartMotionEvents.cs**

Inspector callbacks shared by VehicleBodyPart and MovingPart. C# events on the component publish the same operation notifications.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public UnityEvent onClosingCompleted` | Inspector UnityEvent for closing arrival. |
| `public UnityEvent onClosingStarted` | Inspector UnityEvent for closing start. |
| `public UnityEvent onOpeningCompleted` | Inspector UnityEvent for opening arrival. |
| `public UnityEvent onOpeningStarted` | Inspector UnityEvent for opening start. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public UnityEvent GetEvent(PartMotionEvent motionEvent)` | Returns the selected Inspector UnityEvent for subscribing with AddListener/RemoveListener. Invalid event values throw ArgumentOutOfRangeException. | — |

## PartMotionPlayback

**Runtime/Exterior/Parts/PartMotionPlayback.cs**

Shared normalized motion state used by procedural parts, animation clips and custom movement drivers.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public PartClipAnimation animation` | Animation clip, binding root and optional closing animation. |
| `public MonoBehaviour customDriver` | Optional component implementing ICustomPartMotion. Inspector callbacks can be used instead, or alongside it. |
| `public bool IsActive { get; private set; }` | Whether an operation is in progress. |
| `public bool IsCustom { get; }` | Whether the selected mode uses a custom movement owner. |
| `public bool IsExternal { get; }` | Whether Animation or Custom owns the pose instead of procedural geometry. |
| `public PartMotionStopReason LastStopReason { get; private set; }` | Most recent operation termination reason. |
| `public UnityEngine.Object Owner { get; private set; }` | Component whose motion is being coordinated. |
| `public int Revision { get; private set; }` | Operation version used to reject stale work after reentrant callbacks. |
| `public PartMotionSignals signals` | Movement lifecycle and external movement requests, available in code and the Inspector. |
| `public float Target { get; private set; }` | Accepted normalized destination (0–1). |
| `public float Value { get; private set; }` | Last reported normalized progress (0–1). |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void Cancel()` | Cancels an active operation and notifies its external movement owner. | — |
| `public void Complete()` | Ends an active operation successfully. | — |
| `public void Configure(UnityEngine.Object owner, int motionMode)` | Assigns the owner and motion mode; a mode change cancels the previous operation and releases its playback resources. | — |
| `public void Dispose()` | Cancels active work and releases implementation and clip resources. | — |
| `public void Drive(float value)` | Passes a normalized control value to the selected implementation. | — |
| `public void Initialize(float value)` | Sets initial progress once; ignores non-finite values and clamps to 0–1. | — |
| `public bool PrepareDrive(float value)` | Prepares an operation for a value already interpolated by the owning control. | — |
| `public void ReportProgress(float value)` | Clamps and publishes actual progress; Custom mode does not write a pose. | — |
| `public bool Request(float target)` | Requests a normalized target; returns whether that operation remains active after callbacks. An already reached endpoint does not restart it. | — |
| `public void SetInput(float value)` | Publishes a changed signed rate request, clamped to −1–1. | — |
| `public void Stop()` | Stops an active operation without successful completion. | — |
| `public void Tick(float deltaTime)` | Publishes the active update and advances the selected implementation; ignores invalid or nonpositive timesteps. | — |

## PartMotionSignals

**Runtime/Exterior/Parts/Motion/PartMotionSignals.cs**

C# and Inspector notifications for accepted requests, progress and operation termination.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<float> Began` | Accepted normalized operation target; a listener may cancel or replace it. |
| `public event Action Cancelled` | After an operation is interrupted, replaced or cancelled. |
| `public event Action Ended` | After successful completion; manual stop and cancellation do not raise it. |
| `public event Action<float> InputChanged` | Changed signed rate demand, including zero on release. |
| `public event Action<float> Moved` | Actual normalized progress after a pose update. |
| `public event Action<float> MoveRequested` | Accepted normalized target request for an external movement owner. |
| `public event Action Stopped` | After successful completion, manual stop or cancellation. |
| `public event Action StopRequested` | Explicit stop/cancel request for an external movement owner. |
| `public event Action<float> TickRequested` | Elapsed seconds during an active motion update. |
| `public UnityEvent<float> onBegin` | Accepted normalized operation target; a listener may cancel or replace it. |
| `public UnityEvent onCancel` | After an operation is interrupted, replaced or cancelled. |
| `public UnityEvent onEnd` | After successful completion; manual stop and cancellation do not raise it. |
| `public UnityEvent<float> onInputChanged` | Changed signed rate demand, including zero on release. |
| `public UnityEvent<float> onMove` | Actual normalized progress after a pose update. |
| `public UnityEvent<float> onMoveRequested` | Accepted normalized target request for an external movement owner. |
| `public UnityEvent onStop` | After successful completion, manual stop or cancellation. |
| `public UnityEvent onStopRequested` | Explicit stop/cancel request for an external movement owner. |
| `public UnityEvent<float> onTick` | Elapsed seconds during an active motion update. |

## PartMotionStopReason

**Runtime/Contracts/Exterior/ICustomPartMotion.cs**

Completion, manual stop and cancellation outcomes for a part-motion operation.

| Value | Meaning |
| --- | --- |
| Completed | `Completed` — Operation completed successfully. |
| Stopped | `Stopped` — Operation stopped manually. |
| Cancelled | `Cancelled` — Operation cancelled or replaced. |

## PedalDrive

**Runtime/Exterior/Bicycle/PedalDrive.cs**

**Inherits / implements:** `ExteriorModule`, `IVehicleResetHandler`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float boostCadenceMultiplier` | Maximum cadence multiplier at full nitro strength. Road speed still determines the requested cadence. Initial value: `1.5f`. |
| `public float Cadence { get; private set; }` | Current crank speed in revolutions per minute. |
| `public float cadenceResponse` | Cadence acceleration/deceleration in RPM per second. |
| `public Transform crank` | Crank pivot; its local axis follows the wheel axle. |
| `public float CrankAngle { get; }` | Current crank angle in degrees. |
| `public float driveRatio` | Driven-wheel revolutions per crank revolution. |
| `public Transform leftPedal` | Independent pedal pivot counter-rotated to keep the left foot platform level. |
| `public Vector3 localAxis` | Crank rotation axis in the pivot's initial local frame. |
| `public float maximumCadence` | Maximum cadence in revolutions/minute. |
| `public float minimumCadence` | Minimum cadence while actively pedalling, in revolutions/minute. |
| `public bool pedalWhileCoasting` | Keep rotating while coasting forward. Otherwise requires forward throttle. |
| `public override ExecutionPhase Phase { get; }` | Presentation, before passenger target solving. |
| `public BalanceRider rider` | Rider whose occupied seat and riding blend enable pedalling. |
| `public Transform rightPedal` | Independent pedal pivot counter-rotated to keep the right foot platform level. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Caches wheel geometry and authored crank/pedal rest poses. | — |
| `public void ResetVehicleState(VehicleResetReason reason)` | Clears cadence and restores the authored crank/pedal pose. | — |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances this mechanism through the vehicle physics pipeline. | — |
| `public override bool SupportsProfile(DriveProfile profile)` | Supports wheel-based profiles. | — |

## SteeringPart

**Runtime/Exterior/Parts/SteeringPart.cs**

Rotates a rudder, outboard motor or another visible steering pivot from a scalar source, independently of vehicle forces.

**Inherits / implements:** [ExteriorModule](Modules.md#exteriormodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform anchor` | Optional independent rotation pivot and local axis frame. Keeps the authored neutral pose. |
| `public MonoBehaviour inputSource` | Optional Steering Source or another IInteriorValueSource. Empty uses the vehicle steering command; disabled or invalid sources produce zero. Default `None / unassigned`. |
| `public Vector3 localAxis` | Rotation axis in the part neutral local frame. Default `Vector3.up`. |
| `public AircraftControlMotionMode motionMode` | Procedural rotation/translation, clip animation or callback-only custom movement. |
| `public float multiplier` | Scales steering travel; zero stops rotation. Default `1`. |
| `public Transform part` | Rudder, outboard motor or other steering pivot. Initial local rotation is neutral. Default `None / unassigned`. |
| `public PartMotionPlayback playback` | Animation/custom implementation and lifecycle callbacks. |
| `public float response` | Steering response per second; zero follows the source immediately. Default `8`. |
| `public bool reverse` | Reverses visible steering rotation. Default `false`. |
| `public bool showGizmos` | Show mode-specific steering motion guides in the Scene view. |
| `public PartMotionSignals Signals { get; }` | Notifications for requests, progress and operation termination. |
| `public float steeringAngle` | Angle in degrees at full steering before Multiplier and Reverse. Default `30`. |
| `public float translationTravel` | Metres of translation at full steering in either direction. |
| `public VehicleController vehicle` | Optional fallback vehicle; finds the parent vehicle when empty. Default `None / unassigned`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void CancelMotion()` | Cancels active movement and releases its operation ownership. | — |
| `public virtual void CompleteCustomMotion()` | Completes the current custom movement operation successfully. | — |
| `public override void Configure(VehicleController owner)` | Resolves the fallback vehicle when none is assigned. | — |
| `public virtual void ReportProgress(float value)` | Reports actual normalized progress from a custom pose owner. | — |
| `public virtual void StopMotion()` | Stops the current movement operation without reporting successful completion. | — |
