.. _uvs-performance--performance-tuning:

Performance tuning
==================

Profile the number of active vehicles, occupants and visible effects expected in the game. Include dynamic passengers, mirrors and damage when measuring the cost of your fleet.

.. _uvs-performance--establish-a-baseline:

Establish a baseline
--------------------

1. Measure movement with one vehicle and effects disabled.
2. Add the intended occupants and record physics cost.
3. Enable mirrors, particles and audio one system at a time.
4. Repeat with the expected active fleet in a player build.

Keep the workload and camera comparable when measuring a change.

Wheel friction and physical lamp channels read their current native properties before updating them and skip identical writes. Runtime changes to grip, handbrake state, surface grip, light settings and external curve/lamp edits remain visible on the next application. This does not cache ground contacts, skip simulation steps or defer lamp events and emissive-renderer updates.

Full-probe paths also avoid redundant work: the tread sampler reuses its identical centre ray, deformation tracks displacement bounds per vertex block, settled audio and palm constraints avoid unchanged native property writes, and free-ragdoll velocity limiting skips sleeping bones. These do not lower solver iterations, contact precision, particle budgets or normal-rebuild quality. Deformation still uses the same vertex order and shared source meshes remain untouched.

Damage meshes use regular GPU buffers for intermittent uploads. Forcing a dynamic-buffer hint on large damaged meshes can increase ongoing rendering cost between impacts, as observed in the Linux/Vulkan release verification. This is separate from the CPU cost of calculating dents or rebuilding normals. Measure both before and after the first visible dent in a player build.

.. _uvs-performance--stationary-vehicles-and-seated-passengers:

Stationary vehicles and seated passengers
-----------------------------------------

Wheel torque, steering and damping outputs skip identical native writes. Inputs, module steps, events and telemetry continue every physics tick. This avoids unnecessary wheel wake-ups where the output is already unchanged; it does not guarantee that a braked vehicle sleeps, since pipeline resets, parking assistance, buoyancy and physical passengers may still keep it active.

The passenger IK anatomy scan caches bone Transform references, refreshing them when the associated Rigidbody changes and rejecting destroyed bodies. It still resolves the current anatomical list, joint limits and bone poses each time. Seated ragdolls remain dynamic with the same solver settings and response to impacts.

The built-in car dashboard redraws its generated texture only when its displayed speed, RPM, speed unit, gear, fuel pixels or headlight indicator changes. Telemetry and Changed events retain their full rate; custom textures and the configured display refresh rate remain supported.

.. _uvs-performance--procedural-suspension-geometry:

Procedural suspension geometry
------------------------------

The modular suspension keeps its normal fixed/render update order. SuspensionHub uses the final smoothed wheel visual directly when available, avoiding a second wheel-pose query whose result would be discarded. Span placement reuses its measured length, skips identity spin work and writes the length scale only when that value changes. ControlArm reuses its Rigidbody and pivot-frame reads within each calculation.

LandingGearSuspension calculates the shared integration subdivision once per step and calculates the contact torque axis only when the wheel has a ground hit. Spring/damper equations, integration substeps, wheel contact and retraction interlocks are unchanged. These reduce redundant work rather than lowering suspension update frequency or visual precision.

.. _uvs-performance--reduce-the-largest-cost-first:

Reduce the largest cost first
-----------------------------

+--------------------------+-------------------------------------------------------------------------------+
| Cost                     | Practical controls                                                            |
+==========================+===============================================================================+
| Wheel/contact physics    | Active vehicles, contact sample counts, collider complexity, physics timestep |
+--------------------------+-------------------------------------------------------------------------------+
| Physical passengers      | Active occupants, character colliders/joints, solver settings                 |
+--------------------------+-------------------------------------------------------------------------------+
| Mirrors                  | View range, resolution, refresh rate and renders-per-frame budget             |
+--------------------------+-------------------------------------------------------------------------------+
| Particles and tire marks | Emission, distance culling, lifetime and bounded capacities                   |
+--------------------------+-------------------------------------------------------------------------------+
| Damage/debris            | Readable mesh complexity, part boundaries and debris lifetime                 |
+--------------------------+-------------------------------------------------------------------------------+

Runtime hand fitting caches up to 64 completed fits per calibrated hand. Seating prepares action handles assigned to that seat; repeated transfers reuse fits while finger blending and IK continue normally. Geometry, pose, rig and fitting changes invalidate reuse, and recalibration clears the cache. New runtime controls can require a fresh fit. See :ref:`grip geometry and binding <uvs-scripting-gripsolving--geometry-and-binding>` for the data used by fitting.

Prepare grips during authoring or binding. Reuse command buffers and unsubscribe observers when disabled. Disable unused systems deliberately; changing a visible material alone does not remove physics work.

The :doc:`Scripting Reference </Scripting/index>` explains ownership and update cost per system.

.. _uvs-performance--inspector-performance-settings:

Inspector performance settings
------------------------------

ContactEnvelope defaults to probing every two fixed steps. Set Probe Every Fixed Steps to 1 for every-step contact sampling. Change one setting at a time and compare the same scene in a player build. Controls are grouped under **Performance** or **Performance: wheel simulation** in their component Inspectors, including embedded module Inspectors in VehicleController.

.. _uvs-performance--tire-contact-sampling--contactenvelope:

Tire contact sampling — ContactEnvelope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All envelope performance fields are in a collapsible **Performance / Optimization** group, also when embedded in VehicleController. **Optimize When Stationary** defaults to true, with **Stationary Probe Every Fixed Steps = 10**. At dt = 0.02 s this gives a 0.2 s stationary probe period. The moving interval remains 2 by default. Movement, drive/steering/flight input, wake-up, mode changes and interval changes refresh immediately. Sub-threshold drift and changes to ground between probes can still use retained support until the next batch. Set the stationary interval lower or disable the new option when fast external terrain changes matter. The existing **Sleeping Probe Interval** independently applies only to sleeping bodies.

Stationary detection uses ``VehicleController.IsMoving(linearSpeedThreshold, angularSpeedThreshold)`` with default tolerances 0.05 m/s and 0.02 rad/s. Full 3D and angular motion count; Rigidbody sleep is not required. Awake suspension damping still advances on cached steps. Steering changes over 0.1 degrees, mount/centre movement over 1 mm, reparenting and tire radius/width changes also refresh stationary support; tiny pose jitter is tolerated. Significant curb corrections refresh every step while moving; stationary corrections use their selected cadence.

**Reuse Native Ground Contact** defaults on. On a currently certified unobstructed box face, the native hit identifies a candidate support, four corner rays certify its current plane and an overlap query excludes other obstacles. This removes the additional centre ray (default 3×9 grid: 4 rays instead of 5). Meshes, gaps, curbs, changed layers, missing or stale native contacts and uncertified surfaces use the fresh centre query. Certification queries remain necessary; GetGroundHit alone is not equivalent to a new envelope ray.

+----------------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                    | Default | Lower-cost choice and tradeoff                                                                                                                                                                                                                                                                                                                                       |
+============================+=========+======================================================================================================================================================================================================================================================================================================================================================================+
| Longitudinal Samples       | 9       | Fewer samples along the tread reduce raycasts but can miss short steps; the effective count is odd, 3–15.                                                                                                                                                                                                                                                            |
+----------------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Width Samples              | 3       | One strip is cheaper than three, but represents tire-edge support less accurately.                                                                                                                                                                                                                                                                                   |
+----------------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Edge Refinement Iterations | 7       | 0–10 binary-search iterations per detected tread-height edge or gap boundary. Lower values reduce extra rays at curbs, with coarser edge location.                                                                                                                                                                                                                   |
+----------------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Probe Every Fixed Steps    | 2       | Schedules a probe once per two fixed ticks by default, reusing radius/support samples between probes; suspension damping still advances every tick. At a 0.02 s fixed timestep this is a 0.04 s probe period, with up to one extra tick of response delay. Use 1 for fast vehicles/sharp obstacles; larger values can miss narrow obstacles or retain stale support. |
+----------------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sleeping Probe Interval    | 0.2 s   | Longer intervals reduce queries only while the native body sleeps without throttle/steering. Removed terrain/support is noticed later. Zero checks every fixed step.                                                                                                                                                                                                 |
+----------------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

LastGroundQueryCount reports actual native raycast calls in the latest Step; cached/sleeping steps report zero. On an unobstructed single planar BoxCollider face, the sampler certifies the whole ray prism with one conservative OverlapBoxNonAlloc and corner rays, then computes the tread samples on that face. Without certified native-contact reuse, a default 3×9 grid needs 5 raycasts instead of 27 there (3 rays for a single-width strip); certified native reuse saves one more ray. The overlap query is additional and is not counted as a raycast. Meshes, Terrain, ambiguous/overlapping support, gaps, sharp slopes and saturated buffers use the full sampler; attempted certification can add work in these fallback cases. The full-probe mode retains the grid/refinement settings and does not reuse ground geometry across sampled ticks. While moving, wheels with an envelope correction greater than 3% of the tire radius are sampled every tick until it drops below that threshold, even when the scheduled interval is larger. This avoids retaining the extra radius across the centre of a curb; an obstacle approached from zero correction can still be noticed later. Cache reuse does not disable native WheelCollider physics or skip drivetrain/force integration. Use every-tick probes for fast vehicles and sharp/uneven terrain. Changes to these fields take effect as the component runs; Configure clears cached support and forces a fresh sample. VehicleController.Teleport also restores base radii and invalidates support immediately, so the next fixed step samples the new location even in a skipped-probe phase. Disabling the envelope restores native wheel radii and clears its cache. Ground Layers can also restrict candidate colliders to real driving surfaces.

Probe Every Fixed Steps is serialized per component. Set it in the component’s Performance section to choose the sampling cadence.

.. _uvs-performance--native-wheel-simulation--suspension:

Native wheel simulation — Suspension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+---------+-----------------------------------------------------------------------------------------------------------------+
| Setting                        | Default | Effect                                                                                                          |
+================================+=========+=================================================================================================================+
| Wheel Substep Speed Threshold  | 5 m/s   | Selects which native simulation count applies below/above this vehicle speed.                                   |
+--------------------------------+---------+-----------------------------------------------------------------------------------------------------------------+
| Wheel Substeps Below Threshold | 12      | Fewer substeps reduce low-speed tire/suspension force calculations, with potentially less stable wheel contact. |
+--------------------------------+---------+-----------------------------------------------------------------------------------------------------------------+
| Wheel Substeps Above Threshold | 15      | Fewer substeps reduce higher-speed tire/suspension force calculations; check braking, bumps and heavy loads.    |
+--------------------------------+---------+-----------------------------------------------------------------------------------------------------------------+

These counts apply to the whole vehicle, not to independent wheels. Unity divides each fixed step into these substeps for tire and suspension forces; it does not change the global Rigidbody fixed timestep. See `Unity's ConfigureVehicleSubsteps contract <https://docs.unity3d.com/ScriptReference/WheelCollider.ConfigureVehicleSubsteps.html>`__. Apply vehicle configuration after changing the counts or threshold, or call Suspension.Configure(vehicle) to apply that module's configuration. A later Wheel.Configure uses the owning vehicle's Suspension settings too. Without Suspension, the existing 5/12/15 fallback remains.

.. _uvs-performance--visual-damage-updates--vehiclemeshdeformation:

Visual damage updates — VehicleMeshDeformation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                     | Default | Lower-cost choice and tradeoff                                                                                                                                |
+=============================+=========+===============================================================================================================================================================+
| Mesh Upload Interval Frames | 1       | 2–16 LateUpdate calls with pending dents batch more hits into one upload/normal rebuild. Visible dents and DeformationChanged arrive later.                   |
+-----------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Recalculate Normals         | Enabled | Disable to retain existing normals while moving vertices. This avoids normal recalculation but deformed lighting is less accurate. Bounds are always updated. |
+-----------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Every accepted hit updates deformation buffers; the interval reduces upload/rebuild frequency rather than skipping damage. It is measured in rendered LateUpdate calls while dents are pending, independently of physics ticks. RestoreShape and component disable flush immediately. Call FlushPendingDeformation() when geometry consumers need pending vertices now; DeformationChanged signals that uploaded geometry is ready. RestoreShape restores the original normals too when normal rebuilding is disabled.

.. _uvs-performance--other-existing-budgets:

Other existing budgets
~~~~~~~~~~~~~~~~~~~~~~

TireCollision.Cylinder Sides defaults to 32; fewer sides reduce generated convex tire complexity at the cost of a more faceted contact shape. Apply vehicle configuration after changing proxy geometry. Mirrors already expose resolution, range, refresh interval and renders-per-frame limits. Particle channels expose distance culling and particle budgets; impact audio/visual profiles have bounded voice/instance capacities. Physical passengers expose free-ragdoll solver iteration counts. Their setup guides and the Inspector reference explain ownership and state-specific behavior. No global quality preset silently changes these systems.

Profiler markers ``UVS.Damage.Prepare``, ``UVS.Damage.Deform`` and ``UVS.Damage.Upload`` separate first-use mesh preparation, dent calculations and vertex/normal/bounds upload. Preparation is included inside a first ``Deform`` call when the mesh was not prewarmed; do not add their inclusive times together. Upload excludes subscriber callbacks from ``DeformationChanged``.

.. _uvs-performance--physics-allocation-costs:

Physics allocation costs
------------------------

Built-in wheel/module loops use an internal indexed iterator to avoid allocating an enumerator when reading the public IReadOnlyList properties. Virtual Wheels/Modules providers remain respected. Ragdoll collision limits use scalar maxima instead of a temporary params array. Wheel-less telemetry uses a shared empty collection. Non-empty wheel telemetry still owns immutable per-step copies for replay/history; these allocations are intentional and are not eliminated by reusing a mutable buffer. GC.Alloc in the Profiler reports memory allocation, separately from garbage-collection CPU time. Compare bytes per physics step, since slow rendered frames can run multiple fixed steps.

TireCollision retains a stable contact-state slot per tire proxy. Writers and contact-modification callbacks copy the complete support state under a short lock; no Unity API runs inside that lock. This avoids ConcurrentDictionary node allocations on updates of a large struct value while retaining coherent contact data for physics worker threads. Removing or rebuilding proxies still updates the dictionary normally.

The demo water-entry effect first rejects colliders attached to a different Rigidbody, before checking their other native properties. For the exact built-in WaterSurface and built-in/null WaterSurfaceProfile, it samples the lake frame/size once per Tick and rejects points outside its oriented footprint before calling the provider. Derived surfaces, custom providers and custom styles retain their virtual sampling path. Each collider's bounds is read once, and passenger ownership is searched only for a potential closest water contact. Every physics step still checks entry/exit, including moving/rotated lakes, trigger/enabled changes and current Rigidbody ownership. No polling interval or proximity approximation delays a splash.

.. _uvs-performance--aircraft-hud-rendering:

Aircraft HUD rendering
----------------------

AircraftHud reuses an unchanged generated image at each scheduled refresh. Changing attitudes are rasterized as exact horizon spans inside the instrument circle, rather than running the complete shading calculation for every pixel. Number glyphs are shared and rendered directly from integers. The 256×256 texture, displayed values, strict horizon boundaries, telemetry-event cadence and default 15 Hz refresh rate are retained. This removes warmed managed allocations from the built-in raster path. A changed image still uploads its texture, so graphics-driver upload cost remains platform-dependent.

.. _uvs-performance--rear-mirror-rendering-cost:

Rear-mirror rendering cost
--------------------------

RearMirrors performs additional camera renders when surfaces pass its observer/frustum/range, refresh and per-component budget checks. The inclusive LateUpdate time includes that scene rendering; its self time reflects only part of the module overhead. Six LateUpdate calls do not imply six camera renders. Reusing render-request objects and shader IDs reduces module allocations, and skipped channels avoid unnecessary frustum calculations. Camera settings are only written when different, with live reads retaining external edits correction. These optimizations preserve resolution, image contents, refresh rates and rendering budgets; they do not remove the scene-rendering cost. The render pipeline can still allocate internally.

Use each channel's culling mask, far clip, resolution and refresh rate to tune rendering quality/cost for the actual cockpit. Maximum Renders Per Frame applies to each RearMirrors component, not globally across the fleet. Disabling unneeded channels through the public enable methods retains ownership cleanup and enable events.

.. _uvs-performance--demo-screen-gui:

Demo screen GUI
---------------

The demo controls and telemetry panels use fixed IMGUI rectangles and paint only during Repaint; their keyboard handling remains in Update/LateUpdate. Automatic GUILayout work is disabled for those components. Keycap parsing and exact style measurements are cached in bounded dictionaries, invalidated when the GUI skin/font changes. Renamed vehicles, changed bindings/provider descriptions, camera mode and selected-vehicle updates still use their live values. Dashboard labels and flight readouts reuse strings while their source values and formatting culture are unchanged.

The demo attitude raster keeps its existing 0.02-degree refresh tolerance and visual output. Its pitch marks are spaced far enough apart that only the nearest mark can satisfy the original strict width/height tests; testing that candidate avoids checking all thirteen positions at every pixel. DrawScreenSpaceUI in a render-thread capture also includes native GUI rendering and graphics synchronization; a reduction in managed OnGUI preparation time is not a direct measurement of the whole render-thread sample or GPU time.

.. _uvs-performance--demo-mirror-selection-policy:

Demo mirror selection policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VehicleSelectorDemo automatically installs the demo-only SelectedVehicleMirrorsDemo adapter. It enables originally enabled RearMirrors components only for the selected vehicle while its CameraRigDemo is enabled, targets that vehicle and uses Interior mode. Orbit, cinematic and free-camera modes disable the fleet mirrors. Selection, camera-mode and target events update the cached component bindings. A small early LateUpdate check also catches direct field edits, a missing/replaced rig or a disabled rig; there is no per-frame scene search. Switching to a vehicle without mirrors leaves the fleet's mirror components disabled. The adapter retains each channel's active flag and the module's Mirrors Enabled setting. Disabling the adapter restores the component-enabled states it captured; Refresh rebuilds bindings after runtime fleet changes. The runtime RearMirrors module itself has no single-player/selection policy.

.. _uvs-performance--locating-vehicle-physics-costs:

Locating vehicle physics costs
------------------------------

``VehicleController.FixedUpdate`` includes the complete module pipeline, not only contact queries. Expand ``UVS.Module.<TypeName>`` to compare passenger constraints, tire collision proxies, engine, feedback and other modules without Deep Profile. Each module marker includes its eligibility checks, physics step and Stepped subscribers; a marker can therefore appear even when the module is disabled or unsupported. Modules with the same type name are aggregated. Dynamic module markers are only created in builds with ENABLE_PROFILER.

``UVS.Vehicle.Schedule`` measures phase preparation. ``UVS.Vehicle.Input`` includes command sampling, direct control and ``UVS.Vehicle.ResetActuators``. ``UVS.Vehicle.Telemetry`` measures snapshot construction and ground-height sampling; ``UVS.Vehicle.PublishTelemetry`` measures AfterPhysicsStep subscribers. Nested inclusive marker times must not be added together. Normalize by vehicle count and physics ticks: 28 controller calls can mean 14 vehicles over two physics steps in one rendered frame. These markers instrument existing work and do not reduce simulation frequency or change its ordering.

.. _uvs-performance--telemetry-and-feedback-sampling:

Telemetry and feedback sampling
-------------------------------

Module lookup tests the requested managed type before testing the native component state. It still walks the current module array in order, includes disabled modules by default, rejects destroyed objects and honors activeOnly; no registry cache can become stale after public array edits. Telemetry retains virtual getters, samples its active gearbox once in the controller and reuses repeated rotation/Transform reads within snapshot construction. Wheel arrays and their read-only wrappers remain independently owned by each snapshot, so retained history cannot change after the next physics step.

TireFeedback shares the road-body and point-velocity sample between touchdown-slip detection and the ordinary per-wheel contact record. Source binding first checks reference identity to avoid repeated Unity object comparisons for unchanged sources. Sampling frequency, per-wheel notifications, slip decay, surface resolution and presentation subscribers are retained. Inclusive feedback marker time can include Sampled subscribers such as tire effects; improvements to the contact sampler do not remove those subscribers' work.

.. _uvs-performance--editor-diagnostics-overhead:

Editor diagnostics overhead
---------------------------

VehicleController and Transmission inspectors request live refreshes through Unity's RequiresConstantRepaint contract, with a 0.1-second gate and no forced refresh while paused. Native selection, input and property-change redraws remain independent of this live refresh gate. Markers UVS.Editor.VehicleInspector, UVS.Editor.TransmissionInspector and UVS.Editor.LiveInspectorRepaint identify the package's inspector work when profiling the Editor process.

Module inspector visibility ignores property-only object-change notifications, since ordinary field values do not determine whether a module is co-located with a controller. Structural hierarchy notifications, undo/redo, play-mode transitions and explicit standalone-inspector preferences still schedule synchronization. UVS.Editor.ModuleInspectorVisibility.Sync measures its complete scan. Hierarchy notifications can still schedule scans even when object-property notifications are filtered; this is not a guarantee of zero scans during Play Mode.

Part-gizmo visibility tests use two optional Transform arguments instead of a temporary params array. Geometry, selection/reference rules and all existing gizmo preferences are retained. These editor changes do not lower runtime physics or effect frequency.

In CPU Hierarchy, each Total includes its children, while Self excludes them. Sum the controller's direct children plus its Self time, rather than adding nested raycasts/effect markers a second time. Small timings can display as 0.0 percent due to rounding, and additional rows can be below the visible area. The built-in controller instruments every scheduled non-null module's eligibility, Step and Stepped callbacks.

When the Profiler target is Play Mode, EditorLoop groups editor activity without a detailed breakdown. Select the Editor process to inspect editor costs and the UVS.Editor markers. An EditorLoop percentage alone cannot attribute the time to gizmos, inspectors, scene rendering or the Profiler, and it is not a player-build cost. See `Unity's explanation of Play mode and Editor samples <https://docs.unity.com/en-us/engine/6000.0/manual/analysis/profiler/play-edit-samples>`__.
