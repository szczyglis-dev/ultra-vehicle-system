# Vehicle physics

Ultra Vehicle System combines Unity physics with configurable vehicle mechanics. `VehicleController` owns the chassis `Rigidbody`, reads input, runs the active `DriveProfile` and schedules the installed modules. Wheel vehicles use `WheelCollider` contacts for suspension and tire forces. Flying and water vehicles use their profile's propulsion and support model, with optional wheels for ground contact.

Start with correct geometry and a stable chassis, then tune suspension, propulsion, steering and assists in that order. Effects and visible suspension parts should follow the resulting motion.

## Inspector quick start: a basic driving chassis

1. Select the root with Vehicle Controller. In **Setup**, choose the drive mode and configure mass/centre of mass in **Setup > Configuration**. Fit permanent chassis colliders on this root's Rigidbody hierarchy.
2. In **Wheels > Wheel Setup**, add each WheelCollider and visual, set radius/width/mass and its drive, steering, service-brake and handbrake roles. Apply configuration and establish support using [Suspension](Suspension.md#inspector-quick-start).
3. In **Modules > Engine > Engine**, configure running state, RPM and power/torque for the profile. Add/connect a [gearbox](Gearbox.md#inspector-quick-start) when selectable gearing is wanted. Profile-managed fields are edited at the owning profile, as indicated by their tooltips.
4. Open **Modules > Drive > Brakes** for service/handbrake behavior and **Steering** for steering/handling assistance. Check baseline vehicle steering/braking values under Setup too; the configured wheel roles decide which contacts receive them.
5. Open **Modules > Physics > Friction** for tire grip, then add optional contact/stability helpers only after the basic chassis works. Apply/save and test launch, braking and a turn on a simple flat collider before adding effects.

## Chassis, coordinates and units

Keep the vehicle root at unit scale, with local +Z forward and +Y up. Put model-specific scaling and orientation corrections on visual children. Body colliders define the chassis shape for impacts; wheel contacts provide tire support separately.

| Setting or property | Purpose |
| --- | --- |
| `VehicleController.Body` | The vehicle's physical `Rigidbody`; use it to read velocity or apply additional forces from custom mechanics. |
| `VehicleController.settings.mass` | Chassis mass in kilograms. Configuration applies a minimum of 1 kg. |
| `VehicleController.settings.centerOfMass` | Explicit local center of mass relative to the vehicle root, in metres. |
| `VehicleController.wheelSetup` | Wheel geometry, references, roles and multipliers. |
| `VehicleController.Wheels` | Runtime wheel adapters for the configured vehicle. |
| `VehicleController.SpeedKph` / `VehicleController.SpeedMph` | Speed magnitude in km/h or mph, including lateral and vertical motion. |
| `VehicleController.ForwardSpeed` | Signed velocity along the configured drive direction, in m/s; positive means forward even when engine direction is inverted. |
| `VehicleController.GetSpeed(SpeedUnit unit)` | Speed magnitude in the requested unit. |

New vehicles and demo prefabs use **Rigidbody > Automatic Inertia Tensor**. Unity calculates rotational inertia from the chassis colliders. You can turn this off and edit **Inertia Tensor** and **Inertia Tensor Rotation** for a custom distribution; applying vehicle configuration does not override that choice. When replacing a model or its colliders, start with the automatic calculation instead of carrying a manual tensor over from another vehicle.

Distances and suspension travel use metres, forces use newtons, and torque uses N·m. Speed fields with a unit selector can be authored in km/h, mph or m/s; changing the displayed unit preserves the physical value. See [Speed units](SpeedUnits.md).

A lower center of mass can reduce rollover tendency, but it cannot correct an incorrect wheelbase, intersecting colliders or insufficient suspension travel. Physical passengers and articulated parts have their own bodies and can affect the loaded vehicle's behavior.

## Wheel geometry and contact

Add each wheel to `VehicleController.wheelSetup` and assign its `WheelCollider`, visual, radius, width and mass. Select the steering, driving, service-brake and handbrake roles for that wheel. Each collider must belong to the vehicle's `Rigidbody` and appear only once in the setup.

`WheelCollider` supplies spring/damper support, slip-based tire friction and wheel rotation. Chassis colliders handle body impacts. Ordinary collider friction materials do not replace the tire-friction configuration: use `settings.grip` and `Surface` components to tune tire grip on different ground materials.

Native wheel contact uses a raycast-based approximation. Sharp steps, thin obstacles and high-speed terrain changes may need additional support:

- `ContactEnvelope` adds sampled contact support around the tire's contact region. Configure its ground filtering, sampling and correction limits for the terrain.
- Solid-tire helpers add physical collision support for cases where native wheel contact alone is insufficient.
- Body collision proxies should leave room for normal wheel travel instead of catching the ground before the tires do.

Set up and tune these helpers after the native wheel geometry works on flat ground. See [Tire contact](ContactEnvelope.md), [Tire collision](TireCollision.md) and [Ground surfaces](Surfaces.md).

## Suspension and body support

`Suspension` configures the native wheel springs, damping and travel. Use its fields rather than maintaining a second set of values directly on the same `WheelCollider`.

| Field | What to tune |
| --- | --- |
| `settings.suspensionTravel` | Available suspension stroke in metres. Leave room for compression and extension at the intended load. |
| `Suspension.spring` | Spring stiffness in N/m. Increase it when the intended load compresses the suspension too far. |
| `Suspension.damper` | Damping in N·s/m. Increase gradually to reduce repeated oscillation after the springs support the load. |
| `Suspension.targetPosition` | Normalized native spring target, from 0 to 1. Tune together with travel and loaded ride height. |
| `Suspension.automaticForceApplication` | Enables placement of wheel-force application points relative to the center of mass. |
| `Suspension.forceOffsetBelowCenterOfMass` | Offset used by automatic force application, in metres. |
| `Suspension.degressiveDamping` | Limits the growth of damping force at high suspension stroke speeds. |
| `Suspension.damperBlowoffSpeed` | Stroke-speed threshold for degressive damping, in m/s. |
| `Suspension.arcadeBumpDamping` | Optional assistance that damps excessive upward body motion while the wheels remain sufficiently supported. |

First check the resting vehicle on level ground, then braking, cornering and a small bump. Add `AntiRoll` after basic suspension support works. A visual `ShockAbsorber` or linkage does not provide physical support unless its corresponding physics override is configured. Use only one shock physics override per wheel.

Disabling a setup component does not necessarily undo values already written to native physics components. Reconfigure the vehicle when changing persistent setup. See [Suspension setup](Suspension.md) and the [suspension scripting reference](Scripting/Suspension.md).

## Propulsion, brakes and steering

Direct wheel driving uses `settings.motorTorque` as a wheel-torque budget distributed across driven wheels. `settings.topSpeedKph` supplies a soft drive-torque fade; it does not forcibly clamp chassis velocity. Descents, impacts and external forces can therefore carry the vehicle beyond that speed.

With a gearbox, engine torque and RPM, gear ratios, drivetrain efficiency and configured power or acceleration limits determine the available wheel torque. Optional clutch and flywheel behavior adds coupling and rotational inertia. `Differential` modes redistribute or couple axle torque; they are not exact constraints on wheel angular velocity.

`Brakes` applies braking through the configured wheel roles and multipliers. `settings.brakeTorque` controls the service-brake torque budget. Set up service brakes and handbrakes deliberately, especially for vehicles with several axles.

The drive profile's **Steering Speed Limit Enabled** switch is shared by every vehicle type. It gates the Steering module's speed-sensitive angle reduction and speed/grip lateral-acceleration cap. It defaults to enabled for existing non-aircraft behavior and disabled for fixed-wing aircraft. Turning it off retains minimum turning radius, Ackermann geometry and steering smoothing. With it enabled, the module's existing options and analog-input policy still apply.

`Steering` drives the configured steering wheels using `settings.steeringAngle`, steering response and per-wheel multipliers. `Steering.speedSensitiveSteering` can reduce steering authority with speed; `Steering.advancedSteeringGeometry` enables the optional radius/grip limits and Ackermann geometry. Negative per-wheel steering multipliers support counter-steering axles.

Tune the visible steering-wheel travel separately from road-wheel angles. See [Vehicle tuning](VehicleTuning.md), [Gearbox](Gearbox.md), [Clutch](Clutch.md) and [Drive dynamics](Scripting/DriveDynamics.md).

## Driving assists and other vehicle types

`TractionControl` and `DrivingAssists` provide configurable slip and stability assistance. Establish suitable geometry, grip and suspension before increasing assistance. `MotorcycleBalance` provides assisted balance and lean for motorcycles.

The active `DriveProfile` determines the vehicle's movement model. Hover, aircraft and water profiles apply their own support and propulsion behavior; changing only a wheeled vehicle's torque settings does not turn it into a flying or floating vehicle. See [Drive profiles](DriveProfiles.md), [Aircraft](Aircraft.md), [Water](Water.md) and [Tracked vehicles](Tracked.md) for the corresponding setup.

These systems are intended for configurable game handling. Motorcycle balance, hover support, aerodynamics and buoyancy are assisted gameplay models rather than engineering simulations.

## Collisions and stabilization

Use `Stabilization` to damp excessive spin during jumps and tumbling, and `Collisions` to supplement native crash rebound and body sliding friction. Optional **Auto Righting** is disabled by default and applies a bounded recovery torque while a slow vehicle on its side touches the ground; roof recovery is excluded. See [Collisions and stabilization](CollisionsAndStabilization.md).

## Reverse longitudinal propulsion

Enable **Invert Drive Direction** on `Engine` when positive throttle must propel the vehicle toward local -Z. `Engine.invertDriveDirection` reverses wheel torque and built-in longitudinal thrust while keeping forward/reverse gear selection and throttle magnitude unchanged. Braking and direction selection use the configured direction through `VehicleController.ForwardSpeed`.

`Engine.DriveDirectionSign` and `VehicleController.DriveDirectionSign` return -1 when inverted and +1 otherwise. Custom drive profiles can multiply longitudinal force by the vehicle's sign. The switch does not rotate meshes, colliders, steering axes or aerodynamic control frames; keep those aligned with the intended handling setup. Leave it disabled on the supplied Car, whose FBX already faces +Z.

## Apply and inspect changes

1. Configure the chassis and `wheelSetup` outside Play Mode.
2. Click **Apply vehicle configuration** in the controller Inspector. From code, call `VehicleController.ApplyConfiguration()` or use `VehicleController.TryApplyConfiguration(out string error)` to handle validation failure.
3. Check the controller's **Live** values and the actual wheel contacts. Distinguish missing input from missing traction or a drivetrain limit.
4. Compare rest, acceleration, braking, reverse, a tight turn, a fast turn, a slope and a landing with the intended load.
5. Save persistent changes outside Play Mode and check a fresh instance of the vehicle.

When tuning high-speed collisions or many articulated bodies, review Unity's fixed timestep, collision-detection mode and solver settings for your scene. Smaller timesteps and more solver work cost CPU time; choose settings using the target platform and expected vehicle count. See [Performance](Performance.md) and [Troubleshooting](Troubleshooting.md).
