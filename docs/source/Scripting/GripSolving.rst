.. _uvs-scripting-gripsolving--grip-fitting-and-steering-ownership:

Grip fitting and steering ownership
===================================

Grip fitting turns a control's surface description into a plausible hand pose for a particular character. It uses palm frames, measured finger geometry and anatomical bounds. Steering adds another problem: the hands may need to release and reposition while the column rotates through more than one revolution.

Keep geometry fitting and hand ownership separate. A fit answers where fingers can close around a surface. A reservation answers which system is allowed to use a hand while steering, operating a switch or performing another task.

.. _uvs-scripting-gripsolving--implementation-map:

Implementation map
------------------

+-------------------------------+------------------------------------------------------------------------+
| Class                         | Responsibility                                                         |
+===============================+========================================================================+
| ``HandGrip``                  | Stores character hand frames and fallback finger poses.                |
+-------------------------------+------------------------------------------------------------------------+
| ``AdaptiveHandGrip``          | Binds a character to a surface and applies fitted finger poses.        |
+-------------------------------+------------------------------------------------------------------------+
| ``FingerGripSolver``          | Computes finger fitting against the supplied grip geometry.            |
+-------------------------------+------------------------------------------------------------------------+
| ``HumanoidFingerCalibration`` | Establishes character-specific finger axes and pad geometry.           |
+-------------------------------+------------------------------------------------------------------------+
| ``SteeringHandRegrip``        | Coordinates steering contacts, availability and external reservations. |
+-------------------------------+------------------------------------------------------------------------+
| ``SteeringRimGeometry``       | Describes the steering rim used by grip calculations.                  |
+-------------------------------+------------------------------------------------------------------------+

.. _uvs-scripting-gripsolving--geometry-and-binding:

Geometry and binding
--------------------

``HandGrip`` describes a character hand in terms of palm and finger frames. ``AdaptiveHandGrip`` uses those measurements and the selected handle's surface to choose finger poses. The fit answers how a particular hand can close around a particular object; it does not move the object's mesh or change the character's bone lengths.

During binding, the solver calibrates/reuses character geometry and prepares the contact fit. During presentation it applies that fit and permitted gestures. Saved finger angles and pressure-pose selection describe the hand's current presentation; measurements such as pad radius and maximum flexion describe the character. Keep those two categories separate when authoring a new rig.

To replace finger posing without replacing seats, implement ``IPassengerHandPose``. Preserve ``TryApplyPose(bool gripping)``, ``Release()`` and ``Unbind()`` semantics: applying a grip, relaxing the current hand and ending the association are different lifecycle operations. A driver that only writes bones but never releases its binding can keep fighting animation after seat exit.

Fit quality depends on calibration before it depends on iteration count. Check the open/reference rotations, flexion axes and pad sizes for the actual character. A solver constrained to incorrect axes can only choose among incorrect poses; increasing iterations makes that error more expensive rather than correcting it.

A binding associates one character with one control geometry. Reuse the fitted coordinates during ordinary motion. Refit or rebind when the underlying dimensions change, such as replacing a wheel rim with a differently sized control. ``AdaptiveHandGrip.MaximumPenetration`` and ``MeanContactGap`` can help distinguish intrusion from fingers that remain visibly separated.

.. _uvs-scripting-gripsolving--steering-angle-mapping:

Steering angle mapping
----------------------

Road-wheel angle and steering-column angle are different units of the steering mechanism even though both are expressed in degrees. A small tire angle may correspond to several turns of the column. Use the vehicle's conversion methods when integrating a wheel device or custom column presentation, and keep mesh-axis inversion outside the logical steering angle.

An unwrapped angle preserves direction and accumulated rotation across full turns. Reducing it to a 0–360° display value before regrip planning loses information about which way the column travelled.

Vehicle ``Settings`` separates road-wheel ``steeringAngle`` from ``steeringWheelRotationAtFullLock`` (column degrees per side). ``SteeringRatio`` and conversion actions map actuator, input and column angles. Mesh inversion/axis orientation are presentation details. An unwrapped column angle can exceed a full revolution.

.. _uvs-scripting-gripsolving--supported-hands-and-reservations:

Supported hands and reservations
--------------------------------

``SteeringHandRegrip`` coordinates which hand can support or reposition on a rotating control. It needs both surface geometry and ownership state. A hand can be physically attached yet unavailable to an application task because another task owns it; conversely an available hand may currently be released.

``IsHandAvailable``, ``IsHandOnWheel`` and ``HandOwner`` expose those distinct questions. Reserve through ``TryReserveHand(left, owner, palmTarget)`` before moving a steering hand for a separate task. An optional target gives the reservation a replacement palm frame; a ``null`` target reserves availability without adding that external drive.

Release through ``ReleaseHand`` using the same owner. Keep the owner alive for the task's lifetime and clean up on disable. Do not claim a reservation by editing the handle's per-hand contact values: those values describe contact presentation, while the reservation is the arbitration boundary.

Regrip planning distinguishes wheel-material and column-support contacts. Contact force remains physical; a reachable plan is not a zero-slip guarantee under arbitrary forces. **Allow Hand Regrip** and **Vary Grip With Steering** independently control repositioning and finger/pressure gestures.

Availability and attachment are distinct. An available hand can be released; an attached hand can be reserved by another owner. ``TryReserveHand`` accepts a live ``UnityEngine.Object`` and optional external palm frame. Only the same owner can update/release it. Destroyed owners return availability; destroying only the target leaves the reservation but removes its drives.

.. _uvs-scripting-gripsolving--reserve-one-hand-for-an-application-task:

Reserve one hand for an application task
----------------------------------------

The reservation owner is the component that must eventually release it. Using ``this`` makes lifetime explicit and lets the steering system recognize the same owner on subsequent requests. The boolean argument selects the hand; ``false`` in this example means the right hand.

A failed reservation means another owner or the current state prevents the task. The application should postpone or cancel its gesture rather than moving the hand anyway. On completion or disable, release through the same owner. A stable optional target lets the steering system follow the external palm frame while preserving ownership rules.

Assign the vehicle's ``SteeringHandRegrip`` and a stable target under the same vehicle. Call ``Begin``/``End`` for the task; the owner releases its reservation on disable.

**Example:** ``ReservedHandTask.cs``

.. raw:: html

   <!-- example: ReservedHandTask.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ReservedHandTask : MonoBehaviour
       {
           public SteeringHandRegrip steering;
           public Transform palmTarget;

           public bool Begin()
               => steering && steering.TryReserveHand(false, this, palmTarget);

           public void End()
           {
               if (steering) steering.ReleaseHand(false, this);
           }

           private void OnDisable() => End();
       }
   }

The external target is a palm contact frame. Use a ``VehicleHandle`` for a reusable scene control, or ``ControlInteraction``/``vehicle.handles`` for committed out-and-back actions. Do not make several systems independently restore the same hand binding.

.. _uvs-scripting-gripsolving--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed grip fitting and steering ownership API </API/GripSolving>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-gripsolving--adaptivehandgrip:

AdaptiveHandGrip
~~~~~~~~~~~~~~~~

:ref:`AdaptiveHandGrip <uvs-api-gripsolving--adaptivehandgrip>` gives the full declared contract.

+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                            | Role                                                                                                                          |
+===================================================================================+===============================================================================================================================+
| ``public virtual void Bind(VehicleHandle surface, Animator animator, bool left)`` | Binds this character hand to a ``VehicleHandle`` surface, calibrates the selected side and prepares adaptive surface fitting. |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Unbind()``                                                  | Releases the current source/hand association and its owned state.                                                             |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ApplyGrip()``                                               | Applies the currently prepared adaptive grip to the mapped hand.                                                              |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Calibrate(Animator animator)``                              | Builds hand measurements/reference frames from the supplied character Animator.                                               |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryApplyPose(bool gripping)``                               | Applies the prepared gripping/released hand pose when this hand-pose provider can supply it.                                  |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Release()``                                                 | Releases this part or hand pose through its declaring type's ownership boundary.                                              |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-gripsolving--handgrip:

HandGrip
~~~~~~~~

:ref:`HandGrip <uvs-api-gripsolving--handgrip>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Method                                                                                                                                                  | Role                                                                              |
+=========================================================================================================================================================+===================================================================================+
| ``public virtual void ApplyPose(bool gripping)``                                                                                                        | Applies the configured character hand pose without creating a new seat occupancy. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual void ConfigureJoint(ConfigurableJoint joint, Rigidbody vehicle, VehicleHandle handle)``                                                | Configures a physical hand joint using the prepared grip frame and drive policy.  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual Quaternion WristRotation(Transform target)``                                                                                           | Returns wrist orientation from the prepared hand/contact frame.                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual Vector3 WristPosition(Transform target)``                                                                                              | Returns the wrist position corresponding to a prepared palm/contact frame.        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual void DriveRotation(ConfigurableJoint joint, Rigidbody vehicle, Transform target, VehicleHandle handle, bool left, float contact = 1)`` | Applies the physical wrist rotational drive in the prepared hand/contact frame.   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. _uvs-scripting-gripsolving--ihandavailabilitysource:

IHandAvailabilitySource
~~~~~~~~~~~~~~~~~~~~~~~

:ref:`IHandAvailabilitySource <uvs-api-gripsolving--ihandavailabilitysource>` gives the full declared contract.

-  ``bool CanUseHand(PassengerSeat seat, PassengerBodyPart hand)`` — Reports whether the requested seat and hand are available for an interaction.

.. _uvs-scripting-gripsolving--ipassengerhandpose:

IPassengerHandPose
~~~~~~~~~~~~~~~~~~

:ref:`IPassengerHandPose <uvs-api-gripsolving--ipassengerhandpose>` gives the full declared contract.

+--------------------------------------+----------------------------------------------------------------------------------------------+
| Method                               | Role                                                                                         |
+======================================+==============================================================================================+
| ``bool TryApplyPose(bool gripping)`` | Applies the prepared gripping/released hand pose when this hand-pose provider can supply it. |
+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``void Release()``                   | Releases this part or hand pose through its declaring type's ownership boundary.             |
+--------------------------------------+----------------------------------------------------------------------------------------------+
| ``void Unbind()``                    | Releases the current source/hand association and its owned state.                            |
+--------------------------------------+----------------------------------------------------------------------------------------------+

.. _uvs-scripting-gripsolving--ivehiclemodule:

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

.. _uvs-scripting-gripsolving--passengerbehaviour:

PassengerBehaviour
~~~~~~~~~~~~~~~~~~

:ref:`PassengerBehaviour <uvs-api-passengercontrollers--passengerbehaviour>` gives the full declared contract.

+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Method                                                                          | Role                                                                          |
+=================================================================================+===============================================================================+
| ``public sealed override void StepPassenger(Passengers core, float deltaTime)`` | Advances passenger work in the supplied seat/core context.                    |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public virtual bool AppliesTo(VehicleController vehicle)``                    | Checks whether this passenger behavior should run for the supplied seat/role. |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. _uvs-scripting-gripsolving--passengermodule:

PassengerModule
~~~~~~~~~~~~~~~

:ref:`PassengerModule <uvs-api-passengercontrollers--passengermodule>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                            | Role                                                                                                                                              |
+===================================================================================================+===================================================================================================================================================+
| ``public sealed override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Intentionally empty sealed module-pipeline entry point. Passenger-local work runs through ``StepPassenger``/``RenderPassenger`` under Passengers. |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreparePassenger(Passengers core, PassengerSeat seat)``                     | Prepares this passenger behavior for an occupied seat.                                                                                            |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetPassenger(Passengers core)``                                           | Resets this passenger behavior's state for the supplied seat.                                                                                     |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RenderPassenger(Passengers core)``                                          | Advances render-time passenger presentation owned by this behavior/core.                                                                          |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                           | Advances passenger work in the supplied seat/core context.                                                                                        |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-gripsolving--steeringhandregrip:

SteeringHandRegrip
~~~~~~~~~~~~~~~~~~

:ref:`SteeringHandRegrip <uvs-api-gripsolving--steeringhandregrip>` gives the full declared contract.

-  ``public virtual bool CanUseHand(PassengerSeat requestedSeat, PassengerBodyPart hand)`` — Reports whether the requested seat and hand are available for an interaction.
-  ``public virtual Transform ColumnSupport(bool left)`` — Current column support.
-  ``public virtual Object HandOwner(bool left)`` — Current hand owner.
-  ``public virtual bool IsFirmlySupported(bool left)`` — Current is firmly supported.
-  ``public virtual bool IsHandAvailable(bool left)`` — Current is hand available.
-  ``public virtual bool IsHandOnWheel(bool left)`` — // Reports whether the hand currently belongs to the wheel rather than an external reservation or transfer.
-  ``public virtual float MaterialAngle(bool left)`` — // Returns the hand's unwrapped position on the rotating wheel material rather than a static world angle.
-  ``public override void PreparePassenger(Passengers core, PassengerSeat passengerSeat)`` — Current prepare passenger.
-  ``public virtual void PreparePose()`` — Current prepare pose.
-  ``public virtual bool ReleaseHand(bool left, Object owner)`` — // Only the reserving owner can return the hand to steering.
-  ``public virtual bool ReleaseSteeringHand(bool left)`` — Current release steering hand.
-  ``public override void RenderPassenger(Passengers core)`` — Current render passenger.
-  ``public override void ResetPassenger(Passengers core)`` — Current reset passenger.
-  ``public virtual bool TakeSteeringHand(bool left)`` — // Reattaches an available hand at its current nearest rim point; capture stays compliant.
-  ``public virtual bool TryReserveHand(bool left, Object owner, Transform palmTarget = null)`` — // Exclusively reserves a hand for another system. A null target releases its drives.
-  ``public virtual bool TrySetLeadingHand(bool left)`` — Current try set leading hand.

.. _uvs-scripting-gripsolving--vehiclemodule:

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
