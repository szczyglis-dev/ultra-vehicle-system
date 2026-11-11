.. _uvs-scripting-presentation--visual-feedback-lifetimes:

Visual feedback lifetimes
=========================

Presentation systems turn cached vehicle feedback into particles and persistent marks. ``TireFeedback`` classifies contact activity once; audio, smoke and skidmarks consume that result. The simulation does not depend on a particle being visible or a ribbon segment being generated.

The main extension concern is resource lifetime. Some effects are continuously reused, some particles live briefly after emission stops, and world-space marks intentionally outlive the current wheel contact. A custom effect should define which resources it owns and when that history is cleared.

.. _uvs-scripting-presentation--configure-in-the-inspector-first:

Configure in the Inspector first
--------------------------------

Follow :ref:`exhaust/tire/jet setup <uvs-particles--inspector-quick-start-add-an-exhaust-outlet>`, :ref:`tire marks <uvs-decals--inspector-quick-start>` and :ref:`ground surface profiles <uvs-surfaces--inspector-quick-start-create-a-gravel-patch>`. Assign the mechanic/feedback source and outputs, apply/save, and test one emitter before writing a custom effect. The lifetime code below is for extending presentation rather than a requirement for ordinary authoring.

.. _uvs-scripting-presentation--implementation-map:

Implementation map
------------------

+--------------------+-------------------------------------------------------------------+
| Class              | Responsibility                                                    |
+====================+===================================================================+
| ``ExhaustSmoke``   | Controls emission from configured exhaust outlets.                |
+--------------------+-------------------------------------------------------------------+
| ``PropulsionJets`` | Presents propulsion exhaust/jet outlets.                          |
+--------------------+-------------------------------------------------------------------+
| ``SkidmarkBuffer`` | Stores bounded world-space ribbon geometry.                       |
+--------------------+-------------------------------------------------------------------+
| ``Skidmarks``      | Consumes contact state and controls trail history.                |
+--------------------+-------------------------------------------------------------------+
| ``TireFeedback``   | Builds per-wheel presentation state after mechanics.              |
+--------------------+-------------------------------------------------------------------+
| ``TireSmoke``      | Manages wheel smoke and granular emission.                        |
+--------------------+-------------------------------------------------------------------+
| ``WheelContact``   | Carries cached contact/activity and selected effect-surface data. |
+--------------------+-------------------------------------------------------------------+

.. _uvs-scripting-presentation--tirefeedback-boundary:

TireFeedback boundary
---------------------

Use feedback when the effect should reflect resolved behavior. A held brake input does not always mean a tire is skidding, and full throttle in the air does not mean dust should appear at the ground. Contact, load, slip and selected surface provide the relevant evidence.

A replacement renderer can consume the same classification without modifying tire friction. Keep any custom physical grip model in the friction/contact layer; otherwise turning off visual effects could unexpectedly change driving behavior.

``TireFeedback`` samples wheel contact, slip and selected effect surface after the mechanical pipeline. ``TireAudio``, ``TireSmoke`` and ``Skidmarks`` consume that state. Visual effect settings do not change friction or engine torque.

.. _uvs-scripting-presentation--particle-ownership:

Particle ownership
------------------

``TireSmoke`` owns per-wheel emission for smoke and granular material. ``ExhaustSmoke`` follows configured outlets and engine activity. ``PropulsionJets`` presents the selected aircraft/hover propulsion outlets. Their source data differs even when each eventually drives a ``ParticleSystem``.

Vehicle creation assigns shared presets from ``Resources/Effects``: tire smoke, exhaust smoke and their materials, loose-ground material, and the skidmark material. These assets do not depend on Demo. The package presets retain built-in contact-normal orientation, surface smoke/sand switching and engine-load animation; a user-supplied prefab retains its existing custom-artwork behavior. Repeating setup fills empty references without replacing custom assignments.

Choose between generated systems and assigned artwork deliberately. A generated system needs owned material/instance cleanup. An assigned system should keep its authored appearance unless the configured integration explicitly allows the module to animate those properties. An external particle framework can replace the renderer while using the same resolved source activity.

Use ``TireSmoke.SetSmokeMode(...)`` with ``TireSmokeMode.Automatic``, ``ContactPatch`` or ``TireRing`` to select automatic detection, ordinary smoke or a requested tire-ring cloud. Tire Ring still respects grounded contact and surface restrictions. ``WheelBurnoutChanged(index, active)`` reports transitions, ``IsWheelBurningOut(index)`` reads state, and ``GetBurnoutParticles(index)`` returns the generated emitter. See :ref:`tire smoke setup <uvs-particles--standing-burnout>` for tuning.

``SetJetsEnabled`` controls jet presentation, not propulsion power. Likewise, turning tire smoke off should not change grip. Use these presentation gates for quality settings and camera-distance policies; keep physical participation in the mechanics that own it.

Distinguish stopping emission from deleting particles. A natural throttle release may stop new exhaust while allowing existing particles to expire. A scene reset may need to clear all owned particles immediately. A pooled vehicle needs a deliberate reset policy so effects from its previous use do not appear at its next spawn.

Assigned particle prefabs are part of the application's art direction. Preserve their authored appearance unless the component's configured mode explicitly delegates animation of those properties. Track generated instances separately from shared assets, and destroy only the resources this effect created.

Generated particle systems belong to their creating module. Assigned systems/prefabs retain authored appearance unless a module explicitly offers custom-particle animation. Emission and outlet pose still follow the module. Disabling stops emission/clears the relevant owned channels according to their policy; natural stops may let existing particles expire.

``TireSmoke`` uses bounded smoke/granular pools per wheel. Surface changes choose emission style without retroactively turning already emitted smoke into grains. Exhaust uses explicit outlets; ``PropulsionJets`` selects its hover/aircraft arrays. ``Propulsion`` mesh animation is separate from particle emission.

.. _uvs-scripting-presentation--mark-buffers:

Mark buffers
------------

Marks store the position and surface properties at creation time. This is why a segment remains on the original ground rather than following the wheel or adopting the next surface's tint. It also explains why marks on moving ground need a different ownership/frame strategy if the application expects them to remain attached to that object.

The newest active segment follows the rendered wheel hub after wheel presentation, with support checked against its original contact collider. This closes the visual gap caused by physics/contact sampling lag at speed. Before the next physics sample commits history, the segment's sampled endpoint is restored; older marks keep their recorded world positions. Loss of contact, disabled feedback, unsupported edges and large jumps stop this live extension. The same mesh and bounded pool are reused, with no extra mark objects or warmed per-frame managed allocations.

Capacity is a history budget. Increasing it retains more trail but also increases potential geometry and upload work. Choose it from expected visible history, not session duration. A bounded buffer makes a long-running driving scene predictable even if the vehicle never stops.

``Skidmarks`` uses a bounded world-space ribbon buffer. Segments keep their recorded surface tint/lifetime. Trails break on contact/surface discontinuity, large jumps or gaps. Old world-space marks do not move with kinematic ground. Changed vertex ranges and maintained bounds limit uploads; capacity bounds history independently of driving time.

.. _uvs-scripting-presentation--clear-a-vehicles-trail-history:

Clear a vehicle's trail history
-------------------------------

An explicit reset action is clearer than coupling every teleport to presentation deletion. A garage teleport may retain existing world marks; restarting a challenge may need a clean track. The application chooses that rule and calls the effect operation accordingly.

Use this for an explicit scene/demo reset where marks should disappear. Pose reset alone need not erase presentation history.

**Example:** ``ClearVehicleTrails.cs``

.. raw:: html

   <!-- example: ClearVehicleTrails.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ClearVehicleTrails : MonoBehaviour
       {
           public Skidmarks marks;
           public void Clear() { if (marks) marks.ClearMarks(); }
       }
   }

``ClearMarks`` breaks prior trails and publishes Cleared. It is different from repairing damaged parts or deleting world debris. See :doc:`performance </Performance>` for workload-based budgeting and :doc:`asset bindings </DemoResources>` for supplied materials.

.. _uvs-scripting-presentation--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed particles and tire marks API </API/Presentation>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-presentation--boatwaterparticles:

BoatWaterParticles
~~~~~~~~~~~~~~~~~~

:ref:`BoatWaterParticles <uvs-api-presentation--boatwaterparticles>` gives the full declared contract.

+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Method                                                      | Role                                                                              |
+=============================================================+===================================================================================+
| ``public override void Configure(VehicleController owner)`` | Caches the vehicle and resolves an unassigned engine reference.                   |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual void RenderWater(float deltaTime)``        | Updates water particles from resolved hull-water contact.                         |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual void Suspend()``                           | Stops owned water-particle presentation according to the module's cleanup policy. |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--ivehiclemodule:

IVehicleModule
~~~~~~~~~~~~~~

:ref:`IVehicleModule <uvs-api-modules--ivehiclemodule>` gives the full declared contract.

+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Method                                                                     | Role                                                                                                                        |
+============================================================================+=============================================================================================================================+
| ``void Configure(VehicleController vehicle)``                              | Repeatable setup contract supplied with the owning ``VehicleController``.                                                   |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``void Step(VehicleController vehicle, Command command, float deltaTime)`` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--particlefactory:

ParticleFactory
~~~~~~~~~~~~~~~

:ref:`ParticleFactory <uvs-api-presentation--particlefactory>` gives the full declared contract.

+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Method                                                                                                       | Role                                                                                  |
+==============================================================================================================+=======================================================================================+
| ``public static ParticleSystem CreateSmoke(string name, Transform parent, Material material, bool exhaust)`` | Creates a smoke particle system using the supplied material and owned parent.         |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public static ParticleSystem CreateSand(string name, Transform parent, Material material)``                | Creates a granular tire-particle system using the supplied material and owned parent. |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public static void SetRate(ParticleSystem system, float rate)``                                            | Sets a particle emission rate on an existing system.                                  |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--propulsionjets:

PropulsionJets
~~~~~~~~~~~~~~

:ref:`PropulsionJets <uvs-api-presentation--propulsionjets>` gives the full declared contract.

+----------------------------------------------------+-------------------------------------------------------------------------------------+
| Method                                             | Role                                                                                |
+====================================================+=====================================================================================+
| ``public virtual void SetJetsEnabled(bool value)`` | Changes propulsion-jet presentation availability without setting mechanical thrust. |
+----------------------------------------------------+-------------------------------------------------------------------------------------+

+--------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Event / callback                                 | Role                                                                                               |
+==================================================+====================================================================================================+
| ``public event Action<bool> JetsEnabledChanged`` | When jet presentation availability changes. Payload: bool; this does not report mechanical thrust. |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--skidmarkbuffer:

SkidmarkBuffer
~~~~~~~~~~~~~~

:ref:`SkidmarkBuffer <uvs-api-presentation--skidmarkbuffer>` gives the full declared contract.

+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Method                                                                                                                                   | Role                                                                                     |
+==========================================================================================================================================+==========================================================================================+
| ``public void Add(Vector3 from, Vector3 to, Vector3 normal, float width, float intensity, float birthTime)``                             | Appends a mark segment to the bounded geometry buffer and returns its buffer identifier. |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public void Add(Vector3 from, Vector3 to, Vector3 normal, float width, float intensity, float birthTime, Color tint, float lifetime)`` | Appends a mark segment to the bounded geometry buffer and returns its buffer identifier. |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public void Upload()``                                                                                                                 | Uploads changed mark geometry to the owned mesh.                                         |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--skidmarks:

Skidmarks
~~~~~~~~~

:ref:`Skidmarks <uvs-api-presentation--skidmarks>` gives the full declared contract.

+--------------------------------------+-------------------------------------------------------------------------+
| Method                               | Role                                                                    |
+======================================+=========================================================================+
| ``public virtual void ClearMarks()`` | Clears this vehicle's recorded mark history and breaks existing trails. |
+--------------------------------------+-------------------------------------------------------------------------+

+----------------------------------------+------------------------------------------------+
| Event / callback                       | Role                                           |
+========================================+================================================+
| ``public event System.Action Cleared`` | After skidmark history is cleared. No payload. |
+----------------------------------------+------------------------------------------------+

.. _uvs-scripting-presentation--tiresmoke:

TireSmoke
~~~~~~~~~

:ref:`TireSmoke <uvs-api-presentation--tiresmoke>` gives the full declared contract.

+----------------------------------------------------------------+---------------------------------------------------------------------------+
| Method                                                         | Role                                                                      |
+================================================================+===========================================================================+
| ``public virtual ParticleSystem GetWheelParticles(int index)`` | Returns the smoke/granular particle systems owned for a configured wheel. |
+----------------------------------------------------------------+---------------------------------------------------------------------------+

+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Method / event / callback                                      | Role                                                                                    |
+================================================================+=========================================================================================+
| ``public event System.Action<int, bool> WheelBurnoutChanged``  | See :ref:`TireSmoke <uvs-api-presentation--tiresmoke>` for configuration and lifecycle. |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public event System.Action<TireSmokeMode> SmokeModeChanged`` | See :ref:`TireSmoke <uvs-api-presentation--tiresmoke>` for configuration and lifecycle. |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public bool IsWheelBurningOut(int index)``                   | See :ref:`TireSmoke <uvs-api-presentation--tiresmoke>` for configuration and lifecycle. |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public ParticleSystem GetBurnoutParticles(int index)``       | See :ref:`TireSmoke <uvs-api-presentation--tiresmoke>` for configuration and lifecycle. |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public void SetSmokeMode(TireSmokeMode mode)``               | See :ref:`TireSmoke <uvs-api-presentation--tiresmoke>` for configuration and lifecycle. |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--vehiclemodule:

VehicleModule
~~~~~~~~~~~~~

:ref:`VehicleModule <uvs-api-modules--vehiclemodule>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                                   |
+===========================================================================================+========================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                          | Role                                                                                                              |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--waterparticlefactory:

WaterParticleFactory
~~~~~~~~~~~~~~~~~~~~

:ref:`WaterParticleFactory <uvs-api-presentation--waterparticlefactory>` gives the full declared contract.

+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Method                                                                                                           | Role                                                                                           |
+==================================================================================================================+================================================================================================+
| ``public static ParticleSystem Create(Transform parent, string name, Material material, bool foam, int budget)`` | Creates an owned water-particle presentation system with the requested style/material context. |
+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

.. _uvs-scripting-presentation--physical-jet-exhaust:

Physical jet exhaust
--------------------

Add the optional ``JetBlast`` to a configured vehicle and assign its outward-facing outlets. Read ``Strength``, or observe forces without replacing vehicle physics:

.. code-block:: csharp

   var blast = vehicle.GetComponent<JetBlast>();
   blast.BodyPushed += (body, force) => Debug.Log($"Jet exhaust pushed {body.name}: {force.magnitude} N");
   blast.SetEnabled(true);

The event runs once for each affected body per outlet and physics step. Avoid logging every call in production. See :ref:`Jet Blast setup <uvs-particles--jet-blast>`.
