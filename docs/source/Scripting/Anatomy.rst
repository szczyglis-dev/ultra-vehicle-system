.. _uvs-scripting-anatomy--joint-and-ik-frames:

Joint and IK frames
===================

Anatomy defines the coordinate frames and motion limits that make a humanoid rig usable by passenger physics and IK. The runtime needs to know not just where a bone is, but which axis bends it, how it connects to its parent and what motion is physically or anatomically permitted.

The workflow has two stages: author and save native joints for the character, then use that character from seats and handles. A vehicle seat changes posture and support; it does not replace the character's anatomical setup.

.. _uvs-scripting-anatomy--implementation-map:

Implementation map
------------------

+-------------------------------+----------------------------------------------------------------------------------------+
| Class                         | Responsibility                                                                         |
+===============================+========================================================================================+
| ``HumanoidJointLimits``       | Contains ``HumanoidJointDefinition`` metadata and internal native frame/limit helpers. |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidAnatomyAuthoring``  | Editor utility that configures the mapped rig's native joints.                         |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidAnatomyPresets``    | Supplies authoring presets used while preparing a rig.                                 |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidIK``                | Uses character frames to resolve limb targets.                                         |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidFingerCalibration`` | Prepares finger-frame and geometry information for grip fitting.                       |
+-------------------------------+----------------------------------------------------------------------------------------+

.. _uvs-scripting-anatomy--authoring-versus-runtime:

Authoring versus runtime
------------------------

For each physical link, verify the intended parent body and joint frame in the character's neutral pose. A correct transform hierarchy alone does not guarantee that the native joint's axis corresponds to anatomical flexion. Errors here appear later as a knee bending sideways or a wrist resisting a reachable handle.

Keep the saved character prefab as the source of anatomical tuning. This makes the same body usable in several vehicles without copying a different skeleton configuration into each seat. Seat-specific support belongs on the vehicle; body proportions, bone colliders and skeletal connections belong on the character.

``HumanoidAnatomyAuthoring`` / ``HumanoidAnatomyPresets`` are editor authoring utilities. They prepare ``ConfigurableJoint`` components and ``HumanoidJointDefinition`` references from the mapped rig. Avatar reference rotations support Humanoid characters; manually mapped rigs need an appropriate neutral pose.

Runtime reads the saved native joint axes, anchors, connections and angular limits. Definition reference rotations/flexion support IK frame conversion. Seats and handles own vehicle support, not a separate per-seat anatomical skeleton.

.. _uvs-scripting-anatomy--tuning-authority:

Tuning authority
----------------

``HumanoidJointDefinition`` stores a reference to the actual ``ConfigurableJoint`` plus the reference rotations/flexion needed by runtime conversion. It is not a second independent set of native angular limits competing with that joint. The runtime reads the saved joint's frame and bounds before using them for physical/IK work.

The editor authoring utilities build a useful starting skeleton from the mapped rig and selected preset. After that, inspect and tune the real joint components on the character prefab. Re-running authoring is an explicit replacement of those authored values, so use it as a rig-preparation operation rather than a runtime seat adjustment.

For a new humanoid variant, validate pelvis orientation, limb lengths, joint axes and collision geometry before preparing grips. Then check the character in more than one seat. A rig that works only because one seat places its targets on an unusual compensating offset is difficult to reuse.

Use a simple validation progression: inspect the neutral pose, move one joint through its intended range, then check a seated pose and finally a moving physical vehicle. Diagnose the frame before widening limits. A very wide limit can hide a rotated axis during setup but produces implausible motion when the body is released.

When creating a rig variant, preserve the relation between reference rotations, collider dimensions and bone proportions. Finger pad dimensions and flexion axes need the same attention as the large limbs because grip fitting measures that geometry rather than guessing a pose from bone names.

Tune actual ``ConfigurableJoint`` components after authoring. Running **Configure anatomical joints** again replaces values with the selected authoring preset. Do not leave a second competing ``CharacterJoint`` on the same physical link.

Locked angular axes and limited axes have distinct semantics. A numerical angle range is not an independent Cartesian Euler box; it is interpreted in the joint's configured native frame. Finger fitting additionally uses calibrated phalanx axes and pad geometry.

.. _uvs-scripting-anatomy--inspect-saved-native-joint-connections:

Inspect saved native joint connections
--------------------------------------

A useful first diagnostic for a character prefab is to find joints that are not connected to another body. A world-connected joint may be intentional, but it deserves inspection before using the rig as a freely moving passenger. The component below only reports configuration; it does not author or overwrite the skeleton.

**Example:** ``PassengerJointInfo.cs``

.. raw:: html

   <!-- example: PassengerJointInfo.cs -->

.. code-block:: csharp

   using UnityEngine;

   namespace VehicleDocumentationExamples
   {
       public class PassengerJointInfo : MonoBehaviour
       {
           public Transform characterRoot;

           public void InspectConnections()
           {
               if (!characterRoot) return;
               foreach (var joint in characterRoot.GetComponentsInChildren<ConfigurableJoint>(true))
               {
                   if (!joint.connectedBody)
                       Debug.LogWarning($"Inspect world-connected joint: {joint.name}", joint);
               }
           }
       }
   }

Run this on the authored character hierarchy before seating creates temporary vehicle supports. A connected body is only one check: still inspect axes, anchors and limits visually. Automatically assigning the parent rigidbody would hide unusual but deliberate rig layouts and is therefore not part of this diagnostic.

.. _uvs-scripting-anatomy--dynamic-and-animation-paths:

Dynamic and animation paths
---------------------------

The physical and animation paths can use the same contact targets while applying them differently. In physical seating, targets guide forces and constraints. In ``AnimatorIK``, animation remains the base pose and selected limbs receive IK overlays. A target that looks plausible in one path still needs validation in the other, especially near reach limits.

For a custom character, decide which path owns the pose before integrating it. Do not allow animation and native dynamic bodies to independently assign the same bone transforms. Use the controller handover boundary when switching between those owners.

A different rig requires validating proportions, collision proxies, mass distribution and reachable contacts. Large support forces do not correct bad frames. See :doc:`passenger physics </Scripting/PassengerPhysics>`, :doc:`controller ownership </Scripting/PassengerControllers>` and :doc:`grip fitting </Scripting/GripSolving>`.

.. _uvs-scripting-anatomy--modify-a-joint-by-id:

Modify a joint by ID
--------------------

Joint IDs belong to each HumanoidPassenger.anatomicalJoints entry. They are unique within that passenger, case-sensitive and editable through jointId. The authoring tool derives defaults from parent-to-child bone connections and preserves existing IDs. For an existing rig, use **Assign missing joint IDs** in its Inspector without resetting native tuning.

.. raw:: html

   <!-- example: NamedAnatomicalJoint.cs -->

.. code-block:: csharp

   using UltraVehicleSystem;
   using UnityEngine;

   public sealed class NamedAnatomicalJoint : MonoBehaviour
   {
       public HumanoidPassenger passenger;
       public string jointId = "LeftForearmToLeftHand";
       [Range(0, 90)] public float sidewaysLimit = 15;

       public bool ApplyLimit()
       {
           return passenger && passenger.UpdateAnatomicalJoint(jointId, joint => {
               var limit = joint.angularYLimit;
               limit.limit = sidewaysLimit;
               joint.angularYMotion = ConfigurableJointMotion.Limited;
               joint.angularYLimit = limit;
           });
       }

       public ConfigurableJoint FindJoint() => passenger ? passenger.GetAnatomicalJoint(jointId) : null;
   }

GetAnatomicalJoint returns null for an unresolved ID. TryGetAnatomicalJoint returns false and a null output; TryGetAnatomicalJointDefinition does the same for the saved metadata entry. Empty/whitespace IDs, duplicate IDs and destroyed references fail safely. ID changes take effect immediately; no cache rebuild is needed. Lookups do not allocate.

UpdateAnatomicalJoint returns false without calling the callback for an unresolved ID or null callback. On success it refreshes native anchors, axes and limits in that entry's cached anatomy data, including the limits read by IK. If the callback throws, its exception propagates after the cache refresh; there is no rollback. A capturing lambda may allocate, so cache the callback when using it repeatedly in a hot loop. If you mutate a retrieved joint directly, call ReadAnatomicalJointSettings afterward to refresh the anatomy cache.

Use runtime updates for tuning existing joints. Changing connections, replacing components or redefining reference axes while occupied requires coordinating the rig's physics/IK ownership; ID lookup does not rebuild seated restraints or cached drive frames. Passenger state transitions may reapply their motor/damping settings. Runtime edits affect the live instance and do not save prefab overrides automatically.

.. _uvs-scripting-anatomy--editor-authoring:

Editor authoring
----------------

``HumanoidJointDefinition`` is a data contract with no public methods or events. Its complete fields are listed in :doc:`Anatomical references API </API/Anatomy>`.

+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                              | Role                                                                                                                                                                               |
+=====================================================================+====================================================================================================================================================================================+
| ``HumanoidAnatomyAuthoring.Configure(HumanoidPassenger passenger)`` | Editor-only authoring operation that configures the mapped character's anatomical native joints. Run it while preparing the character prefab; it can replace tuned joint settings. |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

``HumanoidAnatomyPresets`` and ``HumanoidJointLimits`` are implementation helpers rather than public extension APIs. For runtime character integration, use the public passenger body/controller and hand-pose contracts instead of calling those helpers.

.. _uvs-scripting-anatomy--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed anatomical references API </API/Anatomy>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.
