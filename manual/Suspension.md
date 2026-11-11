# Suspension setup

See [Crash, contact and landing effects](DamageFeedback.md) for configurable impact layers, scraping, glass breakage, suspension cues and pooled particles.

Start with native wheel suspension supporting the chassis. `Suspension` configures the WheelColliders' springs, dampers, travel and force application. Visible linkages are separate helpers; they should follow a working physical setup rather than conceal an unsupported vehicle.

## Inspector quick start

1. Select the vehicle root outside Play Mode. Open **Vehicle Controller > Wheels > Wheel Setup**. Add one entry per wheel, assign its native **Wheel Collider** and visual Transform, and set radius, width, mass and the steering/drive/brake roles. Use **Discover child Wheel Colliders** only for colliders belonging to this chassis Rigidbody, then review the generated entries.
2. Open **Vehicle Controller > Setup > Configuration**. Set **Suspension Travel** in metres and check chassis mass/centre of mass. Position the wheel mounts and chassis colliders so the tires can compress without immediately striking bodywork or the ground with the chassis.
3. Open **Modules > Drive > Suspension**, adding Suspension through **Add module...** if absent. Set **Spring**, **Damper** and **Target Position** for the expected load. Edit these fields here rather than the greyed-out managed values on individual WheelColliders.
4. Press **Apply vehicle configuration** and save. Enter Play Mode on flat ground and let the car settle. Check each wheel has usable travel, the body is supported, and no visual linkage is supplying a second physical support path by mistake.
5. Drive over one low bump, brake and turn. Adjust spring/damping first. Then configure **Anti Roll** under Drive and the landing settings below if needed. Add ControlArm, ShockAbsorber and other visible linkage helpers only after the physical wheel setup works.

Use [Support the vehicle](#support-the-vehicle) for tuning and [Add visible linkage](#add-visible-linkage) for model bindings. A Suspension module cannot infer wheel mounts or wheel roles from mesh names.

## Support the vehicle

1. Check real scale, mass, centre of mass, wheel radius and chassis clearance. Configure wheel geometry through **VehicleController > Wheels > Wheel Setup**.
2. Set **Vehicle Settings > Suspension Travel** to a usable stroke in metres.
3. Add/register Suspension and set **Spring**, **Damper** and **Target Position**. Test the intended loaded vehicle, not a visually identical object with a different mass.
4. Apply vehicle configuration on flat ground. Let the vehicle settle with no drive/steering input and check that each wheel remains within usable travel.
5. Test braking, a steady turn and a small bump before adding contact-envelope or anti-roll assistance.
6. Add the visible linkage only after the contact wheels and chassis behave correctly.

Spring is stiffness in N/m and damper is in N·s/m. Greater mass needs appropriate support; increasing travel alone does not increase spring force. Target Position sets the native spring's rest target along its stroke, rather than moving the collider Transform.

### Wheel mount versus suspension extension

The WheelCollider Transform/Center defines its mounting reference; the wheel hub moves through suspension travel below that reference. Applying a nonzero suspension stroke can therefore place the hub/visual lower than a setup tested with zero Suspension Distance. This does not necessarily mean the mount Transform moved.

Set the intended radius, travel and rest/load first, then position the mount/centre to fit the vehicle at that loaded ride height. Keep appropriate compression/rebound clearance. Zeroing native Suspension Distance afterward is not a persistent offset: the module can overwrite it on configuration, and it removes the intended stroke.

Bound Wheel/native fields are greyed out where a vehicle/module owns them. Edit Wheel Setup, vehicle travel, Suspension or an assigned shock override as indicated. Settings written to native springs can remain installed when the setup module is disabled; disabling it is not equivalent to restoring a completely untouched WheelCollider.

## Landing compression and rebound

**Landing Response** temporarily softens springs and damping after a qualifying wheel landing, then restores the authored settings. It is enabled for grounded profiles; side/roof contacts use collision response instead.

- **Landing Minimum Air Time** and **Landing Minimum/Full Response Speed** determine when and how strongly it responds, including motion from chassis rotation and moving ground.
- **Landing Spring Multiplier**, **Landing Damper Multiplier** and **Landing Bump Stop Multiplier** control compression and rebound.
- **Landing Response Duration** and **Landing Minimum Cycles** control recovery time. **Allow Landing Rebound** releases the expansion limiter until suspension motion settles.

Correct insufficient wheel travel, early chassis contact or excessive stiffness before lowering damping further. This response changes suspension coefficients; the optional bounce below adds a whole-vehicle push. See the [Suspension settings](InspectorReference/Drive.md#suspension) for defaults and limits.

## Optional whole-vehicle landing bounce

**Landing Ground Bounce** adds bounded rebound assistance after a wheel landing. It is enabled by default for grounded profiles; switch it off to keep only native suspension compression and oscillation.

**Progressive Landing Bounce** delivers one assisted release over the rising suspension stroke. **Progressive Landing Recovery** and **Landing Settling Damping Ratio** tune settling. With progressive mode disabled, **Landing Bounce Maximum Count** limits the assisted sequence.

**Directional Landing Response** prepares each axle for an angled touchdown. **Directional Landing Bounce** applies the push near supporting wheel contacts, allowing pitch/roll; use **Landing Contact Leverage**, **Landing Bounce Maximum Tilt** and **Landing Bounce Maximum Rotation** to constrain it. **Landing Bounce Restitution** and **Landing Bounce Maximum Speed** set rebound strength and its target cap.

Small contact flickers, side/roof contacts and continuous grounded driving do not start bounces. Disabling the response or teleporting clears pending assistance. `LandingBounceCount` and `LandingBounceSpeed` report the current response. See the [Suspension settings](InspectorReference/Drive.md#suspension) for all parameters.

## Spring, damping and bump response

Tune static support before damping. If the suspension already sits at an end stop under normal load, inspect mass, spring, travel and target rather than trying to cure it with damping. Once support is reasonable, add enough damping to settle repeated oscillation without making every bump harsh.

**Degressive Damping** limits high-speed compression damping above **Damper Blowoff Speed**, while retaining rebound damping and low-speed body control. Compression blowoff does not reduce the damper on the extension stroke, so stored spring energy can dissipate instead of launching the chassis. It is intended to avoid a sharp road input generating an excessive linear damper impulse. It does not add travel or change the tire's geometry.

**Wheel Damping Rate** damps native wheel rotation, not suspension stroke. **Limit Expansion Velocity** is a separate native suspension option. Keep those distinct when a tire spins too long versus when the body bounces.

**Arcade Bump Damping** is optional extra supported-body upward-motion damping. Its rise-speed/response settings affect the chassis when sufficiently supported. Tune physical travel/contact first; this assistance should not be the first response to an overlapping collider.

## Force application and body sway

With **Automatic Force Application** enabled, the module places wheel force application relative to the chassis centre of mass. **Force Offset Below Center Of Mass** and **Body Sway Travel Ratio** affect the lever arm and resulting pitch/roll. With automatic placement off, **Force Application Height** supplies the explicit baseline.

This force point is not the suspension mount or a visual hub offset. Changing it affects body response to tire forces; changing the mesh position does not. Contact-envelope radius corrections are accounted for so force placement remains consistent with the current effective support radius.

## Anti-roll support

Add/enable `AntiRoll` explicitly, create an axle pair using the left/right `Wheel` adapters and set **Stiffness**. It transfers forces between supported sides based on their suspension travel difference; it does not overwrite chassis orientation.

The pair requires both wheels to have native ground support. At an edge with one wheel airborne, it does not apply only half of an axle force that would artificially lift the chassis. Excess stiffness can reduce compliant behavior over uneven ground, so compare a steady corner and a one-sided bump independently.

## Add visible linkage

Choose helpers based on the actual model assembly:

| Helper | Model purpose |
| --- | --- |
| `ShockAbsorber` | Telescoping casing and piston between chassis/wheel attachments |
| `ControlArm` | Arm geometry between chassis and moving hub |
| `SuspensionHub` | Hub presentation following wheel support/steering geometry |
| `SteeringTieRod` | Steering linkage and its geometric steering relationship |
| `SuspensionAxle` | Axle assembly presentation |
| `HalfShaft` | Shaft endpoints/orientation as suspension moves |

Assign the relevant wheel, pivots and attachment points at the actual model joints. Keep import scale/orientation offsets on child meshes. Test full compression, rebound and both steering locks; do not set angular/length limits that prevent the assembly reaching a valid wheel pose.

A ShockAbsorber's casing/piston slide rather than being treated as arbitrarily stretchable meshes. Their physical lengths and allowable minimum/maximum assembly length must agree with the mesh. A visual helper cannot force incompatible attachment points to meet.

### Optional physical shock override

Assign a shock's native WheelCollider and enable **Override Wheel Physics** to supply per-wheel spring, damper, travel and target through Suspension. Use one override per wheel. The helper must belong to the same vehicle and be active for that override to apply; a visual-only shock should leave it off.

**Motion Ratio** is shock travel divided by wheel travel. Wheel-equivalent stiffness and damping scale with its square. For a ratio of 0.5, a shock stiffness of 40000 N/m gives 10000 N/m at the wheel, not 20000. Choose wheel travel separately rather than confusing mesh length with suspension stroke.

When an override is active, changing the global spring may not change that wheel. Reconfigure after assigning/changing the relevant shock references. See [linkage contracts](Scripting/Suspension.md) for detailed axis/length conversion and code tuning.

## Wheel spin and coasting

`WheelDynamics` derives airborne rotational damping using **Airborne Spin Half Life**, wheel inertia and the configured ground damping baseline. It does not add engine propulsion or suspension spring force. Test a jump to distinguish tire spin loss from a drivetrain shift decision.

`Coasting` uses a tiny **Contact Release Torque** to release native low-speed sticky tire behavior when rolling/towing on slopes. **Release Below RPM** and **Minimum Slope Degrees** bound that assistance. It respects brake/drive priorities and is not an engine or parking-brake replacement.

Configure parking through Brakes/parking policy and trailer braking, rather than trying to make damping statically hold a vehicle forever. Keep visual tire settling separate too: Wheel's visual suspension smoothing changes the rendered hub interpolation, not the native spring support.

## Troubleshoot

| Observation | First adjustment |
| --- | --- |
| Suspension rests at an end stop | Mass, travel, spring and target position |
| Body repeatedly bounces | Damping after static support is correct |
| Sharp bumps are excessively harsh | Available travel, degressive damping and collider clearance |
| Wheel appears lower after Apply | Mount/centre versus loaded stroke; vehicle owns native travel |
| Only one wheel ignores global tuning | Assigned physical shock override |
| Chassis looks rigid or lifts at corners | Force application and anti-roll settings |
| Linkage pops or cannot reach | Attachment geometry, length limits and competing Transform writers |

Aircraft hinged gear has a separate [setup](Aircraft.md#hinged-gear-suspension). For rolling curbs and solid obstacles, continue with [Contact envelope](ContactEnvelope.md) and [Tire collision](TireCollision.md).

## Performance tuning

ContactEnvelope exposes edge-refinement and probe-interval controls; Suspension exposes vehicle-wide native wheel substeps. See [Inspector performance settings](Performance.md#inspector-performance-settings) for cost/precision tradeoffs and when to apply changes.

## Scene view gizmos

Select the vehicle root to preview its suspension helpers together, or select an individual helper to inspect its geometry. These guides also work outside Play mode. Expand **Gizmos** at the bottom of each component Inspector to control anchors, connecting lines, reference axes, ranges and labels separately. Components with editable anchors also expose **Show editing handles**.

- **Suspension** shows each wheel’s full compression/extension stroke in yellow and its unloaded spring target in green. Outside Play mode the preview uses vehicle travel and Suspension settings, including enabled per-wheel ShockAbsorber overrides; in Play mode it uses the configured wheel values. The target is not the loaded ride height.
- **ShockAbsorber** shows both mounting eyes, their current separation and minimum/maximum mechanical length. Red indicates travel outside the configured range.
- **SuspensionHub**, **SuspensionAxle**, **ShockAbsorber** and **HalfShaft** show their configured rotation permissions and angular limits in the same neutral frames used by their pose solvers.
- **ControlArm** shows the arm sweep when Constrain Hub To Arc is enabled, or the native wheel travel when it is disabled. **HalfShaft** also shows the CV joint angle range in the current bending plane.
- **SteeringTieRod** shows both steering directions, rack travel, knuckle rotation limits and rod articulation limits.

Rotation axes use red X, green Y and blue Z. A locked axis is marked as locked; an unrestricted axis has a full circle. The arcs describe separate Euler-axis settings, rather than a combined reachable volume. Gizmo switches only affect the Scene view and do not change suspension physics.

## Build your own visual suspension assembly

1. Finish the physical wheel first: keep the WheelCollider mount and `Wheel` adapter on the vehicle, assign its visual wheel root, and verify loaded ride height and travel. Create separate clean pivots for the hub, arms, shock casing/piston and shafts; keep model orientation corrections on child meshes.
2. Add only the helpers matching your model. Use `SuspensionHub` for the upright, `ControlArm` for chassis-to-hub arms, `ShockAbsorber` for telescoping sections, `SteeringTieRod` for rack/knuckle linkage, `HalfShaft` for the driven shaft and `SuspensionAxle` for an axle assembly. Several arms may follow the same wheel. Enable **Constrain Hub To Arc** for a fixed-length wishbone path. Disable it to follow the native wheel suspension axis without changing track width, as in the Monster Truck demo. In that mode the visual arm branches fit between their anchors; they do not enforce a fixed arm length.
3. Assign wheel references, chassis and moving-side attachment points at the actual joint centres. Set each helper's axes, neutral orientation, lengths and allowed angles to match the mesh. Keep chassis anchors outside the moving assembly so a solver does not move its own reference.
4. Leave shock Override Wheel Physics off for appearance-only assemblies. Enable it only when this shock deliberately owns that wheel's physical settings; assign its native WheelCollider and account for motion ratio. Apply vehicle configuration after changing physical settings.
5. Check the Scene gizmos, then test full compression, full droop and both steering locks in Play mode. Watch casing/piston overlap, shaft reach, joint limits and tire clearance. Correct geometry before smoothing. Remove Animator tracks or scripts that also write the solved pivots.

For a linkage geometry the supplied helpers cannot represent, write a separate visual component that reads the resolved wheel pose and moves only your model pivots. Choose one owner and a frame order consistent with wheel presentation; an arbitrary LateUpdate order does not guarantee it runs after other visual writers. Do not move the WheelCollider mount each frame just to match a mesh. Detailed helper axis and length contracts are in the Suspension scripting chapter.

## Build aircraft landing-gear suspension

Start with deployed gear and native wheel support before adding retraction. Place a WheelCollider mount and Wheel adapter for each contact wheel, configure radius/travel and use Suspension for springs and dampers. Assign appropriate braking and steering roles: a nose/tail wheel need not be driven, and main wheels need not steer. Verify the aircraft rests on its wheels without hull overlap.

For a straight telescoping strut, use the same visual shock/hub workflow above. For a load-bending hinged leg, add `LandingGear`, author a `LandingGearPart` for each deployed/retracted assembly, then add `LandingGearSuspension` and populate its parts with `LandingGearSuspensionPart` entries. Each entry links its gear part and native WheelCollider, hinge axis and signed maximum opening angle. Set authoredAngle to the bend already present in the deployed model (zero for a straight leg).

Tune Spring Torque (N·m/rad), Damping Torque (N·m·s/rad) and Angular Inertia (kg·m²) for hinge response. The native wheel supplies support; the hinge visual response does not replace wheel spring tuning. Check that wheel/contact geometry remains aligned throughout loaded travel, and avoid adding another solver to the same leg pivot.

Test symmetric touchdown, one-wheel touchdown, taxi steering/braking and retraction separately. Coordinate gear sequencing with `LandingGearSuspension.IsStraight`, and use `ResetSuspension()` in the aircraft reset flow to clear residual bend/velocity. Let LandingGear manage contact availability during deployment; hiding the mesh alone does not retract its physical wheel. See the Aircraft chapter for the deployment and reset setup.
