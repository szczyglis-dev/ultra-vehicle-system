.. _uvs-scripting-interactions--committed-control-interactions:

Committed control interactions
==============================

A control interaction coordinates presentation around one gameplay action. It can commit immediately, move an IK hand, play an Animator gesture or delegate to a custom driver. The gameplay caller supplies what should happen; the interaction decides when that action is committed and when the presentation is finished.

This is useful for controls such as a gear lever, cockpit switch or release button. The same action can use different character presentation without duplicating its mechanical rule. The key contract is one commit per accepted request, with explicit completion and cancellation.

.. _uvs-scripting-interactions--implementation-map:

Implementation map
------------------

+---------------------------------------+--------------------------------------------------------------------+
| Class                                 | Responsibility                                                     |
+=======================================+====================================================================+
| ``ControlInteraction``                | Owns request admission, mode, timeout and commit/completion state. |
+---------------------------------------+--------------------------------------------------------------------+
| ``ControlInteractionAnimationEvents`` | Relays Animator events to the active interaction.                  |
+---------------------------------------+--------------------------------------------------------------------+
| ``HandleController``                  | Provides the IK out-and-back hand movement.                        |
+---------------------------------------+--------------------------------------------------------------------+
| ``SwitchAnimator``                    | Example destination whose requested state is changed at commit.    |
+---------------------------------------+--------------------------------------------------------------------+

``ControlInteraction`` separates one gameplay commit from Immediate, IK, Animator, IKThenAnimator or Custom presentation. IKThenAnimator holds one token across reach, gesture and return; its completion notification follows the return. Configure it using the :doc:`setup guide </ControlInteractions>`.

.. _uvs-scripting-interactions--request-lifecycle:

Request lifecycle
-----------------

``ControlInteractionRequest`` is the identity of one interaction attempt. Its methods address that attempt, not whichever action happens to be active later. This is important when a timeline or asynchronous animation can report completion after the user cancelled and started something else.

Store the request passed to a custom driver's ``Begin``. Call its ``Commit()`` at the meaningful contact moment, then ``Complete()`` when presentation ends. ``Cancel()`` ends the attempt without undoing an earlier commit. The request checks whether it remains active, preventing a stale callback from committing a newer interaction.

The component's animation entry points intentionally target the current request because an Animation Event carries no captured request identity. Use ``ControlInteractionAnimationEvents`` on the object that actually receives the Animator event. For callbacks that can outlive one animation, capture the request object instead of calling a generic component-level commit later.

Read the lifecycle as admitted → started → committed → completed, with cancellation possible while active. Commitment changes gameplay; completion ends the presentation. A cancelled animation cannot generally undo a projectile already fired or a switch already toggled. If a mechanic needs rollback, implement that as a separate application rule.

Choose the mode by the presentation owner. ``Immediate`` requires no character gesture. ``IK`` needs a valid hand-transfer setup. ``Animator`` still requires an occupied seat even when an Animator is explicitly assigned. ``Custom`` delegates timing to an ``IControlInteractionDriver`` and should release its own animation resources on cancellation.

``TryBegin`` returns admission. ``Commit`` invokes the supplied callback before ``onCommit``, at most once. ``Complete`` commits first if needed, then completes. Cancellation does not undo an already committed mechanic. Busy/disabled/missing requirements return ``false``; fallback belongs to the caller.

IK delegates contact travel and limb ownership to ``vehicle.handles``. Animator temporarily switches the selected limb and uses elapsed times or Animation Events. Custom calls an ``IControlInteractionDriver``. Timeout bounds unfinished Animator/Custom requests; zero disables it.

Animation Event entry points on the component address the current request. Use the event relay on the actual Animator ``GameObject``. Custom asynchronous code should retain the exact request object so late callbacks cannot commit a newer action.

.. _uvs-scripting-interactions--drive-from-an-application-animation:

Drive from an application animation
-----------------------------------

The driver stores the request passed to ``Begin``. Its public methods are suitable for animation/timeline callbacks that address the current pending request. A truly asynchronous task should capture that exact request in its completion closure, so a delayed callback cannot accidentally address a newer request.

The interaction owns whether a request is still valid. Calling the request's methods after cancellation is therefore safer than retaining only a generic “commit current action” function. The driver below leaves actual animation startup to the application and demonstrates the ownership and cleanup boundary.

Set interaction mode to Custom and assign this component as Custom Driver. Have your animation/timeline call ``Contact`` and ``Finished``. The example owns only timing; it does not silently change a character's limb mode.

**Example:** ``ApplicationInteractionDriver.cs``

.. raw:: html

   <!-- example: ApplicationInteractionDriver.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ApplicationInteractionDriver : MonoBehaviour, IControlInteractionDriver
       {
           private ControlInteractionRequest pending;

           public void Begin(ControlInteractionRequest request)
           {
               pending = request;
               // Start your animation; capture request in any asynchronous callback.
           }

           public void Contact() => pending?.Commit();

           public void Finished()
           {
               var request = pending;
               pending = null;
               request?.Complete();
           }

           public void Cancel(ControlInteractionRequest request)
           {
               if (pending == request) pending = null;
               // Stop animation/tweens owned by this request.
           }
       }
   }

For a genuinely asynchronous callback, close over the request passed to ``Begin`` instead of looking up the mutable pending field later. Request methods reject stale/inactive requests.

.. _uvs-scripting-interactions--commit-a-switch-once:

Commit a switch once
--------------------

Place the mechanical change in one commit path. The callback below toggles the switch at commit; wiring the same toggle again into Inspector ``On Commit`` would invoke it twice and could return the switch to its original position.

Use completion/cancellation to restore UI or input gates that belong to the gesture, not to replay the mechanical action. If ``TryBegin`` rejects the request, the caller decides whether to queue it, show feedback or invoke a deliberately chosen fallback. There is no automatic fallback that silently bypasses presentation requirements.

Assign a configured interaction and switch. Leave Inspector On ``Commit`` empty if the callback below is the gameplay action.

**Example:** ``SwitchInteractionBinding.cs``

.. raw:: html

   <!-- example: SwitchInteractionBinding.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SwitchInteractionBinding : MonoBehaviour
       {
           public ControlInteraction interaction;
           public SwitchAnimator target;

           public bool Activate()
           {
               if (!interaction || !target) return false;
               return interaction.TryBegin(() => target.Toggle());
           }
       }
   }

Call ``Cancel`` when abandoning the interaction. The action can be admitted even if an ``onStarted`` callback immediately cancels it; use completion/cancellation events to restore UI state.

.. _uvs-scripting-interactions--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed committed control interactions API </API/Interactions>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-interactions--controlinteraction:

ControlInteraction
~~~~~~~~~~~~~~~~~~

:ref:`ControlInteraction <uvs-api-interactions--controlinteraction>` gives the full declared contract.

+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                         | Role                                                                                                                                             |
+================================================================+==================================================================================================================================================+
| ``public virtual bool TryBegin(Action onCommit = null)``       | Requests a control interaction; ``true`` means admitted, not necessarily committed or completed.                                                 |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySetAnimationLayer(string layerName)`` | Select the next gesture layer by name while idle; empty clears the weight override.                                                              |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySetAnimationLayer(int layerIndex)``   | Select by current Animator layer index; -1 clears the override. Invalid layers or busy interactions return false.                                |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Begin()``                                | ``UnityEvent``-friendly wrapper around ``TryBegin``; it discards the bool result. Use ``TryBegin`` when the caller must handle refusal.          |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CommitAnimation()``                      | Commits the current interaction from an Animation Event entry point.                                                                             |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CompleteAnimation()``                    | Completes the current interaction from an Animation Event entry point.                                                                           |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Commit()``                               | Commits gameplay at most once for the addressed interaction request.                                                                             |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Complete()``                             | Completes an active request, committing first if necessary; after commit rechecks request identity before cleanup/completion notification.       |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Cancel()``                               | Cancels the active interaction, stops owned driver/transfer/animation state and invokes ``onCancelled``. Already committed gameplay is retained. |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                  | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.              |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                  | Role                                                                                                                                    |
+===================================+=========================================================================================================================================+
| ``public UnityEvent onStarted``   | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately.                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onCommit``    | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onCompleted`` | After the interaction completes. No payload; completion commits first if still needed.                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onCancelled`` | After an active interaction is cancelled. No payload; committed gameplay is not rolled back.                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-interactions--controlinteractionanimationevents:

ControlInteractionAnimationEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`ControlInteractionAnimationEvents <uvs-api-interactions--controlinteractionanimationevents>` gives the full declared contract.

+---------------------------------------------+------------------------------------------------------------------------------+
| Method                                      | Role                                                                         |
+=============================================+==============================================================================+
| ``public virtual void CommitAnimation()``   | Commits the current interaction from an Animation Event entry point.         |
+---------------------------------------------+------------------------------------------------------------------------------+
| ``public virtual void CompleteAnimation()`` | Completes the current interaction from an Animation Event entry point.       |
+---------------------------------------------+------------------------------------------------------------------------------+
| ``public virtual void CancelInteraction()`` | Relays an Animator cancellation event to the configured control interaction. |
+---------------------------------------------+------------------------------------------------------------------------------+

.. _uvs-scripting-interactions--controlinteractionrequest:

ControlInteractionRequest
~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`ControlInteractionRequest <uvs-api-interactions--controlinteractionrequest>` gives the full declared contract.

+----------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Method                     | Role                                                                                                                       |
+============================+============================================================================================================================+
| ``public bool Commit()``   | Commits only while this request is still the owner's ``ActiveRequest``. A stale request cannot commit a newer interaction. |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``public bool Complete()`` | Completes only this still-active request; stale callbacks return ``false``.                                                |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``public void Cancel()``   | Cancels only if this exact request remains active; it cannot cancel a newer request.                                       |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-interactions--icontrolinteractiondriver:

IControlInteractionDriver
~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`IControlInteractionDriver <uvs-api-interactions--icontrolinteractiondriver>` gives the full declared contract.

+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                             | Role                                                                                                                                      |
+====================================================+===========================================================================================================================================+
| ``void Begin(ControlInteractionRequest request)``  | Accepts ownership of one exact interaction request. Start application presentation and retain that request for delayed commit/completion. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| ``void Cancel(ControlInteractionRequest request)`` | Stops presentation owned by the supplied request and releases only that request's resources.                                              |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
