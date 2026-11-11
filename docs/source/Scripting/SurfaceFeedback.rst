.. _uvs-scripting-surfacefeedback--surface-lookup-and-feedback:

Surface lookup and feedback
===========================

Ground classification has two independent consumers: physics needs a grip value, while presentation needs a description of sound, particles and marks. The package keeps these separate so art changes do not silently retune the vehicle's handling.

A ground patch can therefore have a ``Surface`` for friction and a ``TireSurface`` for effect selection. A ``TireSurfaceProfile`` is a reusable presentation asset. Matching the two is an authoring decision rather than an implicit conversion from a material name.

.. _uvs-scripting-surfacefeedback--implementation-map:

Implementation map
------------------

+------------------------+-----------------------------------------------------------------+
| Class                  | Responsibility                                                  |
+========================+=================================================================+
| ``Friction``           | Reads physical grip and writes native tire friction behavior.   |
+------------------------+-----------------------------------------------------------------+
| ``Surface``            | Stores the physical grip multiplier on a contact collider.      |
+------------------------+-----------------------------------------------------------------+
| ``TireFeedback``       | Resolves and caches the presentation classification.            |
+------------------------+-----------------------------------------------------------------+
| ``TireSurface``        | Maps a collider/hierarchy or Terrain layers to effect profiles. |
+------------------------+-----------------------------------------------------------------+
| ``TireSurfaceProfile`` | Stores presentation assets and effect multipliers.              |
+------------------------+-----------------------------------------------------------------+
| ``WheelContact``       | Publishes the selected profile with per-wheel feedback.         |
+------------------------+-----------------------------------------------------------------+

.. _uvs-scripting-surfacefeedback--physical-friction:

Physical friction
-----------------

The exact-collider rule makes physical authoring predictable but requires attention on compound ground. A component on a parent's ``GameObject`` does not automatically supply grip to every child collider. Put the physical surface on each collider that needs it, or implement an explicit alternative lookup policy.

Vehicle grip and ground grip multiply rather than replace each other. Check a vehicle on a known reference ground before changing both at once. Otherwise a low tire-grip setup and a low ground multiplier can combine into a much larger reduction than intended.

``Friction`` reads ``Surface`` from the exact collider in the native ``WheelHit``. Forward stiffness is vehicle grip multiplied by that component's grip. Side stiffness additionally uses handbrake/tracked policy. ``TireSurfaceProfile`` does not participate in this calculation.

This lookup does not traverse parents or painted Terrain Layers. Supply a custom friction module if physical grip must follow a layered terrain map.

.. _uvs-scripting-surfacefeedback--presentation-classification:

Presentation classification
---------------------------

Hierarchy lookup is useful when several colliders share one visual surface family. A nearer mapping lets a small child patch override the surrounding terrain or road. An explicitly present mapping with no profile can intentionally clear presentation, so it must not be confused with an absent mapping.

Treat shared profile assets as reusable configuration. If one vehicle needs a runtime variation, use a deliberate local configuration/asset instance rather than editing a shared asset that every nearby tire reads. Physical grip remains a separate setting even when the visible road, sound and particles all come from one authored surface family.

``TireFeedback`` resolves ``TireSurface`` from the contact collider or nearest parent, with an owned cache invalidated by mapping revisions. A nearer component takes precedence even when its profile is empty. Without an active nearest ``TireSurface``, ``TireFeedback`` uses ``defaultSurface``. An active nearest component with an empty profile resolves ``null`` instead of falling through to its parent or ``defaultSurface``. The result is published in each ``WheelContact``.

``TireSurfaceProfile`` controls particles, marks, tire audio, rolling activity and brake audio. Its optional ``brakingLoop`` replaces the Brake Audio component recording for wheels on that surface. For empty recordings, ``useDefaultTireLoopWhenEmpty`` and ``useDefaultBrakeLoopWhenEmpty`` independently choose component fallback or silence. Defaults are false for tire audio and true for brake audio. Surface tire volume/pitch apply to its fallback recording; ``brakeAudioMultiplier`` scales either brake recording. A ``null`` profile uses general vehicle-effect settings. Set ``particlesEnabled``/``marksEnabled`` or per-effect multipliers independently.

Terrain mappings sample the dominant painted layer from an editor/runtime-prepared classification. ``RefreshTerrain()`` rebuilds the cache after painting or changing mappings. Painting does not automatically produce a layer-dependent physical friction model.

.. _uvs-scripting-surfacefeedback--configure-a-ground-patch:

Configure a ground patch
------------------------

The adapter demonstrates both responsibilities on one collider object. ``grip`` changes the mechanical multiplier; ``effects`` chooses an existing presentation asset. ``RefreshTerrain()`` refreshes the classification data where Terrain mapping is relevant; it is not a command to recalculate native tire friction.

For a level-authoring workflow, these components can normally be saved directly on the ground prefab. The runtime example is useful for generated terrain patches or objects created by an application tool.

Attach this example to the same object as the ground collider. It configures both systems explicitly. Assign a pre-authored effect profile; it never edits a shared profile asset at runtime.

**Example:** ``GroundPatchSetup.cs``

.. raw:: html

   <!-- example: GroundPatchSetup.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       [RequireComponent(typeof(Collider))]
       public class GroundPatchSetup : MonoBehaviour
       {
           [Range(.05f, 3)] public float grip = .8f;
           public TireSurfaceProfile effects;

           private void Awake()
           {
               var physical = GetComponent<Surface>();
               if (!physical) physical = gameObject.AddComponent<Surface>();
               physical.grip = grip;

               var presentation = GetComponent<TireSurface>();
               if (!presentation) presentation = gameObject.AddComponent<TireSurface>();
               presentation.profile = effects;
               presentation.RefreshTerrain();
           }
       }
   }

.. _uvs-scripting-surfacefeedback--replace-a-presentation-mapping-at-runtime:

Replace a presentation mapping at runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A generated ground patch can change which effect profile it resolves without editing the shared profile asset. Assign the patch's ``TireSurface``, request another profile, then refresh classification data. This changes new feedback resolution; existing particles/marks keep their recorded lifetimes and properties.

**Example:** ``GroundEffectMapping.cs``

.. raw:: html

   <!-- example: GroundEffectMapping.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class GroundEffectMapping : MonoBehaviour
       {
           public TireSurface mapping;

           public void Select(TireSurfaceProfile profile)
           {
               if (!mapping) return;
               mapping.profile = profile;
               mapping.RefreshTerrain();
           }
       }
   }

A ``null`` profile on an active nearest mapping deliberately resolves no profile; it does not fall through to a parent/default. This adapter also does not change ``Surface.grip``. For Terrain-layer mappings, update the intended layer entries rather than assuming the single profile replaces painted-layer selection.

.. _uvs-scripting-surfacefeedback--consumers-and-transitions:

Consumers and transitions
-------------------------

A surface profile is shared presentation configuration. ``TireAudio`` interprets its loop and audio multipliers, ``TireSmoke`` interprets particle activity/style, and ``Skidmarks`` records mark properties when a segment is created. Each consumer owns how a transition is rendered.

When the wheel moves from road to dirt, new emissions and sounds follow the newly resolved profile. Existing particles and marks keep their own lifetime/history; they do not need to be rewritten to match the current wheel surface. This avoids making old road marks change tint because the wheel later touched mud.

For a new effect, consume the selected ``WheelContact`` profile and resolved contact activity. Do not repeat a different parent lookup in the effect unless the application intentionally wants a different classification policy. Shared classification keeps particles, marks and sound in agreement.

``TireSmoke`` uses grounded skid/rolling activity. Generated systems use bounded smoke/grain pools; custom systems retain their authored design. ``Skidmarks`` records per-segment tint and lifetime so old marks keep the surface on which they were created. ``TireAudio`` crossfades profile loops per wheel; profile changes do not allocate an unbounded number of voices.

See :doc:`presentation lifetimes </Scripting/Presentation>` for pooling and :doc:`setup </Surfaces>` for the Inspector workflow.

.. _uvs-scripting-surfacefeedback--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed ground surfaces and classification API </API/SurfaceFeedback>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-surfacefeedback--friction:

Friction
~~~~~~~~

:ref:`Friction <uvs-api-surfacefeedback--friction>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                          |
+=========================================================================+===============================================================================================================+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Reads Surface from exact native hit colliders and writes forward/side friction with handbrake/tracked policy. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.                          |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-surfacefeedback--ivehiclemodule:

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

.. _uvs-scripting-surfacefeedback--tiresurface:

TireSurface
~~~~~~~~~~~

:ref:`TireSurface <uvs-api-surfacefeedback--tiresurface>` gives the full declared contract.

+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Method                                                                               | Role                                                                                                                  |
+======================================================================================+=======================================================================================================================+
| ``public virtual void RefreshTerrain()``                                             | Rebuilds cached painted-Terrain-layer classification after mapping/paint changes.                                     |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public virtual TireSurfaceProfile Resolve(Collider collider, Vector3 worldPoint)`` | Resolves the mapped effect profile for a native hit, including dominant Terrain-layer classification when configured. |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-surfacefeedback--tiresurfaceprofile:

TireSurfaceProfile
~~~~~~~~~~~~~~~~~~

:ref:`TireSurfaceProfile <uvs-api-surfacefeedback--tiresurfaceprofile>` gives the full declared contract.

+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| Method                                                          | Role                                                                               |
+=================================================================+====================================================================================+
| ``public virtual float Rolling(float speed)``                   | Evaluates this surface profile's rolling-presentation activity.                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public virtual float ParticleActivity(WheelContact contact)`` | Evaluates tire-particle activity from rolling/skid inputs and profile multipliers. |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public virtual float MarkActivity(WheelContact contact)``     | Evaluates skidmark activity using this surface profile's presentation multipliers. |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+

.. _uvs-scripting-surfacefeedback--vehiclemodule:

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
