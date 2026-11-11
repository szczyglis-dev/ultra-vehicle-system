# Seats

A seat defines the occupant's position, attachment and body support. This page covers seated fitting, restraints, rider support and collision response. Create the seat/body association in [Passengers](Passengers.md) first. Configure hand and foot targets in [Handles](Handles.md), and prepare the character's joints in [Human anatomy](HumanAnatomy.md).

## Inspector quick start

1. Select the root and open **Vehicle Controller > Seats**. Enable passengers if missing and use **Add passenger seat**, or select an existing seat child in the Hierarchy.
2. Assign its prepared **Passenger Seat > Body** or **Passenger Seat > Body Prefab** and choose the passenger controller/attachment policy described in [Passengers](Passengers.md). Begin with one occupant; an arbitrary character mesh is not automatically a configured ragdoll.
3. Create/position the **Passenger Seat > Spine Anchor** at the seated pelvis origin and drag it into the field. Use the seat's pose/preview tools to fit the character before raising physical restraint strengths.
4. Configure limb modes and assign hand/foot anchors or handles using [Handles](Handles.md). Set the collision/tilt response and g-force policy on the seat independently of its initial pose.
5. Save scene/prefab references and test boarding or initial occupancy, normal driving, one hard landing and exit. Tune support only after verifying that each reference belongs to the intended seat/vehicle.

## Find a setting in the seat Inspector

| Task | Full Inspector path |
| --- | --- |
| Choose the character/controller | Passenger Seat > Body / Body Prefab / Passenger Controller |
| Fit the main origin and immediate exit | Passenger Seat > Spine Anchor / Exit Anchor |
| Set automatic spawning | Passenger Seat > Spawn On Start (below Parent While Seated), and Passengers > Spawn On Start |
| Assign a hand or foot | Passenger Seat > Hands, feet and head > Left Hand / Right Hand / Left Foot / Right Foot > Mode / Handle / Anchor |
| Tune a limb | Passenger Seat > Hands, feet and head > [limb] > Advanced / Fine tuning |
| Configure its damage release | Passenger Seat > Hands, feet and head > [limb] > Damage feedback |
| Select its release surfaces | Passenger Seat > Hands, feet and head > [limb] > Release colliders |
| Support the head | Passenger Seat > Hands, feet and head > Head > Hold Head Forward (then Head Pitch / Head Spring / Head Damper / Maximum Head Torque) |
| Configure entry/release exclusions | Passenger Seat > Settings > Colliders and collisions |
| Configure auto-eject and body surfaces | Passenger Seat > Settings > Damage / Auto-eject > [option] / Eject colliders |
| Tune harness/body restraints | Passenger Seat > Settings > Fine Tuning > [option] |
| Configure force protection | Passenger Seat > Settings > Force limits > [option] |
| Add independent attachments | Passenger Seat > Custom supports > Transform Supports / Joint Supports > [item] |
| Adjust the authored seated fit | Passenger Seat > Seated pose > [position / rotation] |
| Bind occupancy/release events | Passenger Seat > Signals and callbacks > [event] |

Force limits is the last Settings group. Transform/Joint Supports use native lists with add/remove/reorder. Anatomical joint entries on **Humanoid Passenger > Anatomical Joints** display **Joint Id** when nonempty, otherwise **Element 0**, **Element 1**, etc. IDs are case-sensitive; use descriptive PascalCase names such as `HipsToSpine`.

## Fit the seated body

1. Use a pre-placed prepared body for initial fitting so the seat preview can show the actual character proportions.
2. Put **Passenger Seat > Spine Anchor** at the intended seated pelvis origin, facing along the occupant's seated forward direction. It is not a camera position or a marker at the top of the spine.
3. Adjust pelvis/backrest fit with the seat's **Passenger Seat > Seated Pose** tools. Check that hips sit above the cushion and the torso has space to move.
4. Place the hands and feet near their natural destinations before applying strong restraints. Bent elbows/knees need room through the full control range.
5. Use **Preview seated pose** and inspect from the front, side and top. Check both sides rather than mirroring a target visually without checking orientation.
6. Test stationary in Play Mode, then accelerate, brake and steer. For occupied support changes, use **Apply seated tuning** to rebuild affected restraints. Save persistent tuning outside Play Mode.

A target beyond limb length cannot be corrected with more spring force. Adjust the seat, contact or model proportions first. Anatomical joint limits remain on the character's saved joints; the seat does not regenerate them.

## Main attachment and rigid transform supports

**Passenger Seat > Attachment Mode** selects the main seating origin's `Spring` (default) or `Parent` independently from the passenger controller. A physical humanoid using Parent keeps its ragdoll active: only the pelvis is attached to Spine Anchor; torso springs are omitted and limb settings remain independent. **Passenger Seat > Parent Make Kinematic** (default true) parks only the held pelvis Rigidbody, not the remaining ragdoll. Turn it off to retain that Rigidbody's dynamic simulation too. Characters without a physical rig use controlled root attachment; Animator and Animator + IK still select animation ownership.

**Passenger Seat > Affect Vehicle Physics** is enabled by default. Disable it for one-way seated support: vehicle motion still drives the physical passenger, but the passenger's torso, hand, foot and head supports do not push or rotate the chassis. Contacts with the passenger's own vehicle are excluded while seated, including released limbs; after exit/ejection the usual release collision settings apply again. Other vehicles and world obstacles keep their existing collision rules. This does not freeze the ragdoll or change the vehicle mass. You can also change `seat.affectVehiclePhysics` from code while occupied. Custom controllers own their physics and must implement an equivalent policy themselves.

**Passenger Seat > Parent Position Offset** and **Passenger Seat > Parent Rotation Offset** use Spine Anchor local coordinates/degrees. For non-physical Spring attachment, **Passenger Seat > Attachment Spring** and **Passenger Seat > Attachment Damper** drive a world-space simulated root pose; physical main springs retain the existing restraint tuning. Changing modes through `SetAttachmentMode` keeps occupancy. **Custom** still leaves the automatic main attachment to application code, but explicitly configured additional supports apply with any controller, including Custom.

Each **Passenger Seat > Custom supports > Transform Supports** entry independently selects **Mode: Spring / Parent**, plus **Body Transform**, **Anchor**, **Active**, **Preserve World Pose**, **Position Offset** and **Rotation Offset**. Mix modes freely with either main attachment mode, with animation, without a ragdoll or with an active ragdoll. Parent is the default for a new transform entry.

- **Parent** actually reparents the transform and enforces its anchor-local pose after ordinary animation/IK. **Make Kinematic** optionally makes only that transform's Rigidbody kinematic while held (default true); its previous setting is restored on release. Disable it to retain dynamic simulation while enforcing the pose. Other bones keep their own physics state.
- **Spring** preserves the original hierarchy. A dynamic Rigidbody receives position forces and rotation torques during passenger physics updates. A kinematic Rigidbody or plain Transform follows a simulated spring pose after animation, so Rigidbody and ragdoll are optional. **Spring / Damper** and **Rotation Spring / Rotation Damper** tune the response; the transform simulation uses unit virtual mass. Spring pose integration caps catch-up at 0.25 seconds per rendered frame.

**Follow Anchor Rotation** is enabled by default. Disable it to capture the target world rotation at attachment/refresh instead of following subsequent anchor rotation. Parent holds that world orientation; both Rigidbody and transform Spring modes spring toward the same fixed world orientation. Preserve World Pose and Rotation Offset still determine the initial target. Position always follows the anchor, including rotation of its local position offset. Refresh recaptures the reference rotation.

**ID / Label** is one optional field: it names the Inspector entry and identifies it through the seat API. IDs are unique within a seat and use exact, case-sensitive matching. Empty IDs keep transform-based access available. `GetTransformSupport("LeftHand")`, `TryGetTransformSupport`, `SetTransformSupportActive`, `UpdateTransformSupport` and `RemoveTransformSupport` have string-ID overloads. Add rejects duplicate nonblank IDs; duplicate IDs introduced through direct edits are ambiguous and ID lookup/mutation returns null/false. IDs do not affect prefab transform resolution or which supports physically run.

Assign Body Transform from Body or Body Prefab; prefab children resolve by child indices on the spawned occupant. Foreign transforms, missing references and anchors inside the passenger hierarchy are skipped. Duplicate body transforms use the first valid active entry. An explicit pelvis/root entry overrides the corresponding automatic main binding. Preserve World Pose captures the current anchor-relative pose before adding offsets; otherwise the target is the anchor plus offsets.

Bindings deliberately override animation/IK for the selected transforms. Choose compatible skeletal constraints and competing scripts yourself; attachment settings do not silently change the controller or remove anatomical joints. Physics requires a dynamic Rigidbody to respond to forces; use transform springs for rigs without physical bodies.

Original parent, sibling order, local pose/scale and any changed kinematic setting are restored on release, handover, reset or disable. Runtime list/settings edits require `RefreshTransformSupports()`; add/remove/update/active API methods refresh automatically. Main spring tuning is captured on refresh. Custom seats also show the support lists, although their automatic main attachment remains application-owned.

### Pelvis and chest support

Seat restraints support the body around the captured seated pose. **Seat Travel** and **Chest Travel** bound translation when the harness travel limit is enabled. **Chest Support Strength** scales chest support independently from the pelvis. The compliant harness's frequency/damping, maximum acceleration and angular torque settings determine how strongly it follows the vehicle.

Use lean/twist limits to allow controlled body movement around the seated frame. These limit the seated support envelope, not individual hip/shoulder anatomy. Relative linear/angular damping suppresses motion relative to the vehicle; it is separate from ordinary world-space Rigidbody damping.

Start with the supplied settings and change one group at a time. Too much stiffness with insufficient damping can oscillate; too much damping makes the body look rigid. If only the chest sags, inspect chest support rather than increasing every hand/foot spring. Reapply seated tuning after changing settings that rebuild restraints.

## G-force limits

Expand **Passenger Seat > Settings > Force limits** on a Passenger Seat to protect an occupied **Ragdoll Physics** passenger against sudden vehicle acceleration or a hard stop against a wall. The limiter is enabled by default, including on existing seats that have no saved override. Animator, Animator + IK, Attach Only, Custom, empty seats, free/ejected ragdolls and kinematic vehicles are excluded.

Detection samples the vehicle's velocity at the seat, including angular motion, using [PhysicsSensors](API/PhysicsSensors.md) and an independent motion history for that seat. Shared chassis/ground readings are available through `vehicle.sensors`; the passenger retains point-specific acceleration history. It uses the gravity-compensated velocity change per physics step: acceleration is expressed in standard G (9.81 m/s²). Free fall alone does not trigger protection; a stationary supported seat reads about 1 G. Both the G threshold and the minimum velocity change must be exceeded. Overload activation additionally requires at least one dynamic bone to exceed the configured relative speed or angular speed. **Protect Constraint Failure** provides a separate safety path for sustained contacts: it admits the same containment if any dynamic bone exceeds twice its configured relative linear/angular speed, or the pelvis exceeds 125% of Maximum Seat Displacement. These failures can occur after light-object impacts without a high chassis G spike. The safety path is checked after physics and before rendering, uses live physics positions/point velocities, and is disabled by either its own option or the main Enabled switch. It does not force a rest pose or release/eject the occupant. A brief suspension landing with the skeleton still following the cabin does not activate protection merely because its measured G is high. The optional force threshold is an **estimated passenger inertial load**, computed from acceleration and physical passenger mass; it is not the vehicle collision contact force.

| Setting | Default | Meaning |
| --- | --- | --- |
| Enabled | On | Allow emergency protection for this seat. |
| Protect Constraint Failure | On | Independently admit containment if relative bone speed/angular speed exceeds twice its limit or pelvis displacement exceeds 125% of its envelope. Does not require the G, delta-v or force thresholds. |
| Monitor After Physics | On | Detect resolved wheel/suspension impulses in the same physics step, even without a chassis collision callback. Off restores pre-solve/collision-only detection; active containment still runs after physics. |
| Minimum G Force | 8 G | Minimum measured acceleration. |
| Minimum Velocity Change | 1 m/s | Minimum gravity-compensated velocity change in one physics step; rejects small high-frequency impulses. |
| Minimum Force | 0 N | Optional additional passenger inertial-force threshold; zero disables this extra test. |
| Protection Time | 0.15 s | Minimum hold after excessive acceleration, at least one physics step; extended until relative bone motion settles. |
| Maximum Relative Speed | 3 m/s | Maximum dynamic bone speed relative to the vehicle's velocity at that bone while protection is active. |
| Maximum Seat Displacement | 0.15 m | Pelvis travel around its seated spine origin during protection. An excessive displacement translates the dynamic body together. |
| Maximum Relative Angular Speed | 360°/s | Maximum bone spin and rotation per physics step relative to the moving vehicle, using live pre-solve rotations. |
| Maximum Joint Separation | 0.025 m | Allowed separation between anatomical joint anchors during protection. |

While below the overload thresholds and the optional constraint-failure safety thresholds, detection does not write body poses, velocities, joint settings or spring values. The ordinary sampling path allocates no managed memory and does not scan skeletal joints. A small rotation-history buffer is allocated once per occupant and refreshed before physics, without changing any bodies. Emergency pose buffers and the ordered joint cache are created only when protection first activates.

On activation, the limiter bounds bone velocities and angular velocities relative to the vehicle. It temporarily increases native solver iterations and makes the existing anatomical and vehicle-to-body angular stops hard by removing their soft limit springs. PhysX uses the joints' actual captured frames, limits and connections. Angular speed is bounded both in velocity and in actual rotation per physics step, using the last live pre-solve bone rotations relative to the moving cabin. This catches an excessive rotation introduced within a single solve; it does not compute substitute Euler limits or return the mannequin to an authored pose. Positional projection and last-resort excessive anchor/pelvis displacement repair keep the skeleton connected. Protection Time is a minimum hold: if relative bone motion is still above one quarter of the configured speed limits when the hold expires, protection is extended until the skeleton slows down. Ordinary spring values, solver settings and projection settings are restored afterwards. With Monitor After Physics enabled, one coroutine per eligible occupied physical seat samples the resolved seat velocity after every native physics solve. This includes WheelCollider and predictive suspension impulses that do not emit a chassis collision callback; overload protection no longer waits for the next pre-solve update. It also runs directly after a new collision and before rendering. Disabling this option restores pre-solve/collision-only detection, while already active protection continues to be enforced after physics. Original joint projection settings are restored when the interval ends, the feature is disabled, the seat changes controller or the occupant exits/ejects. During protection, chassis and affected ragdoll interpolation is temporarily disabled and corrected physics poses are published before rendering, preventing an old stretched pose from lingering in the image. With multiple seats, every observed physical occupant joins the protected chassis display frame, even if its own protection is inactive. This prevents one-frame road-speed displacement between an unprotected seat and a chassis whose interpolation was temporarily disabled. Original interpolation is restored for all joined occupants when the last active interval ends. Exiting restores that occupant immediately. Explicit ejection and configured damage ejection take precedence over containment.

**Measured G-force** and **G-force protection active** are read-only Play Mode indicators shown when the group is expanded. Lower the activation thresholds to cover weaker impacts, or raise them if protection engages on intended rough-terrain motion. These settings are live; they do not rebuild the seat's ordinary restraints. Teleport/reset and entry clear the velocity history so a deliberate reset is not treated as a collision.

Implementation is isolated in the static `PassengerGForceLimiter` helper, with separate runtime state owned by each seat. Serialized tuning lives in `PassengerGForceLimits`; seats do not share detection history.

## Collision and tilt response

Limb release and passenger ejection have separate configuration. They run for an eligible occupied physical humanoid; they are not general-purpose animation triggers for every passenger controller. Empty/ineligible seats skip damage handling. Tilt is not calculated unless an unreleased limb or the enabled auto-eject policy needs it. Collision force and relative speed are calculated once only if collision release/ejection needs them. Force limits have their own eligibility checks; disabling auto-eject does not disable those limits.

### Configure each limb independently

1. Select the seat component, then expand **Passenger Seat > Hands, feet and head > Left Hand** (or Right Hand / Left Foot / Right Foot).
2. Set **Mode**, **Handle** or **Anchor** for its ordinary seated ownership. An assigned Handle takes precedence over the direct Anchor.
3. Expand **Damage feedback** below **Advanced / Fine tuning**. Enable **Release On Collision** and/or **Release On Spin** for this limb only.
4. For collision release set **Minimum Collision Force** in newtons and **Minimum Collision Speed** in m/s. Both thresholds must qualify. Force is contact impulse divided by the fixed timestep.
5. For tilt release set **Minimum Angle** and **Tilt Delay**. Angle measures vehicle up against gravity up; 90 degrees means on its side. Upright yaw turns do not qualify. Each limb has its own continuous timer.
6. Repeat for the other limbs with their own thresholds, or leave their damage policies off. A released limb has runtime `EffectiveMode == Free`; its authored Mode/Handle/Anchor are retained.

Call `seat.ReleaseLimb(PassengerBodyPart.LeftHand)` for an explicit release, and inspect `seat.leftHand.IsReleasedByDamage`. `HandsReleasedByDamage` and `FeetReleasedByDamage` indicate that both corresponding limbs are released. **Passenger Seat > Signals and callbacks > On Limb Released** reports each individual release; the group callbacks run when both hands or both feet have become released.

### Configure whole-passenger ejection

1. Open **Passenger Seat > Settings > Damage / Auto-eject**.
2. Enable **Enable Passenger Ejection**, then **Eject Passenger On Collision** and/or **Eject Passenger On Spin**.
3. Set the corresponding **Minimum Ejection Collision Force / Minimum Ejection Collision Speed** or **Minimum Ejection Angle / Ejection Tilt Delay**. These thresholds are independent from each limb's settings.
4. Set **Passenger Ejection Velocity** if an additional vehicle-local velocity change is required. Existing body momentum is preserved by the physical release.
5. Set **Reseat Ejected On Reset** if explicit reset should return this same damage-ejected body when it remains eligible. It does not steal an actor from another seat.

Ejection ends occupancy and releases the whole passenger. Limb release leaves the passenger seated. Whole-passenger ejection takes priority when the same damage sample qualifies for both.

### Contact exclusions

Seat-wide entry/release policies are under **Passenger Seat > Settings > Colliders and collisions > Collision exclusions on entry / Collisions on release**. Configure **Exclude Vehicle Collisions On Enter**, **Exclude Self Collisions On Enter**, **Enable Vehicle Colliders On Release** and **Enable Self Colliders On Release** there. Each limb also has its own two **Enable … Colliders On Release** fields directly inside **Hands, feet and head > [limb]**. Native joint exclusions and adjacent skeletal-body exclusions still apply.

For selected cabin surfaces use the independent lists:

| Purpose | Full Inspector path | Runtime field |
| --- | --- | --- |
| Contacts for one released/Free limb | Passenger Seat > Hands, feet and head > [limb] > Release colliders | `seat.leftHand.releaseColliders` (or the other limb) |
| Contacts for the entire ejected body | Passenger Seat > Settings > Damage / Auto-eject > Eject colliders | `seat.ejectColliders` |

Each item is a `PassengerCollisionSurface` containing **Collider**, **Ignore World Collisions** and **Ignore Vehicle Collisions**. Assign existing non-trigger cabin surfaces such as the cushion, backrest, roof, dashboard or actual door collider. Keep surfaces enabled; contact pairs are managed instead of toggling shared collider objects. A moving door's surface belongs under that door.

A limb list admits contacts only for that limb when Free; it does not release the other limbs or enable whole-body contact. The eject list applies to the whole passenger after detachment. Already admitted contacts remain admitted through subsequent limb releases/ejection; another activation does not revoke them. Explicit restoration/reset clears that admission state. Existing application-owned collision exclusions are respected.

The ignore checkboxes describe the listed cabin surface's contacts with the environment or other eligible vehicle surfaces; they do not mean “ignore this passenger's hand.” When the same collider appears in several lists, each enabled ignore policy wins over unchecked copies (logical OR across its entries). Passenger cabin contacts and specially managed moving parts keep their own filtering rules; raycasts/triggers are unaffected.

All these lists support **+ / −** and drag reordering. **Copy colliders**, **Paste colliders** and **Reset colliders** beneath each list share a clipboard across limbs and eject lists. Paste copies collider references and both policies. Reset clears only that list immediately, without a confirmation dialog; Undo/Redo works for paste/reset and serialized list edits.

For runtime edits, replace individual entries/lists and call `seat.RefreshCollisionSettings()`. Example:

**Example: `SeatSurfaceConfiguration.cs`**

<!-- example: SeatSurfaceConfiguration.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public sealed class SeatSurfaceConfiguration : MonoBehaviour
    {
        public PassengerSeat seat;
        public Collider dashboardCollider;

        public void ConfigureLeftHand()
        {
            if (!seat || !dashboardCollider) return;
            seat.leftHand.releaseColliders = new[] {
                new PassengerCollisionSurface {
                    collider = dashboardCollider,
                    ignoreWorldCollisions = true,
                    ignoreVehicleCollisions = false
                }
            };
            seat.RefreshCollisionSettings();
        }
    }
}
```

`SetReleaseCollisions` controls broader vehicle/self policies separately. Empty cabin lists skip their per-step surface checks. Shared surface filtering can remain necessary after a seat becomes empty because an ejected body still contacts those surfaces.

Released dynamic limbs use **Humanoid Passenger > Free Ragdoll > Collision Detection**. Fit intersecting geometry before enabling broad contacts: restraints pulling a body through a collider can cause jitter.

### Restore after damage

Release is latched until explicit restoration/reset or a new seat attachment. Becoming upright does not reattach a limb automatically. `seat.RestoreDamageFeedback()` resets the damage state and built-in seated support, or emits the Custom occupant's reset request. Preserve and check actual occupancy when restoring UI or gameplay ownership. Selected-collider contact admission remains stable across damage activations; explicit restoration starts a new contact-ownership cycle.

## Motorcycle rider support

Fit the pelvis, foot pegs and handlebar contacts before tuning extra rider support. Keep the knees outside the motorcycle using reachable foot/hip geometry; do not use seat springs to conceal incorrect anatomical hip limits.

On `PassengerSeat`, **Hold Head Forward** adds artificial angular spring support to the seated ragdoll head. A runtime PhysX angular drive evaluates its spring and damping together with the native constraints; it does not apply an explicit PD torque on each physics step. All three linear axes of this support remain free, so only the anatomical neck locates the head. **Head Pitch** is relative to the seat's neutral forward pose: zero faces forward, negative looks up and positive looks down. **Head Spring**, **Head Damper** and **Maximum Head Torque** control stiffness, damping relative to the chassis and the torque cap. They can be adjusted in Play Mode.

This requires a Humanoid Avatar, a saved anatomical joint on the mapped head and a dynamic head Rigidbody. It runs only for an occupied enabled Ragdoll Physics seat. Animator, Animator + IK, Attach Only, Custom, empty seats and ejected bodies receive no head torque. Disabling support immediately clears its runtime drive and removes the temporary angular support; saved anatomy remains intact. The demo uses zero-degree pitch. The same settings work for a quad, car, boat or aircraft without a BalanceRider component. Support is off by default on new seats; older enabled rider support is transferred to its assigned seat.

## Balance rider: motorcycles, bicycles and scooters

**Balance Rider** is an optional passenger behaviour, independent of the drive profile. Add it through **Tools > UltraVehicleSystem > Add Component > Passengers > Seats > Balance Rider** or Unity’s Add Component menu, then assign its **Seat**. New components work with any profile; **Motorcycle Profile Only** is an optional restriction. The demo motorcycle keeps that restriction and its existing foot motion.

A **Passenger Seat** represents an occupancy and body-support frame; it can support a standing character as well as a seated one. For a scooter, place its pelvis/backrest anchor at the rider’s standing hip height above the deck, with suitable orientation, and place the foot targets on the deck. Fit hands to the handlebar and preview the pose. Adjust foot pinning and the seat’s compliant harness to the intended stance. For a bicycle or motorcycle, put the same anchor over the saddle. Do not enable speed-dependent foot placement merely because a vehicle has handlebars: choose each foot’s policy explicitly.

### Independent foot policies

| Setting | Behavior and required poses |
| --- | --- |
| Speed Blend | Interpolates from Ground to Riding using Riding Blend. Requires both transforms. |
| Riding | Follows the Riding transform continuously. Use it for the scooter’s planted foot, both feet on a deck, or foot targets parented beneath animated bicycle pedals. Only Riding is required. |
| Ground | Follows the Ground transform continuously; only Ground is required. |
| Unchanged | Leaves this foot’s ordinary Seat binding intact. |

Left and right policies are independent. A foot with an assigned Handle keeps that Handle’s priority; Balance Rider does not replace it. Missing required poses leave the Seat’s existing anchor intact. Disabling the behaviour, changing its seat or making it inapplicable releases its generated anchors and restores the original direct bindings. It does not remove targets assigned by another system after it released ownership.

**Blend Source = Speed** uses speed magnitude, including reverse motion, between **Lift Starts At** and **Fully Raised At**. **Blend Speed** limits how quickly progress changes, in normalized units per second. **Manual** uses **Manual Riding Blend** instead: zero requests Ground, one requests Riding. This lets custom controls or an animation request a push-off/return pose without changing the vehicle input interface. Only feet in Speed Blend use this progress; Riding and Ground follow their transforms directly. Ground poses are authored transforms, not terrain raycasts.

| Vehicle / stance | Starting configuration |
| --- | --- |
| Motorcycle | Both feet Speed Blend between low-speed ground poses and pegs. Keep the demo’s 1–8 km/h blend as a starting point and fit the poses to the model. |
| Bicycle | For simple feet-down/feet-up transitions, use Speed Blend. For pedalling, choose Riding and parent targets under pedals animated by your own crank/animation logic. Balance Rider follows these targets; it does not generate a pedal cycle or propulsion. |
| Scooter with both feet on deck | Fit a standing pelvis anchor and use Riding for both feet, with targets on the deck. |
| Scooter with one pushing foot | Use Riding for the planted foot and Speed Blend for the other. Select Manual and animate Manual Riding Blend plus the Ground/Riding transforms for a push gesture. The gesture does not itself accelerate the vehicle. |
| Quad / fixed riding stance | Keep feet on riding rests with Riding or leave their Seat anchors unchanged. Use Wheeled drive mode. |

For a bicycle, add **Exterior > Bicycle > Pedal Drive** and assign the rider, crank and independent pedal pivots. Make both pedal pivots direct children of the crank with matching axle frames; set Local Axis to the crank axle. Place each Foot Riding anchor below its pedal and select Speed Blend to transition from ground support. Drive Ratio, cadence and response control pedalling; the component supplies moving targets before the passenger solver, without adding propulsion. Ragdoll and Animator + IK follow those targets; pure Animator requires a pedalling animation. See [Pedal Drive settings](InspectorReference/Exterior.md#pedaldrive).

### Optional physical torso support

**Support Balance** applies a bounded spring torque to the seated/standing humanoid ragdoll pelvis. **Forward Lean** sets the target forward/backward lean relative to the pelvis/backrest frame. **Steering Lean** adds signed side lean from steering input; zero disables steering-dependent lean. **Balance Spring**, **Balance Damper** and **Maximum Balance Torque** set stiffness, damping relative to the chassis and the torque cap. Support is off by default. Start with modest values and a reachable stance; excessive support can oppose the neck, hip or harness limits.

This supports the rider’s body, not the vehicle chassis. Two-wheel vehicle upright/lean assistance remains part of MotorcycleProfile. Four-wheel vehicles continue to use Wheeled. The support requires an occupied active Ragdoll Physics seat and a dynamic humanoid pelvis; Animator/IK/Attach Only/Custom controllers and ejected occupants receive no balancing torque. Disabling the behaviour or support stops added torque without changing the skeleton’s joint limits. Head support remains separately configurable on Passenger Seat.

### Runtime posture input

Change these public settings on the existing component; no special vehicle input source is needed:

**Example: `BalanceRiderPostureInput.cs`**

<!-- example: BalanceRiderPostureInput.cs -->
```csharp
using UltraVehicleSystem;
using UnityEngine;

public sealed class BalanceRiderPostureInput : MonoBehaviour
{
    [SerializeField] private BalanceRider rider;

    // Call from your animation/input code: 0 = ground, 1 = riding/deck.
    public void SetFootReturn(float progress)
    {
        if (!rider) return;
        rider.leftFootMode = RiderFootMode.Riding;
        rider.rightFootMode = RiderFootMode.SpeedBlend;
        rider.blendSource = RiderBlendSource.Manual;
        rider.manualRidingBlend = Mathf.Clamp01(progress);
    }
}
```

## Quads and other straddled wheeled vehicles

A quad uses **Wheeled** drive mode. It does not require MotorcycleProfile or a special quad profile: four-wheel contact, braking, engine/transmission, differential and steering use the same modules as a car.

1. Configure four Wheel Colliders in **Vehicle Controller > Wheels**. Enable steering on the front pair; choose rear-wheel drive or all four driven wheels. Set each wheel’s radius, width, travel, drive weight and brake role, then apply the configuration.
2. Fit chassis mass, center of mass, track width, suspension and tire grip to the actual model. Start with a low center of mass and moderate steering travel; a quad can roll over naturally, and it does not use motorcycle lean/balance assistance. Anti Roll is available when additional roll resistance is wanted.
3. Add a **Passenger Seat** with **Ragdoll Physics**. Position the pelvis/backrest anchor over the saddle and author left/right foot anchors on the foot rests. Use **Seated pose** to fit the pelvis, feet and hand targets; preview the pose before increasing restraint springs. Keep feet on their riding rests, including when stopped.
4. Use **Motorcycle Handlebar** for the two grip tubes. Parent its grip centers under the moving handlebar, assign it to both seat hand bindings, and use **Prepare hand grip**. Despite its name, this handle works with Wheeled and does not require BalanceRider or MotorcycleProfile.
5. Animate the handlebar with **Steering Wheel Animator**. Assign the handlebar transform, choose its local hinge axis, enable **Override Steering Angle** and set **Steering Angle At Full Lock** (for example 25–35° as a visual starting point). The angle follows resolved wheel steering, not a keyboard-specific input. This local visual angle does not change tire steering. Use Invert if the model turns the wrong way. Keep the hand grip centers beneath this moving transform so IK follows it.
6. Enable the seat’s **Hold Head Forward** if the leaning torso lets the head fall. Start with zero **Head Pitch** and tune pitch, stiffness, damping and torque cap in Play Mode. The support points along the seat’s forward frame, so fit torso lean through the pelvis/backrest anchor rather than tipping the entire Seat object solely to recline the body.

BalanceRider is optional. Its foot-ground transition is intended for two-wheel riders and is usually unnecessary on a quad. If a custom vehicle needs it, disable **Motorcycle Profile Only** and supply all four foot poses. Head support belongs to the seat and works even when BalanceRider is absent or disabled. Ordinary keyboard, analog, external AI and direct sources can drive the quad through the same Vehicle Controller interfaces used for cars.

## Check a fitted seat

| Symptom | Check first |
| --- | --- |
| Body folds or oscillates | Reach, original anatomy and support travel before increasing springs |
| Direct Anchor seems ignored | A Handle is still assigned and has priority |
| Wrist is correct but fingers penetrate | Grip dimensions/calibration in the hand guide |
| Foot follows position but twists freely | Align Rotation is separate from Pin To Anchor |
| Free arm keeps chasing a target | Another IK/animation writer, wrong effective mode or an active handle |
| Released hand does not reattach | Damage release latch and reset policy |
| Foot transfer stays on accelerator | Resolved brake demand, helper update owner and thresholds |

## Custom ragdoll joint supports

Use **Passenger Seat > Custom Ragdoll Joint Supports > Joint Supports** for additional support at an arbitrary anatomical joint. For example, use a knee target to keep a rider’s knee outside the fuel tank while retaining a spring response to motion. Each entry holds one joint pivot; the original anatomical joint and its angular limits continue to operate.

1. Find the desired **Joint ID** in the occupant’s **Anatomical Joints** list. A knee is normally the joint connecting the thigh to the lower leg. Copy its exact ID; names depend on that rig’s mapping and can be edited by its author.
2. Create an empty target under the vehicle or seat and place it where the knee should be held. Use a vehicle-owned target rather than parenting the target to the supported limb.
3. Add a Joint Supports entry, set **Joint ID**, **Anchor** and **Active**. Keep **Local Offset** at zero to act at the anatomical pivot; use an offset to hold another point on the same rigidbody.
4. Start with moderate **Spring**, **Damper** and **Maximum Force**. Spring pulls the point toward the target; damper reduces motion relative to that moving target. The cap limits their combined force. Increase stiffness only enough to get the required support, so it can work alongside the existing hand, foot and torso restraints.
5. Leave **Hold Rotation** off for a knee that should still rotate within its anatomical limits. Enable it only when an orientation is also required. Then set the desired body rotation using **Rotation Offset**, and tune **Rotation Spring**, **Rotation Damper** and **Maximum Torque** separately. The target orientation is the anchor rotation plus this offset, not an automatically captured seated pose.

Joint-ID supports run in Play mode on an enabled occupied `HumanoidPassenger`, independently of controller and ragdoll state. They apply physical forces only to dynamic joint rigidbodies; kinematic bodies cannot respond to forces. For plain transforms or kinematic bones, choose Spring in Custom Transform Supports. An entry with an unknown/ambiguous ID or no anchor is skipped. Exiting, ejection, seat disable and controller handover release tracking; a newly seated occupant is resolved by its own joint IDs.

Custom supports remain active if ordinary hand/foot damage restraints release while the character stays seated. Use `SetJointSupportActive` to release those custom supports according to your own damage logic. They apply artificial forces to the passenger without applying an equal opposite force to the vehicle. They cannot override locked anatomical axes or make an unreachable pose physically valid.

Position support uses N/m, N/(m/s) and N; rotation uses Nm/rad, Nm/(rad/s) and Nm. Zero maximum force/torque disables that contribution. Anchors may move during play; damping accounts for their motion. Keep targets near reachable limb positions and move them smoothly for a soft response.

### Configure a knee target from code

Attach this script to an application object, assign a seat and an empty knee target, and copy the knee’s actual Anatomical Joint ID into the Inspector. The setup can run before occupancy.

<!-- example: KneeSeatSupport.cs -->
```csharp
using UltraVehicleSystem;
using UnityEngine;

public sealed class KneeSeatSupport : MonoBehaviour
{
    public PassengerSeat seat;
    public Transform kneeTarget;
    public string kneeJointId = "LeftUpperLegToLeftLowerLeg";

    private void Start()
    {
        if (!seat || !kneeTarget) return;
        var support = seat.GetJointSupport(kneeJointId);
        if (support == null)
        {
            support = new PassengerJointSupport { jointId = kneeJointId };
            if (!seat.AddJointSupport(support)) return;
        }
        support.anchor = kneeTarget;
        support.spring = 500f;
        support.damper = 30f;
        support.maximumForce = 300f;
        support.holdRotation = false;
        seat.SetJointSupportActive(kneeJointId, true);
    }

    public void ReleaseKnee() => seat.SetJointSupportActive(kneeJointId, false);
    public void HoldKnee() => seat.SetJointSupportActive(kneeJointId, true);
}
```

For live changes, `seat.UpdateJointSupport(kneeJointId, support => support.spring = 700f)` edits the entry and restarts target tracking. `TryGetJointSupportState` exposes the supported world point, target point and last applied force/torque; see the [API reference](API/PassengerControllers.md#passengerjointsupportstate).

Select the vehicle or seat to show yellow target markers and lines to resolved anatomical pivots. Under the bottom **Gizmos** foldout, **Show anchors**, **Show connections** and **Show labels** control these guides independently. A pre-placed **Passenger Seat > Body** can supply joint positions for the editor preview; a prefab-only occupant is resolved after spawning.

## Seated recovery without pose resets

Physical seated limbs follow their anatomical joints and configured seat/handle supports. A closed palm uses a native point attachment and spring-driven wrist rotation. Explicit vehicle resets, re-entry and `ResetSeatedPose()` place the body deliberately.

Strong impacts can temporarily stretch native constraints. **Solver Iterations** and **Solver Velocity Iterations** improve constraint accuracy; a smaller project **Fixed Timestep** reduces movement between physics solves at a higher CPU cost. WheelCollider substeps refine wheel simulation, not the passenger skeleton. The package does not change the project timestep automatically.

Test the timestep, solver settings and collision policy with reachable limb targets and the actual vehicle. See [PhysX joint tuning](https://nvidia-omniverse.github.io/PhysX/physx/5.3.1/docs/Joints.html) for solver convergence and projection tradeoffs.

## Motorcycle foot reversing and rider animations

### Choose how the motorcycle reverses

In **Balance Rider > Reversing**, choose **Reverse Mode**:

- **Reverse Gear** retains the ordinary engine/transmission reverse.
- **Foot Pushing** brakes forward motion first, then selects neutral and uses bounded backward wheel torque to represent human effort. Holding reverse alternates the driver's feet. Positive throttle resumes forward gear. Explicit reverse-gear input cannot engage engine reverse in this mode.

Tune **Balance Rider > Reversing > Foot Reverse Speed** (m/s, default **1.3**, about **4.7 km/h**), **Foot Push Torque** (total Nm across driven supported wheels), **Foot Reverse Engage Speed** and **Foot Step Period** (seconds per left/right pair). These settings do not change the forward steering or engine tune. New riders retain Reverse Gear; the demo motorcycle shows Foot Pushing and lets you switch it in the demo panel.

The same rider works with Wheeled Profile for a quad or scooter: disable **Motorcycle Profile Only**. The drive profile retains its usual forward handling.

### Set up the driver feet

Add **Balance Rider**, assign its **Seat**, and set the seat role to **Humanoid Driver**. Assign left/right **Ground** and **Riding** targets, and leave both foot modes on **Speed Blend** (or Ground for permanently lowered feet). Keep **Allow Foot Pushing** enabled. Choose **Push Feet > Both** for a motorcycle, or **Left / Right** for a scooter; set the unused foot mode to Riding and assign its deck target. Disabled prevents foot propulsion. Only the selected feet need usable ground targets. Foot Pushing also requires an occupant, a supported wheel-driven vehicle and unreleased selected feet; braking/handbrake, ejection, airborne motion or disabling the behavior removes its assistance. Held reverse lowers the feet before pushing. Ordinary reverse input still brakes a moving motorcycle before walking begins.

**Foot Start Blend Time** (default 0.12 s) blends from the supported foot pose into walking. Set zero for an immediate transition. **Foot Step Distance**, **Foot Step Height**, **Use Wheel Ground Plane** and **Foot Ground Clearance** tune the procedural gait. **Foot Motion Smooth Time** (default 0.06 s) smooths the physical targets; **Foot Ground Smooth Time** (default 0.08 s) steadies the support plane on uneven ground. Set either to zero to disable that smoothing. Ground projection reuses wheel contacts. The step period shortens at higher reverse speed to keep planted feet within reach. In Ragdoll Physics the normal seat foot supports follow the alternating targets; Animator + IK can use the same targets. Pure Animator uses your clips and the animation bridge below instead of writing animated bones procedurally. Foot-assisted propulsion requires physical vehicle driving, not Direct control.

### Connect your own Animator

Add **Rider Animator** and assign its Balance Rider. Leave **Animator** empty to follow the occupant's seated animation source, including the sampled source used by a physical ragdoll. An explicit Animator is also supported. This component does not replace your controller or require a particular clip.

Create the float parameters you need (names are configurable): **RiderSpeed** (signed m/s), **RiderSteeringAngle** and **RiderLean** (signed degrees), **RiderFeetBlend** (0 ground / 1 riding), and **RiderStepPhase** (0–1). Missing parameters are skipped. To synchronize a walking clip with the physical gait, use RiderStepPhase as that Animator state's Motion Time parameter.

Under **Event And State Rules**, add independent rules for steering/lean angle ranges, raised/lowered feet, reversing, foot pushing, airborne/grounded or each planted foot. Each rule can hold a bool, fire entry/exit triggers, crossfade to an optional state on a selected layer and invoke custom callbacks. Angle Hysteresis prevents repeated callbacks at a boundary. For example, use Steering Angle **10..45** for a right-turn pose and **-45..-10** for left; use Feet Lowered for a stopped stance and Foot Pushing for your reverse-walking state. Configure masks and layer weights with the existing [Passenger Animator Layers](API/PassengerControllers.md#passengeranimatorlayers) component and your controller.

Balance Rider also exposes **Motion Updated**, **Foot Pushing Changed** and **Foot Planted** as Inspector callbacks and C# events. `MotionState` contains the same data for custom integrations. Call `RiderAnimator.RefreshBindings()` after changing rule arrays, parameter names, the rider reference or controller from code.

### Trigger custom animations from code

Add a rule with **Condition > Custom**, choose an **Action Name** such as `LookBehind`, and configure its bool, triggers or state exactly like an automatic rule. Your code controls it with `SetActionActive("LookBehind", condition)`, `PlayAction("LookBehind")` and `StopAction("LookBehind")`. Repeated SetActionActive calls with the same value do not restart the animation. PlayAction deliberately retriggers entry. Custom actions end when the seat becomes empty; call StopAction when your own action finishes. These APIs work with Animator, Animator + IK and a configured ragdoll animation source.

To play a state directly, call `PlayAnimation("Upper Body.LookBehind", layer: 1, fadeSeconds: .2f)`. The state must exist in the assigned Animator Controller; the method returns false if no usable Animator/state/layer exists. Use Animator transitions or an exit action to return to the riding state. Layer masks keep the action limited to the intended body parts.

### Add a rear passenger

Use a separate Passenger Seat with role **Humanoid Passenger**, its own pelvis, hand/grab and foot-peg targets, and an optional Balance Rider/Rider Animator. Set foot modes to Riding so a passenger keeps their feet on the pegs. A passenger never takes over driver foot propulsion. The demo has **RearPassenger**, initially empty; use its Add/Remove button or `Spawn()` / `TryExit()` on that seat. Driver and passenger can use independent controller modes and animation rules.
