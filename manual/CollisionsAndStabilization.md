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
- **Righting Build Time** smoothly increases torque after that delay; use a positive duration for a gradual lift.
- **Righting Contact Grace** lets an active recovery bridge short support gaps while rolling from the chassis onto the tires. It cannot start recovery in flight. A longer gap stops the assistance and restarts its delay and buildup. Airborne leveling and damping yield while this recovery is active.
- **Righting On Wheel Support** also accepts usable tire support from below, allowing assistance before the chassis rests on its side.
- **Righting Roll Only** corrects bank around local Z without correcting pitch or heading.
- **Righting Minimum Tilt** starts recovery on a vehicle resting on its side; recovery then continues until tilt falls below 5 degrees. Roll-only recovery also waits for bank velocity to settle.
- **Righting Maximum Tilt** defaults to 125 degrees and is limited to 135 degrees. Assistance stops beyond it; roof landings are excluded.
- **Righting Maximum Speed**, in m/s, blocks assistance during fast sliding or tumbling.
- **Righting Strength** and **Righting Damping** tune the angular spring and resistance.
- **Righting Maximum Acceleration**, in degrees/s², bounds the push.

The motorcycle demo and motorcycle authoring defaults enable Auto Righting, wheel support and roll-only correction. Recovery starts at 65 degrees, stays eligible up to 100 degrees and 12 m/s, waits 0.15 seconds, then builds torque over 0.6 seconds, with 0.25 seconds of support-gap grace. Disable Auto Righting to opt out. Driver ejection suspends this help while Motorcycle Balance suppresses riding assistance. An active Auto Righting retains roll control until the supported motorcycle is within 15 degrees of upright. Motorcycle Balance then resumes roll control and Auto Righting ends in that same physics step. Stabilization runs after riding balance in the Balance phase, so the two controllers do not apply competing roll springs. Supported riding also excludes airborne leveling and damping.

Losing ground contact beyond Contact Grace, falling beyond the maximum tilt, exceeding the speed limit, disabling recovery or disabling the component clears recovery progress. Terrain, chassis shape, constraints and overhead obstacles can prevent recovery. This is optional gameplay assistance and can add energy; passive airborne stabilization remains independent.

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

## Vehicle cargo

Add **World > Cargo > Vehicle Cargo** to a Rigidbody item and assign its **Vehicle** (or initially parent it under the vehicle). **Free** (`Dynamic`, the default) uses normal gravity, friction and tumbling: no attraction or upright correction, and cargo can fall out. **Vehicle Response** defaults to zero to prevent cargo pushing its carrier; **Override Carrier Material** is off, preserving normal physics materials.

Choose **Secured** for fixed placement, **Spring** for an elastic mount, or **Tethered** for a slack rope that only pulls beyond **Tether Length**. **Attachment > Anchor** is optional; without one, the captured carrier placement is used. Tune stiffness, damping, force limits and the local attachment point. Rotation remains free unless **Align Rotation** is enabled; distance/force/torque thresholds can break the attachment. **Reaction Scale** optionally transfers attachment forces to the anchor body, independently of contact response.

**Collisions** excludes selected carrier groups, layers, individual colliders or whole hierarchies; default exclusions cover carrier wheels. `SetMode`, `SetAnchor`, collision setters and `BreakAttachment` apply at runtime. `Release()` also clears carrier ownership. Call `RefreshBinding()` after changing shapes, or `RefreshCollisionFilters()` after editing collision lists directly. The demo Military 6x6 has an open compound-collider bed with free cargo. See [VehicleCargo API](API/CollisionsAndStabilization.md#vehiclecargo) and [Inspector settings](InspectorReference/World.md#vehiclecargo).

## Optional airborne leveling

Enable **Stabilization → Airborne leveling → Auto Level Airborne** for bounded roll recovery around the vehicle-local longitudinal Z axis during jumps. It supports cars and motorcycles, builds torque smoothly from the start of flight over `airborneDelay`, and stops at wheel/body contact. Tune spring strength, damping, acceleration cap and the eligible tilt range; the default eligible range reaches 170 degrees of bank. Heading and translational flight velocity are not directly corrected. The motorcycle, bicycle and scooter demo prefabs enable this option.

**Prevent Outward Air Roll** is enabled by default when using airborne leveling: manual sideways input can help return toward upright but cannot deepen the bank, including retained smoothed input after crossing upright. Forward/backward input remains independent. Disable this checkbox for unrestricted manual airborne roll; rider roll then reduces automatic leveling. Automatic assistance does not correct local X pitch or local Y yaw; forward/backward rider input retains its own airborne control. Driver ejection suspends leveling when Motorcycle Balance suppresses riding assistance. **Auto Righting** remains a separate, ground-contact option.

## Motorcycle bank on slopes

In **Motorcycle Balance → Ground Assist**, enable **Reduce Lean On Slopes** to taper both the requested bank and the physical world-bank boundary as terrain gets steeper. The default transition starts at 5 degrees and reaches **Slope Lean Minimum Scale** (`0.2`) at 45 degrees. **Slope Lean Response Time** defaults to `0.35` seconds to smooth changes of terrain and filter short bumps. Handlebar steering remains available without waiting for the reduced bank, while the bank contribution to turning fades. The motorcycle, bicycle and scooter demo prefabs enable this option.

## Custom wheel and body collision handling

Derive from `VehicleCollisionHandler` and attach the component to the target object or an ancestor of its colliders. Enabled handlers automatically register their non-trigger child colliders. No vehicle prefab changes or global event subscription are needed. Both existing wheels and subsequently enabled wheels receive the rule.

- Override `ExcludeWheelSupport(Collider target)` to return `true` for shapes that a vehicle should strike rather than climb. The shared exclusion applies to native WheelCollider suspension, solid tire support and ContactEnvelope/landing queries. Chassis contact remains physical. This rule is sampled at registration and applies to all UVS vehicles; it is not a per-contact notification.
- Override `HandleBodyCollision(VehicleController vehicle, Collision collision, bool entering)` for chassis and physical tire-body contacts. `entering` distinguishes entry from stay. Return `false` to continue normal handling. Return `true` after handling a contact to stop lower-priority handlers and standard package processing for that pair: vehicle collision/impact notifications, damage fed by those notifications/hinged-part relays, body crash/sliding assistance, panel impact-unlatching and supplemental tire contact observation. Other targets and other collider pairs remain unaffected.
- Higher `CollisionPriority` runs first. Equal priorities retain registration order. A body callback is dispatched once per vehicle, self/target collider pair, entry/stay phase and physics step even when several package modules observe the native callback. Copy values out of `Collision` before retaining them; Unity may reuse it.
- Call `RefreshCollisionColliders()` after adding/removing colliders or changing priority. Use `RefreshWheelSupport()` when only support admission changes; it resamples the cached shapes without rebuilding body hooks. Disabling/destroying the handler releases its registrations. If overriding `OnEnable` or `OnDisable`, call `base` exactly once.

Body callbacks run on the main thread **after the native physics solve**. Returning `true` claims package processing; it does not erase the already solved physical impulse, ignore the chassis collider or prevent unrelated Unity `OnCollision...` components from running. For native one-way ragdoll response the existing `RagdollCollisionHelper` contact modifier remains responsible. Do not use these callbacks to teleport objects out of penetration or repeatedly add a second copy of the native impact impulse.

Example: exclude soft tagged/component-marked targets from wheel support and route their body impacts to your component. Define the `SoftObstacle` tag first. Save these two classes as separate scripts, then add `SoftObstacleCollision` beside/above the target colliders. Remove the tag check if you only use components.

<!-- example: SoftObstacleCollision.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

public class CustomImpactReceiver : MonoBehaviour
{
    public int HitCount { get; private set; }

    // Replace this body with your animation, gameplay or damage response.
    public virtual void ReceiveVehicleImpact(VehicleController vehicle, Collision collision)
    {
        HitCount++;
        Debug.Log($"Hit by {vehicle.name} at {collision.relativeVelocity.magnitude:F1} m/s", this);
    }
}

public class SoftObstacleCollision : VehicleCollisionHandler
{
    public override int CollisionPriority => 100;

    public override bool ExcludeWheelSupport(Collider target)
        => target.CompareTag("SoftObstacle") || target.GetComponentInParent<CustomImpactReceiver>();

    public override bool HandleBodyCollision(VehicleController vehicle, Collision collision, bool entering)
    {
        var receiver = collision.collider.GetComponentInParent<CustomImpactReceiver>();
        if (!receiver && !collision.collider.CompareTag("SoftObstacle")) return false;
        if (entering && receiver) receiver.ReceiveVehicleImpact(vehicle, collision);
        return true; // Claim stay too; do not reapply the entry animation/damage every step.
    }
}
```

`RagdollCollisionHelper` uses this same support hook for mannequin colliders. Standing bones remain hittable by the body but cannot become a tall suspension support surface. Ragdoll activation alone does not restore wheel support: the live skeleton must first collapse below 0.9 m in gravity-up height (scaled by the helper root). Once native contacts confirm support from below and the initial moving-body push has ended for 0.2 s, native wheel/tire support returns, so subsequent vehicles can physically run over the fallen body. After admission, run-over contacts keep support enabled rather than switching it off whenever a vehicle touches the ragdoll. A 1.0 m release boundary avoids toggling while a limb bounces; recovery to a standing or seated pose excludes support again. No extra ground raycasts are used. Existing knockdown prediction, native ragdoll contacts, damage scaling and impact audio continue normally because the helper does not claim body processing. Detached damage parts also use the same underlying support-exclusion service. Independent owners hold separate leases; releasing one rule cannot restore another rule's excluded wheel pair, and the final release restores the original ignore state.

For presentation-only admission keep using `IDamageContactFilter`: it filters sound/visual feedback rather than taking ownership of physical collision processing. The new hook does not replace that narrower contract.
