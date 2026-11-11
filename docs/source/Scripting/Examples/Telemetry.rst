.. _uvs-scripting-examples-telemetry--telemetry-and-measurements:

Telemetry and measurements
==========================

Read completed physics snapshots for game rules and presentation. These components subscribe once and unsubscribe on disable; assign references before enabling them.

See :doc:`Events implementation </Scripting/Events>` for the underlying contracts.

.. _uvs-scripting-examples-telemetry--measure-a-trip-without-counting-teleports:

Measure a trip without counting teleports
-----------------------------------------

**Setup:** Assign vehicle and call ClearTrip when a new journey starts.

**Behavior:** Integrates speed over physics time; it does not count a teleport as travelled distance. Wheelspin while stationary contributes no chassis distance.

Save as ``TripDistanceCounter.cs``.

.. raw:: html

   <!-- example: TripDistanceCounter.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class TripDistanceCounter : MonoBehaviour
       {
           public VehicleController vehicle;
           public float Metres { get; private set; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; }
           void Sample(Telemetry t)
           {
               // Velocity is m/s; DeltaTime belongs to this physics snapshot.
               Metres += t.Velocity.magnitude * t.DeltaTime;
           }
           public void ClearTrip() { Metres = 0; }
       }
   }

.. _uvs-scripting-examples-telemetry--speed-warning-with-hysteresis:

Speed warning with hysteresis
-----------------------------

**Setup:** Assign vehicle and connect entered/exited UnityEvents. Configure thresholds in km/h.

**Behavior:** The warning switches at separate thresholds, preventing rapid event chatter near the limit.

Save as ``OverspeedAlarm.cs``.

.. raw:: html

   <!-- example: OverspeedAlarm.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class OverspeedAlarm : MonoBehaviour
       {
           // Separate entry and exit thresholds keep noise around the limit from retriggering events.
           public VehicleController vehicle;
           public float limitKph = 80, hysteresisKph = 5;
           public UnityEvent entered = new UnityEvent(), exited = new UnityEvent();
           bool alarm;
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; alarm = false; }
           void Sample(Telemetry t)
           {
               bool next = alarm ? t.SpeedKph > Mathf.Max(0, limitKph - hysteresisKph) : t.SpeedKph > limitKph;
               if (next == alarm) return;
               alarm = next;
               if (alarm) entered.Invoke(); else exited.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-telemetry--measure-a-braking-interval:

Measure a braking interval
--------------------------

**Setup:** Assign vehicle. Call Arm immediately before starting a braking test.

**Behavior:** Starts measuring when resolved braking exceeds 0.1 and speed exceeds 5 km/h. Logs distance/time when speed falls below 0.5 km/h.

Save as ``BrakingDistanceMeter.cs``.

.. raw:: html

   <!-- example: BrakingDistanceMeter.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class BrakingDistanceMeter : MonoBehaviour
       {
           // Measure only after the driver actually requests braking.
           public VehicleController vehicle;
           bool armed, measuring;
           float metres, seconds;
           public void Arm() { armed = true; measuring = false; metres = seconds = 0; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; armed = measuring = false; }
           void Sample(Telemetry t)
           {
               if (!armed) return;
               if (!measuring && t.Brake > .1f && t.SpeedKph > 5) measuring = true;
               if (!measuring) return;
               metres += t.Velocity.magnitude * t.DeltaTime;
               seconds += t.DeltaTime;
               if (t.SpeedKph >= .5f) return;
               Debug.Log($"Stopping distance: {metres:F1} m in {seconds:F2} s", this);
               armed = measuring = false;
           }
       }
   }

.. _uvs-scripting-examples-telemetry--keep-a-bounded-gear-change-history:

Keep a bounded gear-change history
----------------------------------

**Setup:** Assign Engine. Read History from a debug UI; do not mutate the returned queue.

**Behavior:** Keeps the last eight accepted gear changes. Logs state changes rather than guessing them from input buttons.

Save as ``ShiftHistoryWindow.cs``.

.. raw:: html

   <!-- example: ShiftHistoryWindow.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class ShiftHistoryWindow : MonoBehaviour
       {
           public Engine engine;
           readonly System.Collections.Generic.Queue<string> history = new System.Collections.Generic.Queue<string>();
           public System.Collections.Generic.IEnumerable<string> History => history;
           void OnEnable() { if (engine) engine.GearChanged += Changed; }
           void OnDisable() { if (engine) engine.GearChanged -= Changed; }
           void Changed(int gear)
           {
               // Use an owned string instead of retaining a live collision or scene object.
               if (history.Count == 8) history.Dequeue();
               history.Enqueue($"{Time.fixedTime:F2}s: gear {gear}");
           }
       }
   }

.. _uvs-scripting-examples-telemetry--update-a-numeric-display-at-a-lower-frequency:

Update a numeric display at a lower frequency
---------------------------------------------

**Setup:** Assign vehicle and connect valueChanged to a UI method accepting float.

**Behavior:** Samples the latest snapshot at 5 Hz while physics keeps its normal rate. The event is useful for text readouts, not smooth needle animation.

Save as ``LowRateSpeedDisplay.cs``.

.. raw:: html

   <!-- example: LowRateSpeedDisplay.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class LowRateSpeedDisplay : MonoBehaviour
       {
           public VehicleController vehicle;
           public UnityEvent<float> valueChanged = new UnityEvent<float>();
           float remaining, latest;
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; remaining = 0; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; }
           void Sample(Telemetry t) { latest = t.SpeedKph; }
           void Update()
           {
               remaining -= Time.unscaledDeltaTime;
               if (remaining > 0) return;
               remaining = .2f; // UI cadence is independent of physics cadence.
               valueChanged.Invoke(latest);
           }
       }
   }

.. _uvs-scripting-examples-telemetry--time-a-fresh-acceleration-run-without-counting-a-teleport:

Time a fresh acceleration run without counting a teleport
---------------------------------------------------------

**Setup:** Assign vehicle and a target speed. Call ``Arm`` while stopped on a straight test route, then accelerate. Read ``Seconds`` after ``finished`` fires.

**Behavior:** Starts timing when speed first passes 1 km/h and completes at the target, using snapshot timesteps. Rejects arming while moving and cancels on teleport. Resolution is one physics tick; it is not a sub-frame timing instrument.

Save as ``AccelerationRunTimer.cs``.

.. raw:: html

   <!-- example: AccelerationRunTimer.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class AccelerationRunTimer : MonoBehaviour
       {
           public VehicleController vehicle;
           [Min(5)] public float targetKph = 100;
           public float Seconds { get; private set; }
           public UnityEvent finished = new UnityEvent();
           bool armed, started;
           public void Arm()
           {
               if (!vehicle || vehicle.IsMoving()) return;
               Seconds = 0; armed = true; started = false;
           }
           void OnEnable()
           {
               if (!vehicle) return;
               vehicle.AfterPhysicsStep += Sample; vehicle.Teleported += Cancel;
           }
           void OnDisable()
           {
               if (vehicle) { vehicle.AfterPhysicsStep -= Sample; vehicle.Teleported -= Cancel; }
               armed = started = false;
           }
           void Cancel(Pose pose) { armed = started = false; }
           void Sample(Telemetry t)
           {
               if (!armed) return;
               if (!started) { if (t.SpeedKph > 1) started = true; return; }
               Seconds += t.DeltaTime;
               if (t.SpeedKph < Mathf.Max(5, targetKph)) return;
               armed = false; finished.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-telemetry--build-a-trip-summary-for-a-delivery-results-screen:

Build a trip summary for a delivery results screen
--------------------------------------------------

**Setup:** Assign vehicle. Call ``BeginTrip`` at dispatch and ``EndTrip`` on arrival; display the public distance, duration, average speed, maximum speed and stopped time afterward.

**Behavior:** Integrates actual snapshot speed/time rather than transform deltas, so a reset does not add teleport distance. Measures the entire active trip, including waits; it continues across a vehicle reset until the application ends it.

Save as ``DeliveryTripSummary.cs``.

.. raw:: html

   <!-- example: DeliveryTripSummary.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class DeliveryTripSummary : MonoBehaviour
       {
           public VehicleController vehicle;
           public float Metres { get; private set; }
           public float Seconds { get; private set; }
           public float StoppedSeconds { get; private set; }
           public float MaximumKph { get; private set; }
           public float AverageKph => Seconds > 0 ? Metres / Seconds * 3.6f : 0;
           bool recording;
           public void BeginTrip()
           { Metres = Seconds = StoppedSeconds = MaximumKph = 0; recording = true; }
           public void EndTrip() { recording = false; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; recording = false; }
           void Sample(Telemetry t)
           {
               if (!recording) return;
               Seconds += t.DeltaTime;
               Metres += t.Velocity.magnitude * t.DeltaTime;
               MaximumKph = Mathf.Max(MaximumKph, t.SpeedKph);
               if (t.SpeedKph < .5f) StoppedSeconds += t.DeltaTime;
           }
       }
   }

.. _uvs-scripting-examples-telemetry--measure-lateral-acceleration-during-a-handling-test:

Measure lateral acceleration during a handling test
---------------------------------------------------

**Setup:** Assign vehicle and run a steady cornering exercise. Call ``ResetPeak`` between runs; read ``CurrentG`` and ``PeakG`` for the handling report.

**Behavior:** Converts chassis-local lateral kinematic acceleration to G units using gravity magnitude. It is not the occupant's full accelerometer reading: gravity/bank contributions to specific force are a separate telemetry contract.

Save as ``CorneringLoadMeter.cs``.

.. raw:: html

   <!-- example: CorneringLoadMeter.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class CorneringLoadMeter : MonoBehaviour
       {
           public VehicleController vehicle;
           public float CurrentG { get; private set; }
           public float PeakG { get; private set; }
           public void ResetPeak() { PeakG = 0; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; CurrentG = 0; }
           void Sample(Telemetry t)
           {
               float gravity = Physics.gravity.magnitude;
               CurrentG = gravity > .001f ? Mathf.Abs(t.LocalAcceleration.x) / gravity : 0;
               PeakG = Mathf.Max(PeakG, CurrentG);
           }
       }
   }

.. _uvs-scripting-examples-telemetry--export-a-bounded-telemetry-recording-to-csv:

Export a bounded telemetry recording to CSV
-------------------------------------------

**Setup:** Assign vehicle and call ``BeginRecording``, then ``StopRecording`` and ``SaveCsv`` from development UI. The platform must allow writing to ``Application.persistentDataPath``. The output is the fixed filename ``vehicle-telemetry.csv``.

**Behavior:** Keeps only the newest bounded sample count and writes once on demand, with invariant decimal formatting. Does not write a file during every physics tick. A later save overwrites the prior CSV; file-access failures are reported to the console.

Save as ``TelemetryCsvExport.cs``.

.. raw:: html

   <!-- example: TelemetryCsvExport.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class TelemetryCsvExport : MonoBehaviour
       {
           public VehicleController vehicle;
           [Range(1, 5000)] public int capacity = 600;
           readonly System.Collections.Generic.Queue<Telemetry> samples =
               new System.Collections.Generic.Queue<Telemetry>();
           bool recording;
           public void BeginRecording() { samples.Clear(); recording = true; }
           public void StopRecording() { recording = false; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; recording = false; }
           void Sample(Telemetry t)
           {
               if (!recording) return;
               int limit = Mathf.Clamp(capacity, 1, 5000);
               while (samples.Count >= limit) samples.Dequeue();
               samples.Enqueue(t);
           }
           public void SaveCsv()
           {
               var csv = new System.Text.StringBuilder("fixed_time,speed_kph,rpm,brake,gear\n");
               var culture = System.Globalization.CultureInfo.InvariantCulture;
               foreach (var t in samples)
                   csv.Append(t.FixedTime.ToString("F3", culture)).Append(',')
                      .Append(t.SpeedKph.ToString("F2", culture)).Append(',')
                      .Append(t.Rpm.ToString("F0", culture)).Append(',')
                      .Append(t.Brake.ToString("F3", culture)).Append(',')
                      .Append(t.Gear.ToString(culture)).Append('\n');
               string path = System.IO.Path.Combine(Application.persistentDataPath, "vehicle-telemetry.csv");
               try { System.IO.File.WriteAllText(path, csv.ToString()); Debug.Log(path, this); }
               catch (System.IO.IOException error) { Debug.LogError(error.Message, this); }
               catch (System.UnauthorizedAccessException error) { Debug.LogError(error.Message, this); }
           }
       }
   }

.. _uvs-scripting-examples-telemetry--compare-native-support-loads-across-one-axle:

Compare native support loads across one axle
--------------------------------------------

**Setup:** Assign vehicle and explicit left/right indices from its runtime wheel order. Use two different indices representing the same axle. Read ``HasReading``, ``LeftFraction`` and ``TotalNewtons`` in your setup overlay.

**Behavior:** Calculates left/right load share only when both wheels have valid native ground hits and a nonzero total load. It measures reported support reaction, not a static vehicle weight distribution or a complete tire-contact-envelope force.

Save as ``AxleLoadBalanceMeter.cs``.

.. raw:: html

   <!-- example: AxleLoadBalanceMeter.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class AxleLoadBalanceMeter : MonoBehaviour
       {
           public VehicleController vehicle;
           public int leftIndex, rightIndex = 1;
           public bool HasReading { get; private set; }
           public float LeftFraction { get; private set; }
           public float TotalNewtons { get; private set; }
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; HasReading = false; }
           void Sample(Telemetry t)
           {
               HasReading = false; LeftFraction = TotalNewtons = 0;
               if (leftIndex == rightIndex || leftIndex < 0 || rightIndex < 0 ||
                   leftIndex >= t.Wheels.Count || rightIndex >= t.Wheels.Count) return;
               var left = t.Wheels[leftIndex]; var right = t.Wheels[rightIndex];
               if (!left.Grounded || !right.Grounded || !left.HasGroundHit || !right.HasGroundHit) return;
               float a = Mathf.Max(0, left.ContactForce), b = Mathf.Max(0, right.ContactForce);
               TotalNewtons = a + b;
               HasReading = TotalNewtons > .01f;
               LeftFraction = HasReading ? a / TotalNewtons : 0;
           }
       }
   }
