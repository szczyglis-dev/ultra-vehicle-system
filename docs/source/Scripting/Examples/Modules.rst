.. _uvs-scripting-examples-modules--custom-vehicle-modules:

Custom vehicle modules
======================

Install these components through Add Module or your normal module registration flow. VehicleController owns Step timing; do not also call Step from FixedUpdate.

See :doc:`Modules implementation </Scripting/Modules>` for the underlying contracts.

.. _uvs-scripting-examples-modules--count-stationary-physics-time:

Count stationary physics time
-----------------------------

**Setup:** Add as a vehicle module. Read Seconds from a gameplay system.

**Behavior:** Accumulates time below a speed threshold; Configure resets its measurement whenever the vehicle is configured again.

Save as ``IdleTimeModule.cs``.

.. raw:: html

   <!-- example: IdleTimeModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class IdleTimeModule : WorldModule
       {
           public float Seconds { get; private set; }
           public override ExecutionPhase Phase => ExecutionPhase.Feedback;
           public override bool SupportsDirectControl => true;
           public override void Configure(VehicleController vehicle) { Seconds = 0; }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               // This is observation only, so direct control is supported explicitly.
               if (vehicle.SpeedKph < .5f) Seconds += deltaTime;
           }
       }
   }

.. _uvs-scripting-examples-modules--emit-a-fixed-time-periodic-callback:

Emit a fixed-time periodic callback
-----------------------------------

**Setup:** Add as a module and connect pulse to lightweight gameplay work.

**Behavior:** Emits at most once per tick; delayed callbacks do not produce an unbounded catch-up loop. Do not use this event to resample input.

Save as ``TelemetryPulseModule.cs``.

.. raw:: html

   <!-- example: TelemetryPulseModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class TelemetryPulseModule : WorldModule
       {
           // Read or request state through its owning component; do not bypass the vehicle pipeline.
           [Min(.02f)] public float interval = 1;
           public UnityEvent pulse = new UnityEvent();
           float elapsed;
           public override ExecutionPhase Phase => ExecutionPhase.Feedback;
           public override void Configure(VehicleController vehicle) { elapsed = 0; }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               elapsed += deltaTime;
               if (elapsed < Mathf.Max(.02f, interval)) return;
               elapsed = 0;
               pulse.Invoke();
           }
       }
   }

.. _uvs-scripting-examples-modules--a-simple-auxiliary-battery-model:

A simple auxiliary battery model
--------------------------------

**Setup:** Add as a module and assign Engine. Charge is an illustrative gameplay percentage, not a simulation of alternator physics.

**Behavior:** Charges while ignition is running and drains otherwise. This example does not block ignition or replace FuelTank.

Save as ``IdleBatteryModule.cs``.

.. raw:: html

   <!-- example: IdleBatteryModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class IdleBatteryModule : WorldModule
       {
           // This is a gameplay charge fraction, independent of engine torque or fuel.
           public Engine engine;
           [Range(0, 1)] public float charge = 1;
           [Min(0)] public float chargePerSecond = .01f, drainPerSecond = .001f;
           public override ExecutionPhase Phase => ExecutionPhase.Feedback;
           public override void Configure(VehicleController vehicle) { if (!engine) vehicle.TryGetModule(out engine); }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               float rate = engine && engine.IsRunning ? chargePerSecond : -drainPerSecond;
               charge = Mathf.Clamp01(charge + rate * deltaTime);
           }
       }
   }

.. _uvs-scripting-examples-modules--categorize-movement-without-update-polling:

Categorize movement without Update polling
------------------------------------------

**Setup:** Add as a module; connect bandChanged to an integer UI or audio parameter.

**Behavior:** Publishes 0 for stationary, 1 for city speed and 2 for faster travel. Each configuration clears the previous category.

Save as ``SpeedBandModule.cs``.

.. raw:: html

   <!-- example: SpeedBandModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class SpeedBandModule : WorldModule
       {
           // Emit on changes only, not on every physics tick.
           public UnityEvent<int> bandChanged = new UnityEvent<int>();
           int previous = -1;
           public override ExecutionPhase Phase => ExecutionPhase.Feedback;
           public override bool SupportsDirectControl => true;
           public override void Configure(VehicleController vehicle) { previous = -1; }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               int band = vehicle.SpeedKph < 1 ? 0 : vehicle.SpeedKph < 50 ? 1 : 2;
               if (band == previous) return;
               previous = band; bandChanged.Invoke(band);
           }
       }
   }

.. _uvs-scripting-examples-modules--count-continuous-wheel-contact-time:

Count continuous wheel-contact time
-----------------------------------

**Setup:** Add as a module. Read ContinuousSeconds to require stable ground contact before a game action.

**Behavior:** Resets when no operational wheel is grounded. Wheel-less vehicles need a different support signal; this is not a universal landed detector.

Save as ``GroundedTimeModule.cs``.

.. raw:: html

   <!-- example: GroundedTimeModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       public sealed class GroundedTimeModule : WorldModule
       {
           // Use the configured operational wheel list, including runtime wheel availability.
           public float ContinuousSeconds { get; private set; }
           public override ExecutionPhase Phase => ExecutionPhase.Feedback;
           public override void Configure(VehicleController vehicle) { ContinuousSeconds = 0; }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               bool supported = false;
               foreach (var wheel in vehicle.Wheels)
                   if (wheel.IsOperational && wheel.Grounded) { supported = true; break; }
               ContinuousSeconds = supported ? ContinuousSeconds + deltaTime : 0;
           }
       }
   }

.. _uvs-scripting-examples-modules--limit-powered-speed-inside-a-depot:

Limit powered speed inside a depot
----------------------------------

**Setup:** Install as a registered module on a wheeled vehicle. Set ``limitKph``; toggle ``limited`` from your depot-zone owner. Keep the normal engine/differential installed.

**Behavior:** After drivetrain resolution it reduces positive wheel propulsion near/above the limit while preserving braking torque. It is a power limiter, not a guaranteed speed cap: downhill gravity or impacts can still accelerate the vehicle.

Save as ``DepotPowerLimiter.cs``.

.. raw:: html

   <!-- example: DepotPowerLimiter.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       [ModuleSetup(IncludeInFull = false)]
       public sealed class DepotPowerLimiter : PhysicsModule
       {
           [Min(1)] public float limitKph = 20;
           public bool limited;
           public override ExecutionPhase Phase => ExecutionPhase.Assistance;
           public override int ExecutionOrder => 600;
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               if (!limited) return;
               float scale = Mathf.Clamp01((limitKph + 3 - vehicle.SpeedKph) / 3);
               foreach (var wheel in vehicle.Wheels)
               {
                   if (!wheel.IsOperational || !wheel.driven) continue;
                   // Leave an opposing torque (for example engine braking) alone.
                   if (wheel.Collider.motorTorque * wheel.Rpm >= 0)
                       wheel.Collider.motorTorque *= scale;
               }
           }
       }
   }

.. _uvs-scripting-examples-modules--apply-a-scripted-gust-to-the-chassis:

Apply a scripted gust to the chassis
------------------------------------

**Setup:** Install as a registered ``PhysicsModule``. Your weather/zone controller calls ``SetGust`` on this instance with a world-space acceleration vector and duration.

**Behavior:** Applies a finite game-time gust to the chassis through ``AddForce``, including airborne motion. Acceleration units are m/s²; this is an authored disturbance, not an aerodynamic surface simulation. Disabling clears the outstanding gust.

Save as ``CrosswindGustModule.cs``.

.. raw:: html

   <!-- example: CrosswindGustModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       [ModuleSetup(IncludeInFull = false)]
       public sealed class CrosswindGustModule : PhysicsModule
       {
           Vector3 acceleration;
           float remaining;
           public override ExecutionPhase Phase => ExecutionPhase.Assistance;
           public void SetGust(Vector3 worldAcceleration, float seconds)
           {
               acceleration = Vector3.ClampMagnitude(worldAcceleration, 20);
               remaining = Mathf.Max(0, seconds);
           }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               if (!vehicle.Body || remaining <= 0 || deltaTime <= 0) return;
               float fraction = Mathf.Min(remaining, deltaTime) / deltaTime;
               vehicle.Body.AddForce(acceleration * fraction, ForceMode.Acceleration);
               remaining = Mathf.Max(0, remaining - deltaTime);
           }
           void OnDisable() { remaining = 0; }
       }
   }

.. _uvs-scripting-examples-modules--add-modest-rolling-resistance-to-a-supported-vehicle:

Add modest rolling resistance to a supported vehicle
----------------------------------------------------

**Setup:** Install as a registered module and use a small ``deceleration`` on a wheeled vehicle. Compare coasting on level ground before combining it with other drag assistance.

**Behavior:** Applies a gravity-plane force opposite motion only with wheel support. Limits its own requested deceleration near zero speed to avoid reversing the vehicle. It does not replace tire friction, slope gravity or a parking brake.

Save as ``RollingResistanceModule.cs``.

.. raw:: html

   <!-- example: RollingResistanceModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       [ModuleSetup(IncludeInFull = false)]
       public sealed class RollingResistanceModule : PhysicsModule
       {
           [Min(0)] public float deceleration = .12f;
           public override ExecutionPhase Phase => ExecutionPhase.Coasting;
           public override int ExecutionOrder => 800;
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               if (!vehicle.Body || deltaTime <= 0) return;
               bool supported = false;
               foreach (var wheel in vehicle.Wheels) if (wheel.Grounded) { supported = true; break; }
               if (!supported) return;
               Vector3 up = Physics.gravity.sqrMagnitude > .001f ? -Physics.gravity.normalized : Vector3.up;
               Vector3 planar = Vector3.ProjectOnPlane(vehicle.Velocity, up);
               float speed = planar.magnitude;
               if (speed < .001f) return;
               float amount = Mathf.Min(Mathf.Max(0, deceleration), speed / deltaTime);
               vehicle.Body.AddForce(-planar / speed * amount, ForceMode.Acceleration);
           }
       }
   }

.. _uvs-scripting-examples-modules--model-coolant-temperature-for-a-game-dashboard:

Model coolant temperature for a game dashboard
----------------------------------------------

**Setup:** Install as a registered module on an engine-equipped vehicle. Bind a UI observer to ``Celsius`` or ``overheated``. Set ambient temperature, warm-up rate and warning threshold for your game.

**Behavior:** Runs a simple load/speed-dependent temperature model in fixed time. Emits one warning on crossing the threshold and rearms after cooling. It only publishes game state: it does not secretly change engine torque or implement real coolant physics.

Save as ``CoolantTemperatureModule.cs``.

.. raw:: html

   <!-- example: CoolantTemperatureModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       [ModuleSetup(IncludeInFull = false)]
       public sealed class CoolantTemperatureModule : PhysicsModule
       {
           public float ambientCelsius = 20, warningCelsius = 105;
           [Min(0)] public float degreesPerSecond = 1;
           public float Celsius { get; private set; } = 20;
           public UnityEvent overheated = new UnityEvent();
           Engine engine;
           bool warned;
           public override ExecutionPhase Phase => ExecutionPhase.Feedback;
           public override void Configure(VehicleController vehicle)
           { vehicle.TryGetModule(out engine); }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               float target = ambientCelsius;
               if (engine && engine.IsRunning)
                   target += 65 + engine.Throttle * 35 - Mathf.Min(20, vehicle.SpeedKph * .15f);
               Celsius = Mathf.MoveTowards(Celsius, target, Mathf.Max(0, degreesPerSecond) * deltaTime);
               if (!warned && Celsius >= warningCelsius) { warned = true; overheated.Invoke(); }
               if (Celsius < warningCelsius - 5) warned = false;
           }
       }
   }

.. _uvs-scripting-examples-modules--accumulate-mileage-until-a-service-is-due:

Accumulate mileage until a service is due
-----------------------------------------

**Setup:** Install as a registered module on a wheeled vehicle. Call ``MarkServiced`` after the workshop transaction succeeds. Save/restore the reading through your own persistence layer if needed.

**Behavior:** Integrates supported chassis speed in fixed time and raises one service reminder per interval. Teleport distance is not added; this is a game odometer based on chassis travel, not driven-wheel revolutions.

Save as ``ServiceMileageModule.cs``.

.. raw:: html

   <!-- example: ServiceMileageModule.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.Events;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples.Cookbook
   {
       [ModuleSetup(IncludeInFull = false)]
       public sealed class ServiceMileageModule : PhysicsModule
       {
           [Min(.01f)] public float intervalKm = 10;
           public float Kilometres { get; private set; }
           public UnityEvent serviceDue = new UnityEvent();
           bool notified;
           public override ExecutionPhase Phase => ExecutionPhase.Feedback;
           public void MarkServiced() { Kilometres = 0; notified = false; }
           public override void Step(VehicleController vehicle, Command command, float deltaTime)
           {
               bool supported = false;
               foreach (var wheel in vehicle.Wheels) if (wheel.Grounded) { supported = true; break; }
               if (!supported) return;
               Kilometres += vehicle.Velocity.magnitude * deltaTime / 1000;
               if (!notified && Kilometres >= Mathf.Max(.01f, intervalKm))
               { notified = true; serviceDue.Invoke(); }
           }
       }
   }
