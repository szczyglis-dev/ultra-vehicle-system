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

**Collisions > Landing Traction Loss** is enabled by default. After at least **Landing Minimum Air Time** (0.15 s) without wheel support, a grounded-profile vehicle landing above **Landing Minimum Speed** (1.5 m/s relative to the contact surface) briefly loses tire grip. Full response is reached at **Landing Full Response Speed** (4.5 m/s). **Landing Grip Recovery Time** (0.85 s) smoothly restores grip and stability assistance.

At full response, **Landing Forward Grip** retains 0.45 of longitudinal grip and **Landing Sideways Grip** retains 0.3 of lateral grip. **Landing Rear Grip Bias** releases rear lateral grip slightly further, allowing the tail to move. Grip reduction is independent of steering angle and sway direction: straight-wheel landings also lose longitudinal and sideways grip. These multiply the existing surface, handbrake, tracked-steering and burnout grip through `Friction`, rather than overwriting tire curves independently. Install/enable `Friction` for the tire-grip effect. Steering stability authority follows the temporary lateral grip multiplier so it does not immediately cancel the landing slide; the saved assist settings stay intact.

**Landing Lateral Sway** (0.45 m/s maximum added lateral speed) and **Landing Yaw Sway** (7 degrees/s maximum additional yaw change) provide a small ground-contact push spread over 0.12 s. Intensity follows normal landing speed and vehicle motion relative to the surface. Direction follows existing lateral momentum, bank, yaw and which side touches first. A symmetric straight landing receives no arbitrary sideways kick. Reverse motion mirrors the yaw response. Very slow landings do not receive a directional shove.

The response is bounded gameplay assistance, separate from native solver impulses and the vertical spring rebound. It is not an exact tire-load or deformation simulation. Dynamic landing surfaces receive the opposite added impulse and torque. Pushes stop on wheel contact loss; reduced grip continues to fade during a brief rebound, and the rebound cannot rearm the effect until stable support and recovery complete. Side/roof landings and air/water profiles are excluded. Teleport, reconfiguration and disabling Collisions clear the response and refresh grip through the existing Friction policies.

For a stronger loose landing, lower Landing Sideways Grip or increase the recovery time gradually. For more body motion, use Suspension's Landing Response independently. Setting either sway value to zero removes that added movement; disabling Landing Traction Loss restores normal grip and stability authority.

On movable supports, the landing sway shares the support's effective mass and inertia and distributes opposite impulses among the contacted bodies. A light box therefore receives a small relative response instead of a chassis-mass kick.

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

The controller's copied `Impacted` event supplies contact position, normal, relative velocity and native impulse. `Collisions` excludes self contacts, missing manifolds, WheelColliders and solid-tire helpers. Separate hinged-panel bodies continue to send their hits to Damage and do not receive a second artificial chassis impulse.

**Minimum Impact Speed** uses normal closing speed in m/s, so sliding speed alone does not trigger a crash response. **Restitution** sets a target normal separation speed as a fraction of incoming normal speed. **Maximum Rebound Speed** caps the additional response target. Existing separation from the Unity solver or a bouncy physics material is counted, and only missing restitution is supplied, bounded by the real normal collision impulse. Setting restitution to zero adds no stopping/rebound impulse. This limit does not cap native PhysX bounce or native angular motion.

The restitution impulse acts at the actual contact, with effective mass derived from chassis mass and inertia. Off-centre impacts can produce yaw, pitch, roll and rear lift depending on contact height and position relative to the center of mass. **Impact Response** enables this correction. **Maximum Angular Kick** limits its additional angular change in degrees/s; reducing it also reduces rebound at contacts with a long lever arm. **Impact Cooldown** prevents closely repeated callbacks from stacking artificial rebound. Dynamic obstacles receive the equal opposite impulse.

Under **Modules > Physics > Collisions > Crash Weight Transfer**, supported heavy impacts produce a short pitch/roll and lift response. **Crash Ground Pivot** biases severe hits toward keeping the struck end low while the opposite end rises; set it to zero to follow only the real contact lever. **Crash Minimum Leverage** prevents a hit near center-of-mass height from becoming visually flat. **Crash Maximum Lift Speed** caps the additional upward speed (zero disables lift). **Crash Rotation Per Speed** and **Crash Maximum Rotation** control rotation strength. **Crash Attack Time** controls rise to peak force (default zero: immediate onset on the next physics step); **Crash Release Time** controls its gradual fade (default 0.14 seconds). Both times shape one bounded impulse budget, so a longer tail does not add energy. Times are captured at impact; both zero deliver the response in one physics step. This envelope controls force delivery, not an animated return of the chassis pose. The actual normal impulse, mass and inertia determine the response; **Crash Energy Fraction** bounds the energy added to the chassis and a movable collision partner. Pending impulses stop when ground support is lost.

In the same section, **Crash Damper Multiplier** and **Crash Suspension Recovery** control temporary damping reduction. **Crash Yaw Variation** follows off-centre contact direction. **Crash Centred Yaw** optionally breaks the perfect symmetry of severe near-centred hits, alternating sides between crashes; this is a presentation effect, not spontaneous yaw from a physically perfect symmetric impact. Set it to zero for no added centred yaw. Teleport, reconfiguration and disable clear pending responses. Landing traction loss remains independent.

Keep native collider restitution low when tuning this component. Start around the default restitution of 0.12 and maximum rebound speed of 3 m/s. Real crush/deformation energy absorption remains an approximation: visual mesh deformation does not change the chassis collider. Correct chassis geometry, mass, center of mass, collision detection and Unity solver settings remain essential.

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
