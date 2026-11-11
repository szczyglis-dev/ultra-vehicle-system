# Particles and tire marks API

Read [the system explanation](../Scripting/Presentation.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [BoatWaterParticles](Presentation.md#boatwaterparticles)
- [EffectsCore](Presentation.md#effectscore)
- [EffectsModule](Presentation.md#effectsmodule)
- [ExhaustSmoke](Presentation.md#exhaustsmoke)
- [ParticleFactory](Presentation.md#particlefactory)
- [JetBlast](Presentation.md#jetblast)
- [JetBlastActivation](Presentation.md#jetblastactivation)
- [PropulsionJets](Presentation.md#propulsionjets)
- [SkidmarkBuffer](Presentation.md#skidmarkbuffer)
- [Skidmarks](Presentation.md#skidmarks)
- [TireBurnoutSmokeSettings](Presentation.md#tireburnoutsmokesettings)
- [TireSmoke](Presentation.md#tiresmoke)
- [TireSmokeMode](Presentation.md#tiresmokemode)
- [WaterParticleFactory](Presentation.md#waterparticlefactory)

## BoatWaterParticles

**Runtime/Effects/Particles/BoatWaterParticles.cs**

Uses hull-water contact for surface-water presentation.

**Inherits / implements:** [EffectsModule](Presentation.md#effectsmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float cullDistance` | Distance beyond which this effect suspends rendering, in metres; zero disables distance culling. |
| `public virtual float CurrentHullRippleRate { get; protected set; }` | Current resolved hull-ripple emission rate, in particles per second. |
| `public virtual float CurrentPropellerRate { get; protected set; }` | Current resolved propeller emission rate, in particles per second. |
| `public virtual float CurrentWakeRate { get; protected set; }` | Current resolved wake emission rate, in particles per second. |
| `public virtual int EmittedSplashCount { get; protected set; }` | Read-only/resolved emitted splash count for `BoatWaterParticles`. |
| `public Engine engine` | Assign the engine Engine component/asset used by BoatWaterParticles. |
| `public Material foamMaterial` | Assign the foam material reference used by BoatWaterParticles. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float fullEffectSpeed` | Hull speed in m/s at which speed-driven water effects reach full contribution. Initial value: `20`. |
| `public Vector2 hullHalfSize` | Used without a `WaterInteraction` component; that component's size takes priority. |
| `public float hullRippleRate` | Base hull-ripple emission rate, in particles per second. |
| `public bool hullRipplesEnabled` | Enables hull ripples behavior for this system. Initial value: `true`. |
| `public Transform motorOutlet` | Optional authored motor outlet; otherwise use `sternOffset` relative to the hull. |
| `public int propellerBudget` | Maximum count/resolution for propeller budget. Larger values increase detail or work performed by this system. Initial value: `384`. |
| `public bool propellerEnabled` | Enables propeller behavior for this system. Initial value: `true`. |
| `public ParticleSystem propellerPrefab` | Assign the propeller prefab reference used by BoatWaterParticles. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float propellerRate` | Propeller, wake and splash emission rates at full channel activity, in particles per second. |
| `public float runningSprayFactor` | Small bow-side droplets produced by forward motion, in addition to real hull impacts. |
| `public int splashBudget` | Maximum count/resolution for splash budget. Larger values increase detail or work performed by this system. Initial value: `192`. |
| `public float splashEntryThreshold` | Minimum inward hull-point speed eligible for entry splash particles, in m/s. |
| `public bool splashesEnabled` | Enables splashes behavior for this system. Initial value: `true`. |
| `public float splashFullEntrySpeed` | Water-entry speed in m/s at which splash intensity reaches full contribution. Initial value: `.45f`. |
| `public ParticleSystem splashPrefab` | Assign the splash prefab reference used by BoatWaterParticles. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float splashRate` | Propeller, wake and splash emission rates at full channel activity, in particles per second. |
| `public Material sprayMaterial` | Assign the spray material reference used by BoatWaterParticles. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 sternOffset` | Fallback propeller-emission point in vehicle-local coordinates, in metres. |
| `public virtual int SystemCount { get; }` | Read-only/resolved system count for `BoatWaterParticles`. |
| `public VehicleController vehicle` | Assign the vehicle VehicleController component/asset used by BoatWaterParticles. |
| `public int wakeBudget` | Maximum count/resolution for wake budget. Larger values increase detail or work performed by this system. Initial value: `256`. |
| `public bool wakeEnabled` | Enables wake behavior for this system. Initial value: `true`. |
| `public ParticleSystem wakePrefab` | Assign the wake prefab reference used by BoatWaterParticles. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float wakeRate` | Propeller, wake and splash emission rates at full channel activity, in particles per second. |
| `public bool waterParticlesEnabled` | Enables water particles behavior for this system. Initial value: `true`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController owner)` | Caches the vehicle and resolves an unassigned engine reference. | `owner` — Unity/application owner whose identity controls this relationship or resource. |
| `public virtual void RenderWater(float deltaTime)` | Updates water particles from resolved hull-water contact. | `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void Suspend()` | Stops owned water-particle presentation according to the module's cleanup policy. | No arguments; no returned value. |

## EffectsCore

**Runtime/Effects/Core/EffectsCore.cs**

Configuration/implementation type for effects core within particles and tire marks.

**Inherits / implements:** [CategoryCore](Modules.md#categorycore).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public EffectsCore()` | Constructs `EffectsCore` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## EffectsModule

**Runtime/Effects/Core/EffectsModule.cs**

Configuration/implementation type for effects module within particles and tire marks.

**Inherits / implements:** [VehicleModule](Modules.md#vehiclemodule), [IEffectsModule](Modules.md#ieffectsmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |

## ExhaustSmoke

**Runtime/Effects/Particles/ExhaustSmoke.cs**

Controls emission from configured exhaust outlets.

**Inherits / implements:** [EffectsModule](Presentation.md#effectsmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool animateCustomParticles` | Animate speed, size and tint on supplied particle prefabs/systems as well as generated defaults. |
| `public bool createDefaultParticles` | Enables create default particles behavior for this system. Initial value: `true`. |
| `public virtual float CurrentActivity { get; protected set; }` | Read-only/resolved current activity for `ExhaustSmoke`. |
| `public virtual float CurrentRate { get; protected set; }` | Current resolved emission rate, in particles per second. |
| `public Material defaultMaterial` | Assign the default material reference used by ExhaustSmoke. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Engine engine` | Assign the engine Engine component/asset used by ExhaustSmoke. |
| `public Transform[] exhaustPoints` | Assign the exhaust points references used by ExhaustSmoke. Entries are processed in list order. |
| `public float idleRate` | Emission rate at idle activity, in particles per second. |
| `public float intensityMultiplier` | Multiplier/fraction controlling intensity multiplier. Increasing it increases this contribution relative to the unscaled value. Initial value: `4`. |
| `public float loadedRate` | Emission rate at full propulsion load, in particles per second. |
| `public float nitroIntensity` | Nitro flame emission multiplier. Default 1; zero stops emission. |
| `public ParticleSystem nitroParticlePrefab` | Nitro flame prefab at Exhaust Points. The optional Demo supplies a default; replace or clear to disable. |
| `public float nitroResponse` | Flame intensity response per second. Default 12; release stops emission immediately. |
| `public float nitroRpmInfluence` | RPM influence on flame emission, speed and size. Default .75; zero preserves the prefab baseline response. |
| `public ParticleSystem particlePrefab` | Assign the particle prefab reference used by ExhaustSmoke. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public ParticleSystem[] particles` | Assign the particles references used by ExhaustSmoke. Entries are processed in list order. |
| `public float response` | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: `12`. |
| `public VehicleController vehicle` | Assign the vehicle VehicleController component/asset used by ExhaustSmoke. |

## ParticleFactory

**Runtime/Effects/Particles/ParticleFactory.cs**

Configuration/implementation type for particle factory within particles and tire marks.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public static ParticleSystem CreateSand(string name, Transform parent, Material material)` | Creates a granular tire-particle system using the supplied material and owned parent. | `name` — Diagnostic name for the generated source/object. `parent` — Owner transform for a newly created presentation resource. `material` — Assigned presentation material; ownership is not transferred implicitly. **Returns:** Returned `ParticleSystem`; ownership remains as specified by the creating/lookup operation. |
| `public static ParticleSystem CreateSmoke(string name, Transform parent, Material material, bool exhaust)` | Creates a smoke particle system using the supplied material and owned parent. | `name` — Diagnostic name for the generated source/object. `parent` — Owner transform for a newly created presentation resource. `material` — Assigned presentation material; ownership is not transferred implicitly. `exhaust` — Exhaust, interpreted by this operation in the declared type. **Returns:** Returned `ParticleSystem`; ownership remains as specified by the creating/lookup operation. |
| `public static void SetRate(ParticleSystem system, float rate)` | Sets a particle emission rate on an existing system. | `system` — Existing `ParticleSystem` to update. `rate` — Requested particle emission rate. |

## PropulsionJets

**Runtime/Effects/Particles/PropulsionJets.cs**

Presents propulsion exhaust/jet outlets.

**Inherits / implements:** [EffectsModule](Presentation.md#effectsmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<bool> JetsEnabledChanged` | When jet presentation availability changes. Payload: bool; this does not report mechanical thrust. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform[] aircraftPoints` | Assign the aircraft points references used by PropulsionJets. Entries are processed in list order. Initial value: `Array.Empty<Transform>()`. |
| `public Color color` | Color and alpha used to render color. Initial value: `new Color(.25f, .65f, 1, .7f)`. |
| `public virtual float CurrentRate { get; protected set; }` | Current resolved emission rate, in particles per second. |
| `public Material defaultMaterial` | Assign the default material reference used by PropulsionJets. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Engine engine` | Assign the engine Engine component/asset used by PropulsionJets. |
| `public bool followPropulsionSpool` | Scale emission by the shared aircraft engine spool. Custom particle prefabs remain untouched. |
| `public Transform[] hoverPoints` | Assign the hover points references used by PropulsionJets. Entries are processed in list order. Initial value: `Array.Empty<Transform>()`. |
| `public float idleRate` | Emission rate at idle activity, in particles per second. |
| `public bool jetsEnabled` | Enables jets behavior for this system. Initial value: `true`. |
| `public float jetSpeed` | Particle launch speed for the generated propulsion jet visuals. Initial value: `4`. |
| `public float loadedRate` | Emission rate at full propulsion load, in particles per second. |
| `public float nitroRateMultiplier` | PropulsionJets emission multiplier at full Nitro output; default 3, minimum 1. |
| `public ParticleSystem particlePrefab` | Assign the particle prefab reference used by PropulsionJets. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public VehicleController vehicle` | Assign the vehicle VehicleController component/asset used by PropulsionJets. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void SetJetsEnabled(bool value)` | Changes propulsion-jet presentation availability without setting mechanical thrust. | `value` — Requested bool state for this operation. |

## SkidmarkBuffer

**Runtime/Effects/Decals/SkidmarkBuffer.cs**

Stores bounded world-space ribbon geometry.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Mesh Mesh { get; }` | Read-only/resolved mesh for `SkidmarkBuffer`. |
| `public int SegmentCount { get; private set; }` | Read-only/resolved segment count for `SkidmarkBuffer`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void Add(Vector3 from, Vector3 to, Vector3 normal, float width, float intensity, float birthTime)` | Appends a mark segment to the bounded geometry buffer and returns its buffer identifier. | `from` — Source movement profile/state. `to` — Target movement profile/state. `normal` — Contact/surface normal in the declared frame. `width` — Mark/tire width in metres. `intensity` — Intensity, interpreted by this operation in the declared type. `birthTime` — Mark creation time. |
| `public void Add(Vector3 from, Vector3 to, Vector3 normal, float width, float intensity, float birthTime, Color tint, float lifetime)` | Appends a mark segment to the bounded geometry buffer and returns its buffer identifier. | `from` — Source movement profile/state. `to` — Target movement profile/state. `normal` — Contact/surface normal in the declared frame. `width` — Mark/tire width in metres. `intensity` — Intensity, interpreted by this operation in the declared type. `birthTime` — Mark creation time. `tint` — Recorded mark color. `lifetime` — ProjectileDemo lifetime in seconds. |
| `public SkidmarkBuffer(int capacity)` | Constructs `SkidmarkBuffer` with the supplied initial state. | `capacity` — Capacity, interpreted by this operation in the declared type. **Returns:** New instance initialized from the supplied arguments. |
| `public void Upload()` | Uploads changed mark geometry to the owned mesh. | No arguments; no returned value. |

## Skidmarks

**Runtime/Effects/Decals/Skidmarks.cs**

Consumes contact state and controls trail history.

**Inherits / implements:** [EffectsModule](Presentation.md#effectsmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action Cleared` | After skidmark history is cleared. No payload. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public float groundOffset` | Ground offset in metres in the owning system's space. Initial value: `.015f`. |
| `public float lifetime` | Time in seconds before the generated object/effect expires. Initial value: `35`. |
| `public Material material` | Use Szczyglis/`UltraVehicleSystem`/Skidmarks or a compatible transparent vertex-color material. |
| `public float maximumGap` | Largest separation that may be joined by one continuous tire trail, in metres. |
| `public int maxSegments` | Maximum count/resolution for max segments. Larger values increase detail or work performed by this system. Initial value: `2048`. |
| `public float minimumDistance` | Minimum distance in metres in the owning system's space. Initial value: `.12f`. |
| `public float minimumIntensity` | Minimum normalized skid/mark activity required to emit a ribbon segment. Initial value: `.12f`. |
| `public virtual int SegmentCount { get; }` | Read-only/resolved segment count for Skidmarks. |
| `public TireFeedback tireFeedback` | Assign the feedback TireFeedback component/asset used by Skidmarks. |
| `public float width` | Base ribbon width in metres for emitted skid marks, before any surface mark-width multiplier. Initial value: `.24f`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ClearMarks()` | Clears this vehicle's recorded mark history and breaks existing trails. | No arguments; no returned value. |

## TireSmoke

**Runtime/Effects/Particles/TireSmoke.cs**

Manages wheel smoke and granular emission.

**Inherits / implements:** [EffectsModule](Presentation.md#effectsmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool createDefaultParticles` | Enables create default particles behavior for this system. Initial value: `true`. |
| `public virtual float CurrentIntensity { get; protected set; }` | Read-only/resolved current intensity for `TireSmoke`. |
| `public Material defaultMaterial` | Assign the default material reference used by TireSmoke. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float emissionResponse` | Response of smoke density to changing slip. Zero follows slip immediately. |
| `public float maximumRate` | Largest permitted particle emission rate, in particles per second. |
| `public float minimumIntensity` | Minimum normalized tire-effect activity required to emit smoke. Initial value: `.12f`. |
| `public ParticleSystem particlePrefab` | Assign the particle prefab reference used by TireSmoke. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Material sandMaterial` | Assign the sand material reference used by TireSmoke. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public TireFeedback tireFeedback` | Assign the feedback TireFeedback component/asset used by TireSmoke. |
| `public ParticleSystem[] wheelParticles` | Assign the wheel particles references used by TireSmoke. Entries are processed in list order. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual ParticleSystem GetWheelParticles(int index)` | Returns the smoke/granular particle systems owned for a configured wheel. | `index` — Zero-based configured-entry index; use the owner's current list ordering. **Returns:** Returned `ParticleSystem`; ownership remains as specified by the creating/lookup operation. |



| Declaration | Usage |
| --- | --- |
| `public event System.Action<int, bool> WheelBurnoutChanged` | When a wheel enters or leaves burnout smoke presentation; carries wheel index and active flag. |
| `public event System.Action<TireSmokeMode> SmokeModeChanged` | After selecting a different tire-smoke presentation mode. |
| `public TireSmokeMode smokeMode` | Automatic selects tire-ring smoke from physical wheelspin; Contact Patch keeps ordinary skid smoke; Tire Ring requests the dense cloud while the tire is slipping. |
| `public TireBurnoutSmokeSettings burnoutSmoke` | Appearance and activation settings for the separate burnout cloud. |
| `public bool IsWheelBurningOut(int index)` | Returns whether the indexed wheel currently requests burnout smoke; false for an invalid index. |
| `public ParticleSystem GetBurnoutParticles(int index)` | Returns the indexed wheel burnout particle system, or null when unavailable. |
| `public void SetSmokeMode(TireSmokeMode mode)` | Switches the smoke presentation mode without changing the mechanical Burnout request. |

## WaterParticleFactory

**Runtime/Effects/Particles/WaterParticleFactory.cs**

Configuration/implementation type for water particle factory within particles and tire marks.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public static ParticleSystem Create(Transform parent, string name, Material material, bool foam, int budget)` | Creates an owned water-particle presentation system with the requested style/material context. | `parent` — Owner transform for a newly created presentation resource. `name` — Diagnostic name for the generated source/object. `material` — Assigned presentation material; ownership is not transferred implicitly. `foam` — Foam, interpreted by this operation in the declared type. `budget` — Budget, interpreted by this operation in the declared type. **Returns:** Returned `ParticleSystem`; ownership remains as specified by the creating/lookup operation. |

## TireSmokeMode

**Runtime/Effects/Particles/TireBurnoutSmoke.cs**

Selects whether tire effects follow ordinary slip, the separate burnout presentation, or both. Mechanical burnout requests still belong to the Burnout module.


### Values

- `Automatic`
- `ContactPatch`
- `TireRing`

## TireBurnoutSmokeSettings

**Runtime/Effects/Particles/TireBurnoutSmoke.cs**

Independent particle appearance and activation thresholds for tire burnout smoke. This changes presentation, not drivetrain torque, slip or grip.


| Declaration | Usage |
| --- | --- |
| `public bool enabled` | Allows the separate burnout cloud to emit when the selected smoke mode requests it. |
| `public float maximumTravelSpeed` | Maximum road-relative wheel travel speed for automatic tire-ring smoke. |
| `public float minimumSpinSpeed` | Minimum excess tire circumference speed over road travel. Locked wheels do not qualify. |
| `public float minimumIntensity` | Minimum surface particle activity required by Automatic mode, normalized 0..1. |
| `public float buildupSeconds` | Seconds for the dense cloud to build up. Smoke already emitted remains in world space. |
| `public float maximumRate` | Maximum burnout cloud emission rate in particles per second. |
| `public Vector2 lifetime` | Minimum and maximum emitted particle lifetime in seconds. |
| `public Vector2 size` | Minimum and maximum starting particle size in metres. |

## JetBlast

**Runtime/Effects/Forces/JetBlast.cs**

Base type: `EffectsModule`. See [configuration and usage](../Particles.md#jet-blast).

| Member | Purpose |
| --- | --- |
| `event Action<Rigidbody, Vector3> BodyPushed` | Target body and applied force in newtons, once per outlet and step. |
| `JetBlastActivation activation` | EngineRunning includes idle; ThrottleOnly requires a throttle request. |
| `float minimumThrottle` | Minimum throttle in ThrottleOnly mode. |
| `Transform[] outlets` | Exhaust origins; local +Z points outward. |
| `float length` | Plume reach in metres. |
| `float startRadius`, `float endRadius` | Plume radii in metres. |
| `float maximumForce` | Force at full power, in newtons per outlet. |
| `float forceMultiplier` | Overall multiplier for idle and full-power forces. |
| `float idleStrength` | Running idle fraction. |
| `LayerMask affectedLayers` | Target collision layers. |
| `int contactCapacity` | Query capacity reserved at configuration. |
| `bool showGizmos` | Selected range preview. |
| `float Strength { get; private set; }` | Resolved engine demand and spool fraction. |
| `bool SupportsReleasedForces` | False; released vehicle-force mode does not emit a powered blast. |
| `void Configure(VehicleController vehicle)` | Bind engine and propulsion; prepare buffers. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Vehicle scheduler entry for physical exhaust. |

## JetBlastActivation

| Value | Behavior |
| --- | --- |
| `EngineRunning` | Emit with a running engine, including configured idle strength. Vehicle selection does not affect activation. |
| `ThrottleOnly` | Require positive throttle above Minimum Throttle. |
