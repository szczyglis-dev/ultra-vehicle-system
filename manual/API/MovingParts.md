# General moving parts API

Read [the system explanation](../Scripting/MovingParts.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [IPartMotionSource](MovingParts.md#ipartmotionsource)
- [MovingPart](MovingParts.md#movingpart)
- [MovingPartMotion](MovingParts.md#movingpartmotion)
- [MovingPartSpace](MovingParts.md#movingpartspace)
- [PartMotionAudio](MovingParts.md#partmotionaudio)
- [PartMotionEvent](MovingParts.md#partmotionevent)
- [PartMotionEvents](MovingParts.md#partmotionevents)
- [PedalDrive](MovingParts.md#pedaldrive)
- [SteeringPart](MovingParts.md#steeringpart)

## IPartMotionSource

**Runtime/Exterior/Parts/IPartMotionSource.cs**

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
| `public event System.Action<bool> MotionEnabledChanged` | // Reports a changed movement request after pending motion is stopped when disabling. |
| `public event System.Action<PartMotionEvent> MotionOccurred` | Reports an admitted movement phase to optional presentation receivers. |
| `public event System.Action<MovingPart> Moved` | // Reports this moving part after its actual pose changes. |
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
| `public virtual float Position { get; protected set; }` | Current translation offset in metres relative to the moving part's captured neutral pose. |
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
| `public virtual void AimAt(Transform target)` | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. | `target` — Configured target object/point; see declared type and owner. |
| `public virtual void AimAt(Vector3 worldPoint)` | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. | `worldPoint` — World-space target/sample point. |
| `public virtual void CaptureNeutralPose()` | Replaces a moving part's neutral baseline and clears its previous motion requests. | No arguments; no returned value. |
| `public virtual float ClampAngle(float angle)` | Returns the requested angle restricted by the moving part's configured angular policy. | `angle` — Angular coordinate in degrees for this geometry operation. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual float ClampPosition(float value)` | Returns a translation offset restricted to the configured travel limits. | `value` — Requested state/value in this operation's domain; use its configured range/unit. **Returns:** Computed float in the operation's documented unit/domain. |
| `public override void Configure(VehicleController vehicle)` | Ensures its neutral pose is captured without recapturing every configuration. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void GetRotationFrame(out Vector3 worldPivot, out Quaternion worldNeutralRotation)` | Returns the moving part's configured rotation pivot/orientation frame. | `worldPivot` — World-space rotation pivot. `worldNeutralRotation` — World-space baseline orientation. |
| `public virtual void GetTranslationFrame(out Vector3 origin, out Vector3 direction)` | Returns the configured frame used to interpret translation travel. | `origin` — World origin/frame for this geometry calculation. `direction` — Direction, interpreted by this operation in the declared type. |
| `public virtual void ReturnToNeutral()` | Requests movement toward the configured neutral pose within the part's limits. | No arguments; no returned value. |
| `public virtual void SetAngle(float angle)` | Immediately applies a moving-part/geometry rotation in degrees. | `angle` — Angular coordinate in degrees for this geometry operation. |
| `public virtual void SetInput(float input)` | Takes signed rate-input ownership for the configured rotation/translation mode; zero pauses rate travel. | `input` — Command handle channel or normalized rate, according to the signature. |
| `public virtual void SetMotionEnabled(bool value)` | Changes moving-part actuation availability and its notification state. | `value` — Requested bool state for this operation. |
| `public virtual void SetNormalizedPosition(float value)` | Maps a 0–1 fraction across the moving part's translation interval. | `value` — Requested state/value in this operation's domain; use its configured range/unit. |
| `public virtual void SetPosition(float value)` | Applies an immediate bounded translation offset in metres from the captured neutral pose. | `value` — Requested state/value in this operation's domain; use its configured range/unit. |
| `public virtual void SetTargetAngle(float angle, bool shortestPath = true)` | Requests smooth motion toward a bounded angle, optionally using shortest-arc policy. | `angle` — Angular coordinate in degrees for this geometry operation. `shortestPath` — Whether angular target travel uses shortest-arc policy. Default: `true`. |
| `public virtual void SetTargetPosition(float value)` | Requests smooth motion toward a bounded translation offset. | `value` — Requested state/value in this operation's domain; use its configured range/unit. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances `Tick` using the controller's timestep; no second caller is needed while registered. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void Stop()` | Clears moving-part rate, target and tracking requests at its current pose. | No arguments; no returned value. |
| `public virtual void Tick(float deltaTime)` | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | `deltaTime` — Elapsed time in seconds supplied by the owning loop. |



| Declaration | Usage |
| --- | --- |
| `public bool reverse` | Mirror motion around the neutral pose without changing input or travel limits. |

## MovingPartMotion

**Runtime/Exterior/Parts/MovingPart.cs**

Defines the allowed moving part motion choices used by this topic.

### Values

- `Rotation`
- `Translation`

## MovingPartSpace

**Runtime/Exterior/Parts/MovingPart.cs**

Defines the allowed moving part space choices used by this topic.

### Values

- `Part`
- `Parent`
- `World`
- `Anchor`

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
| `public UnityEvent closingCompleted` | Inspector UnityEvent for closing arrival. |
| `public UnityEvent closingStarted` | Inspector UnityEvent for closing start. |
| `public UnityEvent openingCompleted` | Inspector UnityEvent for opening arrival. |
| `public UnityEvent openingStarted` | Inspector UnityEvent for opening start. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public UnityEvent GetEvent(PartMotionEvent motionEvent)` | Returns the selected Inspector UnityEvent for subscribing with AddListener/RemoveListener. Invalid event values throw ArgumentOutOfRangeException. | — |

## PedalDrive

**Runtime/Exterior/Bicycle/PedalDrive.cs**

**Inherits / implements:** `ExteriorModule`, `IVehicleResetHandler`.

| Member | Meaning |
| --- | --- |
| `public override ExecutionPhase Phase { get; }` | Presentation, before passenger target solving. |
| `public BalanceRider rider` | Rider whose occupied seat and riding blend enable pedalling. |
| `public Transform crank` | Crank pivot; its local axis follows the wheel axle. |
| `public Transform leftPedal` | Independent pedal pivot counter-rotated to keep the left foot platform level. |
| `public Transform rightPedal` | Independent pedal pivot counter-rotated to keep the right foot platform level. |
| `public Vector3 localAxis` | Crank rotation axis in the pivot's initial local frame. |
| `public float driveRatio` | Driven-wheel revolutions per crank revolution. |
| `public float minimumCadence` | Minimum cadence while actively pedalling, in revolutions/minute. |
| `public float maximumCadence` | Maximum cadence in revolutions/minute. |
| `public float cadenceResponse` | Cadence acceleration/deceleration in RPM per second. |
| `public bool pedalWhileCoasting` | Keep rotating while coasting forward. Otherwise requires forward throttle. |
| `public float Cadence { get; private set; }` | Current crank speed in revolutions per minute. |
| `public float CrankAngle { get; }` | Current crank angle in degrees. |
| `public override bool SupportsProfile(DriveProfile profile)` | Supports wheel-based profiles. |
| `public void ResetVehicleState(VehicleResetReason reason)` | Clears cadence and restores the authored crank/pedal pose. |
| `public override void Configure(VehicleController vehicle)` | Caches wheel geometry and authored crank/pedal rest poses. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances this mechanism through the vehicle physics pipeline. |

## Shared motion playback API

`MovingPartMotion` and `AircraftControlMotionMode` append `Animation` and `Custom` after `Rotation`/`Translation`. `PartMotionPlayback` provides `Request(float)`, `Tick(float)`, `ReportProgress(float)`, `Complete()`, `Stop()`, `Cancel()`, `Dispose()` and normalized `Value`/`Target`/`IsActive`. Its `signals` contains C# events and Inspector UnityEvents; `animation` binds an Animator/clip, and `customDriver` optionally implements `ICustomPartMotion`.

`ICustomPartMotion.BeginMotion(PartMotionPlayback)`, `TickMotion(PartMotionPlayback, float)` and `StopMotion(PartMotionPlayback, PartMotionStopReason)` form the driver contract. Stop reasons are Completed, Stopped and Cancelled. Only Custom dispatches the driver. See the [setup and lifecycle table](../MovingParts.md#choose-how-the-part-moves) and [complete example](../Scripting/MovingParts.md#custom-motion-driver).

## SteeringPart

**Runtime/Exterior/Parts/SteeringPart.cs**

Rotates a rudder, outboard motor or another visible steering pivot from a scalar source, independently of vehicle forces.

**Inherits / implements:** [ExteriorModule](Modules.md#exteriormodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public MonoBehaviour inputSource` | Optional Steering Source or another IInteriorValueSource. Empty uses the vehicle steering command; disabled or invalid sources produce zero. Default `None / unassigned`. |
| `public Vector3 localAxis` | Rotation axis in the part neutral local frame. Default `Vector3.up`. |
| `public float multiplier` | Scales steering travel; zero stops rotation. Default `1`. |
| `public Transform part` | Rudder, outboard motor or other steering pivot. Initial local rotation is neutral. Default `None / unassigned`. |
| `public float response` | Steering response per second; zero follows the source immediately. Default `8`. |
| `public bool reverse` | Reverses visible steering rotation. Default `false`. |
| `public float steeringAngle` | Angle in degrees at full steering before Multiplier and Reverse. Default `30`. |
| `public VehicleController vehicle` | Optional fallback vehicle; finds the parent vehicle when empty. Default `None / unassigned`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController owner)` | Resolves the fallback vehicle when none is assigned. | `owner` — Owning vehicle. |
