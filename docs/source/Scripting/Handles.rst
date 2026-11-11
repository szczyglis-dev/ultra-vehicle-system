.. _uvs-scripting-handles--limb-handles-and-transfers:

Limb handles and transfers
==========================

A handle is the passenger-facing description of a control or support target. It tells the passenger system where a hand or foot should make contact. Some handles also move that contact in response to input, such as a pedal travelling under the driver's foot. The seat owns the limb binding; the handle owns the contact geometry and control presentation.

Keep the contact and the mechanic separate. A throttle handle can move the cockpit lever while an input provider supplies propulsion intent to the engine. Replacing the lever model or hand pose then does not require replacing the engine. For a custom control, first decide whether you need a new target, a new motion mapping or a new gameplay action; these have different extension points.

For custom Animator/Timeline gestures, independent arm/finger weights and common contact/value events, follow :doc:`Custom handle animation and IK </HandleAnimation>`.

.. _uvs-scripting-handles--implementation-map:

Implementation map
------------------

+-------------------------------------------+-----------------------------------------------------------------------------------------+
| Class                                     | Responsibility                                                                          |
+===========================================+=========================================================================================+
| ``IHandle`` / ``VehicleHandle``           | Common contact, preparation, binding and input contract.                                |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``AnchorHandle``                          | Exposes authored hand/foot anchors without control animation.                           |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``SteeringWheelHandle`` / ``YokeHandle``  | Describes steering contacts, surface geometry and hand participation.                   |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``JoystickHandle``                        | Supplies authored joystick grip contacts; SteeringStickAnimator owns pitch/roll motion. |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``MotorcycleHandle``                      | Supplies fixed left/right contacts with prepared finger poses.                          |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``ThrottleHandle`` / ``ThrottleAnimator`` | Separate throttle palm contact and anchored model motion.                               |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``PedalHandle``                           | Supplies pedal foot/ankle geometry; PedalAnimator owns input and travel.                |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``HandleController`` / ``HandleUse``      | Per-vehicle registry, admission, exclusive limb ownership, travel and return.           |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``SwitchHandle``                          | Supplies switch palm contact; SwitchAnimator owns detents, travel and events.           |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| ``Passengers``                            | Updates occupants after the vehicle handle pass.                                        |
+-------------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-scripting-handles--tutorial-implement-your-own-contact:

Tutorial: implement your own contact
------------------------------------

1. Choose the smallest extension. Use AnchorHandle for a fixed target or an existing handle plus an animated **Target Override** when only the target moves. Implement a VehicleHandle subclass when contact selection itself is custom.
2. Add your subclass under the intended vehicle. Give **[Your handle] > ID** a unique case-sensitive PascalCase value and set **Allowed limbs**. Override ``GetAnchor(PassengerBodyPart)`` to return the correct world-space Transform or null when unsupported/unavailable.
3. Keep each target outside the character skeleton. Parent it under the moving control when contact follows model motion. Use an ankle frame for a foot, and the matching wrist/palm contact convention for the hand.
4. Implement ``SetInput(Command, float)`` only if the handle needs vehicle input for its contact logic. A separate control animator should own the mesh; avoid moving it again in GetAnchor, which can be queried more than once per frame.
5. Assign the component at **Passenger Seat > Hands, feet and head > [limb] > Handle**, with **Mode = IK Handle**. Check ``Supports(part)``/Allowed limbs as well as GetAnchor; returning a target does not override ownership admission.
6. Configure **Actions** only for temporary use. For programmatic transfers use ``vehicle.handles``, check admission and let it restore the home target. Do not directly parent a passenger wrist to the new control.
7. Configure pose/contact overlays under **Limb IK, animation and contact > [limb] Pose**. Observe **Signals and callbacks** for contact/value events instead of inferring contact solely from proximity.
8. For a runtime-created component call ``vehicle.handles.Refresh()`` after inserting it into the vehicle hierarchy. For a new control animator/module, register/discover that module separately. Removal/disable must stop your own resource ownership too.

The example below is a complete minimal contact class. It can be connected to a built-in control animator or your own presentation script; the handle itself does not need to know which animation framework moves the target.

.. _uvs-scripting-handles--handle-contract:

Handle contract
---------------

The seat asks its configured handle for a target for a specific ``PassengerBodyPart``. ``GetAnchor(part)`` returns a stable ``Transform``, or ``null`` if that part is unsupported. Moving the transform updates the target without replacing the binding. Creating a new target on every query would repeatedly invalidate contact identity and generate unnecessary objects.

Preparation has two levels. ``Prepare()`` establishes reusable handle geometry. ``BindBodyPart(part, ik, animator)`` prepares that geometry for the current occupant, including adaptive finger binding when enabled. Keep character proportions and calibration on the character; a handle should describe its control surface rather than assume one particular hand size.

``vehicle.handles`` discovers every handle belonging to that vehicle, including handles outside Passengers. Nested vehicles are excluded. The vehicle calls ``SetInput(command, deltaTime)`` in stable ``InputOrder``, then evaluates automatic requests and advances transfers at the Feedback phase, after resolved braking and before passenger solvers. Value-change events sampled in LateUpdate become eligible on the next physics tick. Do not advance these operations from another loop. Pedal visual animation retains its own render callback.

``HandDriven(left)`` indicates whether the physical hand should be guided, ``HandSteering(left)`` whether it participates in steering support, and ``HandContact(left)`` supplies contact participation. These are different questions: a travelling hand may remain guided while its locked surface contact is released. The bool ``left`` means left hand when ``true`` and right hand when ``false``.

.. _uvs-scripting-handles--connect-a-custom-target:

Connect a custom target
~~~~~~~~~~~~~~~~~~~~~~~

Use a ``VehicleHandle`` subclass when the application already knows where a palm should go. Place the component and its contact beneath the vehicle, assign it to the relevant seat limb, and let your animation or aiming system move the contact. The passenger system continues to own the limb; the application owns only the target pose.

**Example:** ``ApplicationPalmHandle.cs``

.. raw:: html

   <!-- example: ApplicationPalmHandle.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ApplicationPalmHandle : VehicleHandle
       {
           public Transform contact;

           public override Transform GetAnchor(PassengerBodyPart part)
               => isActiveAndEnabled && part == PassengerBodyPart.RightHand ? contact : null;
       }
   }

The example accepts only the right hand and returns ``null`` for other parts. Add separate left/right targets if both hands are supported. For a palm-contact binding, place the target on the palm's contact surface; for a foot, use the ankle frame expected by the limb configuration. A wrist pivot and a palm contact are not interchangeable positions.

.. _uvs-scripting-handles--runtime-handover:

Runtime handover
----------------

A limb configuration selects its mode, handle and optional direct anchor. Changing those choices rebuilds that limb's owned contact at the next applicable passenger pass. Other limbs and torso support remain in place. This is useful for changing a hand from a steering wheel to an auxiliary control without making the passenger exit and enter again.

Use ``vehicle.handles.TryUse(seat, limb, target, onArrival)`` for a timed out-and-back action. It returns a new ``HandleUse`` token, or null when admission fails. ``TryUse(seat, target)`` uses the preferred limb and, if enabled, other allowed limbs. An ID overload accepts a unique case-sensitive handle ID. ``Get(id)`` returns null for missing or duplicate IDs; ``TryGet`` returns false. Blank IDs remain accessible by component reference. Set IDs before Refresh; do not rename a registered ID without refreshing.

``TryAcquire`` gives an application-driven target persistent ownership until its token is cancelled. ``TryAcquireAnimator`` reserves the same limb and temporarily selects Animator mode. Tokens expose Phase, IsActive, Arrived, Completed and Cancelled; ``Return()`` requests a normal return, while ``Cancel()`` restores ownership immediately. An Animator acquisition completes immediately on Return because its clip owns the return presentation. Persistent acquisitions have no automatic arrival event. Keep the token with delayed application callbacks and check IsActive. Cancellation after commit does not undo the action.

Requests require an enabled seat and target on the same vehicle, a live occupant and an eligible, unreleased limb. Admission checks availability, not anatomical reach distance. **Minimum Attachments** preserves support on the source control. Requests are independent per seat/limb; a blocked request returns null. **Interrupt Lower Priority** permits replacing a lower-priority timed request, while persistent and Animator ownership stay protected. **Allow Unsupported Departure** bypasses the support minimum. Automatic requests retry while active; animated gestures start once per activation.

The controller saves the original handle, hold flag and mode. During travel it owns a transient geometry adapter; only that adapter supplies the intermediate target. On arrival it binds the actual destination for its grip configuration, then releases and returns after Return Delay. Coordinates are relative to the vehicle, so chassis translation/rotation does not leave the limb behind. Feet follow the same lifted trajectory and preserve the destination's rotation requirement. Re-activating an automatic action during return reverses travel from the current pose.

When borrowing a steering hand, the controller uses the steering planner reservation API; the remaining attached hand takes leadership when steering. The planner continues to own wheel geometry, finger poses and rim regrip. A second request cannot remove the last required hand. Controls without a minimum may remain unsupported.

Seat exit cancels its tokens before detach. Target disable/destruction, damage release, external mode/binding changes and missing contacts cancel on the next controller step. Vehicle disable, teleport/reset, Refresh and destruction also clean up. Restoration only changes a binding still owned by that token; a newer foreign binding and a deliberate mode change are preserved. ``CancelSeat`` and ``CancelAll`` are explicit cleanup APIs. Refresh cancels work and rebuilds discovery and ID maps; it is a setup boundary, not a per-frame operation.

**Example:** ``GearLeverReach.cs``

.. raw:: html

   <!-- example: GearLeverReach.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class GearLeverReach : MonoBehaviour
       {
           public VehicleController vehicle;
           public PassengerSeat seat;
           private HandleUse request;
           public void GearChanged()
           {
               if (request != null && request.IsActive) return;
               request = vehicle.handles.TryUse(seat, PassengerBodyPart.RightHand, "GearLever");
           }
           private void OnDisable() => request?.Cancel();
       }
   }

.. _uvs-scripting-handles--finger-pose-transitions:

Finger pose transitions
-----------------------

``VehicleHandle.fingerBlendDuration`` controls the duration in seconds for changing from the currently displayed finger pose to this handle's pose (default 0.12 s, zero applies immediately). The passenger captures the actual phalanx rotations before releasing/rebinding a grip solver, restores them after synchronous fitting, then applies a SmoothStep quaternion blend to the destination pose. Controller travel preserves the captured finger pose. Returning to the wheel uses the wheel's duration. ``maximumFingerSpeed`` continues to limit pose changes within a bound handle; the handover itself uses Finger Blend Duration.

Interrupted transitions start from the current visible pose. Only mapped finger bones are affected; wrist IK, palm contacts and attached props retain their ownership. The blend uses scaled time, pauses at timeScale zero and advances once by elapsed time even when posing runs repeatedly in a frame. Zero finger weight leaves animation ownership intact. Initial seating and editor preview do not blend.

.. _uvs-scripting-handles--grip-dimensions:

Grip dimensions
---------------

Grip dimensions describe the surface the fingers should wrap around. They do not resize the visible model. If the configured grip is thicker than the rendered lever, the fingers can close around an invisible larger cylinder; if it is thinner, they can cut through the mesh. Measure the actual control in the same local frame used by the handle before tuning finger fitting.

.. _uvs-scripting-handles--cylindrical-controls:

Cylindrical controls
~~~~~~~~~~~~~~~~~~~~

``VehicleHandle.gripDiameter`` is the full cylinder diameter in metres, not its radius. A 0.04 m diameter describes a 4 cm thick grip. The cylinder runs along the palm anchor's local X axis. Its centerline lies half that diameter toward local +Y from the palm contact. The target therefore describes contact on the cylinder surface rather than the center of the rod.

For a new lever, create a unit-scale contact child at the desired palm contact. Align its local X with the length of the grip and +Y toward the rod's centerline. Keep imported-mesh axis corrections on a separate mesh child. Positive uniform scale preserves the geometric assumptions; a nonuniformly scaled cylinder cannot be represented by a single diameter.

``adaptiveGrip`` enables fitting for supported hand bindings. ``gripDiameter`` describes the object; character finger lengths, flexion axes and pad sizes describe the hand. Increasing the grip diameter to hide a bad finger axis usually fixes one pose while making others worse. Validate the contact orientation and character calibration first.

.. _uvs-scripting-handles--steering-rims-and-authored-contacts:

Steering rims and authored contacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A wheel uses ``rimRadius`` for the centerline radius and ``tubeRadius`` for the rim tube's radius. These are two different measurements, and ``tubeRadius`` is a radius rather than the cylinder diameter above. ``tubeDepthRadius`` can describe a different fore/aft tube section. ``customRim`` replaces the circular centerline with a closed set of at least three samples for irregular wheels.

``leftAngle`` and ``rightAngle`` place contacts around the rim. ``reverseApproach`` changes which direction faces away from the driver. With ``authoredTargets``, the component retains manually placed palm targets instead of generating their position from the rim. ``stickGrip`` then selects cylindrical fitting at those authored targets, which is useful for a joystick or another grip that uses steering-hand behavior without being a wheel rim.

Geometry changes require preparation and occupant rebinding, not just a new numeric value. Apply them at an explicit authoring/spawn boundary when possible. The following component is intended for an unoccupied vehicle: it updates a cylinder dimension and prepares the handle. For an already occupied seat, also perform the appropriate occupant binding refresh through its normal passenger lifecycle.

**Example:** ``CylinderGripSetup.cs``

.. raw:: html

   <!-- example: CylinderGripSetup.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CylinderGripSetup : MonoBehaviour
       {
           public VehicleHandle handle;
           [Min(.004f)] public float diameterMetres = .04f;

           public void ApplyBeforeSeating()
           {
               if (!handle) return;
               handle.gripDiameter = Mathf.Max(.004f, diameterMetres);
               handle.Prepare();
           }
       }
   }

This example changes the common cylindrical measurement. It does not change ``SteeringWheelHandle.tubeRadius``, scale a mesh or calibrate a character. For a steering rim, configure the rim-specific measurements instead. See :doc:`Grip solving </Scripting/GripSolving>` for fitting and steering reservations.

.. _uvs-scripting-handles--pedal-state-and-actions:

Pedal state and actions
-----------------------

``PedalAnimator`` moves the pedal between released and pressed angles. The separate ``PedalHandle.anchor`` provides the occupant's ankle contact. Parent that contact to the moving pedal so the target follows travel. ``motion`` holds the pivot mapping; ``releasedAngle`` and ``pressedAngle`` describe the model's endpoints in degrees.

With ``useResolvedPedals``, throttle/brake presentation follows ``DriveDemand`` and ``ServiceBrake``. This matters for signed forward/reverse input: a command can request the opposite direction while mechanics are still resolving it as braking. Reading the resolved actuator makes the foot match the vehicle's actual pedal interpretation. Other ``HandleInput`` selections read their mapped command channel.

``pressDuration`` and ``releaseDuration`` are the seconds needed for full travel. Smaller demands stop proportionally earlier. ``TargetValue`` is requested demand in 0–1; ``Value`` is current displayed travel. The render-rate ``Tick`` moves between them. ``onValueChanged`` reports displayed-value changes, so it can fire repeatedly while a pedal travels rather than only once when demand changes.

+-------------------------+----------------------------------------------------------------------------------+
| Operation               | Ownership and result                                                             |
+=========================+==================================================================================+
| ``SetValue(value)``     | Takes external ownership, clamps to 0–1 and requests smooth travel.              |
+-------------------------+----------------------------------------------------------------------------------+
| ``SetImmediate(value)`` | Takes external ownership and synchronizes value/pose immediately.                |
+-------------------------+----------------------------------------------------------------------------------+
| ``FollowInput()``       | Returns demand ownership to the configured input mapping.                        |
+-------------------------+----------------------------------------------------------------------------------+
| ``ResetMotion()``       | Releases external ownership, resets demand/travel and applies the released pose. |
+-------------------------+----------------------------------------------------------------------------------+

For a scripted pedal sequence, call ``SetValue`` when its demand changes and ``FollowInput`` when the sequence ends. Ordinary driving should remain in input-following mode. Calling ``SetValue`` every frame from an unrelated script would keep taking ownership away from input.

.. _uvs-scripting-handles--moving-one-foot-between-pedals:

Moving one foot between pedals
------------------------------

Bind the seat foot directly to the accelerator handle as its home. On the brake handle enable Use On Action, assign the occupied Seat, select RightFoot, set Allowed limbs to Right foot and choose ServiceBrake. This reads resolved service braking, including drivetrain direction logic. Threshold and Release Threshold provide hysteresis. Start with Travel Duration 0.18 s, Release Duration 0, Return Delay 0 and Lift Height 0.035 m. The controller requests the brake while service braking is above threshold and returns to the configured accelerator home afterwards.

For a clutch or another shared contact, configure an equivalent Command rule. Use ValueChange for levers/switches whose movement should trigger a reach. That trigger observes an action already in progress; to commit a command exactly when the hand arrives, use TryUse with an arrival callback or ControlInteraction, rather than enabling a second automatic rule on the same destination.

A rule must name its seat explicitly. This prevents one passenger from consuming another passenger's limbs. An unoccupied or foreign seat cannot be used. The demo car and bus use this configuration without helper components.

.. _uvs-scripting-handles--switch-requests-and-settled-presentation:

Switch requests and settled presentation
----------------------------------------

``SwitchAnimator`` presents two-position off/on controls or three-position negative/neutral/positive controls. ``Position`` is the requested detent; ``Value`` is normalized displayed travel. ``transitionDuration`` controls how long the visible mechanism takes to reach its destination. The paired ``SwitchHandle.anchor`` follows the model and provides a palm target.

Use ``SetValue(bool)`` or ``Toggle()`` for binary controls. Enable ``threePosition`` before calling ``SetPosition(SwitchPosition.Negative)``; invalid enum values throw, and a negative binary position is rejected with an exception. For three-position geometry, ``neutralOffset`` is the middle pose between ``motion.minimum`` and ``motion.maximum``, expressed in the selected motion unit.

``PositionChanged`` and ``ValueChanged`` report changed requests. ``PositionReached`` and ``Switched`` report settled motion from ``SwitchAnimator.Tick``. A change between negative and positive changes the detent but keeps ``IsOn`` ``true``, so a bool-only listener cannot distinguish those states. Use position events when all three detents carry different meaning.

``SetImmediate`` and ``SetPositionImmediate`` synchronize silently. A mechanic-to-control binding should use them when displaying an existing state, so displaying “gear deployed” does not issue another gear request. Use request events for player intent and settled events for physical clicks; ``SwitchAudio`` already follows settled presentation.

.. _uvs-scripting-handles--observe-all-switch-detents:

Observe all switch detents
~~~~~~~~~~~~~~~~~~~~~~~~~~

When a three-position switch has different meanings at both ends, subscribe to ``PositionChanged`` instead of the bool event. This observer captures the subscribed source and removes the same handler on disable. It exposes the requested detent for application UI; use ``PositionReached`` instead if the consumer needs settled presentation.

**Example:** ``SwitchDetentObserver.cs``

.. raw:: html

   <!-- example: SwitchDetentObserver.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SwitchDetentObserver : MonoBehaviour
       {
           public SwitchAnimator control;
           public SwitchPosition RequestedPosition { get; private set; }
           private SwitchAnimator subscribed;

           private void OnEnable()
           {
               subscribed = control;
               if (!subscribed) return;
               subscribed.Prepare();
               RequestedPosition = subscribed.Position;
               subscribed.PositionChanged += Receive;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.PositionChanged -= Receive;
               subscribed = null;
           }

           private void Receive(SwitchPosition position) => RequestedPosition = position;
       }
   }

Editing ``control`` while enabled does not rebind the captured subscription. Use an explicit rebind or disable/re-enable this adapter when changing its source. Keep the gameplay action in the request/interaction path rather than adding it to a passive readout.

.. _uvs-scripting-handles--temporary-hand-transfer:

Temporary hand transfer
-----------------------

For an explicit cockpit action, call TryUse and commit in its arrival callback. Configure travel, release and return delay on the destination handle. ControlInteraction combines the same scheduler with IK, masked Animator gestures or a custom driver. See :doc:`timed interactions </ControlInteractions>`.

.. _uvs-scripting-handles--extending-or-selecting-a-handle:

Extending or selecting a handle
-------------------------------

Derive ControlAnimator for new control motion or value sources, and ControlHandle for the corresponding IK contact. Set Allowed limbs, return stable transforms, and override ReadInteractionValue when automatic ValueChange requests should follow the control. Keep command meaning in the control/application and limb scheduling in vehicle.handles. Set minimumAttachments for controls that must retain support. Add control components at runtime, then call vehicle.handles.Refresh once.

.. _uvs-scripting-handles--hand-pose-authoring-metadata:

Hand pose authoring metadata
----------------------------

Hand/finger closure sliders are editor authoring helpers. See :doc:`Reusable hand positions </HandPositions>` for saving poses and thumb/finger curl axes, and :doc:`animation and IK </HandleAnimation>` for contact and Animator relay order.

.. _uvs-scripting-handles--car-handbrake:

Car handbrake
-------------

The demo car uses an ``AnchorHandle`` with ID ``Handbrake``, restricted to the driver's right hand. Its palm contact is parented to the moving parking brake lever. Automatic use samples ``HandleActionSource.Command`` with ``HandleInput.Handbrake``: the hand stays on the lever while the command is held, then returns to the steering wheel after a short release delay. Outbound travel is 0.16 seconds, return travel 0.28 seconds; finger blending is 0.1 seconds. Priority 10, Interrupt Lower Priority and Allow Unsupported Departure let this request interrupt a lower-priority timed right-hand action and borrow the right hand even while the left hand is using another control. Other limbs keep their own requests; persistent and Animator ownership remain protected.

.. _uvs-scripting-handles--synchronizing-control-motion-with-limb-arrival:

Synchronizing control motion with limb arrival
----------------------------------------------

SwitchAnimator, PedalAnimator, RotaryAnimator, ThrottleAnimator, GearPaddleAnimator, GearLeverAnimator and AnchoredControlAnimator expose **Wait For Handle** (on by default) and **Fake Sync Handle Motion** (off by default). Every control animator references its separate IK contact through Handle. IK handles never animate the control model. The handle's use settings select the occupant and preferred limb and provide the outbound/return times. SteeringWheelAnimator and its steering variants are excluded.

Wait For Handle starts visual motion after the central controller reports Holding and the real limb has reached its contact. An occupied but busy limb normally waits until available; explicit priority-interruption rules can admit a higher-priority timed request. There is no timeout bypass. A missing/disabled handle or absent occupant permits immediate motion. Initial synchronization and editor preview stay silent and do not request a limb. The actual brake, gearbox, lights and other mechanical commands still react immediately; only cockpit presentation waits.

Fake Sync Handle Motion captures the initial contact pose relative to the vehicle before motion starts. Outbound travel targets that captured pose even if the control moves; after arrival the limb follows the live contact. It is independent of Wait For Handle: turning wait off and fake sync on allows immediate control motion with an approach to its original pose. Both can be enabled. Finger blending and return travel retain their existing settings.

The demo enables waiting and disables fake sync on the Car handbrake, profile switch, indicator/wiper stalks, gear paddles, aircraft landing gear switch and Bus gear lever. The handbrake's contact is linked to its animator. Controls without an explicit occupant keep working normally. A helper owns one request for the operation, holds it through visual motion, and releases it afterwards; a continuously held handbrake retains the hand until release. Disable cancels pending synchronization and restores limb ownership.

All controls using Wait For Handle verify actual limb arrival after timed IK transit: the physical palm contact (or foot/ankle bone) must be within 2.5 cm of the target. Hands also wait for the configured finger-blend interval. The check is latched for the operation, so a moving control does not repeatedly pause for a following limb. Existing home attachments are checked too. HumanoidIK supplies the limb bones; humanoid Animator bones are supported when HumanoidIK is absent. Occupied custom rigs must supply those bones/contact data; missing contact data does not falsely report arrival. Controls without an occupant still animate immediately. For a permanently attached control with no action seat, the occupied seat and limb are inferred from the existing home binding, including a foot temporarily borrowed by another pedal. The demo handbrake lift takes 0.22 seconds and lowering 0.20 seconds.

.. _uvs-scripting-handles--smooth-physical-reattachment:

Smooth physical reattachment
----------------------------

After a transfer returns to its home handle, a physical palm can still have a small residual distance from the IK target. Rebinding captures the native point constraint at the real palm position, then eases that offset to the live contact in vehicle coordinates. The duration follows the destination's finger-blend duration, with a minimum of 0.08 seconds. Wrist drive strength rises with the same blend. This prevents a one-tick positional correction at the end of a switch-to-throttle return while retaining the configured return path and finger blending. Initial seating retains immediate authored attachment; disabling or replacing a limb removes its transient capture state.

.. _uvs-scripting-handles--animator-and-ik-handle-ownership:

Animator and IK handle ownership
--------------------------------

All moving controls use the same separation: an Interior animator owns geometry, input/value sampling, events and travel; a Passengers IK handle owns the limb anchor, allowed limbs, hand/finger pose and reach/return settings. Link the animator's Handle to the contact and the contact's Animator back to the visual controller. Both references are serialized in the demo.

+------------------------------------------+----------------------------------+
| Visual controller                        | IK contact                       |
+==========================================+==================================+
| RotaryAnimator / AnchoredControlAnimator | RotaryHandle                     |
+------------------------------------------+----------------------------------+
| PedalAnimator                            | PedalHandle                      |
+------------------------------------------+----------------------------------+
| SwitchAnimator                           | SwitchHandle                     |
+------------------------------------------+----------------------------------+
| GearPaddleAnimator                       | GearPaddleHandle                 |
+------------------------------------------+----------------------------------+
| GearLeverAnimator                        | GearLeverHandle                  |
+------------------------------------------+----------------------------------+
| ThrottleAnimator                         | ThrottleHandle                   |
+------------------------------------------+----------------------------------+
| SteeringStickAnimator                    | JoystickHandle                   |
+------------------------------------------+----------------------------------+
| SteeringWheelAnimator / YokeAnimator     | SteeringWheelHandle / YokeHandle |
+------------------------------------------+----------------------------------+

ControlAnimator derives from VehicleHandleAnimator and centralizes Handle, Wait For Handle, Fake Sync Handle Motion and motion guides. ControlHandle derives from AnchorHandle and reads interaction values from its paired animator. PedalHandle adds ankle geometry; it has no input or model travel fields. Steering handles retain only grip/rim geometry and limb support policy. Add animators under Interior / Animators and contacts under Passengers / IK / Handles. The Tools menu also provides Interior / Control Pairs to create and connect both components with a single undoable action. Controls that do not need occupant interaction may leave Handle empty. InstrumentNeedle derives from RotaryAnimator and does not need an IK contact.

Use ``vehicle.handles.Get(id)`` for limb ownership, then use the assigned ControlHandle.animator (or a direct serialized animator reference) to request visual state. Bind lights, wipers, profiles and switch audio to SwitchAnimator. GearShiftAnimator.Animators accepts IGearShiftAnimator implementations, including GearPaddleAnimator. There are no combined motion-and-IK compatibility components.

.. _uvs-scripting-handles--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The following declarations belong to the current runtime types. See the linked API sections for parameters, return values, state and configuration.

.. _uvs-scripting-handles--anchorhandle:

AnchorHandle
~~~~~~~~~~~~

-  **AnchorHandle** — ``public override Transform GetAnchor(PassengerBodyPart part)`` — Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part.

.. _uvs-scripting-handles--handleanimatorbinding:

HandleAnimatorBinding
~~~~~~~~~~~~~~~~~~~~~

:ref:`HandleAnimatorBinding <uvs-api-handles--handleanimatorbinding>` gives the full declared contract.

-  ``public void Apply()`` — Current apply.
-  ``public void BeginControlChange()`` — Current begin control change.
-  ``public void ContactEnter()`` — Current contact enter.
-  ``public void ContactExit()`` — Current contact exit.
-  ``public void EndControlChange()`` — Current end control change.
-  ``public void SetControlValue(float value)`` — Current set control value.
-  ``public void SetFingerWeight(float value)`` — Current set finger weight.
-  ``public void SetIKWeight(float value)`` — // Animation Events use one simple argument and can live on the animated character.

.. _uvs-scripting-handles--handlecontroller:

HandleController
~~~~~~~~~~~~~~~~

-  **HandleController** — ``public event Action<HandleUse> Finished`` — After completion or cancellation has released ownership and restored any owned binding. Payload is the ended token.
-  **HandleController** — ``public event Action<HandleUse> Started`` — After a token owns its limb. Payload is the new token.
-  **HandleController** — ``public void CancelAll()`` — Immediately cancel every active token, blocking reentrant acquisition from cancellation callbacks.
-  **HandleController** — ``public void CancelSeat(PassengerSeat seat)`` — Immediately cancel tokens for one seat. Blocks reentrant acquisition during cleanup.
-  **HandleController** — ``public VehicleHandle Current(PassengerSeat seat, PassengerBodyPart limb)`` — Returns the requested destination while a token owns the limb; otherwise its configured handle. May be null for direct anchors.
-  **HandleController** — ``public VehicleHandle Get(string id)`` — Exact ID lookup; null for missing or duplicate IDs. Disabled registered handles remain discoverable.
-  **HandleController** — ``public HandleUse GetUse(PassengerSeat seat, PassengerBodyPart limb)`` — Returns the active ownership token for this seat and limb, otherwise null.
-  **HandleController** — ``public void Refresh()`` — Cancel active work and rebuild handle discovery, IDs, subscriptions and priority order. Call after adding/removing handles or editing IDs/priorities.
-  **HandleController** — ``public HandleUse TryAcquire(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target)`` — Admit persistent application-driven target ownership; returns null on refusal. Cancel the returned token to restore the home binding.
-  **HandleController** — ``public HandleUse TryAcquireAnimator(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target)`` — Admit persistent ownership with Animator mode. Cancel restores mode only if it is still Animator.
-  **HandleController** — ``public bool TryGet(string id, out VehicleHandle handle)`` — Exact case-sensitive ID lookup. Returns false for missing, blank/unregistered or duplicate IDs.
-  **HandleController** — ``public HandleUse TryReachAndHold(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target)`` — Reach using outbound timing, then retain ownership until Return or Cancel. Returns null if unavailable.
-  **HandleController** — ``public HandleUse TryUse(PassengerSeat seat, PassengerBodyPart limb, string id, Action onArrival = null)`` — Admit an out-and-back reach or return null. Explicit-limb overloads require that limb; the target-only overload uses preferred/fallback settings. Callback runs once on arrival.
-  **HandleController** — ``public HandleUse TryUse(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, Action onArrival = null)`` — Admit an out-and-back reach or return null. Explicit-limb overloads require that limb; the target-only overload uses preferred/fallback settings. Callback runs once on arrival.
-  **HandleController** — ``public HandleUse TryUse(PassengerSeat seat, VehicleHandle target, Action onArrival = null)`` — Admit an out-and-back reach or return null. Explicit-limb overloads require that limb; the target-only overload uses preferred/fallback settings. Callback runs once on arrival.

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method / event / callback                                                                                                            | Role                                                                                                      |
+======================================================================================================================================+===========================================================================================================+
| ``public HandleUse TryAcquire(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, bool forceIK)``                      | See :ref:`HandleController <uvs-api-handles--handlecontroller>` for the declared lifecycle and arguments. |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public HandleUse TryReachAndHold(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, bool forceIK)``                 | See :ref:`HandleController <uvs-api-handles--handlecontroller>` for the declared lifecycle and arguments. |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public HandleUse TryUse(PassengerSeat seat, PassengerBodyPart limb, VehicleHandle target, bool forceIK, Action onArrival = null)`` | See :ref:`HandleController <uvs-api-handles--handlecontroller>` for the declared lifecycle and arguments. |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-handles--handlefingerposition:

HandleFingerPosition
~~~~~~~~~~~~~~~~~~~~

-  **HandleFingerPosition** — ``public HandleFingerPosition Copy()`` — Independent copy of this finger configuration.
-  **HandleFingerPosition** — ``public Vector3 Rotation(HandleFingerSegment segment)`` — Typed lookup of the base/middle/tip rotation; rejects invalid enum values.
-  **HandleFingerPosition** — ``public Vector3 Rotation(int segment)`` — Returns base, middle or tip rotation for segment 0, 1 or 2.
-  **HandleFingerPosition** — ``public void SetRotation(HandleFingerSegment segment, Vector3 rotation)`` — Sets a joint rotation in calibrated bone-local XYZ degrees; rejects invalid enum values.

.. _uvs-scripting-handles--handlehandpose:

HandleHandPose
~~~~~~~~~~~~~~

-  **HandleHandPose** — ``public HandleHandPose Copy()`` — Deep copy including all five finger configurations.
-  **HandleHandPose** — ``public HandleFingerPosition Finger(HandleFinger finger)`` — Typed finger lookup; invalid enum values throw ArgumentOutOfRangeException.
-  **HandleHandPose** — ``public HandleFingerPosition Finger(string digit)`` — Returns the configured Thumb, Index, Middle or Ring finger; other names use Little.
-  **HandleHandPose** — ``public void SetFinger(HandleFinger finger, HandleFingerPosition position)`` — Replaces the chosen finger configuration; rejects null and invalid enum values.

.. _uvs-scripting-handles--handlehandposition:

HandleHandPosition
~~~~~~~~~~~~~~~~~~

-  **HandleHandPosition** — ``public HandleHandPosition Copy()`` — Deep resolved-value copy, including the resolved Auto-apply closure policy, with independent left/right/finger objects and no preset link.
-  **HandleHandPosition** — ``public HandleHandPose Hand(bool leftHand)`` — Returns the resolved local/shared hand data.
-  **HandleHandPosition** — ``public HandleHandPose Hand(HandleHandSide side)`` — Resolved hand data, using the optional shared preset. Invalid enum values throw ArgumentOutOfRangeException.
-  **HandleHandPosition** — ``public void SetHand(HandleHandSide side, HandleHandPose pose)`` — Replaces the resolved side in local data or the linked preset; rejects null.

.. _uvs-scripting-handles--handlehandpositionprofile:

HandleHandPositionProfile
~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`HandleHandPositionProfile <uvs-api-handles--handlehandpositionprofile>` gives the full declared contract.

.. _uvs-scripting-handles--handleuse:

HandleUse
~~~~~~~~~

-  **HandleUse** — ``public event Action Arrived`` — After binding the destination and running the arrival callback. Persistent acquisitions do not emit this event.
-  **HandleUse** — ``public event Action Cancelled`` — After cancellation has released ownership. An already committed action is not undone.
-  **HandleUse** — ``public event Action Completed`` — After the return completes and the home binding is restored.
-  **HandleUse** — ``public bool BeginAnimation()`` — Give an arrived, held hand to Animator ownership; Return restores its original mode and performs the timed home trip. Returns false if ownership/state is no longer valid.
-  **HandleUse** — ``public bool BeginAnimation(bool keepHandOnTarget)`` — With true, retain hand IK/physical support while animating fingers; Return/cancellation restores finger ownership. False uses whole-limb animation.
-  **HandleUse** — ``public void Cancel()`` — Idempotent immediate cancellation. Never restores a newer foreign binding.
-  **HandleUse** — ``public void Return()`` — Release persistent/automatic holding and request a timed return. For an outbound trip, return follows arrival.

.. _uvs-scripting-handles--ihandle:

IHandle
~~~~~~~

-  **IHandle** — ``void SetInput(Command command, float deltaTime)`` — Updates custom IK contact targets; it never owns instrument geometry.

-  ``void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` — Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.

-  ``Transform GetAnchor(PassengerBodyPart part)`` — Returns the stable contact transform for a supported body part, or ``null`` when unavailable/unsupported.

-  ``float HandContact(bool left)`` — Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.

-  ``bool HandDriven(bool left)`` — Reports whether the selected hand should receive physical target guidance.

-  ``bool HandSteering(bool left)`` — Reports whether the selected hand participates in steering support.

-  ``void Prepare()`` — Initializes the contact or synchronizes its initial state without requesting a limb.

.. _uvs-scripting-handles--motorcyclehandle:

MotorcycleHandle
~~~~~~~~~~~~~~~~

-  **MotorcycleHandle** — ``public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` — Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.
-  **MotorcycleHandle** — ``public override Transform GetAnchor(PassengerBodyPart part)`` — Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part.

.. _uvs-scripting-handles--pedalhandle:

PedalHandle
~~~~~~~~~~~

-  **PedalHandle** — ``public override Transform GetAnchor(PassengerBodyPart part)`` — Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part.
-  **PedalHandle** — ``public override void Prepare()`` — Initializes the contact or synchronizes its initial state without requesting a limb.
-  **PedalHandle** — ``public virtual bool TryGetFootPose(out Vector3 position, out Quaternion rotation)`` — Resolves fixed ankle position and foot pitch from Ankle Anchor and Contact Anchor without creating a target.

.. _uvs-scripting-handles--steeringwheelhandle:

SteeringWheelHandle
~~~~~~~~~~~~~~~~~~~

-  **SteeringWheelHandle** — ``public virtual bool AllowsHand(bool left)`` — Checks enabled state and the configured left/right grip-mode permission.
-  **SteeringWheelHandle** — ``public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` — Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.
-  **SteeringWheelHandle** — ``public virtual Vector3 Centerline(float angle)`` — Evaluates the steering-rim centerline at an angular coordinate in the wheel's local frame.
-  **SteeringWheelHandle** — ``public override Transform GetAnchor(PassengerBodyPart part)`` — Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part.
-  **SteeringWheelHandle** — ``public virtual void GetContactFrame(float angle, out Vector3 point, out Quaternion rotation)`` — Returns a world-space contact point/orientation at an angular coordinate around the steering rim.
-  **SteeringWheelHandle** — ``public virtual void GetPalmContactFrame(float angle, float pressure, out Vector3 point, out Quaternion rotation)`` — Returns a world palm-contact frame including the requested pressure adjustment.
-  **SteeringWheelHandle** — ``public override float HandContact(bool left)`` — Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.
-  **SteeringWheelHandle** — ``public override bool HandDriven(bool left)`` — Reports whether the selected hand should receive physical target guidance.
-  **SteeringWheelHandle** — ``public virtual bool HandPinch(bool left)`` — Reports whether the selected hand uses the pinch gesture.
-  **SteeringWheelHandle** — ``public override bool HandSteering(bool left)`` — Reports whether the selected hand participates in steering support.
-  **SteeringWheelHandle** — ``public virtual float PalmPressure(bool left)`` — Returns normalized palm-pressure presentation for the selected hand.
-  **SteeringWheelHandle** — ``public override void Prepare()`` — Initializes the contact or synchronizes its initial state without requesting a limb.
-  **SteeringWheelHandle** — ``public virtual float RadiusAt(float angle)`` — Returns the steering-rim tube radius at the supplied angular coordinate.
-  **SteeringWheelHandle** — ``public override void ResolveHandPositions(bool left, out HandleHandPose primary, out HandleHandPose secondary, out float blend)`` — Selects the configured grip/pinch and blends the pressure configuration using current steering contact demand.
-  **SteeringWheelHandle** — ``public virtual void SetGripMode(SteeringGripMode mode)`` — Chooses both hands, left only, right only or released steering-grip permission.
-  **SteeringWheelHandle** — ``public virtual void SetHandContact(bool left, float contact)`` — Sets normalized physical contact participation for one hand; finger pose is independent of contact.
-  **SteeringWheelHandle** — ``public virtual void SetHandControl(bool left, bool driven, bool steering)`` — Selects physical-guidance and steering-support participation independently for one hand.
-  **SteeringWheelHandle** — ``public virtual void SetHandPinch(bool left, bool value)`` — Enables/disables the selected hand's pinch gesture.
-  **SteeringWheelHandle** — ``public virtual void SetHandPinch(bool left, float amount)`` — Sets a clamped 0–1 Pinch-to-Wrapped blend. Zero uses normal grip/pressure selection; one uses the saved Pinch pose.
-  **SteeringWheelHandle** — ``public virtual void SetPalmPressure(bool left, float value)`` — Sets the blend towards the authored pressure hand position; the calibrated palm contact stays unchanged.
-  **SteeringWheelHandle** — ``public virtual float SignedDistance(Vector3 worldPoint)`` — Returns signed world-space distance to the steering tube surface; positive means outside.
-  **SteeringWheelHandle** — ``public virtual float SignedDistanceLocal(Vector3 point)`` — Evaluates a wheel-local point against the steering tube and returns scaled surface distance.
-  **SteeringWheelHandle** — ``public override bool Supports(PassengerBodyPart part)`` — Whether Allowed limbs and any specialized geometry policy permit this limb.
-  **SteeringWheelHandle** — ``public virtual void UpdateTargets()`` — Updates steering palm targets from current geometry without changing seat occupancy.

.. _uvs-scripting-handles--vehiclehandle:

VehicleHandle
~~~~~~~~~~~~~

-  **VehicleHandle** — ``public virtual void SetInput(Command command, float deltaTime)`` — Updates custom IK contact targets; it never owns instrument geometry.

-  **VehicleHandle** — ``public event Action<HandleContactContext> ContactEnded`` — Once when contact is lost or released (including exit/disable/rebinding). Payload retains the original occupant identity.

-  **VehicleHandle** — ``public event Action<HandleContactContext> ContactStarted`` — Once on a not-touching to touching transition; C# event runs before the matching UnityEvent.

-  **VehicleHandle** — ``public event Action<HandleContactContext> ContactUpdated`` — Once per contact sample while touching, including its start sample. Payload identifies handle, seat, occupant, part and target.

-  **VehicleHandle** — ``public UnityEvent<HandleContactContext> onContactEnded`` — Inspector-configurable counterpart of ContactEnded. Runs after the C# event for the same phase.

-  **VehicleHandle** — ``public UnityEvent<HandleContactContext> onContactStarted`` — Inspector-configurable counterpart of ContactStarted. Runs after the C# event for the same phase.

-  **VehicleHandle** — ``public UnityEvent<HandleContactContext> onContactUpdated`` — Inspector-configurable counterpart of ContactUpdated. Runs after the C# event for the same phase.

-  **VehicleHandle** — ``public UnityEvent<HandleValueContext> onValueChangeStarted`` — Inspector-configurable counterpart of ValueChangeStarted. Runs after the C# event for the same phase.

-  **VehicleHandle** — ``public UnityEvent<HandleValueContext> onValueChangeStopped`` — Inspector-configurable counterpart of ValueChangeStopped. Runs after the C# event for the same phase.

-  **VehicleHandle** — ``public UnityEvent<HandleValueContext> onValueChanging`` — Inspector-configurable counterpart of ValueChanging. Runs after the C# event for the same phase.

-  **VehicleHandle** — ``public event Action<HandleValueContext> ValueChangeStarted`` — Once when a significant value change or explicit BeginValueChange starts activity.

-  **VehicleHandle** — ``public event Action<HandleValueContext> ValueChangeStopped`` — Once when the value settles for valueStopDelay, explicit EndValueChange runs or the handle is disabled/destroyed.

-  **VehicleHandle** — ``public event Action<HandleValueContext> ValueChanging`` — Each active changed/manual sample; does not imply contact or commit a gameplay action.

-  **VehicleHandle** — ``public void BeginValueChange()`` — Starts explicit value activity, emitting Started only when idle. Constant-value samples still emit progress until EndValueChange.

-  **VehicleHandle** — ``public virtual void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` — Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.

-  **VehicleHandle** — ``public void ClearHandPositionOverride(HandleHandSide side)`` — Restores normal selection and wheel pressure/pinch blending for that hand.

-  **VehicleHandle** — ``public void EndValueChange()`` — Ends manual/automatic activity and emits Stopped once if active. Safe when idle.

-  **VehicleHandle** — ``public void EnsureHandPositions()`` — Initializes missing configurations with the defaults for the handle type; existing local or shared poses remain unchanged.

-  **VehicleHandle** — ``public abstract Transform GetAnchor(PassengerBodyPart part)`` — Returns the stable contact transform for a supported body part, or ``null`` when unavailable/unsupported.

-  **VehicleHandle** — ``public HandleFingerPosition GetFingerPosition(int positionIndex, HandleHandSide side, HandleFinger finger)`` — Typed access to one finger of one configured hand.

-  **VehicleHandle** — ``public virtual Transform GetHandAnchor(PassengerBodyPart part)`` — Returns the configured palm target with pose offsets. Feet keep the raw anchor; source geometry remains on GetAnchor.

-  **VehicleHandle** — ``public HandleHandPose GetHandPose(int positionIndex, HandleHandSide side)`` — Resolved local/shared hand data; edits to shared data affect all handles linked to that asset.

-  **VehicleHandle** — ``public HandleHandPosition GetHandPosition(int index)`` — Strict indexed lookup; invalid indices throw ArgumentOutOfRangeException. HandPosition(int) remains the clamped lookup.

-  **VehicleHandle** — ``public HandleHandPosition GetHandPosition(string name)`` — Named lookup; a missing name throws KeyNotFoundException.

-  **VehicleHandle** — ``public int GetHandPositionOverride(HandleHandSide side)`` — Returns the explicit position index, or -1 for automatic selection.

-  **VehicleHandle** — ``public HandlePoseSettings GetPoseSettings(PassengerBodyPart part)`` — Returns the live settings for this body part; lazily restores a null settings object. Invalid enum throws ArgumentOutOfRangeException.

-  **VehicleHandle** — ``public virtual float HandContact(bool left)`` — Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.

-  **VehicleHandle** — ``public virtual bool HandDriven(bool left)`` — Reports whether the selected hand should receive physical target guidance.

-  **VehicleHandle** — ``public HandleHandPosition HandPosition(int index)`` — Returns a position, clamping the index to the available list.

-  **VehicleHandle** — ``public virtual bool HandSteering(bool left)`` — Reports whether the selected hand participates in steering support.

-  **VehicleHandle** — ``public HandleHandPosition MakeHandPositionLocal(int index)`` — Replaces the entry with a deep local copy of its resolved values, detaching any shared asset.

-  **VehicleHandle** — ``public virtual void Prepare()`` — Initializes the contact or synchronizes its initial state without requesting a limb.

-  **VehicleHandle** — ``public void ReleaseContact(PassengerSeat seat, PassengerBodyPart part)`` — Releases one tracked pair and emits Ended once if touching. Safe when untracked.

-  **VehicleHandle** — ``public bool ReportContact(PassengerSeat seat, PassengerBodyPart part, bool touching)`` — Records touching/not-touching for the current occupant. Select Manual contactSource to use the report; events are emitted when SampleContact runs. No geometric contact required in Manual mode.

-  **VehicleHandle** — ``public virtual void ResetHandle()`` — Resets local handle state through the common extensible handle contract.

-  **VehicleHandle** — ``public virtual void ResolveHandPositions(bool left, out HandleHandPose primary, out HandleHandPose secondary, out float blend)`` — Resolves local or shared left/right configurations and their blend. Base handles use their normal grip; wheels select pinch or blend pressure.

-  **VehicleHandle** — ``public void ResolveHandPositions(HandleHandSide side, out HandleHandPose primary, out HandleHandPose secondary, out float blend)`` — Typed access to the current configuration sources and blend; dispatches to the handle-specific resolver.

-  **VehicleHandle** — ``public void SampleContact(PassengerSeat seat, PassengerBodyPart part)`` — Samples one tracked seat/part and emits contact transitions plus progress while touching. Seats call this after ordinary posing and rigid supports; custom pipelines can call it explicitly.

-  **VehicleHandle** — ``public void SampleInteraction(float deltaTime)`` — Samples the current source and advances generic activity using finite nonnegative seconds. The first sample establishes a silent baseline. Built-in handles call it in LateUpdate.

-  **VehicleHandle** — ``public void SetAnimationValue(float value)`` — Selects the explicit animation signal and stores a finite scalar X/vector. Invalid values are ignored. Sampling emits events; no mechanical action is performed.

-  **VehicleHandle** — ``public void SetAnimationValue(Vector3 value)`` — Selects the explicit animation signal and stores a finite scalar X/vector. Invalid values are ignored. Sampling emits events; no mechanical action is performed.

-  **VehicleHandle** — ``public void SetDefaultHandPosition(int index)`` — Sets the normal grip index with strict index validation.

-  **VehicleHandle** — ``public void SetFingerPosition(int positionIndex, HandleHandSide side, HandleFinger finger, HandleFingerPosition position)`` — Replaces one finger in the resolved hand; rejects null.

-  **VehicleHandle** — ``public void SetHandPose(int positionIndex, HandleHandSide side, HandleHandPose pose)`` — Replaces resolved hand data, including the shared asset when linked; rejects null.

-  **VehicleHandle** — ``public void SetHandPositionOverride(HandleHandSide side, int index)`` — Temporarily forces that hand to use one configured pose with no automatic gesture blend. Does not replace contact geometry, steering ownership or physics. Not serialized.

-  **VehicleHandle** — ``public void SetPoseTarget(PassengerBodyPart part, Transform target)`` — Sets a final world-space target override for this part. Null returns to the handle contact target.

-  **VehicleHandle** — ``public void SetPoseWeights(PassengerBodyPart part, float position, float rotation, float fingers)`` — Sets position, rotation and finger weights independently. Values clamp to 0–1; non-finite values become zero. No re-entry/rebind required.

-  **VehicleHandle** — ``public virtual bool Supports(PassengerBodyPart part)`` — Whether Allowed limbs and any specialized geometry policy permit this limb.

-  **VehicleHandle** — ``public bool TrackContact(PassengerSeat seat, PassengerBodyPart part, Transform contact)`` — Registers a contact transform for the current occupant and limb. Returns false for inactive/transitioning/empty seats or a limb bound to another handle. Built-in humanoids register their mapped bones/palm contacts automatically.

-  **VehicleHandle** — ``public bool TryGetContactState(PassengerSeat seat, PassengerBodyPart part, out HandleContactContext state)`` — Returns the last sampled snapshot for the current occupant, or false/default when unavailable; false-contact snapshots remain valid while tracked.

-  **VehicleHandle** — ``public bool TryGetHandPosition(string name, out HandleHandPosition position)`` — Finds the first exact, case-sensitive position name. Returns false and null for missing/empty names.

.. _uvs-scripting-handles--temporary-ik-in-animator-seats:

Temporary IK in Animator seats
------------------------------

A handle request can borrow IK for one mapped humanoid hand or foot without changing the seat controller or overwriting ``PassengerBodyPartConfig.mode``. This works for standard and custom ``VehicleHandle`` subclasses.

**Example:** ``ForceIKHandleExample.cs``

.. raw:: html

   <!-- example: ForceIKHandleExample.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public sealed class ForceIKHandleExample : MonoBehaviour
       {
           public VehicleController vehicle;
           public PassengerSeat seat;
           public VehicleHandle target;
           private HandleUse use;

           public void Acquire()
           {
               if (!vehicle || !seat || !target) return;
               use?.Cancel();
               use = vehicle.handles.TryAcquire(
                   seat, PassengerBodyPart.RightHand, target, forceIK: true);
           }

           public void Release()
           {
               use?.Cancel();
               use = null;
           }

           private void OnDisable() => Release();
       }
   }

For timed travel, use ``TryUse(seat, limb, target, forceIK: true)`` or ``TryReachAndHold(seat, limb, target, forceIK: true)``. A held token can ``Return()`` through its normal return path or ``Cancel()`` immediately. ``TryAcquire`` also accepts the currently assigned home handle when forcing IK, allowing an animated limb to temporarily follow its existing contact.

For normal per-handle ownership, set ``target.ControlMode = HandleControlMode.IK`` or ``HandleControlMode.AnimatorIK``. The seat controller stays unchanged. Switching this mode cancels the handle's existing requests; ``TryAcquireAnimator`` explicitly reserves animation ownership for an interaction. For ``IKThenAnimator``, the IK override yields while full-limb animation plays and resumes for return; a finger-only animation can keep the arm on its IK target.

``config.IsIKForced`` reports a handle-driven or temporary IK override; ``config.EffectiveMode`` includes it. ``use.ForcesIK`` records whether a token borrowed IK. The original bindings, hold setting and authored mode are restored when ownership ends. Priority interruptions retain the original return destination and override; old tokens cannot release a replacement request. A new external binding/mode assignment stops the old override rather than being overwritten by it. Damage releases always take precedence.

In Animator seats, ``HumanoidPassenger.SolveSeatedIK()`` solves only forced limbs. Animator + IK keeps its normal full overlay; physical passengers keep their native body policy. Leave ``automaticSeatedIK`` enabled, or call ``SolveSeatedIK()`` after evaluating your own animation pipeline. Custom and Attach Only seat controllers and unmapped limb chains are not eligible for this automatic overlay.

The demo's ``AimingHandDemo`` uses the same forced request for Y: Right → Left → Off, including the yellow Animator car. It does not switch the seat's controller or implement a separate aiming IK solver.
