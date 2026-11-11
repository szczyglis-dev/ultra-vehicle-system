.. _uvs-inspectorconfiguration--inspector-controls-by-system:

Inspector controls by system
============================

Use a component's enabled checkbox to disable a whole responsibility. Use its behavior switches to change part of an enabled system. Configure drive profiles in Setup/ProfileSwitcher, and model-mounted helpers on their objects. Public authoring fields are configuration; transient read-only state is for observation.

+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| System            | Main configuration choices                                                                        | Guide                                                                                    |
+===================+===================================================================================================+==========================================================================================+
| Controller/input  | Input source, category/local order, action references, analog/digital channel metadata            | :doc:`Configuration </Configuration>`, :doc:`Input </Input>`                             |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Wheels/suspension | Radius/width/mass, independent roles, springs/damping/travel, anti-roll, envelope/contact helpers | :doc:`Suspension </Suspension>`, :doc:`Tire collision </TireCollision>`                  |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Engine/gearbox    | RPM/torque curve, power/acceleration caps, ratios, shift timing and direction guards              | :doc:`Vehicle tuning </VehicleTuning>`, :doc:`Gearbox </Gearbox>`                        |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Clutch/assists    | Pedal/automatic operation, torque capacity/inertia, slip/stability policies                       | :doc:`Clutch </Clutch>`, :doc:`Traction control </TractionControl>`                      |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Brakes/parking    | Digital rise ramp, handbrake/rolling torque, slope release window, service/parking assistance     | :doc:`Gearbox </Gearbox>`, :doc:`Clutch </Clutch>`                                       |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Ground strategies | Wheel setup, motorcycle balance, tracked side slots/pivot/grip                                    | :doc:`Drive profiles </DriveProfiles>`, :doc:`Tracked </Tracked>`                        |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Air strategies    | Support/leveling, input/rate/attitude response, limits, gear protection, propulsion visuals       | :doc:`Aircraft </Aircraft>`                                                              |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Water             | Provider/fallback, hull sample dimensions, resistance/rocking/depth hold and effect switches      | :doc:`Water </Water>`, :doc:`Boat </Boat>`, :doc:`Submarine </Submarine>`                |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Passengers        | Body/controller, per-limb mode/anchor/handle, contact/hold, harness and ejection/reseat policy    | :doc:`Passengers </Passengers>`, :doc:`Seats </Seats>`                                   |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Boarding          | Access point, speed/clearance checks, door references, animation profile and timing               | :doc:`Passenger access </PassengerAccess>`                                               |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Interior          | Control axes/ranges, interaction mode, mirror budgets and HUD binding                             | :doc:`Interior controls </InteriorControls>`, :doc:`Interior systems </InteriorSystems>` |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Body/damage       | Part IDs/hinges, damage/deformation/detachment switches, thresholds and collision-release policy  | :doc:`Damage </Damage>`, :doc:`Moving parts </MovingParts>`                              |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Lights            | Channel availability, sources/lenses, beam/indicator state, automatic/explicit overrides          | :doc:`Lights </Lights>`                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Audio/effects     | Mixer/spatial response, clips/profiles, event mappings, particle assets/rates and bounded pools   | :doc:`Audio </Audio>`, :doc:`Particles </Particles>`, :doc:`Tire marks </Decals>`        |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Towing            | Attach distance/alignment, break policy, hitch motion, forwarded/detached brakes                  | :doc:`Towing </Towing>`                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Weapons           | Firing/drop enable, cadence, payload references, launch/motor/blast and presentation              | :doc:`Weapons </Weapons>`                                                                |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. _uvs-inspectorconfiguration--basic-inspector-workflow:

Basic Inspector workflow
------------------------

1. Stop Play Mode. Select the vehicle root (the object with Vehicle Controller) or open its prefab for editing. Start from a vehicle that already moves correctly before adding optional equipment.
2. Open **Vehicle Controller > Modules** and choose the system's category. If the module is missing, use **Add module...** at the bottom. For an existing component added directly with Unity's **Add Component**, use **Discover and order vehicle modules**, then **Apply vehicle configuration**. Required parent modules should be added before configuring their submodules; resolve any parent-missing warning shown by the Inspector.
3. Expand the module. Use **+** on an array/list for each lamp, sound, axle, outlet or other entry. Drag the requested component, Transform or Project asset into the new slot. An empty array is usually an unconfigured set of outputs, not a request to find every matching model object automatically.
4. Create model-specific children in the Hierarchy where needed: hinges, lamp sources, exhaust outlets, cockpit screens or seat anchors. Select a child to edit its local helper component. Module discovery does not create this geometry or fill all its references for you.
5. Edit reusable profiles in the **Project** window. Scene Transforms/components belong in scene/prefab component fields, not in a shared profile asset. Duplicate a shared asset first if only this vehicle should receive a different configuration.
6. Press **Apply vehicle configuration** when references or managed mechanical settings change. Save the scene; apply intended prefab instance overrides or save changes in Prefab Mode. Play Mode edits normally disappear on stopping.
7. Enter Play Mode and test one responsibility at a time. Use **Live** for mechanic state, then inspect its sound/visual output. A missing input, contact or engine state cannot be fixed by increasing an effect's intensity.

The **Modules** tab's **Sort modules > Alphabetical / Execution order** changes display order only. **Category execution order** changes scheduling priority between categories within the dependency rules. Sorting the list is not a physics tuning action.

.. _uvs-inspectorconfiguration--find-the-right-inspector:

Find the right Inspector
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| What you want to add                    | Select / open                                                                 | First practical guide                                                                                                                                                 |
+=========================================+===============================================================================+=======================================================================================================================================================================+
| Wheel contact and suspension            | Root > Wheels, then Modules > Drive > Suspension                              | :ref:`Suspension <uvs-suspension--inspector-quick-start>`                                                                                                             |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Engine, gears, clutch and axle coupling | Root > Modules > Engine                                                       | :ref:`Gearbox <uvs-gearbox--inspector-quick-start>`, :ref:`Clutch <uvs-clutch--inspector-quick-start>`, :ref:`Differential <uvs-differential--inspector-quick-start>` |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Headlights, brake lamps and indicators  | Root > Modules > Exterior > Lights; lamp children for Unity Light geometry    | :ref:`Lights <uvs-lights--inspector-quick-start-add-one-headlight-pair>`                                                                                              |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Engine, tire and event sound            | Root > Effects > Audio and its nested audio modules                           | :ref:`Audio <uvs-audio--inspector-quick-start-one-working-engine-loop>`                                                                                               |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Smoke, exhaust and jets                 | Root > Effects; outlet children for positions/directions                      | :ref:`Particles <uvs-particles--inspector-quick-start-add-an-exhaust-outlet>`                                                                                         |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tire marks and surface effects          | Root > Effects; road/terrain object for surface helpers                       | :ref:`Tire marks <uvs-decals--inspector-quick-start>`, :ref:`Surfaces <uvs-surfaces--inspector-quick-start-create-a-gravel-patch>`                                    |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Opening/damageable panels               | Panel pivot > VehicleBodyPart/DamagePart, then root registries                | :ref:`Moving parts <uvs-movingparts--inspector-steps-for-the-body-parts-list>`, :ref:`Damage <uvs-damage--inspector-workflow-and-part-registries>`                    |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Screens, mirrors and fuel               | Root > Modules > Interior or Engine; model children for screen/camera anchors | :ref:`Interior systems <uvs-interiorsystems--inspector-quick-start>`                                                                                                  |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Driver and passengers                   | Root > Seats; seat and prepared character objects for local references        | :doc:`Passengers </Passengers>` and :ref:`Seats <uvs-seats--inspector-quick-start>`                                                                                   |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Camera views                            | Root > Modules > World > Cameras and its camera submodules                    | :doc:`Cameras </Cameras>`                                                                                                                                             |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Boat/water equipment                    | Root > Setup and Modules > World; separate water scene object                 | :ref:`Water <uvs-water--inspector-quick-start-connect-a-boat-to-water>`                                                                                               |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Trailer connection                      | Each vehicle root and its own hitch child                                     | :ref:`Towing <uvs-towing--inspector-quick-start>`                                                                                                                     |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mounted weapons                         | Barrel/muzzle and payload objects, with vehicle-owned modules                 | :ref:`Weapons <uvs-weapons--inspector-quick-start-one-mounted-barrel>`                                                                                                |
+-----------------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-inspectorconfiguration--managed-fields:

Managed fields
--------------

Fields that the vehicle assigns during configuration are greyed out in the component inspector. The tooltip identifies where to edit them. This applies only to an actual binding: an unassigned wheel or unregistered child module keeps its editable fields. In mixed selections, a field is locked if any selected component is managed; select the unassigned components separately to edit it.

For native ``WheelCollider`` components, Wheel Setup owns radius and mass. Installed Suspension owns travel, spring/damper, target position and force application; Wheel Dynamics can also own damping. Enabled Friction owns only the stiffness of each friction curve, so the other curve settings and the wheel centre remain editable. Removing the corresponding binding/module restores editing. Assigned Shock Absorber settings can override suspension values for an individual wheel.

An Airplane drive profile owns engine power/RPM settings. With landing gear enabled, it also owns the spring/damper, selected steering-assistance fields and parking brake torque. Those fields become editable again when the relevant profile policy is removed. Owner references assigned unconditionally during module configuration are also read-only while the module is registered. References filled only when empty remain editable.

.. _uvs-inspectorconfiguration--editors-and-subclass-configuration:

Editors and subclass configuration
----------------------------------

Root modules can be edited through the controller's grouped inspectors. **Show standalone module inspectors** also exposes their ordinary Unity inspectors. These editor preferences do not change simulation membership or enabled state.

Specialized inspectors apply to component subclasses. Manually drawn inspectors show additional serialized subclass configuration under **Custom fields**. Use :doc:`Scripting </Scripting>` to override behavior rather than adding a second configuration path for an existing responsibility.

.. _uvs-inspectorconfiguration--component-actions-and-removal:

Component actions and removal
-----------------------------

Right-click a component header inside the Vehicle Controller Inspector to open its context menu:

-  **Copy Values** copies that component through Unity's component clipboard.
-  **Paste Values** pastes compatible component values, including assigned references and enabled state. It updates an existing component rather than adding another one. Ordinary Unity Inspector copy/paste uses the same clipboard. Apply Vehicle Configuration afterward when a setting needs configuration to reach native physics.
-  **Remove Component** removes only that component and updates module registration. Removal is available in Edit Mode and is disabled when another component still requires it through ``RequireComponent``.

Removing **Vehicle Controller** through Unity's ordinary Remove Component action prompts whether to remove its remaining vehicle modules. Choose **Keep modules** to leave them in place, or **Remove modules** to clean modules directly on that same GameObject. Dependents are removed before their required components. Modules required by a remaining non-module component are retained and listed in the prompt.

Cleanup leaves all child objects and their components untouched and keeps the Rigidbody, colliders, wheel adapters, model objects, non-module helpers and nested vehicles. Removing a whole GameObject or destroying a vehicle during Play Mode does not open the cleanup prompt. Undo/Redo restores or repeats the controller/module removal without asking again.

For every field, default and nested configuration block, use the :doc:`complete Inspector reference </InspectorReference>` at the end of this manual.
