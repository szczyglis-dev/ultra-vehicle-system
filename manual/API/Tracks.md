# Tracked movement API

Read [the system explanation](../Scripting/Tracks.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [TrackedProfile](Tracks.md#trackedprofile)
- [TrackPathBuilder](Tracks.md#trackpathbuilder)
- [TrackPathBuilder.LinkOrder](Tracks.md#trackpathbuilderlinkorder)
- [TrackPathBuilder.LinkPosition](Tracks.md#trackpathbuilderlinkposition)
- [Tracks](Tracks.md#tracks)
- [TrackVisuals](Tracks.md#trackvisuals)
- [TrackVisuals.Belt](Tracks.md#trackvisualsbelt)
- [TrackVisuals.Roller](Tracks.md#trackvisualsroller)

## TrackedProfile

**Runtime/Drive/Profiles/TrackedProfile.cs**

Maps tracked propulsion/turning intent into movement behavior.

**Inherits / implements:** [DriveProfile](DriveProfiles.md#driveprofile).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float insideTrackSpeedRatio` | Inside belt target speed relative to the outside belt during a moving turn. |
| `public float lateralGrip` | Lateral tire grip relative to ordinary tires, allowing the road wheels to skid sideways during turns. |
| `public float lateralStability` | Grounded chassis lateral-velocity damping per second. Keeps the hull following its heading while road wheels scrub during turns. Zero disables it. |
| `public float lowSpeedTurnGrip` | Lateral grip during a powered brake-steer launch. Blends to Lateral Grip between 1 and 4 m/s; use the same value to disable the release. |
| `public float maximumLateralStabilityAcceleration` | Maximum lateral stability acceleration in m/s², additionally limited by tire contact load and surface grip. |
| `public float pivotTrackSpeed` | Equal and opposite belt speed during a stationary turn, in m/s at full steering. |
| `public float pivotTransitionTime` | Time in seconds used for pivot transition time. Larger values make this phase/wait last longer. Initial value: `0.3f`. |
| `public bool redistributeSteeringTorque` | Route unused inside-track drive torque to the outside track within the existing engine torque and power limits. |
| `public float steeringBrakeTorque` | Maximum per-wheel braking for inside belt speed regulation; shared service/parking brakes take priority. |
| `public float steeringMix` | Steering strength applied to the configured inside-track speed reduction. |
| `public float trackSpeedResponse` | Response toward track speed response. Higher values follow the requested state faster. Initial value: `2f`. |
| `public float turnSpeedCompensation` | Speed compensation during moving turns: accelerates the outside belt to preserve the mean belt-speed target. Zero uses brake-steer speed loss. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Ensures a Tracks component exists; explicit side membership remains vehicle-owned configuration. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public override float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Resolves engine output and side/pivot demand, then applies bounded tracked propulsion to the configured sides. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public TrackedProfile()` | Constructs `TrackedProfile` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## TrackPathBuilder

**Runtime/Exterior/TrackPathBuilder.cs**

Prepares reusable closed paths during authoring.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform[] explicitLinks` | Additional links, or the complete list when Links Parent is empty. Duplicates are removed. |
| `public virtual Transform[] GeneratedNodes { get; set; }` | Read-only/resolved generated nodes for `TrackPathBuilder`. |
| `public bool leftBelt` | Marks this path as the left track belt; unchecked configures the right belt. Initial value: `true`. |
| `public Transform linksParent` | Collect mesh objects recursively from this parent. Leave empty to use only Explicit Links. |
| `public LinkOrder order` | Selects the order policy for this configuration. Options: `AroundBelt`, `InputOrder`. Initial value: `LinkOrder.AroundBelt`. |
| `public Transform pathParent` | Optional destination. If empty, a dedicated Path object is created beside this builder. |
| `public LinkPosition position` | Selects the position policy for this configuration. Options: `MeshBoundsCenter`, `TransformPivot`. Initial value: `LinkPosition.MeshBoundsCenter`. |
| `public bool reverseOrder` | Reverse the node order and matching links together. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public float travelDirection` | Direction relative to positive wheel rim speed; default matches clockwise ordering in vehicle Y/Z. |
| `public TrackVisuals visuals` | Assign the vehicle's `TrackVisuals`. Automatically found in parents when available. |

## TrackPathBuilder.LinkOrder

**Runtime/Exterior/TrackPathBuilder.cs**

Defines the allowed link order choices used by this topic.

### Values

- `AroundBelt`
- `InputOrder`

## TrackPathBuilder.LinkPosition

**Runtime/Exterior/TrackPathBuilder.cs**

Defines the allowed link position choices used by this topic.

### Values

- `MeshBoundsCenter`
- `TransformPivot`

## Tracks

**Runtime/Drive/Grounded/Tracks.cs**

Owns explicit side membership and tracked support policy.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public WheelCollider[] leftWheels` | Assign the left wheels references used by Tracks. Entries are processed in list order. Initial value: `Array.Empty<WheelCollider>()`. |
| `public virtual float PivotBlend { get; protected set; }` | Read-only/resolved pivot blend for Tracks. |
| `public WheelCollider[] rightWheels` | Assign the right wheels references used by Tracks. Entries are processed in list order. Initial value: `Array.Empty<WheelCollider>()`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Clears retained pivot state/blend before tracked movement resumes. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual int SideOf(WheelCollider wheel)` | Resolves a native wheel's left/right tracked-side membership. | `wheel` — Native wheel or wheel adapter being configured/queried. **Returns:** Computed int in the operation's documented unit/domain. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Applies supported load/grip-limited lateral/pivot stabilization for an active tracked profile. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## TrackVisuals

**Runtime/Exterior/TrackVisuals.cs**

Moves visible links and rollers from wheel motion.

**Inherits / implements:** [ExteriorModule](Modules.md#exteriormodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Belt leftBelt` | Configuration for left belt. Expand this field; its settings are described under TrackVisuals.Belt. Initial value: `new Belt()`. |
| `public virtual float LeftSpeed { get; protected set; }` | Read-only/resolved left speed for `TrackVisuals`. |
| `public Belt rightBelt` | Configuration for right belt. Expand this field; its settings are described under TrackVisuals.Belt. Initial value: `new Belt()`. |
| `public virtual float RightSpeed { get; protected set; }` | Read-only/resolved right speed for `TrackVisuals`. |
| `public Roller[] rollers` | Ordered rollers configuration entries. Expand each item; see TrackVisuals.Roller for its individual settings. Initial value: `Array.Empty<Roller>()`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void AdvanceVisuals(float deltaTime)` | Advances belt-link and roller presentation from the configured wheel motion. | `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override void Configure(VehicleController owner)` | Caches vehicle/Tracks and prepares left/right belt paths and retained link poses. | `owner` — Unity/application owner whose identity controls this relationship or resource. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual bool TryGetPathPoint(Belt belt, int index, out Vector3 position)` | Reads an interpolated point/orientation on a prepared belt path without advancing belt travel. | `belt` — Track side/path to query. `index` — Zero-based configured-entry index; use the owner's current list ordering. `position` — Requested point or switch detent; see its declared type and owning operation. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## TrackVisuals.Belt

**Runtime/Exterior/TrackVisuals.cs**

Configuration/implementation type for belt within tracked movement.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform[] links` | Assign the links references used by TrackVisuals.Belt. Entries are processed in list order. Initial value: `Array.Empty<Transform>()`. |
| `public Transform[] path` | Assign the path references used by TrackVisuals.Belt. Entries are processed in list order. Initial value: `Array.Empty<Transform>()`. |
| `public float Travel { get; }` | Read-only/resolved travel for Belt. |
| `public float travelDirection` | Path travel direction relative to positive wheel rim speed. |



| Declaration | Usage |
| --- | --- |
| `public bool reverse` | Reverse belt travel along its authored path. |

## TrackVisuals.Roller

**Runtime/Exterior/TrackVisuals.cs**

Configuration/implementation type for roller within tracked movement.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool left` | Uses the left belt speed rather than the right when rotating this visible roller. |
| `public Vector3 localAxis` | Local axis around which the configured motion or operation takes place. Initial value: `Vector3.right`. |
| `public float radius` | Physical radius in metres; use half the outside diameter of the represented shape. Initial value: `.5f`. |
| `public Transform transform` | Assign the transform reference used by TrackVisuals.Roller. Leave unassigned only when this feature is optional or the component can resolve it automatically. |


| Declaration | Usage |
| --- | --- |
| `public bool reverse` | Reverse the visible roller spin. |
