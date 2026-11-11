.. _uvs-scripting-index--scripting-reference:

Scripting reference
===================

:ref:`Modules list <uvs-modulesandarchitecture--modules-list>` — browse components by category, with purposes and requirements.

:doc:`Events reference </Scripting/EventsReference>` — event and Inspector-callback tables grouped by class, with arguments and firing conditions.

:doc:`Custom modules </Scripting/CustomModules>` — create, install and schedule your own component, including Add Component and Tools menus.

:doc:`Profiling and debugging </Scripting/ProfilingAndDebugging>` — capture vehicle work and add custom markers.

Use the setup guide to build and check a system first. These chapters explain implementation contracts and provide complete C# components. Examples use the ``VehicleDocumentationExamples`` namespace; save a component in the named file, reference the runtime assembly and assign the listed scene references before use.

.. _uvs-scripting-index--start-with-inspector-setup:

Start with Inspector setup
--------------------------

Configuring the built-in components does not require writing the implementations described in this reference. Use :ref:`Basic Inspector workflow <uvs-inspectorconfiguration--basic-inspector-workflow>` for adding modules, assigning references, applying configuration and saving. Start with the relevant practical guide below; return to these technical chapters for custom behavior and application integration.

+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| System                               | Inspector-first guides                                                                                                                                                                                     |
+======================================+============================================================================================================================================================================================================+
| Chassis, wheels, brakes and steering | :doc:`Physics </Physics>`, :doc:`Suspension </Suspension>`, :doc:`Tire collision </TireCollision>`, :doc:`Contact envelope </ContactEnvelope>`                                                             |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Power and transmission               | :doc:`Gearbox </Gearbox>`, :doc:`Clutch </Clutch>`, :doc:`Differential </Differential>`, :doc:`TCS </TractionControl>`, :doc:`Boost actions </DrivingActions>`                                             |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Movement families and switching      | :doc:`Drive profiles </DriveProfiles>`, :doc:`Aircraft </Aircraft>`, :doc:`Boat </Boat>`, :doc:`Submarine </Submarine>`, :doc:`Tracks </Tracked>`, :doc:`Combined vehicles </CombinedVehicles>`            |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Environment and physical responses   | :doc:`Water </Water>`, :doc:`Ground surfaces </Surfaces>`, :doc:`Crash/landing response </CollisionsAndStabilization>`, :doc:`Towing </Towing>`                                                            |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Panels, wheels and damage            | :doc:`Moving parts </MovingParts>`, :ref:`Damage registries and setup <uvs-damage--inspector-workflow-and-part-registries>`, :doc:`Wipers </Wipers>`                                                       |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lighting, sound and particles        | :doc:`Lights </Lights>`, :doc:`Audio </Audio>`, :doc:`Particles </Particles>`, :doc:`Tire marks </Decals>`                                                                                                 |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cockpit and views                    | :doc:`Controls/instruments </InteriorControls>`, :doc:`Screens/mirrors/fuel </InteriorSystems>`, :doc:`Cameras </Cameras>`, :doc:`Input </Input>`                                                          |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Occupants and boarding               | :doc:`Passengers </Passengers>`, :doc:`Seats </Seats>`, :doc:`Passenger access </PassengerAccess>`, :doc:`Humanoid preparation </HumanAnatomy>`                                                            |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hands, feet and authored animation   | :doc:`Handles </Handles>`, :doc:`Saved hand positions </HandPositions>`, :doc:`Grip fitting </SteeringHandGrip>`, :doc:`Animation/IK </HandleAnimation>`, :doc:`Timed interactions </ControlInteractions>` |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mounted weapons and payloads         | :doc:`Weapons </Weapons>`                                                                                                                                                                                  |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Use the :doc:`Inspector field reference </InspectorReference>` for exact fields/defaults after completing a setup. Keep the API contracts and examples below for cases that need code; they are not additional components to install for every vehicle.

.. _uvs-scripting-index--code-examples:

Code examples
-------------

:doc:`Scripting examples </Scripting/Examples/index>` contains 100 standalone components in 10 categories, with setup instructions, comments and expected behavior.

.. _uvs-scripting-index--reading-a-technical-chapter:

Reading a technical chapter
---------------------------

Each topic starts with the system's purpose and the relationship between its parts. **Implementation map** names the classes responsible for each role. Individual component sections explain purpose and cooperation first, then configuration, technical behavior and integration points. They cover data flow, configuration authority and public operations together. Examples appear beside the behavior they illustrate, with setup, expected results and lifetime considerations. API identifiers use ``code formatting``; values include units or normalized conventions where those affect integration.

For a new extension, read :doc:`Architecture </Architecture>`, then :doc:`Scripting </Scripting>` and the relevant topic. For an existing integration, use the :doc:`API map </API>` to reach the owner of the operation. Each topic ends with a complete public method/event index, including package base contracts. The :doc:`API reference </API>` adds exact arguments, results, event payloads and declared state/configuration.

.. _uvs-scripting-index--integrate-with-the-vehicle:

Integrate with the vehicle
--------------------------

:ref:`What is available directly on vehicle <uvs-scripting--what-is-available-directly-on-vehicle>` — shortcuts, seats, body parts, handles, telemetry data/settings, chassis state, module queries and events.

+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Task                                                                 | Read                                                                                                  |
+======================================================================+=======================================================================================================+
| Understand category/phase ownership                                  | :doc:`Architecture </Architecture>`                                                                   |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Choose an extension point                                            | :doc:`Scripting </Scripting>`                                                                         |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Install a custom module on the root or a child                       | :ref:`Step-by-step installation <uvs-scripting--install-your-component-on-a-vehicle-step-by-step>`    |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Find public operations                                               | :doc:`API map </API>`                                                                                 |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Open/close a body part and read requested versus actual state        | :ref:`Body-part scripting <uvs-scripting-damage--open-a-named-part>`                                  |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Operate a generic moving part and observe arrival                    | :ref:`Moving-part operations <uvs-scripting-movingparts--operate-a-movingpart-and-read-its-state>`    |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Read collision impacts, accepted damage or supply a custom response  | :ref:`Impact notification guide <uvs-scripting-damage--choose-the-impact-notification>`               |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Register, find or replace modules                                    | :doc:`Module lifecycle </Scripting/Modules>`                                                          |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Supply commands and switch providers                                 | :doc:`Input </Scripting/Input>`                                                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Find events by name and owner                                        | :doc:`Events reference </Scripting/EventsReference>`                                                  |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Observe without polling physics                                      | :doc:`Events and telemetry </Scripting/Events>`                                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Add or switch movement modes                                         | :doc:`Drive profiles </Scripting/DriveProfiles>`                                                      |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Write an independent movement profile and select it in the Inspector | :ref:`Profile from scratch <uvs-scripting-driveprofiles--create-an-independent-profile-from-scratch>` |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-index--events-and-subscriptions:

Events and subscriptions
------------------------

Use events to connect UI, audio and application rules to accepted vehicle state changes. Subscribe to the owning component with ``+=``, remove the same handler with ``-=``, and read current state once when binding. For continuous readings, use telemetry snapshots.

:ref:`Events and telemetry <uvs-scripting-events--subscribe-to-a-components-events>` explains handler arguments, initial state, safe source changes and cleanup with a complete engine/seat example. It also covers :ref:`Inspector callbacks <uvs-scripting-events--inspector-callbacks-and-c-events>`, which use ``UnityEvent.AddListener`` / ``RemoveListener`` instead of C# event syntax. Exact payloads and firing conditions are listed in the corresponding :doc:`API topic </API>`.

.. _uvs-scripting-index--mechanics-and-environment:

Mechanics and environment
-------------------------

+--------------------------------------------------+------------------------------------------------------+
| Topic                                            | Reference                                            |
+==================================================+======================================================+
| Wheel authoring, native/envelope/solid contact   | :doc:`Wheel contact </Scripting/WheelContact>`       |
+--------------------------------------------------+------------------------------------------------------+
| Springs, shock overrides and linkage             | :doc:`Suspension </Scripting/Suspension>`            |
+--------------------------------------------------+------------------------------------------------------+
| Engine, gears, clutch, differential and TCS      | :doc:`Drivetrain </Scripting/DriveDynamics>`         |
+--------------------------------------------------+------------------------------------------------------+
| Boat resistance and rocking                      | :doc:`Boat </Scripting/Boat>`                        |
+--------------------------------------------------+------------------------------------------------------+
| Track sides and belt paths                       | :doc:`Tracks </Scripting/Tracks>`                    |
+--------------------------------------------------+------------------------------------------------------+
| Flight, gear and instruments                     | :doc:`Aircraft </Scripting/Aircraft>`                |
+--------------------------------------------------+------------------------------------------------------+
| Providers, depth hold and propeller presentation | :doc:`Water </Scripting/Water>`                      |
+--------------------------------------------------+------------------------------------------------------+
| Physical grip versus effect surfaces             | :doc:`Surface feedback </Scripting/SurfaceFeedback>` |
+--------------------------------------------------+------------------------------------------------------+
| Physical hitch lifecycle                         | :doc:`Towing </Scripting/Towing>`                    |
+--------------------------------------------------+------------------------------------------------------+
| Hits, detachment and restoration                 | :doc:`Damage </Scripting/Damage>`                    |
+--------------------------------------------------+------------------------------------------------------+
| Aiming, projectiles, rockets and payloads        | :doc:`Weapons </Scripting/Weapons>`                  |
+--------------------------------------------------+------------------------------------------------------+

.. _uvs-scripting-index--characters-and-presentation:

Characters and presentation
---------------------------

+-----------------------------------------------------------------+------------------------------------------------------------------+
| Topic                                                           | Reference                                                        |
+=================================================================+==================================================================+
| Occupancy, custom characters and controller factory             | :doc:`Passenger controllers </Scripting/PassengerControllers>`   |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Dynamic supports, release and collision policy                  | :doc:`Passenger physics </Scripting/PassengerPhysics>`           |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Skeletal frames                                                 | :doc:`Anatomy </Scripting/Anatomy>`                              |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Contact targets and transfer actions                            | :doc:`Handles </Scripting/Handles>`                              |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Finger fit, steering mapping and reservations                   | :doc:`Grip solving </Scripting/GripSolving>`                     |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Animated boarding and reservations                              | :doc:`Passenger access </Scripting/PassengerAccess>`             |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Committed IK/Animator/custom gestures                           | :doc:`Interactions </Scripting/Interactions>`                    |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Instruments, mirrors and fuel                                   | :doc:`Interior </Scripting/Interior>`                            |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Exterior part motion, blade timing, parking and cockpit binding | :doc:`Exterior motion and moving parts </Scripting/MovingParts>` |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Channel output and indicator timing                             | :doc:`Lights </Scripting/Lights>`                                |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Audio sources and custom channels                               | :doc:`Audio </Scripting/Audio>`                                  |
+-----------------------------------------------------------------+------------------------------------------------------------------+
| Particle/mark resource ownership                                | :doc:`Presentation </Scripting/Presentation>`                    |
+-----------------------------------------------------------------+------------------------------------------------------------------+

.. _uvs-scripting-index--profiling-and-debugging:

Profiling and debugging
-----------------------

:doc:`Profiling and debugging </Scripting/ProfilingAndDebugging>` covers repeatable captures, built-in UVS samples, custom ProfilerMarker scopes and integration diagnostics.

.. _uvs-scripting-index--crash-presentation:

Crash presentation
------------------

:ref:`Crash Feedback <uvs-damagefeedback--shared-events-and-api>` provides copied contact events, configurable audio and particles, and custom contact submission. Use damage events for authoritative damage logic.

.. _uvs-scripting-index--scripting-topics:

Scripting topics
----------------

.. toctree::
   :maxdepth: 1

   Aircraft
   PassengerAccess
   Audio
   Boat
   Damage
   Input
   Interactions
   CustomModules
   DriveProfiles
   DriveDynamics
   Events
   MovingParts
   GripSolving
   Interior
   Anatomy
   Lights
   Handles
   Modules
   Suspension
   PassengerControllers
   PassengerPhysics
   ProfilingAndDebugging
   Examples/index
   SurfaceFeedback
   Towing
   Tracks
   Presentation
   Water
   Weapons
   WheelContact
