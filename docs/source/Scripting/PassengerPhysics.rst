.. _uvs-scripting-passengerphysics--physical-passengers-and-restraints:

Physical passengers and restraints
==================================

A physical passenger is a connected rigidbody skeleton supported by the vehicle at selected contact points. The anatomical joints constrain how bones can move relative to each other. Seat restraints support the pelvis and chest, while hand and foot bindings connect selected limbs to controls or rests.

These layers solve different problems. The skeleton provides anatomy; the harness provides vehicle-relative support; a handle provides a contact frame; collision policy decides which contacts may occur. Tune them separately so a stiff hand target is not used to hide a misplaced seat or an invalid joint axis.

.. _uvs-scripting-passengerphysics--implementation-map:

Implementation map
------------------

+----------------------------------+------------------------------------------------------------------------+
| Class                            | Responsibility                                                         |
+==================================+========================================================================+
| ``PassengerPhysics``             | Coordinates physical passenger pose/support behavior.                  |
+----------------------------------+------------------------------------------------------------------------+
| ``PassengerRestraints``          | Stores harness, release, damping and ejection configuration.           |
+----------------------------------+------------------------------------------------------------------------+
| ``PassengerSeatConstraints``     | Builds and updates vehicle-relative support constraints.               |
+----------------------------------+------------------------------------------------------------------------+
| ``PassengerCollisionExclusions`` | Tracks the passenger collision-exclusion policy.                       |
+----------------------------------+------------------------------------------------------------------------+
| ``PassengerFreeRagdoll``         | Handles released-body physics and restoration boundaries.              |
+----------------------------------+------------------------------------------------------------------------+
| ``PassengerBodyPartConfig``      | Describes each limb's mode, target and support choices.                |
+----------------------------------+------------------------------------------------------------------------+
| ``HumanoidPassenger``            | Connects the authored character bodies and runtime passenger behavior. |
+----------------------------------+------------------------------------------------------------------------+

.. _uvs-scripting-passengerphysics--initialization-and-update-order:

Initialization and update order
-------------------------------

Prepare the rig before tuning vehicle supports. Check that each intended bone has the correct mass, collider and connection, and that the authored pose is reachable from the seat. Entering the vehicle establishes the seated pose; subsequent physical motion should come from constraints and forces, rather than a separate script teleporting those same bones each frame.

Target timing is part of the integration. A moving joystick or pedal needs to publish its current target before the seat resolves limb support. Keep custom target updates within the relevant ownership/update flow instead of adding an unrelated late writer that causes the hand to chase the previous frame's pose.

Author the humanoid's ``Rigidbody``/``ConfigurableJoint`` skeleton before Play Mode. Saved joints provide axes, connections, anchors and angular bounds. **Configure anatomical joints** is an explicit editor operation that can overwrite tuning.

Seating establishes the pelvis and limb pose, prepares grips, then creates vehicle supports. Interior targets advance in Presentation before ``Passengers`` in ``TireFeedback``. Ordinary physical stepping uses forces/joints rather than positional IK writes. The character Animator is suspended on the physical path and restored on handover.

Physical arms and legs are not driven towards live IK targets. Controlled arm and leg joints use passive damping and anatomical limits, while the seat, palms and feet provide the actual spring attachments. Explicit relaxed-rest hand settings retain their authored weak springs. There are no additional whole-body stabilizing forces, shoulder-to-wheel reach joints, shrinking capture limits or automatic pose resets. Explicit ``ResetSeatedPose`` and vehicle reset calls still reset immediately. See :ref:`seated physics <uvs-seats--seated-recovery-without-pose-resets>`.

.. _uvs-scripting-passengerphysics--pelvischest-support:

Pelvis/chest support
--------------------

A compliant harness allows bounded movement under acceleration and then settles relative to the moving vehicle. ``harnessFrequency`` describes response speed in Hz, while ``harnessDampingRatio`` controls how oscillatory that response is. ``harnessMaximumAcceleration`` limits the support budget so a large pose error cannot request unlimited force.

Tune the neutral seated pose and travel envelope before increasing support. If the pelvis is held in the wrong place, stronger support increases conflict with the skeleton. If the chest envelope is too small for the intended posture, the passenger can look rigid even with otherwise soft springs.

+------------------------------------------------+---------------------------------------------------------------------+
| Group                                          | Role                                                                |
+================================================+=====================================================================+
| ``softHarness``                                | Compliant pelvis and upper-chest support                            |
+------------------------------------------------+---------------------------------------------------------------------+
| ``harnessFrequency`` / ``harnessDampingRatio`` | Mass-scaled support response                                        |
+------------------------------------------------+---------------------------------------------------------------------+
| ``harnessMaximumAcceleration``                 | Finite support-force budget                                         |
+------------------------------------------------+---------------------------------------------------------------------+
| ``seatTravel`` / ``harnessChestTravel``        | Translation envelope when ``limitHarnessTravel`` is enabled         |
+------------------------------------------------+---------------------------------------------------------------------+
| Side/forward/twist limits                      | Seat-aligned angular envelope                                       |
+------------------------------------------------+---------------------------------------------------------------------+
| ``chestSupportStrength``                       | Chest support relative to pelvis                                    |
+------------------------------------------------+---------------------------------------------------------------------+
| Relative damping                               | Bounded velocity-relative settling with the moving vehicle          |
+------------------------------------------------+---------------------------------------------------------------------+
| Solver iterations                              | Minimum seated-bone solver settings; higher authored values survive |
+------------------------------------------------+---------------------------------------------------------------------+

The head/neck are not fixed to the vehicle. Bone constraints retain anatomical limits. Increasing support cannot correct impossible seat geometry or limb reach.

.. _uvs-scripting-passengerphysics--seated-fitting-and-hand-rests:

Seated fitting and hand rests
-----------------------------

A rest and a grip need different behavior. A hand resting beside the driver may need yielding positional support and little rotational authority. A hand operating a control needs an aligned palm/contact frame and a deliberate force limit. Choose the limb mode first, then tune its positional and angular drives independently.

Foot translation and ankle orientation are also separate. A foot can remain pinned to a pedal while its ankle follows a compliant rotational drive. Avoid using the rendered toe as the ankle target; incorrect target frames create apparent leg reach and joint-limit problems that spring tuning cannot solve.

A direct hand rest uses IKHandle, ``Hold``, ``relaxedRest``, no handle and no palm contact. Its positional spring/damper/force cap provide yielding support; ``limitRestTravel`` optionally adds a positional stop. Weak arm springs/damping are separate from wrist support.

Align Rest Rotation adds angular support toward the authored target orientation using ``restRotationSpring``/``restRotationDamper``/``maximumRestRotationTorque``. Position and rotation remain independently tunable. Reapply seated tuning after structural support/pose changes; target rotations and live drive settings can then follow their current binding.

``Free`` mode removes vehicle supports. ``poseFreeArm`` can establish an initial arm pose; afterward native gravity, damping and angular limits own movement. Foot pinning locks target translation; ``alignRotation`` supplies a compliant ankle drive. ``AnimatorIK`` uses the same target frames but not these physical holds.

.. _uvs-scripting-passengerphysics--contact-policy:

Contact policy
--------------

Collision policy decides which colliders may meet while a passenger is supported. The seated body often overlaps the vehicle's seating volume, so suppressing selected self/vehicle contacts prevents support constraints from fighting those overlaps. A released limb may need vehicle contact restored so it can hit the dashboard or door.

The seat holds the policy even while empty. ``SetCollisionExclusions(self, vehicle)`` chooses entry exclusions; ``SetReleaseCollisions(...)`` chooses what becomes permitted on release, globally or for one limb. ``RefreshCollisionSettings()`` reapplies the configured policy to the current occupant. These operations do not create a release or ejection themselves. Per-limb and seat-wide release permissions combine, while native neighboring-joint exclusions remain effective.

Use the public policy operations rather than repeatedly calling ``Physics.IgnoreCollision`` for the same owned pairs from another script. The package tracks changes it owns and must be able to restore them during handover. Unity layer policy and application-owned exclusions can still prevent a contact even after the seat permits it.

.. _uvs-scripting-passengerphysics--configure-contact-release:

Configure contact release
-------------------------

Collision exclusions describe permission, not a release command. The example retains suppressed contacts while seated and permits vehicle contact for the right hand after that limb is released. It does not detach the hand or force an impact. Use the release/damage rules to decide when a limb becomes free.

This distinction lets an application configure policy before an occupant enters. The same policy can then be applied to the next character without searching for its bone colliders in gameplay code.

Assign an occupied physical seat or an empty seat configuration. Call ``Apply`` from your setup UI. This permits the right hand to collide with the vehicle after release while retaining entry exclusions.

**Example:** ``PassengerContactPolicy.cs``

.. raw:: html

   <!-- example: PassengerContactPolicy.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class PassengerContactPolicy : MonoBehaviour
       {
           public PassengerSeat seat;

           public void Apply()
           {
               if (!seat) return;
               seat.SetCollisionExclusions(self: true, vehicle: true);
               seat.SetReleaseCollisions(PassengerBodyPart.RightHand,
                   self: false, vehicle: true);
           }
       }
   }

.. _uvs-scripting-passengerphysics--damage-release-and-ejection:

Damage release and ejection
---------------------------

Evaluate collision thresholds using the documented quantity. Impulse divided by timestep is an average force estimate, so force and relative-speed thresholds provide different filters. A slow heavy squeeze and a fast impact may have different gameplay meaning even if one threshold is similar.

Limb release removes the vehicle support for that limb while preserving its skeletal connection. Ejection hands the whole character to free-ragdoll behavior. Keep respawn and score rules at this whole-character boundary rather than treating a released hand as an exited passenger.

Limb collision release requires configured minimum force and relative speed. Force is copied contact impulse divided by the physics timestep; it is an average contact force, not vehicle mass. The spin option uses sustained gravity-relative tilt rather than yaw rate. Separate enable/force/speed/tilt settings govern whole-passenger ejection, which takes priority over limb-only release.

Released limbs remain connected to the skeleton with angular limits. Release latches until reset/re-entry/restoration; returning upright alone does not regrip. ``RestoreDamageFeedback`` restores the seated supports. Whole-body reset/reseat applies only to the eligible previously released character and does not steal a character in another seat.

.. _uvs-scripting-passengerphysics--free-ragdoll-handover:

Free ragdoll handover
---------------------

A free ragdoll is still an anatomical skeleton, but it no longer has vehicle-relative seat and control supports. Handover releases the harness, hand/foot contact and seated pose drives so the body's native joints and contact response can act freely. It is not equivalent to merely making an Animator invisible.

The transition must restore appropriate body, collision and animation ownership. A custom character controller should wait for its own reattachment boundary before resuming transform animation; enabling animation immediately on a still-dynamic ragdoll would introduce a competing pose owner.

Choose an application lifetime policy for the detached character: leave it in the world, recover it after a delay, replace it with another representation or return it to a pool. Seating/reset APIs can restore an eligible released occupant, but do not decide multiplayer respawn ownership or erase unrelated world characters.

Ejection releases vehicle restraints, finger binding and pose motors, then activates passive skeletal physics. Free-ragdoll damping and solver settings control settling without a stored seated-pose spring. Previously captured collision/Animator/solver settings are restored on appropriate reattachment/handover.

The application owns the detached body lifetime. Use :doc:`passenger controllers </Scripting/PassengerControllers>` for animation/application ownership, :doc:`handles </Scripting/Handles>` for limb bindings, and :doc:`grip solving </Scripting/GripSolving>` for contact geometry.

.. _uvs-scripting-passengerphysics--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed physical passengers and limb configuration API </API/PassengerPhysics>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-passengerphysics--humanoidik:

HumanoidIK
~~~~~~~~~~

:ref:`HumanoidIK <uvs-api-passengerphysics--humanoidik>` gives the full declared contract.

+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Method                                                                                                                        | Role                                                                                                       |
+===============================================================================================================================+============================================================================================================+
| ``public virtual void Solve(PassengerSeat seat)``                                                                             | Solves the mapped humanoid pose for the supplied limb targets/configuration.                               |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void Solve(PassengerSeat seat, bool initializeFreeArms)``                                                    | Solves the mapped humanoid pose for the supplied limb targets/configuration.                               |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveHands(PassengerSeat seat)``                                                                        | Solves the selected hand targets using the character's mapped arm/palm frames.                             |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveHands(PassengerSeat seat, bool initializeFreeArms)``                                               | Solves the selected hand targets using the character's mapped arm/palm frames.                             |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveFootPosition(bool left, Vector3 position, Vector3 bend)``                                          | Solves a leg toward the requested ankle/foot target while respecting its mapped frames.                    |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void CapturePalmFrames()``                                                                                   | Captures the mapped wrist-to-palm frames used by subsequent hand targeting.                                |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void MapAnimator(Animator animator)``                                                                        | Resolves humanoid bone references from the supplied Animator, optionally filling only missing references.  |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void MapAnimator(Animator animator, bool fillMissingOnly)``                                                  | Resolves humanoid bone references from the supplied Animator, optionally filling only missing references.  |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryArmPose(PassengerSeat seat, bool left, out Quaternion upperRotation, out Quaternion lowerRotation)`` | Solves a candidate arm pose for the supplied target; ``false`` leaves the caller responsible for fallback. |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryLegPose(PassengerSeat seat, bool left, out Quaternion upperRotation, out Quaternion lowerRotation)`` | Solves a candidate leg pose for the supplied ankle target.                                                 |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Method / event / callback                                                                          | Role                                                                                                   |
+====================================================================================================+========================================================================================================+
| ``public virtual void SolveHands(PassengerSeat seat, bool initializeFreeArms, HandleLimbs limbs)`` | See :ref:`HumanoidIK <uvs-api-passengerphysics--humanoidik>` for the declared lifecycle and arguments. |
+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public virtual void Solve(PassengerSeat seat, bool initializeFreeArms, HandleLimbs limbs)``      | See :ref:`HumanoidIK <uvs-api-passengerphysics--humanoidik>` for the declared lifecycle and arguments. |
+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengerphysics--passengerbodypartconfig:

PassengerBodyPartConfig
~~~~~~~~~~~~~~~~~~~~~~~

:ref:`PassengerBodyPartConfig <uvs-api-passengerphysics--passengerbodypartconfig>` gives the full declared contract.

+--------------------------------------------------------------------+----------------------------------------------------------------------------+
| Method                                                             | Role                                                                       |
+====================================================================+============================================================================+
| ``public virtual Transform ResolveTarget(PassengerBodyPart part)`` | Resolves this limb configuration's effective direct/handle contact target. |
+--------------------------------------------------------------------+----------------------------------------------------------------------------+

.. _uvs-scripting-passengerphysics--passengerfootconfig:

PassengerFootConfig
~~~~~~~~~~~~~~~~~~~

:ref:`PassengerFootConfig <uvs-api-passengerphysics--passengerfootconfig>` gives the full declared contract.

+---------------------------------------------+---------------------------------------------------------------------+
| Method                                      | Role                                                                |
+=============================================+=====================================================================+
| ``public void PinTo(VehicleHandle target)`` | Assigns an ankle target/handle and the foot's hold/rotation policy. |
+---------------------------------------------+---------------------------------------------------------------------+
| ``public void PinTo(Transform target)``     | Assigns an ankle target/handle and the foot's hold/rotation policy. |
+---------------------------------------------+---------------------------------------------------------------------+
| ``public void ReleasePin()``                | Removes the foot's pinned target/hold policy.                       |
+---------------------------------------------+---------------------------------------------------------------------+
