.. _uvs-scripting-passengeraccess--animated-access-contracts:

Animated access contracts
=========================

Passenger access coordinates an asynchronous journey between a standing character and a seat. The seat supplies an entry/exit endpoint and admission rules; an access motion moves or animates the character; ``PassengerAccess`` owns the reservation and the sequence that hands ownership across.

This is useful when a button press should open a door, play a boarding animation and only then establish occupancy. It is a different operation from immediate ``PassengerSeat.TryEnter``, so admission, animation progress and final seat state must be observed separately.

.. _uvs-scripting-passengeraccess--implementation-map:

Implementation map
------------------

+----------------------------+---------------------------------------------------------------------------+
| Class                      | Responsibility                                                            |
+============================+===========================================================================+
| ``AccessAnimationEvents``  | Relays animation access markers into the sequence.                        |
+----------------------------+---------------------------------------------------------------------------+
| ``AccessAnimationProfile`` | Stores animation states, references and timing configuration.             |
+----------------------------+---------------------------------------------------------------------------+
| ``AccessMotion``           | Abstract motion adapter for beginning, sampling and ending access.        |
+----------------------------+---------------------------------------------------------------------------+
| ``HumanoidAccessMotion``   | Built-in Animator-based humanoid access implementation.                   |
+----------------------------+---------------------------------------------------------------------------+
| ``PassengerAccess``        | Owns the entry/exit state machine, reservation and cancellation.          |
+----------------------------+---------------------------------------------------------------------------+
| ``SeatAccess``             | Describes the seat endpoint, outside marker, door and admission settings. |
+----------------------------+---------------------------------------------------------------------------+

``PassengerAccess`` owns a reservation and the entry/exit state machine; ``AccessMotion`` owns character motion. ``SeatAccess`` stores the seat, outside endpoint, optional door, profile and admission/clearance settings.

.. _uvs-scripting-passengeraccess--admission-and-completion:

Admission and completion
------------------------

A reservation prevents another access request from taking the seat during the handover. Entry does not become occupancy merely because motion starts; exit can release occupancy while the access sequence still owns the character's departure. Application controls should represent “boarding” or “exiting” explicitly instead of treating every admitted request as already complete.

Use ``Finished`` to release application UI locks, then inspect actual occupancy to decide possession. Cancellation can happen before or after a particular handover boundary, so a single animation-success flag is not a replacement for checking the seat.

``TryEnter``/``TryExit`` return admission, not final occupancy/completion. ``State`` progresses through Opening, Moving and Closing. Entry commits occupancy after motion handover; exit releases seating before motion while retaining reservation. ``Finished``/completed/cancelled are distinct from seat ``Entered``/``Exited``.

An outside marker supplies a feet-level endpoint and optional heading. Ground projection changes the effective endpoint without moving the marker. Exit clearance is an endpoint capsule check, not navigation or full-body obstacle avoidance.

.. _uvs-scripting-passengeraccess--animation-bindings:

Animation bindings
------------------

``HumanoidAccessMotion`` moves the character using an Animator-backed access sequence. The animation profile provides the reference frames and state/timing configuration; ``SeatAccess`` supplies the endpoint and optional door. The same character motion can therefore be reused with different seat endpoints if the authored geometry and animation remain compatible.

Configure the standing/seated reference states as well as enter/exit states. Root-motion orientation, useful clip range and transition settings must agree with the reference used for spatial matching. A clip that looks correct in isolation can still hand the character to the seat with an offset if its import or state setup differs from the reference.

Use ``AccessAnimationProfile.useAnimatorRootMotion`` for unbaked Animator root tracks; ``rootMotionScale`` and ``rootMotionRotationWeight`` tune stride and turning. Disable it for movement baked into the skeleton. ``useFootIK`` independently enables ground-foot correction. Manual contact curves use normalized clip time, independently for each foot and direction. Inspector setup is described in :ref:`Animated access <uvs-passengeraccess--adapt-a-clip-to-the-cabin>`.

For another animation framework, derive ``AccessMotion`` instead of making ``PassengerAccess`` discover that framework. Implement admission, sampling, completion and cleanup there. Use ``CanPlay`` to reject incompatible access before reservation/motion becomes an abandoned partial operation.

The reference clip supplies a spatial/timing calibration for the state being played. Keep its useful motion range consistent with the Animator state's speed, transition and offsets. If those disagree, a visually correct clip can still reach the handover point at the wrong place or time.

Door markers are part of the same timeline. Verify that they fall inside the played range and are delivered from the actual animated object. A clip containing an event outside its useful range cannot open the door simply because that event exists in the asset.

``AccessAnimationProfile`` explicitly supplies controller/layer, standing/seated/enter/exit paths, triggers and matching Humanoid reference clips. The Animator owns playback; references calibrate spatial frames. The built-in adapter expects single-clip access states matching those references, not arbitrary Blend Trees.

Configure useful clip ranges, retained import orientation/position, state offsets/exit times, playback speed, transition allowance and completion timeout together. For a door starting closed, profile door events must exist in the useful range and be delivered at playback. Already-open and doorless paths need no door markers. ``State`` transitions complete only after the terminal-state handover.

.. _uvs-scripting-passengeraccess--request-and-observe-access:

Request and observe access
--------------------------

Assign ``PassengerAccess`` on the character and a configured ``SeatAccess``. The named completion handler survives cancellation and is unsubscribed from the exact captured source.

**Example:** ``PassengerAccessButton.cs``

.. raw:: html

   <!-- example: PassengerAccessButton.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class PassengerAccessButton : MonoBehaviour
       {
           public PassengerAccess access;
           public SeatAccess target;
           public bool LastCompleted { get; private set; }
           private PassengerAccess subscribed;

           private void OnEnable()
           {
               subscribed = access;
               if (subscribed) subscribed.Finished += OnFinished;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.Finished -= OnFinished;
               subscribed = null;
           }

           public bool Enter() => access && access.TryEnter(target);
           public bool Exit() => access && access.TryExit();
           private void OnFinished(PassengerAccess source, bool success)
               => LastCompleted = success;
       }
   }

.. _uvs-scripting-passengeraccess--directional-lifecycle-events:

Directional lifecycle events
----------------------------

Use ``EnterBegin``, ``EnterInProgress``, ``EnterFinished``, ``EnterCancelled`` and the corresponding ``Exit...`` events to distinguish boarding from leaving. Begin runs after admission and ``BeforeEnter``/``BeforeExit`` checks, in Opening. Progress runs only in Moving, after sampling the motion. Finished means the complete operation succeeded, including any required door closure. Cancelled reports a reserved operation that failed or was interrupted; a request rejected before reservation emits no lifecycle events.

``EnterInProgress``/``ExitInProgress`` supply a ``PassengerAccessProgress`` value: ``Context`` retains the original vehicle/passenger/seat, ``IsEntering`` gives the direction, ``NormalizedTime`` is nominal motion time from 0 to 1, and ``ElapsedTime``/``Duration`` are seconds. It starts at zero and can repeat one while animation blending, marker waits or final handover continue. Do not unlock controls or assume occupancy from progress alone. Progress callbacks can cancel; the old operation then stops before committing occupancy or publishing stale Inspector progress.

The Inspector exposes the same directional lifecycle through ``onEnterBegin``, ``onEnterInProgress``, ``onEnterFinish``, ``onEnterCancelled`` and their ``onExit...`` counterparts. Progress is a dynamic float argument (0..1); the other Inspector callbacks have no arguments. Existing ``started``, ``completed``, ``cancelled``, ``Finished``, ``Before...``, ``After...`` and ``StateChanged`` remain available. Prefer one API family for each application action to avoid handling the same phase twice.

The normal order is Before → Opening/started/directional Begin → Moving/progress → Closing → Idle/outcome cleanup → completed/Finished(success)/directional Finished → After. On failure, cancelled/Finished(false)/directional Cancelled/Cancelled replace the success notifications. A Before listener can veto a reserved attempt before directional Begin; cancellation is still reported. A begin callback that calls ``Cancel`` or disables the component is cleaned up after begin observers return, and the request returns false. Capture the context passed to a callback instead of reading ``Target`` after completion, because ``Target`` is already cleared.

.. _uvs-scripting-passengeraccess--handle-boarding-and-leaving-from-your-own-code:

Handle boarding and leaving from your own code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add this component to an application object, assign the character's **Passenger Access** and the destination **Seat Access**, then call ``Enter``, ``Exit`` or ``Cancel`` from your input/gameplay code. ``ControlsLocked`` and ``MotionProgress`` can feed an application HUD or input gate. Ownership is decided from actual occupancy at the outcome, including cancellation rollback.

**Example:** ``PassengerAccessLifecycle.cs``

.. raw:: html

   <!-- example: PassengerAccessLifecycle.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class PassengerAccessLifecycle : MonoBehaviour
       {
           public PassengerAccess access;
           public SeatAccess target;
           public bool ControlsLocked { get; private set; }
           public bool IsSeated { get; private set; }
           public float MotionProgress { get; private set; }
           private PassengerAccess subscribed;

           private void OnEnable()
           {
               subscribed = access;
               if (!subscribed) return;
               subscribed.EnterBegin += OnBegin;
               subscribed.ExitBegin += OnBegin;
               subscribed.EnterInProgress += OnProgress;
               subscribed.ExitInProgress += OnProgress;
               subscribed.EnterFinished += OnEnterFinished;
               subscribed.ExitFinished += OnExitFinished;
               subscribed.EnterCancelled += OnCancelled;
               subscribed.ExitCancelled += OnCancelled;
               ControlsLocked = subscribed.IsBusy;
               IsSeated = subscribed.passenger && subscribed.passenger.Seat;
           }

           private void OnDisable()
           {
               if (subscribed) {
                   subscribed.EnterBegin -= OnBegin;
                   subscribed.ExitBegin -= OnBegin;
                   subscribed.EnterInProgress -= OnProgress;
                   subscribed.ExitInProgress -= OnProgress;
                   subscribed.EnterFinished -= OnEnterFinished;
                   subscribed.ExitFinished -= OnExitFinished;
                   subscribed.EnterCancelled -= OnCancelled;
                   subscribed.ExitCancelled -= OnCancelled;
               }
               subscribed = null;
               ControlsLocked = false;
           }

           // True means admitted. Outcome events decide whether the journey succeeded.
           public bool Enter() => access && access.TryEnter(target);
           public bool Exit() => access && access.TryExit();
           public void Cancel() { if (access) access.Cancel(); }

           private void OnBegin(PassengerSeatContext context)
           {
               ControlsLocked = true;
               MotionProgress = 0;
           }

           private void OnProgress(PassengerAccessProgress progress)
           {
               MotionProgress = progress.NormalizedTime;
               // progress.Context.Seat identifies the destination even after detachment.
               // A value of one is not yet an EnterFinished/ExitFinished notification.
           }

           private void OnEnterFinished(PassengerSeatContext context)
           {
               UpdateOccupancy(context);
               Debug.Log("Boarding finished: " + context.Seat.name);
           }

           private void OnExitFinished(PassengerSeatContext context)
           {
               UpdateOccupancy(context);
               Debug.Log("Leaving finished: " + context.Seat.name);
           }

           private void OnCancelled(PassengerSeatContext context)
           {
               UpdateOccupancy(context);
               Debug.Log("Access interrupted; currently seated: " + IsSeated);
           }

           private void UpdateOccupancy(PassengerSeatContext context)
           {
               ControlsLocked = false;
               IsSeated = context.Passenger && context.Passenger.Seat;
           }
       }
   }

For the complete field/property/method signatures, see :doc:`the access API </API/PassengerAccess>` and :ref:`Inspector fields <uvs-inspectorreference-world--passengeraccess>`. For all events grouped by their emitting class, see :ref:`Events reference <uvs-scripting-eventsreference--passengeraccess>`.

.. _uvs-scripting-passengeraccess--tutorial-custom-motion-with-the-built-in-coordinator:

Tutorial: custom motion with the built-in coordinator
-----------------------------------------------------

This is the preferred integration when you want different motion but still want the package's reservation, admission, door coordination, callbacks and occupancy handover.

1. Validate your ``PassengerBody`` and seat with immediate occupancy. Choose the appropriate **Passenger Seat > Passenger Controller**. For a framework that owns all pose/physics, use Custom and ``CustomPassengerBody``; for built-in seated animation/IK use its matching controller.
2. Create a class deriving ``AccessMotion``. Override ``CanPlay`` to check references without acquiring resources. Implement ``Begin`` to capture state/start motion, ``Sample`` to advance motion and ``End`` to release only the resources acquired by this adapter.
3. Override ``GetDuration`` for nominal progress. If your framework finishes independently, override ``IsComplete`` and ``CompletionTimeout``; ``NormalizedTime == 1`` does not guarantee that external animation has finished.
4. Add your adapter beside **Passenger Access** on the character. Assign it to **Passenger Access > Motion**, and assign the body to **Passenger Access > Passenger**. Remove/disable an unused competing adapter.
5. Keep a configured **Seat Access > Seat / Outside** and its **Settings** limits. A profile is needed by HumanoidAccessMotion, not by every custom adapter. A doorless prototype can leave **Seat Access > Door** empty.
6. Supply the references required by your motion adapter. Custom seat ownership does not require **Passenger Seat > Spine Anchor**; the built-in ``HumanoidAccessMotion`` still requires that seated pelvis endpoint and a valid humanoid pelvis.
7. Send input through ``PassengerAccess.TryEnter``/``TryExit``. Never also call ``seat.TryEnter`` inside Sample: the coordinator commits occupancy at its own handover boundary.
8. In success/cancellation handlers restore locomotion according to actual occupancy, including an interrupted exit that has been reseated. If Begin returns false after acquiring a resource, clean up that partial acquisition in Begin; do not depend on successful Begin having occurred.
9. Test interruption/disable and moving endpoints. Your framework must own any navigation, collision sweep and skeleton/character-controller handover it needs; endpoint clearance is not a whole-path solver.

.. _uvs-scripting-passengeraccess--minimal-root-motion-adapter-for-an-application-owned-character:

Minimal root-motion adapter for an application-owned character
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates the contract with a doorless, nonphysical ``CustomPassengerBody``. It smoothly moves the character root between two authored root markers. It is deliberately not a Humanoid clip retargeter or obstacle-avoiding walking controller. Use **Passenger Seat > Passenger Controller = Custom**, leave **Custom supports** lists empty, and have your application hold the seated pose/root after successful entry. Both markers must be outside the character hierarchy. **Seated Root** is a root-space destination; do not substitute a pelvis marker for a root marker.

**Example:** ``ApplicationAccessMotion.cs``

.. raw:: html

   <!-- example: ApplicationAccessMotion.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public sealed class ApplicationAccessMotion : AccessMotion
       {
           public Transform seatedRoot;
           public Transform outsideRoot;
           [Min(0.01f)] public float duration = 1.2f;
           private Transform character, destination;
           private Vector3 startPosition;
           private Quaternion startRotation;
           private bool active;

           public override bool CanPlay(SeatAccess access, PassengerBody body, bool entering)
               => !active && access && body is CustomPassengerBody &&
                  access.seat && access.seat.Controller == PassengerControllerType.Custom &&
                  seatedRoot && outsideRoot;

           public override bool Begin(SeatAccess access, PassengerBody body, bool entering)
           {
               if (!CanPlay(access, body, entering)) return false;
               character = body.transform;
               destination = entering ? seatedRoot : outsideRoot;
               startPosition = character.position;
               startRotation = character.rotation;
               active = true;
               return true;
           }

           public override float GetDuration(SeatAccess access, bool entering)
               => Mathf.Max(0.01f, duration);

           public override bool IsComplete => active && character && destination &&
               (Vector3.Distance(character.position, destination.position) < 0.001f &&
                Quaternion.Angle(character.rotation, destination.rotation) < 0.1f);

           public override void Sample(float normalizedTime)
           {
               if (!active || !character || !destination) return;
               float t = Mathf.SmoothStep(0, 1, Mathf.Clamp01(normalizedTime));
               character.SetPositionAndRotation(
                   Vector3.Lerp(startPosition, destination.position, t),
                   Quaternion.Slerp(startRotation, destination.rotation, t));
           }

           public override void End(bool completed)
           {
               // Do not force a teleport here: exit rollback/actual occupancy is decided by the coordinator.
               // An integration that acquired locomotion/animation resources must release them here too.
               active = false;
               character = destination = null;
           }
       }
   }

For NavMesh/Timeline/network motion, replace interpolation with that framework's start/update/stop calls. Do not start navigation toward the seated pelvis while physics is still pinning the character. Capture exactly the state your integration changes; restore it on rejection/cancellation, or hand it to the seated controller on success. The custom root example leaves movement/input control to the caller so no hidden script toggles your framework.

.. _uvs-scripting-passengeraccess--door-contract-for-a-custom-adapter:

Door contract for a custom adapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``AccessMotion.UsesAnimationDoorEvents`` defaults to false: the coordinator can request/wait for door state through SeatAccess. If your framework supplies its own timeline markers, override it to true and route open/close markers through ``PassengerAccess.AnimationDoor(bool)``. Account for actual door readiness and timeout. Do not enable event-driven door handling without delivering the required markers. The built-in HumanoidAccessMotion also supports its documented wait-for-door animation marker.

.. _uvs-scripting-passengeraccess--tutorial-replace-more-of-the-access-system:

Tutorial: replace more of the access system
-------------------------------------------

Use a ``PassengerAccess`` subclass when you still want to identify the coordinator as a PassengerAccess. Public request/state operations are virtual, but its internal sequence is not a collection of independently overridable phases. Prefer delegating to base.TryEnter/base.TryExit and customizing the motion or SeatAccess admission checks. If you replace a request entirely, you own its full reservation, state, callback and cancellation contract; base cleanup cannot manage an unrelated external sequence automatically.

``PassengerSeat.TryReserve(PassengerAccess owner)`` and ``ReleaseReservation(owner)`` require a PassengerAccess owner, not an arbitrary MonoBehaviour/interface. Occupancy operations enforce reservations; do not bypass a live reservation held by another operation. A subclass remains compatible with this owner type.

For a completely separate coordinator:

1. Prepare your character with the required PassengerBody and seat controller, commonly Custom for an external character framework.
2. Resolve ``vehicle.passengers`` after initialization, or retain a specific PassengerSeat reference. The shortcut can be null and includes disabled modules.
3. Own approach movement, door interaction, concurrency, cancellation and pose transitions in your framework. Validate occupancy again at the handover point.
4. Commit immediate entry using ``vehicle.passengers.TryEnter(body, seat)`` or ``seat.TryEnter(body)``. Handle a false result by restoring your preparation. These APIs do not play animation.
5. Observe seat/core occupancy callbacks and separately publish your application's full-sequence completion. Seat Entered/Exited are not access-animation completion events.
6. Release with ``TryExit``, or eject with the seat API when appropriate. Restore character movement/input based on actual state. A Custom body needs application-owned pose/physics/impulse handling.

Keep one authoritative coordinator per character. Reusing the built-in PassengerAccess + custom AccessMotion normally avoids duplicating the reservation and rollback logic.

.. _uvs-scripting-passengeraccess--cancellation-and-extension:

Cancellation and extension
--------------------------

A custom ``AccessMotion`` implements ``Begin``, ``Sample`` and ``End``. ``Begin`` accepts the selected ``SeatAccess``, character body and direction; use it to acquire only the motion resources this adapter owns. ``Sample(float normalizedTime)`` receives progress, while ``End(bool completed)`` is the cleanup boundary for both success and interruption.

Use ``IsComplete``, ``GetDuration`` and ``CompletionTimeout`` coherently when the external animation or navigation system can outlast nominal progress. A timeout must end the adapter's ownership rather than leaving a character controller disabled forever. Keep seat selection and player identity outside the reusable motion adapter.

``Cancel`` unwinds motion/reservation. Interrupted ordinary exit may reseat its own released occupant; external ejection is not undone. Already committed occupancy may remain after closure cancellation. Read actual occupancy in completion handlers.

Derive from ``AccessMotion`` for navigation, another animation framework or whole-body clearance. Implement its completion/timeout contract. Derive ``SeatAccess`` for custom door admission/readiness. Do not infer the controlled player or target vehicle inside a reusable motion adapter.

.. _uvs-scripting-passengeraccess--context-bearing-access-hooks:

Context-bearing access hooks
----------------------------

BeforeEnter/BeforeExit precede collision preparation and door/motion side effects; AfterEnter/AfterExit report whole-sequence success. Cancelled supplies the same original PassengerSeatContext after failed/cancelled cleanup. These are separate from immediate seat occupancy hooks. See :ref:`the access lifecycle guide <uvs-passengeraccess--before-and-after-the-whole-access-sequence>`.

.. _uvs-scripting-passengeraccess--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed animated access API </API/PassengerAccess>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-passengeraccess--accessanimationevents:

AccessAnimationEvents
~~~~~~~~~~~~~~~~~~~~~

:ref:`AccessAnimationEvents <uvs-api-passengeraccess--accessanimationevents>` gives the full declared contract.

+-------------------------------------------------+---------------------------------------------------------------------------------+
| Method                                          | Role                                                                            |
+=================================================+=================================================================================+
| ``public virtual void AccessOpenDoor()``        | Delivers an animation marker requesting opening of the current access door.     |
+-------------------------------------------------+---------------------------------------------------------------------------------+
| ``public virtual void AccessWaitForOpenDoor()`` | Holds the animation until the actual door opens or Door Timeout cancels access. |
+-------------------------------------------------+---------------------------------------------------------------------------------+
| ``public virtual void AccessCloseDoor()``       | Delivers an animation marker requesting closure of the current access door.     |
+-------------------------------------------------+---------------------------------------------------------------------------------+

.. _uvs-scripting-passengeraccess--accessmotion:

AccessMotion
~~~~~~~~~~~~

:ref:`AccessMotion <uvs-api-passengeraccess--accessmotion>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                                                                 |
+============================================================================================+======================================================================================================================================================+
| ``public abstract bool Begin(SeatAccess access, PassengerBody passenger, bool entering)``  | Attempts to begin character motion for the selected endpoint/body/direction. False rejects the adapter operation before successful motion ownership. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void End(bool completed)``                                               | Ends the motion adapter, using the completion flag to restore or hand over its owned state.                                                          |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanPlay(SeatAccess access, PassengerBody passenger, bool entering)`` | Checks whether the motion adapter can play this access operation for the supplied body and direction.                                                |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float GetDuration(SeatAccess access, bool entering)``                     | Returns nominal access-motion duration for this endpoint and direction.                                                                              |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Sample(float normalizedTime)``                                      | Receives normalized access progress from ``PassengerAccess``; implement pose/motion sampling without choosing a new seat.                            |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengeraccess--humanoidaccessmotion:

HumanoidAccessMotion
~~~~~~~~~~~~~~~~~~~~

:ref:`HumanoidAccessMotion <uvs-api-passengeraccess--humanoidaccessmotion>` gives the full declared contract.

+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                        | Role                                                                                                                                    |
+===============================================================================================+=========================================================================================================================================+
| ``public virtual void Configure(AccessAnimationProfile profile)``                             | Selects the ``AccessAnimationProfile`` used by subsequent access motion.                                                                |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool Begin(SeatAccess target, PassengerBody passenger, bool isEntering)``   | Validates humanoid Animator, clips, mapped feet/pelvis and non-ragdoll state, then captures character/Animator state for access motion. |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void End(bool completed)``                                                  | Ends the motion adapter, using the completion flag to restore or hand over its owned state.                                             |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Duration(bool entering)``                                              | Returns the built-in humanoid motion duration for the selected access direction/configuration.                                          |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanPlay(SeatAccess target, PassengerBody passenger, bool isEntering)`` | Checks whether the motion adapter can play this access operation for the supplied body and direction.                                   |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float GetDuration(SeatAccess target, bool isEntering)``                     | Returns nominal access-motion duration for this endpoint and direction.                                                                 |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Sample(float normalizedTime)``                                         | Evaluates the access motion or water style at the supplied normalized/world sample coordinates.                                         |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReleaseIdleFeet()``                                                     | Releases temporary idle-foot ownership held during humanoid access motion.                                                              |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengeraccess--passengeraccess:

PassengerAccess
~~~~~~~~~~~~~~~

:ref:`PassengerAccess <uvs-api-passengeraccess--passengeraccess>` gives the full declared contract.

+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                              | Role                                                                                                                                                 |
+=====================================================+======================================================================================================================================================+
| ``public virtual bool TryEnter(SeatAccess access)`` | Admits an asynchronous entry and reserves the endpoint/seat. True means started, not occupied/completed; observe Finished and actual seat occupancy. |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit()``                   | Admits asynchronous departure. Seat release and motion completion occur at different boundaries; observe Finished for sequence outcome.              |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AnimationDoor(bool open)``    | Routes an animation door request into the current passenger access sequence.                                                                         |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Cancel()``                    | Unwinds this access attempt's motion/reservation and performs its state-specific occupancy cleanup. Already committed occupancy need not be undone.  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                   | Role                                                                                                                                                                         |
+====================================================================+==============================================================================================================================================================================+
| ``public event Action<PassengerSeatContext> EnterBegin``           | Once an admitted entry starts in Opening, after Before checks; seat reservation is held.                                                                                     |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onEnterBegin``                                 | Inspector counterpart of ``EnterBegin``; no payload.                                                                                                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerAccessProgress> EnterInProgress``   | After each entry motion sample in Moving, starting at zero; progress one is not whole-sequence completion.                                                                   |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<float> onEnterInProgress``                     | Inspector counterpart of ``EnterInProgress``; receives normalized motion time (0..1).                                                                                        |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> EnterFinished``        | Only after the entire entry succeeds, including the required door state and reservation/Target cleanup.                                                                      |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onEnterFinish``                                | Inspector counterpart of ``EnterFinished``; no payload.                                                                                                                      |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> EnterCancelled``       | After a reserved entry is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing.                                                            |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onEnterCancelled``                             | Inspector counterpart of ``EnterCancelled``; no payload.                                                                                                                     |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> ExitBegin``            | Once an admitted exit starts in Opening, after Before checks; seat reservation is held.                                                                                      |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onExitBegin``                                  | Inspector counterpart of ``ExitBegin``; no payload.                                                                                                                          |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerAccessProgress> ExitInProgress``    | After each exit motion sample in Moving, starting at zero; progress one is not whole-sequence completion.                                                                    |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<float> onExitInProgress``                      | Inspector counterpart of ``ExitInProgress``; receives normalized motion time (0..1).                                                                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> ExitFinished``         | Only after the entire exit succeeds, including the required door state and reservation/Target cleanup.                                                                       |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onExitFinish``                                 | Inspector counterpart of ``ExitFinished``; no payload.                                                                                                                       |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> ExitCancelled``        | After a reserved exit is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing.                                                             |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onExitCancelled``                              | Inspector counterpart of ``ExitCancelled``; no payload.                                                                                                                      |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeEnter``          | Before collision preparation, door requests and entry motion, after reservation succeeds. Payload: immutable PassengerSeatContext.                                           |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterEnter``           | After the complete entry sequence succeeds and the reservation/Target are cleared. Payload: immutable PassengerSeatContext.                                                  |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> BeforeExit``           | Before collision preparation, door requests and exit motion, while occupancy is retained. Payload: immutable PassengerSeatContext.                                           |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> AfterExit``            | After the complete exit sequence succeeds and the reservation/Target are cleared. Payload: immutable PassengerSeatContext.                                                   |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeatContext> Cancelled``            | After a started/prepared sequence is cancelled and the reservation/Target are cleared; context retains the original seat/passenger. Payload: immutable PassengerSeatContext. |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerAccess, AccessState> StateChanged`` | When access sequencing changes. Payload: ``PassengerAccess`` and ``AccessState``; seat occupancy may commit at a different boundary.                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerAccess, bool> Finished``            | When an access attempt ends. Payload: ``PassengerAccess`` and success bool; inspect actual occupancy after cancellation/handover.                                            |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent started``                                      | Inspector callback when access sequencing starts; no payload.                                                                                                                |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent completed``                                    | Inspector callback when access succeeds; no payload.                                                                                                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent cancelled``                                    | Inspector callback when access is cancelled; no payload.                                                                                                                     |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengeraccess--passengeraccessprogress:

PassengerAccessProgress
~~~~~~~~~~~~~~~~~~~~~~~

:ref:`PassengerAccessProgress <uvs-api-passengeraccess--passengeraccessprogress>` describes the value properties used by progress listeners.

+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                                                     | Role                                                                                                                |
+============================================================================================================================================+=====================================================================================================================+
| ``public PassengerAccessProgress(PassengerSeatContext context, bool isEntering, float normalizedTime, float elapsedTime, float duration)`` | Constructs an immutable progress sample with captured identities, direction, normalized time and timing in seconds. |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengeraccess--seataccess:

SeatAccess
~~~~~~~~~~

:ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` gives the full declared contract.

+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Method                                                                 | Role                                                                                         |
+========================================================================+==============================================================================================+
| ``public virtual void RequestDoor(bool open)``                         | Requests the configured access door's required state for the current operation.              |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool DoorReady(bool open)``                           | Checks whether the configured door has reached the required access state.                    |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool CanContinue(PassengerBody passenger)``           | Checks whether an admitted seat-access sequence can still continue.                          |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool CanUse(PassengerBody passenger, bool entering)`` | Checks whether a seat-access endpoint is currently usable by the supplied passenger.         |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool IsExitClear(PassengerBody passenger)``           | Checks the configured outside endpoint capsule for exit clearance; it does not plan a route. |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Method / event / callback                      | Role                                                                                                  |
+================================================+=======================================================================================================+
| ``public UnityEvent onEnterBegin``             | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<float> onEnterInProgress`` | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onEnterFinish``            | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onEnterCancelled``         | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onExitBegin``              | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<float> onExitInProgress``  | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onExitFinish``             | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onExitCancelled``          | See :ref:`SeatAccess <uvs-api-passengeraccess--seataccess>` for the declared lifecycle and arguments. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-passengeraccess--motion-ownership-and-cancellation:

Motion ownership and cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The coordinator retains the motion provider admitted for the whole operation. Replacing **Passenger Access > Motion** during access cancels the operation and cleans up the original provider. Keep admission queries side-effect free. Return a finite, nonnegative duration and completion timeout.

Cancellation requested inside ``Begin``, ``End``, or the exit occupancy callback is deferred until that call returns. This prevents committing an already cancelled entry or rolling back an exit before detachment completes. A successful ``Begin`` owns one cleanup call; a throwing ``Begin`` also receives ``End(false)`` to release partially acquired resources. A ``Begin`` returning false must clean up its own partial work. ``End`` must tolerate cleanup of partial initialization.
