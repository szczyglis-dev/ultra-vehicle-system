.. _uvs-scripting-events--events-and-telemetry:

Events and telemetry
====================

Events connect the vehicle to UI, audio and application rules without making those consumers run the mechanics themselves. There are two useful kinds of observation: snapshots for continuously changing state, and notifications for accepted transitions such as ignition, entry or a committed interaction.

A display usually needs the latest ``Telemetry``; a quest or interaction system usually needs a particular event. Choosing the right source avoids reconstructing meaning from raw velocities or repeatedly comparing Inspector fields.

.. _uvs-scripting-events--configure-built-in-responses-in-the-inspector-first:

Configure built-in responses in the Inspector first
---------------------------------------------------

For collision and landing sound, configure Audio/Damage Audio using :ref:`collision and landing sound setup <uvs-audio--inspector-quick-start-collision-and-landing-sounds>`. For an authored control action, wire the Inspector's On Commit UnityEvent using :ref:`ControlInteraction <uvs-controlinteractions--inspector-quick-start-wire-a-ui-action>`.

Typed C# events listed below are not automatically Inspector UnityEvent fields. Custom subscribers require code (or an application adapter); assigning a clip to Event Audio needs no custom subscription script.

.. _uvs-scripting-events--effect-event-ownership:

Effect event ownership
----------------------

Subscribe directly to the component that owns a mechanic. Collision contacts are published by VehicleController.Impacted as Impact; qualified wheel touchdowns by Suspension.Landed as LandingEvent. DamageAudio listens to both and keeps sound thresholds independent of damage. Nonphysical scripted damage can also use Damage.Hit.

Stabilization publishes Overturned and Recovered with the Telemetry snapshot that caused the transition. These events work without an audio component or custom event hub.

Events and EventAudio are optional application-defined channels. Configure a custom ID such as ``ApplicationAlert`` and matching recordings on EventAudio, assign its Events reference, then call Events.Publish with that ID, intensity and position. No built-in mechanic translates its events into string IDs. Disable or remove these custom components without affecting standard audio or physics.

Pair direct subscriptions with unsubscriptions in OnEnable/OnDisable. DamageAudio updates its Suspension bindings when owned modules are registered, removed or reconfigured; repeated configuration does not duplicate listeners. It ignores disabled or foreign sources and keeps generated sources under its Audio core's mute and mix controls.

.. _uvs-scripting-events--implementation-map:

Implementation map
------------------

+-----------------------+----------------------------------------------------------------------------------------------------------+
| Class                 | Responsibility                                                                                           |
+=======================+==========================================================================================================+
| ``Events``            | Publishes application-defined custom effect events.                                                      |
+-----------------------+----------------------------------------------------------------------------------------------------------+
| ``Impact``            | Stores copied collision information for deferred consumers.                                              |
+-----------------------+----------------------------------------------------------------------------------------------------------+
| ``LandingEvent``      | Copies qualified wheel landing height, flight time, incoming speed, load, intensity and force estimates. |
+-----------------------+----------------------------------------------------------------------------------------------------------+
| ``Telemetry``         | Carries the cached vehicle readings used by displays and observers.                                      |
+-----------------------+----------------------------------------------------------------------------------------------------------+
| ``VehicleController`` | Publishes command, configuration, ownership, collision and post-pipeline notifications.                  |
+-----------------------+----------------------------------------------------------------------------------------------------------+
| ``VehicleModule``     | Exposes lifecycle notifications around registered module work.                                           |
+-----------------------+----------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-events--subscribe-to-a-components-events:

Subscribe to a component's events
---------------------------------

An event lets a component notify your application when something happens. For example, ``Engine.EngineStateChanged`` reports an ignition/shutdown state change, while ``PassengerSeat.Entered`` reports that a body has actually occupied the seat. Subscribe to the component that owns the result you need, rather than reconstructing it from input or polling every frame.

A C# subscription has three parts: the source instance, the event and a handler with matching arguments. ``engine.EngineStateChanged += OnEngineStateChanged`` adds the handler; ``-=`` removes that same handler from that same engine. An ``Action<bool>`` event needs a handler accepting one bool. ``PassengerSeat.Exited`` needs a body and ``PassengerExitReason``, in that order.

Subscribe in ``OnEnable`` and unsubscribe in ``OnDisable`` for an observer that should follow its Unity enabled lifetime. Use named methods, or retain a delegate if using a lambda. Writing a new lambda when unsubscribing creates another delegate and does not remove the original subscription.

.. _uvs-scripting-events--bind-engine-and-seat-state:

Bind engine and seat state
~~~~~~~~~~~~~~~~~~~~~~~~~~

Assign the engine and seat in the Inspector. The example reads their initial state, then updates only when their events fire. Reading initial state matters because subscribing does not replay earlier events: an already running engine or occupied seat may not change again soon.

**Example:** ``VehicleEventBinding.cs``

.. raw:: html

   <!-- example: VehicleEventBinding.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class VehicleEventBinding : MonoBehaviour
       {
           public Engine engine;
           public PassengerSeat seat;
           public bool EngineRunning { get; private set; }
           public bool SeatOccupied { get; private set; }

           private Engine subscribedEngine;
           private PassengerSeat subscribedSeat;

           private void OnEnable() => Bind(engine, seat);
           private void OnDisable() => Unsubscribe();

           public void Bind(Engine nextEngine, PassengerSeat nextSeat)
           {
               Unsubscribe();
               engine = nextEngine;
               seat = nextSeat;
               EngineRunning = engine && engine.EngineRunning;
               SeatOccupied = seat && seat.Occupant;
               if (!isActiveAndEnabled) return;

               subscribedEngine = engine;
               subscribedSeat = seat;
               if (subscribedEngine)
                   subscribedEngine.EngineStateChanged += OnEngineStateChanged;
               if (subscribedSeat)
               {
                   subscribedSeat.Entered += OnEntered;
                   subscribedSeat.Exited += OnExited;
               }
           }

           private void Unsubscribe()
           {
               if (subscribedEngine)
                   subscribedEngine.EngineStateChanged -= OnEngineStateChanged;
               if (subscribedSeat)
               {
                   subscribedSeat.Entered -= OnEntered;
                   subscribedSeat.Exited -= OnExited;
               }
               subscribedEngine = null;
               subscribedSeat = null;
           }

           private void OnEngineStateChanged(bool running) => EngineRunning = running;
           private void OnEntered(PassengerBody body) => SeatOccupied = true;
           private void OnExited(PassengerBody body, PassengerExitReason reason)
               => SeatOccupied = false;
       }
   }

Call ``Bind(nextEngine, nextSeat)`` when the application changes vehicles. It removes old subscriptions before adding new ones and captures the actual subscribed instances for cleanup. Merely assigning another Inspector field while enabled does not move an existing subscription. The properties above are ready for a UI adapter; they do not start the engine, enter a seat or change input ownership.

.. _uvs-scripting-events--inspector-callbacks-and-c-events:

Inspector callbacks and C# events
---------------------------------

C# events use ``+=`` and ``-=``. Inspector callbacks are ``UnityEvent`` fields: configure them in the Inspector, or use ``AddListener`` and ``RemoveListener`` for runtime listeners. For example, ``ControlInteraction.onCommit`` is a ``UnityEvent``, not an event named ``Commit``; ``Commit()`` is the operation that commits the interaction.

For a runtime listener, pair ``interaction.onCommit.AddListener(OnCommitted)`` with ``interaction.onCommit.RemoveListener(OnCommitted)`` at the same lifecycle boundary. ``OnCommitted`` takes no arguments for this callback. Configure persistent Inspector listeners on the component itself; removing a runtime listener is not a request to erase those Inspector bindings.

Choose the notification boundary deliberately. A switch request event means the requested detent changed; a settled event means its visible travel finished. A successful access request means the sequence started; seat entry means occupancy changed. Use the owning type's :ref:`API event table <uvs-api--event-subscriptions-and-payloads>` for the exact payload and timing. Keep a gameplay action in one commit path so an Inspector listener and a supplied callback do not invoke it twice.

.. _uvs-scripting-events--choose-the-observation-point:

Choose the observation point
----------------------------

The word “after” in ``AfterPhysicsStep`` refers to completion of the package's ordered module work. Unity still owns native simulation timing. If an observer needs a result from a later native collision callback, use that callback's notification rather than assuming that an additional native simulation has just occurred.

Keep synchronous handlers short. Copy the values needed for later UI or application work and return. For a buffered history, retain value snapshots rather than a reference to a live ``Collision``. For asynchronous processing, the application is responsible for thread boundaries; event delivery itself is on Unity's main thread.

``AfterPhysicsStep`` publishes the immutable telemetry snapshot after the module pipeline. It describes the outputs from that pipeline and the current cached physics readings; it is not a separate extra physics simulation. Cache it for UI rendering.

Action events generally report actual transitions made through public methods. Assigning a public field does not necessarily invoke the same validation/events. Continuous observers report resolved state. Publishers run synchronously on Unity's main thread; avoid re-entering the same action from its event.

Use a copied ``Impact`` when work outlives a collision callback. A live Unity ``Collision`` belongs to that callback. ``Impact.Telemetry`` carries the vehicle’s latest completed snapshot; check ``HasTelemetry`` for manually constructed impacts. Contact-time point, normal, velocity and impulse remain separate from this cached snapshot.

.. _uvs-scripting-events--diagnostic-snapshot:

Diagnostic snapshot
-------------------

Read ``vehicle.Telemetry`` or subscribe to ``AfterPhysicsStep`` for one consistent set of readings. ``Position`` and ``Rotation`` describe the chassis in world space. ``Velocity`` is in m/s, ``Acceleration`` in m/s² and ``AngularVelocity`` in radians/second. ``LocalVelocity`` and ``LocalAcceleration`` use chassis axes: X right, Y up, Z forward. Acceleration includes gravity; ``SpecificForce`` subtracts it, so a stationary supported vehicle reads about 1 G and free fall about 0 G. ``FixedTime`` and ``DeltaTime`` identify the sample's simulation time.

The snapshot also contains mass and centre of mass, the sampled ``InputCommand``, direct-control status, engine running state and torque, driven-wheel RPM, signed gear ratio, shift state, clutch engagement and slip, and fuel amount, capacity, fraction and consumption. Missing optional modules produce zero/false readings; ``HasFuelTank`` distinguishes an absent tank from an empty one. A disabled tank reports its remaining fuel and zero consumption.

When **Setup > Telemetry > Per-wheel diagnostics > Wheel Details** is enabled, ``Wheels`` contains a copied read-only entry for every configured wheel, in ``vehicle.Wheels`` order. Each entry reports hub pose, signed RPM and angular speed, tire circumference speed, steering, submitted motor/brake torque, suspension extension/compression, contact point/normal/force and longitudinal/lateral slip. Check ``IsOperational``, ``Grounded`` and ``HasGroundHit`` before interpreting contact data. Supplemental tread support may report ``Grounded`` without a detailed wheel hit. See :ref:`the field reference <uvs-api-events--wheeltelemetry>` for units and availability.

Direct control derives motion and tire spin from the commanded poses. Its contact force is an estimate of static support and its slip readings are zero; they do not represent a physical tire-force solution. Native-mode contact readings come from the preceding Unity physics solve, while submitted torques reflect the current module pipeline. The wheel pose is the unsmoothed hub pose, rather than the rendered visual interpolation.

Snapshots retain their values when stored for history, including the wheel list. ``Telemetry.Wheels`` is a ``WheelTelemetryCollection`` value: up to four entries are stored inline, and larger rigs allocate only their extra-entry array. Direct indexing and foreach avoid collection boxing. Converting to ``IReadOnlyList<WheelTelemetry>`` or another interface boxes the value; retain the concrete type in hot paths. Native wheel-name reads still produce strings, so complete telemetry capture is not allocation-free. The public ``Telemetry`` constructor builds a motion-only snapshot; extended module/wheel readings are populated by ``VehicleController``.

.. _uvs-scripting-events--observe-without-polling-physics:

Observe without polling physics
-------------------------------

The component initializes from ``Telemetry`` before subscribing, so a newly opened readout can show the current cached state immediately. It captures the subscribed vehicle separately from the editable ``vehicle`` field. Cleanup therefore removes the handler from the object that actually owns it, even if the field was changed in the Inspector.

Expose read-only properties to a UI framework and let that framework decide formatting and refresh frequency. The mechanical event should not depend on a particular text label, canvas or unit display.

Attach this to a UI/controller object and assign the vehicle. It exposes values for your UI framework; no UI package is required. It subscribes once and removes that subscription on disable.

**Example:** ``VehicleReadout.cs``

.. raw:: html

   <!-- example: VehicleReadout.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class VehicleReadout : MonoBehaviour
       {
           public VehicleController vehicle;
           public float SpeedKph { get; private set; }
           public float Rpm { get; private set; }
           private VehicleController subscribed;

           private void OnEnable()
           {
               subscribed = vehicle;
               if (!subscribed) return;
               Receive(subscribed.Telemetry);
               subscribed.AfterPhysicsStep += Receive;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.AfterPhysicsStep -= Receive;
               subscribed = null;
           }

           private void Receive(Telemetry state)
           {
               SpeedKph = state.SpeedKph;
               Rpm = state.Rpm;
           }
       }
   }

Rebind the component when changing its vehicle; merely editing the field while enabled does not move the captured subscription.

.. _uvs-scripting-events--state-and-lifecycle-events:

State and lifecycle events
--------------------------

Prefer the publisher closest to the rule you are implementing. A seat's ``Entered`` event means occupancy has changed; an access sequence's ``Finished`` event means that sequence has ended. Those are different moments and can have different outcomes after cancellation. Similarly, an accepted damage hit and a completed geometry upload serve different consumers.

When implementing a derived component, preserve the relationship between state mutation and notification. Publish success only after the corresponding state is valid. Callers may inspect the component synchronously inside a handler, so notifying before updating its state exposes an inconsistent result.

+------------------------+----------------------------------------------------------------------------------------------------------+
| Source                 | Observe                                                                                                  |
+========================+==========================================================================================================+
| ``ControlInteraction`` | Inspector callbacks ``onStarted``, ``onCommit``, ``onCompleted`` and ``onCancelled``                     |
+------------------------+----------------------------------------------------------------------------------------------------------+
| ``Damage``             | Accepted ``DamageHit`` snapshots                                                                         |
+------------------------+----------------------------------------------------------------------------------------------------------+
| ``Engine``             | Ignition and accepted gear changes                                                                       |
+------------------------+----------------------------------------------------------------------------------------------------------+
| ``FuelTank``           | Quantity change, empty transition and actual fuel increase                                               |
+------------------------+----------------------------------------------------------------------------------------------------------+
| ``PassengerSeat``      | ``Entered``, ``Exited``, ``ControllerChanged`` and custom ``ResetRequested``                             |
+------------------------+----------------------------------------------------------------------------------------------------------+
| ``Suspension``         | ``Landed(LandingEvent)`` at first wheel contact; ``LandingCompleted(LandingEvent)`` at all-wheel support |
+------------------------+----------------------------------------------------------------------------------------------------------+
| ``VehicleController``  | Configuration, input source, module membership, drive profile, teleport and sampled command              |
+------------------------+----------------------------------------------------------------------------------------------------------+

Use named handlers or retain delegate references when unsubscribing. A protected Raise helper emits a notification; it does not implement the corresponding state change for a replacement.

.. _uvs-scripting-events--opening-and-closing-operations:

Opening and closing operations
------------------------------

VehicleBodyPart and MovingPart publish OpeningStarted, OpeningCompleted, ClosingStarted and ClosingCompleted; motionEvents exposes the same four UnityEvents for Inspector bindings. Start precedes pose movement; completion follows actual arrival. Interrupted/reversed operations do not synthesize success. VehicleBodyPart.OpenChanged reports changes to the requested open/closed state. See :ref:`motion event timing and audio <uvs-movingparts--motion-events-and-four-audio-cues>` and the :doc:`public API </API/MovingParts>`.

.. _uvs-scripting-events--wheel-landing-events:

Wheel landing events
--------------------

Subscribe to ``Suspension.Landed`` for one notification at first upright wheel support after the configured minimum airborne time. Subscribe to ``LandingCompleted`` for the later arrival of all operational wheel rays. Both can fire in one step on a flat landing. Completion does not mean settled springs or full wheel load. Teleport, reconfiguration and disable cancel pending observation. Event delivery remains available with ``landingResponse=false``; disabling the Suspension component stops it.

The immutable :ref:`LandingEvent <uvs-api-events--landingevent>` includes Height (centre-of-mass apex descent along gravity, metres), AirTime (seconds), ImpactSpeed (surface-relative normal incoming m/s), SupportForce (sum of current native WheelHit forces), Intensity, contact position/normal/collider and IsRebound. EstimatedImpulse is chassis mass × incoming normal speed. EstimatedForce is that momentum divided by the physics step; neither is a measured contact impulse or peak force. These estimates describe incoming severity even when predictive absorption has softened the native first contact. Later axle contacts can increase ImpactSpeed in LandingCompleted.

Use a handler such as ``void OnLanding(LandingEvent value)`` and pair ``suspension.Landed += OnLanding`` with ``suspension.Landed -= OnLanding``. For a sound integration, map ``value.Intensity`` to gain or configure Damage Audio → Landing Sound. DamageAudio receives the copied LandingEvent directly, including intensity and contact position. A genuine assisted rebound can produce another event after sufficient unsupported time, marked IsRebound; resting contact updates do not repeat the event. Raising helpers on derived Suspension classes retain subscribers; replacing the mechanic owns its event timing.

.. _uvs-scripting-events--events-reference:

Events reference
----------------

For event names, arguments and firing conditions grouped by declaring class, see :doc:`Events reference </Scripting/EventsReference>`.

.. _uvs-scripting-events--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed telemetry and feedback events API </API/Events>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-events--events:

Events
~~~~~~

:ref:`Events <uvs-api-events--events>` gives the full declared contract.

-  ``public event Action<EffectEvent> Raised`` — Current raised.
-  ``public virtual void Publish(string id, float intensity, Vector3 position)`` — Current publish.

.. _uvs-scripting-events--ivehiclemodule:

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

.. _uvs-scripting-events--telemetry:

Telemetry
~~~~~~~~~

-  **Telemetry** — ``public bool HasSection(TelemetrySections section)`` — Checks availability flags captured with this snapshot.

-  **Telemetry** — ``public float GetSpeed(SpeedUnit unit)`` — Returns speed from the captured snapshot in the requested unit.

.. _uvs-scripting-events--tirefeedback:

TireFeedback
~~~~~~~~~~~~

:ref:`TireFeedback <uvs-api-events--tirefeedback>` gives the full declared contract.

+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                   |
+=========================================================================+========================================================================================================+
| ``public override void Configure(VehicleController v)``                 | Resizes contact storage and clears surface caches for the configured wheel set.                        |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Samples wheel contact/activity and resolves presentation surfaces, then publishes changes and Sampled. |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public virtual void ClearSurfaceCache()``                             | Invalidates cached collider-to-effect-surface resolutions so later feedback can resolve again.         |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                     | Role                                                                                                                      |
+======================================================================+===========================================================================================================================+
| ``public event Action Sampled``                                      | After TireFeedback updates its wheel/contact classification. No payload; read the component's current cached feedback.    |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<int, bool> WheelGroundedChanged``              | When a wheel's feedback grounded state changes. Payload: wheel index and grounded bool.                                   |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<int, TireSurfaceProfile> WheelSurfaceChanged`` | When a wheel's selected presentation surface changes. Payload: wheel index and ``TireSurfaceProfile``, possibly ``null``. |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> SkiddingChanged``                        | When aggregate feedback skid state changes. Payload: bool.                                                                |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-events--vehiclemodule:

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

.. _uvs-scripting-events--wheeltelemetrycollection:

WheelTelemetryCollection
~~~~~~~~~~~~~~~~~~~~~~~~

-  **WheelTelemetryCollection** — ``public Enumerator GetEnumerator()`` — Returns a value enumerator without allocating when used directly by foreach.

See :ref:`WheelTelemetryCollection <uvs-api-events--wheeltelemetrycollection>` for immutable indexing and iteration.

.. _uvs-scripting-events--wheeltelemetrycollectionenumerator:

WheelTelemetryCollection.Enumerator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **WheelTelemetryCollection.Enumerator** — ``public bool MoveNext()`` — Advances to the next captured wheel.
-  **WheelTelemetryCollection.Enumerator** — ``public void Reset()`` — Restarts enumeration before the first entry.
-  **WheelTelemetryCollection.Enumerator** — ``public void Dispose()`` — No resources are owned by the value enumerator.

.. _uvs-scripting-events--configure-telemetry-capture:

Configure telemetry capture
---------------------------

Open **Vehicle Controller > Setup > Telemetry**, directly below **Configuration**. **Per-wheel diagnostics > Wheel Details** defaults off; **Vehicle diagnostics > Controls**, **Motion**, **Body**, **Powertrain**, **Fuel** and **Ground** default on. These switches stop the corresponding optional capture work and apply on the next fixed-step publication, including runtime edits.

+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Group         | Captured diagnostics                                                         | Disabled behavior                                                                                         |
+===============+==============================================================================+===========================================================================================================+
| Controls      | Input command, throttle, service brake, steering and handbrake               | No copied command/control readings; input and mechanics continue                                          |
+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Motion        | Acceleration, local motion, angular velocity, attitude, airspeed and G-force | Optional calculations/readings omitted; the live motion sensors retain their history for mechanics        |
+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Body          | Chassis mass and world centre of mass                                        | Native body-property capture omitted                                                                      |
+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Powertrain    | RPM, running state, torque, gearbox and clutch                               | Diagnostic drivetrain reads omitted; drivetrain simulation continues                                      |
+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Fuel          | Tank presence, quantity, capacity and consumption                            | Diagnostic tank lookup omitted; consumption continues                                                     |
+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Ground        | Grounded-wheel count and chassis ground clearance                            | Diagnostic chassis-height ray and aggregate ground count omitted; physical wheel support queries continue |
+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Wheel Details | Full copied per-wheel list                                                   | Wheels is empty and no wheel pose, name, slip or torque snapshot is collected                             |
+---------------+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

World **Position**, **Rotation**, **Velocity**, **SpeedKph**, **ForwardSpeed**, **FixedTime**, **DeltaTime**, **IsDirectControl** and configured **WheelCount** remain available. Pose and timing support mechanics such as overturn detection independently of the optional display groups. Sensor contact/impact history is mechanic-owned and is not switched off here.

Inspect ``snapshot.Sections`` or call ``snapshot.HasSection(TelemetrySections.Wheels)`` before consuming optional data. Disabled readings are zero/false/null and must not be interpreted as real measurements. **Live** shows an explanation for disabled groups and never enables collection automatically. HUDs and custom consumers of a disabled group no longer receive its readings. A retained older snapshot keeps both its values and its original Sections flags.

Set fields through ``vehicle.telemetry``, for example ``wheelDetails``, at runtime; no Apply Configuration or module rebuild is needed. A null options object falls back to the defaults.
