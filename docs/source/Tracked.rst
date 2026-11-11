.. _uvs-tracked--build-a-tracked-vehicle:

Build a tracked vehicle
=======================

Tracked vehicles use wheel contacts for traction and steering, with optional segmented belt animation. Configure the left/right mechanical sides first, then prepare each visible belt. The animated links do not need a physical chain of joints.

.. _uvs-tracked--1-configure-the-mechanical-sides:

1. Configure the mechanical sides
---------------------------------

1. Prepare a unit-scale vehicle root facing +Z, with its Rigidbody, hull colliders and road-wheel contacts. Choose **Tools → UltraVehicleSystem → Add Vehicle → Tracked**.
2. In **Wheel Setup**, configure the road wheels and their Drive, Brake and intended Handbrake roles. Leave Steer off: tracked steering uses different left/right belt demands rather than rotating the road wheels.
3. On **Tracks**, assign every contact wheel to exactly one **Left Wheels** or **Right Wheels** array. Keep the sides separate and remove duplicate assignments.
4. Apply vehicle configuration. Confirm straight forward/reverse travel, moving turns, stationary pivot turns and braking before adding visual links.

**Inside Track Speed Ratio** controls inside-belt reduction. **Pivot Track Speed** and its response settings control stationary turning. Allow sufficient lateral tire slip for fixed road wheels to turn; tune Lateral Grip and optional lateral-stability settings after basic propulsion works. Engine power, brake torque and contact geometry also affect the result.

.. _uvs-tracked--tune-moving-turns-and-pivots:

Tune moving turns and pivots
----------------------------

The side arrays live on ``Tracks``; turning policy lives in the selected ``TrackedProfile``. Do not tune belt animation to change the physical turn rate. Start with a known straight-road baseline before changing these groups:

+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Profile group                                              | Effect                                                                        |
+============================================================+===============================================================================+
| Steering Mix / Inside Track Speed Ratio                    | How strongly steering reduces the inside belt target during moving turns      |
+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Steering Brake Torque                                      | Maximum per-wheel inside-belt speed-regulation braking                        |
+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Pivot Track Speed                                          | Equal/opposite belt target at full stationary steering, in m/s                |
+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Pivot Transition Time / Track Speed Response               | Blend into pivot behavior and belt target response                            |
+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Turn Speed Compensation                                    | Raises the outside target to preserve more of the mean speed in a turn        |
+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Redistribute Steering Torque                               | Routes unused inside drive to the outside within existing engine torque/power |
+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Lateral Grip / Low Speed Turn Grip                         | Sideways scrub allowed by Friction, including powered launch release          |
+------------------------------------------------------------+-------------------------------------------------------------------------------+
| Lateral Stability / Maximum Lateral Stability Acceleration | Supported hull lateral damping with a bounded acceleration                    |
+------------------------------------------------------------+-------------------------------------------------------------------------------+

At full steering, a smaller inside-speed ratio makes the moving turn tighter but demands more speed difference/scrub. Pivot speed is a target, not a guarantee the engine has enough power to achieve it. Shared service braking and handbrake take priority over steering drive/regulation.

Use positive driven-wheel weights and sufficient usable engine output. Steering itself can request drive demand for a pivot, so a stationary turn is not merely rotating an otherwise unpowered Rigidbody. If the hull refuses to turn, inspect contact, brakes and lateral scrub before adding a larger engine.

Low Speed Turn Grip blends toward ordinary tracked lateral grip as road speed rises. Lateral stability corrects supported sideways drift within contact/grip limits; it is separate from making each road wheel adhere without slip. Excessive lateral tire grip can fight the very skid steering the profile needs.

.. _uvs-tracked--side-membership:

Side membership
~~~~~~~~~~~~~~~

Assign every mechanical road wheel explicitly to one side for predictable behavior. Empty side slots have geometric fallback for supported consumers, but partial/duplicate membership is difficult to reason about and should not be a model-authoring strategy. Keep left/right references inside this vehicle's wheel set, separate from visible rollers and link segments.

Use :doc:`suspension </Suspension>` to get loaded contact distribution correct and :doc:`surfaces </Surfaces>` for physical friction. A visual path builder does not repair a side that has no traction support.

.. _uvs-tracked--2-prepare-the-track-model:

2. Prepare the track model
--------------------------

1. In your modeling application, separate the left and right belt meshes from the hull, sprockets and rollers.
2. Split each belt into individual tread links or short rigid sections. Export each moving section as a separate mesh object so Unity imports it as its own GameObject/Transform. A single continuous mesh, even with several materials, is not a list of movable links.
3. Arrange the segments around the complete closed belt in their resting positions, including the upper run, lower run and curves around the end wheels. Keep their dimensions and spacing consistent enough for a continuous appearance.
4. Place the segments under separate **Left Links** and **Right Links** parents. Keep moving links as siblings rather than nesting one link under another. Hull meshes and visible rollers should not be inside these collection groups.
5. Prefer pivots near each segment's center. If exported parts share an inconvenient common pivot, the builder's **Mesh Bounds Center** option can use their mesh centers instead.
6. Import the model and check its scale and orientation. Put ``TrackVisuals`` on the vehicle root or a transform aligned with the vehicle: X across the hull, Y up and Z forward. Automatic ordering follows the belt loop in this transform's Y/Z plane.

The builder creates a motion path from these prepared objects. It does not cut a combined mesh, generate missing tread geometry or create Rigidbody/joint chains. Keep traction WheelColliders on the configured road wheels, separate from the moving belt links.

.. _uvs-tracked--3-generate-the-paths-with-trackpathbuilder:

3. Generate the paths with TrackPathBuilder
-------------------------------------------

1.  Add **Track Visuals** to the vehicle and register it with the controller. You can use **Modules → Add module** or add the component and choose **Discover and order vehicle modules**.
2.  Open the TrackVisuals component's context menu and choose **Create Path Builders**. This creates a left and a right builder for that component. Alternatively, add **Track Path Builder** manually for each side and assign **Visuals** to the same TrackVisuals component.
3.  On the left builder, enable **Left Belt** and set **Links Parent** to Left Links. On the right builder, disable Left Belt and choose Right Links. The parent collector includes child mesh objects, so exclude sprockets, rollers and hull geometry.
4.  To select links individually, leave Links Parent empty and populate **Explicit Links**. You can also combine a parent collection with additional explicit entries; duplicate transforms are collected only once.
5.  Choose **Position → Mesh Bounds Center** for centers derived from mesh geometry, or **Transform Pivot** when the exported pivots already describe the belt path.
6.  Choose **Order → Around Belt** for automatic ordering around the Y/Z loop. If Create Path Builders copied an existing belt, it starts with **Input Order**; change it to Around Belt when you want automatic ordering. For unusual shapes, use Input Order, leave Links Parent empty and arrange Explicit Links around the complete loop in the intended order.
7.  Leave **Path Parent** empty to create a dedicated destination, or assign a separate path parent for that side. Keep this destination outside the moving-link hierarchy and separate from the other belt's destination.
8.  With the vehicle in a scene or Prefab Mode, outside Play Mode, press **Build Motion Path**. The builder assigns that side's Path and Links arrays together and preserves the model's resting pose.
9.  Inspect the numbered Scene lines. They should trace one continuous closed belt without jumping between unrelated segments. Use **Reverse Order** when the complete node/link order needs reversing, then build again.
10. Repeat for the other side, save the prefab and apply vehicle configuration before entering Play Mode.

Each belt needs at least three distinct link centers. If centers coincide, correct the model or use Mesh Bounds Center instead of shared pivots. Rebuilding updates this builder's generated nodes; keep custom children and components outside those generated nodes.

.. _uvs-tracked--4-create-the-paths-manually:

4. Create the paths manually
----------------------------

1. Add/configure **Track Visuals** and prepare the separate left/right link objects as above.
2. Create a **Left Track Path** parent that moves with the vehicle but is not inside a moving link. Add empty child GameObjects for its path nodes.
3. Place one node at the intended center or reference position of each left tread section in its resting pose. Use at least three distinct nodes and include the entire loop.
4. Fill **Left Belt → Path** in traversal order around the belt. The last entry connects back to the first automatically; do not add a duplicate closing node at the same position.
5. Fill **Left Belt → Links** with exactly the same number of entries. Each index must reference the tread section placed at the corresponding path node. Keep the matching nodes and links together when reordering.
6. Set **Travel Direction**, starting with the default -1. Build an independent right path and repeat the same process under Right Belt.
7. Apply configuration and save. Enter Play Mode from the authored resting pose so the system can retain each link's mesh orientation and its offset from the corresponding node.

Author or rebuild the paths outside Play Mode. Their positions and link offsets are prepared when the vehicle is configured; editing moving links during playback is not a replacement for editing the source path.

.. _uvs-tracked--5-match-direction-and-animate-rollers:

5. Match direction and animate rollers
--------------------------------------

Drive forward slowly and inspect both belts. Their lower runs should move toward the rear relative to the hull. If a correctly ordered belt travels backward, reverse that belt's **Travel Direction** sign. If the links jump across the belt, correct Path order and its matching Links rather than changing the speed sign.

For additional visible sprockets or rollers, add entries to **TrackVisuals → Rollers**. Assign each Transform, choose its left/right side, set its Radius and local rotation axis. Keep these rollers outside the builder's link collection. Mechanical road-wheel visuals may already be driven by their Wheel Setup and should not receive a second rotation owner.

Visible belt speed follows the configured wheels' rim speed, including reverse and airborne wheelspin. Disabling TrackVisuals leaves the mechanical drive intact. See :doc:`Track scripting </Scripting/Tracks>` for custom setup and movement APIs.

.. _uvs-tracked--test-a-complete-tracked-vehicle:

Test a complete tracked vehicle
-------------------------------

First disable TrackVisuals and verify the mechanics: straight forward/reverse, a moving left/right turn, a stationary pivot and a brake stop. Repeat on an incline and split-grip ground. Then enable the belt presentation and inspect direction/speed against each side's wheel RPM.

+-----------------------------------------------+--------------------------------------------------------------------------+
| Symptom                                       | Check                                                                    |
+===============================================+==========================================================================+
| Hull drives straight but will not turn        | Side assignments, inside speed/braking policy and excessive lateral grip |
+-----------------------------------------------+--------------------------------------------------------------------------+
| Stationary steering does nothing              | Engine running/available torque, brake priority and pivot configuration  |
+-----------------------------------------------+--------------------------------------------------------------------------+
| Turn loses more speed than desired            | Compensation/torque redistribution versus real power/contact limits      |
+-----------------------------------------------+--------------------------------------------------------------------------+
| Hull drifts sideways after a turn             | Surface grip, tracked lateral settings and bounded lateral stability     |
+-----------------------------------------------+--------------------------------------------------------------------------+
| Belt moves backward but mechanics are correct | That belt's Travel Direction sign                                        |
+-----------------------------------------------+--------------------------------------------------------------------------+
| Links jump across the loop                    | Node order and corresponding Link indices, not the speed sign            |
+-----------------------------------------------+--------------------------------------------------------------------------+
| Rollers jitter                                | Duplicate wheel/roller Transform animation owners                        |
+-----------------------------------------------+--------------------------------------------------------------------------+
| Builder collects hull objects                 | Clean Links Parent or use an explicit list                               |
+-----------------------------------------------+--------------------------------------------------------------------------+

For profile/side APIs, see :doc:`Track scripting </Scripting/Tracks>` and :doc:`API </API/Tracks>`. For gearbox, differential and TCS tuning, use their own guides; tune one drivetrain policy at a time rather than copying a road-car setup blindly.
