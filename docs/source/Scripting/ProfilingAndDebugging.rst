.. _uvs-scripting-profilinganddebugging--profiling-and-debugging:

Profiling and debugging
=======================

Use Unity's Profiler to locate expensive vehicle work before changing quality or update rates. This chapter covers profiling and existing diagnostics; a dedicated UVS debug class will be documented when it is available.

.. _uvs-scripting-profilinganddebugging--capture-a-useful-baseline:

Capture a useful baseline
-------------------------

1. Open **Window > Analysis > Profiler**, enable CPU Usage and record a repeatable scene. Start with Deep Profile disabled. Warm up initialization, mesh preparation, pools and passenger grip fitting before capturing steady driving.
2. Prefer a Development Build on the target device and attach the Profiler to that player. Editor captures are useful for finding a call path but also include Inspector, gizmo and editor overhead. Keep vehicle count, camera, fixed timestep and input route the same between comparisons.
3. Record separate cases: idle, driving over uneven ground, steering with passengers, repeated impacts, detachment/repair and aircraft gear operation. Keep startup and one-off events as separate measurements instead of averaging them into steady driving.
4. Stop recording and inspect CPU Usage in Timeline to locate the expensive frame/thread. Use Hierarchy and search for UVS markers to compare calls, total time, self time and GC Alloc. Total time includes nested samples; adding parent and child times would count work twice.
5. Compare several frames and repeated runs, including spikes. A rendered frame can contain several fixed ticks; compare cost per tick as well as per frame. More physics ticks can explain a frame spike even when each module costs the same.

Measure native physics, rendering and GPU work separately too. UVS samples time the code inside their scopes; they do not include every later WheelCollider solver, draw call or GPU operation triggered by that code. Wait time is also different from useful CPU work. Use Deep Profile briefly only if the existing samples cannot isolate a call, then confirm the result again with it disabled because its instrumentation changes timing.

.. _uvs-scripting-profilinganddebugging--built-in-controller-and-module-markers:

Built-in controller and module markers
--------------------------------------

-  ``UVS.Vehicle.Input``: input sampling, direct-control/ignition handling and transient-output reset; includes the nested ``UVS.Vehicle.ResetActuators`` wheel-output clearing scope.
-  ``UVS.Vehicle.Schedule``: building the phase lists for the captured registry. It excludes the subsequent mechanic steps.
-  ``UVS.Module.<TypeName>``: the controller's per-module scope, created lazily and cached with ENABLE_PROFILER. It includes eligibility checks and, when eligible, Step plus Stepped observers. Several instances of the same type share the displayed name; use Timeline context/call counts or isolate one vehicle to distinguish them. A scope can appear even when its module is skipped.
-  ``UVS.Vehicle.Telemetry``: sensor sampling and snapshot construction after the scheduled mechanics.
-  ``UVS.Vehicle.PublishTelemetry``: publishing the snapshot, including synchronous subscriber work. A slow HUD/application subscriber can therefore appear here.

The module scope covers scheduled work, not all independent Unity callbacks or nested owners. A custom module automatically receives its type marker when the controller reaches it; it does not need access to the internal StepMarker property.

.. _uvs-scripting-profilinganddebugging--detailed-subsystem-markers:

Detailed subsystem markers
--------------------------

-  ``UVS.ContactEnvelope``: tire support sampling.
-  ``UVS.Damage.ApplyImpact``: routed damage processing; ``UVS.Damage.Prepare``, ``UVS.Damage.Deform`` and ``UVS.Damage.Upload`` separate mesh preparation, deformation and upload work. Upload can happen in a different callback from the hit.
-  ``UVS.Passengers.Grip``, ``UVS.Passengers.Grip.FullFit`` and ``UVS.Passengers.Grip.Refit``: hand fitting and its expensive fit/refit paths. Compare initial fitting with steady contact separately.
-  ``UVS.Passenger.ActivateRagdoll``: the activation boundary for a physical passenger.
-  ``UVS.TireSmoke.Sample``, ``UVS.ExhaustSmoke`` and ``UVS.Skidmarks.Upload``: particle feedback sampling/update and skidmark buffer upload.

If a sample is absent, exercise its code path and check the profiled player and build configuration. Markers do not make unsupported paths execute. After finding a hotspot, use the Performance chapter to choose the relevant Inspector tradeoff, then recapture the same scenario.

.. _uvs-scripting-profilinganddebugging--add-your-own-marker:

Add your own marker
-------------------

Create one reusable marker with a stable descriptive name and wrap only the operation you want to measure. Auto returns a scope that ends when the using block exits, including an early return or exception. Do not create names containing per-frame values or object IDs, allocate a marker on each tick, or leave Begin/End unbalanced. Keep scopes synchronous; do not span an await, yield or several frames.

Save as ProfiledVehicleProbe.cs, attach under a vehicle and register it as a module. The example measures a small application-owned wheel query; replace that block with your real operation. The controller also supplies UVS.Module.ProfiledVehicleProbe around the scheduled call.

.. raw:: html

   <!-- example: ProfiledVehicleProbe.cs -->

.. code-block:: csharp

   using UltraVehicleSystem;
   using Unity.Profiling;

   public class ProfiledVehicleProbe : PhysicsModule
   {
       private static readonly ProfilerMarker probeMarker =
           new ProfilerMarker("MyGame.Vehicle.CountGroundedWheels");

       public int GroundedWheels { get; private set; }

       public override void Step(VehicleController vehicle, Command command, float deltaTime)
       {
           using (probeMarker.Auto())
           {
               int count = 0;
               foreach (var wheel in vehicle.Wheels)
                   if (wheel.Grounded) count++;
               GroundedWheels = count;
           }
       }
   }

After registering and enabling it, record a fixed tick and search CPU Usage for MyGame.Vehicle.CountGroundedWheels. Use a project prefix to separate your samples from package markers. The same pattern works inside an ordinary Update/LateUpdate or event subscriber; that sample appears under the callback actually executing it. Profiler scopes are diagnostic instrumentation, not a gameplay clock or a replacement for deltaTime.

.. _uvs-scripting-profilinganddebugging--debug-the-integration-boundary:

Debug the integration boundary
------------------------------

Check controller validation messages, registry membership, enabled state and profile/direct-control compatibility before investigating a missing Step. Observe CommandSampled, module Stepped and AfterPhysicsStep to locate where a value changes. Subscribe/unsubscribe with your component's lifecycle, and avoid per-frame logging during timing captures because logging alters the workload. Use the existing suspension/linkage gizmos to inspect anchors and limits; they are visual diagnostics, not extra physical constraints.

For Unity's API contract and capture guidance, see the official ProfilerMarker reference and profiling best practices linked below.

-  `Unity ProfilerMarker <https://docs.unity.com/en-us/engine/6000.0/script-reference/unity/profiling/profilermarker>`__
-  `Unity profiling best practices <https://unity.com/how-to/best-practices-for-profiling-game-performance>`__
