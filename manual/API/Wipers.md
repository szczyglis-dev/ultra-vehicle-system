# Exterior wipers API

Read [the system explanation](../Scripting/MovingParts.md#wipers) for ownership and extension contracts.

## Types

- [Wiper](Wipers.md#wiper)
- [WiperBlade](Wipers.md#wiperblade)
- [Wipers](Wipers.md#wipers)
- [WiperSwitchBinding](Wipers.md#wiperswitchbinding)
- [WiperType](Wipers.md#wipertype)

## Wiper

**Runtime/Exterior/Wipers/Wipers.cs**

Configuration/implementation type for wiper within exterior wipers.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform anchor` | Assign the anchor reference used by Wiper. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 anchorLocalPosition` | Blade position expressed relative to the optional anchor, in metres. |
| `public Transform blade` | Assign the blade reference used by Wiper. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float CurrentPhase { get; }` | Current independent cycle phase from zero to less than one; the outer end of travel is phase 0.5. |
| `public float cyclesPerMinute` | Complete out-and-back cycles per minute. On an entry, used when independentSettings is enabled; zero pauses motion. |
| `public WiperBlade helper` | Assign the helper WiperBlade component/asset used by Wiper. |
| `public string id` | Unique, nonblank, case-sensitive ID within the owning list. Duplicate authored IDs cannot be addressed individually. |
| `public bool independentSettings` | Uses this entry's authored running state and cyclesPerMinute instead of shared defaults. Individual runtime API overrides also work when this flag is false. |
| `public bool IsParked { get; }` | True at phase zero, when the blade is at its parked pose. |
| `public Vector3 localAxis` | Local axis around which the configured motion or operation takes place. Initial value: `Vector3.forward`. |
| `public float parkedAngle` | Parked angle in degrees, relative to the owning mechanism's reference frame. |
| `public bool reverse` | Reverses the authored sweep direction for this wiper. |
| `public bool running` | Running request when independentSettings is enabled. |
| `public float sweepAngle` | Sweep angle in degrees, relative to the owning mechanism's reference frame. Initial value: `75`. |
| `public WiperType type` | Selects the mechanism/visual variant used by this configuration. Options: `Front`, `Rear`, `Custom`. |

## WiperBlade

**Runtime/Exterior/Wipers/WiperBlade.cs**

Maps normalized stroke to authored blade geometry.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual float Angle { get; }` | Read-only/resolved angle for `WiperBlade`. |
| `public float maximumAngle` | Upper rotation angle in degrees for the configured motion. Initial value: `65`. |
| `public float minimumAngle` | Lower rotation angle in degrees for the configured motion. |
| `public AnchoredRotation motion` | Anchor, axes and range describing the visible control's motion. Initial value: `new AnchoredRotation { localAxis = Vector3.forward }`. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public WiperType type` | Selects the mechanism/visual variant used by this configuration. Options: `Front`, `Rear`, `Custom`. |
| `public virtual float Value { get; protected set; }` | Current value in this control's domain; use the declaring control's detailed value contract. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void CaptureRestPose()` | Captures the currently authored rest pose for this geometry mapper or blade. | No arguments; no returned value. |
| `public virtual void ParkImmediate()` | Places the blade at its parked pose without waiting for a wiper cycle. | No arguments; no returned value. |
| `public virtual void SetValue(float value)` | Applies normalized blade stroke using the captured spindle/rest geometry; it does not run a wiper clock. | `value` — Requested state/value in this operation's domain; use its configured range/unit. |

## Wipers

**Runtime/Exterior/Wipers/Wipers.cs**

Owns wiper cycle timing, running state and blade dispatch.

**Inherits / implements:** [ExteriorModule](Modules.md#exteriormodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action AudioStopped` | Requests stopping wiper audio. |
| `public event Action Parked` | When wipers reach their parked state. No payload. |
| `public event Action<bool> RunningChanged` | When the wiper running request changes. Payload: bool; a stop can still finish the current cycle. |
| `public event Action<float> SpeedChanged` | After `SetSpeed` changes requested wiper speed. Payload: configured cycle-speed value; zero pauses motion. |
| `public event Action<Wiper, bool, float> StrokeAudioRequested` | Specific wiper, stroke direction and resolved cycles per minute for optional audio. |
| `public event Action StrokeBatchStarted` | Begins a mechanism tick; receivers can deduplicate shared voices within this batch. |
| `public event Action<bool> StrokeStarted` | When a wiper stroke starts. Payload: returning bool, `true` for the return stroke and `false` for the outward stroke. |
| `public event Action<string> WiperParked` | When an entry reaches/is immediately placed at its parked pose; payload is its ID. |
| `public event Action<Wiper> WiperRemoved` | Reports an entry removed from the mechanism so optional receivers can release its resources. |
| `public event Action<string, bool> WiperRunningChanged` | After an API changes an entry's effective running request; payload is its ID and new bool request. |
| `public event Action<string, float> WiperSpeedChanged` | After an API changes an entry's effective speed; payload is its ID and cycles per minute. |
| `public event Action<string, bool> WiperStrokeStarted` | Reports entry ID and stroke direction: false for outward, true for return. Entries have independent phase clocks. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public float cyclesPerMinute` | Default complete outward-and-return wiper cycles per minute. Initial value: `45`. |
| `public virtual bool IsParked { get; }` | True when every entry is at its parked pose. |
| `public virtual bool IsRunning { get; }` | True when any entry is requested running; with an empty list, reports the shared default request. |
| `public List<Wiper> wipers` | Ordered wipers configuration entries. Expand each item; see Wiper for its individual settings. Initial value: `new List<Wiper>()`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void CaptureRestPoses()` | Captures rest poses for the wiper geometry owned by the module. | No arguments; no returned value. |
| `public override void Configure(VehicleController vehicle)` | Applies current blade pose only during Play Mode so Edit Mode configuration does not recapture an animated neutral pose. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual float GetSpeed(string id)` | Reports the identified entry's effective cycles per minute. Returns zero for an unresolved ID. | — |
| `public virtual Wiper GetWiper(string id)` | Finds a blade entry by exact ID. Returns null for blank, missing or ambiguous duplicate IDs. | — |
| `public virtual bool IsWiperRunning(string id)` | Reports the identified entry's effective request, including runtime overrides. False for an unresolved ID; a stopped blade can still be finishing its cycle. | — |
| `public virtual bool Park(string id)` | Stops and immediately parks one entry without completing its cycle; returns false for an unresolved ID. | — |
| `public virtual void ParkAll()` | Stops every entry and immediately parks all blades and stops their stroke audio. | — |
| `public virtual bool RegisterWiper(Wiper wiper)` | Adds an entry with a unique, nonblank ID. Returns false for null, duplicate IDs, duplicate entries or reused helper/blade references. | — |
| `public virtual bool RestoreWiperControl(string id)` | Clears one entry's runtime running/speed overrides, returning it to its current independent authored settings or shared defaults. Returns false for unresolved IDs. | — |
| `public virtual void SetRunning(bool value)` | Requests the wiper running state; stopping finishes the current cycle before parking. | `value` — Requested bool state for this operation. |
| `public virtual bool SetRunning(string id, bool value)` | The bool-only overload sets every entry's request and clears per-entry running overrides. The ID overload changes only that entry and returns false for an unresolved ID. Stopping finishes the current cycle. | — |
| `public virtual void SetSpeed(float speed)` | Changes wiper cycle speed; zero pauses cycle motion. | `speed` — Speed, interpreted by this operation in the declared type. |
| `public virtual bool SetSpeed(string id, float speed)` | The float-only overload applies the rate to every entry and clears individual speed overrides. The ID overload changes only one rate. Rates are clamped to zero or greater; non-finite values are rejected. ID overload returns false on rejection. | — |
| `public virtual void Tick(float deltaTime)` | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void Toggle()` | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component. | No arguments; no returned value. |
| `public virtual bool Toggle(string id)` | The no-argument overload stops all entries if any is requested running, otherwise starts all. The ID overload toggles one entry and returns false for an unresolved ID. | — |
| `public virtual bool UnregisterWiper(string id)` | Immediately parks and removes the identified entry and releases its generated audio source. User-provided audio sources are retained. Returns false for unresolved IDs. | — |

## WiperSwitchBinding

**Runtime/Exterior/Wipers/WiperSwitchBinding.cs**

Configuration/implementation type for wiper switch binding within exterior wipers.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool onMeansRunning` | Maps the switch On position to running wipers; unchecked reverses that mapping. Initial value: `true`. |
| `public SwitchAnimator switchAnimator` | Assign the switch handle SwitchHandle component/asset used by WiperSwitchBinding. |
| `public Wipers wipers` | Assign the wipers Wipers component/asset used by WiperSwitchBinding. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Synchronize(bool immediate)` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request. | `immediate` — Whether to bypass normal presentation travel. |
| `public virtual void Tick(float deltaTime)` | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## WiperType

**Runtime/Exterior/Wipers/Wipers.cs**

Defines the allowed wiper type choices used by this topic.

### Values

- `Front`
- `Rear`
- `Custom`
