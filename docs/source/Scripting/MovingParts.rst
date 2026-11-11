.. _uvs-scripting-movingparts--exterior-motion-and-moving-parts:

Exterior motion and moving parts
================================

``MovingPart`` is a reusable motion actuator for a visible vehicle part. It can rotate, slide, follow a target or move under rate input around an authored neutral pose. Gameplay provides requests; the component owns constrained motion and pose application.

Use it for an independently controlled mechanism such as a turret base, sliding platform or adjustable exterior part. Keep the higher-level rule — who may operate it, what it aims at and whether an action is allowed — in the application or a dedicated mechanic.

For windshield wipers, ``Wipers`` owns stroke timing, parking and audio, while ``WiperBlade`` maps the phase to blade geometry. Use their dedicated controls rather than running a second actuator or timer on the same blade.

.. _uvs-scripting-movingparts--implementation-map:

Implementation map
------------------

+------------------------+--------------------------------------------------------------------------+
| Class                  | Responsibility                                                           |
+========================+==========================================================================+
| ``DamagePart``         | Defines released-part ownership that can stop vehicle-controlled motion. |
+------------------------+--------------------------------------------------------------------------+
| ``ExteriorModule``     | Base integration with the vehicle module lifecycle.                      |
+------------------------+--------------------------------------------------------------------------+
| ``MovingPart``         | Owns rotation/translation requests, constraints and scheduled motion.    |
+------------------------+--------------------------------------------------------------------------+
| ``WiperBlade``         | Maps a stroke phase to blade geometry.                                   |
+------------------------+--------------------------------------------------------------------------+
| ``Wipers``             | Owns blade timing, requests, parking and stroke audio.                   |
+------------------------+--------------------------------------------------------------------------+
| ``WiperSwitchBinding`` | Synchronizes a cockpit switch with the wiper module.                     |
+------------------------+--------------------------------------------------------------------------+

``MovingPart`` is an Exterior module configured on an owned child or with an explicit part transform. It captures a neutral pose once; ``CaptureNeutralPose`` deliberately replaces that baseline and clears requests.

.. _uvs-scripting-movingparts--rotation-and-translation:

Rotation and translation
------------------------

The neutral pose is the coordinate origin for a mechanism, not necessarily its closed or minimum position. A target is measured relative to that baseline. ``CaptureNeutralPose`` intentionally replaces the baseline, so call it while the model is at its authored neutral pose rather than at an arbitrary animated point.

A rotational mechanism can run from rate input, a target angle or world-target tracking. A translation uses a bounded metre offset and an explicit frame. Changing control mode changes the active request; use ``Stop()`` to clear retained rate/target/tracking ownership before another application system takes over the same part.

A custom actuator can reuse ``GetRotationFrame``, ``GetTranslationFrame``, ``ClampAngle`` and ``ClampPosition`` to remain consistent with configured limits. Do not implement a separate axis convention for a UI slider: map that slider to the existing normalized/target operation so the component remains the authority for geometry.

Choose the frame before tuning the limits. A translation in world space behaves differently from one along the vehicle's local axis when the vehicle turns. An anchor frame is useful when the mechanism belongs to a separate stable mounting point. Keep that anchor independent of the moving part to avoid measuring motion from a frame the actuator itself changes.

Rate and target requests also have different meanings. Rate input says “keep moving in this direction”; a target says “move to this bounded offset.” A hold button should release its rate request when input ownership ends. A workshop preset should request a target instead of simulating a held button until a guessed time elapses.

Rotation uses the local axis/forward, optional hinge anchor, signed angle limits and angular speed. Rate input supports full turns; target angles can use shortest-arc policy. ``AimAt`` follows a world point or transform around the allowed axis.

Translation uses metres from neutral in Part, Parent, World or Anchor space. Direction angles rotate the axis inside that frame. Parent motion is followed, and scale compensation preserves configured world travel. Invalid self/descendant anchors fall back to the neutral part frame.

.. _uvs-scripting-movingparts--operate-a-movingpart-and-read-its-state:

Operate a MovingPart and read its state
---------------------------------------

For a named door with Body/VehicleBodyPart, use the existing :ref:`open/close adapter and state guide <uvs-scripting-damage--open-a-named-part>`, or ``vehicle.parts`` as described in :ref:`vehicle entry points <uvs-scripting--what-is-available-directly-on-vehicle>`. A generic MovingPart has no ``Open()``/``Close()`` methods; it accepts normalized, angle, distance or rate requests.

+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Goal                                              | MovingPart API                                                                                                                        |
+===================================================+=======================================================================================================================================+
| Move to the end/start of configured travel        | ``SetNormalizedPosition(1)`` / ``SetNormalizedPosition(0)``. Normalized travel works across all four modes.                           |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Request an external clip/custom target explicitly | ``StartMotion(target)`` with normalized 0..1. Procedural modes route it to their normal target operation.                             |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Rotate toward an angle / slide toward a distance  | ``SetTargetAngle(degrees)`` / ``SetTargetPosition(metres)`` in the matching procedural mode.                                          |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Apply an immediate procedural pose                | ``SetAngle(degrees)`` / ``SetPosition(metres)``. These interrupt the previous operation.                                              |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Use a held input                                  | ``SetInput(-1..1)``; release with zero. See the existing :ref:`two-button example <uvs-scripting-movingparts--hold-button-slider>`.   |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Pause/interrupt a request                         | ``Stop()``; ``Cancel()`` also exposes cancellation through the common lifecycle. Neither represents successful arrival.               |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Disable movement policy                           | ``SetMotionEnabled(false)``. It clears the pending request; re-enabling does not resume an old command automatically.                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Read actual/reported progress                     | ``NormalizedPosition`` in 0..1; ``Angle`` in degrees or ``Position`` in metres for their procedural mode.                             |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Read demand                                       | ``TargetAngle``, ``TargetPosition``, ``Input`` in the matching procedural mode; ``playback.Target`` for normalized external requests. |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Read activity                                     | ``IsMoving``, ``IsOpening``, ``IsClosing``. Activity is not proof that an endpoint has been reached.                                  |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

Configure which end means open: **Increasing Is Opening** controls the event meaning, while **Reverse** mirrors geometry. Do not assume normalized 1 always means your application's open pose when you authored the opposite mapping. ``ReturnToNeutral()`` requests the captured zero offset in procedural modes, which may differ from the minimum limit; external modes request progress 0.

Use ``OpeningCompleted`` / ``ClosingCompleted`` for arrival and ``Moved(MovingPart)`` for actual/reported movement updates. ``MotionEnabledChanged(bool)`` reports a movement-policy change. The existing :ref:`operation-event example <uvs-scripting-movingparts--subscribe-to-operation-events-and-configure-cues>` shows subscriptions and cleanup; the :ref:`common lifecycle table <uvs-movingparts--lifecycle-and-inspector-callbacks>` covers begin/move/end/stop/cancel without duplicating those bindings here. A partially open target can complete successfully at its requested value. For Custom, use the existing :ref:`driver example <uvs-scripting-movingparts--custom-motion-driver>` to report progress and completion.

.. _uvs-scripting-movingparts--hold-button-slider:

Hold-button slider
------------------

The adapter stores both button states so releasing one button does not erase the other. It calculates a single signed rate request and stops on disable. This cleanup is important for touch controls and possession handovers, where the normal release event may never reach an object being disabled.

The example does not know the slider's axis, distance or speed. Those remain on ``MovingPart``, so the same input adapter can operate a differently authored mechanism without changing its code.

Configure translation geometry in the Inspector, then connect press/release callbacks to this component. Both buttons held result in zero. No keyboard convention is built into the moving part.

**Example:** ``SliderButtons.cs``

.. raw:: html

   <!-- example: SliderButtons.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SliderButtons : MonoBehaviour
       {
           public MovingPart slider;
       public MovingPartAudio doorAudio;
           private bool forward, backward;

           public void SetForward(bool pressed) { forward = pressed; Apply(); }
           public void SetBackward(bool pressed) { backward = pressed; Apply(); }
           private void Apply()
           {
               if (slider) slider.SetInput((forward ? 1 : 0) - (backward ? 1 : 0));
           }
           private void OnDisable()
           {
               forward = backward = false;
               if (slider) slider.Stop();
           }
       }
   }

``SetTargetPosition`` moves toward a bounded metre offset; ``SetPosition`` applies it immediately; ``SetNormalizedPosition`` maps the travel interval. ``ReturnToNeutral`` requests zero within limits. ``SetInput``\ (0) pauses; ``Stop`` clears rate/target/tracking.

Disabling clears commands at the current pose. A detached ``DamagePart`` ancestor cancels motion so physics owns debris. Controller scheduling normally advances the module; only use ``Tick`` for a loop you explicitly own.

.. _uvs-scripting-movingparts--direction-specific-motion-curves:

Direction-specific motion curves
--------------------------------

MovingPart.increasingMotionCurve and decreasingMotionCurve map normalized elapsed time to bounded travel progress for fixed-target rotation/translation. Linear is the default. Speed/translationSpeed sets average speed; the curve slope redistributes speed within the trip. Repeating the same target preserves progress, while retargeting starts from the actual pose. Instant setters and Stop cancel prior curve state. Rate input and aiming retain their speed-limited control. See :ref:`motion curve setup <uvs-movingparts--shape-movement-speed-with-curves>` for curve axes, fallbacks and physical-door behavior.

.. _uvs-scripting-movingparts--configure-curves-from-code:

Configure curves from code
~~~~~~~~~~~~~~~~~~~~~~~~~~

Assign the parts in the Inspector. This example gives both components a gentle start and stop in one direction and a faster initial closing/decreasing motion that slows at the end. Other geometry and speed settings stay in the part components.

.. raw:: html

   <!-- example: PartMotionCurves.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   public sealed class PartMotionCurves : MonoBehaviour
   {
       public MovingPart movingPart;
       public UltraVehicleSystem.VehicleBodyPart door;

       private static AnimationCurve SlowFinish() => new AnimationCurve(
           new Keyframe(0, 0, 2, 2), new Keyframe(1, 1, 0, 0));

       private void Awake()
       {
           if (movingPart) {
               movingPart.increasingMotionCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
               movingPart.decreasingMotionCurve = SlowFinish();
           }
           if (door) {
               door.openingMotionCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
               door.closingMotionCurve = SlowFinish();
           }
       }
   }

.. _uvs-scripting-movingparts--subscribe-to-operation-events-and-configure-cues:

Subscribe to operation events and configure cues
------------------------------------------------

This component can be attached to a UI/controller object. Assign its door, optional moving part and clips. It configures distinct start/arrival cues and a dedicated closing-arrival emitter, and subscribes/unsubscribes through the public API. The optional MovingPart callback uses the same Inspector event object that designers can wire without code.

.. raw:: html

   <!-- example: PartOperationEventsExample.cs -->

.. code-block:: csharp

   using UltraVehicleSystem;
   using UnityEngine;

   public sealed class PartOperationEventsExample : MonoBehaviour
   {
       public UltraVehicleSystem.VehicleBodyPart door;
       public MovingPart slider;
       public MovingPartAudio doorAudio;
       public Transform latchAudioAnchor;
       public AudioClip openingClip;
       public AudioClip closedClip;

       private void OnEnable()
       {
           if (door && doorAudio) {
               doorAudio.motionSource = door;
               door.OpeningStarted += OnOpening;
               door.ClosingCompleted += OnClosed;
               doorAudio.movementAudio.SetClips(PartMotionEvent.OpeningStarted, openingClip);
               doorAudio.movementAudio.SetClips(PartMotionEvent.ClosingCompleted, closedClip);
               var closing = doorAudio.movementAudio.closingCompleted;
               closing.overrideSettings = true;
               closing.audioAnchor = latchAudioAnchor;
               closing.volume = 0.8f;
               closing.spatialBlend = 1;
           }
           if (slider) slider.motionEvents.GetEvent(PartMotionEvent.OpeningCompleted).AddListener(OnSliderOpened);
       }

       private void OnDisable()
       {
           if (door && doorAudio) {
               doorAudio.motionSource = door;
               door.OpeningStarted -= OnOpening;
               door.ClosingCompleted -= OnClosed;
           }
           if (slider) slider.motionEvents.GetEvent(PartMotionEvent.OpeningCompleted).RemoveListener(OnSliderOpened);
       }

       public void OpenDoor() { if (door) door.Open(); }
       public void CloseDoor() { if (door) door.Close(); }
       private void OnOpening() => Debug.Log("Opening starts before the door moves.");
       private void OnClosed() => Debug.Log("The actual door has reached its closing target.");
       private void OnSliderOpened() => Debug.Log("The moving part reached its opening target.");
   }

The public IsOpening/IsClosing properties describe pending operations. On MovingPartAudio, audio settings and clip arrays can also be edited directly; GetSettings resolves a cue’s active override. PlayMotionAudio returns whether it played a cue; GetMotionAudioSource never creates a source. StopMotionAudio affects generated sources only. Interrupting an operation does not emit its completed event. See :ref:`event timing, endpoint and source ownership rules <uvs-movingparts--motion-events-and-four-audio-cues>`.

.. _uvs-scripting-movingparts--wipers:

Wipers
------

``Wipers`` belongs to the Exterior module category and owns blade clocks, parking and audio. ``WiperBlade`` owns geometry; ``WiperSwitchBinding`` connects an interior stalk to the exterior module. See :doc:`setup </Wipers>` and the :doc:`API </API/Wipers>`.

``Wipers`` owns a separate phase clock for each ``Wiper`` entry. ``WiperBlade`` remains geometry-only. Helpers must be listed explicitly; do not schedule another timer for the same blade. Existing entries inherit the module's running/speed/audio defaults unless individual settings are enabled, so equally configured blades remain synchronized.

Each entry has a unique, case-sensitive ``id``. ``independentSettings`` selects its authored ``running`` and ``cyclesPerMinute``; ``overrideAudio`` independently selects entry clips, volume and pitch synchronization. Entry ``audioSource`` can bind a dedicated voice. Independent rates/requests receive private generated voices when needed, while inherited synchronized entries can share the module's audio source without replaying the same stroke for each blade.

``SetRunning(bool)``, ``Toggle()`` and ``SetSpeed(float)`` operate on all entries; setting group speed intentionally replaces individual rates. ID overloads affect one blade, even when it inherits authored defaults. ``RestoreWiperControl(id)`` clears its runtime overrides. ``IsRunning`` reports any running request and ``IsParked`` requires all phases at zero; query one blade through ``IsWiperRunning(id)``, ``GetSpeed(id)`` and ``GetWiper(id).IsParked``/``CurrentPhase``.

Stopping completes that blade's current cycle. Zero speed pauses its phase, so a stopped blade at zero speed needs a positive rate to finish or an explicit ``Park(id)``/``ParkAll()`` for immediate parking. Disable parks every blade while retaining requests. Registration rejects duplicate IDs and reused helpers/blades; removal immediately parks and releases generated audio, preserving user-provided sources. Call ``CaptureRestPoses`` only at the intended neutral geometry.

``WiperStrokeStarted``, ``WiperRunningChanged``, ``WiperSpeedChanged`` and ``WiperParked`` identify individual entries. Aggregate ``StrokeStarted`` coalesces equal directions within one Tick; aggregate ``RunningChanged`` reports changes to the any-running state. Direct field edits do not publish API running/speed notifications. ``Tick`` advances once per rendered frame and rejects disabled modules and non-finite elapsed times.

.. _uvs-scripting-movingparts--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed general moving parts API </API/MovingParts>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-movingparts--ipartmotionsource:

IPartMotionSource
~~~~~~~~~~~~~~~~~

:ref:`IPartMotionSource <uvs-api-movingparts--ipartmotionsource>` gives the full declared contract.

-  ``event Action MotionAudioStopped`` — Requests stopping movement audio after interruption or disable.
-  ``event Action<PartMotionEvent> MotionOccurred`` — Reports an admitted movement phase to optional presentation receivers.

.. _uvs-scripting-movingparts--ivehiclemodule:

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

.. _uvs-scripting-movingparts--movingpart:

MovingPart
~~~~~~~~~~

:ref:`MovingPart <uvs-api-movingparts--movingpart>` gives the full declared contract.

-  ``public event System.Action ClosingCompleted`` — Current closing completed.
-  ``public event System.Action ClosingStarted`` — Current closing started.
-  ``public event System.Action MotionAudioStopped`` — Requests stopping movement audio after interruption or disable.
-  ``public event System.Action<bool> MotionEnabledChanged`` — // Reports a changed movement request after pending motion is stopped when disabling.
-  ``public event System.Action<PartMotionEvent> MotionOccurred`` — Reports an admitted movement phase to optional presentation receivers.
-  ``public event System.Action<MovingPart> Moved`` — // Reports this moving part after its actual pose changes.
-  ``public event System.Action OpeningCompleted`` — Current opening completed.
-  ``public event System.Action OpeningStarted`` — Current opening started.
-  ``public virtual void AimAt(Transform target)`` — Current aim at.
-  ``public virtual void AimAt(Vector3 worldPoint)`` — Current aim at.
-  ``public virtual void CaptureNeutralPose()`` — // Explicit rebasing for runtime authoring; repeated Configure never captures an animated pose.
-  ``public virtual float ClampAngle(float angle)`` — // Clamps to sorted travel limits when enabled; unrestricted parts retain unwrapped rotation.
-  ``public virtual float ClampPosition(float value)`` — Current clamp position.
-  ``public override void Configure(VehicleController vehicle)`` — Binds the component to its configured owner and selected source.
-  ``public virtual void GetRotationFrame(out Vector3 worldPivot, out Quaternion worldNeutralRotation)`` — // Read the neutral rotation frame without capturing/rebasing or moving the part.
-  ``public virtual void GetTranslationFrame(out Vector3 origin, out Vector3 direction)`` — // Shared by simulation and gizmos. Direction is unit length so all limits remain in metres.
-  ``public virtual void ReturnToNeutral()`` — Current return to neutral.
-  ``public virtual void SetAngle(float angle)`` — Current set angle.
-  ``public virtual void SetInput(float input)`` — Current set input.
-  ``public virtual void SetMotionEnabled(bool value)`` — Current set motion enabled.
-  ``public virtual void SetNormalizedPosition(float value)`` — Current set normalized position.
-  ``public virtual void SetPosition(float value)`` — Current set position.
-  ``public virtual void SetTargetAngle(float angle, bool shortestPath = true)`` — Current set target angle.
-  ``public virtual void SetTargetPosition(float value)`` — Current set target position.
-  ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` — Current step.
-  ``public virtual void StartMotion(float normalizedTarget)`` — Requests normalized travel in the selected mode.
-  ``public virtual void ReportProgress(float normalizedValue)`` — Reports externally produced progress for Animation/Custom integrations.
-  ``public virtual void CompleteCustomMotion()`` — Marks the active Custom operation successful; stopping/cancelling is not success.
-  ``public virtual void Cancel()`` — Cancels the pending operation and clears retained demands.
-  ``public virtual void Stop()`` — // Stops the current operation and clears the transient command that would otherwise continue it.
-  ``public virtual void Tick(float deltaTime)`` — Current tick.

.. _uvs-scripting-movingparts--partmotionaudio:

PartMotionAudio
~~~~~~~~~~~~~~~

:ref:`PartMotionAudio <uvs-api-movingparts--partmotionaudio>` gives the full declared contract.

+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Member                                                                          | Meaning                                                                                                                |
+=================================================================================+========================================================================================================================+
| ``public AudioClip[] GetClips(PartMotionEvent motionEvent)``                    | Returns the selected cue’s clip array by reference. Invalid event values throw ArgumentOutOfRangeException.            |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``public void SetClips(PartMotionEvent motionEvent, params AudioClip[] clips)`` | Replaces the selected clip array; null becomes an empty array. Invalid event values throw ArgumentOutOfRangeException. |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Audio member                                                             | Behavior                                                                                                                                                                         |
+==========================================================================+==================================================================================================================================================================================+
| ``public VehicleAudioSettings GetSettings(PartMotionEvent motionEvent)`` | Returns the selected cue override when Override Settings is enabled, otherwise returns the shared audioSettings instance. Invalid enum values throw ArgumentOutOfRangeException. |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-movingparts--partmotionevents:

PartMotionEvents
~~~~~~~~~~~~~~~~

:ref:`PartMotionEvents <uvs-api-movingparts--partmotionevents>` gives the full declared contract.

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                                                                            |
+=============================================================+====================================================================================================================================================+
| ``public UnityEvent openingStarted``                        | Inspector callback for opening Started. On PartMotionAudio this is the optional settings override for that cue.                                    |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent openingCompleted``                      | Inspector callback for opening Completed. On PartMotionAudio this is the optional settings override for that cue.                                  |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent closingStarted``                        | Inspector callback for closing Started. On PartMotionAudio this is the optional settings override for that cue.                                    |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent closingCompleted``                      | Inspector callback for closing Completed. On PartMotionAudio this is the optional settings override for that cue.                                  |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent GetEvent(PartMotionEvent motionEvent)`` | Returns the selected Inspector UnityEvent for subscribing with AddListener/RemoveListener. Invalid event values throw ArgumentOutOfRangeException. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-movingparts--steeringpart:

SteeringPart
~~~~~~~~~~~~

:ref:`SteeringPart <uvs-api-movingparts--steeringpart>` gives the full declared contract.

.. _uvs-scripting-movingparts--methods:

Methods
^^^^^^^

+-------------------------------------------------------------+------------------------------------------------------+-----------------------------+
| Signature                                                   | Role and behavior                                    | Arguments and result        |
+=============================================================+======================================================+=============================+
| ``public override void Configure(VehicleController owner)`` | Resolves the fallback vehicle when none is assigned. | ``owner`` — Owning vehicle. |
+-------------------------------------------------------------+------------------------------------------------------+-----------------------------+

.. _uvs-scripting-movingparts--vehiclemodule:

VehicleModule
~~~~~~~~~~~~~

:ref:`VehicleModule <uvs-api-modules--vehiclemodule>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                                   |
+===========================================================================================+========================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                          | Role                                                                                                              |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-movingparts--wiperblade:

WiperBlade
~~~~~~~~~~

:ref:`WiperBlade <uvs-api-wipers--wiperblade>` gives the full declared contract.

.. _uvs-scripting-movingparts--methods-1:

Methods
^^^^^^^

+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                     | Role and behavior                                                                                        | Arguments and result |
+===============================================+==========================================================================================================+======================+
| ``public virtual void CaptureRestPose()``     | Captures the currently authored rest pose for this geometry mapper or blade.                             | —                    |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void ParkImmediate()``       | Places the blade at its parked pose without waiting for a wiper cycle.                                   | —                    |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetValue(float value)`` | Applies normalized blade stroke using the captured spindle/rest geometry; it does not run a wiper clock. | —                    |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-scripting-movingparts--wipers-1:

Wipers
~~~~~~

:ref:`Wipers <uvs-api-wipers--wipers>` gives the full declared contract.

.. _uvs-scripting-movingparts--events-and-inspector-callbacks:

Events and Inspector callbacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Member                                                    | Meaning                                                                                                                   |
+===========================================================+===========================================================================================================================+
| ``public event Action Parked``                            | When wipers reach their parked state. No payload.                                                                         |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> RunningChanged``              | When the wiper running request changes. Payload: bool; a stop can still finish the current cycle.                         |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<float> SpeedChanged``               | After ``SetSpeed`` changes requested wiper speed. Payload: configured cycle-speed value; zero pauses motion.              |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> StrokeStarted``               | When a wiper stroke starts. Payload: returning bool, ``true`` for the return stroke and ``false`` for the outward stroke. |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<string> WiperParked``               | When an entry reaches/is immediately placed at its parked pose; payload is its ID.                                        |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<string, bool> WiperRunningChanged`` | After an API changes an entry's effective running request; payload is its ID and new bool request.                        |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<string, float> WiperSpeedChanged``  | After an API changes an entry's effective speed; payload is its ID and cycles per minute.                                 |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<string, bool> WiperStrokeStarted``  | Reports entry ID and stroke direction: false for outward, true for return. Entries have independent phase clocks.         |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-movingparts--methods-2:

Methods
^^^^^^^

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                       | Role and behavior                                                                                                                                                                                                                                   | Arguments and result |
+=================================================================+=====================================================================================================================================================================================================================================================+======================+
| ``public virtual void CaptureRestPoses()``                      | Captures rest poses for the wiper geometry owned by the module.                                                                                                                                                                                     | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Configure(VehicleController vehicle)``   | Applies current blade pose only during Play Mode so Edit Mode configuration does not recapture an animated neutral pose.                                                                                                                            | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual AudioSource GetAudioSource(string id = null)`` | Returns the shared source or the last resolved source for the selected wiper ID without modifying Audio Settings.                                                                                                                                   | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual float GetSpeed(string id)``                    | Reports the identified entry's effective cycles per minute. Returns zero for an unresolved ID.                                                                                                                                                      | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual Wiper GetWiper(string id)``                    | Finds a blade entry by exact ID. Returns null for blank, missing or ambiguous duplicate IDs.                                                                                                                                                        | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool IsWiperRunning(string id)``               | Reports the identified entry's effective request, including runtime overrides. False for an unresolved ID; a stopped blade can still be finishing its cycle.                                                                                        | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool Park(string id)``                         | Stops and immediately parks one entry without completing its cycle; returns false for an unresolved ID.                                                                                                                                             | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void ParkAll()``                               | Stops every entry and immediately parks all blades and stops their stroke audio.                                                                                                                                                                    | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool RegisterWiper(Wiper wiper)``              | Adds an entry with a unique, nonblank ID. Returns false for null, duplicate IDs, duplicate entries or reused helper/blade references.                                                                                                               | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool RestoreWiperControl(string id)``          | Clears one entry's runtime running/speed overrides, returning it to its current independent authored settings or shared defaults. Returns false for unresolved IDs.                                                                                 | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetRunning(bool value)``                  | Requests the wiper running state; stopping finishes the current cycle before parking.                                                                                                                                                               | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool SetRunning(string id, bool value)``       | The bool-only overload sets every entry's request and clears per-entry running overrides. The ID overload changes only that entry and returns false for an unresolved ID. Stopping finishes the current cycle.                                      | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetSpeed(float speed)``                   | Changes wiper cycle speed; zero pauses cycle motion.                                                                                                                                                                                                | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool SetSpeed(string id, float speed)``        | The float-only overload applies the rate to every entry and clears individual speed overrides. The ID overload changes only one rate. Rates are clamped to zero or greater; non-finite values are rejected. ID overload returns false on rejection. | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Tick(float deltaTime)``                   | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.                                                                                                                 | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Toggle()``                                | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                                                                                                                                 | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool Toggle(string id)``                       | The no-argument overload stops all entries if any is requested running, otherwise starts all. The ID overload toggles one entry and returns false for an unresolved ID.                                                                             | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool UnregisterWiper(string id)``              | Immediately parks and removes the identified entry and releases its generated audio source. User-provided audio sources are retained. Returns false for unresolved IDs.                                                                             | —                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

-  ``public event Action<Wiper, bool, float> StrokeAudioRequested`` — Wiper lifecycle and presentation notification.

-  ``public event Action<Wiper> WiperRemoved`` — Wiper lifecycle and presentation notification.

-  ``public event Action AudioStopped`` — Wiper lifecycle and presentation notification.

-  ``public event Action StrokeBatchStarted`` — Wiper lifecycle and presentation notification.

.. _uvs-scripting-movingparts--wiperswitchbinding:

WiperSwitchBinding
~~~~~~~~~~~~~~~~~~

:ref:`WiperSwitchBinding <uvs-api-wipers--wiperswitchbinding>` gives the full declared contract.

.. _uvs-scripting-movingparts--methods-3:

Methods
^^^^^^^

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                           | Role and behavior                                                                                                                   | Arguments and result |
+=====================================================+=====================================================================================================================================+======================+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         | —                    |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | —                    |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-scripting-movingparts--custom-motion-driver:

Custom motion driver
--------------------

Assign a component like this to **Motion > Custom Driver** (or the root **Custom Driver** on MovingPart/VehicleBodyPart). It uses explicit references, stores its authored endpoints separately, performs all pose writes itself and reports actual progress. The same driver contract is shared by body panels, aircraft parts and control geometry; it receives the requesting playback instance.

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   public sealed class LocalSlideDriver : MonoBehaviour, ICustomPartMotion
   {
       public Transform part;
       public Vector3 closedLocalPosition;
       public Vector3 openLocalPosition;
       [Min(0.001f)] public float fullTravelSeconds = 1;
       private PartMotionPlayback active;

       public void BeginMotion(PartMotionPlayback motion)
       {
           if (active != null && active != motion) active.Cancel();
           active = motion;
           if (!part) motion.Cancel();
       }

       public void TickMotion(PartMotionPlayback motion, float deltaTime)
       {
           if (!part) { motion.Cancel(); return; }
           float value = Mathf.MoveTowards(motion.Value, motion.Target,
               deltaTime / Mathf.Max(0.001f, fullTravelSeconds));
           part.localPosition = Vector3.Lerp(closedLocalPosition, openLocalPosition, value);
           int revision = motion.Revision;
           motion.ReportProgress(value);
           // A progress listener may have stopped/replaced the operation.
           if (motion.IsActive && motion.Revision == revision && Mathf.Approximately(value, motion.Target)) motion.Complete();
       }

       public void StopMotion(PartMotionPlayback motion, PartMotionStopReason reason)
       {
           if (active == motion) active = null;
           // Stop any external tween/task here. Completed is distinct from Cancelled/Stopped.
       }

       private void OnDisable()
       {
           var previous = active; active = null;
           previous?.Cancel();
       }
   }

Do not share a stateful driver between unrelated simultaneous mechanisms unless it explicitly tracks each requesting playback. The Animator root/part and other external objects remain your responsibility in Custom mode.

For a UnityEvents-only adapter, keep a reference to the MovingPart, connect **Signals and callbacks > On Move Requested** to your ``MoveTo(float)`` and **On Stop Requested** to your stop method. Feed progress back through ``MovingPart.ReportProgress`` and success through ``MovingPart.CompleteCustomMotion``. VehicleBodyPart uses the same names; control animators expose ``ReportMotionProgress``, ``CompleteCustomMotion``, ``StopMotion`` and ``CancelMotion``. These public component methods can also be targeted from Inspector UnityEvents. Use ``playback`` on a nested HandleMotion/AnchoredRotation for direct C# integrations.

For C# observers, subscribe to ``part.Signals.Began``, ``part.Signals.Moved``, ``part.Signals.Ended``, etc., and remove those subscriptions in your cleanup. ``part.StartMotion(1)`` requests the end pose; ``part.Cancel()`` interrupts it. Built-in normalized targeting continues to work in procedural modes.

``Signals and callbacks`` work in **Rotation, Translation, Animation and Custom**. Procedural movement does not require an Animator. Start, progress, successful completion, stop and cancellation describe the operation independently of its motion implementation; changing direction cancels the previous operation before starting the replacement. ``On Tick`` receives elapsed seconds when active playback is updated. A stop or cancellation does not report successful completion. In Custom mode, your implementation must report progress and explicitly complete the operation when it actually finishes.

.. _uvs-scripting-movingparts--tutorial-your-own-animator-and-door-animation-events:

Tutorial: your own Animator and door Animation Events
-----------------------------------------------------

This tutorial works with both **VehicleBodyPart (Body Part)** and **MovingPart (Moving Part)**. Use **Custom** when your Animator Controller owns the animation and its clips report completion back to the part. The steps below use Body Part; for Moving Part, use the corresponding **Moving Part > Motion**, **Motion Events** and **Signals and callbacks** fields.

1. On the door, set **Body Part > Motion > Custom** and leave **Custom Driver** empty.
2. In your Animator Controller, create ``Open`` and ``Close`` trigger parameters and transitions to the corresponding non-looping clips. Let each clip reach its completion event before transitioning out.
3. Under **Body Part > Motion Events > Opening Started**, add the object with your Animator, select **Animator > SetTrigger(string)** and enter ``Open``. Under **Motion Events > Closing Started**, connect the same method with ``Close``.
4. Save the following component as ``DoorAnimationEvents.cs``, add it to the **same GameObject as the Animator**, and assign the door component to **Door Animation Events > Body Part**. The door itself may be on another object.

.. code-block:: csharp

   using UltraVehicleSystem;
   using UnityEngine;

   public class DoorAnimationEvents : MonoBehaviour
   {
       public VehicleBodyPart bodyPart;

       public void OpeningFinished()
       {
           bodyPart.ReportProgress(1f);
           bodyPart.CompleteCustomMotion();
       }

       public void ClosingFinished()
       {
           bodyPart.ReportProgress(0f);
           bodyPart.CompleteCustomMotion();
       }
   }

For a Moving Part, replace the field declaration in the relay with ``public MovingPart bodyPart;`` and assign your Moving Part component to that field. Both components expose ``ReportProgress(float)`` and ``CompleteCustomMotion()``, so the two completion methods remain unchanged.

5. In Unity's **Animation** window, add an Animation Event at the end of the opening clip and select ``OpeningFinished``. At the end of the closing clip, select ``ClosingFinished``. Animation Events call components on the Animator's GameObject; they are not Inspector UnityEvent lists.
6. Request movement through ``bodyPart.Open()`` / ``bodyPart.Close()`` or your usual interaction. On arrival, the relay reports the endpoint and completes the active operation, firing **Motion Events > Opening Completed / Closing Completed** and **Signals and callbacks > On End / On Stop**. Do not use ``Stop()`` to report success: it interrupts the operation without firing completion.

You can also attach your own public methods to **Signals and callbacks > On Begin** in any motion mode. Its dynamic ``float`` argument is the requested target (``1`` to open, ``0`` to close). If your external controller supports interruption, connect **Signals and callbacks > On Stop Requested** to its stop method; ensure interrupted clips do not subsequently report completion for a replacement operation.
