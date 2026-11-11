# Collisions and stabilization

`Collisions` adds configurable crash rebound and body sliding friction. `Stabilization` limits excessive airborne rotation and optionally helps a vehicle on its side return to its wheels. Both are independent Physics modules; `Damage` continues to handle dents, damage accumulation and detached parts. Disabling damage does not disable physical crash response.

Profile creation presets install both modules. The demo vehicle prefabs include them; the Demo scene inherits the components from those prefabs. Add them to an existing vehicle through **Add Component > UltraVehicleSystem > Physics**, or the controller's module picker, then apply vehicle configuration. No damage parts, extra colliders or per-frame raycasts are required.

## Inspector quick start

1. Select the root and open **Modules > Physics**. Expand **Collisions** and **Stabilization**, or add them through **Add module...**. Damage and sound use separate components.
2. In Collisions, configure **Impact Response**, **Crash Weight Transfer**, **Body Sliding** and wheel-landing grip/sway independently.
3. For wheel compression/rebound, open **Modules > Drive > Suspension**. Keep **Coordinate Landing Response** in Collisions enabled when coordinating grip recovery with smooth suspension landing.
4. In Stabilization, begin with airborne damping; enable optional **Auto Righting** only for wanted side recovery. Apply/save, then compare a four-wheel landing, nose-first landing and wall impact.
5. Configure recordings under **Effects > Audio > Damage Audio**, following [Audio](Audio.md#inspector-quick-start-collision-and-landing-sounds). Physical response settings do not choose the clip.

## Stabilization in flight

The damping and automatic righting normally run only for profiles whose `Medium` is `Grounded`, including wheeled, motorcycle and tracked vehicles. **Affect Other Profiles** explicitly opts into damping aircraft, water and hover vehicles; leave it off when their profiles supply angular control.

The module reads current native wheel support and recent body contacts recorded by the controller. After losing all support for **Airborne Delay**, it applies inertia-aware opposing angular impulses. **Airborne Damping** controls local pitch, yaw and roll separately, in inverse seconds. **Maximum Spin** is a soft threshold in degrees/s: **Overspeed Damping** progressively increases resistance above it. **Maximum Deceleration** limits angular slowdown in degrees/s². Normal flight retains translation and momentum; there is no forced pose, hard angular clamp or automatic leveling with the recovery option disabled.

Start with the supplied mild pitch/roll damping and weaker yaw damping. Increase overspeed damping for violent crash spins; increase ordinary damping only if normal jumps still rotate too freely. Small wheel hops are protected by the delay. Passive damping can remove rotational energy; it does not simulate aerodynamic body lift.

To suspend vehicle forces and assistance, see [Release and restore all vehicle forces](DriveProfiles.md#release-and-restore-all-vehicle-forces).

## Landing on the wheels

`Suspension` provides a separate **Landing Response**, enabled by default for grounded profiles. It temporarily reduces damping and releases the expansion limiter so landing load compresses the wheels and the springs produce a smooth rebound. The ordinary response scales with landing speed and fades back to normal without an added launch impulse. For actual whole-vehicle hops after wheel touchdown, use Suspension’s default-enabled [Landing Ground Bounce](Suspension.md#optional-whole-vehicle-landing-bounce), which adds bounded, diminishing rebound pushes for grounded profiles and can be disabled in the Inspector. Tune its minimum flight time/speed, full-response speed, damper multiplier and duration in Suspension. See [landing compression and rebound](Suspension.md#landing-compression-and-rebound).

## Brief loss of grip and directional sway

**Collisions > Landing Traction Loss** briefly reduces tire grip after a wheel landing, then restores it over **Landing Grip Recovery Time**. Set the minimum air time and impact speed to exclude small bumps; **Landing Forward/Sideways Grip** and **Landing Rear Grip Bias** set the remaining grip. The effect requires `Friction` and applies to grounded profiles landing on their wheels.

**Landing Lateral Sway** and **Landing Yaw Sway** add a bounded response following the vehicle's existing motion and contact direction. Set either to zero to disable it. Suspension rebound is configured separately in [Suspension](Suspension.md#landing-compression-and-rebound). See the [Collisions settings](InspectorReference/Physics.md#collisions) for all thresholds and defaults.

## Optional return to the wheels

**Auto Righting** defaults to **false**. Enable it to apply a smooth spring-and-damper torque toward gravity up when a slow vehicle on its side has a ground-like body contact. It never teleports or directly sets rotation.

- **Righting Delay** requires sustained eligible contact before assistance begins.
- **Righting Minimum Tilt** starts recovery on a vehicle resting on its side; recovery then continues until tilt falls below 5 degrees.
- **Righting Maximum Tilt** defaults to 125 degrees and is limited to 135 degrees. Assistance stops beyond it; roof landings are excluded.
- **Righting Maximum Speed**, in m/s, blocks assistance during fast sliding or tumbling.
- **Righting Strength** and **Righting Damping** tune the angular spring and resistance.
- **Righting Maximum Acceleration**, in degrees/s², bounds the push.

Losing ground contact, falling beyond the maximum tilt, exceeding the speed limit, disabling recovery or disabling the component clears recovery progress. Terrain, chassis shape, constraints and overhead obstacles can prevent recovery. This is optional gameplay assistance and can add energy; passive airborne stabilization remains independent.

## Crash rebound and rotation

**Collisions > Impact Response** adds contact-point rebound above **Minimum Impact Speed**. **Restitution** sets its strength; **Maximum Rebound Speed**, **Maximum Angular Kick** and **Impact Cooldown** limit the additional response. Native PhysX collision response remains active.

**Crash Weight Transfer** adds a short pitch/roll and lift response to supported heavy impacts. Tune its rotation, lift and energy limits, then **Crash Attack/Release Time** for onset and fade. **Crash Damper Multiplier** and **Crash Suspension Recovery** control temporary suspension softening; set **Crash Centred Yaw** to zero to disable added yaw on centred hits.

Keep native material restitution low while tuning. Correct collider geometry, mass and centre of mass remain essential. See the [Collisions settings](InspectorReference/Physics.md#collisions) for the full parameter reference.

## Sliding on the side or roof

**Body Friction** defaults to 0.8 for stronger deceleration when sliding on the side or roof. It adds contact friction only during sustained body sliding, above **Minimum Body Tilt**, on a ground-like contact relative to gravity. Wheel support and wall scrapes are excluded. The impulse opposes relative tangential point velocity, is bounded by normal contact impulse times the configured coefficient, and cannot reverse that point velocity in one correction. Moving/dynamic surfaces are handled relative to their motion and receive the opposite impulse.

This supplements native collider-material friction. Use moderate coefficients to avoid counting strong friction twice. It does not apply airborne drag, prevent all rolling, or artificially glue a crashed vehicle to the road.

## Measurements and scripting

`vehicle.sensors.LocalAngularVelocity` reports local pitch/yaw/roll rates in radians/s; `LocalSpinDegrees` reports degrees/s, and `SpinDegreesPerSecond` is total angular speed. `HasBodyContact` means a body contact has been recorded since the last reset; inspect `LastBodyContactTime` to determine freshness. `BodyContactNormal` is the last copied world normal. Contact measurements work independently of the Collisions component and are invalidated by the controller's normal sensor reset/teleport lifecycle.

`Stabilization.IsAirborne` and `IsRighting` expose the module's current decision. Sensors remain measurements: they do not apply forces. Mechanics use current Rigidbody pose/velocity and wheel support, rather than relying on telemetry sampled after the previous mechanics pipeline. Direct-control/kinematic vehicles do not receive these physical forces.

See [the Inspector settings](InspectorReference/Physics.md#collisions), [physics sensors API](API/PhysicsSensors.md), [vehicle physics](Physics.md) and [damage](Damage.md).

### Collision effect notifications

`VehicleController.Impacted` supplies the existing copied collision context. DamageAudio subscribes directly, ignores self contacts and applies its own audio thresholds and material profiles. Collisions configures physical response only; it does not publish effect IDs. Turning its physical response off does not silence collision effects.

## Overturn detection

Stabilization also detects sustained tilt using **Detect Overturn**, **Overturn Angle**, **Overturn Delay** and **Recovery Angle**. Read `IsOverturned` or subscribe to `Overturned(Telemetry)` and `Recovered(Telemetry)`. Detection works independently of Auto Righting and Affect Other Profiles. Each transition includes its copied vehicle pose, speed and other telemetry readings.

For vehicles whose tires reach an obstacle before the chassis, enable **Crash From Wheel Impacts** together with **Crash Weight Transfer**. This is enabled in the demo motorcycle and Monster Truck. Only near-vertical obstacle contacts contribute: ordinary wheel support and landings remain separate. Simultaneous tire contacts against the same obstacle contribute to one impact, so both front wheels affect its strength and direction. Actual tire impulse, energy limits and the shared impact cooldown still apply.
