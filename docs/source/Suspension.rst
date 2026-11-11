.. _uvs-suspension--suspension-setup:

Suspension setup
================

See :doc:`Crash, contact and landing effects </DamageFeedback>` for configurable impact layers, scraping, glass breakage, suspension cues and pooled particles.

Start with native wheel suspension supporting the chassis. ``Suspension`` configures the WheelColliders' springs, dampers, travel and force application. Visible linkages are separate helpers; they should follow a working physical setup rather than conceal an unsupported vehicle.

.. _uvs-suspension--inspector-quick-start:

Inspector quick start
---------------------

1. Select the vehicle root outside Play Mode. Open **Vehicle Controller > Wheels > Wheel Setup**. Add one entry per wheel, assign its native **Wheel Collider** and visual Transform, and set radius, width, mass and the steering/drive/brake roles. Use **Discover child Wheel Colliders** only for colliders belonging to this chassis Rigidbody, then review the generated entries.
2. Open **Vehicle Controller > Setup > Configuration**. Set **Suspension Travel** in metres and check chassis mass/centre of mass. Position the wheel mounts and chassis colliders so the tires can compress without immediately striking bodywork or the ground with the chassis.
3. Open **Modules > Drive > Suspension**, adding Suspension through **Add module...** if absent. Set **Spring**, **Damper** and **Target Position** for the expected load. Edit these fields here rather than the greyed-out managed values on individual WheelColliders.
4. Press **Apply vehicle configuration** and save. Enter Play Mode on flat ground and let the car settle. Check each wheel has usable travel, the body is supported, and no visual linkage is supplying a second physical support path by mistake.
5. Drive over one low bump, brake and turn. Adjust spring/damping first. Then configure **Anti Roll** under Drive and the landing settings below if needed. Add ControlArm, ShockAbsorber and other visible linkage helpers only after the physical wheel setup works.

Use :ref:`Support the vehicle <uvs-suspension--support-the-vehicle>` for tuning and :ref:`Add visible linkage <uvs-suspension--add-visible-linkage>` for model bindings. A Suspension module cannot infer wheel mounts or wheel roles from mesh names.

.. _uvs-suspension--support-the-vehicle:

Support the vehicle
-------------------

1. Check real scale, mass, centre of mass, wheel radius and chassis clearance. Configure wheel geometry through **VehicleController > Wheels > Wheel Setup**.
2. Set **Vehicle Settings > Suspension Travel** to a usable stroke in metres.
3. Add/register Suspension and set **Spring**, **Damper** and **Target Position**. Test the intended loaded vehicle, not a visually identical object with a different mass.
4. Apply vehicle configuration on flat ground. Let the vehicle settle with no drive/steering input and check that each wheel remains within usable travel.
5. Test braking, a steady turn and a small bump before adding contact-envelope or anti-roll assistance.
6. Add the visible linkage only after the contact wheels and chassis behave correctly.

Spring is stiffness in N/m and damper is in N·s/m. Greater mass needs appropriate support; increasing travel alone does not increase spring force. Target Position sets the native spring's rest target along its stroke, rather than moving the collider Transform.

.. _uvs-suspension--wheel-mount-versus-suspension-extension:

Wheel mount versus suspension extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The WheelCollider Transform/Center defines its mounting reference; the wheel hub moves through suspension travel below that reference. Applying a nonzero suspension stroke can therefore place the hub/visual lower than a setup tested with zero Suspension Distance. This does not necessarily mean the mount Transform moved.

Set the intended radius, travel and rest/load first, then position the mount/centre to fit the vehicle at that loaded ride height. Keep appropriate compression/rebound clearance. Zeroing native Suspension Distance afterward is not a persistent offset: the module can overwrite it on configuration, and it removes the intended stroke.

Bound Wheel/native fields are greyed out where a vehicle/module owns them. Edit Wheel Setup, vehicle travel, Suspension or an assigned shock override as indicated. Settings written to native springs can remain installed when the setup module is disabled; disabling it is not equivalent to restoring a completely untouched WheelCollider.

.. _uvs-suspension--landing-compression-and-rebound:

Landing compression and rebound
-------------------------------

**Landing Response** is enabled by default for grounded drive profiles. After a genuine flight, spring stiffness and damping temporarily soften and the native expansion limiter can be released so the wheels compress under the landing load and the springs produce a visible, smooth body rebound. With the optional whole-vehicle bounce disabled, the response changes only native spring/damper coefficients without applying an upward impulse or animating the chassis; mass, spring rate and available wheel travel still determine the motion.

-  **Landing Minimum Air Time** (0.15 s) ignores small wheel-contact flickers.
-  **Landing Minimum Speed** (1.5 m/s) and **Landing Full Response Speed** (4.5 m/s) scale the effect with downward contact speed relative to the landing surface, including chassis rotation and moving surfaces.
-  **Landing Spring Multiplier** (0.6) retains 60% of each authored spring stiffness at full response. Values below one allow a deeper initial squat. The baseline includes each active ShockAbsorber override; the response never overwrites those authored values.
-  **Landing Bump Stop Multiplier** (1.5) progressively increases native stiffness over the last 20% of compression, including the next predicted stroke. The initial stroke stays soft while the end of travel absorbs the impact and preserves a stronger rebound.
-  **Landing Damper Multiplier** (0.2) is the fraction of ordinary damping retained at full response. Increase it for less bounce; lower it for a softer, livelier landing.
-  **Landing Response Duration** (0.9 s) is the recovery window at full landing strength.
-  **Landing Minimum Cycles** (2.5) extends that window using the softened spring period, ``2π √(chassis mass / total softened wheel stiffness)``. A heavy, soft vehicle gets more time than a short-travel car. Both the duration and cycle allowance scale down smoothly for weaker impacts. Set cycles to zero to use only the speed-scaled duration.
-  **Allow Landing Rebound** temporarily releases **Limit Expansion Velocity** during the response. Keep this enabled when the vehicle lands rigidly with little upward spring recovery.

With **Allow Landing Rebound**, the native expansion limiter stays released until actual suspension stroke and supported-body motion remain quiet for 0.25 s, after response recovery and assisted bounces finish. It does not re-enable in the middle of a stroke when a response timer expires. Optional arcade rise damping also yields during that settling period.

The springs and dampers are prepared during descent, before the first wheel contact. Spring stiffness stays low for the initial compression, then recovers smoothly through the first rebound. Damping stays reduced longer, allowing subsequent up/down oscillations before it progressively returns over the remaining spring cycles. Keeping the springs weak for the whole window would lose rebound strength and encourage bottoming on short-travel cars. Intermediate landings retain progressively more authored spring stiffness and damping, so smaller impacts produce smaller, faster-decaying oscillations. On contact, severity is refined against the actual surface normal and motion. A rebound cannot rearm itself: the response must finish and wheel support settle before a new landing is eligible. Side/roof contacts do not receive this wheel-landing response. Aircraft and water profiles retain their own suspension policy.

The response composes with degressive damping, ContactEnvelope and each active ShockAbsorber wheel override. Optional arcade bump damping fades during the landing response instead of immediately removing the rebound. Normal driving settings remain unchanged after the short response; disabling the component or teleporting restores authored spring stiffness, native damping and the configured expansion limit. Turning off **Landing Response** restores ordinary behavior.

Very short travel, a chassis collider touching the ground before its wheels, or an overly stiff spring can still prevent useful compression. Correct those limits before reducing damping further. See :doc:`Collisions and stabilization </CollisionsAndStabilization>` for airborne spin and body-contact behavior.

Weak wheel landings keep the springs closer to their normal stiffness and retain more damping, producing faster, smaller oscillations that settle sooner. Landing strength grows quadratically between **Landing Minimum Speed** and **Landing Full Response Speed**, using downward contact speed relative to the surface rather than a fixed drop height. Full-strength duration and cycle settings scale down for weak impacts, with a smooth recovery. Progressive bounce grows smoothly with qualifying impact speed; the legacy single-impulse mode retains its upper-half strength gate.

.. _uvs-suspension--optional-whole-vehicle-landing-bounce:

Optional whole-vehicle landing bounce
-------------------------------------

**Landing Ground Bounce** under **Suspension → Optional Whole-Vehicle Landing Bounce** is enabled by default for grounded profiles, together with **Landing Response**. Turn the checkbox off to keep only suspension compression and body oscillation. For hard impacts, it supplements the native suspension during rebound, allowing the whole vehicle and its tires to leave the ground after a wheel landing. With progressive bounce, assistance scales smoothly above Landing Minimum Speed. Directional landings use the recorded airborne approach speed as well as the first wheel contact, so a gentle first axle touch does not discard the landing energy. This remains bounded rebound assistance alongside the native wheel springs.

**Directional Landing Response** retains the airborne approach speed for spring/damper preparation when an angled body touches before the wheels. Each wheel then gets its own initial compression phase, so the later axle does not inherit the first axle's already recovered spring. The stored speed only prepares suspension coefficients; assisted bounce energy still comes from actual wheel touchdown speed.

With **Directional Landing Bounce**, the release acts between the centre of mass and the average supporting wheel contact. **Landing Contact Leverage** sets that blend. Partial axle/side support can produce pitch/roll, following the local surface normal and point velocity; effective point mass includes chassis inertia. **Landing Bounce Maximum Tilt** bounds eligible wheel landings (55 degrees by default), while **Landing Bounce Maximum Rotation** bounds the additional angular change. Side and roof landings remain passive. Disable directional bounce for the original central impulse and broad-support gate. Dynamic support receives the opposite impulse.

**Progressive Landing Bounce** is enabled by default. It releases force over the rising, loaded suspension stroke instead of applying a single launch impulse. Force falls as the suspension extends, and the first release spends a finite allowance that includes lifting the chassis through the remaining suspension travel. Existing upward motion counts toward the rebound target; no push is applied without wheel support. Progressive mode assists only the first release; later bounces use native springs and dampers. A takeoff already produced by native suspension also consumes that first opportunity. **Progressive Landing Recovery** (0.5) controls the initial recovery. During subsequent supported oscillations, **Landing Settling Damping Ratio** (0.25) keeps damping near a steady mass/spring-based target. Normal damping returns smoothly once wheel stroke and chassis motion have become quiet. A ratio of 1 is critical damping; smaller values allow oscillation. The target does not increase authored damping, and per-wheel damper overrides remain respected. Switch Progressive Landing Bounce off to compare with the previous single-impulse response and its original recovery duration. The first push waits for the initial squat and the rising suspension stroke. Directional bounce accepts partial wheel support; central bounce requires at least half the operational wheels. It accounts for the travel still to extend, so a long-travel monster truck can also clear the ground. It adds only the separation speed missing from the existing native rebound. Directional leverage can add bounded pitch/roll. On dynamic surfaces, it uses relative contact velocity and effective mass and gives the contacted surface an equal opposite impulse.

-  **Landing Bounce Restitution** (0.45) scales the impact speed used for the next hop. In legacy mode, a later assisted hop is bounded by both its own impact speed and the previous hop budget, each reduced by restitution.
-  **Landing Bounce Maximum Speed** (2 m/s) caps the requested residual upward speed above full tire extension. Remaining native spring work can affect actual flight height; this is a target cap, not a velocity clamp.
-  **Landing Bounce Maximum Count** (3) bounds the assisted sequence in legacy mode. Progressive mode uses only one assisted release. Speeds below 0.25 m/s stop the sequence early.

Only a genuine airborne wheel landing can start a sequence. Tiny contact flickers, side/roof landings and continuous grounded motion cannot start repeated pushes. Later hops can have shorter flight times than the original landing threshold, but their speed budgets keep shrinking. Optional arcade rise damping and the expansion limiter yield during an active bounce sequence. Turning the option off, teleporting, disabling Landing Response or disabling Suspension clears pending pushes.

``LandingBounceCount`` reports releases in the current/last episode; ``LandingBounceSpeed`` reports the last target residual speed. The ordinary spring/damper landing response remains available with **Landing Ground Bounce** off.

Demo resets align grounded vehicles with gravity while preserving their heading, including when the vehicle was first selected while tilted. The controller’s ``Teleport`` and ``ResetVehicle`` APIs preserve the supplied rotation and clear motion on attached dynamic bodies so moving controls and panels cannot twist the chassis immediately after reset.

.. _uvs-suspension--spring-damping-and-bump-response:

Spring, damping and bump response
---------------------------------

Tune static support before damping. If the suspension already sits at an end stop under normal load, inspect mass, spring, travel and target rather than trying to cure it with damping. Once support is reasonable, add enough damping to settle repeated oscillation without making every bump harsh.

**Degressive Damping** limits high-speed compression damping above **Damper Blowoff Speed**, while retaining rebound damping and low-speed body control. Compression blowoff does not reduce the damper on the extension stroke, so stored spring energy can dissipate instead of launching the chassis. It is intended to avoid a sharp road input generating an excessive linear damper impulse. It does not add travel or change the tire's geometry.

**Wheel Damping Rate** damps native wheel rotation, not suspension stroke. **Limit Expansion Velocity** is a separate native suspension option. Keep those distinct when a tire spins too long versus when the body bounces.

**Arcade Bump Damping** is optional extra supported-body upward-motion damping. Its rise-speed/response settings affect the chassis when sufficiently supported. Tune physical travel/contact first; this assistance should not be the first response to an overlapping collider.

.. _uvs-suspension--force-application-and-body-sway:

Force application and body sway
-------------------------------

With **Automatic Force Application** enabled, the module places wheel force application relative to the chassis centre of mass. **Force Offset Below Center Of Mass** and **Body Sway Travel Ratio** affect the lever arm and resulting pitch/roll. With automatic placement off, **Force Application Height** supplies the explicit baseline.

This force point is not the suspension mount or a visual hub offset. Changing it affects body response to tire forces; changing the mesh position does not. Contact-envelope radius corrections are accounted for so force placement remains consistent with the current effective support radius.

.. _uvs-suspension--anti-roll-support:

Anti-roll support
-----------------

Add/enable ``AntiRoll`` explicitly, create an axle pair using the left/right ``Wheel`` adapters and set **Stiffness**. It transfers forces between supported sides based on their suspension travel difference; it does not overwrite chassis orientation.

The pair requires both wheels to have native ground support. At an edge with one wheel airborne, it does not apply only half of an axle force that would artificially lift the chassis. Excess stiffness can reduce compliant behavior over uneven ground, so compare a steady corner and a one-sided bump independently.

.. _uvs-suspension--add-visible-linkage:

Add visible linkage
-------------------

Choose helpers based on the actual model assembly:

+--------------------+-----------------------------------------------------------------+
| Helper             | Model purpose                                                   |
+====================+=================================================================+
| ``ShockAbsorber``  | Telescoping casing and piston between chassis/wheel attachments |
+--------------------+-----------------------------------------------------------------+
| ``ControlArm``     | Arm geometry between chassis and moving hub                     |
+--------------------+-----------------------------------------------------------------+
| ``SuspensionHub``  | Hub presentation following wheel support/steering geometry      |
+--------------------+-----------------------------------------------------------------+
| ``SteeringTieRod`` | Steering linkage and its geometric steering relationship        |
+--------------------+-----------------------------------------------------------------+
| ``SuspensionAxle`` | Axle assembly presentation                                      |
+--------------------+-----------------------------------------------------------------+
| ``HalfShaft``      | Shaft endpoints/orientation as suspension moves                 |
+--------------------+-----------------------------------------------------------------+

Assign the relevant wheel, pivots and attachment points at the actual model joints. Keep import scale/orientation offsets on child meshes. Test full compression, rebound and both steering locks; do not set angular/length limits that prevent the assembly reaching a valid wheel pose.

A ShockAbsorber's casing/piston slide rather than being treated as arbitrarily stretchable meshes. Their physical lengths and allowable minimum/maximum assembly length must agree with the mesh. A visual helper cannot force incompatible attachment points to meet.

.. _uvs-suspension--optional-physical-shock-override:

Optional physical shock override
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assign a shock's native WheelCollider and enable **Override Wheel Physics** to supply per-wheel spring, damper, travel and target through Suspension. Use one override per wheel. The helper must belong to the same vehicle and be active for that override to apply; a visual-only shock should leave it off.

**Motion Ratio** is shock travel divided by wheel travel. Wheel-equivalent stiffness and damping scale with its square. For a ratio of 0.5, a shock stiffness of 40000 N/m gives 10000 N/m at the wheel, not 20000. Choose wheel travel separately rather than confusing mesh length with suspension stroke.

When an override is active, changing the global spring may not change that wheel. Reconfigure after assigning/changing the relevant shock references. See :doc:`linkage contracts </Scripting/Suspension>` for detailed axis/length conversion and code tuning.

.. _uvs-suspension--wheel-spin-and-coasting:

Wheel spin and coasting
-----------------------

``WheelDynamics`` derives airborne rotational damping using **Airborne Spin Half Life**, wheel inertia and the configured ground damping baseline. It does not add engine propulsion or suspension spring force. Test a jump to distinguish tire spin loss from a drivetrain shift decision.

``Coasting`` uses a tiny **Contact Release Torque** to release native low-speed sticky tire behavior when rolling/towing on slopes. **Release Below RPM** and **Minimum Slope Degrees** bound that assistance. It respects brake/drive priorities and is not an engine or parking-brake replacement.

Configure parking through Brakes/parking policy and trailer braking, rather than trying to make damping statically hold a vehicle forever. Keep visual tire settling separate too: Wheel's visual suspension smoothing changes the rendered hub interpolation, not the native spring support.

.. _uvs-suspension--troubleshoot:

Troubleshoot
------------

+-----------------------------------------+--------------------------------------------------------------------+
| Observation                             | First adjustment                                                   |
+=========================================+====================================================================+
| Suspension rests at an end stop         | Mass, travel, spring and target position                           |
+-----------------------------------------+--------------------------------------------------------------------+
| Body repeatedly bounces                 | Damping after static support is correct                            |
+-----------------------------------------+--------------------------------------------------------------------+
| Sharp bumps are excessively harsh       | Available travel, degressive damping and collider clearance        |
+-----------------------------------------+--------------------------------------------------------------------+
| Wheel appears lower after Apply         | Mount/centre versus loaded stroke; vehicle owns native travel      |
+-----------------------------------------+--------------------------------------------------------------------+
| Only one wheel ignores global tuning    | Assigned physical shock override                                   |
+-----------------------------------------+--------------------------------------------------------------------+
| Chassis looks rigid or lifts at corners | Force application and anti-roll settings                           |
+-----------------------------------------+--------------------------------------------------------------------+
| Linkage pops or cannot reach            | Attachment geometry, length limits and competing Transform writers |
+-----------------------------------------+--------------------------------------------------------------------+

Aircraft hinged gear has a separate :ref:`setup <uvs-aircraft--hinged-gear-suspension>`. For rolling curbs and solid obstacles, continue with :doc:`Contact envelope </ContactEnvelope>` and :doc:`Tire collision </TireCollision>`.

.. _uvs-suspension--performance-tuning:

Performance tuning
------------------

ContactEnvelope exposes edge-refinement and probe-interval controls; Suspension exposes vehicle-wide native wheel substeps. See :ref:`Inspector performance settings <uvs-performance--inspector-performance-settings>` for cost/precision tradeoffs and when to apply changes.

.. _uvs-suspension--scene-view-gizmos:

Scene view gizmos
-----------------

Select the vehicle root to preview its suspension helpers together, or select an individual helper to inspect its geometry. These guides also work outside Play mode. Expand **Gizmos** at the bottom of each component Inspector to control anchors, connecting lines, reference axes, ranges and labels separately. Components with editable anchors also expose **Show editing handles**.

-  **Suspension** shows each wheel’s full compression/extension stroke in yellow and its unloaded spring target in green. Outside Play mode the preview uses vehicle travel and Suspension settings, including enabled per-wheel ShockAbsorber overrides; in Play mode it uses the configured wheel values. The target is not the loaded ride height.
-  **ShockAbsorber** shows both mounting eyes, their current separation and minimum/maximum mechanical length. Red indicates travel outside the configured range.
-  **SuspensionHub**, **SuspensionAxle**, **ShockAbsorber** and **HalfShaft** show their configured rotation permissions and angular limits in the same neutral frames used by their pose solvers.
-  **ControlArm** shows the arm sweep when Constrain Hub To Arc is enabled, or the native wheel travel when it is disabled. **HalfShaft** also shows the CV joint angle range in the current bending plane.
-  **SteeringTieRod** shows both steering directions, rack travel, knuckle rotation limits and rod articulation limits.

Rotation axes use red X, green Y and blue Z. A locked axis is marked as locked; an unrestricted axis has a full circle. The arcs describe separate Euler-axis settings, rather than a combined reachable volume. Gizmo switches only affect the Scene view and do not change suspension physics.

.. _uvs-suspension--build-your-own-visual-suspension-assembly:

Build your own visual suspension assembly
-----------------------------------------

1. Finish the physical wheel first: keep the WheelCollider mount and ``Wheel`` adapter on the vehicle, assign its visual wheel root, and verify loaded ride height and travel. Create separate clean pivots for the hub, arms, shock casing/piston and shafts; keep model orientation corrections on child meshes.
2. Add only the helpers matching your model. Use ``SuspensionHub`` for the upright, ``ControlArm`` for chassis-to-hub arms, ``ShockAbsorber`` for telescoping sections, ``SteeringTieRod`` for rack/knuckle linkage, ``HalfShaft`` for the driven shaft and ``SuspensionAxle`` for an axle assembly. Several arms may follow the same wheel. Enable **Constrain Hub To Arc** for a fixed-length wishbone path. Disable it to follow the native wheel suspension axis without changing track width, as in the Monster Truck demo. In that mode the visual arm branches fit between their anchors; they do not enforce a fixed arm length.
3. Assign wheel references, chassis and moving-side attachment points at the actual joint centres. Set each helper's axes, neutral orientation, lengths and allowed angles to match the mesh. Keep chassis anchors outside the moving assembly so a solver does not move its own reference.
4. Leave shock Override Wheel Physics off for appearance-only assemblies. Enable it only when this shock deliberately owns that wheel's physical settings; assign its native WheelCollider and account for motion ratio. Apply vehicle configuration after changing physical settings.
5. Check the Scene gizmos, then test full compression, full droop and both steering locks in Play mode. Watch casing/piston overlap, shaft reach, joint limits and tire clearance. Correct geometry before smoothing. Remove Animator tracks or scripts that also write the solved pivots.

For a linkage geometry the supplied helpers cannot represent, write a separate visual component that reads the resolved wheel pose and moves only your model pivots. Choose one owner and a frame order consistent with wheel presentation; an arbitrary LateUpdate order does not guarantee it runs after other visual writers. Do not move the WheelCollider mount each frame just to match a mesh. Detailed helper axis and length contracts are in the Suspension scripting chapter.

.. _uvs-suspension--build-aircraft-landing-gear-suspension:

Build aircraft landing-gear suspension
--------------------------------------

Start with deployed gear and native wheel support before adding retraction. Place a WheelCollider mount and Wheel adapter for each contact wheel, configure radius/travel and use Suspension for springs and dampers. Assign appropriate braking and steering roles: a nose/tail wheel need not be driven, and main wheels need not steer. Verify the aircraft rests on its wheels without hull overlap.

For a straight telescoping strut, use the same visual shock/hub workflow above. For a load-bending hinged leg, add ``LandingGear``, author a ``LandingGearPart`` for each deployed/retracted assembly, then add ``LandingGearSuspension`` and populate its parts with ``LandingGearSuspensionPart`` entries. Each entry links its gear part and native WheelCollider, hinge axis and signed maximum opening angle. Set authoredAngle to the bend already present in the deployed model (zero for a straight leg).

Tune Spring Torque (N·m/rad), Damping Torque (N·m·s/rad) and Angular Inertia (kg·m²) for hinge response. The native wheel supplies support; the hinge visual response does not replace wheel spring tuning. Check that wheel/contact geometry remains aligned throughout loaded travel, and avoid adding another solver to the same leg pivot.

Test symmetric touchdown, one-wheel touchdown, taxi steering/braking and retraction separately. Coordinate gear sequencing with ``LandingGearSuspension.IsStraight``, and use ``ResetSuspension()`` in the aircraft reset flow to clear residual bend/velocity. Let LandingGear manage contact availability during deployment; hiding the mesh alone does not retract its physical wheel. See the Aircraft chapter for the deployment and reset setup.
