# Suspension and linkage API

Read [the system explanation](../Scripting/Suspension.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [AntiRoll](Suspension.md#antiroll)
- [AntiRoll.Axle](Suspension.md#antirollaxle)
- [ControlArm](Suspension.md#controlarm)
- [HalfShaft](Suspension.md#halfshaft)
- [ShockAbsorber](Suspension.md#shockabsorber)
- [SteeringTieRod](Suspension.md#steeringtierod)
- [Suspension](Suspension.md#suspension)
- [SuspensionAxle](Suspension.md#suspensionaxle)
- [SuspensionHub](Suspension.md#suspensionhub)
- [SuspensionRotationAxes](Suspension.md#suspensionrotationaxes)
- [SuspensionRotationLimits](Suspension.md#suspensionrotationlimits)

## AntiRoll

**Runtime/Drive/Suspension/AntiRoll.cs**

Adds cross-wheel roll support for the configured wheel relationships.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Axle[] axles` | Ordered axles configuration entries. Expand each item; see AntiRoll.Axle for its individual settings. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public float stiffness` | Anti-roll force scale applied from left/right suspension compression difference; increase it to resist body roll. Initial value: `4500`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Step(VehicleController v, Command c, float dt)` | Transfers bounded anti-roll load between eligible supported wheels in configured axle pairs. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## AntiRoll.Axle

**Runtime/Drive/Suspension/AntiRoll.cs**

Value data for axle; its fields are listed below.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Wheel left` | Assign the left Wheel component/asset used by AntiRoll.Axle. |
| `public Wheel right` | Assign the right Wheel component/asset used by AntiRoll.Axle. |

## ControlArm

**Runtime/Drive/Suspension/ControlArm.cs**

Resolves a visual control arm against its authored geometry.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float armLength` | Distance from hinge centre to outer ball joint, in metres. Pivot local X points outward; local Z is the hinge axis. |
| `public bool constrainNativeWheel` | Allows the linkage to constrain the native wheel mount; turn off for a visual-only control arm. Initial value: `true`. |
| `public virtual float CurrentAngle { get; protected set; }` | Read-only/resolved current angle for `ControlArm`. |
| `public Transform frontLeg` | Assign the front leg reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Transform hub` | Assign the hub reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 hubOffset` | Local-space hub offset vector used to place or size the corresponding geometry. Initial value: `new Vector3(0, .25f, 0)`. |
| `public Transform innerFrontAnchor` | Assign the inner front anchor reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Transform innerRearAnchor` | Assign the inner rear anchor reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 localLengthAxis` | Local mesh axis representing its length; align it with the modeled shaft, arm or linkage. Initial value: `Vector3.up`. |
| `public float maximumAngle` | Upper rotation angle in degrees for the configured motion. Initial value: `30`. |
| `public float meshLength` | Original mesh length used to scale the mesh to the distance between its anchors. Initial value: `2`. |
| `public float minimumAngle` | Lower rotation angle in degrees for the configured motion. Initial value: `-30`. |
| `public Transform outerJoint` | Assign the outer joint reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public virtual bool OutsideTravel { get; }` | Read-only/resolved outside travel for `ControlArm`. |
| `public Transform pivot` | Assign the pivot reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Transform rearLeg` | Assign the rear leg reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public SuspensionRotationLimits rotationLimits` | Allowed rotation axes and optional lower/upper angle bounds for this linkage. Initial value: `new SuspensionRotationLimits()`. |
| `public Transform shockAnchor` | Assign the shock anchor reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float shockMountFraction` | Multiplier/fraction controlling shock mount fraction. Increasing it increases this contribution relative to the unscaled value. Initial value: `.7f`. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public SteeringTieRod steeringLinkage` | Assign the steering linkage SteeringTieRod component/asset used by ControlArm. |
| `public Transform upright` | Assign the upright reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public WheelCollider wheel` | Assign the wheel reference used by ControlArm. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Wheel wheelAdapter` | Assign the wheel adapter Wheel component/asset used by ControlArm. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual Vector3 ResolveHub(Vector3 sample)` | Resolves the hub position from this control arm's authored geometry. | `sample` — Output water sample; read it only when sampling returns `true`. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation. |
| `public virtual void UpdatePose()` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |

## HalfShaft

**Runtime/Drive/Suspension/HalfShaft.cs**

Presents axle articulation and shaft rotation.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public SuspensionRotationLimits articulation` | Swing permissions in the neutral mesh frame. For a Y cylinder along chassis X, Z permits vertical articulation. |
| `public Transform innerAnchor` | Assign the inner anchor reference used by HalfShaft. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public virtual float JointAngle { get; }` | Read-only/resolved joint angle for `HalfShaft`. |
| `public Vector3 localRotationAxis` | Cardinal mesh axis used for both length and rotation (Unity cylinder: Y). |
| `public float maximumJointAngle` | Maximum joint angle in degrees, relative to the owning mechanism's reference frame. Initial value: `45`. |
| `public float meshLength` | Original mesh length used to scale the mesh to the distance between its anchors. Initial value: `2`. |
| `public Transform outerAnchor` | Assign the outer anchor reference used by HalfShaft. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 rotationOffset` | Orientation adjustment relative to the owning anchor/frame. Vector values are Euler angles in degrees. |
| `public Transform shaft` | Assign the shaft reference used by HalfShaft. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public virtual float SpinAngle { get; protected set; }` | Read-only/resolved spin angle for `HalfShaft`. |
| `public SuspensionRotationAxes spinAxes` | Permitted spin axes in mesh-local space. Enable the selected `localRotationAxis` to retain wheel spin. |
| `public float spinMultiplier` | Multiplier/fraction controlling spin multiplier. Increasing it increases this contribution relative to the unscaled value. Initial value: `1`. |
| `public float spinOffset` | Spin offset in metres in the owning system's space. |
| `public WheelCollider wheel` | Assign the wheel reference used by HalfShaft. Leave unassigned only when this feature is optional or the component can resolve it automatically. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void UpdatePose()` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |

## ShockAbsorber

**Runtime/Drive/Suspension/ShockAbsorber.cs**

Animates a telescoping shock and optionally overrides one wheel's physics.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public SuspensionRotationLimits articulation` | Allowed articulation axes and angle bounds for the visible linkage. Initial value: `new SuspensionRotationLimits()`. |
| `public Transform casing` | Assign the casing reference used by ShockAbsorber. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float casingLength` | Casing length in metres in the owning system's space. Initial value: `.65f`. |
| `public Transform chassisAnchor` | Assign the chassis anchor reference used by ShockAbsorber. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public virtual float Compression { get; }` | Resolved suspension compression of the configured wheel. |
| `public virtual float CurrentLength { get; }` | Read-only/resolved current length for `ShockAbsorber`. |
| `public float damper` | Shock damping coefficient, N s/m. |
| `public Vector3 localLengthAxis` | Local mesh axis representing its length; align it with the modeled shaft, arm or linkage. Initial value: `Vector3.up`. |
| `public float maximumLength` | Longest permitted linkage length in metres. Initial value: `1.25f`. |
| `public float meshLength` | Original mesh length used to scale the mesh to the distance between its anchors. Initial value: `2`. |
| `public float minimumLength` | Shortest permitted linkage length in metres. Initial value: `.7f`. |
| `public float motionRatio` | Shock travel / wheel travel. Wheel-equivalent spring and damping scale with this ratio squared. |
| `public virtual bool OutsideTravel { get; }` | Read-only/resolved outside travel for `ShockAbsorber`. |
| `public bool overrideWheelPhysics` | Overrides this wheel's native spring, damper and travel through the UVS Suspension module. Use one active override per wheel. |
| `public Transform piston` | Assign the piston reference used by ShockAbsorber. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float pistonLength` | Piston length in metres in the owning system's space. Initial value: `.65f`. |
| `public Vector3 rotationOffset` | Orientation adjustment relative to the owning anchor/frame. Vector values are Euler angles in degrees. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public float spring` | Shock spring stiffness, N/m. Motion ratio converts this to wheel stiffness. |
| `public float suspensionTravel` | Available wheel suspension travel in metres. Align the collider mount for this travel rather than setting travel to zero to align a mesh. Initial value: `.65f`. |
| `public float targetPosition` | Normalized suspension spring rest position: 0 is fully extended and 1 is fully compressed. Loaded height also depends on mass and spring strength. Initial value: `.5f`. |
| `public WheelCollider wheel` | Assign the wheel reference used by ShockAbsorber. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Transform wheelAnchor` | Assign the wheel anchor reference used by ShockAbsorber. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public virtual float WheelDamper { get; }` | Read-only/resolved wheel damper for `ShockAbsorber`. |
| `public virtual float WheelSpring { get; }` | Read-only/resolved wheel spring for `ShockAbsorber`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void UpdatePose()` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |

## SteeringTieRod

**Runtime/Drive/Suspension/SteeringTieRod.cs**

`Tracks` steering-link endpoints and geometry.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual float CurrentAngle { get; protected set; }` | Read-only/resolved current angle for `SteeringTieRod`. |
| `public Transform knuckle` | Assign the knuckle reference used by SteeringTieRod. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 localLengthAxis` | Local mesh axis representing its length; align it with the modeled shaft, arm or linkage. Initial value: `Vector3.up`. |
| `public float maximumRackTravel` | Maximum rack travel in metres in the owning system's space. Initial value: `.25f`. |
| `public float maximumSteeringAngle` | Maximum steering angle in degrees, relative to the owning mechanism's reference frame. Initial value: `40`. |
| `public float meshLength` | Original mesh length used to scale the mesh to the distance between its anchors. Initial value: `2`. |
| `public float previewSteeringAngle` | Preview steering angle in degrees, relative to the owning mechanism's reference frame. |
| `public virtual float RackDisplacement { get; protected set; }` | Read-only/resolved rack displacement for `SteeringTieRod`. |
| `public Transform rackEnd` | Assign the rack end reference used by SteeringTieRod. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 rackLocalAxis` | Direction vector defining rack local axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: `Vector3.right`. |
| `public Transform rackReference` | Assign the rack reference reference used by SteeringTieRod. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public virtual bool Reachable { get; protected set; }` | Read-only/resolved reachable for `SteeringTieRod`. |
| `public Transform rod` | Assign the rod reference used by SteeringTieRod. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public SuspensionRotationLimits rodArticulation` | Rod swivel permissions relative to the rack frame, with its mesh axis pointing across the chassis. |
| `public float rodLength` | Rod length in metres in the owning system's space. Initial value: `1.2f`. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public Transform steeringArmAnchor` | Assign the steering arm anchor reference used by SteeringTieRod. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Transform steeringLever` | Assign the steering lever reference used by SteeringTieRod. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Transform steeringPivot` | Independent kingpin anchor on the suspension carrier. Keep it outside the steered knuckle hierarchy. |
| `public SuspensionRotationLimits steeringRotation` | Knuckle rotation permissions in the native wheel frame. Native steering uses local Y. |
| `public WheelCollider wheel` | Assign the wheel reference used by SteeringTieRod. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 wheelCenterOffset` | Neutral wheel centre relative to the steering pivot, in the native wheel frame (metres). |
| `public virtual Vector3 WorldSteeringOffset { get; }` | Read-only/resolved world steering offset for `SteeringTieRod`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ApplyNativeSteering(float angle)` | Applies resolved linkage steering placement to the native wheel configuration. | `angle` — Angular coordinate in degrees for this geometry operation. |
| `public virtual float ResolveSteering(float demand)` | Resolves the linkage's steering geometry for the supplied wheel/angle state. | `demand` — Normalized actuator demand. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual void UpdatePose()` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |

## Suspension

**Runtime/Drive/Suspension/Suspension.cs**

Configures native wheel support and suspension-related response.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule), [IVehicleResetHandler](Modules.md#ivehicleresethandler).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<LandingEvent> Landed` | Once at first upright wheel contact after at least landingMinimumAirTime without wheel support. Copied LandingEvent includes apex descent, flight time, relative incoming speed, contact data, load and documented force estimates. Independent of landingResponse; low-speed contacts can have zero Intensity. Assisted rebound contacts are marked IsRebound. |
| `public event Action<LandingEvent> LandingCompleted` | Once when all operational wheel rays first have support after Landed. May occur in the same step. TimeSinceTouchdown describes axle approach, not suspension settling. Reset/teleport/disable cancels pending completion. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool allowLandingRebound` | Temporarily release the expansion limiter during landing response, allowing the springs to push the chassis back upward. Initial value: `true`. |
| `public bool arcadeBumpDamping` | Game-oriented damping of excessive upward body motion while most wheels remain supported. |
| `public bool automaticForceApplication` | Place the wheel force application point below this vehicle's centre of mass. |
| `public float bodySwayTravelRatio` | Additional force lever arm as a fraction of suspension travel, allowing body pitch and roll. |
| `public float bumpDampingResponse` | Response toward bump damping response. Higher values follow the requested state faster. Initial value: `10`. |
| `public float damper` | Damping strength opposing motion; larger values reduce oscillation but can slow the response. Initial value: `2295`. |
| `public float damperBlowoffSpeed` | Suspension stroke speed where the damper force stops rising linearly (m/s). |
| `public bool degressiveDamping` | Limit high-speed compression damper force while retaining rebound damping and low-speed body control. |
| `public bool directionalLandingBounce` | Apply landing rebound at the supporting wheels rather than only the centre of mass, allowing directional pitch and roll on angled landings. Default: `true`. |
| `public bool directionalLandingResponse` | Retain the approach speed while airborne so an angled chassis touch cannot instantly cancel the following wheel compression response. Assisted bounce energy still uses actual wheel contact speed. Default: `true`. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public float forceApplicationHeight` | Manual force-application height in metres, used when Automatic Force Application is off. Initial value: `0.15f`. |
| `public float forceOffsetBelowCenterOfMass` | Distance below the chassis centre of mass used to place the automatic wheel force-application point. Initial value: `.3f`. |
| `public float landingAngularBrakingTime` | Near the support plane, reduce the allowed approach speed using the remaining tilt divided by this time in seconds. Zero disables this final braking zone. Default: `.06f`. |
| `public float landingAngularContactGrace` | Seconds to fade angular touchdown damping after every wheel ray finds support, allowing the last axle to compress before assistance ends. Zero ends it immediately at full ray contact. Default: `.12f`. |
| `public float landingAngularDamping` | Angular damping rate in 1/s during partial wheel touchdown. With the speed limit enabled, only rotation above the allowed approach speed is damped. Default: `26`. |
| `public float landingAngularMaximumDeceleration` | Maximum requested relative angular deceleration during partial touchdown, in degrees/s squared. Default: `3600`. |
| `public float landingAngularMaximumSpeed` | Soft maximum relative approach rotation in degrees/s during angled touchdown. Faster rotation is progressively damped rather than clamped. Default: `60`. |
| `public bool landingAngularSpeedLimit` | Only brake excessive rotation toward the support plane. Ordinary axle descent remains free; disable to restore continuous angular damping. Default: `true`. |
| `public int LandingBounceCount { get; private set; }` | Whole-vehicle bounce releases in the current/last episode. Clears on configuration, teleport, response/option disable or component disable. |
| `public int landingBounceMaximumCount` | Maximum diminishing whole-vehicle bounce releases in one landing episode. Initial value: `3`. |
| `public float landingBounceMaximumRotation` | Maximum angular speed change from an assisted landing rebound in degrees/s. Bounds partial-wheel leverage without clamping native collision rotation. Default: `35`. |
| `public float landingBounceMaximumSpeed` | Upper limit on requested upward speed after the tires clear full suspension travel, relative to the surface, in m/s. Initial value: `2`. |
| `public float landingBounceMaximumTilt` | Maximum gravity-relative chassis tilt in degrees for assisted wheel rebound. Side and roof landings remain passive. Default: `55`. |
| `public float landingBounceRestitution` | Fraction of impact speed retained for the next hop. Each following hop is also bounded by the previous speed budget multiplied by this fraction. Initial value: `.45f`. |
| `public float LandingBounceSpeed { get; private set; }` | Last released target residual speed above full tire droop, in m/s; native spring work can change actual flight height. Clears with the bounce state. |
| `public float landingBumpStopMultiplier` | Progressive native stiffness at the end of landing travel, relative to each authored spring. Predicts the next compression step to absorb the impact before the rigid travel limit; only active during landing response. Initial value: `1.5f`. |
| `public float landingContactLeverage` | Blend the rebound application point from the centre of mass to the average supporting wheel contact. Higher values produce more pitch/roll from partial axle support. Default: `.75f`. |
| `public float landingDamperMultiplier` | Fraction of the normal damper retained at full landing response. Lower values allow more body bounce. Initial value: `.2f`. |
| `public float landingEventFullSpeed` | Surface-relative touchdown speed in m/s producing full LandingEvent intensity and landing event audio gain. Independent of physical landing assistance; minimum uses Landing Minimum Speed. Default: `15`. |
| `public float landingFullResponseSpeed` | Downward landing speed producing the full configured response, in m/s. Initial value: `4.5f`. |
| `public bool landingGroundBounce` | Enables a bounded assisted whole-vehicle hop on hard upright wheel landings. Blends in over the upper half of landing strength; ordinary reset drops use native suspension forces. Requires Landing Response. Enabled by default for grounded profiles. Initial value: `true`. |
| `public float landingImpactCompressionSpeed` | Requested normal compression speed after a predicted hard touchdown, in m/s. Lower values give the suspension more time to compress. Default: `1.5f`. |
| `public float landingImpactLeverage` | Impact impulse lever from chassis centre of mass to the weighted tire contacts. Lower values distribute more of the hard landing load through the chassis instead of instantly pitching it about the first axle. Default: `.15f`. |
| `public float landingImpactMinimumSpeed` | Minimum genuine airborne downward approach speed in m/s that arms predictive impact absorption. Lower-speed landings retain the normal spring response. Default: `8`. |
| `public float landingImpactReserveTravel` | Fraction of suspension travel reserved before the rigid compression stop. Protects against crossing the full stroke in one physics step. Default: `.15f`. |
| `public float landingMinimumAirTime` | Minimum continuous time without wheel support before a landing can activate the response, in seconds. Initial value: `.15f`. |
| `public float landingMinimumCycles` | Natural spring cycles at full landing strength, derived from chassis mass and softened wheel stiffness. Weaker impacts use fewer cycles; zero uses only the speed-scaled duration. Initial value: `2.5f`. |
| `public float landingMinimumSpeed` | Minimum downward contact speed relative to the landing surface, in m/s. Initial value: `1.5f`. |
| `public bool landingResponse` | Temporarily soften springs and damping after a genuine airborne wheel landing, allowing compression, rebound and a gradual settling of the chassis. Initial value: `true`. |
| `public float LandingResponse { get; private set; }` | Current 0–1 landing spring/damping blend, including preparation during descent; clears after settling, configuration, teleport or disable. |
| `public float landingResponseDuration` | Full-strength recovery time in seconds; the natural spring period and Landing Minimum Cycles can extend it. Weaker impacts use a shorter smooth recovery. Initial value: `.9f`. |
| `public float landingSpringMultiplier` | Fraction of each authored wheel spring retained at full landing response, including active shock overrides. Returns smoothly to the authored stiffness. Initial value: `.6f`. |
| `public bool limitExpansionVelocity` | Enables the native suspension expansion-velocity limit to restrict fast extension. Initial value: `true`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public bool predictiveLandingCompression` | Predict tire contact within the next physics step and absorb excessive approach speed before suspension hard-stop correction can flatten or displace the chassis. Requires Landing Response. Does not change the body pose. Default: `true`. |
| `public bool progressiveAngularLanding` | Dissipate chassis rotation toward the support plane while only some wheels have landed after genuine flight. Uses torque, leaving yaw and rotation away from the ground free. Requires Landing Response. Default: `true`. |
| `public bool showGizmos` | Shows selected-vehicle spring travel and rest-target guides. Configure individual channels in the bottom Gizmos foldout. |
| `public float spring` | Spring stiffness. Larger values produce a stronger restoring force for the same displacement. Initial value: `26250`. |
| `public float supportedRiseSpeed` | Upward body speed in m/s allowed before optional arcade bump damping acts while most wheels are supported. Initial value: `.75f`. |
| `public float targetPosition` | Normalized suspension spring rest position: 0 is fully extended and 1 is fully compressed. Loaded height also depends on mass and spring strength. Initial value: `0.5f`. |
| `public float wheelDampingRate` | Native WheelCollider rotational damping applied to the wheel. Initial value: `.02f`. |
| `public int wheelSubstepsAboveThreshold` | Native suspension/tire force substeps above the speed threshold. Lower counts trade contact stability for less simulation work. Apply configuration after editing. Default 15. |
| `public int wheelSubstepsBelowThreshold` | Native suspension/tire force substeps below the speed threshold. Lower counts reduce simulation work but can increase jitter or reduce contact stability. Apply configuration after editing. Default 12. |
| `public float wheelSubstepSpeedThreshold` | Vehicle speed threshold in m/s for choosing native WheelCollider substep counts. Applies to the whole vehicle, not separate wheels. Apply configuration after editing. Default 5 m/s. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController v)` | Builds owned shock-override mappings, clears travel history and applies configured native wheel spring/damper/travel policy. | `v` — V, interpreted by this operation in the declared type. |
| `public virtual void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |
| `public override void Step(VehicleController v, Command c, float dt)` | Updates per-wheel override settings, force-application placement and motion-dependent damping using envelope/native support. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## SuspensionAxle

**Runtime/Drive/Suspension/SuspensionAxle.cs**

Configuration/implementation type for suspension axle within suspension and linkage.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public SuspensionRotationLimits articulation` | Allowed articulation axes and angle bounds for the visible linkage. Initial value: `new SuspensionRotationLimits()`. |
| `public virtual float CurrentLength { get; }` | Read-only/resolved current length for `SuspensionAxle`. |
| `public Transform housing` | Assign the housing reference used by SuspensionAxle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Transform leftAnchor` | Assign the left anchor reference used by SuspensionAxle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 localLengthAxis` | Local mesh axis representing its length; align it with the modeled shaft, arm or linkage. Initial value: `Vector3.up`. |
| `public float meshLength` | Original mesh length used to scale the mesh to the distance between its anchors. Initial value: `2`. |
| `public Transform rightAnchor` | Assign the right anchor reference used by SuspensionAxle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Vector3 rotationOffset` | Orientation adjustment relative to the owning anchor/frame. Vector values are Euler angles in degrees. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void UpdatePose()` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |

## SuspensionHub

**Runtime/Drive/Suspension/SuspensionHub.cs**

Provides hub/kingpin geometry for the wheel assembly.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool followSteering` | When checked, follow steering is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public Vector3 positionOffset` | Position adjustment in the owning anchor/frame's local axes; normally measured in metres. |
| `public SuspensionRotationLimits rotationLimits` | Allowed rotation axes and optional lower/upper angle bounds for this linkage. Initial value: `new SuspensionRotationLimits()`. |
| `public Vector3 rotationOffset` | Orientation adjustment relative to the owning anchor/frame. Vector values are Euler angles in degrees. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public SteeringTieRod steeringLinkage` | Assign the steering linkage SteeringTieRod component/asset used by SuspensionHub. |
| `public WheelCollider wheel` | Assign the wheel reference used by SuspensionHub. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Wheel wheelAdapter` | Optional UVS wheel: follows its smoothed visual position after `Wheel.LateUpdate`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void UpdatePose()` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |

## SuspensionRotationAxes

**Runtime/Drive/Suspension/SuspensionRotationLimits.cs**

Defines the allowed suspension rotation axes choices used by this topic.

### Values

- `None = 0`
- `X = 1`
- `Y = 2`
- `Z = 4`
- `All = X \| Y \| Z`

## SuspensionRotationLimits

**Runtime/Drive/Suspension/SuspensionRotationLimits.cs**

Configuration/implementation type for suspension rotation limits within suspension and linkage.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public SuspensionRotationAxes allowedAxes` | Selects the allowed axes policy for this configuration. Options: `None`, `X`, `Y`, `Z`, `All`. Multiple flags can be combined. Initial value: `SuspensionRotationAxes.All`. |
| `public bool limitAngles` | When checked, limit angles is active; when unchecked the owning system skips that optional policy. |
| `public Vector3 maximumAngles` | Lower/upper components defining the maximum angles range in the owning mechanism's units. Initial value: `new Vector3(180, 180, 180)`. |
| `public Vector3 minimumAngles` | Lower/upper components defining the minimum angles range in the owning mechanism's units. Initial value: `new Vector3(-180, -180, -180)`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public float Angle(float angle, Vector3 axis)` | Returns a signed angular component in degrees for the configured constrained frame. | `angle` — Angular coordinate in degrees for this geometry operation. `axis` — Axis interpreted in the declaring geometry frame. **Returns:** Computed float in the operation's documented unit/domain. |
| `public Quaternion Apply(Quaternion desired, Quaternion neutral)` | Applies authored angular permissions/limits to a world rotation relative to its reference frame. | `desired` — Desired, interpreted by this operation in the declared type. `neutral` — Neutral reference orientation/pose. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation. |
| `public Quaternion ApplyLocal(Quaternion relative)` | Constrains a local requested rotation to the configured angular permissions and bounds. | `relative` — Whether the operation interprets its change relative to current state. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation. |
