# Water sampling and movement API

Read [the system explanation](../Scripting/Water.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [SubmarineProfile](Water.md#submarineprofile)
- [WaterContact](Water.md#watercontact)
- [WaterInteraction](Water.md#waterinteraction)
- [WaterProvider](Water.md#waterprovider)
- [WaterSample](Water.md#watersample)
- [WaterSurfaceProfile](Water.md#watersurfaceprofile)
- [WaterSurface](Water.md#watersurface)

## SubmarineProfile

**Runtime/Drive/Profiles/SubmarineProfile.cs**

Consumes water state for underwater movement.

**Inherits / implements:** [FreeProfile](DriveProfiles.md#freeprofile).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool holdDepth` | Hold the current world height after releasing ascend/dive controls. Requires propulsion power; disable for passive vertical drift. |
| `public float hullHalfHeight` | Hull half height. Initial value: `1.5f`. |
| `public float lateralResistance` | Lateral resistance. Initial value: `1.8f`. |
| `public float levelingStrength` | Leveling strength. Initial value: `4`. |
| `public float maximumPitch` | Maximum pitch. Initial value: `18`. |
| `public override string Medium { get; }` | Movement-family label used by the profile contract. |
| `public float quadraticResistance` | Quadratic resistance. Initial value: `.025f`. |
| `public float turnResponse` | Turn response. Initial value: `2`. |
| `public float verticalAcceleration` | Vertical acceleration. Initial value: `2`. |
| `public float verticalResistance` | Vertical resistance. Initial value: `2`. |
| `public Vector2 waterCenter` | Water center. Initial value: `new Vector2(-280, 80)`. |
| `public float waterLevel` | Flat fallback water-surface height in world metres. |
| `public Vector2 waterSize` | Water size. Initial value: `new Vector2(400, 640)`. |
| `public float yawRate` | Yaw rate. Initial value: `.42f`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public virtual bool ContainsWater(Vector3 position)` | Checks whether a position lies inside this profile's fallback water region. | `position` — Requested point or switch detent; see its declared type and owning operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public override float ResolveBoostDemand(VehicleController vehicle, Command command)` | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Samples valid water, applies immersion-dependent buoyancy/resistance and powered movement/depth-hold response. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public SubmarineProfile()` | Constructs `SubmarineProfile` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## WaterContact

**Runtime/World/Water/WaterInteraction.cs**

Value data for water contact; its fields are listed below.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float bowEntry` | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
| `public Vector3 forward` | Forward. |
| `public float forwardSpeed` | Forward speed. |
| `public Vector2 halfSize` | Half size. |
| `public float hullMotion` | Hull motion. |
| `public float impact` | Impact. |
| `public float leftEntry` | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
| `public float pitch` | Pitch. |
| `public Vector3 position` | Position. |
| `public Vector3 relativeVelocity` | Relative velocity. |
| `public Vector3 right` | Right. |
| `public float rightEntry` | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
| `public float roll` | Roll. |
| `public float speed` | Speed. |
| `public float sternEntry` | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
| `public WaterSample surface` | Copied water height, normal and flow at the hull sample. |
| `public bool wet` | Wet. |

## WaterInteraction

**Runtime/World/Water/WaterInteraction.cs**

Connects vehicle water sampling and hull contact state.

**Inherits / implements:** [WorldModule](Modules.md#worldmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<bool> InteractionEnabledChanged` | When the master water-interaction gate changes. Payload: bool; the gate affects water physics, not just effects. |
| `public event System.Action<WaterProvider> ProviderChanged` | When assigned water provider changes. Payload: `WaterProvider`, possibly `null`. |
| `public event System.Action<bool> SubmergedChanged` | When sampled body-center submergence changes. Payload: bool; this is not an arbitrary hull wetness percentage. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Vector2 hullHalfSize` | Half-width / half-length in metres, shared by water audio and particle contact points. |
| `public virtual bool IsSubmerged { get; protected set; }` | Current is submerged predicate; read it instead of maintaining a second application flag. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public override bool SupportsReleasedForces { get; }` | Keeps passive maintenance/observation active during release; Drive and Engine suppress force output, and TireCollision keeps native solid proxies without supplemental tread forces. |
| `public bool useProfileFallback` | Allow the Boat profile's flat water when no explicit provider is assigned. |
| `public bool waterInteractionEnabled` | Master switch for water interaction: buoyancy, water audio and water particles. |
| `public WaterProvider waterProvider` | Assign the water provider WaterProvider component/asset used by WaterInteraction. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public static WaterContact Read(VehicleController vehicle, Vector2 fallbackHalfSize)` | Builds surface-boat hull contact from the vehicle's water sampling and configured hull dimensions; non-Boat/dry/invalid vehicles return a dry contact. | `vehicle` — Vehicle context/owner receiving the operation. `fallbackHalfSize` — Half-width/half-length used when building fallback hull contact. **Returns:** Returned `WaterContact`; ownership remains as specified by the creating/lookup operation. |
| `public virtual void SetInteractionEnabled(bool value)` | Changes the vehicle's water-interaction gate, affecting sampling/physics as well as its contact state. | `value` — Requested bool state for this operation. |
| `public virtual void SetWaterProvider(WaterProvider provider)` | Replaces the assigned water adapter and publishes the provider change. | `provider` — Assigned water adapter; `null` selects the configured fallback policy where supported. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Samples the root center of mass and publishes a changed submerged/not-submerged state. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual bool TrySample(Vector3 worldPosition, out WaterSample sample)` | Queries valid water at a world position; `false` means no sample, not height zero. | `worldPosition` — World-space query position in Unity metres. `sample` — Output water sample; read it only when sampling returns `true`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public static bool TrySampleSurface(VehicleController vehicle, Vector3 position, out WaterSample sample)` | Queries the provider's surface sample through vehicle water policy. | `vehicle` — Vehicle context/owner receiving the operation. `position` — Requested point or switch detent; see its declared type and owning operation. `sample` — Output water sample; read it only when sampling returns `true`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## WaterProvider

**Runtime/World/Water/WaterProvider.cs**

Abstract sampling adapter and `WaterSample` data contract.

**Inherits / implements:** `MonoBehaviour`.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public abstract bool TrySample(Vector3 worldPosition, out WaterSample sample)` | Queries valid water at a world position; `false` means no sample, not height zero. | `worldPosition` — World-space query position in Unity metres. `sample` — Output water sample; read it only when sampling returns `true`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## WaterSample

**Runtime/World/Water/WaterProvider.cs**

Value data for water sample; its fields are listed below.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float height` | Sampled water surface world height in metres. |
| `public Vector3 normal` | World-space unit normal of sampled support/contact surface. |
| `public Vector3 velocity` | World water-flow velocity including relevant wave motion, in m/s. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public WaterSample(float height, Vector3 normal, Vector3 velocity)` | Constructs `WaterSample` with the supplied initial state. | `height` — Height, interpreted by this operation in the declared type. `normal` — Contact/surface normal in the declared frame. `velocity` — World velocity in m/s. **Returns:** New instance initialized from the supplied arguments. |

## WaterSurfaceProfile

**Runtime/World/Water/WaterSurfaceProfile.cs**

Configuration/implementation type for water style within water sampling and movement.

**Inherits / implements:** `ScriptableObject`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Color deepColor` | Color and alpha used to render deep color. Initial value: `new Color(.025f, .15f, .34f, 1)`. |
| `public float depthAbsorption` | Strength of depth-based water-color absorption. Initial value: `.3f`. |
| `public Color foamColor` | Color and alpha used to render foam color. Initial value: `new Color(.7f, .88f, .87f, 1)`. |
| `public float reflectionStrength` | Multiplier for the water material's reflection contribution. Initial value: `.8f`. |
| `public float rippleScale` | Multiplier/fraction controlling ripple scale. Increasing it increases this contribution relative to the unscaled value. Initial value: `.055f`. |
| `public float rippleStrength` | Visible small-ripple contribution to the water surface. Initial value: `.13f`. |
| `public float roughness` | Water-surface roughness used by its material; larger values soften the reflective appearance. Initial value: `.34f`. |
| `public Color shallowColor` | Color and alpha used to render shallow color. Initial value: `new Color(.065f, .32f, .52f, 1)`. |
| `public float shorelineFoam` | Amount of depth/shoreline foam produced by the water shader. Initial value: `.55f`. |
| `public Vector4 waveA` | Direction X/Z, wavelength in metres, amplitude in metres. Shared by CPU sampling and shader. |
| `public Vector4 waveB` | Second wave: X/Z direction in the first two components, wavelength in metres in Z, and amplitude in metres in W. Initial value: `new Vector4(-.4f, .92f, 11, .045f)`. |
| `public float waveSpeed` | Multiplier for wave phase speed shared by CPU surface sampling and shader animation. Initial value: `.65f`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual WaterSample Sample(Vector3 position, float time, float baseHeight, bool waves)` | Evaluates the configured water-wave style at a world position/time using base height and optional wave participation. | `position` — Requested point or switch detent; see its declared type and owning operation. `time` — Explicit sample time in seconds. `baseHeight` — World water baseline height. `waves` — Whether wave displacement participates in the sample. **Returns:** Returned `WaterSample`; ownership remains as specified by the creating/lookup operation. |

## WaterSurface

**Runtime/World/Water/WaterSurface.cs**

Built-in water-surface provider implementation.

**Inherits / implements:** [WaterProvider](Water.md#waterprovider).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool animateWaves` | Enables time-varying wave height and normal instead of a flat surface. |
| `public bool depthEffectsEnabled` | Uses existing camera depth if available; no camera/depth/opaque passes are requested by this component. |
| `public bool generateGrid` | Generate a bounded grid for vertex waves. Disable to retain your authored mesh. |
| `public float gridCellSize` | Grid-cell size in metres for the generated water mesh; smaller cells create a denser mesh. Initial value: `5`. |
| `public virtual int GridVertexCount { get; }` | Read-only/resolved grid vertex count for `WaterSurface`. |
| `public Material materialOverride` | Explicit water material; leave empty to retain the material authored on the renderer. |
| `public bool reflectionsEnabled` | Enables reflections behavior for this system. Initial value: `true`. |
| `public bool renderSurface` | When checked, render surface is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public virtual float SampleTime { get; }` | Read-only/resolved sample time for `WaterSurface`. |
| `public Vector2 size` | Water surface width and length in metres. Initial value: `new Vector2(400, 640)`. |
| `public WaterSurfaceProfile style` | Assign the style WaterSurfaceProfile component/asset used by WaterSurface. |
| `public MeshRenderer surfaceRenderer` | Assign the surface renderer reference used by WaterSurface. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public bool waterEnabled` | Enables water behavior for this system. Initial value: `true`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void RenderSurface()` | Updates the built-in water surface's rendered representation. | No arguments; no returned value. |
| `public override bool TrySample(Vector3 position, out WaterSample sample)` | Queries valid water at a world position; `false` means no sample, not height zero. | `position` — Requested point or switch detent; see its declared type and owning operation. `sample` — Output water sample; read it only when sampling returns `true`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TrySampleAtTime(Vector3 position, float time, out WaterSample sample)` | Queries the built-in water model at an explicit time for consistent wave evaluation. | `position` — Requested point or switch detent; see its declared type and owning operation. `time` — Explicit sample time in seconds. `sample` — Output water sample; read it only when sampling returns `true`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
