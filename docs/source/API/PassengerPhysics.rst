.. _uvs-api-passengerphysics--physical-passengers-and-limb-configuration-api:

Physical passengers and limb configuration API
==============================================

Read :doc:`the system explanation </Scripting/PassengerPhysics>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _uvs-api-passengerphysics--types:

Types
-----

-  :ref:`HumanoidIK <uvs-api-passengerphysics--humanoidik>`
-  :ref:`PassengerBodyPart <uvs-api-passengerphysics--passengerbodypart>`
-  :ref:`PassengerBodyPartConfig <uvs-api-passengerphysics--passengerbodypartconfig>`
-  :ref:`PassengerBodyPartMode <uvs-api-passengerphysics--passengerbodypartmode>`
-  :ref:`PassengerCollisionSurface <uvs-api-passengerphysics--passengercollisionsurface>`
-  :ref:`PassengerFootConfig <uvs-api-passengerphysics--passengerfootconfig>`
-  :ref:`PassengerGForceLimits <uvs-api-passengerphysics--passengergforcelimits>`
-  :ref:`PassengerHandConfig <uvs-api-passengerphysics--passengerhandconfig>`
-  :ref:`PassengerLimbDamageFeedback <uvs-api-passengerphysics--passengerlimbdamagefeedback>`
-  :ref:`PassengerRestraints <uvs-api-passengerphysics--passengerrestraints>`
-  :ref:`RagdollCollisionHelper <uvs-api-passengerphysics--ragdollcollisionhelper>`
-  :ref:`RagdollCollisionRelay <uvs-api-passengerphysics--ragdollcollisionrelay>`

.. _uvs-api-passengerphysics--humanoidik:

HumanoidIK
----------

**Runtime/World/Passengers/IK/HumanoidIK.cs**

Uses character frames to resolve limb targets.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-passengerphysics--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                                                                                      |
+=====================================+==============================================================================================================================================================+
| ``public Transform leftElbowHint``  | Assign the left elbow hint reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftFoot``       | Left-foot bone/contact configuration used by the character or seat.                                                                                          |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftHand``       | Left-hand bone/contact configuration used by the character or handle.                                                                                        |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftLowerArm``   | Assign the left lower arm reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.   |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftLowerLeg``   | Assign the left lower leg reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.   |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftUpperArm``   | Assign the left upper arm reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.   |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftUpperLeg``   | Assign the left upper leg reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.   |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool matchTargetRotation`` | Aligns solved limb end orientation with the assigned target where the IK path supports it.                                                                   |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumForearmRoll`` | Forearm roll for standalone IK without passenger anatomy. Passenger rigs use the saved elbow twist range instead.                                            |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightElbowHint`` | Assign the right elbow hint reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightFoot``      | Right-foot bone/contact configuration used by the character or seat.                                                                                         |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightHand``      | Right-hand bone/contact configuration used by the character or handle.                                                                                       |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightLowerArm``  | Assign the right lower arm reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightLowerLeg``  | Assign the right lower leg reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightUpperArm``  | Assign the right upper arm reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightUpperLeg``  | Assign the right upper leg reference used by HumanoidIK. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--methods:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                     | Role and behavior                                                                                          | Arguments and result                                                                                                                                                                                                                                                                                                                                                                                                                           |
+===============================================================================================================================+============================================================================================================+================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public virtual void CapturePalmFrames()``                                                                                   | Captures the mapped wrist-to-palm frames used by subsequent hand targeting.                                | No arguments; no returned value.                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void MapAnimator(Animator animator)``                                                                        | Resolves humanoid bone references from the supplied Animator, optionally filling only missing references.  | ``animator`` — Character Animator providing mapped bones/animation context.                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void MapAnimator(Animator animator, bool fillMissingOnly)``                                                  | Resolves humanoid bone references from the supplied Animator, optionally filling only missing references.  | ``animator`` — Character Animator providing mapped bones/animation context. ``fillMissingOnly`` — Preserve existing mapped references and fill only missing ones.                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Solve(PassengerSeat seat)``                                                                             | Solves the mapped humanoid pose for the supplied limb targets/configuration.                               | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Solve(PassengerSeat seat, bool initializeFreeArms)``                                                    | Solves the mapped humanoid pose for the supplied limb targets/configuration.                               | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``initializeFreeArms`` — Whether to establish an initial pose for otherwise free arms.                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Solve(PassengerSeat seat, bool initializeFreeArms, HandleLimbs limbs)``                                 | Solves only the selected limb chains, leaving the other chains unchanged.                                  | ``limbs`` is a mask of hands/feet to solve.                                                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveHands(PassengerSeat seat, bool initializeFreeArms, HandleLimbs limbs)``                            | Solves only selected hands, including their configured rest/free initialization policy.                    | Feet and unselected hands are untouched.                                                                                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveFootPosition(bool left, Vector3 position, Vector3 bend)``                                          | Solves a leg toward the requested ankle/foot target while respecting its mapped frames.                    | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``position`` — Requested point or switch detent; see its declared type and owning operation. ``bend`` — Bend, interpreted by this operation in the declared type.                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveHands(PassengerSeat seat)``                                                                        | Solves the selected hand targets using the character's mapped arm/palm frames.                             | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveHands(PassengerSeat seat, bool initializeFreeArms)``                                               | Solves the selected hand targets using the character's mapped arm/palm frames.                             | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``initializeFreeArms`` — Whether to establish an initial pose for otherwise free arms.                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryArmPose(PassengerSeat seat, bool left, out Quaternion upperRotation, out Quaternion lowerRotation)`` | Solves a candidate arm pose for the supplied target; ``false`` leaves the caller responsible for fallback. | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``upperRotation`` — Upper rotation, interpreted by this operation in the declared type. ``lowerRotation`` — Lower rotation, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryLegPose(PassengerSeat seat, bool left, out Quaternion upperRotation, out Quaternion lowerRotation)`` | Solves a candidate leg pose for the supplied ankle target.                                                 | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``upperRotation`` — Upper rotation, interpreted by this operation in the declared type. ``lowerRotation`` — Lower rotation, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--passengerbodypart:

PassengerBodyPart
-----------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Defines the allowed passenger body part choices used by this topic.

.. _uvs-api-passengerphysics--values:

Values
~~~~~~

-  ``LeftHand``
-  ``RightHand``
-  ``LeftFoot``
-  ``RightFoot``

.. _uvs-api-passengerphysics--passengerbodypartconfig:

PassengerBodyPartConfig
-----------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Describes each limb's mode, target and support choices.

.. _uvs-api-passengerphysics--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                  | Meaning                                                                                                                                                           |
+=========================================================+===================================================================================================================================================================+
| ``public Transform anchor``                             | Assign the anchor reference used by PassengerBodyPartConfig. Leave unassigned only when this feature is optional or the component can resolve it automatically.   |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBodyPartMode EffectiveMode { get; }`` | Read-only/resolved effective mode for ``PassengerBodyPartConfig``.                                                                                                |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableSelfCollidersOnRelease``            | Enable contacts between this Free limb and the ragdoll's own body. Neighboring skeletal bodies keep collisions disabled.                                          |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableVehicleCollidersOnRelease``         | Enable contacts with the vehicle when this limb enters Free. The seat-wide setting also enables this for released limbs.                                          |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleHandle handle``                         | Assign the handle VehicleHandle component/asset used by PassengerBodyPartConfig.                                                                                  |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsIKForced { get; }``                     | Whether the assigned IK/Animator + IK handle or an active temporary request enables IK for this limb. Damage release and explicit Free ownership take precedence. |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsControlled { get; }``                   | Whether this body part uses an IK handle rather than animation or free motion.                                                                                    |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsReleasedByDamage { get; }``             | Current is released by damage predicate; read it instead of maintaining a second application flag.                                                                |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBodyPartMode mode``                   | Selects the operating policy; see the listed options and the owning component guide. Options: ``IKHandle``, ``Animator``, ``Free``.                               |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                          | Role and behavior                                                          | Arguments and result                                                                                                                                                         |
+====================================================================+============================================================================+==============================================================================================================================================================================+
| ``public virtual Transform ResolveTarget(PassengerBodyPart part)`` | Resolves this limb configuration's effective direct/handle contact target. | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Returned ``Transform``; ownership remains as specified by the creating/lookup operation. |
+--------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------+----------------------------------------------------------------------+
| Declaration                                             | Usage                                                                |
+=========================================================+======================================================================+
| ``public PassengerLimbDamageFeedback damageFeedback``   | Independent collision and tilt release policy for this hand or foot. |
+---------------------------------------------------------+----------------------------------------------------------------------+
| ``public PassengerCollisionSurface[] releaseColliders`` | Cabin surfaces admitted only for this limb when it is Free.          |
+---------------------------------------------------------+----------------------------------------------------------------------+

.. _uvs-api-passengerphysics--passengerbodypartmode:

PassengerBodyPartMode
---------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Defines the allowed passenger body part mode choices used by this topic.

.. _uvs-api-passengerphysics--values-1:

Values
~~~~~~

-  ``[InspectorName("IK Handle")] IKHandle = 0``
-  ``Animator = 1``
-  ``Free = 2``

.. _uvs-api-passengerphysics--passengerfootconfig:

PassengerFootConfig
-------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Per-foot mode, target and pinning/rotation configuration used by the seat.

**Inherits / implements:** :ref:`PassengerBodyPartConfig <uvs-api-passengerphysics--passengerbodypartconfig>`.

.. _uvs-api-passengerphysics--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                                                                                                                                                        |
+=============================================+================================================================================================================================================================================================================================================================================+
| ``public bool alignRotation``               | Guide the ankle orientation towards the authored target rotation, including moving pedals. Disabled by default.                                                                                                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float damper``                     | Damping strength opposing motion; larger values reduce oscillation but can slow the response. Initial value: ``70``.                                                                                                                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool hold``                        | Chooses how the limb is supported at its target while the passenger is seated. Initial value: ``true``.                                                                                                                                                                        |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool limitTravel``                 | When checked, limit travel is active; when unchecked the owning system skips that optional policy.                                                                                                                                                                             |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAcceleration``        | Force/torque budget for maximum acceleration; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame.                                                                                                 |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRotationTorque``      | Force/torque budget for maximum rotation torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``25``.                                                                       |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool pinToAnchor``                 | Physically lock the foot position to its resolved anchor while Hold and IK Handle mode are enabled. Requires a physical seated passenger. Overrides spring and travel settings; ankle rotation remains free unless Align Rotation or the handle's foot mode requests rotation. |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rotationDamper``             | Damping for rotation damper. Higher values oppose relative motion more strongly. Initial value: ``12``.                                                                                                                                                                        |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rotationSpring``             | Restoring stiffness for rotation spring. Higher values resist displacement more strongly. Initial value: ``160``.                                                                                                                                                              |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spring``                     | Spring stiffness. Larger values produce a stronger restoring force for the same displacement. Initial value: ``1200``.                                                                                                                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float travel``                     | Maximum positional slack in metres around the pinned foot target when travel limiting is enabled. Initial value: ``.035f``.                                                                                                                                                    |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool UsesTargetRotation { get; }`` | Effective rotation policy: explicit Align Rotation or the assigned handle's rotation requirement.                                                                                                                                                                              |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--methods-2:

Methods
~~~~~~~

+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| Signature                                   | Role and behavior                                                   | Arguments and result                                                      |
+=============================================+=====================================================================+===========================================================================+
| ``public void PinTo(Transform target)``     | Assigns an ankle target/handle and the foot's hold/rotation policy. | ``target`` — Configured target object/point; see declared type and owner. |
+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``public void PinTo(VehicleHandle target)`` | Assigns an ankle target/handle and the foot's hold/rotation policy. | ``target`` — Configured target object/point; see declared type and owner. |
+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``public void ReleasePin()``                | Removes the foot's pinned target/hold policy.                       | No arguments; no returned value.                                          |
+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--passengergforcelimits:

PassengerGForceLimits
---------------------

**Runtime/World/Passengers/Seats/PassengerGForceLimits.cs**

Serialized per-seat emergency settings. All thresholds are live. See :ref:`G-force limits <uvs-seats--g-force-limits>` for activation and cleanup.

.. _uvs-api-passengerphysics--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                       | Meaning                                                                                                                                                                                                                                                                 |
+==============================================+=========================================================================================================================================================================================================================================================================+
| ``public bool enabled``                      | Enable transient protection for an occupied physical ragdoll. Default: true.                                                                                                                                                                                            |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumJointSeparation``      | Maximum anatomical anchor separation while active, metres. Authored angular ranges are retained; soft limit springs are restored after protection. Default: .025; minimum .001.                                                                                         |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRelativeAngularSpeed`` | Maximum bone angular speed and rotation per physics step relative to the moving vehicle, based on the live pre-solve pose, degrees/second. Default: 360; minimum 1.                                                                                                     |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRelativeSpeed``        | Maximum dynamic bone speed relative to the local vehicle point velocity, m/s. Default: 3; minimum .1.                                                                                                                                                                   |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumSeatDisplacement``     | Maximum pelvis displacement from the seated spine origin while active, metres. Default: .15; minimum .01.                                                                                                                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumForce``                | Optional minimum passenger inertial load in N, not vehicle contact force. Zero disables this additional test. Default: 0; minimum 0.                                                                                                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumGForce``               | Minimum gravity-compensated seat acceleration in standard G. Default: 8; minimum 1.                                                                                                                                                                                     |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumVelocityChange``       | Minimum gravity-compensated change of seat velocity per physics step, m/s. Default: 1; minimum 0.                                                                                                                                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool monitorAfterPhysics``          | Observe overloads immediately after every physics solve, including wheel/suspension impulses without a body collision callback. Disable to retain pre-solve and collision-only detection; already active protection is still enforced after physics. Default: ``true``. |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool protectConstraintFailure``     | Independently engage existing containment above twice the relative bone speed limits or 125% of Maximum Seat Displacement, even without a large chassis G spike. Main enabled switch still applies. Default: ``true``.                                                  |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float protectionTime``              | Minimum hold after an overload, at least one physics step; extended until relative bone motion settles. Default: .15; minimum 0.                                                                                                                                        |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--passengerhandconfig:

PassengerHandConfig
-------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Configuration/implementation type for passenger hand config within physical passengers and limb configuration.

**Inherits / implements:** :ref:`PassengerBodyPartConfig <uvs-api-passengerphysics--passengerbodypartconfig>`.

.. _uvs-api-passengerphysics--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                       | Meaning                                                                                                                                                                                                                                                     |
+==============================================+=============================================================================================================================================================================================================================================================+
| ``public bool alignRestRotation``            | Let the physical resting wrist follow its anchor rotation with a bounded angular spring. Uses the calibrated palm frame when a ``HandGrip`` is present, otherwise the wrist frame. Reapply seated tuning after enabling; anchor rotation then updates live. |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool animateThumb``                 | Allow grip solvers to pose the thumb. Disable to keep its authored local pose across handle changes.                                                                                                                                                        |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float damper``                      | Damping strength opposing motion; larger values reduce oscillation but can slow the response. Initial value: ``180``.                                                                                                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeArmDamper``               | Damping for free arm damper. Higher values oppose relative motion more strongly. Initial value: ``3``.                                                                                                                                                      |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeArmMaximumDampingTorque`` | Force/torque budget for free arm maximum damping torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``15``.                                            |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 freeWristRotation``         | Reference wrist Euler rotation in degrees for the optional initialized free-arm pose.                                                                                                                                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool hold``                         | Chooses how the limb is supported at its target while the passenger is seated. Initial value: ``true``.                                                                                                                                                     |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool limitRestTravel``              | Bound wrist distance from the rest anchor using a native joint limit. Disable for force-limited spring support only, allowing the hand to yield under larger loads. Reapply seated tuning after editing.                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRestForce``            | Force/torque budget for maximum rest force; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``80``.                                                         |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRestRotationTorque``   | Force/torque budget for maximum rest rotation torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``8``.                                                |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool palmContact``                  | Uses a configured palm contact frame when binding the hand to its control.                                                                                                                                                                                  |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool poseFreeArm``                  | In Free mode, pose this arm toward its direct anchor once on entry, then let it hang. No car-to-hand support or angular position spring is created. Reapply seated tuning to change the initial pose.                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool relaxedRest``                  | Soft support around a direct hand anchor, with weaker arm pose motors and free wrist rotation. Reapply seated tuning after editing. Handles and palm grips retain their own support.                                                                        |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restArmDamper``               | Damping for rest arm damper. Higher values oppose relative motion more strongly. Initial value: ``1.5f``.                                                                                                                                                   |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restArmMaximumTorque``        | Force/torque budget for rest arm maximum torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``15``.                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restArmSpring``               | Restoring stiffness for rest arm spring. Higher values resist displacement more strongly. Initial value: ``6``.                                                                                                                                             |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restDamper``                  | Damping for rest damper. Higher values oppose relative motion more strongly. Initial value: ``24``.                                                                                                                                                         |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restRotationDamper``          | Damping for rest rotation damper. Higher values oppose relative motion more strongly. Initial value: ``2``.                                                                                                                                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restRotationSpring``          | Restoring stiffness for rest rotation spring. Higher values resist displacement more strongly. Initial value: ``12``.                                                                                                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restSpring``                  | Restoring stiffness for rest spring. Higher values resist displacement more strongly. Initial value: ``300``.                                                                                                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restTravel``                  | Rest travel in metres in the owning system's space. Initial value: ``.12f``.                                                                                                                                                                                |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spring``                      | Spring stiffness. Larger values produce a stronger restoring force for the same displacement. Initial value: ``2200``.                                                                                                                                      |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool UsesFreeArmPose { get; }``     | Read-only/resolved uses free arm pose for ``PassengerHandConfig``.                                                                                                                                                                                          |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool UsesRelaxedRest { get; }``     | Read-only/resolved uses relaxed rest for ``PassengerHandConfig``.                                                                                                                                                                                           |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--passengerlimbdamagefeedback:

PassengerLimbDamageFeedback
---------------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs** Serialized independently at ``seat.leftHand.damageFeedback``, ``rightHand.damageFeedback``, ``leftFoot.damageFeedback`` and ``rightFoot.damageFeedback``. Inspector: **Passenger Seat > Hands, feet and head > [limb] > Damage feedback**.

+----------------------------------------+-----------------------------------------------------------------------------+
| Member                                 | Meaning / default                                                           |
+========================================+=============================================================================+
| ``public bool releaseOnCollision``     | Release this limb after qualifying contact; false.                          |
+----------------------------------------+-----------------------------------------------------------------------------+
| ``public bool releaseOnSpin``          | Release this limb after sustained gravity-relative tilt; false.             |
+----------------------------------------+-----------------------------------------------------------------------------+
| ``public float minimumCollisionForce`` | Average collision force threshold, N; 20000. Both force/speed must qualify. |
+----------------------------------------+-----------------------------------------------------------------------------+
| ``public float minimumCollisionSpeed`` | Relative contact speed threshold, m/s; 3.                                   |
+----------------------------------------+-----------------------------------------------------------------------------+
| ``public float minimumAngle``          | Vehicle tilt against gravity up, degrees; 90. Not ordinary yaw.             |
+----------------------------------------+-----------------------------------------------------------------------------+
| ``public float tiltDelay``             | Continuous time beyond the angle before release, seconds; 0.1.              |
+----------------------------------------+-----------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--passengercollisionsurface:

PassengerCollisionSurface
-------------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs** One serialized entry in a limb's ``releaseColliders`` or the seat's ``ejectColliders``. Inspector paths and ownership are described in :ref:`Seat contact exclusions <uvs-seats--contact-exclusions>`.

+-----------------------------------------+--------------------------------------------------------------------------------+
| Member                                  | Meaning / default                                                              |
+=========================================+================================================================================+
| ``public Collider collider``            | Existing cabin/door surface; null.                                             |
+-----------------------------------------+--------------------------------------------------------------------------------+
| ``public bool ignoreWorldCollisions``   | Ignore eligible physical contacts between this surface and environment; false. |
+-----------------------------------------+--------------------------------------------------------------------------------+
| ``public bool ignoreVehicleCollisions`` | Ignore eligible contacts between this surface and vehicle surfaces; false.     |
+-----------------------------------------+--------------------------------------------------------------------------------+

Flags merge by collider identity across lists: true wins over false for each flag. They do not toggle Collider.enabled. Limb lists admit only their Free limb; the eject list admits the entire ejected body. Subsequent damage activations retain admitted contacts until explicit restoration/reset. Use ``seat.RefreshCollisionSettings()`` after direct runtime list/entry edits.

.. _uvs-api-passengerphysics--passengerrestraints:

PassengerRestraints
-------------------

**Runtime/World/Passengers/Physics/PassengerRestraints.cs**

Stores harness, release, damping and ejection configuration.

.. _uvs-api-passengerphysics--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                         | Meaning                                                                                                                                                                                                       |
+================================================+===============================================================================================================================================================================================================+
| ``public float chestSupportStrength``          | Scales chest support independently of the pelvis. Reapply seated tuning or re-enter the seat after editing. One preserves the original support.                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float ejectionTiltDelay``             | Time in seconds that the ejection tilt must be sustained before releasing the occupant. Initial value: ``.1f``.                                                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ejectPassengerOnCollision``      | Whole occupant release after a sufficiently strong new contact.                                                                                                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ejectPassengerOnSpin``           | Whole occupant release after sustained roll/pitch tilt.                                                                                                                                                       |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enablePassengerEjection``        | Allow the whole occupant to detach from the seat into a free ragdoll. Removes every hand, foot, pelvis and chest restraint. Independent of the limb-only options above.                                       |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessAngularDamper``          | Damping for harness angular damper. Higher values oppose relative motion more strongly. Initial value: ``3``.                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessAngularSpring``          | Restoring stiffness for harness angular spring. Higher values resist displacement more strongly. Initial value: ``16``.                                                                                       |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessChestTravel``            | Harness chest travel in metres in the owning system's space. Initial value: ``.06f``.                                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessDampingRatio``           | Multiplier/fraction controlling harness damping ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: ``1``.                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessForwardLean``            | Seat-relative forward/backward angular travel in degrees around the captured seated pose. Initial value: ``22``.                                                                                              |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessFrequency``              | Natural frequency used to derive compliant harness spring strength, in Hz. Initial value: ``3``.                                                                                                              |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessLimitDamperPerKg``       | Angular travel-limit damping scaled by supported mass. Initial value: ``6``.                                                                                                                                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessLimitSpringPerKg``       | Angular travel-limit stiffness scaled by supported mass. Initial value: ``60``.                                                                                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessMaximumAcceleration``    | Force/torque budget for harness maximum acceleration; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``80``. |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessMaximumTorquePerKg``     | Maximum angular support torque per kilogram of supported mass. Initial value: ``8``.                                                                                                                          |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessSideLean``               | Soft angular travel around the captured seated pose, measured in seat axes.                                                                                                                                   |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessTwist``                  | Seat-relative twist travel in degrees around the captured seated pose. Initial value: ``28``.                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool limitHarnessTravel``             | Keep the pelvis inside Seat Travel and the chest inside Chest Travel using native joint limits. Angular sway stays physical.                                                                                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumEjectionAngle``          | Gravity-relative tilt angle in degrees required for the spin/overturn ejection policy. Initial value: ``90``.                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumEjectionCollisionForce`` | Minimum average contact force in N: impulse divided by the physics timestep.                                                                                                                                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumEjectionCollisionSpeed`` | Minimum relative collision speed in m/s; force and speed thresholds must both be met.                                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 passengerEjectionVelocity``   | Optional additional velocity in vehicle-local m/s. Existing ragdoll linear/angular motion is preserved.                                                                                                       |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reseatEjectedOnReset``           | Allows vehicle reset to restore an eligible occupant previously ejected from this seat. Initial value: ``true``.                                                                                              |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float seatDamper``                    | Damping for seat damper. Higher values oppose relative motion more strongly. Initial value: ``1300``.                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float seatSpring``                    | Restoring stiffness for seat spring. Higher values resist displacement more strongly. Initial value: ``14000``.                                                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float seatTravel``                    | Seat travel in metres in the owning system's space. Initial value: ``.025f``.                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool softHarness``                    | Bounded native spring drives support pelvis and chest without bone pose overrides. Foot pins are configured separately on each foot.                                                                          |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverIterations``                | Minimum solver iterations on seated bones only. Zero preserves the body's setting; higher authored values are retained. Restored on release.                                                                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverVelocityIterations``        | Minimum velocity solver iterations while seated; higher per-body settings are preserved. Initial value: ``4``.                                                                                                |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float torsoSwayDegrees``              | Torso sway degrees in degrees, relative to the owning mechanism's reference frame. Initial value: ``12``.                                                                                                     |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--ragdollcollisionhelper:

RagdollCollisionHelper
----------------------

**Runtime/World/Damage/RagdollCollisionHelper.cs**

Standing-character knockdown and bounded physical response to moving bodies. Contact impulses permit normal closing speed plus the configured additional budget; world-speed safety limits temporarily permit the contacting surface speed. Before the solve, nearby moving colliders are tested at their predicted pose over two physics steps; a predicted bone overlap can activate the ragdoll early, avoiding the one-step kinematic delay. This does not prescribe a roll animation. Zero-feedback chassis sweep filtering remains in place so vehicle panels do not separate at CCD time of impact. Early knockdown predicts geometry before the solve; the dynamic ragdoll retains its configured native collision mode. While moving contacts are active, solver iterations are raised to at least 32 position / 12 velocity iterations and restored afterwards (also on helper disable). Only the standing-to-ragdoll impact arms hood recovery, for at most two seconds and only for the vehicle that knocked the character down. Contacts with an already fallen ragdoll never arm or extend this upward recovery, so repeated run-overs keep native contact response. Within that initial window, if a bone remains over 5 cm inside an upright vehicle collider for at least 0.04 s, a bounded depenetration fallback moves the complete live skeleton towards the exterior together. Per-step displacement is capped by Maximum Depenetration Speed times the fixed timestep; joint angles and velocities are preserved. It uses native physics poses, includes articulated body panels, and releases its hull cache after the contact clears. No authored pose reset or launch impulse is applied.

**Inherits / implements:** ``MonoBehaviour``, :ref:`ICollisionDamageResponse <uvs-api-damage--icollisiondamageresponse>`.

.. _uvs-api-passengerphysics--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                                                                                                                                              |
+=============================================================+======================================================================================================================================================================================================================+
| ``public virtual float CollisionDamageScale { get; }``      | Read-only/resolved collision damage scale for ``RagdollCollisionHelper``.                                                                                                                                            |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool disableJointProjection``                      | Disables native joint projection on the activated ragdoll to avoid projection-driven impact corrections. Initial value: ``true``.                                                                                    |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsKnockedDown { get; }``              | Current is knocked down predicate; read it instead of maintaining a second application flag.                                                                                                                         |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngularSpeed``                        | Maximum bone angular speed in radians/second.                                                                                                                                                                        |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBoneSpeed``                           | Free-flight bone speed cap in metres/second; moving contacts temporarily raise this budget.                                                                                                                          |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumCarrySpeed``                          | Maximum retained carry speed after contact ends, plus 2 m/s slack. During contact, the budget permits the actual surface speed so the car cannot overtake a capped bone. Fades after release; never applies a force. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumContactVelocityChange``               | Additional normal impulse budget beyond closing speed, in units of bone mass times this velocity change.                                                                                                             |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDepenetrationSpeed``                  | Free-ragdoll overlap correction cap in metres/second. During a moving-body contact the cap is at least the surface speed, bounded at 12 m/s for this temporary increase; the upward launch cap still applies.        |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumUpwardSpeed``                         | Upward speed cap prevents launch impulses while allowing the body to climb a hood.                                                                                                                                   |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumImpactSpeed``                         | Minimum incoming normal speed of the contacting body and relative impact required to knock down a standing character. Idle animation touching a parked body is not an impact.                                        |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public CollisionDetectionMode ragdollCollisionDetection`` | Native collision detection mode used by the dynamic ragdoll. Initial value: ``CollisionDetectionMode.ContinuousDynamic``.                                                                                            |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useSpeculativeContacts``                      | Speculative contacts while standing/animated. Dynamic ragdolls keep Ragdoll Collision Detection to avoid ghost contacts at rest and preserve vehicle panel sweeps.                                                   |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float vehicleContactFriction``                     | Friction used for the helper's bounded contacts with external dynamic bodies. Initial value: ``.45f``.                                                                                                               |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float vehicleDamageScale``                         | Scales collision speed used for vehicle damage; normal environment collisions remain unchanged.                                                                                                                      |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float vehicleResponse``                            | Inverse-mass/inertia response of the other dynamic body for this contact only. Zero makes the contact one-way.                                                                                                       |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengerphysics--ragdollcollisionrelay:

RagdollCollisionRelay
---------------------

**Runtime/World/Damage/RagdollCollisionRelay.cs**

Configuration/implementation type for ragdoll collision relay within physical passengers and limb configuration.

**Inherits / implements:** ``MonoBehaviour``.
