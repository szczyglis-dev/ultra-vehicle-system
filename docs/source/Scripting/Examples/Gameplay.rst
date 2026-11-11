.. _uvs-scripting-examples-gameplay--driving-challenges-and-gameplay:

Driving challenges and gameplay
===============================

Small challenge rules driven by authoritative telemetry. These examples expose UnityEvents rather than depending on a particular UI, mission framework or scoring backend.

See :doc:`Events implementation </Scripting/Events>` for the underlying contracts.

.. _uvs-scripting-examples-gameplay--require-sustained-launch-speed:

Require sustained launch speed
------------------------------

**Setup:** Assign vehicle and connect passed. Re-enable the component to reset the challenge.

**Behavior:** Requires more than 40 km/h for two continuous physics seconds; slowing down resets the timer.

Save as ``RollingStartGate.cs``.

.. raw:: html

   <!-- example: RollingStartGate.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class RollingStartGate : MonoBehaviour
       {
           // A short excursion below the threshold resets the continuous-speed requirement.
           public VehicleController vehicle;
           public UnityEvent passed = new UnityEvent();
           float held;
           bool done;
           void OnEnable() { held = 0; done = false; if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; }
           void Sample(Telemetry t)
           {
               if (done) return;
               held = t.SpeedKph > 40 ? held + t.DeltaTime : 0;
               if (held < 2) return;
               done = true; passed.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-gameplay--penalize-sustained-harsh-acceleration:

Penalize sustained harsh acceleration
-------------------------------------

**Setup:** Assign vehicle. Read Penalty for a local training score.

**Behavior:** Integrates the amount above a planar acceleration threshold. Vertical suspension movement and gravity do not directly count. Reset on a new exercise.

Save as ``SmoothDrivingScore.cs``.

.. raw:: html

   <!-- example: SmoothDrivingScore.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class SmoothDrivingScore : MonoBehaviour
       {
           // Integrate excess acceleration over time rather than charging once per frame.
           public VehicleController vehicle;
           [Min(0)] public float threshold = 4;
           public float Penalty { get; private set; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; }
           void Sample(Telemetry t)
           {
               Vector3 planar = Vector3.ProjectOnPlane(t.Acceleration, t.Rotation * Vector3.up);
               Penalty += Mathf.Max(0, planar.magnitude - threshold) * t.DeltaTime;
           }
           public void ResetScore() { Penalty = 0; }
       }
   }

.. _uvs-scripting-examples-gameplay--count-sustained-loss-of-wheel-contact:

Count sustained loss of wheel contact
-------------------------------------

**Setup:** Assign a wheeled vehicle and connect completed.

**Behavior:** Requires at least one configured wheel and 0.4 seconds with no grounded wheels. It counts contact loss, not geometric jump height.

Save as ``AirborneChallenge.cs``.

.. raw:: html

   <!-- example: AirborneChallenge.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class AirborneChallenge : MonoBehaviour
       {
           // Rearm only after contact returns; award once per airborne interval.
           public VehicleController vehicle;
           public UnityEvent completed = new UnityEvent();
           float airborne;
           bool awarded;
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; airborne = 0; awarded = false; }
           void Sample(Telemetry t)
           {
               if (t.WheelCount == 0 || t.GroundedWheels > 0) { airborne = 0; awarded = false; return; }
               airborne += t.DeltaTime;
               if (airborne < .4f || awarded) return;
               awarded = true; completed.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-gameplay--measure-a-reversing-exercise:

Measure a reversing exercise
----------------------------

**Setup:** Assign vehicle and call Begin to start a five-metre reversing task.

**Behavior:** Counts signed forward motion only while reversing. Sideways sliding does not complete the task.

Save as ``ReverseDistanceTask.cs``.

.. raw:: html

   <!-- example: ReverseDistanceTask.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class ReverseDistanceTask : MonoBehaviour
       {
           // Forward travel never subtracts from or advances this reversing-only counter.
           public VehicleController vehicle;
           public UnityEvent completed = new UnityEvent();
           float distance;
           bool active;
           public void Begin() { distance = 0; active = true; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; active = false; }
           void Sample(Telemetry t)
           {
               if (!active) return;
               distance += Mathf.Max(0, -t.ForwardSpeed) * t.DeltaTime;
               if (distance < 5) return;
               active = false; completed.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-gameplay--require-a-stopped-handbraked-vehicle:

Require a stopped handbraked vehicle
------------------------------------

**Setup:** Assign vehicle and connect completed. Begin/CancelZone must be called by your validated parking-zone logic.

**Behavior:** Requires two seconds below 0.5 km/h with the handbrake requested. The zone system remains responsible for vehicle identity and full containment.

Save as ``ParkingDwellTask.cs``.

.. raw:: html

   <!-- example: ParkingDwellTask.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class ParkingDwellTask : MonoBehaviour
       {
           // The external zone decides containment; this component decides the stopping dwell.
           public VehicleController vehicle;
           public UnityEvent completed = new UnityEvent();
           bool inZone, done;
           float held;
           public void BeginZone() { inZone = true; done = false; held = 0; }
           public void CancelZone() { inZone = false; held = 0; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; CancelZone(); }
           void Sample(Telemetry t)
           {
               if (!inZone || done) return;
               held = t.SpeedKph < .5f && t.Handbrake ? held + t.DeltaTime : 0;
               if (held < 2) return;
               done = true; completed.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-gameplay--complete-a-delivery-only-inside-the-loading-bay:

Complete a delivery only inside the loading bay
-----------------------------------------------

**Setup:** Assign vehicle, a ``BoxCollider`` describing the bay, and the rear ``VehicleBodyPart``. Call ``BeginDelivery`` for each job and set ``cargoPresent`` from inventory. The bay collider is a measurement volume, not an automatic boarding trigger.

**Behavior:** Requires the chassis origin inside the oriented box, near-zero motion, the handbrake request and an opened cargo door for a continuous dwell. Loss of any condition resets progress. Completion fires once; opening state is a request, so this also excludes an active opening animation.

Save as ``LoadingBayDelivery.cs``.

.. raw:: html

   <!-- example: LoadingBayDelivery.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class LoadingBayDelivery : MonoBehaviour
       {
           public VehicleController vehicle;
           public BoxCollider bay;
           public VehicleBodyPart cargoDoor;
           public bool cargoPresent = true;
           [Min(.1f)] public float unloadSeconds = 3;
           public UnityEvent delivered = new UnityEvent();
           float elapsed;
           bool active;
           public void BeginDelivery() { elapsed = 0; active = true; }
           void Update()
           {
               if (!active || !vehicle || !bay || !cargoDoor) return;
               Vector3 point = bay.transform.InverseTransformPoint(vehicle.transform.position) - bay.center;
               Vector3 half = bay.size * .5f;
               bool inside = Mathf.Abs(point.x) <= half.x && Mathf.Abs(point.y) <= half.y && Mathf.Abs(point.z) <= half.z;
               bool ready = inside && cargoPresent && !vehicle.IsMoving() && vehicle.Command.Handbrake &&
                   cargoDoor.IsOpen && !cargoDoor.IsOpening && !cargoDoor.IsReleased;
               elapsed = ready ? elapsed + Time.deltaTime : 0;
               if (elapsed < unloadSeconds) return;
               active = false; cargoPresent = false; delivered.Invoke();
           }
           void OnDisable() { active = false; elapsed = 0; }
       }
   }

.. _uvs-scripting-examples-gameplay--meter-a-taxi-trip-by-distance-and-waiting-time:

Meter a taxi trip by distance and waiting time
----------------------------------------------

**Setup:** Assign vehicle. Call ``StartHire`` after accepting the passenger and ``FinishHire`` at drop-off. Read ``Fare`` for your UI; tune game-currency rates.

**Behavior:** Charges a flag-down amount plus supported travel and stopped waiting time. Uses snapshot velocity/timestep so a teleport position jump is not billable distance. It is local game state and does not charge an external account.

Save as ``TaxiFareMeter.cs``.

.. raw:: html

   <!-- example: TaxiFareMeter.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class TaxiFareMeter : MonoBehaviour
       {
           public VehicleController vehicle;
           [Min(0)] public float flagDown = 3, perKm = 2, perWaitingMinute = .5f;
           public float Fare { get; private set; }
           public bool Hired { get; private set; }
           public void StartHire() { if (!Hired) { Fare = flagDown; Hired = true; } }
           public void FinishHire() { Hired = false; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; Hired = false; }
           void Sample(Telemetry t)
           {
               if (!Hired || t.GroundedWheels == 0) return;
               Fare += t.Velocity.magnitude * t.DeltaTime / 1000 * Mathf.Max(0, perKm);
               if (t.SpeedKph < 1) Fare += t.DeltaTime / 60 * Mathf.Max(0, perWaitingMinute);
           }
       }
   }

.. _uvs-scripting-examples-gameplay--issue-at-most-one-speeding-ticket-per-zone-visit:

Issue at most one speeding ticket per zone visit
------------------------------------------------

**Setup:** Assign vehicle and fine amount. Your zone owner calls ``EnterZone(limitKph)`` once for a visit and ``LeaveZone`` on departure. Resolve overlapping zones before feeding this single-zone adapter.

**Behavior:** Issues one fine after a sustained speed violation, with a tolerance and dwell to reject brief spikes. Re-entering starts a new visit. It reports an event and accumulated local penalty; it does not change vehicle controls.

Save as ``SpeedZoneTicket.cs``.

.. raw:: html

   <!-- example: SpeedZoneTicket.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class SpeedZoneTicket : MonoBehaviour
       {
           public VehicleController vehicle;
           [Min(0)] public float toleranceKph = 3, fine = 50;
           [Min(.1f)] public float graceSeconds = 2;
           public float TotalPenalty { get; private set; }
           public UnityEvent ticketed = new UnityEvent();
           float limit, elapsed;
           bool inside, issued;
           public void EnterZone(float limitKph)
           { limit = Mathf.Max(0, limitKph); inside = true; issued = false; elapsed = 0; }
           public void LeaveZone() { inside = false; elapsed = 0; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; LeaveZone(); }
           void Sample(Telemetry t)
           {
               if (!inside || issued) return;
               elapsed = t.SpeedKph > limit + toleranceKph ? elapsed + t.DeltaTime : 0;
               if (elapsed < graceSeconds) return;
               issued = true; TotalPenalty += Mathf.Max(0, fine); ticketed.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-gameplay--accept-race-checkpoints-only-in-order:

Accept race checkpoints only in order
-------------------------------------

**Setup:** Assign vehicle and checkpoint count. Start via ``BeginRun``; each checkpoint trigger passes its own index and the entering ``VehicleController`` to ``Visit``. The trigger must resolve the entering vehicle, not call this for every collider indiscriminately.

**Behavior:** Rejects wrong vehicles, out-of-order checkpoints and repeated colliders from the same checkpoint. Measures elapsed game time and aborts a running attempt if the vehicle teleports. A checkpoint is accepted only once.

Save as ``OrderedCheckpointRun.cs``.

.. raw:: html

   <!-- example: OrderedCheckpointRun.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class OrderedCheckpointRun : MonoBehaviour
       {
           public VehicleController vehicle;
           [Min(1)] public int checkpointCount = 5;
           public int NextCheckpoint { get; private set; }
           public float FinishSeconds { get; private set; }
           public UnityEvent finished = new UnityEvent();
           bool running;
           float started;
           public void BeginRun() { NextCheckpoint = 0; FinishSeconds = 0; started = Time.time; running = true; }
           public void Visit(int index, VehicleController entrant)
           {
               if (!running || entrant != vehicle || !vehicle || index != NextCheckpoint) return;
               NextCheckpoint++;
               if (NextCheckpoint < Mathf.Max(1, checkpointCount)) return;
               running = false; FinishSeconds = Time.time - started; finished.Invoke();
           }
           void OnEnable() { if (vehicle) vehicle.Teleported += Abort; }
           void OnDisable() { if (vehicle) vehicle.Teleported -= Abort; running = false; }
           void Abort(Pose pose) { running = false; }
       }
   }

.. _uvs-scripting-examples-gameplay--track-damage-to-a-fragile-cargo-consignment:

Track damage to a fragile cargo consignment
-------------------------------------------

**Setup:** Assign vehicle and local cargo integrity. Call ``LoadCargo`` to begin a shipment. Choose an impulse threshold and scale for your game, then listen to ``cargoLost``.

**Behavior:** Reduces application-owned cargo integrity from copied body-impact impulses. Ignores colliders belonging to wheel support, and fails once at zero. It is separate from vehicle ``DamagePart`` health and uses collision impulses as a tunable game rule.

Save as ``FragileCargoMonitor.cs``.

.. raw:: html

   <!-- example: FragileCargoMonitor.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class FragileCargoMonitor : MonoBehaviour
       {
           public VehicleController vehicle;
           [Min(0)] public float toleratedImpulse = 500, damagePerNewtonSecond = .01f;
           public float Integrity { get; private set; }
           public UnityEvent cargoLost = new UnityEvent();
           bool loaded;
           public void LoadCargo() { Integrity = 100; loaded = true; }
           void OnEnable() { if (vehicle) vehicle.Impacted += Hit; }
           void OnDisable() { if (vehicle) vehicle.Impacted -= Hit; }
           void Hit(Impact impact)
           {
               if (!loaded || !impact.HasContact) return;
               if (impact.SelfCollider && impact.SelfCollider.GetComponentInParent<Wheel>()) return;
               float excess = Mathf.Max(0, impact.Impulse.magnitude - toleratedImpulse);
               Integrity = Mathf.Max(0, Integrity - excess * Mathf.Max(0, damagePerNewtonSecond));
               if (Integrity > 0) return;
               loaded = false; cargoLost.Invoke();
           }
       }
   }
