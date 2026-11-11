.. _uvs-scripting-examples-presentation--presentation-and-diagnostics:

Presentation and diagnostics
============================

Observers for camera effects, trails and development tools. They do not write to passenger bones, the chassis pose or mechanical control state.

See :doc:`Presentation implementation </Scripting/Presentation>` for the underlying contracts.

.. _uvs-scripting-examples-presentation--enable-a-trail-above-a-speed-threshold:

Enable a trail above a speed threshold
--------------------------------------

**Setup:** Assign vehicle and a TrailRenderer on a visual mount.

**Behavior:** Changes only trail emission, with hysteresis. Disabling stops emission while existing trail segments expire naturally.

Save as ``SpeedTrailGate.cs``.

.. raw:: html

   <!-- example: SpeedTrailGate.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class SpeedTrailGate : MonoBehaviour
       {
           // Change emission only; existing trail segments retain their authored lifetime.
           public VehicleController vehicle;
           public TrailRenderer trail;
           public float startKph = 100, stopKph = 90;
           void Update()
           {
               if (!vehicle || !trail) return;
               trail.emitting = vehicle.SpeedKph > (trail.emitting ? stopKph : startKph);
           }
           void OnDisable() { if (trail) trail.emitting = false; }
       }
   }

.. _uvs-scripting-examples-presentation--smooth-camera-field-of-view-from-speed:

Smooth camera field of view from speed
--------------------------------------

**Setup:** Assign a Camera dedicated to this effect and vehicle. Disable other FOV writers for that camera.

**Behavior:** Expands FOV from 60 to 75 degrees up to 180 km/h, and restores its original setting on disable. This changes FOV, not the near clip plane.

Save as ``SpeedCameraFov.cs``.

.. raw:: html

   <!-- example: SpeedCameraFov.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class SpeedCameraFov : MonoBehaviour
       {
           // This effect owns only fieldOfView; leave camera movement to its normal controller.
           public VehicleController vehicle;
           public Camera targetCamera;
           float original;
           void OnEnable() { if (targetCamera) original = targetCamera.fieldOfView; }
           void LateUpdate()
           {
               if (!vehicle || !targetCamera) return;
               float target = Mathf.Lerp(60, 75, Mathf.Clamp01(vehicle.SpeedKph / 180));
               targetCamera.fieldOfView = Mathf.Lerp(targetCamera.fieldOfView, target, 1 - Mathf.Exp(-4 * Time.deltaTime));
           }
           void OnDisable() { if (targetCamera) targetCamera.fieldOfView = original; }
       }
   }

.. _uvs-scripting-examples-presentation--send-a-copied-impact-signal-to-effects:

Send a copied impact signal to effects
--------------------------------------

**Setup:** Assign vehicle and connect pulse to a float-valued effect action.

**Behavior:** Emits a normalized impulse signal with a cooldown. Impact is a copied snapshot; no Collision object is retained past the callback.

Save as ``ImpactSeverityPulse.cs``.

.. raw:: html

   <!-- example: ImpactSeverityPulse.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class ImpactSeverityPulse : MonoBehaviour
       {
           // The cooldown bounds repeated effects during a multi-contact collision.
           public VehicleController vehicle;
           public UnityEvent<float> pulse = new UnityEvent<float>();
           [Min(1)] public float fullImpulse = 10000;
           float nextTime;
           void OnEnable() { if (vehicle) vehicle.Impacted += Hit; }
           void OnDisable() { if (vehicle) vehicle.Impacted -= Hit; }
           void Hit(Impact impact)
           {
               if (Time.unscaledTime < nextTime) return;
               float strength = Mathf.Clamp01(impact.Impulse.magnitude / fullImpulse);
               if (strength < .05f) return;
               nextTime = Time.unscaledTime + .25f;
               pulse.Invoke(strength);
           }
       }
   }

.. _uvs-scripting-examples-presentation--keep-a-short-telemetry-history:

Keep a short telemetry history
------------------------------

**Setup:** Assign vehicle and call CopyHistory from a main-thread diagnostic tool.

**Behavior:** Stores up to 120 immutable snapshots. CopyHistory allocates intentionally on request; the recording loop uses a preallocated ring.

Save as ``PhysicsSnapshotRecorder.cs``.

.. raw:: html

   <!-- example: PhysicsSnapshotRecorder.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class PhysicsSnapshotRecorder : MonoBehaviour
       {
           // Read or request state through its owning component; do not bypass the vehicle pipeline.
           public VehicleController vehicle;
           readonly Telemetry[] samples = new Telemetry[120];
           int next, count;
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Record; }
           void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Record; }
           void Record(Telemetry t) { samples[next] = t; next = (next + 1) % samples.Length; count = Mathf.Min(count + 1, samples.Length); }
           public Telemetry[] CopyHistory()
           {
               var result = new Telemetry[count];
               int first = (next - count + samples.Length) % samples.Length;
               for (int i = 0; i < count; i++) result[i] = samples[(first + i) % samples.Length];
               return result;
           }
       }
   }

.. _uvs-scripting-examples-presentation--log-control-source-handovers:

Log control-source handovers
----------------------------

**Setup:** Assign vehicle. Enable only while diagnosing control ownership.

**Behavior:** Reports source changes and initial state; it avoids logging every physics command and flooding the console.

Save as ``InputChangeLogger.cs``.

.. raw:: html

   <!-- example: InputChangeLogger.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class InputChangeLogger : MonoBehaviour
       {
           // Observe ownership changes rather than logging the continuously sampled command.
           public VehicleController vehicle;
           void OnEnable()
           {
               if (!vehicle) return;
               vehicle.InputSourceChanged += Changed;
               Changed(vehicle.inputSource);
           }
           void OnDisable() { if (vehicle) vehicle.InputSourceChanged -= Changed; }
           void Changed(MonoBehaviour source)
           {
               Debug.Log(source ? $"Input owner: {source.name} ({source.GetType().Name})" : "Input owner released", this);
           }
       }
   }

.. _uvs-scripting-examples-presentation--play-a-dedicated-reversing-beeper:

Play a dedicated reversing beeper
---------------------------------

**Setup:** Assign vehicle and an AudioSource with a looping warning clip, Play On Awake off. This script must be the sole playback owner of that source.

**Behavior:** Beeps during actual backward chassis motion above a small threshold. Stops on disable or when forward/stopped. Selecting reverse gear without moving does not beep in this policy.

Save as ``ReversingBeeper.cs``.

.. raw:: html

   <!-- example: ReversingBeeper.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class ReversingBeeper : MonoBehaviour
       {
           public VehicleController vehicle;
           public AudioSource beeper;
           void Update()
           {
               if (!beeper) return;
               bool reversing = vehicle && vehicle.ForwardSpeed < -.3f;
               if (reversing && !beeper.isPlaying) { beeper.loop = true; beeper.Play(); }
               if (!reversing && beeper.isPlaying) beeper.Stop();
           }
           void OnDisable() { if (beeper) beeper.Stop(); }
       }
   }

.. _uvs-scripting-examples-presentation--dim-cockpit-backlighting-with-the-beam-state:

Dim cockpit backlighting with the beam state
--------------------------------------------

**Setup:** Assign ``Lights`` and a CanvasGroup containing only the dashboard backlight artwork. Keep it separate from the whole dashboard UI and from the dimmer component itself.

**Behavior:** Fades between daytime/nighttime illumination values using exponential smoothing. It reads ``Lights`` output policy and does not change headlight requests or render materials.

Save as ``DashboardNightDimmer.cs``.

.. raw:: html

   <!-- example: DashboardNightDimmer.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class DashboardNightDimmer : MonoBehaviour
       {
           public Lights lights;
           public CanvasGroup backlight;
           [Range(0, 1)] public float daytime = .15f, nighttime = .8f;
           [Min(0)] public float response = 6;
           float original;
           void OnEnable() { if (backlight) original = backlight.alpha; }
           void Update()
           {
               if (!backlight) return;
               float target = lights && lights.BeamMode != BeamMode.Off ? nighttime : daytime;
               backlight.alpha = Mathf.Lerp(backlight.alpha, target,
                   1 - Mathf.Exp(-Mathf.Max(0, response) * Time.deltaTime));
           }
           void OnDisable() { if (backlight) backlight.alpha = original; }
       }
   }

.. _uvs-scripting-examples-presentation--add-bounded-vibration-to-a-camera-child-pivot:

Add bounded vibration to a camera child pivot
---------------------------------------------

**Setup:** Assign vehicle and an otherwise unwritten child pivot beneath the camera owner, with the camera mesh/view below it. Do not assign the chassis, wheel root or a pivot moved by the UVS camera owner.

**Behavior:** Adds a small noise offset scaled by speed and restores the original local position on disable. It is a visual layer beneath the camera owner; it does not feed motion back into vehicle physics.

Save as ``CockpitVibrationPivot.cs``.

.. raw:: html

   <!-- example: CockpitVibrationPivot.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class CockpitVibrationPivot : MonoBehaviour
       {
           public VehicleController vehicle;
           public Transform pivot;
           [Min(0)] public float maximumMetres = .005f, frequency = 18;
           Vector3 neutral;
           void OnEnable() { if (pivot) neutral = pivot.localPosition; }
           void LateUpdate()
           {
               if (!pivot) return;
               float amount = vehicle ? Mathf.Clamp01(vehicle.SpeedKph / 80) * maximumMetres : 0;
               float time = Time.time * frequency;
               Vector3 noise = new Vector3(Mathf.PerlinNoise(time, 0) - .5f,
                   Mathf.PerlinNoise(0, time) - .5f, 0);
               pivot.localPosition = neutral + noise * (2 * amount);
           }
           void OnDisable() { if (pivot) pivot.localPosition = neutral; }
       }
   }

.. _uvs-scripting-examples-presentation--billboard-a-vehicle-label-at-a-modest-update-rate:

Billboard a vehicle label at a modest update rate
-------------------------------------------------

**Setup:** Assign vehicle, the viewing Camera and a child TextMesh; set its alignment/anchor for your model. Use a separate label child, never the vehicle root. Restrict visibility through its Renderer rather than disabling this script.

**Behavior:** Faces the camera and displays vehicle name plus speed four times per second. Hides the renderer beyond a maximum distance and restores visibility on disable. It does not discover a global player camera.

Save as ``FleetVehicleLabel.cs``.

.. raw:: html

   <!-- example: FleetVehicleLabel.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class FleetVehicleLabel : MonoBehaviour
       {
           public VehicleController vehicle;
           public Camera viewer;
           public TextMesh label;
           [Min(1)] public float visibleMetres = 100;
           float nextRefresh;
           Renderer labelRenderer;
           bool originalVisible;
           void OnEnable()
           {
               nextRefresh = 0;
               labelRenderer = label ? label.GetComponent<Renderer>() : null;
               if (labelRenderer) originalVisible = labelRenderer.enabled;
           }
           void LateUpdate()
           {
               if (!vehicle || !viewer || !label) return;
               label.transform.rotation = viewer.transform.rotation;
               if (labelRenderer) labelRenderer.enabled =
                   Vector3.Distance(viewer.transform.position, vehicle.transform.position) <= visibleMetres;
               if (Time.time < nextRefresh) return;
               nextRefresh = Time.time + .25f;
               label.text = vehicle.name + "\n" + vehicle.SpeedKph.ToString("0") + " km/h";
           }
           void OnDisable() { if (labelRenderer) labelRenderer.enabled = originalVisible; }
       }
   }

.. _uvs-scripting-examples-presentation--highlight-sustained-native-tire-slip-for-tuning:

Highlight sustained native tire slip for tuning
-----------------------------------------------

**Setup:** Assign vehicle and a separate warning object. Tune a slip threshold and debounce time on representative terrain. This is a diagnostic overlay, not a traction-control implementation.

**Behavior:** Shows a warning only after any grounded wheel with a valid native ground hit sustains excessive longitudinal or lateral slip. Telemetry from unsupported contacts is ignored and the overlay clears on disable.

Save as ``WheelSlipDiagnostic.cs``.

.. raw:: html

   <!-- example: WheelSlipDiagnostic.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class WheelSlipDiagnostic : MonoBehaviour
       {
           public VehicleController vehicle;
           public GameObject warning;
           [Min(0)] public float slipThreshold = .4f, dwellSeconds = .2f;
           float elapsed;
           void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
           void OnDisable()
           {
               if (vehicle) vehicle.AfterPhysicsStep -= Sample;
               elapsed = 0; if (warning) warning.SetActive(false);
           }
           void Sample(Telemetry t)
           {
               bool slipping = false;
               foreach (var wheel in t.Wheels)
                   if (wheel.Grounded && wheel.HasGroundHit &&
                       Mathf.Max(Mathf.Abs(wheel.ForwardSlip), Mathf.Abs(wheel.SidewaysSlip)) > slipThreshold)
                   { slipping = true; break; }
               elapsed = slipping ? elapsed + t.DeltaTime : 0;
               if (warning) warning.SetActive(slipping && elapsed >= dwellSeconds);
           }
       }
   }
