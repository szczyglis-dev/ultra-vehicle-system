.. _uvs-api-anatomy--anatomical-references-api:

Anatomical references API
=========================

Read :doc:`the system explanation </Scripting/Anatomy>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

The editor authoring entry point is ``HumanoidAnatomyAuthoring.Configure(HumanoidPassenger passenger)``. It belongs to editor rig preparation and can overwrite saved native joint tuning. It is separate from the runtime data contract below; keep calls in an editor assembly.

.. _uvs-api-anatomy--types:

Types
-----

-  :ref:`HumanoidJointDefinition <uvs-api-anatomy--humanoidjointdefinition>`

.. _uvs-api-anatomy--humanoidjointdefinition:

HumanoidJointDefinition
-----------------------

**Runtime/World/Passengers/Physics/HumanoidJointLimits.cs**

Saved native joint reference with neutral-frame/flexion metadata used by passenger physics and IK.

.. _uvs-api-anatomy--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                           | Meaning                                                                                                                                                                                  |
+==================================================+==========================================================================================================================================================================================+
| ``public Vector3 anchor``                        | Runtime copy of the native joint anchor in the joint body's local frame.                                                                                                                 |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 axis``                          | Runtime copy of the native primary joint axis.                                                                                                                                           |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Rigidbody body``                        | Runtime-captured ``Rigidbody`` on joint, refreshed when native anatomical settings are read; not a visual body transform.                                                                |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 connectedAnchor``               | Runtime copy of the connected anchor in the connected body's frame.                                                                                                                      |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Rigidbody connectedBody``               | Runtime-captured connected ``Rigidbody`` from ``joint.connectedBody``.                                                                                                                   |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Quaternion connectedReferenceRotation`` | Reference connected body rotation relative to the passenger root.                                                                                                                        |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float highX``                           | Runtime copy of the native high angular-X limit in degrees.                                                                                                                              |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public ConfigurableJoint joint``               | Saved ``ConfigurableJoint`` supplying native axes, anchors, connections and angular limits.                                                                                              |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string jointId``                        | Unique, case-sensitive editable ID. Authoring generates parent-bone-to-child-bone names and preserves existing IDs on rebuild. Empty/duplicate IDs cannot be resolved by runtime lookup. |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lowX``                            | Runtime copy of the native low angular-X limit in degrees.                                                                                                                               |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float referenceFlexion``                | Neutral bend angle in degrees, used by the IK hinge solver.                                                                                                                              |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Quaternion referenceRotation``          | Reference body rotation relative to the passenger root.                                                                                                                                  |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 secondaryAxis``                 | Runtime copy of the native secondary joint axis.                                                                                                                                         |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float y``                               | Runtime angular-Y range in degrees; locked Y is represented as zero.                                                                                                                     |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float z``                               | Runtime angular-Z range in degrees; locked Z is represented as zero.                                                                                                                     |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
