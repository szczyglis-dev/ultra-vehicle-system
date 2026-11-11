# Body operation and damage API

Read [the system explanation](../Scripting/Damage.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [Body](#body)
- [Damage](#damage)
- [DamageCollisionRelay](#damagecollisionrelay)
- [DamageHit](#damagehit)
- [DamageImpactMetric](#damageimpactmetric)
- [DamageImpactProfile](#damageimpactprofile)
- [DamagePart](#damagepart)
- [DamagePoolOverflow](#damagepooloverflow)
- [ICollisionDamageResponse](#icollisiondamageresponse)
- [IDamageImpactEffect](#idamageimpacteffect)
- [PartMaterial](#partmaterial)
- [PartType](#parttype)
- [VehicleBodyPart](#vehiclebodypart)
- [VehicleMeshDeformation](#vehiclemeshdeformation)
- [WheelPart](#wheelpart)

## Body

**Runtime/Exterior/Parts/Body.cs**

Finds and operates authored `VehicleBodyPart` entries.

**Inherits / implements:** [ExteriorModule](Modules.md#exteriormodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public DamagePart[] damageParts` | Additional damage boundaries (DamagePart or WheelPart). Damage.RefreshParts merges these with its own parts; separate from opening Body.parts. |
| `public VehicleBodyPart[] parts` | Ordered parts configuration entries. Expand each item; see VehicleBodyPart for its individual settings. Initial value: `Array.Empty<VehicleBodyPart>()`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool Close(string id)` | Requests closure of this part or the body part selected by ID. | `id` — Case-sensitive authored body-part identifier. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual void CloseAll()` | Requests closure of every eligible authored body part. | No arguments; no returned value. |
| `public virtual VehicleBodyPart GetPart(string id)` | Finds the authored body part by its case-sensitive ID. | `id` — Case-sensitive authored body-part identifier. **Returns:** Returned `VehicleBodyPart`; ownership remains as specified by the creating/lookup operation. |
| `public virtual bool Open(string id)` | Requests opening of this part or the body part selected by ID. | `id` — Case-sensitive authored body-part identifier. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual void OpenAll()` | Requests opening of every eligible authored body part. | No arguments; no returned value. |
| `public virtual bool SetOpen(string id, bool open)` | Requests a body part's open/closed target. | `id` — Case-sensitive authored body-part identifier. `open` — Requested open state. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool SetPhysics(string id, bool enabled)` | Looks up the case-sensitive part ID and requests that part's physics policy, returning `false` when no eligible target exists. | `id` — Case-sensitive authored body-part identifier. `enabled` — Requested enable flag. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool Toggle(string id)` | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component. | `id` — Case-sensitive authored body-part identifier. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |

## Damage

**Runtime/Physics/Damage/Damage.cs**

**Inherits / implements:** [PhysicsModule](Modules.md#physicsmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<DamageHit, float> DeformationRequested` | Accepted hit and radius before part detachment; optional deformation receivers process it synchronously. |
| `public event Action EffectsCleared` | Requests clearing optional impact presentation. |
| `public event Action FullyRepaired` | After the full-repair pass and managed effect cleanup. This is a pass-completion event, not proof that destroyed/unrecoverable objects were recreated. |
| `public event Action<DamageHit> Hit` | When a damage hit is accepted. Payload: `DamageHit`; mesh upload can occur later in `LateUpdate`. |
| `public event Action PartsChanged` | Reports that the damage boundary list has been refreshed. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool damageEnabled` | Enables damage behavior for this system. Initial value: `true`. |
| `public float damageMultiplier` | Multiplier/fraction controlling damage multiplier. Increasing it increases this contribution relative to the unscaled value. Initial value: `1`. |
| `public bool deformationEnabled` | Enables deformation behavior for this system. Initial value: `true`. |
| `public bool detachmentEnabled` | Enables detachment behavior for this system. Initial value: `true`. |
| `public float impactRadius` | Impact radius in metres in the owning system's space. Initial value: `.9f`. |
| `public float minimumImpactSpeed` | Minimum relative collision speed in m/s required for collision-driven damage. Initial value: `3`. |
| `public DamagePart[] parts` | Ordered parts configuration entries. Expand each item; see DamagePart for its individual settings. Initial value: `Array.Empty<DamagePart>()`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount)` | Submits a scripted impact to the damage system, subject to its enabled damage policy. | — |
| `public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount, float impactSpeed, float impulse, float force)` | Applies gameplay damage with physical metadata: speed in m/s, impulse in N·s and average force in N. | — |
| `public virtual void ClearEffects()` | Returns all active visual leases and clears their cooldowns. | — |
| `public override void Configure(VehicleController vehicle)` | Binds collision/impact processing to the supplied vehicle. | — |
| `public virtual DamagePart GetPart(string id)` | Returns one registered case-sensitive Part Id. Blank, missing or duplicate IDs return null. | — |
| `public virtual void ReceiveImpact(Impact impact)` | Processes a copied impact snapshot through vehicle damage policy. | — |
| `public virtual void RefreshParts()` | Merges and deduplicates current Parts, owned Body.damageParts and owned WheelPart children; captures repair state/ownership and retains detached references. Call after runtime authoring changes. Does not discover every unregistered ordinary DamagePart automatically. | — |
| `public virtual void RepairAll()` | Repairs retained registered parts and prepared dents, clears managed impact effects, then emits FullyRepaired. Missing/destroyed objects are not recreated; individual failures require application reconstruction. | — |
| `public virtual bool RepairPart(DamagePart part)` | Repairs one registered retained part by unique ID or reference through RepairFully; returns false when missing, unregistered, ambiguous or not recoverable. Independent of future damage/detachment switches. | — |
| `public virtual bool RepairPart(string id)` | Repairs one registered retained part by unique ID or reference through RepairFully; returns false when missing, unregistered, ambiguous or not recoverable. Independent of future damage/detachment switches. | — |

## DamageCollisionRelay

**Runtime/Physics/Damage/DamageCollisionRelay.cs**

Relays relevant native collisions into damage handling.

**Inherits / implements:** `MonoBehaviour`.

## DamageHit

**Runtime/Physics/Damage/Damage.cs**

### State and configuration

| Member | Meaning |
| --- | --- |
| `public readonly float Amount` | Read-only amount stored by this snapshot/data object. |
| `public readonly Vector3 Direction` | Point: copied world-space contact or impact position; Direction: world-space direction in which the hit deforms or pushes the part. |
| `public readonly float Force` | Estimated average force in N, calculated as collision impulse divided by fixed timestep; zero when unavailable. |
| `public readonly bool HasPhysicalImpact` | True when finite, nonnegative speed, impulse and force metadata were supplied. |
| `public readonly bool HasTelemetry` | True when a telemetry snapshot was supplied; Damage supplies its vehicle’s latest completed snapshot. |
| `public readonly float ImpactSpeed` | Physical collision speed into the surface in m/s; zero when unavailable. |
| `public readonly float Impulse` | Collision impulse magnitude in N·s; zero when unavailable. |
| `public readonly DamagePart Part` | Damage boundary selected for this copied hit. |
| `public readonly Vector3 Point` | Point: copied world-space contact or impact position; Direction: world-space direction in which the hit deforms or pushes the part. |
| `public readonly Telemetry Telemetry` | Latest completed vehicle telemetry snapshot. Check HasTelemetry; contact-time measurements remain in the impact fields. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public DamageHit(DamagePart part, Vector3 point, Vector3 direction, float amount, float impactSpeed, float impulse, float force, Telemetry? telemetry = null)` | Initializes the hit; physical overload values use m/s, N·s and N. | — |
| `public DamageHit(DamagePart part, Vector3 point, Vector3 direction, float amount, Telemetry? telemetry = null)` | Constructs `DamageHit` with the supplied initial state. | — |

## DamageImpactMetric

**Runtime/Effects/Damage/Profiles/DamageImpactProfile.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

Values: `DamageAmount`, `ImpactSpeed`, `Impulse`, `Force`.

## DamageImpactProfile

**Runtime/Effects/Damage/Profiles/DamageImpactProfile.cs**

Scripted impact matching, normalized metric evaluation, shared Sound bank and optional custom visual effect.

| Declaration | Meaning |
| --- | --- |
| `public bool responseEnabled` | Disable this response without removing its material mapping. |
| `public PartMaterial material` | Built-in part material matched when Material Id is empty. |
| `public string materialId` | Optional case-sensitive custom material key, matched against DamagePart.materialId. Overrides enum matching. |
| `public DamageImpactMetric metric` | Input units for thresholds: damage units, m/s, N s or N. Physical metrics require physical impact data. |
| `public float minimumImpact` | Lowest accepted input in the selected metric's units. |
| `public float maximumImpact` | Input mapped to full response. Higher inputs clamp unless Ignore Above Maximum is enabled. |
| `public bool ignoreAboveMaximum` | Reject inputs above Maximum Impact instead of clamping them. |
| `public float cooldown` | Seconds between custom visual effects. The Sound bank owns its audio cooldown. |
| `public DamageSoundBank sound` | Shared Single/StrengthGroups audio response. Input strength comes from the normalized profile metric. |
| `public GameObject effectPrefab` | Pooled prefab, such as particles, a light burst or custom IDamageImpactEffect behavior. No prefab is instantiated per hit. |
| `public int effectPoolSize` | Instances to prewarm for this profile, subject to Damage's total instance budget. Zero disables visuals. |
| `public float effectLifetime` | Maximum effect lease in seconds before returning to the pool. Include child/sub-emitter lifetime. |
| `public Vector2 effectScaleRange` | Uniform effect-scale endpoints mapped from normalized impact. Multiplies the prefab's original scale. |
| `public bool alignToImpact` | Orient local +Z opposite the deformation direction. Rotation Offset is applied afterward. |
| `public Vector3 effectRotationOffset` | Additional prefab orientation in degrees relative to the impact frame. |
| `public float surfaceOffset` | Move the effect outward from the hit point, opposite the deformation direction, in metres. |
| `public virtual bool Matches(DamagePart part)` | Checks whether this enabled profile matches the part material or custom key. | — |
| `public virtual bool TryEvaluate(DamageHit hit, out float intensity)` | Validates thresholds and available metadata; returns accepted status and normalized intensity. | — |

## DamagePart

**Runtime/Exterior/Parts/DamagePart.cs**

**Inherits / implements:** `MonoBehaviour`.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<DamagePart, float> Damaged` | After the part accepts damage. Payload: `DamagePart` and accepted amount. |
| `public event Action<DamagePart> Detached` | After a damage part detaches. Payload: that `DamagePart`. |
| `public event Action<DamagePart, float> Repaired` | After damage is actually removed. Payload: `DamagePart` and repaired amount. |
| `public event Action<DamagePart> Restored` | After a successful full repair, with remount/state/mesh restoration applied; wheel Attached has already been updated. Incremental Repair(amount) does not emit it. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual float Damage { get; protected set; }` | Read-only/resolved damage for `DamagePart`. |
| `public bool damageEnabled` | Default true. Gates routed hits and direct ReceiveDamage; does not repair previous damage or prevent explicit Detach. |
| `public float debrisAngularDamping` | Angular drag applied to the debris Rigidbody after release. Default 0.5; does not replace inherited angular velocity. |
| `public float debrisColliderMinimumThickness` | Minimum world-space thickness in metres for an automatically generated debris collider. Default: `.03f`. |
| `public float debrisContactAngularChange` | Additional angular speed allowance in degrees/s for moving-object contact impulses and the combined post-solver spin budget. Default: `180`. |
| `public float debrisContactSpeedChange` | Additional linear speed allowance in m/s for moving-object contacts and the combined post-solver contact budget. Stationary ground retains full support and stopping forces. Default: `4`. |
| `public float debrisDepenetrationSpeed` | Maximum overlap-recovery velocity in m/s after release. Default 2; does not clamp release velocity or ordinary impact response. |
| `public float debrisGroundPenetrationTolerance` | Ground overlap in metres tolerated before correcting a crushed part. Default: `.01f`. |
| `public bool debrisGroundProjection` | Correct deep solver penetration into stationary ground after a heavy vehicle crushes a thin part. Operates only at real ground contacts; free flight remains physical. Default: `true`. |
| `public float debrisGroundProjectionLimit` | Maximum ground penetration correction in metres per contact callback. Default: `.3f`. |
| `public float debrisMaximumAngularSpeed` | Native released-part angular speed limit in degrees/s with contact stabilization enabled. Detached Wheel Parts can raise this to preserve inherited tire RPM. Default: `720`. |
| `public int debrisSolverIterations` | Native position solver iterations on released debris. More iterations improve thin-panel support under a heavy vehicle. Default: `12`. |
| `public float debrisSurfaceSpeedMultiplier` | Multiplier of the impacting surface world speed used by the debris contact speed budget. Faster pre-solver debris motion is preserved; the contact speed-change allowance is added. Default: `1.25f`. |
| `public int debrisVelocitySolverIterations` | Native velocity solver iterations on released debris. Default: `4`. |
| `public MeshFilter[] deformableMeshes` | Readable MeshFilter meshes deformed by impacts on this damage part; assign only meshes that should visibly dent. Initial value: `Array.Empty<MeshFilter>()`. |
| `public float deformationMultiplier` | Zero disables mesh dents. Does not affect detachment. |
| `public Collider[] detachedVehicleColliders` | Solid chassis-owned shapes enabled on detachment, outside detachable groups. Author disabled and assign each to one part before startup. Full repair restores captured enabled states; nested parent release also activates them. Invalid/trigger/wheel/foreign/debris references are skipped. Empty disables this feature. Initial value: `Array.Empty<Collider>()`. |
| `public float detachmentMultiplier` | Zero prevents collision detachment. |
| `public float detachThreshold` | Accumulated damage required to detach this group. |
| `public bool excludeDebrisFromWheelSupport` | Keep detached panels out of native wheel suspension support. Solid tire and chassis colliders still push the debris, without firing full wheel spring forces into a light panel. Default: `true`. |
| `public bool generateMissingDebrisCollider` | Generate a simple box from this part's mesh bounds on release if its damage boundary has no solid collider. Prevents detached lamps/glass from falling through the world. Authored colliders are retained. Default: `true`. |
| `public virtual bool IsDetached { get; protected set; }` | Current is detached predicate; read it instead of maintaining a second application flag. |
| `public float mass` | Physical mass in kilograms. Increasing it increases the inertia and the load carried by connected supports. Initial value: `15`. |
| `public PartMaterial material` | Selects the material policy for this configuration. Options: `Metal`, `Glass`, `Plastic`, `Rubber`, `Mechanical`. Initial value: `PartMaterial.Metal`. |
| `public string materialId` | Optional case-sensitive impact material key, e.g. carbon or wood. Matching custom profiles take priority over the enum response. |
| `public string partId` | Stable identifier for scripts and damage reactions. |
| `public bool prewarmDebrisPhysics` | Prepare the disabled debris contact helper and shared contact code during startup, reducing first-detachment allocation/JIT work. Does not create a Rigidbody or change attached collision geometry. Default: `true`. |
| `public float releasedCollisionDelay` | Minimum seconds to ignore former vehicle collisions after release. Overlapping pairs wait until separated. |
| `public bool stabilizeDebrisContacts` | Limit solver contact impulses on released parts, preventing thin panels trapped under heavy vehicles from being explosively ejected. Does not clamp inherited release velocity. Default: `true`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool Detach(Rigidbody vehicleBody)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | — |
| `public virtual void ReceiveDamage(float amount)` | Applies an accepted damage amount to this damage part and evaluates its detachment threshold. | — |
| `public virtual float Repair(float amount)` | Removes up to the requested nonnegative damage amount and returns the actual repaired amount. Does not reattach a detached part. | — |
| `public virtual bool RepairFully()` | Fully repairs retained objects: restores the saved attachment pose when detached, clears damage/exclusions, restores original Rigidbody settings, resets owned VehicleBodyPart hinges and prepared part meshes. Returns false if a detached part lost its captured parent. Runtime debris Rigidbody removal is deferred and cancelled by another immediate detach. Does not clear independent child damage accumulators. | — |


## DamagePoolOverflow

**Runtime/Effects/Damage/Profiles/DamageImpactProfile.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

Values: `Skip`, `ReplaceOldest`.

## ICollisionDamageResponse

**Runtime/Physics/Damage/ICollisionDamageResponse.cs**

Lets a target alter collision damage severity.

### State and configuration

| Member | Meaning |
| --- | --- |
| `float CollisionDamageScale { get; }` | Read-only/resolved collision damage scale for `ICollisionDamageResponse`. |

## IDamageImpactEffect

**Runtime/Effects/Damage/Profiles/DamageImpactProfile.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `void PlayImpact(DamageHit hit, float intensity)` | Initializes a leased effect using hit metadata and normalized intensity. | — |
| `void StopImpact()` | Resets a pooled effect before return or replacement. | — |

## PartMaterial

**Runtime/Exterior/Parts/DamagePart.cs**

Values: `Metal`, `Glass`, `Plastic`, `Rubber`, `Mechanical`, `Custom`.

## PartType

**Runtime/Exterior/Parts/VehicleBodyPart.cs**

Defines the allowed part type choices used by this topic.

### Values

- `Door`
- `Hood`
- `Trunk`
- `Tailgate`
- `Other`

## VehicleBodyPart

**Runtime/Exterior/Parts/VehicleBodyPart.cs**

Defines a named opening/moving body element.

**Inherits / implements:** `MonoBehaviour`, [IPartMotionSource](MovingParts.md#ipartmotionsource).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action ClosingCompleted` | Once after the actual pose reaches the requested closing target. No payload. |
| `public event System.Action ClosingStarted` | Once before a closing operation moves the pose. No payload. |
| `public event System.Action MotionAudioStopped` | Requests stopping movement audio after interruption or disable. |
| `public event System.Action<PartMotionEvent> MotionOccurred` | Reports an admitted movement phase to optional presentation receivers. |
| `public event System.Action<bool> OpenChanged` | When the part's requested open state changes. Payload: bool; this is not a generic arrival event. |
| `public event System.Action OpeningCompleted` | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
| `public event System.Action OpeningStarted` | Once before an opening operation moves the pose. No payload; interruptions never imply completion. |
| `public event System.Action<bool> PhysicsChanged` | When the part's `usePhysics` policy changes. Payload: bool. |
| `public event System.Action Released` | After the body part is released from vehicle-owned motion. No payload. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform AudioEmitter { get; }` | Transform used as the emitter for movement presentation. |
| `public AnimationCurve closingMotionCurve` | Normalized elapsed time to closing progress, independently of opening. Speed determines average commanded degrees per second. Default: linear time-to-progress curve. |
| `public float completionTolerance` | Actual hinge angle tolerance in degrees for completion, default 1. Applies to animated and physical VehicleBodyPart. |
| `public virtual float CurrentAngle { get; }` | Read-only/resolved current angle for `VehicleBodyPart`. |
| `public float damper` | Damping strength opposing motion; larger values reduce oscillation but can slow the response. Initial value: `50`. |
| `public Vector3 hingeAnchor` | Hinge position in this transform's local mesh coordinates. Zero uses its origin. |
| `public Vector3 hingeAxis` | Direction vector defining hinge axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: `Vector3.up`. |
| `public virtual bool IsClosing { get; }` | An accepted closing operation is pending; false after completion or cancellation. |
| `public virtual bool IsImpactUnlatched { get; protected set; }` | Whether an impact has released the latch. Separate from the requested IsOpen state and physical detachment. |
| `public virtual bool IsOpen { get; }` | Current is open predicate; read it instead of maintaining a second application flag. |
| `public virtual bool IsOpening { get; }` | An accepted opening operation is pending; false after completion or cancellation. |
| `public virtual bool IsReleased { get; protected set; }` | Current is released predicate; read it instead of maintaining a second application flag. |
| `public virtual HingeJoint Joint { get; }` | Read-only/resolved joint for `VehicleBodyPart`. |
| `public float mass` | Physical mass in kilograms. Increasing it increases the inertia and the load carried by connected supports. Initial value: `15`. |
| `public float minimumUnlatchForce` | Minimum average impact force in N, computed from impulse / fixed timestep. Default 4000. |
| `public float minimumUnlatchSpeed` | Minimum speed along the contact normal in m/s. Default 1. |
| `public PartMotionEvents motionEvents` | Inspector UnityEvent callbacks for the same four operation notifications; also accessible through GetEvent. |
| `public float openAngle` | Open angle in degrees, relative to the owning mechanism's reference frame. Initial value: `70`. |
| `public AnimationCurve openingMotionCurve` | Normalized elapsed time to opening progress. Linear gives constant commanded speed; flatten the end to slow before fully open. Physical hinges follow this spring target under load. Default: linear time-to-progress curve. |
| `public string partId` | Text identifier/name for part id. Keep it consistent with the referenced animation, profile or application setting. |
| `public PartType partType` | Selects the part type policy for this configuration. Options: `Door`, `Hood`, `Trunk`, `Tailgate`, `Other`. |
| `public bool permanentImpactUnlatch` | Keep an impact-unlatched part loose until Close or SetOpen(false) is called. Default false. |
| `public float releasedCollisionDelay` | Minimum seconds to ignore former vehicle collisions after release. Overlapping pairs wait until separated. |
| `public float speed` | Average commanded angular speed in degrees per second. Opening/closing curves shape travel; physical hinges follow the moving spring target under load. Initial value: `100`. |
| `public float spring` | Spring stiffness. Larger values produce a stronger restoring force for the same displacement. Initial value: `300`. |
| `public float temporaryUnlatchDelay` | Minimum time before temporary release can relatch near closed position. Default 0.25 s. |
| `public float unlatchedDamperMultiplier` | Hinge damping scale while impact-unlatched; 0..1, default 1. |
| `public float unlatchedSpringMultiplier` | Closing spring scale while impact-unlatched; 0..1, default 1. Zero permits free swinging. |
| `public bool unlatchOnImpact` | Allow physical impacts to release the closed latch. Default true. Both thresholds must pass. |
| `public bool usePhysics` | Uses a physical hinge instead of directly animating the part transform. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Close()` | Requests closure of this part or the body part selected by ID. | No arguments; no returned value. |
| `public virtual void Open()` | Requests opening of this part or the body part selected by ID. | No arguments; no returned value. |
| `public virtual void RefreshIgnoredCollisions()` | Refreshes collision pairs for a body part after ownership/geometry changes. | No arguments; no returned value. |
| `public virtual void Release()` | Releases this part or hand pose through its declaring type's ownership boundary. | No arguments; no returned value. |
| `public virtual void RepairFully()` | Closes the retained panel, clears release/unlatch/motion state, restores its captured closed pose and rebuilds the physical hinge if enabled. Does not recreate a destroyed panel or clear a separate DamagePart accumulator. | — |
| `public virtual void SetOpen(bool value)` | Requests a body part's open/closed target. | `value` — Requested bool state for this operation. |
| `public virtual void SetPhysics(bool value)` | Changes `usePhysics` for an unreleased part and emits `PhysicsChanged` only on an actual policy change; released parts ignore it. | `value` — Requested bool state for this operation. |
| `public virtual void Toggle()` | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component. | No arguments; no returned value. |
| `public virtual bool TryUnlatchFromImpact(float force, float speed)` | Apply the same configured latch policy from a custom impact system. Returns false for disabled, animated, already-open/released/unlatched parts or rejected thresholds. | `force` — finite average force in N. `speed` — finite normal impact speed in m/s. Returns true only for a newly released latch. |



| Declaration | Usage |
| --- | --- |
| `public bool reverse` | Mirror motion around the neutral pose without changing input or travel limits. |
| `public float EffectiveOpenAngle { get; }` | Resolved door-open target including the authored reverse direction. |

## VehicleMeshDeformation

**Runtime/Physics/Damage/VehicleMeshDeformation.cs**

Owns readable mesh instances, dent buffers and geometry restoration.

**Inherits / implements:** [PhysicsModule](Modules.md#physicsmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action DeformationChanged` | After pending deformation geometry is uploaded. No payload; inspect owned geometry at this boundary. |
| `public event System.Action Restored` | After deformable shape is restored to rest geometry. No payload. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Damage damage` | Assign the damage Damage component/asset used by DamageAudio. |
| `public float dentPerDamage` | Visual displacement per accepted damage unit, in metres. |
| `public float maximumDent` | Largest total vertex displacement from its rest pose, in metres. |
| `public int meshUploadIntervalFrames` | Rendered LateUpdate calls with pending dents before uploading changed meshes. Higher values batch more impacts and normal rebuilds, but dents and DeformationChanged appear later. Damage calculation still runs for every hit. Default 1. |
| `public bool recalculateNormals` | Rebuild lighting normals when uploading dents. Disable to reduce mesh rebuild cost while retaining existing normals; deformed lighting becomes less accurate. Bounds are always updated. Default enabled. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController owner)` | Stores the vehicle whose hover transition geometry should be displayed. | `owner` — Unity/application owner whose identity controls this relationship or resource. |
| `public virtual void Deform(DamageHit hit, float radius, float dentPerDamage, float maximumDent)` | Queues a bounded dent in readable mesh geometry around a supplied local impact point. | `hit` — Hit, interpreted by this operation in the declared type. `radius` — Geometry influence/tube radius in the declared units. `dentPerDamage` — Dent displacement scale per accepted damage amount. `maximumDent` — Maximum displacement relative to rest geometry. |
| `public virtual void FlushPendingDeformation()` | Immediately uploads pending vertex changes and publishes DeformationChanged, bypassing the batching delay. No-op when nothing is pending. | — |
| `public virtual void RestoreShape()` | Restores owned deformable meshes to their captured rest geometry. | No arguments; no returned value. |
| `public virtual void RestoreShape(DamagePart part)` | The DamagePart overload restores its configured prepared meshes only, clears dent buffers and flushes the upload. Other part dents remain. Restored emits if at least one prepared shape was restored. | — |

## WheelPart

**Runtime/Exterior/Parts/WheelPart.cs**

Inherits [DamagePart](Damage.md#damagepart). Add to the visual wheel root. See [setup and repair tutorials](../Damage.md#detachable-wheels).

**Inherits / implements:** [DamagePart](Damage.md#damagepart).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool Attached { get; }` | True while this part is not detached and its linked Wheel is attached. Prefer this or Wheel.Attached to a second application flag. |
| `public int colliderSegments` | Cylinder resolution, clamped 8–32; default 20. Radius and width use the assigned wheel geometry. |
| `public PhysicsMaterial debrisMaterial` | Optional friction/bounce material. Otherwise creates a rubber-like runtime PhysicsMaterial for detached tire collision. |
| `public bool generateRollingCollider` | Default true: creates a convex cylindrical tire collision proxy on first release and enables it only while detached. Disable to use authored debris colliders. |
| `public Wheel wheel` | Required Wheel adapter on the separate WheelCollider mount. Its Visual must be this part transform or a child; the mount cannot be inside this detachable group. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Detach(Rigidbody vehicleBody)` | Validates linked visual/mount separation, prepares debris collision, uses shared DamagePart release, disables native wheel simulation before notifications and inherits axle spin. False for invalid/already-detached setups. Global damage gates apply to routed hits, not this explicit operation. | — |
