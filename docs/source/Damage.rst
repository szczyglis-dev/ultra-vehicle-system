.. _uvs-damage--opening-parts-and-collision-damage:

Opening parts and collision damage
==================================

See :doc:`Crash, contact and landing effects </DamageFeedback>` for configurable impact layers, scraping, glass breakage, suspension cues and pooled particles.

Physical crash response, side/roof sliding and optional return to the wheels are configured separately in :doc:`Collisions and stabilization </CollisionsAndStabilization>`.

.. _uvs-damage--optional-presentation-components:

Optional presentation components
--------------------------------

**Damage** calculates damage and detachment. **Mesh Deformation** receives deformation requests before parts detach; **Damage Feedback** receives accepted hits for pooled visuals. Assign their **Damage** source. Create Vehicle includes both receivers; remove or disable either independently. Dent limits are configured on Mesh Deformation, and visual pool limits on Damage Feedback. Shared presentation profiles are configured on Damage Feedback for reuse by visuals and Damage Audio; physics settings remain on Damage.

.. _uvs-damage--moving-parts-damage-parts-and-wheel-parts:

Moving parts, damage parts and wheel parts
------------------------------------------

A ``MovingPart`` controls a part's motion: opening, closing, rotation or translation. ``VehicleBodyPart`` is the separate hinged-panel helper for named doors, hoods and hatches operated by ``Body``. Use these when a model should move during normal operation; opening a door does not itself damage it.

A ``DamagePart`` defines a damage boundary: which meshes and colliders share accumulated damage, a material and a detachment threshold. Add it to fixed panels as well as moving doors. A door can have both responsibilities: its moving helper operates the hinge, while its damage helper receives impacts and can release it.

``WheelPart`` is the wheel-specific damage helper derived from ``DamagePart``. Place it on the visual wheel group and link the ``Wheel`` adapter on the separate collider mount. It also handles wheel disconnection and restoration; an ordinary panel damage helper cannot replace that integration.

Choose **deformation**, **detachment**, or both. Deformation dents supported readable render meshes while the part stays mounted; it does not reshape the physics collider. Detachment releases the whole damage boundary as independent Rigidbody debris and disables its attached mechanisms as appropriate. Their global switches and per-part multipliers are independent, so a rigid detachable lamp need not deform and a dentable chassis need not detach.

This guide configures collision damage, visual mesh dents, detachable groups and repair boundaries. Build working doors/hatches through :doc:`Moving parts </MovingParts>` first. Opening state, accumulated damage and detached debris are independent responsibilities.

.. _uvs-damage--add-a-door-or-hatch:

Add a door or hatch
-------------------

The complete hinge/ID registry workflow is in :ref:`Moving parts: doors and hatches <uvs-movingparts--add-a-door-or-hatch>`. Return here when that part should also accumulate damage, dent or detach. A body-opening helper is optional on a fixed damage boundary.

.. _uvs-damage--add-collision-damage:

Add collision damage
--------------------

For a click-by-click setup, start with :ref:`Inspector workflow and part registries <uvs-damage--inspector-workflow-and-part-registries>` below. The list in Body is an additional registry, not a complete view of the vehicle's damage parts.

1. Add/register ``Damage`` on the vehicle. It requires ``VehicleMeshDeformation``; check both components are present and enabled for visual dents.
2. Add a ``DamagePart`` to each intended boundary, such as a bumper, hood or door group.
3. Assign those helpers in **Damage > Parts**, give them stable distinct **Part Id** values and set their material classification.
4. Keep the root chassis outside detachable groups. The vehicle root itself cannot become an ordinary detached part.
5. Fit simple collision proxies and assign each part's supported **Deformable Meshes**.
6. Set minimum impact speed, damage multiplier/radius and the part-specific policies below.
7. Test one moderate controlled impact before testing a high-speed crash or several nested groups.

A boundary owns the meshes/colliders under it until another nested DamagePart takes ownership. Assign a mesh to its actual nearest boundary rather than copying every child mesh into every ancestor list. Root/bodywork hierarchy therefore affects which part receives a hit.

.. _uvs-damage--inspector-workflow-and-part-registries:

Inspector workflow and part registries
--------------------------------------

Configure the vehicle outside Play Mode so changes are saved. Select the vehicle root in the Hierarchy and use **Vehicle Controller > Modules** to reach its grouped module inspectors. Select the actual panel or wheel child in the Hierarchy to add/edit its part components. VehicleBodyPart, DamagePart and WheelPart are components on those child objects, rather than separate root vehicle modules.

.. _uvs-damage--which-parts-list-should-i-use:

Which Parts list should I use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Inspector location                       | Component reference accepted    | Purpose                                                                                                                                                              |
+==========================================+=================================+======================================================================================================================================================================+
| Modules > Exterior > Body > Parts        | VehicleBodyPart                 | Doors, hood, trunk and other panels operated by Body's open/close actions. This does not register collision damage.                                                  |
+------------------------------------------+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Modules > Physics > Damage > Parts       | DamagePart, including WheelPart | Main registry of damageable boundaries. Use this as the usual place to register a new bumper, door or other damageable group.                                        |
+------------------------------------------+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Modules > Exterior > Body > Damage Parts | DamagePart, including WheelPart | Additional damage registrations supplied by this Body. Damage merges them into its own registry when configured/refreshed. This list does not mirror Damage > Parts. |
+------------------------------------------+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Register a damage helper in either damage registry; adding the same reference to both is unnecessary because Damage deduplicates them. Body > Parts is independent: a damageable opening door needs its VehicleBodyPart registered there and its DamagePart registered in a damage registry.

**Car example:** Body > Parts contains the two doors, hood and trunk. Body > Damage Parts contains only the front-left WheelPart; other damage helpers are assigned directly in Physics > Damage > Parts. Seeing one wheel in the Body list therefore does not mean the car has only one damageable part.

.. _uvs-damage--add-a-fixed-damageable-part-for-example-a-bumper:

Add a fixed damageable part, for example a bumper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In the Hierarchy, select or create a child group containing only the bumper's geometry and collision shapes. Keep the permanent chassis outside it. Fit a simple BoxCollider or other suitable solid collision proxy; a MeshCollider intended for dynamic debris must be convex. Do not add a separate Rigidbody merely to register an attached fixed bumper: the detachment code prepares its debris body when released.
2. On that group, choose **Add Component > UltraVehicleSystem > Exterior > Parts > Damage Part**. Give **Part Id** a stable unique value, for example ``BumperFront``. Select **Material** and optionally **Material Id** for the impact profile classification.
3. Enable **Damage Enabled**. Set **Detach Threshold**, **Detachment Multiplier** and **Mass**. A Detachment Multiplier of zero prevents collision-driven detachment; it does not turn off damage accumulation.
4. If dents are wanted, populate **Deformable Meshes** with this boundary's readable MeshFilter components and use a positive **Deformation Multiplier**. If only detachment is wanted, set that multiplier to zero. Do not assign meshes owned by another nested DamagePart.
5. Select the vehicle root, open **Modules > Physics**, and expand **Damage**. If absent, add it through **Add module...** by selecting Damage; use the same module action to add Body under Exterior only if you need a Body registry or opening panels.
6. Expand **Damage > Parts**, press **+**, and drag the bumper's DamagePart component header into the new element. Dragging its GameObject also works when Unity can resolve the required component. Alternatively, place this reference in **Exterior > Body > Damage Parts**; do not put it in Body > Parts, which accepts VehicleBodyPart instead.
7. In Damage, enable **Damage Enabled** and **Detachment Enabled** for collision-triggered release. Enable **Deformation Enabled** and the required VehicleMeshDeformation component if dents are intended. Tune **Minimum Impact Speed**, **Damage Multiplier** and **Impact Radius** for the vehicle.
8. Press **Apply vehicle configuration** at the bottom of the vehicle Inspector after editing registrations. This configures Damage and merges its part references. **Discover and order vehicle modules** finds modules; it does not automatically register every ordinary DamagePart child. Save the scene and apply intended prefab overrides, or save the prefab when editing it directly.
9. Enter Play Mode and drive the part into a controlled obstacle. Check that the intended boundary receives damage and releases, the permanent chassis remains solid, and repair/reset remounts retained debris. For a bumper that reveals an otherwise open nose, configure :ref:`Detached Vehicle Colliders <uvs-damage--protect-exposed-chassis-after-detachment>` as well.

.. _uvs-damage--add-an-opening-panel-that-can-also-be-damaged:

Add an opening panel that can also be damaged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Follow :ref:`Add a door or hatch <uvs-movingparts--add-a-door-or-hatch>` to create its pivot, VehicleBodyPart and Body > Parts entry. Confirm normal opening/closing before adding damage.
2. Add DamagePart to the same door/panel group when the whole opening panel should detach as one boundary. Give it a stable Part Id, configure its collision shapes and damage settings, and register that DamagePart in **Damage > Parts** or **Body > Damage Parts** as above.
3. Keep the frame on the permanent chassis. Keep any separately damageable glass/lamp group under its own DamagePart and assign its meshes to that boundary. Do not make two motion components control the same Transform.
4. Test both closed and open impacts. **Use Physics** on VehicleBodyPart selects a physical hinge; it is separate from damage admission and threshold detachment. Releasing the damage group also releases its body-opening helpers; another Open command does not repair it.

.. _uvs-damage--add-a-damageable-wheel:

Add a damageable wheel
~~~~~~~~~~~~~~~~~~~~~~

Use the :ref:`wheel Inspector tutorial <uvs-damage--tutorial-make-one-wheel-damageable>`. Add **Wheel Part** on the visual wheel group and assign **Wheel** to the adapter on the separate WheelCollider mount. Register it in either damage list, then apply vehicle configuration. Owned WheelPart children are also discovered during Damage configuration/refresh; ordinary DamagePart children are not discovered this way. Do not add both WheelPart and an ordinary DamagePart to the same visual wheel group.

.. _uvs-damage--check-the-registration-when-something-is-missing:

Check the registration when something is missing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Symptom                                               | What to check in the Inspector                                                                                                                  |
+=======================================================+=================================================================================================================================================+
| Body > Damage Parts shows only a wheel                | Open Physics > Damage > Parts for the main registry. The Body list is not a summary of all parts.                                               |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| A new DamagePart child never receives routed hits     | Assign it to one damage registry and apply vehicle configuration. Merely adding the child component is insufficient for an ordinary DamagePart. |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| A door opens but does not take damage                 | Body > Parts only registers opening behavior. Add/register DamagePart and enable the global and per-part damage switches.                       |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| A door takes damage but Body cannot open it           | Add VehicleBodyPart to the hinge group and reference it in Body > Parts; verify its Part Id and hinge settings.                                 |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| A part takes damage but never detaches                | Check global Detachment Enabled, the part's positive Detachment Multiplier and Detach Threshold.                                                |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| A released bumper leaves a hole in the collision hull | Add a permanent chassis collider through that part's Detached Vehicle Colliders list.                                                           |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Changes disappear after stopping Play Mode            | Perform authoring outside Play Mode and save the scene/prefab.                                                                                  |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-damage--protect-exposed-chassis-after-detachment:

Protect exposed chassis after detachment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use **Damage Part > Detached Vehicle Colliders** for collision shapes that belong to the structure revealed by a missing panel. The list is empty by default; clearing it disables this feature for that part.

1. Create a simple solid collider under the permanent chassis, outside all detachable groups. Keep its GameObject active and uncheck the collider's **Enabled** checkbox.
2. Fit the shape to the exposed frame, slightly behind the attached bumper. Preserve ground clearance and avoid wheel travel. A BoxCollider is usually sufficient; no additional Rigidbody is required.
3. Assign it to the bumper's **Detached Vehicle Colliders** list before startup. Give each fallback collider one owning DamagePart; duplicate owners are warned about and rejected at startup.
4. Detach the bumper: the shape becomes enabled before ``Detached`` is raised. Existing debris clearance exclusions prevent the released bumper from colliding immediately with this newly exposed frame. Seated passenger exclusions are also applied.
5. Use ``RepairFully``, the registered Damage repair methods, or vehicle reset to remount retained parts and restore the fallback collider's captured enabled state. Incremental ``Repair(amount)`` does not remount a part or change its exposed structure.

The Car demo and sample prefabs configure **Front bumper** with **Exposed front frame Collider**, an initially disabled chassis BoxCollider. Its inset face protects the open nose after bumper release. Attached driving uses the original bumper collider. The fallback bottom is above the original bumper bottom to retain ramp clearance.

Activation is event-driven: no extra update loop, raycasts, penetration queries, solver iterations or Rigidbody are added. Once enabled, the simple compound shape participates in normal native physics contacts. Missing, destroyed and invalid references are safe to skip; triggers, WheelColliders, colliders inside the detached part, foreign vehicles and shapes on separate rigidbodies are rejected when repair state is captured. Author disabled shapes; an initially enabled shape retains that authored state after full repair. Disabling or deleting detached debris does not remove the exposed chassis protection. Destroyed parts still require an application reconstruction policy.

.. _uvs-damage--route-and-scale-a-hit:

Route and scale a hit
~~~~~~~~~~~~~~~~~~~~~

Collision response uses real contact data. When a manifold contains several contacts, the contact with the greatest normal impact speed is selected (the deepest contact breaks ties). Its position is projected along the contact normal onto the struck collider surface, so overlapping shapes do not place impact effects inside the obstacle. If the surface query fails, the original contact point is retained. The built-in severity uses relative speed into the surface normal above **Minimum Impact Speed**, then applies the global multiplier and distance falloff inside **Impact Radius**. Tangential rolling/sliding speed alone is not the same as impact severity. This is tunable gameplay damage, not a complete material/energy failure simulation.

The system excludes appropriate self/support-only contacts rather than damaging the chassis from every wheel callback. A collision with no valid contact is not treated as a body hit at a fallback origin.

For scripted hits, use ``ApplyImpact(point, direction, amount)`` or the copied-impact API. The explicit amount is application severity routed through the configured part/radius policies; it is not automatically interpreted as a collision speed or explosion impulse. See :doc:`Damage scripting </Scripting/Damage>` for exact event/order contracts.

.. _uvs-damage--independent-damage-policies:

Independent damage policies
---------------------------

+-----------------------------+-----------------------------------------------------------------------------------------------------+
| Setting                     | What it controls                                                                                    |
+=============================+=====================================================================================================+
| Damage Enabled              | Global admission of future damage; each DamagePart/WheelPart also has its own Damage Enabled switch |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| Deformation Enabled         | Future visual dents                                                                                 |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| Detachment Enabled          | Future threshold-driven part release                                                                |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| Part Deformation Multiplier | Relative dent response; zero suppresses dents for this part                                         |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| Part Detachment Multiplier  | Threshold contribution; zero suppresses collision detachment                                        |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| Detach Threshold            | Accumulated effective damage required for release                                                   |
+-----------------------------+-----------------------------------------------------------------------------------------------------+

For example, a rigid glass/lamp group can accumulate damage or detach while its deformation multiplier is zero. Disabling future damage does not erase existing accumulation, dents or debris. A direct low-level part action is not interchangeable with a routed collision hit.

Use ``Damage.Hit`` for accepted routed hit information and part events for damage/repair/detachment transitions. Place custom lamp failure, glass effects or health rules at an appropriate accepted-state boundary instead of running the same action from both raw collision and routed damage events.

.. _uvs-damage--prepare-dentable-meshes:

Prepare dentable meshes
-----------------------

Use readable ``MeshFilter`` meshes with enough vertices in the region that should deform. Enable Read/Write on their model import settings where needed. A sparse flat panel cannot show a detailed local dent merely because the radius is small.

This visual path is not a general SkinnedMeshRenderer deformation system. Simple physics collision proxies remain separate; deforming render vertices does not automatically rebuild the chassis collider into the same dented shape.

**Dent Per Damage** scales vertex displacement and **Maximum Dent** caps total displacement from the original rest shape. Check the same part under repeated hits so the cap behaves as expected. Increasing mesh density increases deformation/upload cost; use representative vehicle/impact counts in performance tests.

The component creates working mesh instances rather than editing every shared source mesh globally. Multiple hits can accumulate before the render upload; ``DeformationChanged`` is a mesh-update boundary, not another damage admission. ``RestoreShape()`` restores prepared mesh shapes without inventing missing/deleted geometry.

.. _uvs-damage--detachment-and-debris:

Detachment and debris
---------------------

A detachable group needs suitable colliders and a sensible **Mass** for its independent Rigidbody. On release it leaves the vehicle hierarchy and keeps appropriate carrier/hinged-body motion. Child body-opening helpers are released too, so another motion component should not continue pulling the debris toward the vehicle.

**Generate Missing Debris Collider** supplies a simple box from the damage boundary's mesh bounds if it has no solid collider. **Debris Collider Minimum Thickness** prevents zero-thickness glass/lamp shapes. This covers visual-only groups such as the demo's detachable lamps and windshield. Existing authored collision shapes are retained. The generated shape activates only on release, disables on repair and is reused on later releases; disable this option when a custom debris effect owns collision behavior.

**Released Collision Delay** is the minimum delay before former vehicle contact exclusions can be restored. Overlapping pairs wait for clearance; it is not an unconditional timer that forces interpenetrating debris to collide immediately. This reduces an explosive correction when a door/panel initially overlaps its former hull.

Detached objects are application lifetime objects. Decide whether to keep them, pool them or remove them after a budgeted interval. Disabling collision damage on the vehicle is not debris cleanup. Test release with a moving vehicle and an already swinging physical door, not only a parked static panel.

.. _uvs-damage--released-panel-collision-stability:

Released panel collision stability
----------------------------------

Released Damage Parts retain their physical collision shape and inherited velocity. Their Rigidbody uses swept Continuous Dynamic detection, avoiding speculative contacts from thin convex edges. Use simple convex collision proxies with a small but nonzero thickness; render meshes do not need to match every collision edge.

**Debris Depenetration Speed** limits only how quickly the solver separates an overlapping released part (default 2 m/s). It does not cap ordinary travel speed or suppress real contacts. **Debris Angular Damping** reduces prolonged spinning (default 0.5). Both settings are applied on release. The existing Released Collision Delay still ignores former-vehicle pairs until the minimum delay has elapsed and their shapes have separated; later contacts with the vehicle remain physical.

**Stabilize Debris Contacts** bounds energy supplied to a released part by moving objects. **Debris Contact Speed Change** and **Debris Contact Angular Change** set the additional motion allowances. Contact modification uses mass/inertia snapshots and handles swept CCD contacts too. Ground and stationary obstacles keep their full support/stopping impulses, preventing a heavy car from pressing a panel through the floor.

A second check bounds the combined result of multiple convex manifolds and CCD passes. It uses the larger of pre-solver debris speed and impacting-surface speed times **Debris Surface Speed Multiplier**, plus the speed allowance. Spin has a corresponding pre-solver allowance. These checks run on actual contacts, preserving faster inherited motion and free flight; they are configurable numerical stabilization, rather than structural metal-crushing physics.

**Debris Solver Iterations** and **Debris Velocity Solver Iterations** improve support for thin, light parts under a heavy chassis. **Debris Maximum Angular Speed** sets the native angular limit with stabilization enabled; Wheel Part can raise it to preserve inherited tire RPM. These native settings apply on release and repair restores original Rigidbody settings.

**Debris Ground Projection** corrects deep penetration at actual stationary, gravity-supporting contacts. **Debris Ground Penetration Tolerance** ignores tiny overlaps; **Debris Ground Projection Limit** bounds a correction. It uses the physical Rigidbody pose and only an actual overlapping collider, without ground snapping in free flight. **Prewarm Debris Physics** prepares disabled helpers and contact code during startup, reducing cold work at the first detachment without creating attached Rigidbodies or changing compound collision geometry.

**Exclude Debris From Wheel Support** prevents native WheelCollider suspension and contact-envelope probes from treating a detached panel as a road surface. It avoids applying a full vehicle spring/damper load to a light panel trapped under the car. Solid tire colliders supplied by Tire Collision and ordinary chassis colliders still interact with the part. This option also covers other vehicles and vehicles created later. It can be changed independently of contact stabilization. Repair, disable and destruction remove the temporary wheel exclusions and solver registration; re-enabling detached debris restores them.

A physical Body Part uses narrow hinge limits near its closed pose. Removing the hinge retains its carrier reference until deferred destruction completes, preventing chassis-local anchors from being interpreted in world space.

.. _uvs-damage--impact-unlatching:

Impact unlatching
-----------------

Each **Body Part > Impact Unlatching** section controls whether a collision can loosen the panel while it stays attached to its hinge. **Unlatch On Impact** enables it. Both **Minimum Unlatch Force** (average contact force in newtons, impulse divided by the physics timestep) and **Minimum Unlatch Speed** (speed into the contact normal in m/s) must be reached. Sliding along the panel or displacement alone does not bypass these thresholds. Physical damage hits routed to the panel use the same policy. This feature requires Use Physics and an existing hinge; it does not detach the part or change its damage threshold.

**Permanent Impact Unlatch** keeps the latch released even if the panel happens to swing closed. Call **Close()** or **SetOpen(false)** to restore its normal latch and closing spring. With this option off, the panel may latch again once **Temporary Unlatch Delay** has elapsed and it is within two degrees of the closed pose. The delay gives an impact time to move the panel away from its closed position.

**Unlatched Spring Multiplier** and **Unlatched Damper Multiplier** scale the ordinary hinge spring and damper while loose. Set spring scale to zero for free swinging, or a small value for a weak tendency to return. Lower damping allows longer motion. The normal opening limits still apply. IsOpen describes the requested opening state; use IsImpactUnlatched to check collision release, and IsReleased/IsDetached for detachment.

The car demo and Sample use permanent impact unlatching, a 1.5 m/s speed threshold, 3000 N force for doors/trunk and 4000 N for the hood. The loose spring scale is 0.05 and damping scale 0.35, allowing a damaged panel to swing without requiring it to detach. Exact forces depend on collider geometry, mass and the fixed timestep.

.. _uvs-damage--detachable-wheels:

Detachable wheels
-----------------

``WheelPart`` inherits ``DamagePart``, so it shares part IDs, damage accumulation, material effects, threshold detachment and repair with panels. Put it on the **visual wheel root**, not on the WheelCollider/suspension mount. The mount and ``Wheel`` adapter remain on the vehicle when the tire becomes debris.

.. _uvs-damage--tutorial-make-one-wheel-damageable:

Tutorial: make one wheel damageable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Start with a working wheel in VehicleController's Wheel Setup. Its WheelCollider mount must have the ``Wheel`` adapter, with Visual referencing the intended visual wheel root.
2.  Select the visual root and add **UltraVehicleSystem > Exterior > Parts > Wheel Part**. The same entry is available through **Tools > UltraVehicleSystem > Add Component > Exterior > Parts > Wheel Part**.
3.  Assign **Wheel** to the adapter on that wheel's collider mount. The adapter's Visual must be this transform or a child of it; the WheelCollider mount must remain outside the detachable group.
4.  Give it a unique **Part Id**, for example ``WheelFrontLeft``. Enable **Damage Enabled**, choose Rubber material and a **Detach Threshold**. Keep Deformation Multiplier at zero if the tire/rim should not dent.
5.  Put it in **Damage > Parts**, or **Body > Damage Parts**. WheelPart components under the vehicle are also discovered by Damage.Configure/RefreshParts; references are retained after debris leaves the hierarchy. After creating runtime parts, call ``damage.RefreshParts()``.
6.  Leave **Generate Rolling Collider** enabled for a generated convex cylindrical tire proxy. It is created/enabled only for detached debris. Radius/width come from Wheel; **Collider Segments** controls resolution. An optional **Debris Material** sets friction/bounce. For a custom tread collider, disable generation and author suitable colliders yourself.
7.  Set **Mass**, low **Debris Angular Damping** for continued rolling, and the normal debris clearance/depenetration options. Detachment carries the vehicle's point velocity and angular velocity plus the wheel's measured axle spin. The result is physical debris, not a WheelCollider vehicle/tire model.
8.  Test a side/obstacle impact, or send a scripted damage hit near that wheel through ``Damage.ApplyImpact``. Ordinary wheel support/rolling contacts remain filtered from vehicle damage. Keep global Damage Enabled/Detachment Enabled on for threshold release.
9.  Observe ``wheel.Attached`` / ``wheel.IsOperational`` (also copied as ``WheelTelemetry.Attached``), ``Wheel.AttachmentChanged`` or ``VehicleController.WheelAttachmentChanged``. On detachment the native collider is disabled, actuators cleared, contact/RPM telemetry reset and vehicle mechanisms skip the wheel. Availability/configuration/profile changes do not reconnect it.
10. Call ``vehicle.RepairPart("WheelFrontLeft")`` or RepairAll to recover the retained wheel, remove its temporary debris physics and resume the native wheel if configuration/profile availability permits.

Damage Enabled can be switched off later without removing the component or changing its stable ID. Disabling damage does not automatically repair an already detached wheel. Explicit ``WheelPart.Detach(vehicle.Body)`` remains available for scripted release; ``Wheel.SetAttached`` is the low-level availability state and does not create/remount debris by itself.

The **UVS Car** demo retains a front-left WheelPart (``WheelFrontLeft``, threshold 12), with **Damage Enabled off** in both the prefab and scene. This keeps the integration available without enabling wheel detachment in normal demo play. The common **R** reset also repairs the selected vehicle.

.. _uvs-damage--repair-and-full-reset:

Repair and full reset
---------------------

+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Goal                                                                                       | API                                                     |
+============================================================================================+=========================================================+
| Restore all prepared dent shapes only                                                      | ``VehicleMeshDeformation.RestoreShape()``               |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Restore prepared meshes belonging to one part only                                         | ``VehicleMeshDeformation.RestoreShape(part)``           |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Reduce attached-part damage without reattachment                                           | ``DamagePart.Repair(amount)``                           |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Fully restore a retained part, including remount/shape/damage                              | ``DamagePart.RepairFully()``                            |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Fully repair one registered part by ID/reference                                           | ``Damage.RepairPart(id)`` / ``Damage.RepairPart(part)`` |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Repair a registered part by ID through the vehicle                                         | ``VehicleController.RepairPart(id)``                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Repair registered damage parts, wheel attachments, released body hinges and prepared dents | ``VehicleController.RepairAll()``                       |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Repair and move/reset the vehicle together                                                 | ``VehicleController.ResetVehicle(position, rotation)``  |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Move/reset pose without repairing damage                                                   | ``VehicleController.Teleport(position, rotation)``      |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. _uvs-damage--tutorial-repair-a-part-or-the-whole-vehicle:

Tutorial: repair a part or the whole vehicle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Give each damage boundary a stable unique Part Id and register it with Damage/Body before damage occurs. Damage captures the attached hierarchy and local pose before release; its registry retains detached object references.
2. Use ``vehicle.RepairPart(id)`` for a UI selection or repair pickup. The boolean reports success. IDs use exact case-sensitive matching; blank/missing/ambiguous IDs return false. The Damage component also supports repairing an explicitly registered part reference.
3. For a complete in-place repair, call ``vehicle.RepairAll()``. It works even with future damage disabled. Retained parts reattach, damage becomes zero, prepared dents reset, hinges close and rebuild as needed, and detached wheels reconnect. Temporary debris collision exclusions and managed impact effects are cleared.
4. Use ``vehicle.ResetVehicle(position, rotation)`` when a respawn/reset should also repair. It performs RepairAll then the normal teleport/passenger-reset workflow and clears wheel spin. RepairAll alone keeps the vehicle's pose and chassis momentum; it clears current wheel actuators but does not reset every engine/gearbox/input/application state.
5. In the demo, press the common **R** reset key to repair the selected vehicle and restore its recorded spawn/passenger pose. No separate repair shortcut or extra action buttons are provided; the demo's aircraft/landing-gear reset preparations are retained.
6. Subscribe to ``DamagePart.Restored``, ``Damage.FullyRepaired`` or ``VehicleController.Repaired`` for your health/UI reactions. ``Repaired(part, amount)`` still reports actual removed damage. A wheel's attached state is already restored when its part Restored notification runs.
7. Test individual repair after a dent, detached-wheel repair, released-door repair and repeated detach/repair cycles. Check deliberately disabled wheels stay unavailable and alternate drive profiles do not accidentally activate wheel contacts.

Repair uses the **existing retained objects**, not clones of missing geometry. If application debris cleanup destroys a part or its saved attachment parent, restore that object through your own respawn/pooling policy. Repair does not replenish weapons, restore unrelated application health, or remove arbitrary user-created constraints. A parent group repair does not automatically clear independently registered child damage accumulators; repair those children too or use RepairAll. Runtime hierarchy/pose edits after the initial snapshot do not redefine the authored mounting pose.

The material classification can inform reactions, but does not automatically implement every glass, mechanical-failure or armor rule. Subscribe/extend through :ref:`Damage scripting <uvs-scripting-damage--observe-accepted-damage>` and :doc:`API </API/Damage>`.

.. _uvs-damage--material-impact-profiles:

Material impact profiles
------------------------

New Damage Feedback components added in the editor receive shared Metal, Glass, Plastic, Rubber and Mechanical profiles from Resources/Effects/Damage. Their clips are in Resources/Audio/Damage and their particle prefabs in Resources/Effects/Damage; they work without importing Demo. Existing custom profiles are preserved. Replace or clear the profiles to customize or disable these responses.

Create an asset with **Assets > Create > UltraVehicleSystem > Damage > Impact Profile** (or **Tools > UltraVehicleSystem > Create Asset > Damage > Impact Profile**), then add it to **Damage Feedback > Scripted Material Responses > Impact Profiles**. Each list entry is a reusable asset containing a material rule, recordings and optional visual prefab. The demo includes Metal, Glass, Plastic, Rubber and Mechanical examples. Assign the corresponding material to each DamagePart. For another material, set the same case-sensitive **Material Id** on the part and profile; this takes priority over the built-in enum and requires no package changes.

The first eligible custom-key profile wins, otherwise the first eligible enum profile wins. Disabled profiles and profiles outside their accepted impact range are skipped. Fallback Impact Profile handles unmatched hits if its thresholds accept them. Each channel selects one profile. Multiple entries for the same material can form intensity bands: enable Ignore Above Maximum on the weaker band and place it before the stronger band.

Choose the threshold metric deliberately:

+---------------+-----------------------------------------------------------------------------------------------------------+
| Metric        | Units and meaning                                                                                         |
+===============+===========================================================================================================+
| Damage Amount | Gameplay damage severity after collision-response scaling; also works with scripted damage.               |
+---------------+-----------------------------------------------------------------------------------------------------------+
| Impact Speed  | Collision speed into the contact surface, in m/s.                                                         |
+---------------+-----------------------------------------------------------------------------------------------------------+
| Impulse       | Collision impulse magnitude, in N·s.                                                                      |
+---------------+-----------------------------------------------------------------------------------------------------------+
| Force         | Average collision force estimated as impulse divided by the fixed physics timestep, in N; not peak force. |
+---------------+-----------------------------------------------------------------------------------------------------------+

Minimum Impact rejects weaker hits. Maximum Impact maps to full intensity; stronger hits saturate unless Ignore Above Maximum rejects them. Accepted hits map to 0–1 intensity. Physical metrics require physical metadata: the original three-argument ApplyImpact call supplies damage severity only. Cooldown is independent per profile, vehicle and audio/visual channel, so sharing an asset never shares playback state between cars.

.. _uvs-damage--pooled-particles-and-custom-effects:

Pooled particles and custom effects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assign Effect Prefab on a profile. Particle systems on the prefab are cached at warmup and restarted at the impact point. Use a one-shot prefab with Play On Awake disabled. Set Effect Lifetime long enough for every child system and sub-emitter to finish. Local +Z points outward, opposite the deformation direction; Rotation Offset corrects the prefab orientation, Surface Offset lifts it above the panel, and Effect Scale Range maps intensity to a multiplier of its original scale.

Effect Pool Size reserves instances for that profile. Damage Feedback' Maximum Effect Instances caps the whole vehicle; earlier profiles receive capacity first. Skip discards requests when the profile pool is busy; Replace Oldest restarts its oldest effect. Pools are prepared on enable/configuration, never instantiated per hit. Effects remain in world space when the vehicle moves. DamageFeedback.Impact Effects Enabled or SetImpactEffectsEnabled(false) clears visuals without disabling deformation or damage sounds.

A custom prefab behavior can implement IDamageImpactEffect. PlayImpact receives the hit and normalized intensity each time the instance is leased; StopImpact must reset transient lights, trails or other state before reuse. Cache references during initialization, avoid allocations in callbacks and do not destroy the pooled object. Callbacks also run when an effect is replaced or cleared. See :ref:`the scripting contract <uvs-scripting-damage--custom-impact-effect>`.

After replacing profile lists, prefabs or pool capacities at runtime, call DamageFeedback.WarmUpEffects() to rebuild the visual pool, and DamageAudio.WarmUp() if audio uses the changed list. Numeric response settings are read during playback. ClearEffects() returns active effects without disposing the prepared pool. Damage Feedback owns the prepared pool independently of the damage mechanic.

.. _uvs-damage--visual-damage-performance:

Visual damage performance
-------------------------

VehicleMeshDeformation can batch mesh uploads over several rendered frames and optionally retain existing normals. Damage calculation continues for every hit. Defaults upload each LateUpdate and rebuild normals. See :ref:`visual damage updates <uvs-performance--visual-damage-updates--vehiclemeshdeformation>` for timing, shading and immediate-flush behavior.

.. _uvs-damage--test-and-diagnose:

Test and diagnose
-----------------

+----------------------------------+---------------------------------------------------------------------------+
| Symptom                          | Check                                                                     |
+==================================+===========================================================================+
| No damage from an impact         | Enabled policy, valid contact, normal impact speed and owned Parts list   |
+----------------------------------+---------------------------------------------------------------------------+
| Wrong panel is damaged           | Boundary hierarchy, collider/mesh ownership and impact radius             |
+----------------------------------+---------------------------------------------------------------------------+
| Accumulation changes but no dent | Readable supported mesh, enough vertices, deformation switches/multiplier |
+----------------------------------+---------------------------------------------------------------------------+
| Panel never detaches             | Enabled detachment, accumulated damage, multiplier and threshold          |
+----------------------------------+---------------------------------------------------------------------------+
| Debris jumps violently           | Collider overlap, released mass/velocity and clearance exclusions         |
+----------------------------------+---------------------------------------------------------------------------+
| Reset leaves dents/debris        | Position reset is not full repair/reconstruction                          |
+----------------------------------+---------------------------------------------------------------------------+

Test deformation-only, detachment-only and completely disabled response separately before combining them in a complete crash sequence.

.. _uvs-damage--repair-in-brief:

Repair in brief
---------------

Call ``vehicle.RepairPart("part.id")`` to restore one registered part, or ``vehicle.RepairAll()`` for an in-place vehicle repair, including retained detached panels, wheel attachments and prepared dents. ``ResetVehicle(position, rotation)`` combines repair with a reset to a chosen pose; ``Teleport(position, rotation)`` only relocates the vehicle. ``DamagePart.Repair(amount)`` reduces damage without remounting a detached object, while ``VehicleMeshDeformation.RestoreShape()`` only removes dents.

Keep repairable debris and its original mounting parent alive: repair restores retained objects rather than spawning replacements. Give boundaries unique stable IDs before release. The earlier Repair and full reset section documents return values, events and nested-part behavior.
