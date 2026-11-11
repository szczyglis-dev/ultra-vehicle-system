# Ground surfaces and classification API

Read [the system explanation](../Scripting/SurfaceFeedback.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [Friction](SurfaceFeedback.md#friction)
- [Surface](SurfaceFeedback.md#surface)
- [TireSurface](SurfaceFeedback.md#tiresurface)
- [TireSurface.LayerMapping](SurfaceFeedback.md#tiresurfacelayermapping)
- [TireSurfaceProfile](SurfaceFeedback.md#tiresurfaceprofile)

## Friction

**Runtime/Physics/Friction/Friction.cs**

Reads physical grip and writes native tire friction behavior.

**Inherits / implements:** [PhysicsModule](Modules.md#physicsmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public float handbrakeLateralGrip` | Multiplier for sideways tire grip while the handbrake affects the wheel; lower values permit easier lateral sliding. Initial value: `0.55f`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Step(VehicleController v, Command c, float dt)` | Reads Surface from exact native hit colliders and writes forward/side friction with handbrake/tracked policy. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## Surface

**Runtime/Physics/Friction/Surface.cs**

Stores the physical grip multiplier on a contact collider.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float grip` | Surface grip multiplier used when a wheel contacts this surface. Initial value: `1`. |

## TireSurface

**Runtime/Effects/Surfaces/TireSurface.cs**

Maps a collider/hierarchy or Terrain layers to effect profiles.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public TireSurfaceProfile profile` | Assign the profile TireSurfaceProfile component/asset used by TireSurface. |
| `public static int Revision { get; private set; }` | Shared revision invalidating contact surface caches after mapping changes. |
| `public LayerMapping[] terrainLayers` | Optional dominant painted layer mapping for a `TerrainCollider` on this object. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void RefreshTerrain()` | Rebuilds cached painted-Terrain-layer classification after mapping/paint changes. | No arguments; no returned value. |
| `public virtual TireSurfaceProfile Resolve(Collider collider, Vector3 worldPoint)` | Resolves the mapped effect profile for a native hit, including dominant Terrain-layer classification when configured. | `collider` — Native collider used for ownership/contact classification. `worldPoint` — World-space target/sample point. **Returns:** Returned `TireSurfaceProfile`; ownership remains as specified by the creating/lookup operation. |

## TireSurface.LayerMapping

**Runtime/Effects/Surfaces/TireSurface.cs**

Value data for layer mapping; its fields are listed below.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public TerrainLayer layer` | TerrainLayer asset associated with this tire-surface profile in terrain sampling. |
| `public TireSurfaceProfile profile` | Assign the profile TireSurfaceProfile component/asset used by TireSurface.LayerMapping. |

## TireSurfaceProfile

**Runtime/Effects/Surfaces/TireSurfaceProfile.cs**

Stores presentation assets and effect multipliers.

**Inherits / implements:** `ScriptableObject`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public float brakeAudioMultiplier` | Scales braking sound for wheels touching this surface, including its custom brakingLoop. Zero mutes the brake contribution. |
| `public AudioClip brakingLoop` | Optional brake recording for this surface. Empty uses BrakeAudio.brakingLoop only when useDefaultBrakeLoopWhenEmpty is true; otherwise it is silent. This does not change the tire loop. |
| `public float fullRollingSpeed` | Ground-relative rolling speed in m/s mapped to full rolling-only activity. Initial value: `12`. |
| `public bool granularParticles` | Use a separate, bounded grain spray pool instead of the smoke preset. Custom wheel systems/prefabs keep their authored design. |
| `public bool looseTracks` | Draw irregular soil ruts instead of rubber grooves, within the same mesh/material. |
| `public Color markColor` | Color and alpha used to render mark color. Initial value: `new Color(.025f, .025f, .025f, .8f)`. |
| `public float markLifetime` | Time before tire marks on this surface fade away, in seconds. |
| `public bool marksEnabled` | Enables marks behavior for this system. Initial value: `true`. |
| `public float markWidthMultiplier` | Multiplier/fraction controlling mark width multiplier. Increasing it increases this contribution relative to the unscaled value. Initial value: `1`. |
| `public float minimumRollingSpeed` | Ground-relative rolling speed in m/s below which rolling-only activity is zero. Initial value: `1`. |
| `public Color particleColor` | Color and alpha used to render particle color. Initial value: `new Color(.78f, .8f, .82f, .25f)`. |
| `public float particleGravity` | Gravity multiplier applied to the generated surface particles. |
| `public Vector2 particleLifetime` | Lower and upper particle lifetimes in seconds. Initial value: `new Vector2(1.8f, 3.2f)`. |
| `public Material particleMaterial` | Assign the particle material reference used by TireSurfaceProfile. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float particleRateMultiplier` | Multiplier/fraction controlling particle rate multiplier. Increasing it increases this contribution relative to the unscaled value. Initial value: `1`. |
| `public bool particlesEnabled` | Enables particles behavior for this system. Initial value: `true`. |
| `public Vector2 particleSize` | Local-space particle size vector used to place or size the corresponding geometry. Initial value: `new Vector2(.32f, .58f)`. |
| `public Vector2 particleSpeed` | Lower and upper initial particle speeds. Initial value: `new Vector2(.08f, .22f)`. |
| `public float rollingAudio` | Rolling-only audio contribution; zero leaves audio driven by slip. |
| `public float rollingMarks` | Minimum mark activity added by ordinary rolling; zero leaves marks driven by slip. |
| `public float rollingParticles` | Minimum particle activity added by ordinary rolling; zero leaves particles driven by slip. |
| `public AudioClip tireLoop` | Audio recording for tire loop. No assigned clip means this recording is unavailable. |
| `public bool useDefaultBrakeLoopWhenEmpty` | When brakingLoop is empty, selects the component brake recording instead of silence. Default true. Surface brakeAudioMultiplier still applies. |
| `public bool useDefaultTireLoopWhenEmpty` | When tireLoop is empty, selects the component tire recording instead of silence. Default false. Surface volume, pitch and activity still apply. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual float MarkActivity(WheelContact contact)` | Evaluates skidmark activity using this surface profile's presentation multipliers. | `contact` — Normalized physical contact participation. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual float ParticleActivity(WheelContact contact)` | Evaluates tire-particle activity from rolling/skid inputs and profile multipliers. | `contact` — Normalized physical contact participation. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual float Rolling(float speed)` | Evaluates this surface profile's rolling-presentation activity. | `speed` — Speed, interpreted by this operation in the declared type. **Returns:** Computed float in the operation's documented unit/domain. |
