# Wheels, contact and damage

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [Coasting](#coasting) | 3 |
| [Collisions](#collisions) | 35 |
| [Damage](#damage) | 7 |
| [DamageCollisionRelay](#damagecollisionrelay) | 0 |
| [DebrisMotion](#debrismotion) | 0 |
| [DynamicObstacle](#dynamicobstacle) | 5 |
| [Friction](#friction) | 1 |
| [PhysicsModule](#physicsmodule) | 0 |
| [Stabilization](#stabilization) | 28 |
| [Surface](#surface) | 1 |
| [TireCollision](#tirecollision) | 4 |
| [VehicleMeshDeformation](#vehiclemeshdeformation) | 5 |
| [Wheel](#wheel) | 16 |
| [WheelDynamics](#wheeldynamics) | 1 |
| [WheelLift](#wheellift) | 25 |
| [WheelLiftPitchSupport](#wheelliftpitchsupport) | 4 |
| [WheelSetup](#wheelsetup) | 17 |

## Coasting

Configuration/implementation type for coasting within wheel definitions and contact.

**Source:** `Runtime/Physics/Wheels/Coasting.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `contactReleaseTorque` | `float` | Tiny intent torque in N·m. It releases native static tire constraints, not engine propulsion. | `.01`; Minimum: .0001f |
| `minimumSlopeDegrees` | `float` | Smallest downhill slope that should release stationary tire contact. Increase to prevent creeping on nearly level surfaces; decrease to allow gentler slopes to start the vehicle rolling. | `1`; Range: 0 to 10 |
| `releaseBelowRpm` | `float` | Wheel RPM below which the small release torque may be applied to let a stationary tire start rolling downhill. Above this speed the module leaves the spinning wheel alone. | `15`; Minimum: 0 |

## Collisions

See [the handling guide](../CollisionsAndStabilization.md). Component enable/disable controls participation; direct control is excluded.

**Source:** `Runtime/Physics/Stability/Collisions.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `bodyFriction` | `float` | Additional body friction coefficient, limited by the normal contact impulse. | `.8`; Range: 0 to 1 |
| `coordinateLandingResponse` | `bool` | Coordinate grip loss and sway with active smooth suspension landing: retain the impact speed before absorption and wait briefly for all tires to carry load. When suspension landing is disabled, use the ordinary immediate response. | `true` |
| `crashAttackTime` | `float` | Seconds for the crash impulse strength to reach its peak. Zero starts at full strength on the next physics step; does not add a waiting period. | `0`; Minimum: 0 |
| `crashCentredYaw` | `float` | Additional yaw target in degrees/s for severe, nearly centred impacts. Alternates direction between crashes to break perfect symmetry; zero disables this presentation effect. | `12`; Minimum: 0 |
| `crashDamperMultiplier` | `float` | Fraction of normal suspension damping retained just after a hard crash. Recovers smoothly through the suspension response window. | `.25`; Range: 0 to 1 |
| `crashEnergyFraction` | `float` | Maximum fraction of normal impact energy converted into additional chassis rotation, including a movable collision partner. | `.08`; Range: 0 to .25f |
| `crashFromWheelImpacts` | `bool` | Also transfer a supported crash through a tire hitting a near-vertical obstacle. Requires Crash Weight Transfer. Ground contacts and wheel landings are excluded; native tire restitution is unchanged. | `false` |
| `crashGroundPivot` | `float` | Blend the supplemental severe-crash direction toward a ground pivot: the struck end stays low while the opposite end rises. Zero follows the actual contact lever only. | `.8`; Range: 0 to 1 |
| `crashMaximumLiftSpeed` | `float` | Maximum additional upward chassis speed in m/s from the supported crash pivot. Couples lift to the pitching response so the struck end stays low. Zero disables lift. | `2`; Minimum: 0 |
| `crashMaximumRotation` | `float` | Maximum additional chassis rotation rate in degrees/s per crash. | `100`; Minimum: 0 |
| `crashMinimumLeverage` | `float` | Minimum effective pitch/roll leverage for severe supported crashes. Prevents a contact near the centre-of-mass height from suppressing the chassis response. Blends in between one and two times Crash Minimum Speed. | `.6`; Range: 0 to 1 |
| `crashMinimumSpeed` | `float` | Normal collision speed in m/s required for chassis weight transfer. | `6`; Minimum: 0 |
| `crashReleaseTime` | `float` | Seconds for crash impulse strength to fade from its peak to zero. Attack and release shape the same bounded impulse budget; longer times do not add energy. | `.14`; Minimum: 0 |
| `crashRotationPerSpeed` | `float` | Pitch/roll target in degrees/s per m/s of closing speed. Scaled by the real normal impulse and contact leverage; native rotation counts toward the target. | `4`; Minimum: 0 |
| `crashSuspensionRecovery` | `float` | Seconds for suspension damping to recover after the impact. | `.7`; Minimum: .05f |
| `crashWeightTransfer` | `bool` | Deliver a short, bounded pitch/roll and lift response during a supported body impact. Ground Pivot can bias the direction; native rotation counts toward the target. | `true` |
| `crashYawVariation` | `float` | Maximum additional yaw-rate target in degrees/s after a hard crash. Direction follows the contact lever; centred impacts add no random yaw. Zero disables it. | `3`; Minimum: 0 |
| `impactCooldown` | `float` | Minimum seconds between additional crash impulses. | `.12`; Minimum: 0 |
| `impactResponse` | `bool` | Supply missing collision restitution after the native solver resolves the impact. | `true` |
| `landingContactHoldTime` | `float` | Maximum seconds after first tire contact to hold grip recovery and defer the sway while the remaining tires acquire load. Zero disables the contact wait; pre-absorption impact strength is still retained. | `.45`; Minimum: 0 |
| `landingForwardGrip` | `float` | Forward grip retained at full landing response, before other grip modifiers. | `.45`; Range: .05f to 1 |
| `landingFullResponseSpeed` | `float` | Normal landing speed producing full grip loss and sway, in m/s. | `4.5`; Minimum: .1f |
| `landingGripRecoveryTime` | `float` | Seconds for tire grip and stability assistance to smoothly recover. | `.85`; Minimum: .05f |
| `landingLateralSway` | `float` | Maximum added sideways speed in m/s at a directional landing. Delivered over a short ground-contact push. | `.45`; Minimum: 0 |
| `landingMinimumAirTime` | `float` | Minimum unsupported flight time before a wheel landing is eligible, in seconds. | `.15`; Minimum: 0 |
| `landingMinimumSpeed` | `float` | Minimum normal landing speed relative to the surface, in m/s. | `1.5`; Minimum: 0 |
| `landingRearGripBias` | `float` | Additional sideways grip reduction on wheels behind the centre of mass during recovery. | `.2`; Range: 0 to .8f |
| `landingSidewaysGrip` | `float` | Sideways grip retained at full landing response, before other grip modifiers. | `.3`; Range: .05f to 1 |
| `landingTractionLoss` | `bool` | Briefly reduce tire grip after an airborne wheel landing and allow a small directional sway. | `true` |
| `landingYawSway` | `float` | Maximum additional yaw-rate change in degrees/s. Direction follows the landing's lateral motion, bank and first wheel contacts. | `7`; Minimum: 0 |
| `maximumAngularKick` | `float` | Maximum angular speed change per impact, in degrees/s. Off-centre contacts naturally pitch, yaw or roll. | `55`; Minimum: 0 |
| `maximumReboundSpeed` | `float` | Maximum additional separation speed, in m/s. | `3`; Minimum: 0 |
| `minimumBodyTilt` | `float` | Minimum gravity-relative tilt for additional body sliding friction. | `45`; Range: 0 to 180 |
| `minimumImpactSpeed` | `float` | Normal closing speed required for an additional response, in m/s. | `4`; Minimum: 0 |
| `restitution` | `float` | Target separation speed as a fraction of normal closing speed. Existing PhysX bounce is counted. | `.12`; Range: 0 to .5f |

## Damage

### State and configuration

**Source:** `Runtime/Physics/Damage/Damage.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `damageEnabled` | `bool` | Allows this module to accept damage. Turn off to stop its damage accumulation, mesh dents and damage-driven detachment. | `true` |
| `damageMultiplier` | `float` | Multiplies accepted impact damage before it is applied to nearby parts. Higher values make the same collision damage parts more and reach detach thresholds sooner. | `1`; Minimum: 0 |
| `deformationEnabled` | `bool` | Allows accepted impacts to bend the affected meshes through MeshDeformation. Turn off to retain damage and detachment while leaving mesh shapes unchanged. | `true` |
| `detachmentEnabled` | `bool` | Allows damaged parts to break away when their detach threshold is reached. Turn off to keep parts attached even if they accumulate damage. | `true` |
| `impactRadius` | `float` | Distance in metres around the hit point that can receive damage and dents. Damage falls off toward the edge; increase to spread a hit over a larger area. | `.9`; Minimum: .01f |
| `minimumImpactSpeed` | `float` | Minimum relative collision speed in m/s required for collision-driven damage. | `3`; Minimum: 0 |
| `parts` | `DamagePart[]` ([fields](Exterior.md#damagepart)) | Body parts that can accumulate damage, deform or detach. Only registered entries are processed; tune each part's damage response in its own settings. | `Empty list` |

## DamageCollisionRelay

Relays relevant native collisions into damage handling.

**Source:** `Runtime/Physics/Damage/DamageCollisionRelay.cs`. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## DebrisMotion

Exists only on released debris. Snapshot before the solver and remove excess contact-generated motion afterwards; airborne and inherited motion are retained.

**Source:** `Runtime/Physics/Damage/DebrisMotion.cs`. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## DynamicObstacle

Opt-in native settings for movable world props pushed by heavier vehicles. Enabled on the five Demo/Samples dynamic crates. No forces, velocity clamps, pose corrections or per-frame updates. Disabling restores captured Rigidbody settings; re-enable captures fresh ownership. Reapply after editing fields or switching kinematic mode.

**Source:** `Runtime/Physics/Stability/DynamicObstacle.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `collisionDetection` | `CollisionDetectionMode` | Collision detection used while this component owns the dynamic obstacle. Speculative contacts cover angular motion and contacts with the vehicle's physical panels. | `CollisionDetectionMode.ContinuousSpeculative` |
| `interpolation` | `RigidbodyInterpolation` | Display interpolation for the obstacle. Interpolate matches the default vehicle display and avoids visible relative stepping. | `RigidbodyInterpolation.Interpolate` |
| `maximumDepenetrationSpeed` | `float` | Maximum native speed for separating overlapping contacts, m/s. Limits penetration recovery kicks, not ordinary collision speed or momentum. | `2`; Minimum: .1f |
| `solverIterations` | `int` | Optional minimum native position solver iterations. Zero preserves the original setting; higher existing values are retained. | `0`; Range: 0 to 255 |
| `solverVelocityIterations` | `int` | Optional minimum native velocity solver iterations. Zero preserves the original setting; higher existing values are retained. | `0`; Range: 0 to 255 |

## Friction

Reads physical grip and writes native tire friction behavior.

**Source:** `Runtime/Physics/Friction/Friction.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `handbrakeLateralGrip` | `float` | Multiplier for sideways tire grip while the handbrake affects the wheel; lower values permit easier lateral sliding. | `0.55`; Range: 0.1f to 1 |

## PhysicsModule

Configuration/implementation type for physics module within module lifecycle and scheduling.

**Source:** `Runtime/Physics/Core/PhysicsModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [VehicleModule](Common.md#vehiclemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## Stabilization

See [the handling guide](../CollisionsAndStabilization.md). Component enable/disable controls participation; direct control is excluded.

**Source:** `Runtime/Physics/Stability/Stabilization.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `affectOtherProfiles` | `bool` | Opt in for air/water/hover profiles. Normally only grounded profiles are supported. | `false` |
| `airborneDamping` | `Vector3` | Local pitch/yaw/roll damping rates in 1/s while airborne. | `new Vector3(.65, .2, .65)` |
| `airborneDelay` | `float` | Delay before airborne damping, in seconds. Airborne leveling instead builds smoothly through this interval. | `.12`; Minimum: 0 |
| `airborneLevelDamping` | `float` | Roll damping in 1/s for optional airborne leveling. | `8`; Minimum: 0 |
| `airborneLevelMaximumAcceleration` | `float` | Maximum airborne leveling acceleration in degrees/s squared. | `360`; Minimum: 0 |
| `airborneLevelMaximumTilt` | `float` | Largest gravity-relative bank angle eligible for airborne leveling. Angles beyond this range retain their physical tumble. | `170`; Range: 0 to 179 |
| `airborneLevelStrength` | `float` | Angular spring strength in 1/s squared for optional airborne leveling. | `16`; Minimum: 0 |
| `autoLevelAirborne` | `bool` | Apply bounded local-Z roll torque toward gravity-relative upright bank during free flight. Does not correct local pitch or yaw; yields to active rider steering unless Prevent Outward Air Roll is enabled. Disabled after driver ejection when motorcycle balance is suppressed. | `false` |
| `autoRighting` | `bool` | Smoothly push a slow vehicle on its side back onto its wheels using torque while the body touches the ground. | `false` |
| `detectOverturn` | `bool` | Monitors chassis tilt and publishes overturn/recovery events. It does not itself right the vehicle or eject passengers. | `true` |
| `maximumDeceleration` | `float` | Maximum angular deceleration in degrees/s squared. | `540`; Minimum: 0 |
| `maximumSpin` | `float` | Soft angular speed threshold in degrees/s; does not hard-clamp velocity. | `180`; Minimum: 0 |
| `overspeedDamping` | `float` | Additional damping above Maximum Spin, in 1/s. | `3`; Minimum: 0 |
| `overturnAngle` | `float` | Tilt from gravity-up, in degrees, that must persist for Overturn Delay before an overturn event is published. Lower values report overturn sooner. | `70`; Range: 10 to 180 |
| `overturnDelay` | `float` | Seconds the excessive-tilt condition must persist before publishing an overturn. | `.25`; Minimum: 0 |
| `preventOutwardAirRoll` | `bool` | When airborne leveling is enabled, block rider roll input away from upright and keep automatic roll recovery active during corrective input. Pitch control is unchanged. | `true` |
| `recoveryAngle` | `float` | Tilt below which an overturned vehicle is considered upright again and the event detector resets. Keep below Overturn Angle to avoid repeated state changes near the boundary. | `40`; Range: 0 to 170 |
| `rightingBuildTime` | `float` | Seconds for recovery torque to build smoothly after Righting Delay. Zero preserves immediate full-strength assistance. | `0`; Minimum: 0 |
| `rightingContactGrace` | `float` | Seconds to continue an already active recovery across brief support gaps while lifting off the chassis onto the wheels. Longer gaps stop recovery and restart its delay and buildup. | `0`; Minimum: 0 |
| `rightingDamping` | `float` | Angular damping in 1/s during recovery. | `7`; Minimum: 0 |
| `rightingDelay` | `float` | Seconds continuously overturned and touching the ground before recovery starts. | `1.5`; Minimum: 0 |
| `rightingMaximumAcceleration` | `float` | Recovery angular acceleration limit in degrees/s squared. | `1440`; Minimum: 0 |
| `rightingMaximumSpeed` | `float` | Maximum chassis speed in m/s during assisted recovery. | `3`; Minimum: 0 |
| `rightingMaximumTilt` | `float` | Maximum tilt eligible for side recovery. Roof landings are excluded. | `125`; Range: 90 to 135 |
| `rightingMinimumTilt` | `float` | Tilt in degrees required to begin recovery. | `55`; Range: 1 to 180 |
| `rightingOnWheelSupport` | `bool` | Allow recovery from excessive lean while usable wheels still touch the ground. Wall/ceiling tire contact is not standing support. | `false` |
| `rightingRollOnly` | `bool` | Recover only sideways bank around the vehicle's longitudinal Z axis. Does not correct wheelies, nose pitch or heading. | `false` |
| `rightingStrength` | `float` | Angular spring strength in 1/s squared. | `12`; Minimum: 0 |

## Surface

Stores the physical grip multiplier on a contact collider.

**Source:** `Runtime/Physics/Friction/Surface.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `grip` | `float` | Surface grip multiplier used when a wheel contacts this surface. | `1`; Range: 0.05f to 3 |

## TireCollision

Adds supplemental solid tire contacts.

**Source:** `Runtime/Physics/Wheels/TireCollision.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `cylinderSides` | `int` | Number of sides in the supplemental tire collision shape. More sides make the shape rounder but add collision work; the implementation clamps this to 12–48. | `32`; Range: 12 to 48 |
| `radiusScale` | `float` | Radius of the supplemental solid tire as a fraction of Wheel's radius. Values slightly below 1 keep it inside the rolling tire; larger values make side/obstacle contact occur earlier. | `.99`; Range: .9f to 1 |
| `supportNormalThreshold` | `float` | Minimum alignment of a contact normal with the support direction for it to count as ground support. Higher values reject steeper side contacts rather than treating them as tread contact. | `.55`; Range: .1f to .95f |
| `treadFriction` | `float` | Friction limit for supplemental tread contacts. Higher values resist sliding more strongly at those contacts; this is separate from the native WheelCollider friction curves. | `1`; Range: 0 to 2 |

## VehicleMeshDeformation

Owns readable mesh instances, dent buffers and geometry restoration.

**Source:** `Runtime/Physics/Damage/VehicleMeshDeformation.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `damage` | `Damage` ([fields](Physics.md#damage)) | Damage source publishing accepted pre-detachment deformation requests. | `None / unassigned` |
| `dentPerDamage` | `float` | Visual displacement per accepted damage unit, in metres. | `.008`; Minimum: 0 |
| `maximumDent` | `float` | Largest total vertex displacement from its rest pose, in metres. | `.35`; Minimum: 0 |
| `meshUploadIntervalFrames` | `int` | Rendered LateUpdate calls with pending dents before uploading changed meshes. Higher values batch more impacts and normal rebuilds, but dents and DeformationChanged appear later. Damage calculation still runs for every hit. Default 1. | `1`; Range: 1 to 16 |
| `recalculateNormals` | `bool` | Rebuild lighting normals when uploading dents. Disable to reduce mesh rebuild cost while retaining existing normals; deformed lighting becomes less accurate. Bounds are always updated. Default enabled. | `true` |

## Wheel

[Wheel contact](../API/WheelContact.md)

**Source:** `Runtime/Physics/Wheels/Wheel.cs`. Component / asset.

When registered in Vehicle Controller → Wheels → Wheel Setup, the copied geometry, roles and references are read-only here. Edit them in Wheel Setup and apply the configuration. Visual suspension smoothing remains local to Wheel.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `brake` | `bool` | Allows service-brake torque on this wheel. Disable for a wheel that should free-roll under the main brake pedal. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `true` |
| `brakeMultiplier` | `float` | Multiplies this wheel's service-brake torque. Use lower front/rear values to tune brake balance; zero removes its service-brake contribution. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `1`; Minimum: 0 |
| `caliper` | `Transform` | Optional brake-caliper mesh following suspension/steering without spinning with the tire. | `None / unassigned` |
| `caliperRotationOffset` | `Quaternion` | Rotation correcting the brake-caliper mesh's axes in the non-spinning hub frame. It aligns the visual without changing brake strength. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `Quaternion.identity` |
| `driven` | `bool` | Includes this wheel among wheels receiving propulsion. Enable only on driven axles; Drive Weight controls its relative share of the base torque budget. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `true` |
| `driveWeight` | `float` | Relative share of base motor torque among driven wheels. At 2 a wheel receives twice the weight of a wheel set to 1; zero excludes it from base allocation. Grip/differential logic can change the final split. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `1`; Minimum: 0 |
| `handbrake` | `bool` | Allows handbrake/parking torque on this wheel. For a typical car, enable on the intended parking-brake axle rather than every wheel automatically. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `false` |
| `mass` | `float` | Native wheel mass in kilograms used in wheel-spin calculations. For a registered wheel, edit this in Wheel Setup; it does not replace the chassis Rigidbody mass. | `25`; Minimum: 1 |
| `radius` | `float` | Tire's rolling radius in metres, used by native wheel contact and wheel-speed calculations. Match half the outside tire diameter; registered wheels take this value from Wheel Setup. | `.34`; Minimum: .05f |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `steering` | `bool` | Allows this wheel to receive vehicle steering. Enable for steering axles; disable for fixed wheels. Steering Multiplier controls its direction and share of the angle. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `false` |
| `steeringMultiplier` | `float` | Per-wheel scale of steering angle; negative values enable opposite-direction steering. | `1` |
| `visual` | `Transform` | Visible wheel mesh rotated and positioned from native suspension and wheel spin. | `None / unassigned` |
| `visualRotationOffset` | `Quaternion` | Rotation correcting the tire mesh's axes relative to the solved wheel pose. Use it for imported meshes whose axle direction differs from the native wheel frame. When registered, edit this value in Vehicle Controller → Wheels → Wheel Setup. | `Quaternion.identity` |
| `visualSuspensionSmoothTime` | `float` | Visual suspension settling time in seconds. Zero follows the native hub directly; tire forces are unaffected. | `.045`; Minimum: 0 |
| `width` | `float` | Full tire width in metres. Used by tire contact sampling, supplemental tire collisions and Scene previews. For a registered wheel, edit Width in Vehicle Controller → Wheels → Wheel Setup and apply configuration. | `.2`; Minimum: .02f |

## WheelDynamics

Applies wheel rotational behavior including airborne losses.

**Source:** `Runtime/Physics/Wheels/WheelDynamics.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `airborneSpinHalfLife` | `float` | Seconds for an unpowered airborne wheel to lose half its spin speed from air damping. Increase to let lifted wheels spin longer; decrease to slow them sooner. | `2`; Minimum: .1f |

## WheelLift

See [Wheel Lift](../DrivingActions.md#wheel-lift-wheelie) for defaults, units and activation guards.

**Source:** `Runtime/Physics/Wheels/WheelLift.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `angleDamping` | `float` | Damping opposing pitch angular velocity while lift control is active. | `18`; Minimum: 0 |
| `angleStrength` | `float` | Pitch correction strength toward the requested lift angle. | `60`; Minimum: 0 |
| `compensateGravity` | `bool` | Add gravity compensation while lifting supported wheels so their weight does not defeat the requested pitch. | `true` |
| `forceCurve` | `AnimationCurve` | Shape of lift force over normalized action strength. Use it to soften the initial pickup or final release. | `AnimationCurve.EaseInOut(0, 0, 1, 1)` |
| `groundContactGraceTime` | `float` | Time to retain the wheelie angle through brief contact loss, then level for landing. No lift force is applied without support. | `.75`; Minimum: 0 |
| `landingTime` | `float` | Duration in seconds of the controlled lowering phase after the request ends. | `1`; Minimum: .1f |
| `landingTimeout` | `float` | Maximum allowed lowering time in seconds before the action releases its remaining support. | `3`; Minimum: .1f |
| `liftPoint` | `Transform` | Optional world-space force point; overrides wheel selection. | `None / unassigned` |
| `localLiftPoint` | `Vector3` | Used in vehicle local space if no lift wheels are available. | `new Vector3(0, 0, 1)` |
| `maximumForce` | `float` | Maximum upward lift force in newtons at the configured lift point. | `12000`; Minimum: 0 |
| `maximumLiftAcceleration` | `float` | Upward assistance acceleration cap in m/s². Keeps the support wheel loaded during lift. | `8`; Minimum: 0 |
| `maximumRecoveryAcceleration` | `float` | Maximum corrective pitch acceleration in rad/s², including recovery during brief contact loss. | `300`; Minimum: 0 |
| `maximumRoll` | `float` | Maximum allowed roll angle in degrees before wheel-lift assistance starts lowering. | `60`; Range: 0 to 89 |
| `maximumSpeed` | `float` | Highest vehicle speed at which the lift request may remain active. | `55`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumSupportDampingAcceleration` | `float` | Maximum chassis acceleration from support rebound damping in m/s². Descending and airborne motion are not damped. | `15`; Minimum: 0 |
| `minimumSpeed` | `float` | Lowest vehicle speed at which wheel lift can start or remain held. Slowing below it starts controlled lowering. | `2`; Speed field; stored in m/s, displayed in the selected speed unit |
| `pitchSupport` | `WheelLiftPitchSupport` ([fields](Physics.md#wheelliftpitchsupport)) | Counter the nose-up moment of tire-driven acceleration before it produces a large wheelie-angle error. | `new WheelLiftPitchSupport()` |
| `releaseTime` | `float` | Seconds over which the held request fades after release before controlled landing completes. | `.35`; Minimum: 0 |
| `requireGroundContact` | `bool` | Require supporting ground contact to start the lift action. | `true` |
| `requireRunningEngine` | `bool` | Require a running engine before a new lift request is admitted. | `true` |
| `riseTime` | `float` | Seconds over which lift strength rises after activation. | `.5`; Minimum: 0 |
| `safetyAngle` | `float` | Pitch safety angle in degrees beyond which the action stops lifting and requests recovery. | `75`; Range: 0 to 89 |
| `supportReboundDamping` | `float` | Damps separation velocity at the supporting tires while this action is active. Zero disables rebound damping. | `10`; Minimum: 0 |
| `targetAngle` | `float` | Requested front-wheel lift angle in degrees relative to the gravity-level vehicle attitude. | `30`; Range: 0 to 75 |
| `wheels` | `Wheel[]` ([fields](Physics.md#wheel)) | Lift at the average position of these wheels. Empty selects operational steering wheels. | `Empty list` |

## WheelLiftPitchSupport

Bounded pitch support that damps boost-induced wheelie oscillation without replacing native contact forces.

**Source:** `Runtime/Physics/Wheels/Control/WheelLiftPitchSupport.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `compensation` | `float` | Fraction of the pitch moment from measured tire acceleration to counter during supported wheel lift. | `1`; Range: 0 to 1.5f |
| `enabled` | `bool` | Controls enabled for this mechanism. | `true` |
| `maximumDriveAcceleration` | `float` | Maximum longitudinal acceleration used by pitch compensation, in m/s². Contact impulses beyond twice this value are rejected. | `20`; Minimum: 0 |
| `responseTime` | `float` | Seconds to smooth measured acceleration. Filters contact and gear-change noise. | `.08`; Minimum: 0 |

## WheelSetup

Persists collider, geometry, visual and wheel-role authoring data.

**Source:** `Runtime/Physics/Wheels/WheelSetup.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `brake` | `bool` | Allows service-brake torque on this wheel. Disable for a wheel that should free-roll under the main brake pedal. | `true` |
| `brakeMultiplier` | `float` | Multiplies this wheel's service-brake torque. Use lower front/rear values to tune brake balance; zero removes its service-brake contribution. | `1`; Minimum: 0 |
| `caliperRotationOffset` | `Quaternion` | Rotation correcting the brake-caliper mesh's axes in the non-spinning hub frame. It aligns the visual without changing brake strength. | `Quaternion.identity` |
| `caliperTransform` | `Transform` | Optional brake caliper mesh. It follows suspension movement and steering but stays still while the tire spins. | `None / unassigned` |
| `drive` | `bool` | Includes this wheel among wheels receiving propulsion. Enable only on driven axles; Drive Weight controls its relative share of the base torque budget. | `true` |
| `driveWeight` | `float` | Relative share of base motor torque among driven wheels. At 2 a wheel receives twice the weight of a wheel set to 1; zero excludes it from base allocation. Grip/differential logic can change the final split. | `1`; Minimum: 0 |
| `enabled` | `bool` | Includes this wheel in vehicle configuration and simulation. Turn off to disable this wheel entry without deleting its collider or saved settings. | `true` |
| `handbrake` | `bool` | Allows handbrake/parking torque on this wheel. For a typical car, enable on the intended parking-brake axle rather than every wheel automatically. | `false` |
| `label` | `string` | Readable wheel name in the controller's setup list, such as Front Left. It identifies the entry for editing and does not choose its physical side or drive role. | `"Wheel"` |
| `mass` | `float` | Native wheel mass in kilograms, copied during configuration. It affects the wheel's rotational inertia/spin response; chassis mass is set separately in Vehicle Settings. | `25`; Minimum: 1 |
| `radius` | `float` | Tire's rolling radius in metres, from axle centre to the outside tread. It sets native contact geometry and speed/torque conversion; it does not resize the visible mesh. | `.45`; Minimum: .05f |
| `steer` | `bool` | Allows this wheel to receive vehicle steering. Enable for steering axles; disable for fixed wheels. Steering Multiplier controls its direction and share of the angle. | `false` |
| `steeringMultiplier` | `float` | Use negative values for counter-steering axles. | `1` |
| `wheelCollider` | `WheelCollider` | Native wheel collider providing this wheel's suspension, road contact, rotation and tire forces. Assign the collider at the wheel mount, separate from the rotating visual mesh. | `None / unassigned` |
| `wheelRotationOffset` | `Quaternion` | Rotation correcting the tire mesh's axes relative to the solved wheel pose. Use it for imported meshes whose axle direction differs from the native wheel frame. | `Quaternion.identity` |
| `wheelTransform` | `Transform` | Tire/rim mesh moved to the wheel's solved suspension position and rotated for steering and spin. Assign the visual, not the fixed collider mount. | `None / unassigned` |
| `width` | `float` | Full tire width in metres copied to Wheel during configuration. Wider tires spread supplemental contact sampling and collision geometry farther sideways; this does not resize the visible tire mesh. | `.2`; Minimum: .02f |
