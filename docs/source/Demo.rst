.. _uvs-demo--demo:

Demo
====

Keep **Demo** selected when importing the package from **Package Manager → My Assets**. Open ``Assets/Szczyglis/UltraVehicleSystem/Demo/Demo.unity``.

.. _uvs-demo--select-a-vehicle:

Select a vehicle
----------------

+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| Key  | Demo vehicle                        | Example systems                                                                                 |
+======+=====================================+=================================================================================================+
| F1   | Car                                 | Rear-wheel drive, physical occupants, opening body parts, damage, windows, road/hover switching |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F2   | Monster Truck                       | Large tires, all-wheel drive and modular suspension                                             |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F3   | Military 6×6                        | Six wheel contacts and all-wheel drive                                                          |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F4   | Bus                                 | Rear drive, cabin controls and commercial audio                                                 |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F5   | Tractor                             | Articulated Semi Trailer and independent trailer brakes                                         |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F6   | Motorcycle                          | Assisted balance and physical rider                                                             |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F7   | Helicopter                          | Rotor spool, flight assistance and pilot controls                                               |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F8   | Airplane                            | Assisted flight, propeller and landing gear                                                     |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F9   | Drone                               | Hover, tilting rotor mounts and RPM-driven rotors                                               |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| 6    | Boat                                | Buoyancy, rudder/helm, water effects and physical driver                                        |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| 7    | Tank                                | Tracked drive, turret and physical projectiles                                                  |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| 8    | Jet                                 | Aerobatic flight, retractable gear, stores and cockpit gestures                                 |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| 9    | Submarine                           | Underwater propulsion, depth hold and dive controls                                             |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F10  | Quad                                | Four wheels, Wheeled profile and Balance Rider; reverse with alternating feet                   |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F12  | Scooter                             | Motorcycle profile, standing rider; reverse with the left foot                                  |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| Home | Bicycle                             | Motorcycle profile, seated Balance Rider and moving pedal targets; reverse with both feet       |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| End  | Spaceship                           | Six-axis flight, stationary hover and local-axis thrust; starts above Drone                     |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+
| F11  | Car (Animator, IK, ragdoll example) | Animated steering and cockpit gestures; compare Animator, Animator + IK and seated ragdoll      |
+------+-------------------------------------+-------------------------------------------------------------------------------------------------+

Page Up / Page Down cycles through the vehicles.

.. _uvs-demo--common-controls:

Common controls
---------------

+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Control                                       | Action                                                                            |
+===============================================+===================================================================================+
| W / S, A / D                                  | Ground driving, or profile-specific flight/water axes                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Space                                         | Ground handbrake or airplane wheel brakes                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| I                                             | Selected engine ignition                                                          |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| F                                             | Enter / exit the driver seat when stopped, where Seat Access is configured        |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| R                                             | Full reset: repair selected vehicle and restore its recorded spawn/passenger pose |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Tab / C                                       | Cycle Orbit, Interior, Cinematic, FREE PARENT and FREE LOOK cameras               |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Mouse / wheel                                 | Camera look/orbit and zoom                                                        |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Backspace                                     | Reset the complete scene (also in Editor Play Mode)                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Escape / click                                | Release / capture pointer                                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| N                                             | Day/night lighting                                                                |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| L                                             | Cycle low beams → high beams → off                                                |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| J / K / V                                     | Left indicator / right indicator / hazards                                        |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| X                                             | Wipers where installed                                                            |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| U                                             | Driving assists                                                                   |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| T, Q / E, numpad gear keys                    | Transmission mode, shifting and gear selection on ground vehicles                 |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Left Shift                                    | Ground-vehicle clutch                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| H (hold), gamepad east face button (B/Circle) | Horn on road vehicles                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| G                                             | Tractor/trailer attachment                                                        |
+-----------------------------------------------+-----------------------------------------------------------------------------------+
| Backquote (~)                                 | Show/hide vehicle and control hint panels                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------+

.. _uvs-demo--vehicle-controls:

Vehicle controls
----------------

+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vehicle                            | Controls                                                                                                                                                                                                       |
+====================================+================================================================================================================================================================================================================+
| Car                                | Enter: Nitro with automatic throttle; Left Ctrl: burnout launch (hold); B: next drive profile (drive/hover); O: opening body parts; F: entry/exit; Y: cycle aiming hand; left mouse: fire while aiming         |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Airplane / Jet                     | Shift/Ctrl: increase/decrease throttle; W/S: pitch; A/D: roll or taxi steering; Q/E: yaw; Space: wheel brakes; G: landing gear; Right Alt: Nitro; Comma: Burnout / propulsion boost (hold; automatic throttle) |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Spaceship                          | Shift/Ctrl: increase/decrease thrust; arrows: local strafe/lift; S/W: pitch; Q/E: yaw; A/D: roll; Z: reverse thrust; Space: clear thrust and brake                                                             |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jet stores                         | Enter: launch rocket; M: drop payload                                                                                                                                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hover                              | Shift/Ctrl: ascend/descend; Q/E: strafe; Enter: Nitro; Comma: propulsion boost (hold)                                                                                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Helicopter                         | Shift/Ctrl: ascend/descend; use the displayed attitude/yaw bindings; Enter: Nitro; Comma: propulsion boost (hold with collective/pitch/roll demand)                                                            |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tank                               | Brackets: turret rotation; Insert/Delete: elevation; Enter: fire; Right Alt: Nitro; Left Ctrl: Burnout                                                                                                         |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Submarine                          | W/S: thrust; A/D: turn; Shift/Ctrl: ascend/dive; Q/Z: pitch; Space: brake; Enter: Nitro; Comma: propulsion boost (hold)                                                                                        |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AI route examples                  | P: cycle Manual → AI (physics) → AI (direct) → Manual                                                                                                                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Other powered vehicles / Motorboat | Enter: Nitro; Left Ctrl: Burnout (hold). Boats require immersion; Nitro and Burnout supply forward throttle automatically. Release Nitro to refill.                                                            |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Reset clears boost requests, retained flight throttle, engine output and wheel spin, then repairs retained damaged/detached parts and dents before restoring the vehicle pose. Use the common R reset key; there are no separate repair buttons/shortcuts. UVS Car’s front-left WheelPart has Damage Enabled off in both prefab and scene. Destroyed debris still needs application respawning.

.. _uvs-demo--cameras:

Cameras
-------

Tab or C cycles **Orbit → Interior → Cinematic → Free Parent → Free Look**. Orbit and Interior use the selected vehicle's ``Cameras`` component and its explicitly assigned ``OrbitCamera.anchor`` and ``InteriorCamera.anchor``. ``CameraRigDemo`` switches and explicitly activates the attached scene camera between these submodules; Cinematic follows its heading through the Demo-only ``CinematicCameraDemo`` submodule. Free Parent and Free Look are custom ``CameraModule`` examples included only in the Demo, selected through the same ``Cameras`` core. Free Parent moves relative to the vehicle and remembers a local pose per vehicle; Free Look moves in world space. See :ref:`custom camera setup <uvs-cameras--custom-camera-submodules>` for extending and activating a view.

Free-camera movement: numpad 8 forward, 2/5 backward, 4/6 sideways, 9/3 up/down. Numpad + increases camera speed.

.. _uvs-demo--reuse-the-examples:

Reuse the examples
------------------

The sample's Prefabs folder contains the example vehicle configurations. ``Scripts`` is organized into ``Cameras``, ``Controls``, ``Environment``, ``UI`` and ``Vehicles``. These folders contain application integrations such as ``LandingGearSwitchDemo``, ``AimingHandDemo``, ``ExternalControlDemo`` and ``DirectWaypointAIDemo``.

See :doc:`Getting started </GettingStarted>` to build a vehicle, :doc:`Scripting </Scripting>` to integrate your game, and :doc:`Demo resources </DemoResources>` for asset bindings and credits.

.. _uvs-demo--compare-physical-and-direct-ai:

Compare physical and direct AI
------------------------------

For road vehicles, press **P** repeatedly to cycle **Manual (physics) → AI (physics) → AI (direct) → Manual (physics)**. The controls panel title reports the active mode and its P hint shows the next transition. Each vehicle retains its selected AI mode when another vehicle is selected. The route examples support Wheeled, Motorcycle and Tracked profiles.

Both AI examples use the same approach checkpoints and driving loop from ``ExternalControlDemo``. ``WaypointAIDemo`` submits throttle, steering and brake commands to an ``ExternalController``, leaving movement to vehicle physics. ``DirectWaypointAIDemo`` instead submits a world position and rotation each physics tick through ``DirectController.SetPose``. The package animates wheel rotation and steering from that direct movement. Automatic direct steering moves smoothly toward the inferred angle and returns to centre at **Steering Speed** (road-wheel degrees per second) in the vehicle settings. This affects wheel and steering-wheel visuals, without changing the supplied chassis path. Explicit analog steering with Automatic Steering disabled follows the supplied value directly. The demo example does not write wheel forces or move the chassis Transform itself.

The direct example preserves the chassis height relative to the route when activated and follows checkpoint height differences. It follows a look-ahead point along the checkpoint segments using continuous path curvature, starts turning before corners, and maintains cruising speed through the loop instead of stopping at each checkpoint. Look-ahead grows with speed and uses at least twice Arrival Distance; Turn Speed limits heading change. It does not use suspension forces or collision response to choose its path, and it has no obstacle avoidance or terrain sampling: an obstructed route can pass through obstacles. Resetting the vehicle restarts route selection at its current pose. Returning to manual or physical AI restores normal Rigidbody ownership through the controller API.

To reuse the example, assign a vehicle, its DirectController, an ordered loop with at least two valid checkpoint Transforms, and optional approach points. Call ``Begin()`` when giving it ownership, then select its controller as the vehicle Input Source. Tune **Speed Kph**, **Acceleration**, **Turn Speed** and **Arrival Distance** on the example. With the demo selector, use ``SetControlMode(vehicle, ControlModeDemo.AIDirect)`` or ``CycleControlMode(vehicle)`` so input ownership stays coordinated.

.. _uvs-demo--movable-boxes:

Movable boxes
~~~~~~~~~~~~~

Both the five **Dynamic crate** objects and the separate nine-box **Crash stack** use Rigidbody **Continuous Dynamic** detection and **Interpolate** display through ``DynamicObstacle``. The stack retains its authored 150 kg mass per box; the smaller crates retain 60 kg. No additional solver iterations or per-frame helper callbacks are enabled. These settings are included in both Demo and Samples scenes.

.. _uvs-demo--animator-passenger-example:

Animator passenger example
--------------------------

Press **F11** to select **Car (Animator, IK, ragdoll example)**. Its prefab is **Demo/Prefabs/CarAnimator.prefab**; supporting clips, Animator Controller and mannequin prefab are in **Demo/Prefabs/CarAnimator**.

1. Start Play Mode and select F11. The driver starts in **Animator** mode: a blend tree supplies both hands' steering poses without live arm IK. The visible wheel uses an 80-degree full-lock range for these fixed-grip clips; tire steering remains unchanged.
2. Press **Escape** to release the mouse. Use **Passenger example** below the vehicle list on the left to press the left/right switches, wave or cancel a gesture. Clicking inside the panel keeps the pointer available.
3. Choose the body strategy in **Seat** (Animator, Animator + IK, Ragdoll) and control ownership in **Handles** (Animator, Animator + IK, IK, Custom). Both default to Animator and switch independently; try Seat = Ragdoll with Handles = Animator. **Custom** uses external demo code rather than handle-owned Animator control. ``LeftContact`` and ``RightContact`` are finger-only layers configured on the handles; complete gestures use arm layers in Animator mode. The action commits once at its clip marker.
4. Inspect **Driver Seat**: the example selects **Parent** attachment for Animator and Animator + IK so the driver follows the moving seat, and **Spring** for Ragdoll to provide physical support while preserving the skeleton hierarchy for animated limbs.
5. Open the passenger's **PassengerAnimator** controller to inspect the steering blend tree and masked gesture layers. Fit gesture contacts and clips before adapting the example to another cockpit.

The ``AnimatorCarDemo`` panel provides separate seat and handle selectors. A change in one row preserves the other row's choice. Built-in modes use each handle's **Animator controller** settings; **Custom** demonstrates external steering and interaction control. See :ref:`the four-mode handle tutorial <uvs-handleanimation--four-mode-example>`. It belongs to the sample and is not a required runtime module. See :ref:`timed control interactions <uvs-controlinteractions--inspector-reach-with-ik-then-animate-a-switch-gesture>` for building an equivalent setup from the Inspector.

.. _uvs-demo--animated-entry-and-exit:

Animated entry and exit
-----------------------

Car and CarAnimator have left/right access profiles in ``Demo/Resources/UVSAccess``. Press **F** while stopped. ``LeftAccess`` / ``RightAccess`` use Animator root motion and manually calibrated foot-contact curves. ``LeftAccessOpen`` / ``RightAccessOpen`` use shorter clips without the door-opening/closing gestures; a door already open before access stays open. Both Car prefabs assign the matching open-door profile.

The closed-door clips issue **AccessOpenDoor**, **AccessWaitForOpenDoor** and **AccessCloseDoor** Animation Events. Playback waits before passage until the actual door is ready; blocked doors cancel after SeatAccess's Door Timeout. To customize stride, foot contacts or marker timing, follow :doc:`Animated access </PassengerAccess>`. Root motion and Foot IK can be configured independently in the profile.

.. _uvs-demo--rotor-contacts-and-jet-blast:

Rotor contacts and jet blast
----------------------------

The helicopter main rotor has three solid blade colliders and a metal body part that cannot detach through collision damage. Ground strikes use normal collision and damage contact sounds.

The demo Jet includes **Jet Blast** at its exhaust. Engine throttle and spool control its strength; bodies behind the nozzle are pushed with less force as distance increases. Newly created jets do not receive this optional component automatically. See :ref:`Jet Blast <uvs-particles--jet-blast>`.

.. _uvs-demo--motorcycle-riders:

Motorcycle riders
-----------------

The rider examples use the normal Inspector settings. Driver seats use **Affect Vehicle Physics** off: the vehicle moves the physical rider without the rider supports pushing the chassis. Enable it on Passenger Seat when two-way physical coupling is wanted. Quad's visible handlebar range is configured independently of road-wheel lock in **Steering Wheel Animator**. Foot reverse speed is configured on **Balance Rider**.

Select **Motorcycle**, **Quad (F10)**, **Scooter (F12)** or **Bicycle (Home)** to open the rider panel below the vehicle list. Quad uses a **Wheeled** profile with **Balance Rider**; Scooter uses a **Motorcycle** profile and a standing driver. Both new examples reverse in neutral using foot propulsion: alternating feet on Quad, left foot on Scooter. The panel also lets you choose both, left or right foot. Prefabs are **Demo/Prefabs/UVS Quad.prefab** and **Demo/Prefabs/UVS Scooter.prefab**. Switch gear/foot reversing, choose the driver's controller mode, and add/remove the optional rear passenger. Animator mode requires a suitable assigned controller; Animator + IK and Ragdoll Physics can follow the authored foot targets. The demo's Rider Animator rules provide parameter/condition examples for your own clips. See :ref:`motorcycle rider setup <uvs-seats--motorcycle-foot-reversing-and-rider-animations>`.
