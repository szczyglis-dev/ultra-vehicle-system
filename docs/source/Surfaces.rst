.. _uvs-surfaces--ground-grip-and-tire-effects:

Ground grip and tire effects
============================

Physical grip and tire presentation are separate. ``Surface`` affects native tire friction through Friction; ``TireSurface`` selects an effect profile for feedback consumers. A dusty sound/particle profile does not itself make the road slippery.

.. _uvs-surfaces--inspector-quick-start-create-a-gravel-patch:

Inspector quick start: create a gravel patch
--------------------------------------------

1. Select the road/patch object holding the ground collider. Add **Surface** for grip and **Tire Surface** for presentation through Add Component. These classify the ground, not the vehicle.
2. Set Surface's **Grip**. In Project, create **Create > UltraVehicleSystem > Surfaces > Tire Surface Profile**, configure its audio/particle/mark options and assign it to the patch's TireSurface setup. For Terrain use the layer mapping below.
3. On the vehicle, check **Modules > Physics > Friction**, **Effects > Tire Feedback**, and the Tire Audio/Tire Smoke/Skidmarks consumers you need. Fill missing references.
4. Apply vehicle configuration, save the profile and scene, then drive onto the patch. Check grip and rolling/skid effects separately: a dusty profile does not itself lower traction.

.. _uvs-surfaces--change-physical-grip:

Change physical grip
--------------------

1. Ensure the vehicle has an enabled registered ``Friction`` module and valid wheel contact.
2. Add **Surface** to the exact GameObject holding the ground collider.
3. Set **Grip** as a multiplier on the vehicle's base grip.
4. Drive the same acceleration, braking and cornering tests on this collider and an unmarked baseline collider.
5. Tune :doc:`TCS </TractionControl>` only after this base contact response is intentional.

Physical lookup checks the actual hit collider object. A Surface placed only on a parent is not found by Friction. For a compound ground hierarchy, configure the collider children deliberately.

The base vehicle grip, ground multiplier, tracked lateral policy and handbrake lateral reduction can all contribute. A large engine torque change does not explain every slide; inspect which physical surface was actually hit. Native friction-curve shape values remain separate from the stiffness the module scales.

.. _uvs-surfaces--give-the-ground-sound-dust-and-marks:

Give the ground sound, dust and marks
-------------------------------------

1. Create a **Tire Surface Profile** through **Assets > Create > UltraVehicleSystem > Surfaces > Tire Surface Profile** (also available from the Project window context menu).
2. Add **Tire Surface** to the collider object or an appropriate parent and assign **Profile**.
3. Configure that asset's tire loop, particles and mark appearance, and enable the desired effect channels.
4. Configure the vehicle's ``TireFeedback`` module and **Default Surface** fallback.
5. Add the actual tire audio/particle/mark modules. Selecting a profile supplies their settings; it does not create every effect consumer automatically.
6. Test an ordinary rolling pass and a skid, then cross the boundary to another ground type.

A nearer TireSurface mapping takes precedence over a parent mapping. For an empty tire loop, Use Default Tire Loop When Empty chooses the Tire Audio component clip or silence; it is off by default. Surface volume, pitch and activity settings still apply when using that fallback. With no profile selected, consumers use their applicable general effect settings/fallback behavior. Keep that distinction when a deliberate silent surface appears to override a vehicle loop.

.. _uvs-surfaces--rolling-activity-versus-skid-activity:

Rolling activity versus skid activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Rolling Particles** and **Rolling Marks** allow activity while rolling without a strong skid. Minimum/Full Rolling Speed define the ramp, in m/s, for that contribution. Set rolling activity to zero for ordinary slip-only effects.

For a grounded physical wheel receiving brake torque, TireFeedback also compares road-relative contact-plane speed with tire rim speed. This retains braking skid activity when the native WheelCollider slip intermittently reports zero for a locked wheel. Parked wheels, airborne wheels and wheels rolling with the road do not gain braking slip from a held command alone. Moving-ground velocity is subtracted; direct-control motion keeps its existing presentation sampling. Marks, smoke and squeal consume the same corrected contact record. Skidmarks still breaks its ribbon on lost contact rather than joining through an air gap.

**Granular Particles** uses the built-in loose-grain style; particle material/color/size/lifetime and rate parameters control its appearance. **Loose Tracks** selects the loose-soil mark style rather than ordinary rubber grooves. Per-channel enabled flags can suppress particles/marks independently.

These options describe presentation. Tire friction, deforming ground and persistent wheel ruts are not automatically simulated by choosing a loose-surface profile. A custom particle prefab/system can retain its own design rather than adopting every built-in preset parameter.

.. _uvs-surfaces--tirefeedback-ownership:

TireFeedback ownership
~~~~~~~~~~~~~~~~~~~~~~

TireFeedback samples wheel contact/activity and resolves effect surfaces. Audio, particles and marks consume that result, so they can agree on the selected ground type. Keep effect lifetime/pooling in those modules rather than creating an unbounded object on every surface sample.

For consumer-specific setup, see :doc:`Audio </Audio>`, :doc:`Particles </Particles>` and :doc:`Tire marks </Decals>`. This guide owns ground classification, not the full emitter/audio/mesh setup.

.. _uvs-surfaces--terrain-layer-mapping:

Terrain layer mapping
---------------------

Place TireSurface on the TerrainCollider object and map its Terrain Layers to effect profiles. The mapping uses the dominant painted layer at the contact position, with the configured base profile as fallback. It is a classification choice, not a blend of every painted audio/particle profile.

Refresh the TerrainSurface cache through ``TireSurface.RefreshTerrain()`` after painting/changing terrain layers at runtime as appropriate. TireFeedback also caches surface lookup; use its cache refresh API when your application changes mappings/hierarchies in ways that require explicit invalidation.

Painted-layer mapping here affects effects only. For painted physical grip, implement the corresponding custom friction integration; adding Terrain layer effects does not change the Surface multiplier per painted pixel.

.. _uvs-surfaces--example-gravel:

Example: gravel
---------------

Create a collider with Surface Grip lower than the road baseline. Independently assign a gravel TireSurfaceProfile with a gravel tire loop, rolling granular dust and loose marks. First test physical acceleration/braking, then balance the sound and visuals at low/high speed.

For a mixed-grip road, split the physical colliders or supply your own per-contact grip logic. For a mixed-effect Terrain, map the painted layers. These are different authoring paths even if they describe the same visible material.

.. _uvs-surfaces--diagnose-a-surface:

Diagnose a surface
------------------

+--------------------------------------------+-----------------------------------------------------------+
| Symptom                                    | Check                                                     |
+============================================+===========================================================+
| Gravel looks dusty but drives like asphalt | Effect profile alone does not change physical grip        |
+--------------------------------------------+-----------------------------------------------------------+
| Grip on a parent has no effect             | Surface must be on the hit collider object                |
+--------------------------------------------+-----------------------------------------------------------+
| Tire loop disappears on one patch          | Selected profile may intentionally have no loop           |
+--------------------------------------------+-----------------------------------------------------------+
| Terrain paint changes nothing physically   | Terrain layer mapping classifies effects only             |
+--------------------------------------------+-----------------------------------------------------------+
| Dust appears only during skids             | Rolling contribution is zero or below its speed threshold |
+--------------------------------------------+-----------------------------------------------------------+
| Runtime edits show old effects             | Terrain/surface caches and consumer refresh ownership     |
+--------------------------------------------+-----------------------------------------------------------+

See :doc:`Surface feedback scripting </Scripting/SurfaceFeedback>` and :doc:`API </API/SurfaceFeedback>` for precedence, cache operations and feedback lifetimes.

.. _uvs-surfaces--create-configuration-assets:

Create configuration assets
---------------------------

All reusable ScriptableObject assets are available through **Assets > Create > UltraVehicleSystem**, including the Project window's **Create** context menu, and through **Tools > UltraVehicleSystem > Create Asset**. Both routes create a new editable asset in the selected Project folder and let you name it.

+---------------------------------------+----------------------------------------------------------------------------+
| Submenu                               | Asset                                                                      |
+=======================================+============================================================================+
| Damage > Impact Profile               | Material-specific impact recordings, pitch, thresholds and pooled effects. |
+---------------------------------------+----------------------------------------------------------------------------+
| Audio > Engine Sound Profile          | Reusable engine sound configuration.                                       |
+---------------------------------------+----------------------------------------------------------------------------+
| Surfaces > Tire Surface Profile       | Tire contact grip and presentation settings.                               |
+---------------------------------------+----------------------------------------------------------------------------+
| Water > Surface Profile               | Reusable water appearance settings.                                        |
+---------------------------------------+----------------------------------------------------------------------------+
| Passengers > Access Animation Profile | Passenger entry/exit animation configuration.                              |
+---------------------------------------+----------------------------------------------------------------------------+

Drive profiles are serialized directly inside VehicleController rather than stored as ScriptableObject assets. Choose those profiles in the vehicle Inspector. Scene behaviors use **Add Component** or **Tools > UltraVehicleSystem > Add Component**.

.. _uvs-surfaces--surface-specific-braking-sound:

Surface-specific braking sound
------------------------------

Assign **Braking Loop** on a Tire Surface Profile to use a different brake recording on that surface. If it is empty, **Use Default Brake Loop When Empty** chooses the Brake Audio component's own clip or silence; it is on by default. Brake Audio Multiplier scales either choice; zero mutes that surface's braking sound. The two empty-clip policies are independent: **Use Default Tire Loop When Empty** is off by default, while the brake checkbox is on. When wheels touch different surfaces, their brake sounds mix proportionally to the number of contacts.
