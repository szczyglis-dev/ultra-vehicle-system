.. _uvs-passengers--passengers:

Passengers
==========

``Passengers`` is the vehicle's coordinator for seats, seated behaviors and handle updates. A ``PassengerSeat`` owns one occupancy slot; a ``PassengerBody`` is the character that can occupy it. The seat's controller mode determines who owns that body's attachment and pose.

This page covers creating seats, choosing controllers and managing occupants. Prepare physical characters in :doc:`Human anatomy </HumanAnatomy>`, fit their body support in :doc:`Seats </Seats>` and limb targets in :doc:`Handles </Handles>`, and add animated boarding through :doc:`Passenger access </PassengerAccess>`.

.. _uvs-passengers--access-the-passenger-system-from-a-vehicle:

Access the passenger system from a vehicle
------------------------------------------

``vehicle.passengers`` returns the first registered ``Passengers`` module, or ``null`` if none is registered. It uses the same module lookup as ``vehicle.TryGetModule<Passengers>(out ...)``; it includes disabled modules and does not add or enable one. Call it after vehicle initialization/registration. ``Passengers.TryEnter`` still checks whether the module is enabled. If an integration deliberately registers multiple cores, use ``vehicle.GetModules<Passengers>(buffer)`` to select the intended one.

**Example:** ``VehiclePassengerShortcutExample.cs``

.. raw:: html

   <!-- example: VehiclePassengerShortcutExample.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public sealed class VehiclePassengerShortcutExample : MonoBehaviour
       {
           public VehicleController vehicle;
           public PassengerBody character;
           public PassengerSeat selectedSeat;

           public bool EnterImmediately()
           {
               var passengers = vehicle ? vehicle.passengers : null;
               return passengers && character && passengers.TryEnter(character, selectedSeat);
           }

           public bool ExitImmediately()
           {
               var passengers = vehicle ? vehicle.passengers : null;
               return passengers && character && passengers.TryExit(character);
           }
       }
   }

For animated boarding, select a seat's ``SeatAccess`` and call the character's ``PassengerAccess.TryEnter(accessPoint)``. For immediate departure use ``vehicle.passengers.TryExit(character)`` after checking the shortcut for null. See :ref:`the step-by-step access setup <uvs-passengeraccess--tutorial-built-in-humanoid-boarding>`.

Inspector paths in this manual include the component and every enclosing header/foldout, for example **Passenger Seat > Hands, feet and head > Left Hand > Damage feedback > Release On Collision**. Headers are visual groups; expand only groups with a foldout arrow.

.. _uvs-passengers--add-an-occupant:

Add an occupant
---------------

1. Select the vehicle and open **VehicleController > Modules > Add module... > Base > World**. Add ``Passengers`` if it is not already installed.
2. Open **VehicleController > Seats** and add a Passenger Seat. Keep seats under this vehicle's Passengers hierarchy; nested vehicles have independent ownership.
3. Give the seat a useful **Seat Id**, such as ``Driver`` or ``RearLeft``, and choose its **Passenger Type**. Use distinct IDs in your application; the role/ID itself does not select a player input source.
4. Create a **Spine Anchor** at the seated pelvis origin, with local +Y up and +Z forward. Assign it to the seat. A detailed fitting workflow is in :ref:`Seat support <uvs-seats--fit-the-seated-body>`.
5. Choose the body source and controller mode below.
6. For initial testing, set limb modes deliberately rather than leaving incorrect handle assignments from another vehicle. Fit those targets in the seat guide.
7. For Ragdoll Physics, preview the pose. For animated/externally posed characters, check the actual animation in Play Mode. Confirm the seat's ``Occupant`` is the intended body. Test with the vehicle stationary before adding acceleration or collision feedback.

If modules were added directly through Unity rather than the controller, use **Discover and order vehicle modules** and **Apply vehicle configuration**. The package discovers seats and handles inside the owned hierarchy; it does not claim seats beneath a different nearest VehicleController.

**Select** beside a passenger or IK panel selects its scene GameObject in the Hierarchy. If the seat has only a prefab template and no spawned instance yet, the scene Select button is disabled; enter Play Mode/spawn the occupant or assign a pre-placed Body.

.. _uvs-passengers--pre-placed-body-or-spawned-prefab:

Pre-placed body or spawned prefab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------+
| Setup                                | Configure                                                 | Intended use                                                             |
+======================================+===========================================================+==========================================================================+
| Pre-placed character                 | Assign **Body**                                           | A character already present in the scene, or deterministic pose previews |
+--------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------+
| Character created by the seat        | Leave Body empty, assign **Body Prefab**                  | A vehicle prefab that brings its own driver/passengers                   |
+--------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------+
| Character created by the application | Keep the application-owned instance and call ``TryEnter`` | A player character, pooled NPC or network-managed character              |
+--------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------+

A pre-placed Body takes priority over Body Prefab. Automatic startup spawning requires **Spawn On Start** on both the core and that seat. An occupied seat cannot spawn a second occupant. Disabling startup spawning does not prevent an explicit ``Spawn()`` or ``TryEnter()`` request.

A body prefab must contain the appropriate ``PassengerBody`` implementation, not merely an Animator or mesh. Use the same prepared character prefab in several seats; each spawned instance still has independent state. Assign pre-placed instances separately so two seats do not compete for the same character.

**Custom** controller mode does not instantiate Body Prefab through ``Spawn``: the application creates the character and supplies it. Automatic core startup also skips Custom seats; explicitly supplying/entering a pre-placed Body is still possible. Keep character creation and ownership in the application for that mode.

.. _uvs-passengers--choose-a-controller:

Choose a controller
-------------------

+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Mode                                                                               | Package responsibility                                                                              | What the application supplies                                    |
+====================================================================================+=====================================================================================================+==================================================================+
| :ref:`Ragdoll Physics <uvs-passengers--tutorial-physical-ragdoll-passenger>`       | Seated physical support and package humanoid posing/IK                                              | Prepared anatomical rig and reachable seat contacts              |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`Animator <uvs-passengers--tutorial-animated-passenger-without-ragdoll>`      | Controlled attachment while application animation poses the character                               | Animator controller, states and animation playback               |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`Animator + IK <uvs-passengers--tutorial-animation-with-hand-and-foot-ik>`    | Animation plus configured limb IK overlays without seated ragdoll                                   | Working humanoid animation and limb targets                      |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`Attach Only <uvs-passengers--tutorial-static-or-externally-posed-passenger>` | Attachment/placement without humanoid pose solving                                                  | A suitable pose/model or another pose owner                      |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`Custom <uvs-passengers--tutorial-application-owned-character>`               | Occupancy bookkeeping; application owns character handling; explicit support lists remain available | Spawning, hierarchy, pose, animation, physics and reset behavior |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

For a mannequin reacting physically to acceleration, choose Ragdoll Physics and use a prepared ``HumanoidPassenger``. For a pre-animated driver, start with Animator or Animator + IK. Attach Only suits a static/externally posed figure; it does not create a seated pose from a standing mesh. Custom is an integration boundary, not an automatic alternate ragdoll solver.

Use ``SetPassengerController`` for a runtime handover. It validates the new mode before detaching the old strategy and can reject a change during an access reservation/transition or when the body lacks required references. An occupied mode change is not a new entry: observe ``ControllerChanged`` rather than treating it as another Entered event.

Seat roles such as Humanoid Driver are descriptive. Entering a driver seat does not assign the vehicle's input source, camera or player authority. Connect those in your application when observing occupancy.

.. _uvs-passengers--passenger-mode-tutorials:

Passenger mode tutorials
------------------------

Choose the controller for **who animates/simulates the character**, then choose Attachment Mode for **how its main seating origin follows the vehicle**. Additional transform supports choose their own Spring/Parent mode. These choices are independent: an animated passenger can follow a spring, and a physical ragdoll can have rigidly parented bones.

+---------------------------------------------------------------------+----------------------+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Desired result                                                      | Passenger Controller | Main Attachment Mode              | Start here                                                                                        |
+=====================================================================+======================+===================================+===================================================================================================+
| Your own sitting animation, no seated ragdoll                       | Animator             | Parent                            | :ref:`Animated passenger <uvs-passengers--tutorial-animated-passenger-without-ragdoll>`           |
+---------------------------------------------------------------------+----------------------+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Your animation with package hand/foot contact                       | Animator + IK        | Parent                            | :ref:`Animation with IK <uvs-passengers--tutorial-animation-with-hand-and-foot-ik>`               |
+---------------------------------------------------------------------+----------------------+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Physical occupant reacting to driving                               | Ragdoll Physics      | Spring                            | :ref:`Physical ragdoll <uvs-passengers--tutorial-physical-ragdoll-passenger>`                     |
+---------------------------------------------------------------------+----------------------+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Physical occupant with a rigid pelvis and simulated remaining bones | Ragdoll Physics      | Parent                            | :ref:`Physical ragdoll <uvs-passengers--tutorial-physical-ragdoll-passenger>`                     |
+---------------------------------------------------------------------+----------------------+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Static figure, custom bone posing or an already-running animation   | Attach Only          | Parent                            | :ref:`Externally posed passenger <uvs-passengers--tutorial-static-or-externally-posed-passenger>` |
+---------------------------------------------------------------------+----------------------+-----------------------------------+---------------------------------------------------------------------------------------------------+
| An external character framework owns all character handling         | Custom               | Application-owned main attachment | :ref:`Application-owned character <uvs-passengers--tutorial-application-owned-character>`         |
+---------------------------------------------------------------------+----------------------+-----------------------------------+---------------------------------------------------------------------------------------------------+

.. _uvs-passengers--shared-setup-and-reference-names:

Shared setup and reference names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete :ref:`Add an occupant <uvs-passengers--add-an-occupant>` once before following a mode tutorial. Start with an enabled vehicle, its enabled Passengers module and one enabled Passenger Seat. For an automatic initial occupant, enable Spawn On Start on both core and seat and assign either Body or Body Prefab. For application-controlled entry, disable automatic spawning and supply your existing instance with ``seat.TryEnter(character)`` when ready.

The similarly named character and vehicle references are different:

+--------------------+------------------------------------+---------------------------------------------------------------------------------------------------+
| Reference          | Where to assign it                 | What it represents                                                                                |
+====================+====================================+===================================================================================================+
| Animator           | HumanoidPassenger on the character | The character's Animator component; use the intended Animator when the model has several          |
+--------------------+------------------------------------+---------------------------------------------------------------------------------------------------+
| Pelvis             | HumanoidPassenger on the character | Hips/pelvis bone, normally Humanoid **Hips**, not the upper torso's Spine bone                    |
+--------------------+------------------------------------+---------------------------------------------------------------------------------------------------+
| IK                 | HumanoidPassenger on the character | The optional HumanoidIK component; required for package limb IK, not ordinary Animator attachment |
+--------------------+------------------------------------+---------------------------------------------------------------------------------------------------+
| Spine Anchor       | PassengerSeat on the vehicle       | An empty vehicle transform at the desired seated pelvis origin, +Y up and +Z forward              |
+--------------------+------------------------------------+---------------------------------------------------------------------------------------------------+
| Body / Body Prefab | PassengerSeat on the vehicle       | A PassengerBody component on the scene character / character prefab root                          |
+--------------------+------------------------------------+---------------------------------------------------------------------------------------------------+

For a valid Humanoid Animator, the package can discover Hips and add/map HumanoidIK at runtime when references are empty. Assign the character's Animator and Pelvis explicitly when authoring to make the intended mapping clear. An automatically present IK component does not mean the Animator controller mode is applying limb IK.

Keep vehicle anchors outside the character's hierarchy. Use Pelvis to align a humanoid's hips; when it is unassigned, controlled attachment falls back to aligning the character root. A custom body adapter can define a different seating origin.

.. _uvs-passengers--tutorial-animated-passenger-without-ragdoll:

Tutorial: animated passenger without ragdoll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this for a driver or NPC whose sitting, steering, talking and idle motion comes from your Animator, with no seated ragdoll simulation. **Animator + Parent** is the simplest starting configuration for an animated figure rigidly carried by the vehicle.

1. Start with your animated character prefab. For a humanoid, configure its Humanoid Avatar and confirm your animation plays correctly before seating it. A clean animation-only model needs no ragdoll Rigidbodies, physical bone colliders or generated anatomical joints.
2. Add **Humanoid Passenger** to the character root. Assign **Animator** and set **Pelvis** to Hips. You do not need to add/configure HumanoidIK manually for this mode. If the model already includes a physical rig, keep its existing anatomical configuration valid; changing controller does not repair an incomplete ragdoll.
3. Assign that component to the seat's **Body** or **Body Prefab**. Select **Passenger Controller → Animator** and **Attachment Mode → Parent**.
4. Assign the vehicle's **Spine Anchor**. Adjust its position/orientation and, if needed, **Parent Position Offset / Parent Rotation Offset**. The anchor is the target for the character's pelvis, not the character's upper Spine bone.
5. Put your sitting clip/state in the character's Animator Controller. For an always-seated spawned NPC, that can be its starting state. For a walking player, switch into the seated state from your entry logic or occupancy events. The seat enables the Animator but does not choose a state or supply a sitting animation.
6. Normally disable **Apply Root Motion** for a seat-driven character. If you need root motion, integrate it deliberately with your attachment so animation does not repeatedly move the character away from the intended seating pose. Disable your ordinary walking/movement scripts while seated through your own character integration.
7. Initially leave **Passenger Seat > Custom supports > Transform Supports** and **Passenger Seat > Custom supports > Joint Supports** empty. Plain Animator mode leaves limb posing to animation; it does not overlay seat hand/foot IK merely because targets are assigned.
8. Enter Play Mode or call TryEnter. Confirm ``seat.Occupant`` is your character, the sitting animation plays, and the character follows the moving vehicle without falling or reacting as a ragdoll. Controlled attachment temporarily makes its passenger Rigidbodies kinematic, disables their contacts and restores the captured settings on detachment.
9. Call ``seat.TryExit()`` to verify release and restoration. Set **Exit Anchor** if you want normal immediate exit placement, and restore your walking state/movement in your integration. If you explicitly eject a prepared HumanoidPassenger, built-in ejection can activate its ragdoll; ordinary seated Animator mode itself does not simulate one.

To add a soft main follow instead, retain Animator and select **Attachment Mode → Spring**. Tune **Attachment Spring / Attachment Damper**. This simulates the attachment pose without requiring a ragdoll; it does not change who plays your animation.

.. _uvs-passengers--tutorial-animation-with-hand-and-foot-ik:

Tutorial: animation with hand and foot IK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this for an animated driver whose hands must remain on a moving steering wheel, yoke or lever, or whose feet should follow pedals while the body keeps playing animation.

1. Complete the Animator tutorial and confirm the seated clip works before adding IK.
2. Ensure the character has **HumanoidIK** and assign it to **HumanoidPassenger → IK**. With a Humanoid Avatar, map its bones using the :ref:`character mapping workflow <uvs-humananatomy--3-add-passenger-components-and-auto-fill-references>`. Only the component/bone mapping steps are needed for animation-only IK; you do not need to create a physical ragdoll for this controller. For a manual rig, supply the corresponding limb mappings and reference pose rather than assuming bone names will be recognized.
3. Select **Passenger Controller → Animator + IK**. Keep **Attachment Mode → Parent** for a rigid main seating origin, or choose Spring for soft root follow.
4. On the seat, select **IK Handle** for only the hands/feet that the package should position. Assign a compatible vehicle Handle or, with Handle empty, a direct Anchor. Follow :ref:`Bind a limb to a control <uvs-handles--bind-a-limb-to-a-control>` and keep the target within reach.
5. Set limbs that should remain controlled by the clip to **Animator**. For example, bind both hands to steering handles while the feet retain their animated pose. Configure fingers/palm fitting separately through :doc:`Hand grips </SteeringHandGrip>`.
6. Leave **Automatic Seated IK** enabled on HumanoidPassenger for the normal animation-then-IK LateUpdate path. For an application-owned animation pipeline, disable it and call ``SolveSeatedIK()`` after your animation evaluation.
7. Test in Play Mode with the controls moving. Confirm the body still plays its clip and only the selected limbs receive the overlay. Start with empty extra support lists: a rigid transform support applied to the same bone runs after ordinary passenger IK and can override its result.
8. Verify exit restores ordinary character behavior. This controller parks passenger Rigidbodies just like Animator; limb IK does not activate seated ragdoll physics.

.. _uvs-passengers--tutorial-physical-ragdoll-passenger:

Tutorial: physical ragdoll passenger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when the occupant should react physically to acceleration, braking, impacts or release/ejection. This mode needs a prepared physical character rather than only a mesh and Animator.

1. Prepare the character using :doc:`Human anatomy </HumanAnatomy>`: map Animator/Pelvis/IK, create the physical bodies/colliders and save the anatomical ConfigurableJoint configuration. Confirm Anatomical Joints and Ragdoll Bodies reference the intended bones before Play Mode.
2. On HumanoidPassenger, enable **Physical While Seated**. Assign the prepared character to the seat's Body or Body Prefab.
3. Select **Passenger Controller → Ragdoll Physics** and **Attachment Mode → Spring**. Ensure the seat belongs to a vehicle with its Rigidbody; the physical seated path needs that vehicle body.
4. Place Spine Anchor at the intended pelvis origin. Configure reachable hand/foot targets and use the :ref:`seated fitting workflow <uvs-seats--fit-the-seated-body>`. **Preview Seated Pose** is available for a pre-placed prepared Ragdoll Physics body; it does not preview the animation tutorials' sitting clips.
5. In Play Mode, start with a stationary vehicle. Tune pelvis/chest support through **Fine Tuning** before testing acceleration. Physical main Spring support uses the restraint settings; **Attachment Spring / Attachment Damper** are the non-physical main-follow settings.
6. Drive slowly, then test braking and impacts. Adjust :ref:`G-force limits <uvs-seats--g-force-limits>` and :ref:`collision/tilt response <uvs-seats--collision-and-tilt-response>` for the intended behavior. Whole-body ejection and release are separate from ordinary limb posing.
7. For a rigid pelvis with the rest of the ragdoll still simulated, switch the main **Attachment Mode → Parent**. **Parent Make Kinematic** affects only the held pelvis Rigidbody; it does not park the entire ragdoll. Torso seat springs are omitted in this configuration, while limb settings remain independent.
8. Add extra Spring/Parent transform supports only where needed, using the mixed-attachment tutorial below. Test reset, exit and ejection after adding them; parented physical bones still participate in your skeleton's existing anatomical connections.

Turning off **Physical While Seated** does not automatically choose or play a seated animation. For application animation without physical simulation, use Animator or Animator + IK instead.

.. _uvs-passengers--tutorial-static-or-externally-posed-passenger:

Tutorial: static or externally posed passenger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this for a figure already posed in a modelling tool, a statue/prop, a character posed by your own scripts, or an existing animation system that should keep its current activation state.

1. Put **HumanoidPassenger** on the model root as the built-in body adapter. Assign Pelvis if it should align a particular bone; otherwise controlled attachment uses the root. For another character implementation, provide a compatible PassengerBody adapter.
2. Assign it to Body or Body Prefab, then select **Passenger Controller → Attach Only** and **Attachment Mode → Parent**.
3. Set Spine Anchor and offsets to position the figure. Supply the actual seated pose yourself: Attach Only does not bend a standing mesh into a sitting character.
4. For a static figure, remove or disable unwanted animation and posing scripts yourself. Attach Only does not force an already-enabled Animator off; it leaves its activation state in application hands.
5. For script-driven posing, run your pose system while the seat carries the character. Its passenger Rigidbodies are still parked by controlled attachment; select Custom if your framework must retain full physics ownership.
6. Test entry, vehicle motion and exit. Choose main Spring if you want soft follow instead of rigid carrying. Add independent transform supports only when selected parts should have an additional attachment.

.. _uvs-passengers--tutorial-application-owned-character:

Tutorial: application-owned character
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when a player/NPC framework must retain control of spawning, hierarchy, animation and physics, and you want package occupancy, reservations and events without automatic character handling.

1. Add **CustomPassengerBody** to the application-owned character. Keep your existing locomotion, animation and physics setup. Use a custom PassengerBody subclass if your integration needs more character-specific behavior.
2. Select **Passenger Controller → Custom** on the seat. This mode does not require Spine Anchor and does not automatically attach or align the character to one. Main Attachment Mode does not take over its main pose.
3. Leave both extra support lists empty for occupancy-only behavior. Explicit Custom Transform Supports and valid dynamic joint supports still apply in Custom mode if you configure them; controller choice does not disable those independently requested bindings.
4. Create or acquire the character in your application. Automatic startup spawning skips Custom seats; assigning Body Prefab is not a spawning workflow for this mode.
5. Call ``seat.TryEnter(customBody)`` and check the returned boolean. Use entry hooks to suspend walking/possession or align the character according to your own framework. The seat records occupancy but does not play a clip, change Rigidbody modes or implement your character's movement.
6. Subscribe to the seat's lifecycle events to restore your framework on release. Handle ``ResetRequested`` if a vehicle reset should reposition or reinitialize the Custom occupant.
7. Call ``seat.TryExit()`` for normal release. Custom mode does not supply the built-in ejection impulse, walking animation or pooling/destruction policy; implement those in your integration if needed.

See the complete :ref:`custom character example <uvs-scripting-passengercontrollers--connect-a-custom-character>` and :ref:`hook ordering <uvs-passengers--before-and-after-hooks>` before connecting possession or collision changes.

.. _uvs-passengers--tutorial-mix-independent-attachments:

Tutorial: mix independent attachments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this to pin a hand or accessory, add a soft body/limb follow, or combine a physical ragdoll with selected rigid attachments. It works with every controller above, including Custom.

1. First make the main character/controller setup work with the extra support lists empty.
2. Add an entry to **Passenger Seat > Custom supports > Transform Supports**. Set **ID / Label** to a unique name such as ``LeftHand``, assign **Body Transform** from Body or Body Prefab, and assign a vehicle **Anchor** outside the character hierarchy. The same ID is the Inspector name and API identifier.
3. Choose that entry's own **Mode → Parent** or **Spring**. It is independent from the seat's main Attachment Mode. An explicit root/pelvis entry overrides the corresponding automatic main binding.
4. For Parent, choose **Make Kinematic**: enabled temporarily parks only this transform's Rigidbody, if present; disabled retains its dynamic simulation while the attachment enforces its pose. Other ragdoll bones keep their own physics state.
5. For Spring, tune position/angular spring and damping. Dynamic Rigidbodies receive forces/torques. Plain transforms and kinematic bodies use a simulated spring pose, so the same entry can work without a ragdoll.
6. Choose **Follow Anchor Rotation**. On follows the moving anchor's rotation. Off captures the target world rotation on attachment/refresh, while position still follows. Use **Preserve World Pose** to capture the current relative pose, or leave it off to target the anchor directly; add position/rotation offsets as needed.
7. Test in Play Mode. Extra bindings override ordinary animation/IK for their selected transforms. If the hand is meant to be posed by Animator + IK instead, remove/disable the competing transform binding rather than expecting both systems to select a pose automatically.
8. At runtime, look up the entry with ``seat.GetTransformSupport("LeftHand")``, toggle it with ``SetTransformSupportActive``, or edit through ``UpdateTransformSupport``. API add/remove/update/active methods refresh bindings; direct list/settings edits require ``RefreshTransformSupports()``. IDs are case-sensitive; blank or duplicate names do not resolve through the ID API.
9. Check reset and exit: original hierarchy, local pose/scale and any kinematic state changed by the support are restored. See :ref:`attachment tuning and lifecycle <uvs-seats--main-attachment-and-rigid-transform-supports>` for the full behavior and :ref:`the public API <uvs-api-passengercontrollers--passengerseat>` for signatures.

For an existing anatomical joint pivot, the separate **Passenger Seat > Custom supports > Joint Supports** list uses Anatomical Joint IDs and physical spring forces. It needs a dynamic joint Rigidbody to respond; the transform Spring list above also works with plain transforms and kinematic bones. See :ref:`joint support setup <uvs-seats--custom-ragdoll-joint-supports>`.

.. _uvs-passengers--fit-and-support-the-character:

Fit and support the character
-----------------------------

The seat owns pelvis/chest support and limb target selection; the character owns its anatomy. Follow :doc:`Seats </Seats>` to fit body support and collision release, and :doc:`Handles </Handles>` for limb ownership, compliant rests and foot pins. Use :doc:`Human anatomy </HumanAnatomy>` for joint preparation and :doc:`Hand grips </SteeringHandGrip>` for fingers and palm fitting.

Preview checks geometry. It does not prove that dynamic support, access animation or collision release will behave correctly during driving. Test each separately in Play Mode.

.. _uvs-passengers--seated-ragdoll-head-support:

Seated ragdoll head support
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Artificial head support is configured on every Passenger Seat and works with any drive profile, including Wheeled quads. Its angle convention and physical prerequisites are described under :ref:`Seated head support <uvs-seats--motorcycle-rider-support>`, together with seat fitting and restraint tuning.

.. _uvs-passengers--occupancy-and-entryexit:

Occupancy and entry/exit
------------------------

Use the appropriate operation for the lifecycle you need:

+--------------------------------------+-----------------------------------------------------------------------------------------------------+
| Operation                            | Meaning                                                                                             |
+======================================+=====================================================================================================+
| ``seat.Spawn()``                     | Use the seat's configured pre-placed body or instantiate its prefab when supported                  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``seat.TryEnter(body)``              | Attempt immediate occupancy with an existing body                                                   |
+--------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``passengers.TryEnter(body, seat)``  | Request a specific seat through the core; omitting the seat lets it find an available eligible seat |
+--------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``seat.TryExit()``                   | Normal immediate exit                                                                               |
+--------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``seat.Eject(velocityChange)``       | Release the occupant; built-in handling adds the supplied world velocity change                     |
+--------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``PassengerAccess.TryEnter/TryExit`` | Begin a coordinated boarding/leaving sequence; see the access guide                                 |
+--------------------------------------+-----------------------------------------------------------------------------------------------------+

A true return indicates the operation described by that method succeeded or was admitted. Animated access has its own later completion outcome; immediate occupancy methods do not play a walking/door animation.

Configure an **Exit Anchor** for normal immediate placement. Ejection is a physical release, not a normal exit pose. Disabling/destroying the seat or disabling the Passengers core releases its occupant; this does not destroy the detached character. The application decides whether it walks away, is pooled, remains as a ragdoll or is destroyed.

Use ``Entered`` and ``Exited`` on the seat or core to update player state, UI and camera ownership. Check the exit reason if normal exit, ejection and component shutdown should have different consequences. Remove subscriptions when your observer is disabled or rebound.

.. _uvs-passengers--before-and-after-hooks:

Before and after hooks
~~~~~~~~~~~~~~~~~~~~~~

``PassengerSeat`` and the owning ``Passengers`` core both expose ``BeforeEnter``, ``AfterEnter``, ``BeforeExit``, ``AfterExit``, ``BeforeEject`` and ``AfterEject``. Every delegate is ``Action<PassengerSeatContext>``. Subscribe to the seat for one slot or the core for all owned seats; subscribing to both observes the same operation twice.

+--------------------------------------+------------------------------------------------------------------------------------------------------+
| Context property                     | Use                                                                                                  |
+======================================+======================================================================================================+
| ``Vehicle``, ``Passenger``, ``Seat`` | Original operation identities, including after detachment; Vehicle can be null for a standalone core |
+--------------------------------------+------------------------------------------------------------------------------------------------------+
| ``ExitReason``                       | Null for entry, otherwise Exit/Ejected/Disabled/Destroyed                                            |
+--------------------------------------+------------------------------------------------------------------------------------------------------+
| ``VelocityChange``                   | Requested world-space ejection delta in m/s; zero for direct TryExit(Ejected)                        |
+--------------------------------------+------------------------------------------------------------------------------------------------------+
| ``PreservePose``                     | Requested exit policy, including animated exit's retained pose                                       |
+--------------------------------------+------------------------------------------------------------------------------------------------------+

Entry order: seat BeforeEnter → core BeforeEnter → attachment → existing seat/core Entered → seat AfterEnter → core AfterEnter. Exit uses the same ordering around detachment and the existing Exited events. The Before hooks run before the controller captures collision/body state, so added components and changed collider settings can participate in attachment.

``Eject(delta)`` and ``TryExit(Ejected)`` both publish BeforeEject → BeforeExit → detachment → AfterExit → optional velocity change → AfterEject (each hook is also forwarded to the core). The direct TryExit form does not call AddVelocity; Custom mode retains its existing no-impulse policy. Damage-triggered ejection and seated manual ragdoll activation use these same boundaries.

Already-invalid requests emit no Before/After pair. A Before observer can still invalidate an admitted request, or a custom attachment can return false: there is then no successful After event. Check the immediate API's boolean return and restore any application-owned preparations on failure. For animated access, use its separate context-bearing Cancelled notification for cleanup.

These are synchronous C# notifications, not veto delegates. Recursive occupancy/controller operations on the same seat are rejected while a Before/attachment/detachment operation is in progress. After and outcome notifications may start another operation once its transition is complete; ejection remains guarded through AfterExit and impulse application, so start a new operation from AfterEject. Subsequent observers must inspect live state when needed; the context retains the original operation identities. Do not throw from observers: exceptions propagate, and subsequent subscribers are not guaranteed to run. Unsubscribe when the observer is disabled or rebound.

The example owns one extra application collider and restores its original enabled state on exit or rejected immediate entry. It filters by character rather than assuming every seat occupant is the local player. Add any required character components in BeforeEnter, before the built-in attachment scans them.

**Example:** ``PassengerColliderHooks.cs``

.. raw:: html

   <!-- example: PassengerColliderHooks.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class PassengerColliderHooks : MonoBehaviour
       {
           public PassengerSeat seat;
           public PassengerBody passenger;
           public Collider extraCollider;
           private PassengerSeat subscribed;
           private bool prepared, wasEnabled;

           private void OnEnable()
           {
               subscribed = seat;
               if (!subscribed) return;
               subscribed.BeforeEnter += Prepare;
               subscribed.AfterExit += Released;
           }

           private void OnDisable()
           {
               if (subscribed) {
                   subscribed.BeforeEnter -= Prepare;
                   subscribed.AfterExit -= Released;
               }
               subscribed = null;
               RestoreCollider();
           }

           private void Prepare(PassengerSeatContext context)
           {
               if (context.Passenger != passenger || !extraCollider) return;
               wasEnabled = extraCollider.enabled;
               prepared = true;
               extraCollider.enabled = false;
               // context.Vehicle and context.Seat identify the vehicle and slot.
           }

           private void Released(PassengerSeatContext context)
           {
               if (context.Passenger == passenger) RestoreCollider();
           }

           private void RestoreCollider()
           {
               if (prepared && extraCollider) extraCollider.enabled = wasEnabled;
               prepared = false;
           }

           public bool Enter()
           {
               bool accepted = false;
               try { accepted = seat && passenger && seat.TryEnter(passenger); return accepted; }
               finally { if (!accepted) RestoreCollider(); }
           }
       }
   }

.. _uvs-passengers--runtime-changes-and-reset:

Runtime changes and reset
~~~~~~~~~~~~~~~~~~~~~~~~~

After adding/removing seats at runtime, call ``Passengers.RefreshPassengers()``. For handles, call ``vehicle.handles.Refresh()`` so its vehicle-wide registry matches the hierarchy. A module created in code must also be registered with the vehicle through the :doc:`module API </Scripting/Modules>`. Discovery of handles and registration of vehicle modules are separate operations.

A vehicle reset can restore a seated pose and collision-release state. With the relevant restraint option, a body ejected by damage can be reseated if still eligible; it is the existing body, not a duplicate spawn. An application-owned Custom occupant receives ``ResetRequested`` so the application decides its reset pose/state.

.. _uvs-passengers--collision-and-tilt-response:

Collision and tilt response
---------------------------

Configure automatic hand/foot release and whole-body ejection in the seat's restraints. Their setup, threshold meanings and restoration rules are centralized in :ref:`Seat collision and damage response <uvs-seats--collision-and-tilt-response>`. Occupancy observers should distinguish a limb becoming Free from the entire passenger exiting.

.. _uvs-passengers--extend-the-system:

Extend the system
-----------------

Use ``PassengerBehaviour`` for additional seated behaviors, ``PassengerBody`` for a different body implementation, or a custom seat/controller strategy for alternate attachment logic. For an existing character framework, start with Custom ownership and handle its reset/lifecycle explicitly instead of enabling two competing character controllers.

Read :doc:`Passenger scripting </Scripting/PassengerControllers>`, :doc:`Passenger physics </Scripting/PassengerPhysics>` and the :doc:`API </API/PassengerControllers>` for signatures, event payloads and extension contracts.

.. _uvs-passengers--verify-a-passenger-setup:

Verify a passenger setup
------------------------

+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Symptom                                           | First check                                                                                        |
+===================================================+====================================================================================================+
| No automatic occupant                             | Core/seat enabled, both startup flags, valid body source and compatible controller                 |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Another prefab never spawns                       | Assigned pre-placed Body has priority, or the seat is already occupied                             |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Character enters but stays standing               | Attach Only/Animator ownership or missing animation; seat attachment does not author a seated clip |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Hands/feet do not follow                          | Limb modes/targets and body/IK requirements in the seat guide                                      |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Runtime-created seat is ignored                   | RefreshPassengers and correct Passengers/vehicle hierarchy                                         |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Driver enters but keyboard/camera stays elsewhere | Application has not connected occupancy to input/camera authority                                  |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Body remains after exit                           | Expected lifecycle: detached character cleanup belongs to the application                          |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------+
