.. _uvs-scripting-suspension--native-suspension-and-visual-linkage:

Native suspension and visual linkage
====================================

``Suspension`` has a physical layer and a model-animation layer. The physical layer configures native wheel springs and dampers that carry the chassis. The animation layer moves shocks, hubs and links so the visible assembly matches wheel travel and steering.

Start by establishing stable wheel support, then fit the linkage around that result. A visually convincing arm cannot compensate for the wrong spring rate, and raising spring force cannot repair a linkage whose endpoints cannot reach the hub.

.. _uvs-scripting-suspension--implementation-map:

Implementation map
------------------

+--------------------+----------------------------------------------------------------------------+
| Class              | Responsibility                                                             |
+====================+============================================================================+
| ``AntiRoll``       | Adds cross-wheel roll support for the configured wheel relationships.      |
+--------------------+----------------------------------------------------------------------------+
| ``ControlArm``     | Resolves a visual control arm against its authored geometry.               |
+--------------------+----------------------------------------------------------------------------+
| ``HalfShaft``      | Presents axle articulation and shaft rotation.                             |
+--------------------+----------------------------------------------------------------------------+
| ``ShockAbsorber``  | Animates a telescoping shock and optionally overrides one wheel's physics. |
+--------------------+----------------------------------------------------------------------------+
| ``SteeringTieRod`` | Tracks steering-link endpoints and geometry.                               |
+--------------------+----------------------------------------------------------------------------+
| ``Suspension``     | Configures native wheel support and suspension-related response.           |
+--------------------+----------------------------------------------------------------------------+
| ``SuspensionHub``  | Provides hub/kingpin geometry for the wheel assembly.                      |
+--------------------+----------------------------------------------------------------------------+

.. _uvs-scripting-suspension--configuration-ownership:

Configuration ownership
-----------------------

``settings.suspensionTravel`` is shared vehicle configuration. The ``Suspension`` component supplies spring and damping policy. A ``ShockAbsorber`` with ``overrideWheelPhysics`` deliberately takes authority for its selected wheel, allowing asymmetric or individually authored support.

Spring force depends on displacement, while damping depends on relative motion. Increasing damping suppresses oscillation but can also resist a fast wheel movement over a bump. Increasing travel provides room for that movement but changes how far the chassis can settle. Tune mass, spring, damper and travel together; changing only visual shock length does not alter available native travel.

``Suspension`` configures ``WheelCollider`` spring/damper, target position, damping, expansion policy, travel and force point. Global travel comes from vehicle ``Settings``. ``ShockAbsorber`` overrides apply only to owned wheels with ``overrideWheelPhysics`` enabled; the first override per wheel is used.

Native ``WheelCollider`` owns suspension support. Visual helpers consume wheel/anchor poses; they do not create an independent unsprung rigidbody solver.

+--------------------------------------+-----------------------------------------+
| Quantity                             | Unit/meaning                            |
+======================================+=========================================+
| Spring                               | N/m                                     |
+--------------------------------------+-----------------------------------------+
| Damper                               | N·s/m                                   |
+--------------------------------------+-----------------------------------------+
| Travel                               | Metres                                  |
+--------------------------------------+-----------------------------------------+
| Target Position                      | Normalized native suspension target     |
+--------------------------------------+-----------------------------------------+
| Motion Ratio                         | Shock stroke / wheel stroke             |
+--------------------------------------+-----------------------------------------+
| Shock wheel-equivalent spring/damper | Shock value multiplied by ratio squared |
+--------------------------------------+-----------------------------------------+

Automatic force placement uses the center of mass, configured offset and travel-dependent body-sway lever. Degressive damping reduces high-stroke-speed damping above the blowoff speed. ``ContactEnvelope`` supplies its support distance to this damping path; native center contact is used without it.

.. _uvs-scripting-suspension--apply-a-load-preset:

Apply a load preset
-------------------

The sample separates a UI-editable preset from the act of applying it. ``ApplyPreset`` writes the authoritative shared fields and asks the controller to validate/reconfigure once. This is useful for a spawn loadout or workshop adjustment; running full vehicle configuration every frame would repeatedly write native settings and rebuild unrelated setup.

A failed configuration should be shown to the caller or logged with vehicle context, as below. For a production editor, validate the requested values before committing an entire multi-field preset, so an invalid wheel definition does not leave the user unsure which settings were accepted.

Attach this application component to a tuning object, assign vehicle and ``Suspension``, then invoke ``ApplyPreset`` after changing mass or a load preset. It deliberately applies configuration once per request, not every frame.

**Example:** ``SuspensionPreset.cs``

.. raw:: html

   <!-- example: SuspensionPreset.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SuspensionPreset : MonoBehaviour
       {
           public VehicleController vehicle;
           public Suspension suspension;
           [Min(1)] public float spring = 30000;
           [Min(0)] public float damper = 2500;
           [Min(.05f)] public float travel = .2f;

           public void ApplyPreset()
           {
               if (!vehicle || !suspension) return;
               suspension.spring = spring;
               suspension.damper = damper;
               vehicle.settings.suspensionTravel = travel;
               if (!vehicle.TryApplyConfiguration(out var error))
                   Debug.LogWarning(error, vehicle);
           }
       }
   }

Per-wheel shock overrides remain authoritative for their wheels. Change those overrides when the preset must cover them too.

.. _uvs-scripting-suspension--visual-assemblies:

Visual assemblies
-----------------

A suspension helper describes a geometric relationship, not an extra wheel-force source. ``ControlArm`` locates the hub from an arm relationship; ``SuspensionHub`` presents the hub/kingpin; ``SteeringTieRod`` resolves steering linkage and can feed configured steering placement to the native wheel. ``HalfShaft`` follows articulation while retaining shaft spin. ``SuspensionAxle`` provides an axle assembly pose.

Author stable chassis-side anchors and the correct wheel/hub references. Then validate each helper with suspension compression and steering separately before combining them. ``UpdatePose()`` is the explicit geometry operation on these helpers, useful for an integration that owns its update; it should not become an additional unconditional call when built-in presentation is already updating the same transform.

For a new linkage shape, extend the helper closest to that geometric responsibility. Keep a model's decorative offsets below the motion transform. If replacing the hub calculation also changes the effective steering center, preserve the native/visual frame relationship rather than correcting only the mesh's apparent position.

Build the assembly using stable neutral frames. Imported models often have inconvenient local axes or scale; place them below motion pivots whose axes and unit scale match the helper's expectations. Keep neutral measurement endpoints separate from transforms that the helper itself moves.

A motion ratio is a geometry conversion. If the shock travels half as far as the wheel, the spring/damper conversion uses the ratio squared; using the raw shock rate as the wheel rate would misrepresent support. Check the intended measurement direction and units before tuning around an apparent stiffness mismatch.

-  ``ShockAbsorber`` places casing/piston between authored endpoints with fixed individual lengths.
-  ``ControlArm``, ``SuspensionHub`` and ``SteeringTieRod`` resolve linkage and kingpin geometry; wheel-center offsets also feed native collider steering placement where configured.
-  ``HalfShaft`` follows connected endpoints and retains tire spin separately from articulation.
-  Axis permissions and angular/length limits constrain the requested geometry; they cannot make incompatible endpoints reachable.

Keep imported mesh transforms below unit-scale motion pivots. Derive mesh length/axis from the actual model. The visual frame and physics frame must refer to the same hub; using already-displaced wheel geometry as the neutral source creates feedback.

See :doc:`wheel contact </Scripting/WheelContact>` for radius correction and :doc:`aircraft </Scripting/Aircraft>` for load-driven gear hinges.

.. _uvs-scripting-suspension--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed suspension and linkage API </API/Suspension>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-suspension--antiroll:

AntiRoll
~~~~~~~~

:ref:`AntiRoll <uvs-api-suspension--antiroll>` gives the full declared contract.

+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                         |
+=========================================================================+==============================================================================================+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Transfers bounded anti-roll load between eligible supported wheels in configured axle pairs. |
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.         |
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--controlarm:

ControlArm
~~~~~~~~~~

:ref:`ControlArm <uvs-api-suspension--controlarm>` gives the full declared contract.

+-------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Method                                                | Role                                                                                    |
+=======================================================+=========================================================================================+
| ``public virtual Vector3 ResolveHub(Vector3 sample)`` | Resolves the hub position from this control arm's authored geometry.                    |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public virtual void UpdatePose()``                  | Recomputes this visual linkage's pose from its authored geometry and current endpoints. |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--halfshaft:

HalfShaft
~~~~~~~~~

:ref:`HalfShaft <uvs-api-suspension--halfshaft>` gives the full declared contract.

+--------------------------------------+-----------------------------------------------------------------------------------------+
| Method                               | Role                                                                                    |
+======================================+=========================================================================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. |
+--------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--ivehiclemodule:

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

.. _uvs-scripting-suspension--shockabsorber:

ShockAbsorber
~~~~~~~~~~~~~

:ref:`ShockAbsorber <uvs-api-suspension--shockabsorber>` gives the full declared contract.

+--------------------------------------+-----------------------------------------------------------------------------------------+
| Method                               | Role                                                                                    |
+======================================+=========================================================================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. |
+--------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--steeringtierod:

SteeringTieRod
~~~~~~~~~~~~~~

:ref:`SteeringTieRod <uvs-api-suspension--steeringtierod>` gives the full declared contract.

+----------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Method                                                   | Role                                                                                    |
+==========================================================+=========================================================================================+
| ``public virtual void ApplyNativeSteering(float angle)`` | Applies resolved linkage steering placement to the native wheel configuration.          |
+----------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public virtual float ResolveSteering(float demand)``   | Resolves the linkage's steering geometry for the supplied wheel/angle state.            |
+----------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public virtual void UpdatePose()``                     | Recomputes this visual linkage's pose from its authored geometry and current endpoints. |
+----------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--suspension:

Suspension
~~~~~~~~~~

:ref:`Suspension <uvs-api-suspension--suspension>` gives the full declared contract.

-  ``public event Action<LandingEvent> Landed`` — // First wheel support after qualifying flight; copied impact context.
-  ``public event Action<LandingEvent> LandingCompleted`` — // All operational wheel rays have support after Landed; not a promise of settled suspension.
-  ``public override void Configure(VehicleController v)`` — Binds the component to its configured owner and selected source.
-  ``public virtual void ResetVehicleState(VehicleResetReason reason)`` — Clears transient state for the supplied reset reason without changing persistent configuration.
-  ``public override void Step(VehicleController v, Command c, float dt)`` — Current step.
-  ``public override bool SupportsProfile(DriveProfile profile)`` — Current supports profile.

.. _uvs-scripting-suspension--suspensionaxle:

SuspensionAxle
~~~~~~~~~~~~~~

:ref:`SuspensionAxle <uvs-api-suspension--suspensionaxle>` gives the full declared contract.

+--------------------------------------+-----------------------------------------------------------------------------------------+
| Method                               | Role                                                                                    |
+======================================+=========================================================================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. |
+--------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--suspensionhub:

SuspensionHub
~~~~~~~~~~~~~

:ref:`SuspensionHub <uvs-api-suspension--suspensionhub>` gives the full declared contract.

+--------------------------------------+-----------------------------------------------------------------------------------------+
| Method                               | Role                                                                                    |
+======================================+=========================================================================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. |
+--------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--suspensionrotationlimits:

SuspensionRotationLimits
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`SuspensionRotationLimits <uvs-api-suspension--suspensionrotationlimits>` gives the full declared contract.

+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Method                                                              | Role                                                                                             |
+=====================================================================+==================================================================================================+
| ``public Quaternion Apply(Quaternion desired, Quaternion neutral)`` | Applies authored angular permissions/limits to a world rotation relative to its reference frame. |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Quaternion ApplyLocal(Quaternion relative)``               | Constrains a local requested rotation to the configured angular permissions and bounds.          |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float Angle(float angle, Vector3 axis)``                   | Returns a signed angular component in degrees for the configured constrained frame.              |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. _uvs-scripting-suspension--vehiclemodule:

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
