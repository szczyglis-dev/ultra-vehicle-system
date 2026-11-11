# Collisions and stabilization API

## Types

- [Collisions](CollisionsAndStabilization.md#collisions)
- [DynamicObstacle](CollisionsAndStabilization.md#dynamicobstacle)
- [Stabilization](CollisionsAndStabilization.md#stabilization)

## Collisions

**Runtime/Physics/Stability/Collisions.cs**

See [the handling guide](../CollisionsAndStabilization.md). Component enable/disable controls participation; direct control is excluded.

**Inherits / implements:** [PhysicsModule](Modules.md#physicsmodule), [IVehicleResetHandler](Modules.md#ivehicleresethandler).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float bodyFriction` | Additional body friction coefficient, limited by the normal contact impulse. |
| `public bool coordinateLandingResponse` | Coordinate grip loss and sway with active smooth suspension landing: retain the impact speed before absorption and wait briefly for all tires to carry load. When suspension landing is disabled, use the ordinary immediate response. Default: `true`. |
| `public float crashDamperMultiplier` | Fraction of normal suspension damping retained just after a hard crash. Recovers smoothly through the suspension response window. Default: `.25f`. |
| `public float crashMaximumRotation` | Maximum additional chassis rotation rate in degrees/s per crash. Default: `100`. |
| `public float crashMinimumLeverage` | Minimum effective pitch/roll leverage in severe supported impacts. Default: `.6f`. |
| `public float crashGroundPivot` | Blend severe-crash direction toward the struck-end ground pivot; zero follows the real contact lever. Default: `.8f`. |
| `public float crashMaximumLiftSpeed` | Maximum additional upward chassis speed in m/s; zero disables lift. Default: `2`. |
| `public float crashEnergyFraction` | Maximum fraction of normal impact energy for the additional rotation/lift, including a movable partner. Default: `.08f`. |
| `public float crashCentredYaw` | Optional yaw target in degrees/s for severe near-centred impacts; alternates sides. Zero disables this presentation effect. Default: `12`. |
| `public float crashMinimumSpeed` | Normal collision speed in m/s required for chassis weight transfer. Default: `6`. |
| `public float crashRotationPerSpeed` | Pitch/roll speed change in degrees/s per m/s of closing speed. Scaled by actual collision impulse so light debris cannot kick the car. Default: `4`. |
| `public float crashSuspensionRecovery` | Seconds for suspension damping to recover after the impact. Default: `.7f`. |
| `public float crashAttackTime` | Seconds to peak crash force; zero begins immediately on the next physics step. Default: `0`. |
| `public float crashReleaseTime` | Seconds for crash force to fade from its peak; preserves the bounded impulse budget. Default: `.14f`. |
| `public bool crashFromWheelImpacts` | Opt in to supported tire impacts against near-vertical obstacles. Requires `crashWeightTransfer`; excludes landings and leaves native tire restitution unchanged. Default: `false`. |
| `public bool crashWeightTransfer` | Deliver a short, bounded pitch/roll impulse through the chassis after a hard body impact. Direction follows the contact normal and gravity. Default: `true`. |
| `public float crashYawVariation` | Maximum small yaw-rate variation in degrees/s after a hard crash. Its sign follows the real contact lever; zero disables it. Default: `3`. |
| `public override int ExecutionOrder { get; }` | Default local order 100. |
| `public float impactCooldown` | Minimum seconds between additional crash impulses. |
| `public bool impactResponse` | Supply missing collision restitution after the native solver resolves the impact. Default: `true`. |
| `public float landingContactHoldTime` | Maximum seconds after first tire contact to hold grip recovery and defer the sway while the remaining tires acquire load. Zero disables the contact wait; pre-absorption impact strength is still retained. Default: `.45f`. |
| `public float landingForwardGrip` | Forward grip retained at full landing response, before other grip modifiers. Initial value: `.45f`. |
| `public float LandingForwardGripScale { get; }` | Current forward tire-grip multiplier before other grip policies. |
| `public float landingFullResponseSpeed` | Normal landing speed producing full grip loss and sway, in m/s. Initial value: `4.5f`. |
| `public float LandingGripLoss { get; private set; }` | Current 0–1 grip-loss envelope; smooth recovery, zero when inactive. |
| `public float landingGripRecoveryTime` | Seconds for tire grip and stability assistance to smoothly recover. Initial value: `.85f`. |
| `public float landingLateralSway` | Maximum added sideways speed in m/s at a directional landing. Delivered over a short ground-contact push. Initial value: `.45f`. |
| `public float landingMinimumAirTime` | Minimum unsupported flight time before a wheel landing is eligible, in seconds. Initial value: `.15f`. |
| `public float landingMinimumSpeed` | Minimum normal landing speed relative to the surface, in m/s. Initial value: `1.5f`. |
| `public float landingRearGripBias` | Additional sideways grip reduction on wheels behind the centre of mass during recovery. Initial value: `.2f`. |
| `public float landingSidewaysGrip` | Sideways grip retained at full landing response, before other grip modifiers. Initial value: `.3f`. |
| `public float LandingSidewaysGripScale { get; }` | Current base lateral grip and stability-authority multiplier; rear wheel bias is applied separately. |
| `public bool landingTractionLoss` | Briefly reduce tire grip after an airborne wheel landing and allow a small directional sway. Initial value: `true`. |
| `public float landingYawSway` | Maximum additional yaw-rate change in degrees/s. Direction follows the landing's lateral motion, bank and first wheel contacts. Initial value: `7`. |
| `public float maximumAngularKick` | Maximum angular speed change per impact, in degrees/s. Off-centre contacts naturally pitch, yaw or roll. |
| `public float maximumReboundSpeed` | Maximum additional separation speed, in m/s. |
| `public float minimumBodyTilt` | Minimum gravity-relative tilt for additional body sliding friction. |
| `public float minimumImpactSpeed` | Normal closing speed required for an additional response, in m/s. |
| `public override ExecutionPhase Phase { get; }` | Contact phase: updates landing grip loss before steering, friction and stability assistance. |
| `public float restitution` | Target separation speed as a fraction of normal closing speed. Existing PhysX bounce is counted. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Clears transient state, binds the configured vehicle and refreshes owned native settings. Called by vehicle configuration. | — |
| `public virtual void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |
| `public override void Step(VehicleController vehicle, Command command, float dt)` | Detects grounded-profile wheel landings, updates recovery and distributes the bounded directional sway while wheels touch ground. No direct-control or kinematic forces. | — |

## DynamicObstacle

**Runtime/Physics/Stability/DynamicObstacle.cs**

Opt-in native settings for movable world props pushed by heavier vehicles. Enabled on the five Demo/Samples dynamic crates. No forces, velocity clamps, pose corrections or per-frame updates. Disabling restores captured Rigidbody settings; re-enable captures fresh ownership. Reapply after editing fields or switching kinematic mode.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public CollisionDetectionMode collisionDetection` | Native collision detection mode. Default ContinuousSpeculative covers angular motion and dynamic panels; kinematic bodies use Speculative when a non-Discrete mode is requested. |
| `public RigidbodyInterpolation interpolation` | Native display interpolation. Default Interpolate matches the default vehicle. |
| `public float maximumDepenetrationSpeed` | Maximum native overlap-separation speed in m/s, retains a lower original cap. Does not cap physical impact speed. Default: `2`. |
| `public int solverIterations` | Minimum position solver passes; retains higher original settings. Default: `0`. Zero preserves original. |
| `public int solverVelocityIterations` | Minimum velocity solver passes; retains higher original settings. Default: `0`. Zero preserves original. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ApplySettings()` | Captures settings on first active application and configures the owned Rigidbody. Reapplication never overwrites the restoration snapshot. No-op when disabled. | No arguments; no return value. |

## Stabilization

**Runtime/Physics/Stability/Stabilization.cs**

See [the handling guide](../CollisionsAndStabilization.md). Component enable/disable controls participation; direct control is excluded.

**Inherits / implements:** [PhysicsModule](Modules.md#physicsmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<Telemetry> Overturned` | Raised once when sustained tilt qualifies; carries the telemetry snapshot at that transition. |
| `public event System.Action<Telemetry> Recovered` | Raised once when tilt falls below the recovery threshold; carries the telemetry snapshot at that transition. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool affectOtherProfiles` | Opt in for air/water/hover profiles. Normally only grounded profiles are supported. |
| `public Vector3 airborneDamping` | Local pitch/yaw/roll damping rates in 1/s while airborne. |
| `public float airborneDelay` | Wait after losing wheel support before applying damping, in seconds. |
| `public bool autoRighting` | Smoothly push a slow vehicle on its side back onto its wheels using torque while the body touches the ground. |
| `public bool detectOverturn` | When checked, detect overturn is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public override int ExecutionOrder { get; }` | Default order 760 in the assistance phase. |
| `public bool IsAirborne { get; private set; }` | Whether the last module step found no wheel support or fresh body contact. |
| `public bool IsOverturned { get; private set; }` | Current is overturned. |
| `public bool IsRighting { get; }` | Whether optional assisted recovery is currently active. |
| `public float maximumDeceleration` | Maximum angular deceleration in degrees/s squared. |
| `public float maximumSpin` | Soft angular speed threshold in degrees/s; does not hard-clamp velocity. |
| `public float overspeedDamping` | Additional damping above Maximum Spin, in 1/s. |
| `public float overturnAngle` | Overturn angle in degrees, relative to the owning mechanism's reference frame. Initial value: `70`. |
| `public float overturnDelay` | Time continuously tilted before reporting overturn, in seconds. |
| `public float recoveryAngle` | Tilt below which an overturned vehicle is considered recovered. Initial value: `40`. |
| `public float rightingDamping` | Angular damping in 1/s during recovery. |
| `public float rightingDelay` | Seconds continuously overturned and touching the ground before recovery starts. |
| `public float rightingMaximumAcceleration` | Recovery angular acceleration limit in degrees/s squared. |
| `public float rightingMaximumSpeed` | Maximum chassis speed in m/s during assisted recovery. |
| `public float rightingMaximumTilt` | Maximum eligible tilt for side recovery; roof recovery is excluded. Default: `125`, range 90–135 degrees. |
| `public float rightingMinimumTilt` | Tilt in degrees required to begin recovery. |
| `public float rightingStrength` | Angular spring strength in 1/s squared. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Clears transient state, binds the configured vehicle and refreshes owned native settings. Called by vehicle configuration. | — |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Runs passive airborne damping and optional grounded recovery for this fixed step. Ignores missing/kinematic bodies and non-positive timesteps. | — |
| `public override bool SupportsProfile(DriveProfile profile)` | Allows grounded profiles by default; affectOtherProfiles opts into other media. | — |
