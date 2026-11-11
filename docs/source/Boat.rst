.. _uvs-boat--boat-setup:

Boat setup
==========

Choose **Boat** for assisted surface flotation, forward/reverse propeller thrust and rudder-style steering. Configure the hull's movement here, its sampled water in :doc:`Water </Water>`, and any underwater vehicle in :doc:`Submarine </Submarine>`. Water rendering, particles, audio and visible propellers are separate from hull forces.

.. _uvs-boat--configure:

Configure
---------

1. Prepare a correctly scaled +Z-forward root with Rigidbody and suitable hull colliders. Choose **Tools > UltraVehicleSystem > Add Vehicle > Boat**, or select Boat under the existing controller's **Setup > Drive mode**.
2. Keep an enabled registered ``Drive`` module. Boat is wheel-free; wheel colliders are not its flotation points.
3. Configure an explicit ``WaterInteraction`` provider or a profile fallback plane using the :ref:`water workflow <uvs-water--set-up-a-water-surface>`.
4. Set mass, centre of mass, **Buoyancy Depth** and **Vertical Damping**, then test with propulsion off on flat sampled water.
5. Tune forward/reverse acceleration and resistance before steering.
6. Tune low-/high-speed steering, then rocking and powered trim.
7. Add occupants, helm motion, sound and particles only after the mechanical tests work consistently.

For a first test, turn off decorative wave excitation and use a simple flat provider. Check actual collider/ground clearance: a solid collider on the visible water plane can support/block the hull independently of buoyancy and hide a configuration error.

.. _uvs-boat--propeller-and-steering-visuals:

Propeller and steering visuals
------------------------------

Use **Propulsion** on the vehicle root (included by Boat setup). In **Propellers**, assign each propeller mesh, its **Local Axis** and rotation speed, or enable **Use Engine Rpm**. Enable **Only With Thrust** to stop at neutral and **Reverse With Thrust** to reverse its spin when backing up. **Only In Water** optionally stops rotation when the hull is dry.

Add **Steering Part** and assign an outboard motor or rudder pivot to **Part**. Connect a **Steering Source** component to **Input Source**, then set **Local Axis**, **Steering Angle**, **Multiplier** and **Reverse**. With no source assigned, it follows the vehicle steering command. Keep the spinning propeller on a child transform of the steering pivot. These components animate the model; hull steering remains controlled by the Boat profile.

.. _uvs-boat--flotation-and-immersion:

Flotation and immersion
-----------------------

The built-in model uses sampled water and centre-of-mass immersion to apply bounded support/vertical damping. It is an assisted hull model, not a per-triangle displaced-volume or flooding simulation. Hull mesh density is not a buoyancy setting.

**Buoyancy Depth** controls the depth scale over which support changes around the sampled height and centre of mass. **Vertical Damping** opposes vertical motion relative to the sampled water's vertical velocity. Check where the centre of mass sits relative to the intended waterline rather than raising the mesh alone to correct immersion.

The hull's physical colliders still handle docks, shore and other solid obstacles. Buoyancy does not make every collision safe or prevent grounding in shallow geometry. Test the intended mass, occupant/cargo arrangement and centre of mass, but do not interpret this assisted model as a naval load/displacement calculation.

Engine-off boats still float, resist motion and coast while in valid water. With an installed Engine, powered thrust/steering require it enabled and running. With no registered engine, the free-profile power policy treats the vehicle as externally powered; do not expect an absent ignition component to stop it.

Outside finite provider/fallback bounds, or with water interaction disabled, the profile supplies no water buoyancy/propulsion. Normal gravity and solid collisions still apply. See :ref:`water ownership switches <uvs-water--enable-or-disable-interaction>` before trying to repair that condition with a stronger spring.

To suspend vehicle forces and assistance, see :ref:`Release and restore all vehicle forces <uvs-driveprofiles--release-and-restore-all-vehicle-forces>`.

.. _uvs-boat--tune-handling:

Tune handling
-------------

.. _uvs-boat--forward-motion-and-coasting:

Forward motion and coasting
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Acceleration** sets the thrust-response scale. **Drag × Forward Drag Scale** contributes linear forward resistance, while **Speed Resistance** adds speed-dependent resistance. Lower resistance retains momentum longer; more thrust is not the only way to increase speed.

Resistance is resolved in the horizontal hull frame relative to water flow. A river current can move a boat relative to world space even when its speed relative to water is small. Check both the provider velocity and vehicle world velocity when tuning a river test.

Throttle is signed for forward/reverse. Brake contributes opposing powered water thrust while moving; it is not a native wheel brake or an anchor that locks position. With propulsion unavailable, water resistance remains but powered braking does not become a separate mechanical hull brake.

.. _uvs-boat--sideways-resistance:

Sideways resistance
~~~~~~~~~~~~~~~~~~~

**Lateral Resistance** damps sideways motion; **Speed Lateral Resistance** increases that response with forward speed. Tune lateral drift independently from forward coasting. Very large lateral resistance can make the hull feel constrained rather than floating, while very little can retain substantial sideslip after a turn.

.. _uvs-boat--underway-and-stationary-steering:

Underway and stationary steering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+--------------------------------------------+
| Setting                             | Effect                                     |
+=====================================+============================================+
| Maximum Yaw Rate                    | Upper requested underway yaw rate, rad/s   |
+-------------------------------------+--------------------------------------------+
| Steering Yaw Response               | Response toward the requested rate         |
+-------------------------------------+--------------------------------------------+
| Angular Damping × Yaw Damping Scale | Yaw resistance                             |
+-------------------------------------+--------------------------------------------+
| Stationary Turn Acceleration        | Low-speed maneuver authority               |
+-------------------------------------+--------------------------------------------+
| Stationary Yaw Rate                 | Low-speed requested turn-rate scale, rad/s |
+-------------------------------------+--------------------------------------------+
| Steering Rise / Return Time         | Digital demand buildup/return              |
+-------------------------------------+--------------------------------------------+

The rudder response first arrests an existing turn when countersteering, instead of accumulating unchecked opposing torque. Test a steady turn, release and reversal at the same speed. Low-speed maneuvering is deliberately configurable assistance; reduce it when a stationary boat should turn only weakly.

Analog steering demand is used directly; digital steering uses the configured rise/return smoothing. Make sure a custom input source labels its analog channels correctly. The helm's visible response is configured in :ref:`Interior controls <uvs-interiorcontrols--steering-wheel-and-hand-contacts>` and should not be used to tune hull yaw forces.

.. _uvs-boat--rocking-waves-and-powered-trim:

Rocking, waves and powered trim
-------------------------------

First make flotation, coast and turning stable. Then tune artificial excitation separately from support:

+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Group                                     | Configure                                                                                                         |
+===========================================+===================================================================================================================+
| Rocking Strength                          | Overall maneuver/background rocking excitation; zero disables excitation while retaining upright support/momentum |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Rocking Spring / Damping                  | Hull attitude settling                                                                                            |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Acceleration Tilt / Maximum Maneuver Tilt | Pitch/roll response to measured acceleration, in bounded degrees                                                  |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Powered Pitch Degrees                     | Sustained bow/stern trim under propeller load and motion                                                          |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Powered Pitch Rise / Release Time         | How gradually trim builds/settles                                                                                 |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Rocking Memory / Loaded Damping           | Retained response after maneuvers                                                                                 |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Ambient Wave Degrees / Period / Interval  | Continuous background sway and its variation                                                                      |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Idle Wave Degrees / Interval              | Occasional stronger impulses, including while moving                                                              |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

Power trim depends on load and actual forward motion; revving a nearly stationary boat should not pump the same trim as a powered run. Compare acceleration, sustained throttle, throttle release and reverse. Changing ambient excitation is different from changing the provider's actual wave height/velocity.

Use a single deliberate combination of sampled waves and artificial rocking. If the result is excessive, reduce one source at a time instead of damping every response into a rigid hull. Setting Rocking Strength to zero does not disable buoyancy.

.. _uvs-boat--hull-tilt-safety-limit:

Hull tilt safety limit
~~~~~~~~~~~~~~~~~~~~~~

**Maximum Hull Tilt** limits the assisted hull's pitch/roll in water (default 35°). The guard requires **Tilt Limit Enabled**, upright stabilization and both attitude axes. It limits powered tilting without locking the hull against collisions. Dependencies and individual settings are listed in the :ref:`Boat Profile reference <uvs-inspectorreference-drive--boatprofile>`.

.. _uvs-boat--animate-a-boat-propeller:

Animate a boat propeller
------------------------

Base ``Propulsion`` is shared by the supported aircraft/hover/submarine families. For Boat, use the :ref:`complete presentation extension <uvs-scripting-boat--animate-a-boat-propeller>` to add that family deliberately. A spinning mesh must not become a second thrust source.

Place a shaft pivot at its axis and keep mesh offsets beneath it. Choose whether visible rotation represents engine RPM, signed thrust intent or coasting motion, then implement/configure that presentation policy. Do not assume reversing hull velocity means the driver requested reverse thrust.

For a helm, use SteeringWheelAnimator and appropriate hand targets; for spray/wake/audio, follow :ref:`Water effects <uvs-water--add-audio-and-particles>`. Those guides own visual/sound setup so it does not need duplicating in the hull profile.

.. _uvs-boat--test-and-diagnose:

Test and diagnose
-----------------

+-----------------------------------------+----------------------------------------------------------------------------------+
| Test or symptom                         | Inspect                                                                          |
+=========================================+==================================================================================+
| Hull falls through visible water        | Provider sampling/bounds, interaction switch and actual centre-of-mass immersion |
+-----------------------------------------+----------------------------------------------------------------------------------+
| Engine-off hull still moves             | Expected buoyancy, momentum and provider current                                 |
+-----------------------------------------+----------------------------------------------------------------------------------+
| Boat stops too abruptly                 | Forward drag/Speed Resistance and brake demand                                   |
+-----------------------------------------+----------------------------------------------------------------------------------+
| Excess sideways drift                   | Lateral resistance before yaw/rocking changes                                    |
+-----------------------------------------+----------------------------------------------------------------------------------+
| Analog steering feels different         | Channel metadata versus digital rise/return policy                               |
+-----------------------------------------+----------------------------------------------------------------------------------+
| Boat rocks while no sampled waves exist | Ambient/idle profile excitation is independent                                   |
+-----------------------------------------+----------------------------------------------------------------------------------+
| Bow jumps under throttle                | Trim strength/rise time, measured motion and initial stability                   |
+-----------------------------------------+----------------------------------------------------------------------------------+
| Crossed water edge and lost support     | Finite dry-space result, not a rendering problem                                 |
+-----------------------------------------+----------------------------------------------------------------------------------+

Use a repeated route: engine-off float, slow forward/reverse, coast, steady turn, countersteer, stop and leave/re-enter the water bounds. Detailed resistance, load history and rocking contracts are in :doc:`Boat scripting </Scripting/Boat>` and :doc:`API </API/Boat>`.
