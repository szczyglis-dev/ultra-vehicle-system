.. _uvs-scripting-examples-input--commands-and-input:

Commands and input
==================

Adapters for UI, remote control and repeatable driving tests. Assign an InputBuffer as the vehicle input source; these examples write requests, not Rigidbody velocity.

See :doc:`Input implementation </Scripting/Input>` for the underlying contracts.

.. _uvs-scripting-examples-input--touch-controls-with-explicit-release:

Touch controls with explicit release
------------------------------------

**Setup:** Add to a UI object; assign the vehicle-owned InputBuffer. Connect pointer-down/up events to these methods.

**Behavior:** Held controls persist between physics ticks. Releasing or disabling the pad clears this adapter’s controls. Use it as the sole writer of these axes.

Save as ``TouchDrivePad.cs``.

.. raw:: html

   <!-- example: TouchDrivePad.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class TouchDrivePad : MonoBehaviour
       {
           public InputBuffer input;
           float throttle, steer;
           public void GasDown() { throttle = 1; Publish(); }
           public void GasUp() { throttle = 0; Publish(); }
           public void SetSteer(float value) { steer = Mathf.Clamp(value, -1, 1); Publish(); }
           void Publish() { if (input) input.SetAnalogAxes(throttle, steer); }
           void OnDisable()
           {
               throttle = steer = 0;
               // Do not leave a held touch active when its panel disappears.
               if (input) input.ClearControls();
           }
       }
   }

.. _uvs-scripting-examples-input--expire-stale-network-controls:

Expire stale network controls
-----------------------------

**Setup:** Assign a dedicated InputBuffer. Call Receive on Unity’s main thread after decoding a network packet.

**Behavior:** Missing packets apply the service brake after the lease expires. This is a local dead-man control, not a networking or authority implementation.

Save as ``RemoteCommandLease.cs``.

.. raw:: html

   <!-- example: RemoteCommandLease.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class RemoteCommandLease : MonoBehaviour
       {
           public InputBuffer input;
           [Min(.05f)] public float leaseSeconds = .3f;
           float deadline;
           public void Receive(float throttle, float steer)
           {
               if (!input || !isActiveAndEnabled) return;
               deadline = Time.unscaledTime + leaseSeconds;
               input.SetAnalogAxes(throttle, steer);
           }
           void Update()
           {
               if (input && Time.unscaledTime >= deadline)
                   input.SetAnalogAxes(0, 0, 1); // Lost connection: request a controlled stop.
           }
           void OnDisable() { if (input) input.ClearControls(); }
       }
   }

.. _uvs-scripting-examples-input--one-shot-gear-buttons:

One-shot gear buttons
---------------------

**Setup:** Assign an InputBuffer and connect UI buttons to Up, Down or Neutral. Use a manual-capable transmission.

**Behavior:** Each click queues one request. The gearbox still validates shifts; a rejected request is not automatically retried.

Save as ``QueuedGearButtons.cs``.

.. raw:: html

   <!-- example: QueuedGearButtons.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class QueuedGearButtons : MonoBehaviour
       {
           public InputBuffer input;
           public void Up() { if (input) input.ShiftGear(1); }
           public void Down() { if (input) input.ShiftGear(-1); }
           public void Neutral() { if (input) input.SelectGear(0); }
           public void Reverse() { if (input) input.SelectGear(-1); }
           public void ReleasePedal()
           {
               // Gear selection does not imply a throttle or clutch request.
               if (input) input.SetClutch(0);
           }
       }
   }

.. _uvs-scripting-examples-input--convert-steering-device-degrees-to-input:

Convert steering-device degrees to input
----------------------------------------

**Setup:** Assign vehicle and a dedicated InputBuffer. Call Submit from your steering-device integration on the main thread.

**Behavior:** Converts logical column degrees using this vehicle’s steering geometry. Throttle/brake remain normalized analog values; model mesh rotation is never used as input.

Save as ``SteeringDeviceAdapter.cs``.

.. raw:: html

   <!-- example: SteeringDeviceAdapter.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class SteeringDeviceAdapter : MonoBehaviour
       {
           public VehicleController vehicle;
           public InputBuffer controls;
           public bool reverseDeviceAxis;
           public void Submit(float columnDegrees, float throttle, float brake)
           {
               if (!vehicle || !controls || !float.IsFinite(columnDegrees)) return;
               float degrees = reverseDeviceAxis ? -columnDegrees : columnDegrees;
               // Use the configured column range rather than a hard-coded 900-degree wheel.
               float steer = Mathf.Clamp(vehicle.SteeringInputFromWheelAngle(degrees), -1, 1);
               controls.SetAnalogAxes(Mathf.Clamp01(throttle), steer, Mathf.Clamp01(brake));
           }
           void OnDisable() { if (controls) controls.ClearControls(); }
       }
   }

.. _uvs-scripting-examples-input--repeatable-throttle-and-brake-run:

Repeatable throttle-and-brake run
---------------------------------

**Setup:** Assign a dedicated InputBuffer and use a flat closed test area. Call Begin from a UI button.

**Behavior:** Requests throttle for the configured duration, then service braking. It does not teleport the car or bypass traction.

Save as ``TimedBrakeTest.cs``.

.. raw:: html

   <!-- example: TimedBrakeTest.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class TimedBrakeTest : MonoBehaviour
       {
           // Advance game time, so pausing the game also pauses this exercise.
           public InputBuffer input;
           [Min(0)] public float accelerateSeconds = 5, brakeSeconds = 3;
           float elapsed;
           bool running;
           public void Begin() { elapsed = 0; running = true; }
           void Update()
           {
               if (!input || !running) return;
               elapsed += Time.deltaTime;
               if (elapsed < accelerateSeconds) input.SetAnalogAxes(1, 0);
               else if (elapsed < accelerateSeconds + brakeSeconds) input.SetAnalogAxes(0, 0, 1);
               else { running = false; input.ClearControls(); }
           }
           void OnDisable() { running = false; if (input) input.ClearControls(); }
       }
   }

.. _uvs-scripting-examples-input--release-held-controls-when-focus-is-lost:

Release held controls when focus is lost
----------------------------------------

**Setup:** Assign a dedicated ``InputBuffer`` selected as the vehicle input source. Connect UI axes to ``Submit``; this component is their sole writer.

**Behavior:** Losing focus or pausing clears remembered pedals and requests a service stop on subsequent updates. Returning requires fresh UI input. This does not run while the whole application is suspended, and braking still depends on tire contact.

Save as ``FocusSafeDrivePad.cs``.

.. raw:: html

   <!-- example: FocusSafeDrivePad.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class FocusSafeDrivePad : MonoBehaviour
       {
           public InputBuffer input;
           float throttle, steering, brake;
           bool focused = true, paused;
           public void Submit(float gas, float turn, float stop)
           {
               if (!focused || paused || !isActiveAndEnabled) return;
               throttle = Mathf.Clamp(gas, -1, 1);
               steering = Mathf.Clamp(turn, -1, 1);
               brake = Mathf.Clamp01(stop);
           }
           void Update()
           {
               if (input) input.SetAnalogAxes(throttle, steering,
                   focused && !paused ? brake : 1);
           }
           void ClearHeld() { throttle = steering = brake = 0; }
           void OnApplicationFocus(bool value) { focused = value; ClearHeld(); }
           void OnApplicationPause(bool value) { paused = value; ClearHeld(); }
           void OnDisable() { ClearHeld(); if (input) input.ClearControls(); }
       }
   }

.. _uvs-scripting-examples-input--a-throttle-only-cruise-control-adapter:

A throttle-only cruise-control adapter
--------------------------------------

**Setup:** Assign vehicle and its dedicated ``InputBuffer``. ``Route`` driver pedals/steering through ``SubmitDriver``, and connect a button to ``ToggleCruise``. Use a forward wheeled profile and a suitable selected gear.

**Behavior:** Captures forward speed above 5 km/h and adjusts throttle with proportional feedback. Driver throttle or braking cancels cruise; steering remains live. It does not brake downhill, shift gears or avoid obstacles.

Save as ``CruiseControlPad.cs``.

.. raw:: html

   <!-- example: CruiseControlPad.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class CruiseControlPad : MonoBehaviour
       {
           public VehicleController vehicle;
           public InputBuffer input;
           [Min(.01f)] public float gain = .2f;
           float throttle, steering, brake, targetKph;
           public bool Cruising { get; private set; }
           public void SubmitDriver(float gas, float turn, float stop)
           {
               throttle = Mathf.Clamp(gas, -1, 1);
               steering = Mathf.Clamp(turn, -1, 1); brake = Mathf.Clamp01(stop);
               if (Mathf.Abs(throttle) > .05f || brake > .05f) Cruising = false;
           }
           public void ToggleCruise()
           {
               if (!vehicle || vehicle.ForwardSpeed < 5f / 3.6f) { Cruising = false; return; }
               Cruising = !Cruising; targetKph = vehicle.ForwardSpeed * 3.6f;
           }
           void Update()
           {
               if (!vehicle || !input) return;
               float gas = Cruising ? Mathf.Clamp01((targetKph - vehicle.ForwardSpeed * 3.6f) * gain) : throttle;
               input.SetAnalogAxes(gas, steering, brake);
           }
           void OnDisable()
           {
               Cruising = false; throttle = steering = brake = 0;
               if (input) input.ClearControls();
           }
       }
   }

.. _uvs-scripting-examples-input--drive-toward-a-parking-approach-point:

Drive toward a parking approach point
-------------------------------------

**Setup:** Assign a dedicated AI ``InputBuffer``, vehicle and a reachable point ahead on a flat closed test area. Select forward gear, start the engine and call ``Begin``.

**Behavior:** Steers toward one point, reduces approach speed and brakes near it; arrival requires low actual speed. It is a minimal forward approach controller, not pathfinding, reverse parking or collision avoidance. Disabling releases its held request.

Save as ``ParkingApproachDriver.cs``.

.. raw:: html

   <!-- example: ParkingApproachDriver.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class ParkingApproachDriver : MonoBehaviour
       {
           public VehicleController vehicle;
           public InputBuffer input;
           public Transform target;
           [Min(1)] public float approachKph = 12;
           [Min(.2f)] public float stopRadius = 2;
           public UnityEvent arrived = new UnityEvent();
           bool driving;
           public void Begin() { driving = true; }
           void Update()
           {
               if (!driving || !vehicle || !input || !target) return;
               Vector3 local = vehicle.transform.InverseTransformPoint(target.position);
               float distance = new Vector2(local.x, local.z).magnitude;
               float radius = Mathf.Max(.2f, stopRadius);
               if (distance <= radius)
               {
                   input.SetAnalogAxes(0, 0, 1);
                   if (vehicle.SpeedKph < .5f) { driving = false; arrived.Invoke(); }
                   return;
               }
               // Brake if the target is behind; a route planner must choose a new approach.
               if (local.z <= 0) { input.SetAnalogAxes(0, 0, 1); return; }
               float desired = Mathf.Min(approachKph, (distance - radius) * 2);
               float error = desired - vehicle.SpeedKph;
               float steer = Mathf.Clamp(Mathf.Atan2(local.x, local.z) * Mathf.Rad2Deg / 35, -1, 1);
               input.SetAnalogAxes(Mathf.Clamp01(error * .25f), steer, Mathf.Clamp01(-error * .2f));
           }
           void OnDisable() { driving = false; if (input) input.ClearControls(); }
       }
   }

.. _uvs-scripting-examples-input--hand-a-stopped-vehicle-between-player-and-ai:

Hand a stopped vehicle between player and AI
--------------------------------------------

**Setup:** Assign two active vehicle-owned ``InputBuffer`` providers, one for player adapters and one for AI. Connect ``GiveToAI`` and ``GiveToPlayer`` to your ownership UI.

**Behavior:** Refuses the handover while the chassis is moving or rotating. Clears both buffers before changing the input owner so queued shifts/held pedals cannot leak into the new session. Your game must also enable the correct upstream writer; this is not network authority.

Save as ``ParkedControlHandover.cs``.

.. raw:: html

   <!-- example: ParkedControlHandover.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class ParkedControlHandover : MonoBehaviour
       {
           public VehicleController vehicle;
           public InputBuffer player, ai;
           public UnityEvent rejected = new UnityEvent();
           public void GiveToAI() { Select(ai); }
           public void GiveToPlayer() { Select(player); }
           void Select(InputBuffer next)
           {
               if (!vehicle || !next || !next.isActiveAndEnabled || vehicle.IsMoving())
               { rejected.Invoke(); return; }
               if (player) player.ClearControls();
               if (ai) ai.ClearControls();
               vehicle.SetInputSource(next);
               // Upstream player/AI writers must respect the selected source.
           }
       }
   }

.. _uvs-scripting-examples-input--reduce-touch-steering-sensitivity-at-speed:

Reduce touch steering sensitivity at speed
------------------------------------------

**Setup:** Assign vehicle and its dedicated ``InputBuffer``; feed normalized UI gas, turn and brake into ``Submit``. Use as the sole writer of those axes.

**Behavior:** Applies a rescaled dead zone and smoothly reduces maximum steering request as speed rises. It changes the input request, not wheel geometry or the vehicle steering configuration.

Save as ``SpeedSensitiveTouchSteering.cs``.

.. raw:: html

   <!-- example: SpeedSensitiveTouchSteering.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class SpeedSensitiveTouchSteering : MonoBehaviour
       {
           public VehicleController vehicle;
           public InputBuffer input;
           [Range(0, .9f)] public float deadZone = .08f;
           [Range(.1f, 1)] public float highSpeedScale = .35f;
           [Min(1)] public float fullReductionKph = 100;
           public void Submit(float throttle, float turn, float brake)
           {
               if (!vehicle || !input || !isActiveAndEnabled) return;
               float dead = Mathf.Clamp(deadZone, 0, .9f);
               float magnitude = Mathf.Clamp01((Mathf.Abs(turn) - dead) / (1 - dead));
               float gain = Mathf.Lerp(1, highSpeedScale,
                   Mathf.Clamp01(vehicle.SpeedKph / Mathf.Max(1, fullReductionKph)));
               input.SetAnalogAxes(throttle, Mathf.Sign(turn) * magnitude * gain, brake);
           }
           void OnDisable() { if (input) input.ClearControls(); }
       }
   }
