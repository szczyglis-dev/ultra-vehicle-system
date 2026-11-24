.. _uvs-scripting-passengercontrollers--passenger-occupancy-and-controllers:

Passenger occupancy and controllers
===================================

Passenger integration separates the fact that a seat is occupied from the way its character is controlled. ``PassengerSeat`` validates and owns occupancy. A controller strategy decides how an admitted body is attached, posed and advanced. The body adapter exposes the character that strategy operates on.

This separation lets an application retain its own character framework while using package seats, reservations and events. Choose the controller by ownership needs: native passenger physics, animation with limb overlays, simple attachment or application-owned behavior.

.. _uvs-scripting-passengercontrollers--implementation-map:

Implementation map
------------------

+-------------------------+---------------------------------------------------------------------------+
| Class                   | Responsibility                                                            |
+=========================+===========================================================================+
| ``CustomPassengerBody`` | Minimal body for application-owned Custom occupancy.                      |
+-------------------------+---------------------------------------------------------------------------+
| ``HumanoidPassenger``   | Connects humanoid rig, pose and physical passenger behavior.              |
+-------------------------+---------------------------------------------------------------------------+
| ``PassengerBody``       | Base character adapter used by seats and controller strategies.           |
+-------------------------+---------------------------------------------------------------------------+
| ``PassengerController`` | Defines per-seat attachment, detachment and stepping behavior.            |
+-------------------------+---------------------------------------------------------------------------+
| ``Passengers``          | Discovers owned seats and schedules passenger work after vehicle.handles. |
+-------------------------+---------------------------------------------------------------------------+
| ``PassengerSeat``       | Owns admission, occupancy, reservations and controller handover.          |
+-------------------------+---------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--operation-hooks:

Operation hooks
---------------

Seat and core Before/After notifications carry :ref:`PassengerSeatContext <uvs-api-passengercontrollers--passengerseatcontext>`, including Vehicle, Passenger, Seat and release parameters. See :ref:`hook ordering and the collider integration example <uvs-passengers--before-and-after-hooks>`. Use seat/core hooks for attachment and detachment; use PassengerAccess hooks when the whole door/motion sequence matters.

.. _uvs-scripting-passengercontrollers--seat-versus-character:

Seat versus character
---------------------

The body adapter is the character-facing half of the integration. It answers whether the body can enter and provides attachment/detachment behavior used by a strategy. The seat-facing half owns who occupies the seat and whether another operation has reserved it. Neither half should silently choose the application's active player.

Use ``HumanoidPassenger`` when the package should operate its mapped humanoid. Use ``CustomPassengerBody`` when an external framework keeps character hierarchy, physics and pose. For a new body subclass, inspect both ``CanEnter`` overloads and the attachment/detachment contract; admission should reject an incompatible strategy before it partially changes the character.

``CustomPassengerBody`` accepts Custom, and automatic spawn-on-start skips Custom. Instantiate that body in the application and request entry explicitly. Choose the seat's controller strategy before requesting entry. Runtime ``SetPassengerController`` is a handover operation and can fail for a busy or incompatible body; check the return instead of assuming the requested enum is already active. ``ControllerChanged`` reports a successful strategy change with the previous and new choices.

Think of the seat as the authority and the controller as its implementation choice. A strategy should not independently announce a second entry or maintain a competing occupied flag. This is especially important when switching a seated character from animation to physics: ownership changes, but there is still one seat and one occupant.

``PassengerType`` describes the seat's role, such as driver or passenger. ``PassengerControllerType`` describes how its occupant is managed. A custom player character can occupy a driver seat without requiring the package to take over its hierarchy or animation; the application must then connect possession and driving input itself.

``PassengerSeat`` owns occupancy, reservation, controller strategy and lifecycle events. ``PassengerBody`` owns the character-specific attachment/detachment/pose hooks. A new controller strategy instance belongs to each seat. ``PassengerType`` classifies the role; ``PassengerControllerType`` selects behavior.

+--------------------+------------------------------------------------------------------------+
| Controller         | Ownership                                                              |
+====================+========================================================================+
| ``RagdollPhysics`` | Physical/IK character path                                             |
+--------------------+------------------------------------------------------------------------+
| Animator           | Application animation on an attached character                         |
+--------------------+------------------------------------------------------------------------+
| ``AnimatorIK``     | Animation with configured limb IK overlays                             |
+--------------------+------------------------------------------------------------------------+
| ``AttachOnly``     | Parenting/alignment without humanoid posing                            |
+--------------------+------------------------------------------------------------------------+
| Custom             | Occupancy only; application owns character hierarchy, pose and physics |
+--------------------+------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--connect-a-custom-character:

Connect a custom character
--------------------------

The example selects the Custom strategy before requesting entry. Either operation can fail, so the result is returned to the caller. Do not update application possession merely because an ``Enter`` button was pressed; update it after successful admission or from the seat's occupancy event.

For Custom mode, decide explicitly what happens to the character's movement controller, camera, collisions and visible seated representation. The seat supplies occupancy coordination, not assumptions about those application systems. On exit, restore only state that the integration actually took ownership of.

Put ``CustomPassengerBody`` on your character, select Custom on the seat and assign the body below. Call ``Enter``/``Exit`` from the application. The boolean return is immediate occupancy admission, not an animated access completion.

**Example:** ``CustomCharacterOccupancy.cs``

.. raw:: html

   <!-- example: CustomCharacterOccupancy.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CustomCharacterOccupancy : MonoBehaviour
       {
           public PassengerSeat seat;
           public CustomPassengerBody character;

           public bool Enter()
           {
               if (!seat || !character || !seat.SetPassengerController(PassengerControllerType.Custom))
                   return false;
               return seat.TryEnter(character);
           }

           public bool Exit() => seat && seat.TryExit();
       }
   }

Handle ``Entered``/``Exited``/``ResetRequested`` to move or animate your character framework. The package does not add a seated pose, ejection impulse or automatic respawn to a Custom occupant.

.. _uvs-scripting-passengercontrollers--replace-the-seat-strategy-factory:

Replace the seat strategy factory
---------------------------------

Override ``CreatePassengerController`` when the existing enum choice should create an application-specific strategy. Returning the base factory result for other choices keeps them available. The created strategy instance belongs to that seat, so counters and captured state are not shared across unrelated seats.

The example calls ``base.Attach`` before recording success. A failed base attachment must not count as an admitted occupant. For a more extensive implementation, pair any acquired resources or subscriptions with ``Detach`` cleanup, and account for both ordinary exit and handover to another strategy.

Use a derived seat when a strategy needs application state while retaining occupancy validation/events. This example counts successful Custom attachments. Its controller extends the public Custom implementation, so it does not call package-internal body helpers.

**Example:** ``ApplicationPassengerSeat.cs``

.. raw:: html

   <!-- example: ApplicationPassengerSeat.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ApplicationPassengerSeat : PassengerSeat
       {
           protected override PassengerController CreatePassengerController(PassengerControllerType type)
               => type == PassengerControllerType.Custom
                   ? new CountingCustomController()
                   : base.CreatePassengerController(type);
       }

       public class CountingCustomController : CustomPassengerController
       {
           public int Attachments { get; private set; }

           public override bool Attach(PassengerBody body, PassengerSeat seat)
           {
               if (!base.Attach(body, seat)) return false;
               Attachments++;
               return true;
           }
       }
   }

Strategies do not publish seat occupancy events themselves. A complete replacement owns its attachment/cleanup work, while the seat retains admission and event ordering. See :doc:`access </Scripting/PassengerAccess>` for asynchronous boarding and :doc:`physics </Scripting/PassengerPhysics>` for dynamic occupants.

.. _uvs-scripting-passengercontrollers--custom-joint-support-api:

Custom joint support API
------------------------

Seat ``jointSupports`` entries are keyed by the occupant’s Anatomical Joint ID. ``GetJointSupport`` returns live settings; edit their spring, damper, target or caps directly, or use ``UpdateJointSupport``. These changes apply on the next passenger physics step, without rebuilding anatomical joints or re-entering the seat. ``SetJointSupportActive`` pauses one support; ``RemoveJointSupport`` deletes its configuration. An empty seat can be configured before a body enters.

See :ref:`custom joint support setup and example <uvs-seats--custom-ragdoll-joint-supports>` for a working knee-target example. ``TryGetJointSupportState`` reports the last calculated force, torque and world points while that support is valid. It returns false when the seat/occupant is unavailable, the entry is inactive, the target or joint cannot be resolved, or no support step has run. The snapshot is a calculated support contribution, not the ragdoll’s total joint load.

IDs use ordinal, case-sensitive matching. The API rejects blank or duplicate IDs. Direct Inspector/list edits remain supported; duplicate seat IDs, duplicate anatomical IDs, missing joints and missing targets are skipped safely. Changing settings does not require a refresh call. The list is empty by default; no additional position constraints are applied until entries are configured.

.. _uvs-scripting-passengercontrollers--independent-attachment-api:

Independent attachment API
--------------------------

Use ``SetAttachmentMode(PassengerAttachmentMode.Parent)`` before entry or during occupancy. Check its boolean result; busy access or incompatible attachment rejects the handover. Spring is the default. The mode does not change the selected controller or turn off a physical ragdoll. Each transform entry separately selects mode = PassengerAttachmentMode.Spring or Parent; springs also simulate plain/kinematic transforms. Parent can optionally make only the held Rigidbody kinematic. Explicit support lists work with every controller, including Custom. Additional bindings use transform references, not anatomical joint IDs; entries authored on Body Prefab resolve on the spawned occupant.

.. raw:: html

   <!-- example: RigidPassengerAttachment.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class RigidPassengerAttachment : MonoBehaviour
       {
           public PassengerSeat seat;
           public Transform passengerBone;
           public Transform vehicleAnchor;

           public bool Configure()
           {
               if (!seat || !seat.SetAttachmentMode(PassengerAttachmentMode.Parent)) return false;
               return seat.AddTransformSupport(new PassengerTransformSupport {
                   id = "passenger.hand",
                   followAnchorRotation = true,
                   mode = PassengerAttachmentMode.Parent,
                   makeKinematic = true,
                   bodyTransform = passengerBone,
                   anchor = vehicleAnchor,
                   positionOffset = new Vector3(0, 0.02f, 0)
               });
           }

           public void ReleaseBone()
           {
               if (seat) seat.SetTransformSupportActive("passenger.hand", false);
           }
       }
   }

Transform overloads operate on the configured bodyTransform reference; string overloads use the same single ID / Label displayed in the Inspector. Use UpdateTransformSupport("passenger.hand", support => support.followAnchorRotation = false) to capture a fixed world rotation on refresh. See :ref:`the detailed API <uvs-api-passengercontrollers--passengerseat>` and :ref:`attachment configuration <uvs-seats--main-attachment-and-rigid-transform-supports>`.

.. _uvs-scripting-passengercontrollers--rider-actions-and-foot-reversing:

Rider actions and foot reversing
--------------------------------

Configure the rider on the driver's seat; the same settings work with Motorcycle Profile or Wheeled Profile. Leave Motorcycle Profile Only disabled for other profiles.

.. raw:: html

   <!-- example: DocumentationPassengerControllers10Example.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   public sealed class DocumentationPassengerControllers10Example : MonoBehaviour
   {
       public BalanceRider rider;
       public RiderAnimator riderAnimator;
       public bool shouldLookBehind;

       public void RunExample()
       {
           rider.reverseMode = RiderReverseMode.FootPushing;
           rider.pushFeet = RiderPushFeet.Both; // Left or Right for a scooter.
           // MotionUpdated reports speed, foot-pushing and planted-foot state.

           // A Custom rule named LookBehind can select your own Animator state/parameters.
           riderAnimator.SetActionActive("LookBehind", shouldLookBehind);
           riderAnimator.PlayAction("LookBehind"); // Explicitly restart its entry.
           riderAnimator.StopAction("LookBehind");

           // Or crossfade directly to a state in the assigned controller.
           bool played = riderAnimator.PlayAnimation("Upper Body.LookBehind", 1, .2f);
       }
   }

Configure masks/layers in the Animator Controller or Passenger Animator Layers. The named action API returns false for an unknown action or disabled bridge; direct playback returns false when the Animator, layer or state is unavailable. Call RefreshBindings after changing the rule definitions. See :ref:`rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>`.

.. _uvs-scripting-passengercontrollers--runtime-presentation-swaps-and-custom-cameras:

Runtime presentation swaps and custom cameras
---------------------------------------------

**Passenger Seat > FPP Swap** can add the optional **Passenger Variants** helper. Assign **First Person > Prefab** and select independent passenger, attachment, limb and handle modes. **Swap On Interior Camera** follows an active UVS Interior view; **Restore Original On Exit/Eject** are independent. Ordinary exit restoration defaults to false, so FPP can leave directly. Enable it to hand animated departure to the original body and its configured PassengerAccess/AccessMotion. Ejection restoration defaults to true. Lifecycle disable/destroy never restores a parked body. Models must support their selected controller: an arms-only animated rig does not automatically become a complete physical ragdoll.

For custom exit motion, call ``seat.PrepareExitPresentation()`` before reserving the seat, then resolve ``seat.Occupant`` again. The call applies the configured restoration policy without detaching. Built-in ``PassengerAccess.TryExit()`` does this automatically and forwards an accepted request to the restored body's access adapter. If restoration is off, the departing variant becomes application-owned; the original remains parked for the next ``Spawn()``. If that same variant re-enters the same seat before the parked original is reused by Spawn, its presentation identity and controller/attachment policies are restored inside the entry transaction. FPP/TPP switching then continues to use the same two bodies. Outside lifetime remains application-owned; an unrelated entrant is never adopted as that variant. Direct ``SetFirstPerson(false)`` / ``RestoreOriginal()`` calls remain available to application-owned logic.

For a custom camera or any gameplay condition, call ``SetFirstPerson``, ``SetVariant`` or provide ``VariantSelector``. ``EvaluateCondition()`` commits immediately after your condition changes. ``ApplyVariantSettings()`` reapplies edited active policies; ``PrepareVariant()`` prewarms an inactive model; ``SetVariantInstance()`` uses your own instance. ``PassengerSeat.TryReplaceOccupant()`` is the lower-level entry point for an entirely application-owned policy. Listen to ``OccupantReplaced`` to update references; swaps do not fire boarding/exit events, and no pending handle action is replayed. Swap requests during boarding, reservation or another transaction are rejected so the caller can retry after completion.

.. _uvs-scripting-passengercontrollers--example-two-application-cameras-and-c-to-swap:

Example: two application cameras and C to swap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add this script to an always-active object. Assign **Variants**, **Third Person Camera** and **First Person Camera** in the Inspector; configure the seat's **FPP Swap > First-person body > Prefab** first. Leave **Swap On Interior Camera** disabled and do not install a ``VariantSelector``: this example owns the choice. Disable other camera-switching scripts, including the demo's C binding, while testing. Keep exactly one active AudioListener on a separate object; remove/disable listeners on these two cameras.

Start seated in the ordinary TPP body, with the TPP camera enabled and FPP camera disabled. C requests a presentation swap before changing the cameras. A rejected request (for example during boarding) leaves the view unchanged; press C again when access finishes. This uses no UVS camera types and works with your own camera positioning/follow scripts. It intentionally handles seated view changes only; your game decides the camera after exit.

.. raw:: html

   <!-- example: PassengerViewExample.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.InputSystem;
   using UltraVehicleSystem;

   public sealed class PassengerViewExample : MonoBehaviour
   {
       public PassengerVariants variants;
       public Camera thirdPersonCamera;
       public Camera firstPersonCamera;
       private bool firstPerson;

       private void Start()
       {
           ApplyCameras();
       }

       private void Update()
       {
           if (Keyboard.current != null && Keyboard.current.cKey.wasPressedThisFrame)
               SetFirstPerson(!firstPerson);
       }

       // Commit the view only after the seat accepts the corresponding body.
       public bool SetFirstPerson(bool value)
       {
           if (!variants || !thirdPersonCamera || !firstPersonCamera ||
               thirdPersonCamera == firstPersonCamera) return false;
           if (!variants.SetFirstPerson(value)) return false;
           firstPerson = value;
           ApplyCameras();
           return true;
       }

       private void ApplyCameras()
       {
           if (thirdPersonCamera) thirdPersonCamera.enabled = !firstPerson;
           if (firstPersonCamera) firstPersonCamera.enabled = firstPerson;
       }
   }

For live pose/support changes use ``SetSpinePose``, ``SetBodyPartTarget/Mode``, ``UpdateBodyPart``, joint/transform support APIs and ``RefreshPassengerSettings``. ``BalanceRider`` exposes lean, foot targets/modes and manual/speed blend setters.

.. _uvs-scripting-passengercontrollers--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed seats, bodies and controller strategies API </API/PassengerControllers>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-passengercontrollers--animatorikpassengercontroller:

AnimatorIKPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`AnimatorIKPassengerController <uvs-api-passengercontrollers--animatorikpassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                                |
+=========================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--animatorpassengercontroller:

AnimatorPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`AnimatorPassengerController <uvs-api-passengercontrollers--animatorpassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                                |
+=========================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--attachonlypassengercontroller:

AttachOnlyPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`AttachOnlyPassengerController <uvs-api-passengercontrollers--attachonlypassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                                |
+=========================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--balancerider:

BalanceRider
~~~~~~~~~~~~

:ref:`BalanceRider <uvs-api-passengercontrollers--balancerider>` gives the full declared contract.

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| Method                                                        | Role                                                                          |
+===============================================================+===============================================================================+
| ``public override bool AppliesTo(VehicleController vehicle)`` | Checks whether this passenger behavior should run for the supplied seat/role. |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public event Action<Vector2> BodyLeanChanged``              | Requested forward/side torso lean changes.                                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public event Action<PassengerBodyPart> FootLifted``         | A foot leaves its target support phase.                                       |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public override void ResetPassenger(Passengers core)``      | Resets this passenger behavior's state for the supplied seat.                 |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public event Action<float> RidingBlendChanged``             | The effective riding blend changes.                                           |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public UnityEvent<Vector2> onBodyLeanChanged``              | Inspector torso-lean callback.                                                |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBodyPart> onFootLifted``         | Inspector support-release callback.                                           |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public UnityEvent<float> onRidingBlendChanged``             | Inspector riding-blend callback.                                              |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

\| ``public event Action<RiderMotionState> MotionUpdated`` \| Rider motion configuration or signal; see the setup guide. \| \| ``public event Action<bool> FootPushingChanged`` \| Rider motion configuration or signal; see the setup guide. \| \| ``public event Action<PassengerBodyPart> FootPlanted`` \| Rider motion configuration or signal; see the setup guide. \| \| ``public UnityEvent<RiderMotionState> onMotionUpdated`` \| Current motion state after rider targets update. Suitable for custom animation integrations. \| \| ``public UnityEvent<bool> onFootPushingChanged`` \| Foot propulsion begins or stops; false is also published on disable or loss of occupancy. \| \| ``public UnityEvent<PassengerBodyPart> onFootPlanted`` \| A foot starts its planted phase. The two feet alternate while pushing backward. \|

+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                                                                           | Meaning                                                                                                                                                                       |
+==================================================================================================================================+===============================================================================================================================================================================+
| ``public virtual void SetBalanceSupport(bool enabled)``                                                                          | Enables/disables the existing bounded ragdoll torso support and clears its previous reference when the policy changes.                                                        |
+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetBodyLean(float forward, float steering)``                                                               | Sets desired forward lean (-60..60 degrees) and steering lean (-45..45 degrees), ignoring non-finite components. Uses existing support; does not directly rotate the vehicle. |
+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFootModes(RiderFootMode left, RiderFootMode right)``                                                    | Chooses ground/riding/speed-blend/unchanged policy independently for both feet. Invalid enum values leave both unchanged.                                                     |
+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFootTargets(Transform leftGround, Transform rightGround, Transform leftRiding, Transform rightRiding)`` | Releases old borrowed foot targets, assigns separate ground/riding anchors and binds the current rider again. Null anchors disable the corresponding optional target.         |
+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetGroundSupport(bool enabled)``                                                                           | Enables per-occupant ground support or retains riding foot targets; independent of driver-only propulsion.                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetRidingBlend(float value)``                                                                              | Selects Manual source and clamps the requested riding blend to 0..1. Existing Blend Speed still smooths the actual transition; ignores non-finite input.                      |
+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void UseSpeedBlend()``                                                                                          | Returns foot positioning to the authored speed-dependent blend policy.                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--custompassengerbody:

CustomPassengerBody
~~~~~~~~~~~~~~~~~~~

:ref:`CustomPassengerBody <uvs-api-passengercontrollers--custompassengerbody>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                |
+===========================================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerSeat seat)``                                       | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                               | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--custompassengercontroller:

CustomPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`CustomPassengerController <uvs-api-passengercontrollers--custompassengercontroller>` gives the full declared contract.

+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                             | Role                                                                                                                |
+====================================================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``                            | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--humanoidpassenger:

HumanoidPassenger
~~~~~~~~~~~~~~~~~

:ref:`HumanoidPassenger <uvs-api-passengercontrollers--humanoidpassenger>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                |
+===========================================================================================+=====================================================================================================================+
| ``public virtual void ActivateRagdoll()``                                                 | Hands the character to free skeletal physics, releasing seated pose ownership.                                      |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void AddVelocity(Vector3 velocityChange)``                              | Adds the supplied velocity change to the character bodies used by this body implementation.                         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool Attach(PassengerSeat seat)``                                       | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                               | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void DetachForTransition()``                                            | Releases seated ownership for an animated character handover while preserving the required transition pose.         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PrepareRagdollCollisions()``                                        | Prepares the character's skeletal collision exclusions and collision relays.                                        |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreviewAccessPose(PassengerSeat seat)``                             | Applies an access reference pose for character/seat authoring or transition preparation.                            |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReadAnatomicalJointSettings()``                                     | Reads saved native joint configuration into the character's runtime anatomical references.                          |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void ResetSeatedPose()``                                                | Restores the character's seated pose/support through the selected physical/animation path.                          |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreAccessReferencePose()``                                      | Restores the character pose retained for an access-motion handover.                                                 |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveSeatedIK()``                                                   | Applies the seated character's configured limb IK targets.                                                          |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void StepSeated(Passengers core, float deltaTime)``                     | Advances this body's seated behavior through its selected character path.                                           |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                 | Role                                                                                                                             |
+==================================================================+==================================================================================================================================+
| ``public event System.Action<HumanoidPassenger> AfterSeatedIK``  | Immediately after seated IK work. Payload: ``HumanoidPassenger``.                                                                |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<HumanoidPassenger> BeforeSeatedIK`` | Immediately before seated IK work. Payload: ``HumanoidPassenger``; custom pose inputs must respect the selected character owner. |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                          | Behavior                                                                                                                                                                                |
+=================================================================================================================+=========================================================================================================================================================================================+
| ``public virtual ConfigurableJoint GetAnatomicalJoint(string jointId)``                                         | Returns the native ConfigurableJoint for a unique live ID, or null when unresolved/ambiguous.                                                                                           |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetAnatomicalJoint(string jointId, out ConfigurableJoint joint)``                      | Returns true and the native ConfigurableJoint for a unique live ID; otherwise false and null. Lookup allocates no managed memory.                                                       |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetAnatomicalJointDefinition(string jointId, out HumanoidJointDefinition definition)`` | Returns the unique definition with a live joint for the case-sensitive ID; false/null for empty, missing, duplicate or destroyed entries.                                               |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateAnatomicalJoint(string jointId, System.Action<ConfigurableJoint> update)``          | Runs the callback on a uniquely resolved joint, then refreshes its cached anatomy/IK data. False for unresolved ID or null callback. Callback exceptions propagate after cache refresh. |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Method / event / callback                                                                | Role                                                                                                                     |
+==========================================================================================+==========================================================================================================================+
| ``public virtual void BlendIntoPhysics(float seconds, Transform referenceFrame = null)`` | See :ref:`HumanoidPassenger <uvs-api-passengercontrollers--humanoidpassenger>` for the declared lifecycle and arguments. |
+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                        | Meaning                                                                                                                                       |
+===============================================+===============================================================================================================================================+
| ``public virtual void RefreshSeatSettings()`` | Rebuilds seated limb physics/tuning in place or solves controlled seated IK. Does not teleport or reset the whole body. No-op while unseated. |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--ivehiclemodule:

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

.. _uvs-scripting-passengercontrollers--passengeranimatorlayers:

PassengerAnimatorLayers
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------+
| Method                                                        | Role                                                        |
+===============================================================+=============================================================+
| ``public void Apply()``                                       | Applies configured overlay weights to the current occupant. |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ``public void RefreshBindings()``                             | Restores previous weights and resolves bindings again.      |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ``public bool SetLayerEnabled(string layerName, bool value)`` | Mutes/restores a configured overlay.                        |
+---------------------------------------------------------------+-------------------------------------------------------------+
| ``public bool SetWeight(string layerName, float weight)``     | Sets a finite weight request for a configured overlay.      |
+---------------------------------------------------------------+-------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--passengerbehaviour:

PassengerBehaviour
~~~~~~~~~~~~~~~~~~

:ref:`PassengerBehaviour <uvs-api-passengercontrollers--passengerbehaviour>` gives the full declared contract.

+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Method                                                                          | Role                                                                          |
+=================================================================================+===============================================================================+
| ``public virtual bool AppliesTo(VehicleController vehicle)``                    | Checks whether this passenger behavior should run for the supplied seat/role. |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public sealed override void StepPassenger(Passengers core, float deltaTime)`` | Advances passenger work in the supplied seat/core context.                    |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--passengerbody:

PassengerBody
~~~~~~~~~~~~~

:ref:`PassengerBody <uvs-api-passengercontrollers--passengerbody>` gives the full declared contract.

+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                   | Role                                                                                                                |
+==========================================================================================+=====================================================================================================================+
| ``public virtual void AddVelocity(Vector3 velocityChange)``                              | Adds the supplied velocity change to the character bodies used by this body implementation.                         |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public abstract bool Attach(PassengerSeat seat)``                                      | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Detach(PassengerExitReason reason)``                              | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void DetachForTransition()``                                            | Releases seated ownership for an animated character handover while preserving the required transition pose.         |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetSeatedPose()``                                                | Restores the character's seated pose/support through the selected physical/animation path.                          |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepSeated(Passengers core, float deltaTime)``                     | Advances this body's seated behavior through its selected character path.                                           |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--passengercontroller:

PassengerController
~~~~~~~~~~~~~~~~~~~

:ref:`PassengerController <uvs-api-passengercontrollers--passengercontroller>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                            | Role                                                                                                                           |
+===================================================================================================+================================================================================================================================+
| ``public abstract bool Attach(PassengerBody body, PassengerSeat seat)``                           | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication.            |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public static PassengerController Create(PassengerControllerType type)``                        | Creates the built-in strategy for a ``PassengerControllerType``; seat factory overrides can substitute application strategies. |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.                    |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(PassengerBody body, Passengers core, float deltaTime)``                | Empty base passenger strategy step; derived strategies decide which body work they own.                                        |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--passengerhandlevariant:

PassengerHandleVariant
~~~~~~~~~~~~~~~~~~~~~~

:ref:`PassengerHandleVariant <uvs-api-passengercontrollers--passengerhandlevariant>` gives the full declared contract.

.. _uvs-scripting-passengercontrollers--passengermodule:

PassengerModule
~~~~~~~~~~~~~~~

:ref:`PassengerModule <uvs-api-passengercontrollers--passengermodule>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                            | Role                                                                                                                                              |
+===================================================================================================+===================================================================================================================================================+
| ``public virtual void PreparePassenger(Passengers core, PassengerSeat seat)``                     | Prepares this passenger behavior for an occupied seat.                                                                                            |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RenderPassenger(Passengers core)``                                          | Advances render-time passenger presentation owned by this behavior/core.                                                                          |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetPassenger(Passengers core)``                                           | Resets this passenger behavior's state for the supplied seat.                                                                                     |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public sealed override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Intentionally empty sealed module-pipeline entry point. Passenger-local work runs through ``StepPassenger``/``RenderPassenger`` under Passengers. |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                           | Advances passenger work in the supplied seat/core context.                                                                                        |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--passengers:

Passengers
~~~~~~~~~~

:ref:`Passengers <uvs-api-passengercontrollers--passengers>` gives the full declared contract.

+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                                                                                                     | Role                                                                                                      |
+============================================================================================================+===========================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                                              | Rebuilds the owned passenger seats, ordered handles and passenger-local behaviors.                        |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void PrepareOccupant(PassengerSeat seat)``                                                | Prepares a seat's occupant and its local handles/passenger behaviors.                                     |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshPassengers()``                                                                | Rebuilds the owned seat and passenger-behavior snapshot. Handles use vehicle.handles.Refresh().           |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetOccupants()``                                                                   | Resets eligible owned seated/released occupants through their seat lifecycle.                             |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``                 | Supplies commands to handles in order, then advances passenger modules and seats from the owned snapshot. |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody body, PassengerSeat seat = null)``                            | Routes an entry request through an owned seat/passenger selection and that seat's validation.             |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerBody body, PassengerExitReason reason = PassengerExitReason.Exit)`` | Requests immediate exit or starts animated departure, depending on the declaring owner.                   |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                                  | Role                                                                                                                                                                     |
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

+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Method / event / callback                                                         | Role                                                                                                       |
+===================================================================================+============================================================================================================+
| ``public UnityEvent<PassengerSeatContext> onBeforeEject``                         | See :ref:`Passengers <uvs-api-passengercontrollers--passengers>` for the declared lifecycle and arguments. |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeatContext> onBeforeEnter``                         | See :ref:`Passengers <uvs-api-passengercontrollers--passengers>` for the declared lifecycle and arguments. |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeatContext> onBeforeExit``                          | See :ref:`Passengers <uvs-api-passengercontrollers--passengers>` for the declared lifecycle and arguments. |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeatContext> onEjected``                             | See :ref:`Passengers <uvs-api-passengercontrollers--passengers>` for the declared lifecycle and arguments. |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeat, PassengerBody> onEntered``                     | See :ref:`Passengers <uvs-api-passengercontrollers--passengers>` for the declared lifecycle and arguments. |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerSeat, PassengerBody, PassengerExitReason> onExited`` | See :ref:`Passengers <uvs-api-passengercontrollers--passengers>` for the declared lifecycle and arguments. |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Member                                                                                | Meaning                                                       |
+=======================================================================================+===============================================================+
| ``public event Action<PassengerSeat, PassengerBody, PassengerBody> OccupantReplaced`` | Committed presentation-body replacement; see API for payload. |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--passengerseat:

PassengerSeat
~~~~~~~~~~~~~

:ref:`PassengerSeat <uvs-api-passengercontrollers--passengerseat>` gives the full declared contract.

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                                                            | Behavior                                                                                                                                                                                                                    |
+===================================================================================================================+=============================================================================================================================================================================================================================+
| ``public virtual bool AddJointSupport(PassengerJointSupport support)``                                            | Adds settings without requiring an occupant. Rejects null, blank IDs and duplicate IDs; an unresolved anatomical ID can be configured before entry.                                                                         |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool AddTransformSupport(PassengerTransformSupport support)``                                    | Adds a non-null entry with both references, rejects duplicate bodyTransform or nonblank ID, refreshes; true means accepted configuration, not necessarily a resolved binding.                                               |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterEject``                                                          | After ejected detachment and the requested built-in velocity change. Custom controllers retain their application-owned physics. Payload: immutable PassengerSeatContext.                                                    |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterEnter``                                                          | After successful attachment and existing Entered notifications. Payload: immutable PassengerSeatContext.                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterExit``                                                           | After detachment and existing Exited notifications. During ejection this precedes the extra velocity change. Payload: immutable PassengerSeatContext.                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeEject``                                                         | Before any ejection detachment, while the seat is still occupied. Payload: immutable PassengerSeatContext.                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeEnter``                                                         | After admission validation, before occupancy assignment and controller attachment. Occupant and Passenger.Seat are still empty. Payload: immutable PassengerSeatContext.                                                    |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeExit``                                                          | While the passenger still owns the seat, before detachment. Includes ordinary exit, ejection, disable and destruction. Payload: immutable PassengerSeatContext.                                                             |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeat, PassengerControllerType, PassengerControllerType> ControllerChanged``        | After a successful seat strategy handover. Payload: seat, previous controller type, new controller type; no extra entry/exit is synthesized.                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Eject(Vector3 velocityChange)``                                                             | Requests whole-occupant release through the seat's controller/body lifecycle.                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool EjectFromImpact(Vector3 velocityChange)``                                                   | Eject through the standard seat lifecycle and retain automatic reset/reseat ownership.                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> Entered``                                                                    | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat.                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody, PassengerExitReason> Exited``                                                | After occupancy is released. Payload identifies occupant and ``PassengerExitReason``; the core delegate also includes the seat.                                                                                             |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerBodyPartConfig GetBodyPart(PassengerBodyPart part)``                                    | Returns the seat configuration for a selected limb/body part.                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerJointSupport GetJointSupport(string jointId)``                                          | Returns the editable support settings, or null for an unresolved or ambiguous ID.                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerTransformSupport GetTransformSupport(string id)``                                       | Returns live settings for a unique ID, otherwise null.                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerTransformSupport GetTransformSupport(Transform bodyTransform)``                         | Returns live settings matching the configured reference, or null for missing/duplicate references. Use the prefab reference for prefab-authored entries.                                                                    |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool PrepareExitPresentation(PassengerExitReason reason = PassengerExitReason.Exit)``            | Applies the optional exit/ejection presentation policy before reservation or custom exit motion. Does not detach; resolve Occupant again afterward. Disable/destroy reasons do not activate parked bodies.                  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCollisionSettings()``                                                                | Reapplies the seat's collision policy to its current occupant.                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshTransformSupports()``                                                                | Restores existing bindings, resolves the current list and applies eligible entries. Empty seats retain settings; all occupied controller/physics combinations can apply explicit bindings.                                  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ReleaseLimb(PassengerBodyPart part)``                                                       | Releases one eligible limb; false for invalid/already released/ineligible requests. Keeps authored mode/anchor/handle.                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReleaseReservation(PassengerAccess owner)``                                                 | Releases a seat reservation belonging to the supplied reservation owner.                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RemoveJointSupport(string jointId)``                                                        | Removes the uniquely identified support and clears runtime support state. Returns false if unresolved.                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RemoveTransformSupport(string id)``                                                         | Removes a uniquely identified entry and refreshes; false for unresolved IDs.                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RemoveTransformSupport(Transform bodyTransform)``                                           | Removes all matching configured references and refreshes; false when none match.                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> ResetRequested``                                                             | When Custom occupancy receives a reset request. Payload: ``PassengerBody``; application owns the actual custom-character reset.                                                                                             |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreDamageFeedback()``                                                                   | Restores the eligible seated limb supports released by damage feedback.                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetAttachmentMode(PassengerAttachmentMode mode)``                                           | Reattaches an occupied built-in body without occupancy events; returns false for invalid modes, busy access/reservation, transitions or incompatible attachment. Rolls back a rejected attach. Custom only stores the mode. |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetCollisionExclusions(bool self, bool vehicle)``                                           | Sets seated self/vehicle collision exclusion policy and updates the occupied character.                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetJointSupportActive(string jointId, bool active)``                                        | Pauses/resumes one support without disabling the seat or changing anatomical joints. Changed state takes effect on the next physics step; deactivation invalidates diagnostics immediately.                                 |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetPassengerController(PassengerControllerType type)``                                      | Requests a validated strategy handover for the seat; an incompatible/busy handover can be rejected.                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(bool self, bool vehicle)``                                             | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(PassengerBodyPart part, bool self, bool vehicle)``                     | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetTransformSupportActive(string id, bool active)``                                         | Changes active state and refreshes when changed; false for unresolved IDs.                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetTransformSupportActive(Transform bodyTransform, bool active)``                           | Enables/disables a unique entry and refreshes when changed; false if unresolved/duplicate.                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Spawn()``                                                                                   | Creates/requests the configured passenger representation through the seat's spawn policy.                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                                           | Advances passenger work in the supplied seat/core context.                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger)``                                                         | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes.                                                                 |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger, PassengerAccess reservation)``                            | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes.                                                                 |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerExitReason reason = PassengerExitReason.Exit, bool preservePose = false)`` | Releases current occupancy through its active strategy and exit reason; it does not run an animated access sequence.                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetJointSupport(string jointId, out PassengerJointSupport support)``                     | Finds exactly one seat support for the case-sensitive anatomical ID. Empty, missing or duplicate IDs return false and null.                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetJointSupportState(string jointId, out PassengerJointSupportState state)``             | Returns the last applied support calculation while the same valid physical occupant, joint and anchor remain available. False/default before the first step, after removal/release or when disabled, invalid or ambiguous.  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetTransformSupport(string id, out PassengerTransformSupport support)``                  | Resolves one exact ordinal ID; false and null for blank, missing or duplicate IDs.                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryReserve(PassengerAccess owner)``                                                         | Reserves a seat for an identified access/request owner without establishing occupancy.                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateJointSupport(string jointId, Action<PassengerJointSupport> update)``                  | Invokes the callback on uniquely resolved settings. Null callbacks or unresolved IDs return false. Clears runtime tracking even if the callback throws; exceptions propagate. Changes apply on the next step.               |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateTransformSupport(string id, Action<PassengerTransformSupport> update)``               | Edits a unique entry and refreshes in finally; false for unresolved IDs or null callbacks. Exceptions propagate. Renaming the ID changes subsequent lookup; duplicate edits make ID lookup ambiguous.                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateTransformSupport(Transform bodyTransform, Action<PassengerTransformSupport> update)`` | Updates a unique entry and refreshes in finally; false for missing/duplicate entries or null callback. Callback exceptions propagate.                                                                                       |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onBeforeEject``                                                                | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onBeforeEnter``                                                                | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onBeforeExit``                                                                 | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerControllerType> onControllerChanged``                                                | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onEjected``                                                                    | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onEntered``                                                                    | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody, PassengerExitReason> onExited``                                                | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onFeetReleased``                                                               | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onHandsReleased``                                                              | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBodyPart> onLimbReleased``                                                           | One callback per newly damage-released limb, under Passenger Seat > Signals and callbacks.                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<PassengerBody> onResetRequested``                                                             | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering.                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                     |
+===============================================================================================================================================+=============================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public event Action<PassengerBodyPart> BodyPartChanged``                                                                                    | After a supported limb edit or individual damage-release recovery. Payload: affected hand/foot.                                                                                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody, PassengerBody> OccupantReplaced``                                                                        | Committed presentation-body replacement; see API for payload.                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshPassengerSettings()``                                                                                            | Reapplies directly edited limb support settings and transform/collision bindings without detaching or resetting the whole occupant. Busy transactions defer this operation.                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RestoreLimb(PassengerBodyPart part)``                                                                                   | Clears damage release for one hand/foot and refreshes its configured support without resetting the other limbs. Returns false if not released, invalid or busy.                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetAttachmentOffsets(Vector3 position, Vector3 rotation)``                                                              | Sets Parent seating-origin position/metre and rotation/degree offsets, then resets that attachment pose. Rejects non-finite values and busy state.                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetBodyPartMode(PassengerBodyPart part, PassengerBodyPartMode mode)``                                                   | Sets an arbitrary hand/foot control mode and refreshes the current occupant; false for invalid values or busy state.                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetBodyPartTarget(PassengerBodyPart part, Transform anchor, VehicleHandle handle = null)``                              | Replaces one limb anchor and optional handle. Does not change its authored mode; returns false for invalid part or busy state.                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHeadSupport(bool enabled, float pitch = 0)``                                                                         | Enables/disables physical head support and sets pitch clamped to -60..60 degrees. Uses the existing seat head spring, damping and torque limits.                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetSpineAnchor(Transform anchor)``                                                                                      | Replaces the seating origin and resets/rebuilds the current seated pose. Rejects null/self/descendant occupant anchors and busy state. Use moving existing anchors for continuous physical adjustment.                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetSpinePose(Vector3 localPosition, Quaternion localRotation)``                                                         | Sets the existing Spine Anchor local position/rotation, preserving its identity for physical supports. Rejects non-finite/zero quaternion values. Controlled occupants are repositioned immediately; dynamic supports follow their moved anchor.                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<Pose> SpinePoseChanged``                                                                                                | After SetSpinePose commits the new anchor-local pose. Payload: position in metres and normalized rotation.                                                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryReplaceOccupant(PassengerBody replacement)``                                                                         | Synchronously replaces the seated body without Entered/Exited events. Replacement must be active, unseated and compatible. Returns false while boarding/reserved/busy or on rejected admission; the previous occupant remains. On success the former body is inactive and unseated. Overload selects controller/attachment; the shorter overload retains current policies. Caller owns both body lifetimes. |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryReplaceOccupant(PassengerBody replacement, PassengerControllerType controller, PassengerAttachmentMode attachment)`` | Synchronously replaces the seated body without Entered/Exited events. Replacement must be active, unseated and compatible. Returns false while boarding/reserved/busy or on rejected admission; the previous occupant remains. On success the former body is inactive and unseated. Overload selects controller/attachment; the shorter overload retains current policies. Caller owns both body lifetimes. |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UpdateBodyPart(PassengerBodyPart part, Action<PassengerBodyPartConfig> update)``                                        | Edits the selected hand/foot configuration, cancels borrowed handle use and refreshes supports/collisions in place. Returns false for invalid part, null edit or a busy transaction. Edit exceptions propagate after refresh.                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--passengervariant:

PassengerVariant
~~~~~~~~~~~~~~~~

:ref:`PassengerVariant <uvs-api-passengercontrollers--passengervariant>` gives the full declared contract.

.. _uvs-scripting-passengercontrollers--passengervariants:

PassengerVariants
~~~~~~~~~~~~~~~~~

:ref:`PassengerVariants <uvs-api-passengercontrollers--passengervariants>` gives the full declared contract.

+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                              |
+==========================================================================================================================+======================================================================================================================================================================================================================================================================================================+
| ``public virtual bool ApplyVariantSettings()``                                                                           | Reapply the currently active profile after editing controller, attachment, limb or handle settings; false if blocked or rejected.                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ClearCachedVariants()``                                                                            | Destroys only unseated helper-created/explicitly owned instances. Retains the current seated variant and leaves application-owned bodies alive.                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool EvaluateCondition()``                                                                              | Evaluates VariantSelector immediately, or the built-in active UVS Interior condition when no selector is assigned. Returns success; false means no available/accepted switch.                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool PrepareVariant(PassengerVariant variant)``                                                         | Prewarms an inactive cached prefab instance without changing occupancy. Returns false outside Play, with invalid policy or without a prefab/registered instance.                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCameraBinding()``                                                                           | Rebinds the optional/vehicle camera core and immediately reevaluates built-in camera selection. Custom cameras use SetFirstPerson, SetVariant or VariantSelector instead.                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RestoreOriginal()``                                                                                | Restores the parked original and its borrowed controller, attachment, limb-mode and handle-mode policies in one transaction. True if already original; false if busy, original unavailable or admission rejected.                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetFirstPerson(bool enabled)``                                                                     | Selects the configured FPP profile when enabled is true; restores original when false. Returns whether the operation succeeded.                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetFirstPersonPrefab(PassengerBody prefab)``                                                       | Restores active FPP first, replaces its optional source and clears inactive caches. Returns false if restoration is blocked. Null disables prefab-based automatic FPP.                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetSeat(PassengerSeat value)``                                                                     | Restores any active original first, then rebinds the target seat. False if restoration is currently blocked.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetVariant(PassengerVariant variant)``                                                             | Selects any valid profile synchronously; null restores original. Retains the currently visible variant if the replacement is rejected. Supports cached registered instances without prefab. Requires an enabled helper and occupied seat. No rendered or physics step occurs between body handovers. |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetVariantInstance(PassengerVariant variant, PassengerBody instance, bool takeOwnership = false)`` | Registers an unseated application-created body for a profile, allowing prefab to be null. Optional takeOwnership lets cache cleanup destroy it; default keeps caller ownership. Rejects original, duplicate, seated and currently active-profile replacements.                                       |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetVariantBody(PassengerVariant variant, out PassengerBody body)``                              | Returns the cached/registered body for the profile, or false if unavailable. Does not spawn or activate it.                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerVariant, PassengerVariant> VariantChanged``                                               | After a successful presentation commit. Payload: previous and current variant; null denotes the original. A variant-owned exit also reports returning to the original policy, without respawning its parked body.                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--ragdollphysicspassengercontroller:

RagdollPhysicsPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`RagdollPhysicsPassengerController <uvs-api-passengercontrollers--ragdollphysicspassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                              | Role                                                                                                                |
+=====================================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``             | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(PassengerBody body, Passengers core, float deltaTime)`` | Calls the admitted body's ``StepSeated`` through the physical passenger path.                                       |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--rideranimationrule:

RiderAnimationRule
~~~~~~~~~~~~~~~~~~

:ref:`RiderAnimationRule <uvs-api-passengercontrollers--rideranimationrule>` gives the full declared contract.

+---------------------------------+-------------------------------------------------------------------------------------+
| Member                          | Behavior                                                                            |
+=================================+=====================================================================================+
| ``public UnityEvent onEntered`` | Condition began, including angle-range transitions. Can call custom animation code. |
+---------------------------------+-------------------------------------------------------------------------------------+
| ``public UnityEvent onExited``  | Condition ended or the occupant/binding was released.                               |
+---------------------------------+-------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--rideranimationrule-1:

RiderAnimationRule
~~~~~~~~~~~~~~~~~~

+---------------------------------+-------------------------------------------------------------------------------------+
| Member                          | Meaning                                                                             |
+=================================+=====================================================================================+
| ``public UnityEvent onEntered`` | Condition began, including angle-range transitions. Can call custom animation code. |
+---------------------------------+-------------------------------------------------------------------------------------+
| ``public UnityEvent onExited``  | Condition ended or the occupant/binding was released.                               |
+---------------------------------+-------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--rideranimator:

RiderAnimator
~~~~~~~~~~~~~

:ref:`RiderAnimator <uvs-api-passengercontrollers--rideranimator>` gives the full declared contract.

+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Member                                                                                  | Behavior                                                                                                  |
+=========================================================================================+===========================================================================================================+
| ``public bool PlayAction(string actionName)``                                           | Retrigger the named custom action.                                                                        |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public bool PlayAnimation(string stateName, int layer = 0, float fadeSeconds = .2f)`` | Crossfade to an existing Animator state; false for missing Animator/state/layer.                          |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public void RefreshBindings()``                                                       | Rebind after changing names, rules, controller or rider.                                                  |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public bool SetActionActive(string actionName, bool active)``                         | Set a named Custom condition without restarting unchanged state. Returns false if unavailable or unknown. |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public bool StopAction(string actionName)``                                           | End the named custom action.                                                                              |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--rideranimator-1:

RiderAnimator
~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Member                                                                                  | Meaning                                                                                                   |
+=========================================================================================+===========================================================================================================+
| ``public bool PlayAction(string actionName)``                                           | Retrigger the named custom action.                                                                        |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public bool PlayAnimation(string stateName, int layer = 0, float fadeSeconds = .2f)`` | Crossfade to an existing Animator state; false for missing Animator/state/layer.                          |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public void RefreshBindings()``                                                       | Rebind after changing names, rules, controller or rider.                                                  |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public bool SetActionActive(string actionName, bool active)``                         | Set a named Custom condition without restarting unchanged state. Returns false if unavailable or unknown. |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public bool StopAction(string actionName)``                                           | End the named custom action.                                                                              |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengercontrollers--vehiclemodule:

VehicleModule
~~~~~~~~~~~~~

:ref:`VehicleModule <uvs-api-modules--vehiclemodule>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                                   |
+===========================================================================================+========================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                          | Role                                                                                                              |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
