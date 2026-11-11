.. _uvs-aircraft--aircraft-setup:

Aircraft setup
==============

The package includes built-in controls and physics for multiple types of flying vehicles: airplanes, aerobatic aircraft, jets, helicopters, drones and hover vehicles. Choose a drive profile for the movement you want, then configure its controls, body, propulsion and optional landing gear. Cockpit animation, rotor visuals, sound and effects can be added independently.

.. _uvs-aircraft--choose-a-flight-profile:

Choose a flight profile
-----------------------

+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Profile            | Suitable vehicles                                              | Movement and control                                                                   |
+====================+================================================================+========================================================================================+
| Airplane           | Light aircraft and other assisted fixed-wing vehicles          | Assisted flight with pitch/bank limits, takeoff handling and ground/air blending.      |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Aerobatic Airplane | Aerobatic and freely maneuvering fixed-wing aircraft           | Pitch, roll and yaw rate control, including inverted flight.                           |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Jet                | Fighter jets and other fast fixed-wing aircraft                | Aerodynamic drag/lift, body-rate controls and G-limited response.                      |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Helicopter         | Helicopters and rotorcraft controlled by tilting the body      | Rotor-powered lift, pitch/roll movement, yaw and optional altitude hold.               |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Hover              | Drones, hovering platforms, flying cars and UFO-style vehicles | Direct forward/reverse movement, sideways thrust, vertical lift and assisted leveling. |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Spaceship          | Gravity-free spacecraft                                        | Local-axis thrust and rotation, with optional flight-path alignment and bank drift.    |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+

A drone is a vehicle configuration rather than a separate profile. Use **Hover** for direct movement and strafing, or **Helicopter** when horizontal movement should come from body tilt. The number and placement of visible rotors are configured separately from the movement profile.

**Spaceship** can hover without thrust. **Align Flight Path** redirects travel toward the nose, **Rotation Release Duration** smooths spin braking after release, and optional **Bank Drift** offsets the path with bank; downward drift is disabled by default. See the :ref:`profile settings <uvs-inspectorreference-drive--spaceshipprofile>` for adjustment and :ref:`Input <uvs-input--keyboard-bindings>` for thrust and braking controls.

.. _uvs-aircraft--one-configurable-fixed-wing-model:

One configurable fixed-wing model
---------------------------------

All fixed-wing physics lives in ``AirplaneProfile``. **Airplane**, **Aerobatic Airplane** and **Jet** are initial parameter presets; the latter two only set constructor defaults and inherit the same implementation. Existing preset type names remain available for saved profiles.

In the Inspector, **Control Mode** selects assisted pitch/bank targets or unrestricted body rates. **Aerodynamics** independently selects simplified lift/alignment or relative-airflow forces. **Progressive Thrust Envelope**, bank compensation, minimum air control authority, rate coordinated turn assistance and G/yaw limiters are editable on every preset. The remaining engine, landing-gear, lift, drag and response parameters are shared too.

To turn a Jet into an assisted light aircraft, select **Assisted Attitude** and **Simplified**, disable **Progressive Thrust Envelope**, enable **Bank Compensation Enabled**, set **Minimum Air Control Authority** to zero and tune engine power, acceleration, speed limits and gear settings for the airframe. To reproduce another preset exactly, copy all its settings: changing the two model selectors alone does not replace its tuning. Configure the vehicle again after changing engine, gear or rate settings.

The supplied Airplane and Jet prefabs explicitly store these settings in both the imported demo and ``Samples~``. The demo scenes inherit their aircraft configuration from those prefabs.

.. _uvs-aircraft--create-an-aircraft:

Create an aircraft
------------------

1. Prepare a unit-scale vehicle root facing +Z with a Rigidbody and a suitable hull collider.
2. Select **Tools → UltraVehicleSystem → Add Vehicle**, then choose the desired flight preset. On an existing vehicle, choose the profile under **VehicleController → Setup → Drive mode** and configure its supporting modules.
3. Set mass and the profile's movement settings. Keep an enabled ``Drive`` module registered so the selected profile receives physics updates.
4. Assign the input source. Use ``KeyboardFlightInput`` for the supplied keyboard controls, ``ActionInput`` for configured actions or ``ExternalController`` for commands from your application. See :doc:`Input </Input>`.
5. Configure propulsion and, where required, engine ignition and fuel. Add landing-gear wheels only when the chosen setup needs them.
6. Apply vehicle configuration and confirm movement before adding cockpit animation, occupants and effects.

Hover and Helicopter profiles do not require Wheel Setup entries. For fixed-wing aircraft, configure the profile's **Use Landing Gear** option according to whether the airframe has physical gear wheels.

To suspend vehicle forces and assistance, see :ref:`Release and restore all vehicle forces <uvs-driveprofiles--release-and-restore-all-vehicle-forces>`.

.. _uvs-aircraft--airplanes-and-jets:

Airplanes and jets
------------------

Configure mass, engine power, thrust, lift speed and flight-control response in **Setup**. Create landing-gear wheels as described in :ref:`Getting started <uvs-gettingstarted--create-your-first-wheel-vehicle>`. Turn **Drive** off on every gear wheel: aircraft propulsion acts on the body, not through driven wheels. Assign taxi steering and braking to the appropriate wheels.

Configure suspension, tire grip, braking and ground steering, then apply vehicle configuration. **Ground Steering Rate** controls keyboard taxi steering in both directions and the return to centre. The cockpit yoke and stick follow the same resolved taxi steering without a second visual delay. **Minimum Ground Turn Radius** still defines the low-speed geometry limit. An idle analog fallback does not override that return; active gamepad/joystick steering retains its direct analog response. Check taxiing, takeoff, engine-off glide and landing before adding cockpit animation.

The supplied keyboard input uses **Space** for wheel service brakes and **Left Alt** for the parking brake. Both lower retained keyboard throttle; parking commands also suppress aircraft thrust for external and analog inputs. Releasing the brake keeps the reduced throttle. A wheel-brake request remains active through takeoff/touchdown contact transitions; airborne wheels receive brake torque but cannot stop the airframe without ground contact.

Enable **Allow Ground Reverse** in the airplane/jet profile (default off), with landing gear and positive **Ground Reverse Speed/Acceleration**. Hold **Ground Reverse Key** (default Z) to reverse on the ground.

The shared wheel modules handle runway contact, including native suspension and supported tire-tread contact. ``AirplaneGroundContact`` exposes ``IsAirborne`` and ``FlightBlend``; takeoff contact grace and transition times control blending between ground and flight handling. Tire smoke, marks and audio use the same contact feedback as ground vehicles.

.. _uvs-aircraft--tune-the-flight-envelope:

Tune the flight envelope
------------------------

Start with mass, thrust, lift speed and maximum speed. Verify takeoff before changing attitude response. Use the drive profile's aircraft engine, gear-suspension, grip and ground-steering settings: Configure reapplies those values to the relevant modules.

Airplane uses assisted attitude limits; Aerobatic Airplane and Jet use body-rate controls for rolls and inverted flight. Jet adds aerodynamic drag/lift and a G-limited response. Tune low-speed authority separately from high-speed response.

Use Landing Gear requires configured wheels. For a wheel-free airframe disable it explicitly and check the hull contact/flight path. For retraction, keep wheel definitions authored and let LandingGear manage contact availability.

.. _uvs-aircraft--helicopters:

Helicopters
-----------

Choose **Helicopter** and tune the following settings in its drive profile:

-  **Acceleration** sets the vertical control authority and the basis for rotor-tilt movement. **Tilt Acceleration Multiplier** adjusts horizontal acceleration from body tilt.
-  **Compensate Gravity** supplies powered lift against gravity. **Vertical Damping** controls climb/descent damping, while **Drag** slows body motion.
-  **Automatic Leveling**, **Attitude Strength** and **Attitude Input Scale** shape the pitch/roll response. **Yaw Acceleration** controls turning around the vertical axis.
-  **Hold Altitude** captures the current height after releasing ascend/descend. With automatic leveling enabled, neutral movement input also brakes horizontal drift. It holds height and damps motion; it does not return the helicopter to a saved horizontal position.

Helicopter configuration ensures a ``Propulsion`` module exists. Set its **Spin Up Seconds** and **Spin Down Seconds**, then assign the main and tail rotor meshes in its propeller entries. Start the engine and allow the rotor to spool up before expecting full lift. Altitude hold requires a running engine and a nearly fully spooled rotor; stopping the engine releases the hold, and lift decreases as the rotor slows.

``KeyboardFlightInput`` maps W/S to pitch, A/D to roll, Q/E to yaw and Shift/Ctrl to ascend/descend. For custom controls, supply ``Command.Pitch``, ``Roll``, ``Yaw`` and ``Lift``. Configure the rotor axes and direction so visible rotation matches the model.

.. _uvs-aircraft--drones-and-hover-vehicles:

Drones and hover vehicles
-------------------------

Choose **Hover** for a drone, hovering platform or flying car that should move directly along its forward and sideways axes. Configure:

-  **Acceleration** for horizontal thrust and lift commands, **Drag** for resistance, and **Yaw Acceleration / Yaw Damping** for turning.
-  **Compensate Gravity** for powered support, **Vertical Damping** for climb/descent damping, and **Maximum Ascent / Descent Acceleration** for vertical correction limits.
-  **Automatic Leveling**, **Attitude Strength**, **Body Tilt Degrees** and **Body Tilt Response** for the hull's assisted attitude and lean.
-  **Surface Support**, **Height**, **Spring**, **Damping** and **Ground Mask** for minimum clearance above nearby surfaces. Height is a ground-clearance setting, not an absolute flight-altitude target. Lift commands still allow ascent above the surface-support region.

With neutral lift input, gravity compensation and damping reduce vertical drift. Hover does not use the Helicopter profile's captured-altitude hold. If an Engine is installed, its running state controls whether the Hover profile applies powered movement.

Hover configuration ensures ``HoverVisuals`` exists. Add rotor or engine mounts to its tilt entries and set their neutral poses. Use ``Propulsion`` for spinning rotor/propeller meshes and ``PropulsionJets`` for visual thrust outlets. Tune actual thrust and attitude forces in the drive profile. Wheel Tilt Response and wheel thrust/steering tilt settings control visual wheel lean on hover-capable cars; they do not change the wheel's authored neutral orientation.

``KeyboardFlightInput`` uses W/S for forward/reverse thrust, A/D for yaw, Q/E for sideways movement and Shift/Ctrl for ascend/descend. Custom providers use ``Command.Throttle``, ``Steering`` or ``Yaw``, ``Strafe`` and ``Lift``.

For a drive/hover vehicle, register both strategies in ``ProfileSwitcher`` and assign a bidirectional ``HoverDriveTransition`` to their IDs. The supplied Car/Porsche uses drive ↔ hover to fold wheels and restore road contact. See :doc:`Combined vehicles </CombinedVehicles>`.

.. _uvs-aircraft--animate-cockpit-and-exterior-controls:

Animate cockpit and exterior controls
-------------------------------------

For yokes, sticks, throttle levers and their passenger contacts, use the full :ref:`aircraft cockpit workflow <uvs-interiorcontrols--aircraft-sticks-yokes-and-throttle-levers>`. That guide owns pivots, ranges, animation ownership and hand binding, so those instructions are not repeated here. A cockpit animation does not provide the flight command itself.

.. _uvs-aircraft--exterior-control-surfaces:

Exterior control surfaces
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add ``AircraftControlSurface`` to each independently moving aileron, elevator, rudder, flap or airbrake assembly.
2. Configure its moving part, independent hinge frame, local axis and travel/direction for the model, then select **Type** (Rudder, left/right Aileron, Elevator, Flap, Airbrake or Custom). Use **Invert** for the needed sign; Custom mixes Pitch/Roll/Yaw through **Custom Mix**.
3. Add/register ``AircraftControlSurfaces`` and fill its **Surfaces** list with those helpers.
4. Test positive/negative pitch, roll and yaw separately. Opposite-side ailerons normally need opposing travel; do not rotate the airframe just to correct one mesh's sign.
5. Add flap/airbrake presentation and check full combinations for geometry clearance.

Use ``AircraftControlSurfaces.SetControls(pitch, roll, yaw)`` for external presentation, ``FollowVehicle()`` to resume command following, and ``SetFlaps`` / ``SetAirbrake`` for the additional channels. These animate geometry; they do not change the profile's aerodynamic authority. Change lift/drag/control policy in the flight strategy when the game requires a physical flap/airbrake effect.

Keep only one Transform writer on each surface. Flight can still work without animated surfaces because the built-in profile applies body forces independently; a moving aileron alone does not prove the correct roll input reached the vehicle.

.. _uvs-aircraft--retractable-landing-gear:

Retractable landing gear
------------------------

1. Add ``LandingGear`` and assign its native WheelCollider list.
2. Add a ``LandingGearPart`` for each moving strut, door or link and register the parts on LandingGear.
3. Assign each part's moving mesh and independent pivot anchor. Set its rotation axis or translation direction, retraction travel, duration and extension/retraction delays.
4. Use **Use current model pose as deployed (0)** to capture the reference pose. Preview the entire sequence, including doors and wheel clearance.
5. Configure the ground-contact/clearance interlock. Check deployment and retraction in flight and rejection on the ground.

**Preview retraction** and ``SetRetraction(0..1)`` use **0 deployed / 1 retracted**. The part's ``SetValue`` and ``DeployedFraction`` use **1 deployed / 0 retracted**. ``maximum`` sets signed retraction travel from the deployed pose; ``minimum`` is not used for gear motion.

``SetDeployed(bool)`` and ``Toggle()`` report whether a request was accepted. ``State``, ``RequestedDeployed``, ``IsDeployed``, ``IsGroundLocked`` and ``StateChanged`` support custom controls and instruments. Wheel contact is enabled at the fully deployed endpoint; hull colliders supply belly contact with the gear raised.

For explicit reset, ``ResetGear(bool deployed)`` applies the requested state immediately, bypassing the ground interlock. Reserve this for reset or spawn logic.

.. _uvs-aircraft--hinged-gear-suspension:

Hinged gear suspension
----------------------

Add ``LandingGearSuspension`` and configure its ``parts``. Each entry references a LandingGearPart, native WheelCollider, hinge axis and signed maximum opening angle. Set ``authoredAngle`` to the opening already present in the deployed model, or zero for a straight leg.

Tune **Spring Torque** in N·m/rad, **Damping Torque** in N·m·s/rad and **Angular Inertia** in kg·m². The native wheel supports the aircraft; contact load also bends the configured hinge. Check hinge limits and wheel alignment throughout suspension travel.

``IsStraight`` indicates readiness for retraction. ``ResetSuspension()`` clears displacement and angular velocity. Coordinate this with gear reset and vehicle teleport in application reset logic.

.. _uvs-aircraft--instruments-sound-and-effects:

Instruments, sound and effects
------------------------------

``AircraftHud`` publishes telemetry and ``Changed``, can bind a controller with ``Bind``, and exposes the landing gear. Assign ``customTexture`` for your own cockpit display. Subscribe to vehicle telemetry for custom airspeed, altitude, attitude and G-load instruments; see :doc:`API </API>`.

Assign an engine sound profile for the selected flight mode. Use ``Propulsion`` for visible propellers and rotors, and optional ``PropulsionJets`` for aircraft outlets. Configure emission, particle prefab/material and propulsion-spool response independently of mechanical thrust. See :doc:`Audio </Audio>` and :doc:`Particles </Particles>`.

For supplied keyboard bindings and example aircraft, see :doc:`Demo </Demo>`. For custom input, see :doc:`Input </Input>`.

For detailed flight, rotorcraft and landing-gear behavior, see :doc:`Aircraft scripting </Scripting/Aircraft>`.

.. _uvs-aircraft--configure-propellers-and-rotor-response:

Configure propellers and rotor response
---------------------------------------

``Propulsion`` provides shared spool state and visible propeller entries. Assign each rotor/shaft Transform, **Local Axis** and signed fixed **Degrees Per Second**, or select **Use Engine Rpm** with **Rpm Ratio**. A negative fixed speed/ratio reverses that visual rotation; it does not reverse the aircraft's thrust by itself.

Keep mesh import corrections beneath a clean shaft pivot. Configure main and tail rotors independently; assigning the whole airframe as a propeller Transform rotates the wrong hierarchy. Inspect at low speed before choosing high visual rates that can alias between frames.

**Spin Up Seconds** and **Spin Down Seconds** affect the shared spool. Helicopter powered support uses spool state, so its start/stop test must include the time to gain/lose rotor support. Demand-gated shaft options are a separate presentation policy; not every propeller should stop when a control axis is neutral.

Use :doc:`Audio </Audio>` for profile sound selection and :ref:`Particles <uvs-particles--propulsion-jets>` for outlet emission. A loop/prefab replacement should not be used to tune thrust, and extra visual rotors do not automatically add extra independently simulated lift points.

.. _uvs-aircraft--a-repeatable-flight-tuning-sequence:

A repeatable flight tuning sequence
-----------------------------------

+-------------------------+------------------------------------------------------------------------------------+
| Stage                   | Check before continuing                                                            |
+=========================+====================================================================================+
| Static setup            | Scale, mass/centre of mass, colliders, input channels and profile/module ownership |
+-------------------------+------------------------------------------------------------------------------------+
| Runway or initial hover | Loaded support, brakes/ground handling or powered rotor spool                      |
+-------------------------+------------------------------------------------------------------------------------+
| Acceleration            | Available thrust/power versus drag; cockpit animation is secondary                 |
+-------------------------+------------------------------------------------------------------------------------+
| Low-speed control       | Lift/authority onset, pitch/roll/yaw signs and stall/assistance behavior           |
+-------------------------+------------------------------------------------------------------------------------+
| Cruise                  | Speed/attitude settling and neutral-input response                                 |
+-------------------------+------------------------------------------------------------------------------------+
| Maneuver                | Requested body rates, available aerodynamic authority and energy loss              |
+-------------------------+------------------------------------------------------------------------------------+
| Engine-off              | Glide/descent or rotor spin-down, not a full powered hold                          |
+-------------------------+------------------------------------------------------------------------------------+
| Landing/reset           | Contact blend, gear endpoint, clearances and transient-state reset                 |
+-------------------------+------------------------------------------------------------------------------------+

Change one group at a time. Airplane's assisted attitude response differs from the body-rate policy in Aerobatic Airplane/Jet, so do not copy every response gain across profiles expecting identical control feel.

Jet's parasite/wing/side pressure drag and induced drag affect energy loss, particularly under load. Its Maximum G, stall angle and path response constrain the assisted response; they are not structural damage or pilot-blackout rules. Those gameplay consequences require an application policy.

Use :ref:`telemetry <uvs-scripting-events--diagnostic-snapshot>` for pose, world/local velocity, angular velocity, attitude and G readings. GForce is specific-force magnitude: roughly 1 G when supported at rest and 0 G in free fall. Airspeed uses the package's still-air velocity model; it is not a separate wind-provider measurement. A world altitude readout and height above ground are different quantities.

.. _uvs-aircraft--diagnose-aircraft-behavior:

Diagnose aircraft behavior
--------------------------

+--------------------------------------------+------------------------------------------------------------------------------------+
| Symptom                                    | Inspect                                                                            |
+============================================+====================================================================================+
| Engine runs but helicopter will not lift   | Powered/spooled Propulsion, gravity compensation and configured vertical authority |
+--------------------------------------------+------------------------------------------------------------------------------------+
| Hover height is not a captured altitude    | Surface Height is clearance support; Hover does not use helicopter hold            |
+--------------------------------------------+------------------------------------------------------------------------------------+
| Runway steering values revert              | Aircraft profile owns its configured ground-module fields                          |
+--------------------------------------------+------------------------------------------------------------------------------------+
| Gear refuses to retract                    | Ground/clearance interlock and hinged-suspension readiness                         |
+--------------------------------------------+------------------------------------------------------------------------------------+
| Gear mesh deployed but no wheel support    | Actual gear endpoint, wheel availability and source Wheel Setup                    |
+--------------------------------------------+------------------------------------------------------------------------------------+
| Aircraft turns but control surfaces do not | Exterior presentation references/FollowVehicle state                               |
+--------------------------------------------+------------------------------------------------------------------------------------+
| Aircraft has effects but no thrust         | Movement profile/input/power ownership rather than audio/particles                 |
+--------------------------------------------+------------------------------------------------------------------------------------+
| G limiter does not cause damage            | Flight-response limit is separate from application damage rules                    |
+--------------------------------------------+------------------------------------------------------------------------------------+

For vehicles that change between road, hover and flight, configure :doc:`registered mode transitions </CombinedVehicles>`. For water contact, use a dedicated :doc:`Boat </Boat>`/:doc:`Submarine </Submarine>` strategy and :doc:`provider </Water>`, rather than treating a rendered ocean as an automatic amphibious mode.

.. _uvs-aircraft--independent-visual-motion-frames:

Independent visual motion frames
--------------------------------

**Aircraft Control Motion > Anchor** and **Landing Gear Part > Anchor** define both the hinge point for rotation and the local axis frame for translation. Tilting an independent anchor changes the movement direction while preserving the authored mesh pose. Translation travel is measured in metres, independently of anchor scale. The Scene view endpoints use the same pose calculation as runtime.

**Landing Gear Suspension Part > Anchor** optionally supplies a separate spring hinge; leave it empty to use **Gear Part > Anchor**. Its local axes define **Local Axis**, and the same hinge drives the visible leg, wheel mount and spring-load torque.

For spinning visuals, **Propulsion > Propellers > Element > Anchor** optionally selects an independent shaft pivot and local axis frame. Keep it outside the rotating mesh hierarchy. With no anchor, the existing mesh-local spin remains in use. Endpoint-driven suspension helpers such as Control Arm, Shock Absorber, Half Shaft and Steering Tie Rod already use their explicit pivot/mount frames.

.. _uvs-aircraft--animation-and-custom-controlgear-geometry:

Animation and custom control/gear geometry
------------------------------------------

AircraftControlMotion and LandingGearPart expose **Mode** = Rotation, Translation, Animation or Custom. **Animation > Animator/Clip** binds the clip root; **Custom Driver** accepts ``ICustomPartMotion``. Lifecycle callbacks appear in **Signals and callbacks** above **Gizmos**. LandingGearPart maps progress 0 to deployed and 1 to retracted; Custom waits for reported progress rather than automatically retracting/extending the transform. Existing controllers still issue deployment requests and apply sequence delays. See :ref:`motion configuration <uvs-movingparts--choose-how-the-part-moves>`.

.. _uvs-aircraft--collidable-rotors:

Collidable rotors
~~~~~~~~~~~~~~~~~

Use separate solid colliders matching the individual blades, attached to the vehicle Rigidbody. Enable **Physics Rotation** for those entries in **Propulsion > Propellers** so their pose advances before simulation. A non-detaching metal ``DamagePart`` (``Detachment Multiplier = 0``) supplies metal contact responses; ``VehicleBodyPart`` in **Custom** motion leaves rotation to Propulsion. The demo helicopter includes this setup.

Airplane, Aerobatic Airplane and Jet profiles also expose **Speed Sensitive Rotation** with separate **Pitch/Yaw/Roll Rate By Speed** curves. X is actual travel speed in km/h and Y multiplies the base rotation rate. The switch defaults off. In Body Rates mode curves scale commanded rates before the existing G/yaw limits; in Assisted Attitude they scale restoring response and rudder demand while preserving target angles, damping and automatic turn coordination. A missing or empty curve uses 1.

**Rotation Release Duration** provides an optional soft release (seconds to approximately 95% settling). Zero preserves existing handling and is the default. In Body Rates mode it controls braking of released rotation axes; in Assisted Attitude it eases released pilot input to neutral while retaining automatic stabilization and damping. Control authority and acceleration limits can extend the actual settling time.
