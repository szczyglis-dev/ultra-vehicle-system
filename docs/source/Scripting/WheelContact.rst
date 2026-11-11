.. _uvs-scripting-wheelcontact--wheel-configuration-and-contact:

Wheel configuration and contact
===============================

Wheel behavior combines authored wheel definitions, runtime adapters and Unity's native ``WheelCollider``. The native collider provides suspension and primary rolling contact. Optional package systems refine obstacle support and solid tire interactions while the visible mesh follows the resulting wheel pose.

The important integration rule is to keep authoring, simulation and presentation frames distinct. A mesh can have import offsets and a visual suspension pose without moving the object from which the physics contact is measured.

.. _uvs-scripting-wheelcontact--implementation-map:

Implementation map
------------------

+-----------------------+--------------------------------------------------------------------------+
| Class                 | Responsibility                                                           |
+=======================+==========================================================================+
| ``ContactEnvelope``   | Samples tire-shaped support and adjusts effective native support radius. |
+-----------------------+--------------------------------------------------------------------------+
| ``TireCollision``     | Adds supplemental solid tire contacts.                                   |
+-----------------------+--------------------------------------------------------------------------+
| ``VehicleController`` | Validates definitions and builds/configures wheel adapters.              |
+-----------------------+--------------------------------------------------------------------------+
| ``Wheel``             | Runtime adapter for one native wheel, actuation and contact state.       |
+-----------------------+--------------------------------------------------------------------------+
| ``WheelDynamics``     | Applies wheel rotational behavior including airborne losses.             |
+-----------------------+--------------------------------------------------------------------------+
| ``WheelSetup``        | Persists collider, geometry, visual and wheel-role authoring data.       |
+-----------------------+--------------------------------------------------------------------------+

.. _uvs-scripting-wheelcontact--wheelsetup-and-wheel:

WheelSetup and Wheel
--------------------

For a manually assembled wheel, add ``Wheel`` to the physics wheel object; its required-component declaration also adds ``WheelCollider``. Assign that collider in the controller's wheel definitions and assign a separate visual transform. The controller can create a missing adapter during configuration, but the saved definition remains the source for geometry and roles.

A driven wheel and a steered wheel are independent roles. Free-rolling trailer and aircraft wheels still need contact and brake configuration even when they receive no engine torque. A visual wheel is not a replacement for a native collider, and adding a collider alone does not declare its role in the vehicle.

``WheelSetup`` is the persisted authoring record. ``TryApplyConfiguration`` copies it to a ``Wheel`` adapter on each collider object, creates a missing adapter, sets mass/geometry/roles and configures the registered mechanics. A ``Wheel`` visual is positioned separately from its collider object.

Validation requires at least one wheel for a wheel-required mode; non-wheel modes accept an empty list. Each collider must be unique and owned by the root ``Rigidbody``. Radius must be at least .05 m, width .02 m and mass 1 kg, with finite values.

Removed adapters have actuation cleared and are disabled. ``SetWheelEnabled`` changes the definition and adapter/collider availability together, subject to the current profile's wheel requirements.

.. _uvs-scripting-wheelcontact--change-wheel-availability:

Change wheel availability
-------------------------

Use the controller operation when a gameplay rule makes a wheel unavailable. The operation keeps the persisted definition, adapter and collider availability together. A direct ``WheelCollider.enabled`` assignment can leave these layers disagreeing and can be overwritten by configuration or a profile transition.

The index comes from the configured wheel list. If an application rebuilds that list at runtime, it should resolve its own stable wheel identity before invoking an index-based action. ``Wheel`` removal, a detached mesh and repair inventory are separate application rules.

This binds an application action to a wheel index from the configured list. It does not detach a mesh or implement tire damage; use it as the availability layer of your own damage system.

**Example:** ``WheelAvailabilityControl.cs``

.. raw:: html

   <!-- example: WheelAvailabilityControl.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class WheelAvailabilityControl : MonoBehaviour
       {
           public VehicleController vehicle;

           public void SetAvailable(int wheelIndex, bool available)
           {
               if (!vehicle || wheelIndex < 0 || wheelIndex >= vehicle.Wheels.Count) return;
               vehicle.SetWheelEnabled(wheelIndex, available);
           }
       }
   }

Do not enable a ``WheelCollider`` independently while a profile transition owns its contacts.

.. _uvs-scripting-wheelcontact--contactenvelope:

ContactEnvelope
---------------

``VehicleController.IsMoving()`` checks total translation and angular velocity (defaults 0.05 m/s and 0.02 rad/s), including direct motion and vertical travel. ContactEnvelope's **Performance / Optimization** foldout enables stationary sampling by default: one batch every ten fixed steps, using configurable speed thresholds. Damping still runs each awake step. Steering changes over 0.1 degrees, mount/centre movement over 1 mm, reparenting and tire radius/width changes also refresh stationary support; tiny pose jitter is tolerated. Movement or a driving/steering request refreshes immediately. A stationary curb correction can be retained between probes; moving significant corrections retain every-step refresh. Existing sleep-only throttling is separate.

Native wheel contacts can replace the extra centre ray only after current corner rays and an overlap query certify an unobstructed box face. The current face supplies the plane; the historical native hit is not accepted blindly. Other terrain and changed/missing contact use the original fresh centre query.

A single native wheel contact is efficient, but a sharp step or narrow obstacle may be poorly represented by a center sample. ``ContactEnvelope`` probes the rolling shape and uses the best supported height to modify the native contact approximation. The extra radius is a temporary solver input, not a visible tire growth effect.

Tune sample density for the obstacles the vehicle must traverse. More probes cost more queries and still cannot make a discontinuous obstacle physically smooth at every speed. Check support normals, layer filtering and the lift cap before increasing resolution; an excluded ground layer cannot be repaired by more samples.

The envelope samples a circular rolling profile longitudinally and across tire width. At a longitudinal offset x its circular support is sqrt(radius² − x²). The maximum sampled support relative to center support temporarily increases the native radius; the displayed tire retains authored physical size.

No center support means no correction: the envelope does not bridge a gap. Ground layers, normal threshold, finite reused hit buffers, sample resolution and lift cap limit the approximation. Owned colliders/triggers are excluded using nearest vehicle ownership, so detached debris can become external geometry.

The radius associated with a native hit is retained for proxy placement, suspension damping and anti-roll travel. Rendering may smooth scalar suspension extension; force/contact resolution uses simulated contact.

.. _uvs-scripting-wheelcontact--tirecollision:

TireCollision
-------------

``TireCollision`` gives the tire a solid interaction envelope for situations such as a sidewall meeting an obstacle. This complements rolling support rather than replacing the wheel's spring and tread traction. It matters most when contact occurs away from the region already supported by the native wheel/envelope.

Configure the actual wheel radius, width, mass and body clearance first. Check arch colliders and nearby body geometry so supplemental contacts do not begin inside the vehicle. Use the native-only setup as a baseline, then enable supplemental contact and inspect the obstacle case it is intended to solve.

A custom collision backend needs a deliberate division of contact responsibility. Preserve suppression of duplicate lower support when the native path is supporting the tire. Otherwise two systems can each provide the full support force, producing an apparent increase in suspension stiffness or lifting the vehicle.

Use supplemental contacts for tire sides and obstacle interactions that primary rolling support does not cover. Their ownership is deliberately complementary: two simultaneous lower support mechanisms would fight over ride height and could add excessive support. Evaluate native contact first, then inspect the supplemental path for the unsupported region.

When debugging, isolate the layers: verify a plain wheel on flat ground, add the envelope for rolling obstacles, then enable solid tire contacts. Keep the rendered tire dimensions consistent with the authored radius and width so apparent penetration can be compared with the actual simulation geometry.

Supplemental solid contacts cover sidewall/obstacle interactions. Native lower support and traction remain primary when center/envelope support is available. Supplemental lower constraints are suppressed in that supported region to avoid duplicate support/traction.

Tire mass/geometry and response parameters determine supplemental constraints. This is a hybrid backend, not deformable tire or independently articulated wheel-body simulation. Check body and arch clearance and tune the timestep for fast impacts.

``Wheel.Grounded`` includes recent loaded tread contacts; automatic shifts require loaded native road contacts. ``WheelDynamics`` supplies airborne bearing losses independently of service braking.

.. _uvs-scripting-wheelcontact--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed wheel definitions and contact API </API/WheelContact>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-wheelcontact--coasting:

Coasting
~~~~~~~~

:ref:`Coasting <uvs-api-wheelcontact--coasting>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                             |
+============================================================================================+==================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Resolves the local Trailer so towing propulsion intent can participate in coasting policy.                       |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Releases native zero-torque holding according to propulsion intent while preserving service/handbrake ownership. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-wheelcontact--contactenvelope-1:

ContactEnvelope
~~~~~~~~~~~~~~~

-  **ContactEnvelope** — ``public void InvalidateSupportQueries()`` — Invalidates centre-ray sharing after custom mid-step scene edits.

:ref:`ContactEnvelope <uvs-api-wheelcontact--contactenvelope>` gives the full declared contract.

-  ``public override void Configure(VehicleController vehicle)`` — Binds the component to its configured owner and selected source.
-  ``public virtual void ResetVehicleState(VehicleResetReason reason)`` — Clears transient state for the supplied reset reason without changing persistent configuration.
-  ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` — Current step.
-  ``public override bool SupportsProfile(DriveProfile profile)`` — Current supports profile.

.. _uvs-scripting-wheelcontact--ivehiclemodule:

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

.. _uvs-scripting-wheelcontact--tirecollision-1:

TireCollision
~~~~~~~~~~~~~

:ref:`TireCollision <uvs-api-wheelcontact--tirecollision>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                                                  |
+============================================================================================+=======================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | During Play Mode, rebuilds owned transient tire proxies, clears pose history and resolves ``ContactEnvelope``.                        |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Advances supplemental tire proxies/contacts, detects discontinuous vehicle motion and preserves the primary rolling-support boundary. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                  |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-wheelcontact--vehiclemodule:

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

.. _uvs-scripting-wheelcontact--wheel:

Wheel
~~~~~

:ref:`Wheel <uvs-api-wheelcontact--wheel>` gives the full declared contract.

+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                              | Role                                                                                                                         |
+=====================================================================================+==============================================================================================================================+
| ``public virtual bool GetGroundHit(out WheelHit hit)``                              | Contact wrapper for native physics and direct presentation ground queries.                                                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void GetWorldPose(out Vector3 position, out Quaternion rotation)`` | Hub pose including spin/steering in both modes.                                                                              |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Configure()``                                                 | Applies clamped native radius/mass, captures contact radius and configures native substeps when attached to a ``Rigidbody``. |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                     | Role                                                                                                                                                                                                                                              |
+===============================================================+===================================================================================================================================================================================================================================================+
| ``public event System.Action<Wheel, bool> AttachmentChanged`` | After state and collider/actuator availability update. Payload: this Wheel and new attached flag.                                                                                                                                                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAttached(bool attached)``            | Sets low-level wheel attachment state, clears actuators/direct/contact/visual history and updates native collider availability. Notifies once per change. Does not physically detach/remount a visual object; use WheelPart for debris lifecycle. |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-wheelcontact--wheeldynamics:

WheelDynamics
~~~~~~~~~~~~~

:ref:`WheelDynamics <uvs-api-wheelcontact--wheeldynamics>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                   |
+============================================================================================+========================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Caches owner/Suspension and captures each wheel's grounded damping baseline.                           |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Updates native rotational damping, including airborne bearing losses independently of service braking. |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                   |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-wheelcontact--wheelsetup:

WheelSetup
~~~~~~~~~~

:ref:`WheelSetup <uvs-api-wheelcontact--wheelsetup>` gives the full declared contract.

+-----------------------------------------------------+---------------------------------------------------------------------+
| Method                                              | Role                                                                |
+=====================================================+=====================================================================+
| ``public static WheelSetup FromWheel(Wheel wheel)`` | Builds an authored wheel definition from an existing wheel adapter. |
+-----------------------------------------------------+---------------------------------------------------------------------+

.. _uvs-scripting-wheelcontact--shared-wheel-support-queries:

Shared wheel-support queries
----------------------------

Tire Collision can reuse Contact Envelope's actual centre ray from the same fixed step when origin, direction, reach and layer mask match exactly. Raw hit candidates are retained, so Tire Collision still applies its own self/layer/normal filters. Cached older envelope support and certified-plane shortcuts do not count as fresh centre rays. No telemetry chassis-height ray is substituted for a wheel ray.

If a custom module moves or changes physics geometry between Contact Envelope and Tire Collision in one step, call ``ContactEnvelope.InvalidateSupportQueries()`` after the edit. The tire module then performs its own raycasts. Envelope disable, reset/teleport and the next sampling step also invalidate sharing.
