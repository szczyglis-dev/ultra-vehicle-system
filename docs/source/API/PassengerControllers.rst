.. _uvs-api-passengercontrollers--seats-bodies-and-controller-strategies-api:

Seats, bodies and controller strategies API
===========================================

Read :doc:`the system explanation </Scripting/PassengerControllers>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _uvs-api-passengercontrollers--types:

Types
-----

-  :ref:`RiderReverseMode <uvs-api-passengercontrollers--riderreversemode>`
-  :ref:`RiderPushFeet <uvs-api-passengercontrollers--riderpushfeet>`
-  :ref:`RiderMotionCondition <uvs-api-passengercontrollers--ridermotioncondition>`
-  :ref:`RiderMotionState <uvs-api-passengercontrollers--ridermotionstate>`
-  :ref:`RiderAnimator <uvs-api-passengercontrollers--rideranimator>`
-  :ref:`RiderAnimationRule <uvs-api-passengercontrollers--rideranimationrule>`
-  :ref:`AnimatorIKPassengerController <uvs-api-passengercontrollers--animatorikpassengercontroller>`
-  :ref:`AnimatorPassengerController <uvs-api-passengercontrollers--animatorpassengercontroller>`
-  :ref:`AttachOnlyPassengerController <uvs-api-passengercontrollers--attachonlypassengercontroller>`
-  :ref:`BalanceRider <uvs-api-passengercontrollers--balancerider>`
-  :ref:`CustomPassengerBody <uvs-api-passengercontrollers--custompassengerbody>`
-  :ref:`CustomPassengerController <uvs-api-passengercontrollers--custompassengercontroller>`
-  :ref:`HumanoidPassenger <uvs-api-passengercontrollers--humanoidpassenger>`
-  :ref:`IPassengerModule <uvs-api-passengercontrollers--ipassengermodule>`
-  :ref:`PassengerAnimatorLayers <uvs-api-passengercontrollers--passengeranimatorlayers>`
-  :ref:`PassengerAnimatorLayers.Layer <uvs-api-passengercontrollers--passengeranimatorlayerslayer>`
-  :ref:`PassengerAttachmentMode <uvs-api-passengercontrollers--passengerattachmentmode>`
-  :ref:`PassengerBehaviour <uvs-api-passengercontrollers--passengerbehaviour>`
-  :ref:`PassengerBody <uvs-api-passengercontrollers--passengerbody>`
-  :ref:`PassengerController <uvs-api-passengercontrollers--passengercontroller>`
-  :ref:`PassengerControllerType <uvs-api-passengercontrollers--passengercontrollertype>`
-  :ref:`PassengerExitReason <uvs-api-passengercontrollers--passengerexitreason>`
-  :ref:`PassengerJointSupport <uvs-api-passengercontrollers--passengerjointsupport>`
-  :ref:`PassengerJointSupportState <uvs-api-passengercontrollers--passengerjointsupportstate>`
-  :ref:`PassengerModule <uvs-api-passengercontrollers--passengermodule>`
-  :ref:`Passengers <uvs-api-passengercontrollers--passengers>`
-  :ref:`PassengerSeat <uvs-api-passengercontrollers--passengerseat>`
-  :ref:`PassengerSeatContext <uvs-api-passengercontrollers--passengerseatcontext>`
-  :ref:`PassengerTransformSupport <uvs-api-passengercontrollers--passengertransformsupport>`
-  :ref:`PassengerType <uvs-api-passengercontrollers--passengertype>`
-  :ref:`RagdollPhysicsPassengerController <uvs-api-passengercontrollers--ragdollphysicspassengercontroller>`
-  :ref:`RiderBlendSource <uvs-api-passengercontrollers--riderblendsource>`
-  :ref:`RiderFootMode <uvs-api-passengercontrollers--riderfootmode>`

.. _uvs-api-passengercontrollers--animatorikpassengercontroller:

AnimatorIKPassengerController
-----------------------------

**Runtime/World/Passengers/Controllers/AnimatorIKPassengerController.cs**

Configuration/implementation type for animator ikpassenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <uvs-api-passengercontrollers--passengercontroller>`.

.. _uvs-api-passengercontrollers--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+----------------------------------------------------------------+
| Member                                                    | Meaning                                                        |
+===========================================================+================================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``AnimatorIKPassengerController``. |
+-----------------------------------------------------------+----------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=========================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--animatorpassengercontroller:

AnimatorPassengerController
---------------------------

**Runtime/World/Passengers/Controllers/AnimatorPassengerController.cs**

Configuration/implementation type for animator passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <uvs-api-passengercontrollers--passengercontroller>`.

.. _uvs-api-passengercontrollers--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+--------------------------------------------------------------+
| Member                                                    | Meaning                                                      |
+===========================================================+==============================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``AnimatorPassengerController``. |
+-----------------------------------------------------------+--------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-1:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=========================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--attachonlypassengercontroller:

AttachOnlyPassengerController
-----------------------------

**Runtime/World/Passengers/Controllers/AttachOnlyPassengerController.cs**

Configuration/implementation type for attach only passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <uvs-api-passengercontrollers--passengercontroller>`.

.. _uvs-api-passengercontrollers--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+----------------------------------------------------------------+
| Member                                                    | Meaning                                                        |
+===========================================================+================================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``AttachOnlyPassengerController``. |
+-----------------------------------------------------------+----------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-2:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=========================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--balancerider:

BalanceRider
------------

**Runtime/World/Passengers/Seats/BalanceRider.cs**

Configurable foot poses and optional physical rider support for seated or standing riders on motorcycles, bicycles, scooters and other vehicles.

**Inherits / implements:** :ref:`PassengerBehaviour <uvs-api-passengercontrollers--passengerbehaviour>`.

.. _uvs-api-passengercontrollers--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                                                                                                    |
+==============================================================+============================================================================================================================================================================================================+
| ``public bool ejectOnExternalImpact``                        | Allow strong external dynamic-body collisions to eject this rider; default true. Independent of the currently selected vehicle and seat tilt/collision policies.                                           |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumExternalImpactSpeed``                  | Minimum normal relative contact speed in m/s; default 4.                                                                                                                                                   |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumExternalImpactVelocityChange``         | Minimum collision impulse divided by chassis mass in m/s; default 1.5. Both thresholds must pass.                                                                                                          |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float externalImpactBalanceDuration``               | Temporary MotorcycleBalance suppression after ejection, in seconds; default 1.5.                                                                                                                           |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float balanceDamper``                               | Relative pelvis/chassis angular damping in Nm per rad/s. Nonnegative; default 25.                                                                                                                          |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float balanceSpring``                               | Pelvis support stiffness in Nm/rad. Nonnegative; default 250.                                                                                                                                              |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public RiderBlendSource blendSource``                      | Choose speed-driven posture transition or a manual blend value. Default Speed.                                                                                                                             |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float blendSpeed``                                  | Rate of the normalized transition between feet-down and riding poses per second. Initial value: ``4``.                                                                                                     |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float forwardLean``                                 | Forward/backward target stance lean relative to the pelvis/backrest frame, degrees; clamped -60..60. Default 0.                                                                                            |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float fullyRaisedAtKph``                            | Fully raised at in km/h (stored value); Speed fields display the selected speed unit. Initial value: ``8``.                                                                                                |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftFootGround``                          | Assign the left foot ground reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                             |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public RiderFootMode leftFootMode``                        | Left-foot pose policy: SpeedBlend, Riding, Ground or Unchanged. Default SpeedBlend.                                                                                                                        |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftFootRiding``                          | Assign the left foot riding reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                             |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float liftStartsAtKph``                             | Lift starts at in km/h (stored value); Speed fields display the selected speed unit. Initial value: ``1``.                                                                                                 |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float manualRidingBlend``                           | Requested Ground-to-Riding progress, clamped 0..1, when the source is Manual. Transition rate remains Blend Speed.                                                                                         |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBalanceTorque``                        | Cap on the added pelvis torque in Nm. Nonnegative; default 120. Zero applies no torque.                                                                                                                    |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool motorcycleProfileOnly``                        | Run this rider behaviour only while the vehicle uses ``MotorcycleProfile``. Disable to use it with another drive profile. Default false on new components; existing serialized restrictions are preserved. |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float RidingBlend { get; protected set; }`` | Read-only/resolved riding blend for ``BalanceRider``.                                                                                                                                                      |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightFootGround``                         | Assign the right foot ground reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                            |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public RiderFootMode rightFootMode``                       | Independent right-foot policy. Default SpeedBlend.                                                                                                                                                         |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightFootRiding``                         | Assign the right foot riding reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                            |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringLean``                                | Additional signed rider side lean at full steering input, degrees; clamped -45..45. Default 0.                                                                                                             |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool supportBalance``                               | Apply optional bounded pelvis support to an occupied dynamic humanoid ragdoll. Default false; does not balance the vehicle.                                                                                |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-3:

Methods
~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                     | Role and behavior                                                             | Arguments and result                                                                                                                                                                       |
+===============================================================+===============================================================================+============================================================================================================================================================================================+
| ``public override bool AppliesTo(VehicleController vehicle)`` | Checks whether this passenger behavior should run for the supplied seat/role. | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void ResetPassenger(Passengers core)``      | Resets this passenger behavior's state for the supplied seat.                 | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\| ``public event Action<RiderMotionState> MotionUpdated`` \| Rider motion configuration or signal; see the setup guide. \| \| ``public event Action<bool> FootPushingChanged`` \| Rider motion configuration or signal; see the setup guide. \| \| ``public event Action<PassengerBodyPart> FootPlanted`` \| Rider motion configuration or signal; see the setup guide. \| \| ``public RiderReverseMode reverseMode`` \| Reverse Gear keeps normal transmission behavior. Foot Pushing selects neutral and uses bounded human-effort wheel torque while an occupied driver can reach the ground. \| \| ``public float footReverseSpeed`` \| Maximum foot-propelled reverse speed in metres per second. \| \| ``public float footPushTorque`` \| Total backward wheel torque in Nm representing the driver's foot pushes, independent of engine power. \| \| ``public float footReverseEngageSpeed`` \| Maximum ground speed in m/s for starting foot pushing. Sideways or backward coasting must finish braking first. \| \| ``public float footStepPeriod`` \| Maximum seconds for a full left/right pair of steps; shortens at higher reverse speed to keep planted feet within reach. Shared by physical targets and animation signals. \| \| ``public bool allowFootPushing`` \| Let this occupied driver provide ground foot targets and provide foot propulsion in Foot Pushing mode with any wheel-driven profile. Passengers never propel the vehicle. \| \| ``public RiderPushFeet pushFeet`` \| Both alternates the feet. Left or Right lets a scooter keep the other foot on its riding/deck target. Disabled prevents foot propulsion. \| \| ``public float footStepDistance`` \| Recovery step distance in metres, relative to the ground pose. \| \| ``public float footStartBlendTime`` \| Seconds to blend the supported foot pose into walking; default 0.12. \| \| ``public float footMotionSmoothTime`` \| Physical target smoothing time in seconds; default 0.06, zero disables smoothing. \| \| ``public float footGroundSmoothTime`` \| Shared wheel support plane smoothing time in seconds; default 0.08, zero disables smoothing. \| \| ``public float footStepHeight`` \| Foot lift in metres during the recovery part of each step. \| \| ``public bool useWheelGroundPlane`` \| Project walking targets onto the existing wheel support plane, without additional raycasts. \| \| ``public float footGroundClearance`` \| Ankle offset above the sampled ground plane in metres. \| \| ``public UnityEvent<RiderMotionState> onMotionUpdated`` \| Current motion state after rider targets update. Suitable for custom animation integrations. \| \| ``public UnityEvent<bool> onFootPushingChanged`` \| Foot propulsion begins or stops; false is also published on disable or loss of occupancy. \| \| ``public UnityEvent<PassengerBodyPart> onFootPlanted`` \| A foot starts its planted phase. The two feet alternate while pushing backward. \| \| ``public RiderMotionState MotionState { get; }`` \| Current resolved rider motion. \| \| ``public bool PushesLeftFoot { get; }`` \| Whether left foot propulsion is selected. \| \| ``public bool PushesRightFoot { get; }`` \| Whether right foot propulsion is selected. \| \| ``public virtual bool CanPushWithFeet { get; }`` \| Whether the occupied driver can currently use the selected ground feet. \|

.. _uvs-api-passengercontrollers--custompassengerbody:

CustomPassengerBody
-------------------

**Runtime/World/Passengers/Bodies/CustomPassengerBody.cs**

Minimal body for application-owned Custom occupancy.

**Inherits / implements:** :ref:`PassengerBody <uvs-api-passengercontrollers--passengerbody>`.

.. _uvs-api-passengercontrollers--methods-4:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                 | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                          |
+===========================================================================================+=====================================================================================================================+===============================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerSeat seat)``                                       | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``controller`` — Controller, interpreted by this operation in the declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                               | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy.                                                                                                                                                            |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--custompassengercontroller:

CustomPassengerController
-------------------------

**Runtime/World/Passengers/Controllers/CustomPassengerController.cs**

Configuration/implementation type for custom passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <uvs-api-passengercontrollers--passengercontroller>`.

.. _uvs-api-passengercontrollers--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+------------------------------------------------------------+
| Member                                                    | Meaning                                                    |
+===========================================================+============================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``CustomPassengerController``. |
+-----------------------------------------------------------+------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-5:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                          | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+====================================================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``                            | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         | ``body`` — Character or rigidbody context, according to the declared type. ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. ``preservePose`` — Whether this handover must retain the current character pose.                                         |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--humanoidpassenger:

HumanoidPassenger
-----------------

**Runtime/World/Passengers/Bodies/HumanoidPassenger.cs**

Connects humanoid rig, pose and physical passenger behavior.

**Inherits / implements:** :ref:`PassengerBody <uvs-api-passengercontrollers--passengerbody>`.

.. _uvs-api-passengercontrollers--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Member                                                           | Meaning                                                                                                                          |
+==================================================================+==================================================================================================================================+
| ``public event System.Action<HumanoidPassenger> AfterSeatedIK``  | Immediately after seated IK work. Payload: ``HumanoidPassenger``.                                                                |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<HumanoidPassenger> BeforeSeatedIK`` | Immediately before seated IK work. Payload: ``HumanoidPassenger``; custom pose inputs must respect the selected character owner. |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                | Meaning                                                                                                                                                                                                              |
+=======================================================================+======================================================================================================================================================================================================================+
| ``public HumanoidJointDefinition[] anatomicalJoints``                 | Configured skeletal joints and reference data used by IK. Tune axes, anchors and limits on each ``ConfigurableJoint`` component.                                                                                     |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Animator animator``                                          | Inspector configuration.                                                                                                                                                                                             |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual ConfigurableJoint[] authoredRagdollJoints { get; }`` | Joint components from the anatomical configuration.                                                                                                                                                                  |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool automaticSeatedIK``                                     | Apply seated IK in ``LateUpdate``: all configured limbs in Animator + IK, or only forced limbs in Animator. Disable to call ``SolveSeatedIK`` from your own animation pipeline.                                      |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float exitCollisionClearance``                               | Keep the previous vehicle excluded until the departing character clears its combined collider bounds by this distance. Prevents animated kinematic limbs from blocking the doors/chassis.                            |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollAngularDamping``                            | Passive rotational damping while falling or lying down. Does not hold a pose or freeze bones.                                                                                                                        |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public CollisionDetectionMode freeRagdollCollisionDetection``       | Collision detection used by released ragdoll bodies. Defaults to Continuous Dynamic; restored to the previous mode on attachment.                                                                                    |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollInertiaScale``                              | Rotational inertia multiplier while released. Defaults to ``4``; reduces abrupt limb rotation without changing mass or linear momentum and restores the original inertia on attachment.                              |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollJointDamping``                              | Passive damping of relative bone rotation. The pose spring stays zero, so joints never return to a riding/idle pose.                                                                                                 |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollMaximumAngularSpeed``                       | Maximum angular speed of released bones in radians/second. Defaults to ``18``; preserves lower per-body limits and restores previous limits on attachment.                                                           |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollMaximumDampingTorque``                      | Force/torque budget for free ragdoll maximum damping torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``20``. |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollMaximumDepenetrationVelocity``              | Maximum separation speed for overlapping free-ragdoll colliders, in m/s. Defaults to ``3``; preserves lower per-body limits and restores previous limits on attachment.                                              |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool freeRagdollPreprocessing``                              | Enable joint preprocessing for free ragdolls. Leave off when impacts pin bones against the ground: preprocessing incompatible contact/joint constraints can sustain head oscillations.                               |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int freeRagdollSolverIterations``                            | Minimum position solver iterations while the character is a free ragdoll. Initial value: ``24``.                                                                                                                     |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int freeRagdollSolverVelocityIterations``                    | Minimum velocity solver iterations while the character is a free ragdoll. Initial value: ``8``.                                                                                                                      |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public HumanoidIK ik``                                              | Assign the ik HumanoidIK component/asset used by HumanoidPassenger.                                                                                                                                                  |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsRagdollActive { get; protected set; }``       | Current is ragdoll active predicate; read it instead of maintaining a second application flag.                                                                                                                       |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform pelvis``                                           | Character pelvis bone used to place and support the seated body.                                                                                                                                                     |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool physicalWhileSeated``                                   | Keeps the seated skeleton physically simulated rather than attaching it as a kinematic character.                                                                                                                    |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Rigidbody[] ragdollBodies``                                  | Assign the ragdoll bodies references used by HumanoidPassenger. Entries are processed in list order. Initial value: ``System.Array.Empty<Rigidbody>()``.                                                             |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int RestraintCount { get; }``                        | Read-only/resolved restraint count for ``HumanoidPassenger``.                                                                                                                                                        |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Animator SeatedAnimator { get; }``                   | Read-only/resolved seated animator for ``HumanoidPassenger``.                                                                                                                                                        |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SoftHarness { get; }``                          | Read-only/resolved soft harness for ``HumanoidPassenger``.                                                                                                                                                           |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-6:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                       | Role and behavior                                                                                                                                                                       | Arguments and result                                                                                                                                                                                                                          |
+=================================================================================================================+=========================================================================================================================================================================================+===============================================================================================================================================================================================================================================+
| ``public virtual void ActivateRagdoll()``                                                                       | Hands the character to free skeletal physics, releasing seated pose ownership.                                                                                                          | No arguments; no returned value.                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void AddVelocity(Vector3 velocityChange)``                                                    | Adds the supplied velocity change to the character bodies used by this body implementation.                                                                                             | ``velocityChange`` — World velocity change in m/s.                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool Attach(PassengerSeat seat)``                                                             | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication.                                                                     | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat)``                                                           | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.                                                                      | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                  |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)``                       | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.                                                                      | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``controller`` — Controller, interpreted by this operation in the declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                                                     | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.                                                                             | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy.                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void DetachForTransition()``                                                                  | Releases seated ownership for an animated character handover while preserving the required transition pose.                                                                             | No arguments; no returned value.                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual ConfigurableJoint GetAnatomicalJoint(string jointId)``                                         | Returns the native ConfigurableJoint for a unique live ID, or null when unresolved/ambiguous.                                                                                           | ``jointId`` — exact authored ID. Output is null on failure.                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PrepareRagdollCollisions()``                                                              | Prepares the character's skeletal collision exclusions and collision relays.                                                                                                            | No arguments; no returned value.                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreviewAccessPose(PassengerSeat seat)``                                                   | Applies an access reference pose for character/seat authoring or transition preparation.                                                                                                | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReadAnatomicalJointSettings()``                                                           | Reads saved native joint configuration into the character's runtime anatomical references.                                                                                              | No arguments; no returned value.                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void ResetSeatedPose()``                                                                      | Restores the character's seated pose/support through the selected physical/animation path.                                                                                              | No arguments; no returned value.                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreAccessReferencePose()``                                                            | Restores the character pose retained for an access-motion handover.                                                                                                                     | No arguments; no returned value.                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveSeatedIK()``                                                                         | Applies the seated character's configured limb IK targets.                                                                                                                              | No arguments; no returned value.                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void StepSeated(Passengers core, float deltaTime)``                                           | Advances this body's seated behavior through its selected character path.                                                                                                               | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetAnatomicalJoint(string jointId, out ConfigurableJoint joint)``                      | Returns true and the native ConfigurableJoint for a unique live ID; otherwise false and null. Lookup allocates no managed memory.                                                       | ``jointId`` — exact authored ID. Output is null on failure.                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetAnatomicalJointDefinition(string jointId, out HumanoidJointDefinition definition)`` | Returns the unique definition with a live joint for the case-sensitive ID; false/null for empty, missing, duplicate or destroyed entries.                                               | ``jointId`` — exact authored ID. Output is null on failure.                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateAnatomicalJoint(string jointId, System.Action<ConfigurableJoint> update)``          | Runs the callback on a uniquely resolved joint, then refreshes its cached anatomy/IK data. False for unresolved ID or null callback. Callback exceptions propagate after cache refresh. | ``jointId`` — exact authored ID. Output is null on failure.                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                                                              | Usage                                                                                                                          |
+==========================================================================================+================================================================================================================================+
| ``public virtual void BlendIntoPhysics(float seconds, Transform referenceFrame = null)`` | Blend the captured animated pose into physical ownership over the requested seconds, optionally relative to a reference frame. |
+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--ipassengermodule:

IPassengerModule
----------------

**Runtime/World/Passengers/Core/PassengerModule.cs**

Configuration/implementation type for ipassenger module within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`IWorldModule <uvs-api-modules--iworldmodule>`.

.. _uvs-api-passengercontrollers--passengeranimatorlayers:

PassengerAnimatorLayers
-----------------------

**Runtime/World/Passengers/Controllers/PassengerAnimatorLayers.cs**

Seat-scoped ownership of configured Animator overlay weights. Masks remain controller authoring assets. :ref:`Inspector setup <uvs-handleanimation--masked-animator-layers>`.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-passengercontrollers--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+----------------------------------------------------------------------------------------------+
| Member                                          | Meaning                                                                                      |
+=================================================+==============================================================================================+
| ``public RuntimeAnimatorController controller`` | Controller edited by Inspector authoring actions; does not switch the occupant's controller. |
+-------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public List<Layer> layers``                   | Configured overlay names, masks, enabled flags and weights.                                  |
+-------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public PassengerSeat seat``                   | Seat whose humanoid supplies the active Animator, including its physical pose source.        |
+-------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-7:

Methods
~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Signature                                                     | Role and behavior                                                                                       | Arguments and result                                                                                    |
+===============================================================+=========================================================================================================+=========================================================================================================+
| ``public void Apply()``                                       | Resolves the current occupant and applies weights. Missing occupants/layers and Base Layer are skipped. | No result. Automatically called during Update while enabled.                                            |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public void RefreshBindings()``                             | Restores previous weights and rebuilds the binding immediately.                                         | No result.                                                                                              |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool SetLayerEnabled(string layerName, bool value)`` | Mutes a configured overlay or restores its requested weight.                                            | Returns false for an unknown configuration name.                                                        |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool SetWeight(string layerName, float weight)``     | Sets a configured request, clamped to 0..1, and applies it when possible.                               | Returns false for an unknown configuration or non-finite weight; does not imply an occupant is present. |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengeranimatorlayerslayer:

PassengerAnimatorLayers.Layer
-----------------------------

**Runtime/World/Passengers/Controllers/PassengerAnimatorLayers.cs**

Serializable configuration entry owned by PassengerAnimatorLayers.

.. _uvs-api-passengercontrollers--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------+------------------------------------------------------------------------------------+
| Member                     | Meaning                                                                            |
+============================+====================================================================================+
| ``public bool enabled``    | True by default; false mutes this overlay without losing its requested weight.     |
+----------------------------+------------------------------------------------------------------------------------+
| ``public AvatarMask mask`` | Authoring mask saved with the Inspector Apply action. Null permits the whole body. |
+----------------------------+------------------------------------------------------------------------------------+
| ``public string name``     | Existing overlay layer name; Base Layer is excluded.                               |
+----------------------------+------------------------------------------------------------------------------------+
| ``public float weight``    | Requested blend weight, initially 1.                                               |
+----------------------------+------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengerattachmentmode:

PassengerAttachmentMode
-----------------------

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Main attachment policy on PassengerSeat. ``Spring = 0`` retains selected controller behavior and is the default. ``Parent = 1`` attaches the main origin to Spine Anchor independently of ragdoll state. Physical humanoids retain their ragdoll with only the pelvis held. Custom retains automatic main attachment ownership.

.. _uvs-api-passengercontrollers--passengerbehaviour:

PassengerBehaviour
------------------

**Runtime/World/Passengers/Core/PassengerBehaviour.cs**

Configuration/implementation type for passenger behaviour within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerModule <uvs-api-passengercontrollers--passengermodule>`.

.. _uvs-api-passengercontrollers--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+---------------------------------------------------------------------------+
| Member                                          | Meaning                                                                   |
+=================================================+===========================================================================+
| ``public override int ExecutionOrder { get; }`` | Default local priority within phase/category.                             |
+-------------------------------------------------+---------------------------------------------------------------------------+
| ``public PassengerSeat seat``                   | Assign the seat PassengerSeat component/asset used by PassengerBehaviour. |
+-------------------------------------------------+---------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-8:

Methods
~~~~~~~

+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                       | Role and behavior                                                             | Arguments and result                                                                                                                                                                       |
+=================================================================================+===============================================================================+============================================================================================================================================================================================+
| ``public virtual bool AppliesTo(VehicleController vehicle)``                    | Checks whether this passenger behavior should run for the supplied seat/role. | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public sealed override void StepPassenger(Passengers core, float deltaTime)`` | Advances passenger work in the supplied seat/core context.                    | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                   |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengerbody:

PassengerBody
-------------

**Runtime/World/Passengers/Bodies/PassengerBody.cs**

Base character adapter used by seats and controller strategies.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-passengercontrollers--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Member                                                                 | Meaning                                                                                               |
+========================================================================+=======================================================================================================+
| ``public virtual bool IsCustomControlled { get; protected set; }``     | Current is custom controlled predicate; read it instead of maintaining a second application flag.     |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsExternallyControlled { get; protected set; }`` | Current is externally controlled predicate; read it instead of maintaining a second application flag. |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerSeat Seat { get; protected set; }``          | Read-only/resolved seat for ``PassengerBody``.                                                        |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-9:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                          |
+==========================================================================================+=====================================================================================================================+===============================================================================================================================================================================================================================================+
| ``public virtual void AddVelocity(Vector3 velocityChange)``                              | Adds the supplied velocity change to the character bodies used by this body implementation.                         | ``velocityChange`` — World velocity change in m/s.                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract bool Attach(PassengerSeat seat)``                                      | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                   |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                  |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``controller`` — Controller, interpreted by this operation in the declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Detach(PassengerExitReason reason)``                              | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy.                                                                                                                                                            |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void DetachForTransition()``                                            | Releases seated ownership for an animated character handover while preserving the required transition pose.         | No arguments; no returned value.                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetSeatedPose()``                                                | Restores the character's seated pose/support through the selected physical/animation path.                          | No arguments; no returned value.                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepSeated(Passengers core, float deltaTime)``                     | Advances this body's seated behavior through its selected character path.                                           | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                      |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengercontroller:

PassengerController
-------------------

**Runtime/World/Passengers/Controllers/PassengerController.cs**

Per-seat strategy for body attachment, detachment and stepping; the seat retains occupancy authority.

.. _uvs-api-passengercontrollers--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+------------------------------------------------------+
| Member                                                    | Meaning                                              |
+===========================================================+======================================================+
| ``public abstract PassengerControllerType Type { get; }`` | Read-only/resolved type for ``PassengerController``. |
+-----------------------------------------------------------+------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-10:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                         | Role and behavior                                                                                                              | Arguments and result                                                                                                                                                                                                                                                                   |
+===================================================================================================+================================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public abstract bool Attach(PassengerBody body, PassengerSeat seat)``                           | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication.            | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static PassengerController Create(PassengerControllerType type)``                        | Creates the built-in strategy for a ``PassengerControllerType``; seat factory overrides can substitute application strategies. | ``type`` — Type, interpreted by this operation in the declared type. **Returns:** Returned ``PassengerController``; ownership remains as specified by the creating/lookup operation.                                                                                                   |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.                    | ``body`` — Character or rigidbody context, according to the declared type. ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. ``preservePose`` — Whether this handover must retain the current character pose.                                         |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(PassengerBody body, Passengers core, float deltaTime)``                | Empty base passenger strategy step; derived strategies decide which body work they own.                                        | ``body`` — Character or rigidbody context, according to the declared type. ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                    |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengercontrollertype:

PassengerControllerType
-----------------------

**Runtime/World/Passengers/Controllers/PassengerController.cs**

Defines the allowed passenger controller type choices used by this topic.

.. _uvs-api-passengercontrollers--values:

Values
~~~~~~

-  ``RagdollPhysics = 0``
-  ``Animator = 1``
-  ``[InspectorName("Animator + IK")] AnimatorIK = 2``
-  ``AttachOnly = 3``
-  ``Custom = 4``

.. _uvs-api-passengercontrollers--passengerexitreason:

PassengerExitReason
-------------------

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Defines the allowed passenger exit reason choices used by this topic.

.. _uvs-api-passengercontrollers--values-1:

Values
~~~~~~

-  ``Exit``
-  ``Ejected``
-  ``Disabled``
-  ``Destroyed``

.. _uvs-api-passengercontrollers--passengerjointsupport:

PassengerJointSupport
---------------------

**Runtime/World/Passengers/Seats/PassengerJointSupport.cs**

Serializable seat-owned support settings. Anatomical constraints remain active; these settings add forces rather than editing limits or creating another native joint.

.. _uvs-api-passengercontrollers--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Member                            | Meaning                                                                                                         |
+===================================+=================================================================================================================+
| ``public bool active``            | Enables this entry, default true. Inactive entries exert no force or torque.                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Transform anchor``       | Target world pose, normally an empty child of the vehicle. Missing target means no support.                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float damper``           | Relative point velocity damping in N/(m/s), default 30. Includes target movement.                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public bool holdRotation``      | Also aligns the joint body to the target orientation. Default false; point-only support leaves angular freedom. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public string jointId``         | Exact Anatomical Joints ID of the occupant. Case-sensitive; duplicates in the seat or occupant are skipped.     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localOffset``    | Body-local offset added to the native joint anchor. Zero holds the anatomical pivot itself.                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float maximumForce``     | Combined position spring/damping force cap in N, default 300. Zero disables positional support.                 |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float maximumTorque``    | Combined angular spring/damping torque cap in Nm, default 40. Zero disables angular support.                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float rotationDamper``   | Relative angular velocity damping in Nm/(rad/s), default 10.                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Vector3 rotationOffset`` | Desired body rotation relative to the anchor in degrees; default zero.                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float rotationSpring``   | Angular stiffness in Nm/rad, default 100.                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float spring``           | Position stiffness in N/m, default 500. Pulls the supported point toward the target.                            |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengerjointsupportstate:

PassengerJointSupportState
--------------------------

**Runtime/World/Passengers/Seats/PassengerJointSupport.cs**

Read-only snapshot of the last applied calculation; positions use metres and vectors use world axes. Read with PassengerSeat.TryGetJointSupportState. It is not an accumulated impulse or measured joint reaction.

.. _uvs-api-passengercontrollers--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-----------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                 |
+=============================================+=========================================================================================+
| ``public readonly Rigidbody Body``          | Dynamic body on the anatomical joint’s GameObject.                                      |
+---------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public readonly Vector3 Force``           | Clamped world force in N passed to AddForceAtPosition.                                  |
+---------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public readonly ConfigurableJoint Joint`` | Resolved anatomical joint; never replaced or reconfigured by the support.               |
+---------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public readonly Vector3 Point``           | Supported world point at calculation time, including the joint anchor and local offset. |
+---------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public readonly Vector3 TargetPosition``  | Target world position used by the last support calculation.                             |
+---------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public readonly Vector3 Torque``          | Clamped world torque in Nm passed to AddTorque; zero when rotation support is off.      |
+---------------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengermodule:

PassengerModule
---------------

**Runtime/World/Passengers/Core/PassengerModule.cs**

Configuration/implementation type for passenger module within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`WorldModule <uvs-api-modules--worldmodule>`, :ref:`IPassengerModule <uvs-api-passengercontrollers--ipassengermodule>`.

.. _uvs-api-passengercontrollers--state-and-configuration-13:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+---------------------------------------------------------------+
| Member                                                   | Meaning                                                       |
+==========================================================+===============================================================+
| ``public sealed override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline. |
+----------------------------------------------------------+---------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-11:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                         | Role and behavior                                                                                                                                 | Arguments and result                                                                                                                                                                                                     |
+===================================================================================================+===================================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual void PreparePassenger(Passengers core, PassengerSeat seat)``                     | Prepares this passenger behavior for an occupied seat.                                                                                            | ``core`` — Owning audio or passenger core supplying shared context. ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                        |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RenderPassenger(Passengers core)``                                          | Advances render-time passenger presentation owned by this behavior/core.                                                                          | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetPassenger(Passengers core)``                                           | Resets this passenger behavior's state for the supplied seat.                                                                                     | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public sealed override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Intentionally empty sealed module-pipeline entry point. Passenger-local work runs through ``StepPassenger``/``RenderPassenger`` under Passengers. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                           | Advances passenger work in the supplied seat/core context.                                                                                        | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                 |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengers:

Passengers
----------

**Runtime/World/Passengers/Core/Passengers.cs**

Discovers owned handles and supplies input before seat work.

**Inherits / implements:** :ref:`WorldModule <uvs-api-modules--worldmodule>`.

.. _uvs-api-passengercontrollers--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                            | Meaning                                                                                                                                                                  |
+===================================================================================+==========================================================================================================================================================================+
| ``public event Action<PassengerSeatContext> AfterEject``                          | After ejected detachment and the requested built-in velocity change. Custom controllers retain their application-owned physics. Payload: immutable PassengerSeatContext. |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterEnter``                          | After successful attachment and existing Entered notifications. Payload: immutable PassengerSeatContext.                                                                 |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterExit``                           | After detachment and existing Exited notifications. During ejection this precedes the extra velocity change. Payload: immutable PassengerSeatContext.                    |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeEject``                         | Before any ejection detachment, while the seat is still occupied. Payload: immutable PassengerSeatContext.                                                               |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeEnter``                         | After admission validation, before occupancy assignment and controller attachment. Occupant and Passenger.Seat are still empty. Payload: immutable PassengerSeatContext. |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeExit``                          | While the passenger still owns the seat, before detachment. Includes ordinary exit, ejection, disable and destruction. Payload: immutable PassengerSeatContext.          |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeat, PassengerBody> Entered``                     | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat.                                                     |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeat, PassengerBody, PassengerExitReason> Exited`` | After occupancy is released. Payload identifies occupant and ``PassengerExitReason``; the core delegate also includes the seat.                                          |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--state-and-configuration-14:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                               | Meaning                                                                                                                                                                              |
+======================================================================+======================================================================================================================================================================================+
| ``public virtual PassengerModule[] PassengerModules { get; }``       | Read-only/resolved passenger modules for Passengers.                                                                                                                                 |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                    | Cross-category execution barrier used by the module pipeline.                                                                                                                        |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerSeat[] Seats { get; }``                    | Read-only/resolved seats for Passengers.                                                                                                                                             |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spawnOnStart``                                         | Creates/adopts the configured occupant(s) at startup when the owning seat/hub is enabled. Initial value: ``true``.                                                                   |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsDirectControl { get; }``              | Opts into direct-mode stepping; keeps seated passenger updates available.                                                                                                            |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsReleasedForces { get; }``             | Keeps passive maintenance/observation active during release; Drive and Engine suppress force output, and TireCollision keeps native solid proxies without supplemental tread forces. |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual VehicleController Vehicle { get; protected set; }`` | Read-only/resolved vehicle for Passengers.                                                                                                                                           |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-12:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                  | Role and behavior                                                                                         | Arguments and result                                                                                                                                                                                                                                                                                          |
+============================================================================================================+===========================================================================================================+===============================================================================================================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                                              | Rebuilds the owned passenger seats, ordered handles and passenger-local behaviors.                        | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PrepareOccupant(PassengerSeat seat)``                                                | Prepares a seat's occupant and its local handles/passenger behaviors.                                     | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshPassengers()``                                                                | Rebuilds the owned seat and passenger-behavior snapshot. Handles use vehicle.handles.Refresh().           | No arguments; no returned value.                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetOccupants()``                                                                   | Resets eligible owned seated/released occupants through their seat lifecycle.                             | No arguments; no returned value.                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``                 | Supplies commands to handles in order, then advances passenger modules and seats from the owned snapshot. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                      |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody body, PassengerSeat seat = null)``                            | Routes an entry request through an owned seat/passenger selection and that seat's validation.             | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. Default: ``null``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                          |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerBody body, PassengerExitReason reason = PassengerExitReason.Exit)`` | Requests immediate exit or starts animated departure, depending on the declaring owner.                   | ``body`` — Character or rigidbody context, according to the declared type. ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. Default: ``PassengerExitReason.Exit``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--vehicle-shortcut:

Vehicle shortcut
~~~~~~~~~~~~~~~~

Use ``vehicle.passengers`` for the first registered ``Passengers`` module. It can be null and does not automatically enable a disabled module. ``Seats`` is a cloned array snapshot; cache it for repeated enumeration. Immediate TryEnter/TryExit on this core do not play access motion; see :ref:`the usage and boarding distinction <uvs-passengers--access-the-passenger-system-from-a-vehicle>`.

+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Declaration                                                                       | Usage                                                                                             |
+===================================================================================+===================================================================================================+
| ``public UnityEvent<PassengerSeatContext> onBeforeEnter``                         | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeat, PassengerBody> onEntered``                     | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeatContext> onBeforeExit``                          | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeat, PassengerBody, PassengerExitReason> onExited`` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeatContext> onBeforeEject``                         | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeatContext> onEjected``                             | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengerseat:

PassengerSeat
-------------

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

``Entered``, ``Exited``, ``ControllerChanged`` and custom ``ResetRequested``

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-passengercontrollers--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                                                     | Meaning                                                                                                                                                                  |
+============================================================================================================+==========================================================================================================================================================================+
| ``public event Action<PassengerSeatContext> AfterEject``                                                   | After ejected detachment and the requested built-in velocity change. Custom controllers retain their application-owned physics. Payload: immutable PassengerSeatContext. |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterEnter``                                                   | After successful attachment and existing Entered notifications. Payload: immutable PassengerSeatContext.                                                                 |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterExit``                                                    | After detachment and existing Exited notifications. During ejection this precedes the extra velocity change. Payload: immutable PassengerSeatContext.                    |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeEject``                                                  | Before any ejection detachment, while the seat is still occupied. Payload: immutable PassengerSeatContext.                                                               |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeEnter``                                                  | After admission validation, before occupancy assignment and controller attachment. Occupant and Passenger.Seat are still empty. Payload: immutable PassengerSeatContext. |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeExit``                                                   | While the passenger still owns the seat, before detachment. Includes ordinary exit, ejection, disable and destruction. Payload: immutable PassengerSeatContext.          |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeat, PassengerControllerType, PassengerControllerType> ControllerChanged`` | After a successful seat strategy handover. Payload: seat, previous controller type, new controller type; no extra entry/exit is synthesized.                             |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> Entered``                                                             | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat.                                                     |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody, PassengerExitReason> Exited``                                         | After occupancy is released. Payload identifies occupant and ``PassengerExitReason``; the core delegate also includes the seat.                                          |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> ResetRequested``                                                      | When Custom occupancy receives a reset request. Payload: ``PassengerBody``; application owns the actual custom-character reset.                                          |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--state-and-configuration-15:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                 | Meaning                                                                                                                                                                                                    |
+========================================================================+============================================================================================================================================================================================================+
| ``public virtual PassengerControllerType ActiveController { get; }``   | Read-only/resolved active controller for ``PassengerSeat``.                                                                                                                                                |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attachmentDamper``                                      | Main non-physical Spring damping; default 20. Captured on refresh.                                                                                                                                         |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerAttachmentMode AttachmentMode { get; }``             | Current main attachment mode; default Spring. Set through SetAttachmentMode.                                                                                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attachmentSpring``                                      | Main non-physical Spring stiffness; default 120. Captured on refresh.                                                                                                                                      |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBody body``                                          | Optional pre-placed body. Leave empty to spawn the prefab.                                                                                                                                                 |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBody bodyPrefab``                                    | Assign the body prefab PassengerBody component/asset used by PassengerSeat.                                                                                                                                |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerControllerType Controller { get; }``         | Read-only/resolved controller for ``PassengerSeat``.                                                                                                                                                       |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string customTypeId``                                         | Application-defined type for Custom occupants; avoids changing the enum.                                                                                                                                   |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableSelfCollidersOnRelease``                           | Enable self contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. Neighboring skeletal bodies keep collisions disabled. |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableVehicleCollidersOnRelease``                        | Enable vehicle contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently.                                                    |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerCollisionSurface[] ejectColliders``                  | Selected surfaces admitted for the whole ejected passenger. Each entry contains a collider and world/vehicle ignore policies. Call RefreshCollisionSettings after runtime edits.                           |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool excludeSelfCollisionsOnEnter``                           | Exclude self contacts on entry and while held. Release options may restore them. Disable to keep self contacts enabled, including after regrip and reseating. Native joint collision settings still apply. |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool excludeVehicleCollisionsOnEnter``                        | Exclude contacts with the vehicle on entry and while held. Release options may restore them. Disable to keep vehicle contacts enabled, including after regrip and reseating.                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform exitAnchor``                                        | Assign the exit anchor reference used by PassengerSeat. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                                 |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool FeetReleasedByDamage { get; }``                  | Read-only/resolved feet released by damage for ``PassengerSeat``.                                                                                                                                          |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerGForceLimits gForceLimits``                          | Enabled-by-default, live emergency acceleration limits; independent per-seat history. See :ref:`G-force limits <uvs-seats--g-force-limits>`.                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool GForceProtectionActive { get; }``                        | Whether temporary overload protection is active for this seat.                                                                                                                                             |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandsReleasedByDamage { get; }``                 | Read-only/resolved hands released by damage for ``PassengerSeat``.                                                                                                                                         |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float headDamper``                                            | Damping relative to chassis angular velocity in Nm per rad/s; default 20.                                                                                                                                  |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float headPitch``                                             | Desired head pitch relative to seat-forward in degrees: negative looks up, positive looks down. Clamped to -60..60; default 0.                                                                             |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float headSpring``                                            | Support stiffness in Nm/rad; default 250.                                                                                                                                                                  |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool holdHeadForward``                                        | Enable artificial head support for this occupied Ragdoll Physics seat, independently of drive profile. Default false.                                                                                      |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public List<PassengerJointSupport> jointSupports``                   | Optional extra supports for this seat; empty by default. One entry per anatomical Joint ID. Settings are live and are retained across occupants.                                                           |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerFootConfig leftFoot``                                | Left-foot bone/contact configuration used by the character or seat. Initial value: ``new PassengerFootConfig()``.                                                                                          |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerHandConfig leftHand``                                | Left-hand bone/contact configuration used by the character or handle. Initial value: ``new PassengerHandConfig()``.                                                                                        |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumHeadTorque``                                     | Support torque cap in Nm; default 80. Zero applies no torque.                                                                                                                                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerBody Occupant { get; protected set; }``      | Body currently admitted to this seat, or ``null`` when empty.                                                                                                                                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool parentMakeKinematic``                                    | Parent mode temporarily makes the held pelvis Rigidbody kinematic; default true. Other bones keep simulating.                                                                                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 parentPositionOffset``                                | Parent mode Spine Anchor local position offset.                                                                                                                                                            |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 parentRotationOffset``                                | Parent mode Spine Anchor local Euler degrees.                                                                                                                                                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool parentWhileSeated``                                      | Parents the occupant to the seat hierarchy while attached; physics still follows the selected passenger controller. Initial value: ``true``.                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float PassengerGForce { get; }``                              | Latest sampled gravity-compensated seat acceleration in standard G; cleared on reset/exit.                                                                                                                 |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool PassengerReleasedByDamage { get; }``             | Read-only/resolved passenger released by damage for ``PassengerSeat``.                                                                                                                                     |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerType passengerType``                                 | Chooses the package occupant type to create for the seat. Options: ``HumanoidDriver``, ``HumanoidPassenger``, ``Custom``. Initial value: ``PassengerType.HumanoidPassenger``.                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerAccess Reservation { get; protected set; }`` | Current seat-access/request reservation identity; reservation does not itself mean occupancy.                                                                                                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerRestraints restraints``                              | Pelvis/chest support, damping, release and ejection settings. Expand to configure each policy. Initial value: ``new PassengerRestraints()``.                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerFootConfig rightFoot``                               | Right-foot bone/contact configuration used by the character or seat. Initial value: ``new PassengerFootConfig()``.                                                                                         |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerHandConfig rightHand``                               | Right-hand bone/contact configuration used by the character or handle. Initial value: ``new PassengerHandConfig()``.                                                                                       |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string seatId``                                               | Application-facing identifier for this seat. Initial value: ``"Passenger"``.                                                                                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                                             | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics.                                                     |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spawnOnStart``                                           | Creates/adopts the configured occupant(s) at startup when the owning seat/hub is enabled. Initial value: ``true``.                                                                                         |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform spineAnchor``                                       | Pelvis / seated spine origin, facing forward, Y up.                                                                                                                                                        |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public List<PassengerTransformSupport> transformSupports``           | Initially empty independent Spring/Parent binding list. Direct edits require RefreshTransformSupports.                                                                                                     |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-13:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                         | Role and behavior                                                                                                                                                                                                           | Arguments and result                                                                                                                                                                                                                                                                                                                    |
+===================================================================================================================+=============================================================================================================================================================================================================================+=========================================================================================================================================================================================================================================================================================================================================+
| ``public virtual bool AddJointSupport(PassengerJointSupport support)``                                            | Adds settings without requiring an occupant. Rejects null, blank IDs and duplicate IDs; an unresolved anatomical ID can be configured before entry.                                                                         | ``jointId`` is the occupant’s exact anatomical ID, where present. Boolean methods report success.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool AddTransformSupport(PassengerTransformSupport support)``                                    | Adds a non-null entry with both references, rejects duplicate bodyTransform or nonblank ID, refreshes; true means accepted configuration, not necessarily a resolved binding.                                               | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool EjectFromImpact(Vector3 velocityChange)``                                                   | Eject through the standard seat lifecycle and retain automatic reset/reseat ownership.                                                                                                                                      | World additional velocity in m/s; returns whether release succeeded.                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Eject(Vector3 velocityChange)``                                                             | Requests whole-occupant release through the seat's controller/body lifecycle.                                                                                                                                               | ``velocityChange`` — World velocity change in m/s. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerBodyPartConfig GetBodyPart(PassengerBodyPart part)``                                    | Returns the seat configuration for a selected limb/body part.                                                                                                                                                               | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Returned ``PassengerBodyPartConfig``; ownership remains as specified by the creating/lookup operation.                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerJointSupport GetJointSupport(string jointId)``                                          | Returns the editable support settings, or null for an unresolved or ambiguous ID.                                                                                                                                           | ``jointId`` is the occupant’s exact anatomical ID, where present. Boolean methods report success.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerTransformSupport GetTransformSupport(string id)``                                       | Returns live settings for a unique ID, otherwise null.                                                                                                                                                                      | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerTransformSupport GetTransformSupport(Transform bodyTransform)``                         | Returns live settings matching the configured reference, or null for missing/duplicate references. Use the prefab reference for prefab-authored entries.                                                                    | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCollisionSettings()``                                                                | Reapplies the seat's collision policy to its current occupant.                                                                                                                                                              | No arguments; no returned value.                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshTransformSupports()``                                                                | Restores existing bindings, resolves the current list and applies eligible entries. Empty seats retain settings; all occupied controller/physics combinations can apply explicit bindings.                                  | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReleaseReservation(PassengerAccess owner)``                                                 | Releases a seat reservation belonging to the supplied reservation owner.                                                                                                                                                    | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RemoveJointSupport(string jointId)``                                                        | Removes the uniquely identified support and clears runtime support state. Returns false if unresolved.                                                                                                                      | ``jointId`` is the occupant’s exact anatomical ID, where present. Boolean methods report success.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RemoveTransformSupport(string id)``                                                         | Removes a uniquely identified entry and refreshes; false for unresolved IDs.                                                                                                                                                | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RemoveTransformSupport(Transform bodyTransform)``                                           | Removes all matching configured references and refreshes; false when none match.                                                                                                                                            | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreDamageFeedback()``                                                                   | Restores the eligible seated limb supports released by damage feedback.                                                                                                                                                     | No arguments; no returned value.                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetAttachmentMode(PassengerAttachmentMode mode)``                                           | Reattaches an occupied built-in body without occupancy events; returns false for invalid modes, busy access/reservation, transitions or incompatible attachment. Rolls back a rejected attach. Custom only stores the mode. | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetCollisionExclusions(bool self, bool vehicle)``                                           | Sets seated self/vehicle collision exclusion policy and updates the occupied character.                                                                                                                                     | ``self`` — Whether the selected policy applies to contacts within the passenger skeleton. ``vehicle`` — Whether the policy applies to passenger-versus-vehicle contacts.                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetJointSupportActive(string jointId, bool active)``                                        | Pauses/resumes one support without disabling the seat or changing anatomical joints. Changed state takes effect on the next physics step; deactivation invalidates diagnostics immediately.                                 | ``jointId`` is the occupant’s exact anatomical ID, where present. Boolean methods report success.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetPassengerController(PassengerControllerType type)``                                      | Requests a validated strategy handover for the seat; an incompatible/busy handover can be rejected.                                                                                                                         | ``type`` — Type, interpreted by this operation in the declared type. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(bool self, bool vehicle)``                                             | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                                                                                 | ``self`` — Whether the selected policy applies to contacts within the passenger skeleton. ``vehicle`` — Whether the policy applies to passenger-versus-vehicle contacts.                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(PassengerBodyPart part, bool self, bool vehicle)``                     | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                                                                                 | ``part`` — Selected body-part enum or part configuration, as declared. ``self`` — Whether the selected policy applies to contacts within the passenger skeleton. ``vehicle`` — Whether the policy applies to passenger-versus-vehicle contacts.                                                                                         |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetTransformSupportActive(string id, bool active)``                                         | Changes active state and refreshes when changed; false for unresolved IDs.                                                                                                                                                  | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetTransformSupportActive(Transform bodyTransform, bool active)``                           | Enables/disables a unique entry and refreshes when changed; false if unresolved/duplicate.                                                                                                                                  | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Spawn()``                                                                                   | Creates/requests the configured passenger representation through the seat's spawn policy.                                                                                                                                   | **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                                           | Advances passenger work in the supplied seat/core context.                                                                                                                                                                  | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger)``                                                         | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes.                                                                 | ``passenger`` — Character body receiving motion/attachment. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger, PassengerAccess reservation)``                            | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes.                                                                 | ``passenger`` — Character body receiving motion/attachment. ``reservation`` — Identity that owns the seat reservation; release must use that owner. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                            |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerExitReason reason = PassengerExitReason.Exit, bool preservePose = false)`` | Releases current occupancy through its active strategy and exit reason; it does not run an animated access sequence.                                                                                                        | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. Default: ``PassengerExitReason.Exit``. ``preservePose`` — Whether this handover must retain the current character pose. Default: ``false``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetJointSupport(string jointId, out PassengerJointSupport support)``                     | Finds exactly one seat support for the case-sensitive anatomical ID. Empty, missing or duplicate IDs return false and null.                                                                                                 | ``jointId`` is the occupant’s exact anatomical ID, where present. Boolean methods report success.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetJointSupportState(string jointId, out PassengerJointSupportState state)``             | Returns the last applied support calculation while the same valid physical occupant, joint and anchor remain available. False/default before the first step, after removal/release or when disabled, invalid or ambiguous.  | ``jointId`` is the occupant’s exact anatomical ID, where present. Boolean methods report success.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetTransformSupport(string id, out PassengerTransformSupport support)``                  | Resolves one exact ordinal ID; false and null for blank, missing or duplicate IDs.                                                                                                                                          | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryReserve(PassengerAccess owner)``                                                         | Reserves a seat for an identified access/request owner without establishing occupancy.                                                                                                                                      | ``owner`` — Unity/application owner whose identity controls this relationship or resource. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateJointSupport(string jointId, Action<PassengerJointSupport> update)``                  | Invokes the callback on uniquely resolved settings. Null callbacks or unresolved IDs return false. Clears runtime tracking even if the callback throws; exceptions propagate. Changes apply on the next step.               | ``jointId`` is the occupant’s exact anatomical ID, where present. Boolean methods report success.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateTransformSupport(string id, Action<PassengerTransformSupport> update)``               | Edits a unique entry and refreshes in finally; false for unresolved IDs or null callbacks. Exceptions propagate. Renaming the ID changes subsequent lookup; duplicate edits make ID lookup ambiguous.                       | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateTransformSupport(Transform bodyTransform, Action<PassengerTransformSupport> update)`` | Updates a unique entry and refreshes in finally; false for missing/duplicate entries or null callback. Callback exceptions propagate.                                                                                       | —                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--per-limb-release-and-inspector-callbacks:

Per-limb release and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| API                                                                           | Contract                                                                                                               |
+===============================================================================+========================================================================================================================+
| ``public virtual bool ReleaseLimb(PassengerBodyPart part)``                   | Releases one eligible limb; false for invalid/already released/ineligible requests. Keeps authored mode/anchor/handle. |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBodyPart> onLimbReleased``                       | One callback per newly damage-released limb, under Passenger Seat > Signals and callbacks.                             |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onHandsReleased`` / ``onFeetReleased``     | Group outcome when both matching limbs have been damage-released, not a notification for every single limb.            |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerLimbDamageFeedback damageFeedback`` (on each limb config)   | Independent contact/tilt thresholds; see PassengerPhysics.                                                             |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerCollisionSurface[] releaseColliders`` (on each limb config) | Surface selection for this Free limb; empty by default.                                                                |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsReleasedByDamage`` / ``EffectiveMode`` (on each limb config)  | Runtime release latch and effective ownership; does not rewrite authored Mode.                                         |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

Seat Inspector callbacks are grouped under **Passenger Seat > Signals and callbacks**: On Before Enter, On Entered, On Before Exit, On Exited, On Before Eject, On Ejected, On Controller Changed, On Reset Requested, On Limb Released, On Hands Released and On Feet Released. The Passengers core exposes its vehicle-wide before/entered/exited/ejected callbacks under **Passengers > Signals and callbacks**. Select dynamic arguments matching the event's actual payload; C# Before/After context hooks remain available separately.

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Declaration                                                        | Usage                                                                                             |
+====================================================================+===================================================================================================+
| ``public UnityEvent<PassengerBody> onBeforeEnter``                 | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onEntered``                     | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onBeforeExit``                  | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody, PassengerExitReason> onExited`` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onBeforeEject``                 | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onEjected``                     | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerControllerType> onControllerChanged`` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onResetRequested``              | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onHandsReleased``               | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onFeetReleased``                | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengerseatcontext:

PassengerSeatContext
--------------------

**Runtime/World/Passengers/Seats/PassengerSeatContext.cs**

Immutable value snapshot for seat/core/access lifecycle notifications. References identify the original operation even after detachment or access Target cleanup. Vehicle can be null for a standalone passenger core. Referenced Unity objects can subsequently be destroyed; this is not a deep copy.

.. _uvs-api-passengercontrollers--state-and-configuration-16:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                              | Meaning                                                                                                                                           |
+=====================================================+===================================================================================================================================================+
| ``public PassengerExitReason? ExitReason { get; }`` | Null for entry; release reason for exit/ejection.                                                                                                 |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBody Passenger { get; }``         | Original actor.                                                                                                                                   |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool PreservePose { get; }``               | Requested preserve-pose policy; true for animated exit's seat-release operation.                                                                  |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerSeat Seat { get; }``              | Original seat, retained after the actor leaves.                                                                                                   |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController Vehicle { get; }``       | Original owning vehicle, or null for a standalone core.                                                                                           |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 VelocityChange { get; }``          | Requested world-space ejection velocity change; zero for ordinary exits and direct TryExit(Ejected). Custom mode does not apply it automatically. |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-14:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                                                                                                    | Role and behavior                                                                                 | Arguments and result                                                                                                                                                                        |
+==============================================================================================================================================================================================================+===================================================================================================+=============================================================================================================================================================================================+
| ``public PassengerSeatContext(VehicleController vehicle, PassengerBody passenger, PassengerSeat seat, PassengerExitReason? exitReason = null, Vector3 velocityChange = default, bool preservePose = false)`` | Captures operation identities and release parameters without a managed event-argument allocation. | vehicle/passenger/seat identify the operation; exitReason is null for entry; velocityChange is the world-space ejection delta in m/s; preservePose reports the requested detachment policy. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengertransformsupport:

PassengerTransformSupport
-------------------------

Serializable settings in **Runtime/World/Passengers/Seats/PassengerTransformSupport.cs**. Each binding independently chooses Spring or Parent with any controller or physics state. See :ref:`setup and lifecycle <uvs-seats--main-attachment-and-rigid-transform-supports>`.

.. _uvs-api-passengercontrollers--state-and-configuration-17:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                  | Meaning                                                                                                                                                                                                               |
+=========================================+=======================================================================================================================================================================================================================+
| ``public bool active``                  | Enable this binding; default true.                                                                                                                                                                                    |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform anchor``             | Vehicle anchor outside the passenger hierarchy.                                                                                                                                                                       |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform bodyTransform``      | Root or child transform from Body or Body Prefab; prefab references resolve on the occupant.                                                                                                                          |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float damper``                 | Position damping; default 20.                                                                                                                                                                                         |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool followAnchorRotation``    | Default true: follow the live anchor rotation. False: capture the target world rotation on bind/refresh and hold/spring toward it, while position still follows. Preserve World Pose and Rotation Offset still apply. |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string id``                    | Optional unique ID / Label, also shown in the Inspector entry header. Ordinal case-sensitive API lookup; blank keeps transform-only access.                                                                           |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool makeKinematic``           | Parent mode temporarily parks only this transform's Rigidbody; default true.                                                                                                                                          |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerAttachmentMode mode`` | Independent binding mode; default Parent.                                                                                                                                                                             |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 positionOffset``       | Anchor-local position offset; default zero.                                                                                                                                                                           |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool preserveWorldPose``       | Capture current anchor-relative pose before adding offsets; default false.                                                                                                                                            |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rotationDamper``         | Angular damping; default 20.                                                                                                                                                                                          |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 rotationOffset``       | Anchor-local Euler rotation offset in degrees; default zero.                                                                                                                                                          |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rotationSpring``         | Angular stiffness; default 120.                                                                                                                                                                                       |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spring``                 | Position stiffness; N/m on dynamic rigidbodies, unit virtual mass for transform simulation. Default 120.                                                                                                              |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--passengertype:

PassengerType
-------------

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Defines the allowed passenger type choices used by this topic.

.. _uvs-api-passengercontrollers--values-2:

Values
~~~~~~

-  ``HumanoidDriver``
-  ``HumanoidPassenger``
-  ``Custom``

.. _uvs-api-passengercontrollers--ragdollphysicspassengercontroller:

RagdollPhysicsPassengerController
---------------------------------

**Runtime/World/Passengers/Controllers/RagdollPhysicsPassengerController.cs**

Configuration/implementation type for ragdoll physics passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <uvs-api-passengercontrollers--passengercontroller>`.

.. _uvs-api-passengercontrollers--state-and-configuration-18:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+--------------------------------------------------------------------+
| Member                                                    | Meaning                                                            |
+===========================================================+====================================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``RagdollPhysicsPassengerController``. |
+-----------------------------------------------------------+--------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--methods-15:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                           | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=====================================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``             | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(PassengerBody body, Passengers core, float deltaTime)`` | Calls the admitted body's ``StepSeated`` through the physical passenger path.                                       | ``body`` — Character or rigidbody context, according to the declared type. ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                    |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--riderblendsource:

RiderBlendSource
----------------

**Runtime/World/Passengers/Seats/BalanceRider.cs**

Select the source of the rider’s Ground-to-Riding transition. It affects only feet using SpeedBlend.

-  ``Speed``: Speed magnitude between Lift Starts At and Fully Raised At requests progress from zero to one.
-  ``Manual``: Manual Riding Blend requests progress from zero to one. Your animation/input logic can update it at runtime.

.. _uvs-api-passengercontrollers--riderfootmode:

RiderFootMode
-------------

**Runtime/World/Passengers/Seats/BalanceRider.cs**

Select how one foot follows the rider’s authored transforms. An assigned foot Handle retains priority, and missing required transforms leave the ordinary Seat binding intact.

-  ``SpeedBlend``: Blend between Ground and Riding using the resolved RidingBlend. Requires both poses.
-  ``Riding``: Follow the Riding transform directly, including a moving pedal or deck anchor.
-  ``Ground``: Follow the Ground transform directly.
-  ``Unchanged``: Leave the foot’s ordinary Seat binding intact.

.. _uvs-api-passengercontrollers--rideranimationrule:

RiderAnimationRule
------------------

**Runtime/World/Passengers/Riding/RiderAnimator.cs**

See :ref:`rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>` for configuration and examples.

+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Member                                    | Meaning                                                                                                 |
+===========================================+=========================================================================================================+
| ``public RiderMotionCondition condition`` | Rider condition controlling this rule. Angle conditions use the signed range below.                     |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public string actionName``              | Unique action name for a Custom condition. Control it with SetActionActive, PlayAction and StopAction.  |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float minimumAngle``             | Inclusive minimum signed steering/lean angle in degrees.                                                |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float maximumAngle``             | Inclusive maximum signed steering/lean angle in degrees.                                                |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float angleHysteresis``          | Extra degrees retained around an active angle range, preventing repeated events at its boundary.        |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float feetBlendThreshold``       | Feet Raised is true above this blend; Feet Lowered below it.                                            |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public string boolParameter``           | Optional Animator bool held while the condition is active.                                              |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public string enterTrigger``            | Optional Animator trigger fired once when this condition begins.                                        |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public string exitTrigger``             | Optional Animator trigger fired once when this condition ends.                                          |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public string state``                   | Optional full Animator state path crossfaded on entry. Empty leaves state selection to your controller. |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public int layer``                      | Animator layer for the optional state.                                                                  |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float fadeSeconds``              | Crossfade duration in seconds for the optional state.                                                   |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onEntered``           | Condition began, including angle-range transitions. Can call custom animation code.                     |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onExited``            | Condition ended or the occupant/binding was released.                                                   |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--rideranimator:

RiderAnimator
-------------

**Runtime/World/Passengers/Riding/RiderAnimator.cs**

See :ref:`rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>` for configuration and examples.

+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Member                                                                                  | Meaning                                                                                                                 |
+=========================================================================================+=========================================================================================================================+
| ``public BalanceRider rider``                                                           | Balance Rider supplying steering, lean, foot and occupancy signals.                                                     |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public Animator animator``                                                            | Optional explicit Animator. Empty follows the occupant's seated animation source, including ragdoll animation sampling. |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public string speedParameter``                                                        | Optional float parameter for forward speed in m/s.                                                                      |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public string steeringParameter``                                                     | Optional signed steering angle float in degrees.                                                                        |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public string leanParameter``                                                         | Optional motorcycle lean float in degrees.                                                                              |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public string feetParameter``                                                         | Optional feet Ground-to-Riding blend float from zero to one.                                                            |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public string phaseParameter``                                                        | Optional normalized alternating step phase float.                                                                       |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public RiderAnimationRule[] rules``                                                   | Independent conditions, angle bands, bools, triggers, state crossfades and custom callbacks.                            |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public void RefreshBindings()``                                                       | Rebind after changing names, rules, controller or rider.                                                                |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public bool SetActionActive(string actionName, bool active)``                         | Set a named Custom condition without restarting unchanged state. Returns false if unavailable or unknown.               |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public bool PlayAction(string actionName)``                                           | Retrigger the named custom action.                                                                                      |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public bool StopAction(string actionName)``                                           | End the named custom action.                                                                                            |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``public bool PlayAnimation(string stateName, int layer = 0, float fadeSeconds = .2f)`` | Crossfade to an existing Animator state; false for missing Animator/state/layer.                                        |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-passengercontrollers--ridermotionstate:

RiderMotionState
----------------

**Runtime/World/Passengers/Riding/RiderMotionState.cs**

See :ref:`rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>` for configuration and examples.

+----------------------------------+------------------------------------------------------------+
| Member                           | Meaning                                                    |
+==================================+============================================================+
| ``public bool seated``           | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public bool grounded``         | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public bool footPushing``      | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public bool reversing``        | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public bool leftFootPlanted``  | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public bool rightFootPlanted`` | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public float speed``           | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public float steeringAngle``   | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public float leanAngle``       | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public float ridingBlend``     | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+
| ``public float stepPhase``       | Rider motion configuration or signal; see the setup guide. |
+----------------------------------+------------------------------------------------------------+

.. _uvs-api-passengercontrollers--ridermotioncondition:

RiderMotionCondition
--------------------

**Runtime/World/Passengers/Riding/RiderMotionState.cs**

``Seated``, ``Grounded``, ``Airborne``, ``SteeringAngle``, ``LeanAngle``, ``FeetRaised``, ``FeetLowered``, ``FootPushing``, ``Reversing``, ``LeftFootPlanted``, ``RightFootPlanted``, ``Custom``. See :ref:`rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>`.

.. _uvs-api-passengercontrollers--riderpushfeet:

RiderPushFeet
-------------

**Runtime/World/Passengers/Riding/RiderMotionState.cs**

``Both``, ``Left``, ``Right``, ``Disabled``. See :ref:`rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>`.

.. _uvs-api-passengercontrollers--riderreversemode:

RiderReverseMode
----------------

**Runtime/World/Passengers/Riding/RiderFootDrive.cs**

``ReverseGear``, ``FootPushing``. See :ref:`rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>`.
