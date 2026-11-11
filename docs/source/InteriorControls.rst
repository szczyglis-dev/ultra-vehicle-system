.. _uvs-interiorcontrols--cockpit-controls-and-instruments:

Cockpit controls and instruments
================================

This guide explains how to build a working cockpit from separate meshes: gauges, steering wheels, pedals, switches, gear paddles, aircraft sticks, yokes and throttle levers. It covers their visual movement, connection to vehicle state, player interaction and passenger hand/foot targets.

Start with a vehicle whose steering, engine, gearbox and input already work. Test each instrument against that vehicle before adding character interaction. For speed units, see :doc:`Speed units </SpeedUnits>`; for individual field descriptions, see the :doc:`Inspector reference </InspectorReference>`.

For custom Animator/Timeline gestures, independent arm/finger weights and common contact/value events, follow :doc:`Custom handle animation and IK </HandleAnimation>`.

.. _uvs-interiorcontrols--inspector-quick-start-add-one-cockpit-control:

Inspector quick start: add one cockpit control
----------------------------------------------

1. Select the independently moving mesh/pivot in the Hierarchy, outside Play Mode. Put the pivot on its actual axis and keep surrounding dashboard geometry outside that group.
2. Add the appropriate animator through **Add Component > UltraVehicleSystem > Interior**: a steering-wheel animator, pedal animator, needle or switch helper. Configure its moving Transform, local axis and range using the corresponding tutorial below.
3. Add/select a built-in value source under **Interior > Controls > Source** when the animator needs one. Assign the owning Vehicle/Engine as required, then drag that source component into **Data Source**. A source reads the mechanic; it does not replace vehicle input.
4. Discover child modules from the vehicle's **Modules** tab and apply/save configuration. Test visible movement from ordinary driving before adding a passenger handle or timed interaction.
5. For a clickable switch, configure the matching mechanic binding and :ref:`ControlInteraction <uvs-controlinteractions--inspector-quick-start-wire-a-ui-action>`. For hands/feet, add the appropriate handle and assign it on the seat as described in :doc:`Handles </Handles>`. These are additional connections, not automatic consequences of adding an animator.

.. _uvs-interiorcontrols--inspector-layout-for-animators:

Inspector layout for animators
------------------------------

Set each control's ordinary range/response settings first. **[Control animator] > IK contact > Handle / Wait For Handle / Fake Sync Handle Motion** configures passenger synchronization. **[Control animator] > Motion > [geometry field]** is near the bottom, immediately above **Signals and callbacks**, followed by **Gizmos**. Motion has spacing above it, not an extra blank row below it.

For Switch Animator, **Initially On / Three Position / Initial Position / Neutral Offset / Transition Duration** are above IK contact. Callback fields such as On Value Changed and On Position Changed are under **Switch Animator > Signals and callbacks**. Pedal, rotary, paddle and other ControlAnimator-based components use the same bottom placement for Motion and callback groups.

**Gear Lever Animator > Gear positions** and keyboard gear-binding arrays have native +/− and drag reordering. Preserve the neutral entry at index 0 in **Keyboard Drive Input > Keyboard bindings > [gear-binding list]**; its remaining entries follow gear order. Preview tools restore their original pose when structural edits invalidate the selected gear.

For complete built-in pairing and custom contact instructions see :ref:`Handles <uvs-handles--tutorial-temporary-switch-throttle-or-pedal>`. For your own values/model mappings see :ref:`Interior scripting <uvs-scripting-interior--tutorial-provide-your-own-values-without-replacing-the-animator>`.

.. _uvs-interiorcontrols--choose-the-parts-of-a-control:

Choose the parts of a control
-----------------------------

A cockpit instrument usually combines several responsibilities:

+------------------+-------------------------------------------------------------+-----------------------------------------------------------------------+
| Part             | What it does                                                | Example                                                               |
+==================+=============================================================+=======================================================================+
| Moving geometry  | Defines the mesh, hinge, axis and travel                    | A speedometer needle or switch lever                                  |
+------------------+-------------------------------------------------------------+-----------------------------------------------------------------------+
| Value source     | Reads the value to display                                  | ``SpeedValueSource`` reads vehicle speed                              |
+------------------+-------------------------------------------------------------+-----------------------------------------------------------------------+
| Animator         | Maps a value or command to the model's pose                 | ``InstrumentNeedle``, ``PedalAnimator``, ``SteeringWheelAnimator``    |
+------------------+-------------------------------------------------------------+-----------------------------------------------------------------------+
| Binding          | Connects a control to a mechanic and synchronizes its state | ``WiperSwitchBinding`` connects a switch to ``Wipers``                |
+------------------+-------------------------------------------------------------+-----------------------------------------------------------------------+
| Interaction      | Decides when a player's action takes effect                 | ``ControlInteraction`` commits an action when a hand reaches a switch |
+------------------+-------------------------------------------------------------+-----------------------------------------------------------------------+
| Passenger target | Tells a seated hand or foot where to go                     | ``SwitchHandle.anchor`` or ``PedalHandle.anchor``                     |
+------------------+-------------------------------------------------------------+-----------------------------------------------------------------------+

A needle can display speed without a passenger. A switch can change wiper state without a hand animation. A hand target can guide a passenger without generating any vehicle input. Add the parts your cockpit needs.

Moving a visual control does not automatically drive the vehicle. ``PedalAnimator.SetValue`` moves a pedal; it does not apply engine throttle. ``ThrottleAnimator.SetThrottle`` moves a lever; it does not update the input source. A usable cockpit connects player intent to the appropriate vehicle action, then displays the resulting state.

.. _uvs-interiorcontrols--interchangeable-data-sources:

Interchangeable data sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All polling animators accept a **Data Source** component implementing ``IInteriorValueSource.ReadValue()``. Use the same contract for steering wheels, pedals, handbrake/brake/clutch levers, throttle grips and rotary instruments. A source only reads data; it does not apply vehicle commands. Sources can be shared by multiple consumers. Stock sources live under Interior / Controls / Source in Add Component and Tools.

+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| Consumer                             | Default source                                       | Returned domain                                              |
+======================================+======================================================+==============================================================+
| SteeringWheelAnimator                | SteeringSource                                       | Resolved steering -1..1; command steering in Hover           |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| PedalAnimator: accelerator           | GasSource                                            | Resolved propulsion; pedal may display its magnitude         |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| PedalAnimator: brake                 | ServiceBrakeSource                                   | Resolved braking 0..1                                        |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| AnchoredControlAnimator              | ServiceBrakeSource, ClutchSource or HandbrakeSource  | Pressure 0..1 or bool as 0/1                                 |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| TwistThrottleAnimator                | GasSource                                            | Propulsion magnitude 0..1                                    |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| ThrottleAnimator                     | GasSource with Use Resolved Demand disabled          | Raw Command.Throttle 0..1                                    |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| YokeAnimator / SteeringStickAnimator | RollSource plus independent Pitch Source             | Signed axes -1..1; roll follows wheel steering while taxiing |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+
| RotaryAnimator / InstrumentNeedle    | EngineRpmSource, SpeedValueSource or a custom source | Physical units matched to the instrument range               |
+--------------------------------------+------------------------------------------------------+--------------------------------------------------------------+

New polling animators added in the editor receive a default source. The shipped development and sample prefabs serialize the source assignments. For a brake/clutch/handbrake lever, replace Data Source with the corresponding source component. Shared sources may live elsewhere. Sources derived from VehicleValueSource resolve the nearest parent vehicle when Vehicle is empty; SpeedValueSource and EngineRpmSource retain their explicit Vehicle/Engine references. An unassigned source keeps the animator's built-in vehicle/command mapping; Rotary remains API-driven. Built-in input-selection fields are hidden fallback configuration for API-created components when Data Source is empty. Configure the visible source component to select an input or resolved/raw behavior.

An assigned disabled source, component not implementing the interface, or non-finite reading produces zero. Axis/pressure consumers clamp the result to their domains; sources return readings, never angles. Animator ranges, smoothing, Wait For Handle and Fake Sync remain presentation settings. ``ThrottleAnimator.SetThrottle`` explicitly overrides the source until ``FollowVehicle`` resumes it; ``PedalAnimator.SetValue`` does the same until ``FollowInput``.

GearLeverAnimator and GearShiftAnimator/GearPaddleAnimator retain ``Gearbox.GearChanged`` subscriptions. Switch bindings continue to use their owning mechanics and switch events; they do not receive a polling Data Source field.

See :ref:`a custom source example <uvs-scripting-interior--provide-custom-control-data>` for application-owned data without a VehicleController dependency.

.. _uvs-interiorcontrols--steering-angle-versus-hand-intent:

Steering angle versus hand intent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SteeringSource.ReadValue returns the resolved visual steering value by default. Its optional ISteeringIntentSource.ReadSteeringIntent contract returns the raw requested steering instead. The distinction is required for self-centering: after the driver releases steering, the wheel may still have an angle, but hand intent is already zero and parked palms can return. Custom scalar-only sources remain supported; implement ISteeringIntentSource too when the source smooths its visual value or models an actuator separately from the requested input.

.. _uvs-interiorcontrols--component-selection:

Component selection
-------------------

All hand/foot operated controls use separate Animator and IK Handle components. Add individual components under Interior / Animators and Passengers / IK / Handles, or use Tools → Interior → Control Pairs to create and connect both. Gauges may omit an IK contact.

+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Control                            | Components to start with                                       | Connection                                               |
+====================================+================================================================+==========================================================+
| Speedometer                        | ``InstrumentNeedle`` + ``SpeedValueSource``                    | Vehicle speed → needle                                   |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Tachometer                         | ``InstrumentNeedle`` + ``EngineRpmSource``                     | Engine RPM → needle                                      |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Fuel or another custom gauge       | ``InstrumentNeedle`` + custom ``InteriorValueSource``          | Numeric value → needle                                   |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Numeric knob or dial               | ``RotaryAnimator``                                             | ``SetValue`` / ``SetNormalizedValue``, optional source   |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Steering wheel                     | ``SteeringWheelAnimator`` + optional ``SteeringWheelHandle``   | Resolved steering → wheel; handle supplies hand contacts |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Accelerator, brake or clutch       | ``PedalAnimator``                                              | Vehicle command/resolved pedal demand → pedal            |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| One foot shared between two pedals | Two ``PedalAnimator`` + ``PedalHandle`` pairs                  | Brake demand selects the foot's destination              |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Gear paddle                        | ``GearPaddleAnimator`` + ``GearShiftAnimator``                 | Accepted gearbox change → paddle animation               |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Two-position switch                | ``SwitchAnimator`` + binding or event action                   | Off/on request ↔ mechanic state                          |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Indicator stalk                    | Three-position ``SwitchAnimator`` + ``IndicatorSwitchBinding`` | Left/off/right ↔ ``Lights``                              |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Wiper switch                       | ``SwitchAnimator`` + ``WiperSwitchBinding``                    | Off/on ↔ ``Wipers``                                      |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Drive/hover selector               | ``SwitchAnimator`` + ``ProfileSwitchBinding``                  | Off/on ↔ registered profile IDs                          |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Aircraft stick                     | ``SteeringStickAnimator`` + ``JoystickHandle`` or a pivot      | Pitch/roll commands → stick                              |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Aircraft yoke                      | ``YokeAnimator`` + optional ``YokeHandle``                     | Roll/ground steering + pitch → wheel and column          |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Aircraft throttle                  | ``ThrottleAnimator`` + ``ThrottleHandle``                      | Throttle command → lever                                 |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Fixed hand rest or footrest        | ``AnchorHandle``                                               | Stationary limb contact                                  |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Motorcycle handlebar               | ``MotorcycleHandle``                                           | Prepared grip geometry for both hands                    |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+
| Digital panel                      | ``CarHud`` or ``AircraftHud``                                  | Telemetry → cockpit surface texture                      |
+------------------------------------+----------------------------------------------------------------+----------------------------------------------------------+

Use **Add Component** and search for the component name, or use its entry under **Tools > UltraVehicleSystem > Add Component**. Helper components belong beside the model geometry. Place steering animators and ``GearShiftAnimator`` beside their control handles; assign their vehicle, engine and model references explicitly.

For modules, use **VehicleController > Modules > Add module...** and select the relevant Interior entry. The controller displays installed modules inside its category panels; model-mounted handles remain on their own objects. If you added modules directly through Unity's Add Component menu, use **Discover and order vehicle modules**, then **Apply vehicle configuration**, and verify that the intended module appears in the controller. Runtime-created modules should be registered through the :doc:`module API </Scripting/Modules>`.

A grayed-out field with a configuration-owner tooltip is assigned by the vehicle. Edit it at the indicated source; the next Apply can replace an edit to its copied value. Geometry fields that the vehicle does not manage remain editable on their helper objects.

.. _uvs-interiorcontrols--prepare-moving-geometry:

Prepare moving geometry
-----------------------

.. _uvs-interiorcontrols--separate-the-parts-that-move:

Separate the parts that move
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A control needs a separate Transform for every independently moving part. A needle baked into the dashboard mesh cannot rotate independently: separate it in your modelling application or provide a separate needle object. Keep the dashboard, dial face and surrounding trim stationary.

A useful arrangement is:

.. code:: text

   Vehicle
     Cockpit
       Speedometer
         DialFace
         NeedleAnchor       <- stationary hinge/reference frame
         NeedleCarrier      <- movingPart
           NeedleMesh       <- imported mesh and its visual offsets
       WiperSwitch
         SwitchAnchor       <- stationary reference frame
         LeverCarrier       <- movingPart
           LeverMesh
           PalmAnchor       <- moves with the lever

The neutral motion anchor and a palm/contact anchor serve different purposes. The motion anchor defines the hinge and stays independent of the part it moves. The palm/contact anchor follows the moving surface, so put it under that part.

.. _uvs-interiorcontrols--choose-the-right-motion-convention:

Choose the right motion convention
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two motion helpers are used by the controls:

+----------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Motion helper                                | Used by                                                    | Neutral-pose convention                                                                                         |
+==============================================+============================================================+=================================================================================================================+
| ``AnchoredRotation``                         | Needles, rotary controls, pedals, paddles and wiper blades | Rotates the part's captured neutral position and orientation around the anchor, preserving its original offset  |
+----------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``HandleMotion`` / ``AircraftControlMotion`` | Switches, aircraft throttle and stick helpers              | Preserves the captured authored neutral pose, then rotates around the anchor or translates along its local axis |
+----------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

For both, the anchor must be a different Transform and must not be a descendant of ``movingPart``. A sibling under the stationary dashboard is suitable. The anchor follows the vehicle; it should not stay behind in world space.

Both helpers preserve an off-centre mesh's neutral offset. Rotation uses the anchor as a hinge; translation uses its orientation as the direction frame and retains the mesh's rest orientation. Set the authored neutral pose before the first animation update. A clean carrier hierarchy remains useful for separating imported mesh corrections from passenger contacts.

**Steering Wheel Animator > Anchor** and **Steering Part > Anchor** provide an optional independent steering hinge and local axis frame; with no anchor these components retain their original rest-local rotation. **Yoke Animator > Pitch Anchor** independently selects the column translation direction. **Steering Stick Animator > Motion > Anchor** defines both pitch and roll axes for its motion helper; the inherited Anchor can supply an independent frame for the ordinary pivot animation.

.. _uvs-interiorcontrols--set-axes-and-travel:

Set axes and travel
~~~~~~~~~~~~~~~~~~~

1. Position the anchor at the physical hinge or needle centre.
2. Rotate the anchor so its local axes are easy to understand.
3. Assign the moving carrier to **Moving Part** and the stationary frame to **Anchor**.
4. Choose **Local Axis** in the anchor's coordinate system: ``(1, 0, 0)`` for local X, ``(0, 1, 0)`` for Y, or ``(0, 0, 1)`` for Z.
5. Set the endpoints. Rotation offsets are degrees. Translation offsets are metres along the normalized anchor direction; scaling the anchor does not multiply the travel distance.
6. Check both endpoints and the neutral pose before fitting the passenger's hands.

For reversed travel, swap the angle/offset endpoints or reverse the local axis. Keep the visual mesh's import correction on a child instead of compensating with several conflicting rotations. Avoid animation clips or another script writing the same moving Transform.

The specialized inspectors show motion geometry in the Scene view. Aircraft motion helpers also offer travel previews and independent-anchor creation; stick previews expose pitch and roll. Return controls to their intended neutral pose before capturing/calibrating a rest pose or saving a prefab.

.. _uvs-interiorcontrols--add-an-rpm-or-speed-needle:

Add an RPM or speed needle
--------------------------

.. _uvs-interiorcontrols--speedometer-from-start-to-finish:

Speedometer from start to finish
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a separate needle carrier and its stationary anchor as above.
2. Add ``InstrumentNeedle`` to the instrument object. Assign **Motion > Moving Part**, **Anchor** and **Local Axis**.
3. Add ``SpeedValueSource`` to the instrument or a nearby helper object.
4. Assign the vehicle to the source's **Vehicle** field.
5. Choose the source's **Speed Unit**. For an ordinary road speedometer, leave **Signed** off so reversing still produces a positive speed reading.
6. Drag the ``SpeedValueSource`` component into the needle's **Data Source** field.
7. Set **Minimum Value** and **Maximum Value** in the source's units. For a 0–240 km/h dial, use 0 and 240 with a Kph source.
8. Set **Minimum Angle** and **Maximum Angle** to match the printed scale. For example, use −130° and +130° for a 260° sweep around the chosen neutral frame.
9. Test at rest, while accelerating and in reverse. Check the end of the dial with a known value before judging the scale from driving alone.

The mapping is linear and clamps at the configured endpoints. A nonlinear printed dial needs a custom mapping/source or implementation. A speed source set to mph with a needle range authored in km/h produces an incorrect reading even if the animation looks smooth.

.. _uvs-interiorcontrols--tachometer:

Tachometer
~~~~~~~~~~

Repeat the speedometer setup with ``EngineRpmSource``. Assign its **Engine**, then assign that source to the needle. Set the value range in RPM, for example 0–8000, and use the angle endpoints printed on the tachometer. The source returns zero when its engine is absent or disabled; an enabled running engine can sit above zero at idle.

.. _uvs-interiorcontrols--response-direct-values-and-events:

Response, direct values and events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Response** controls exponential visual smoothing per second. Larger values approach the target more quickly; zero applies it immediately. This is separate from engine or vehicle response. The numeric value and its change event can update before the smoothed needle reaches its final angle.

Without a source, use ``SetValue`` for values in the configured units or ``SetNormalizedValue`` for a 0–1 fraction. ``SetImmediate`` updates both the value and pose immediately. These are useful for initialization and testing. With an enabled source assigned, the next update reads the source again and replaces a manually requested value. Disabling an assigned source makes its reading zero; disabling the engine while its RPM source remains enabled makes that source return zero.

``InstrumentNeedle`` inherits the same mapping and events as ``RotaryAnimator``. **On Value Changed** supplies the requested/clamped value in instrument units, not the displayed angle. Use it for related presentation if needed. It is not a measurement of the vehicle unless the instrument's source provides that measurement.

.. _uvs-interiorcontrols--fuel-temperature-pressure-and-other-values:

Fuel, temperature, pressure and other values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implement ``InteriorValueSource.ReadValue()`` for any numeric reading, assign the component to **Data Source**, and match the needle range to the returned units. The :ref:`complete fuel-source example <uvs-scripting-interior--add-a-fuel-needle-source>` returns ``FuelTank.Fraction``; configure its needle range as 0–1. A source returning litres needs a range in litres instead.

A value source can be reused by several instruments. Each needle can have its own sweep and smoothing. Missing data and warning lamps should be represented separately if the application needs to distinguish “zero” from “sensor unavailable”.

.. _uvs-interiorcontrols--configure-a-rotary-knob:

Configure a rotary knob
-----------------------

Use ``RotaryAnimator`` to map a numeric value to a visible knob. Set Data Source, value range, angle range and anchored geometry as for a needle. UI or code can call SetValue or SetNormalizedValue. Leave Data Source empty for an application-owned setting.

For hand operation, add a separate ``RotaryHandle``, parent its Anchor to the moving knob and assign it to the animator's Handle field. Configure the contact's ID, allowed limbs, occupant and grip pose in Passengers IK. The animator owns travel/events; the handle owns only limb contact. Tools → Interior → Control Pairs → Rotary creates and links both components.

.. _uvs-interiorcontrols--steering-wheel-and-hand-contacts:

Steering wheel and hand contacts
--------------------------------

.. _uvs-interiorcontrols--animate-the-wheel:

Animate the wheel
~~~~~~~~~~~~~~~~~

1. Put the wheel mesh beneath a Transform at the steering column axis.
2. Place ``SteeringWheelAnimator`` on the steering-wheel object alongside its ``SteeringWheelHandle``, then assign **Vehicle** to the parent vehicle controller and **Steering Wheel** to that object. Keep the animator registered in the vehicle module list.
3. Set **Local Rotation Axis** in that Transform's local frame. Use **Invert** if necessary.
4. Set the vehicle's steering-wheel rotation at full lock to suit the cockpit. This is the visible steering wheel rotation, not the road-wheel steering angle.
5. Use **Capture steering wheel rest pose** while the wheel is centred, then test left and right full lock.

The animator follows resolved vehicle steering. It does not steer the car by being rotated manually. Boat steering has a separate **Boat Steering Response** for visual settling; hover presentation follows its command-driven steering. Keep input configuration in the :doc:`input system </Input>`.

.. _uvs-interiorcontrols--attach-a-drivers-hands:

Attach a driver's hands
~~~~~~~~~~~~~~~~~~~~~~~

Add the appropriate contact handle to the moving wheel or handlebar, then follow :ref:`limb binding <uvs-handles--bind-a-limb-to-a-control>` and :doc:`hand fitting </SteeringHandGrip>`. Those guides cover seat assignment, wheel-rim dimensions, motorcycle grip preparation and fingers. This animator owns the wheel's visible movement; the handle provides contact geometry.

.. _uvs-interiorcontrols--pedals-and-foot-movement:

Pedals and foot movement
------------------------

.. _uvs-interiorcontrols--accelerator-brake-and-clutch:

Accelerator, brake and clutch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add ``PedalAnimator`` to the pedal control and configure its Motion with an independent hinge and moving mesh.
2. Assign GasSource, ServiceBrakeSource or ClutchSource to Data Source. Configure resolved/raw sampling on the source. Set released/pressed angles and independent press/release durations on the animator.
3. Add ``PedalHandle`` in Passengers IK. Put its Anchor on the moving pedal, then assign this contact to the animator's Handle.
4. Assign the driver's home foot to that IK handle. For a shared brake/accelerator foot, configure the brake contact's seat and preferred foot; the animator coordinates reaching when braking.
5. Keep Wait For Handle enabled when travel should wait for actual foot arrival. Mechanics still react immediately. Use SetValue or SetImmediate only for explicit visual presentation; FollowInput resumes command sampling.

.. _uvs-interiorcontrols--foot-operation-mode:

Foot operation mode
~~~~~~~~~~~~~~~~~~~

The **PedalHandle**, not the animator, owns Foot Mode. Press follows its moving Anchor. Rotation keeps Ankle Anchor outside the moving geometry and aims the foot towards the pedal contact; the ankle remains fixed while the foot tilts. The seat's foot Hold and IK Handle mode must remain enabled. An incomplete Rotation setup supplies no IK target.

.. _uvs-interiorcontrols--bind-the-passengers-foot:

Bind the passenger's foot
~~~~~~~~~~~~~~~~~~~~~~~~~

Set the seat's foot Handle to PedalHandle, never PedalAnimator. Configure allowed feet and transfer/return timings on the contact. Configure the value source on its component and model endpoints, response and Wait/Fake options on the animator. The contact observes its animator for generic value signals but never moves the pedal model.

.. _uvs-interiorcontrols--animate-a-gear-paddle:

Animate a gear paddle
---------------------

Add ``GearPaddleAnimator`` for the moving model and ``GearPaddleHandle`` for its palm contact. Parent the contact under the moving paddle and assign the animator's Handle. Set direction, pressed angle, press/return duration and Downshift Delay on the animator. Set occupant, allowed hand, reach/return timing and finger pose on the IK handle.

Assign the paddle animators to **GearShiftAnimator → Animators**. They implement IGearShiftAnimator and receive accepted gear changes. IK handles do not consume gearbox events. The Car uses the left hand for downshifts and the right hand for upshifts. Wait For Handle waits for the real palm; busy hands wait without a timeout bypass; the handbrake can interrupt a lower-priority timed paddle request through Interrupt Lower Priority. The press callback fires when visual pressing starts.

.. _uvs-interiorcontrols--floor-gear-lever:

Floor gear lever
~~~~~~~~~~~~~~~~

Use **GearLeverAnimator** for model movement and **GearLeverHandle** for the driver's contact. Assign Engine (to follow its active gearbox) or Gearbox directly, a stationary floor Anchor and a separate Moving Part whose origin matches that pivot. Parent the shaft, grip and palm contact below Moving Part. Select Rotation or Translation and author unique signed gear entries: -1 reverse, 0 neutral, positive forward gears. The Inspector previews each entry without commanding the gearbox.

Assign the driver's seat and preferred hand on the handle; leave Use On Action off because gearbox events request the reach. Wait For Handle waits for real contact before moving the lever. **Shift Duration** (default 0.18 s) controls visual lever travel independently of mechanical shift time. **Downshift Delay** defaults to 0.75 s after the latest reduction; repeated reductions restart the timer, while first gear, neutral, reverse and upshifts bypass it. Paddles use their own 0.25 s default. These delays affect presentation only.

The demo Bus alone has this floor lever, to the driver's right, with a compact gate around the first-gear pose. See :ref:`the full gear-control setup <uvs-scripting-interior--floor-mounted-gear-lever>` for ownership and repeated-shift behavior.

.. _uvs-interiorcontrols--bind-a-switch:

Bind a switch
-------------

.. _uvs-interiorcontrols--configure-two-positions:

Configure two positions
~~~~~~~~~~~~~~~~~~~~~~~

Add ``SwitchAnimator`` to the visible control. Assign its Motion geometry, off/on endpoints and transition duration. Add ``SwitchHandle`` in Passengers IK, parent its Anchor to the moving lever and assign the animator's Handle. The handle contains limb/pose settings; detents and events are on the animator.

Toggle, SetValue and SetImmediate are animator APIs. Immediate synchronization is silent. Connect lights, wipers, profiles and switch audio to SwitchAnimator, while seats and ControlInteraction targets reference SwitchHandle.

.. _uvs-interiorcontrols--configure-three-positions:

Configure three positions
~~~~~~~~~~~~~~~~~~~~~~~~~

Enable Three Position on SwitchAnimator. Select negative, neutral and positive detents and a neutral offset. PositionChanged/PositionReached distinguish all detents; binary IsOn treats negative and positive as on. IndicatorSwitchBinding maps the three positions to left/off/right lights.

.. _uvs-interiorcontrols--choose-the-correct-event:

Choose the correct event
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+---------------------------------------------+------------------------------------+
| Event                                         | When it fires                               | Typical use                        |
+===============================================+=============================================+====================================+
| ``PositionChanged`` / **On Position Changed** | Requested detent changes                    | Left/neutral/right action          |
+-----------------------------------------------+---------------------------------------------+------------------------------------+
| ``ValueChanged`` / **On Value Changed**       | Off/on status changes                       | Binary mechanic request            |
+-----------------------------------------------+---------------------------------------------+------------------------------------+
| ``PositionReached``                           | Visible travel reaches the requested detent | Completion feedback                |
+-----------------------------------------------+---------------------------------------------+------------------------------------+
| ``Switched``                                  | Visible travel settles, with its bool state | Settled-position click or feedback |
+-----------------------------------------------+---------------------------------------------+------------------------------------+

A request event can fire before the mesh reaches its destination. Immediate/silent synchronization does not send another user request. Do not wire a mechanic toggle to both request and completion events; one gesture would act twice. ``SwitchAudio`` can provide settled-position sound; see :doc:`Audio </Audio>`.

.. _uvs-interiorcontrols--indicator-stalk:

Indicator stalk
~~~~~~~~~~~~~~~

Add ``IndicatorSwitchBinding``, assign **Lights** and the three-position **Switch Animator**, then choose **Left Position** as Negative or Positive. The opposite endpoint means right and Neutral means off. Left Position cannot be Neutral.

The binding sends switch requests to ``Lights`` and follows changes made through keyboard/API control. Hazards have a separate control; their active state leaves this stalk centred. Vehicle Handles advances the switch animation once per physics step. The binding synchronizes commands and state.

.. _uvs-interiorcontrols--wiper-switch:

Wiper switch
~~~~~~~~~~~~

Add ``WiperSwitchBinding``, assign **Wipers** and **Switch Animator**. With **On Means Running** enabled, on requests running wipers; disable it for reversed switch semantics. The binding follows the module's aggregate running request, rather than the exact blade angle or completion of parking.

Use ``Wipers.SetSpeed`` separately for wipe frequency. This switch binding is an on/off control, not a multi-speed stalk. For an intermittent/multi-speed design, connect separate application actions to the wiper speed/running API. Blade setup and individual wiper control are covered in :ref:`Exterior wipers <uvs-wipers--wipers>`.

.. _uvs-interiorcontrols--other-binary-actions:

Other binary actions
~~~~~~~~~~~~~~~~~~~~

Connect **On Value Changed** to an action that accepts a bool, such as ``Lights.SetHeadlights(bool)``, using the dynamic bool argument in the UnityEvent menu. This sends the requested state. A method that blindly toggles state can become inverted when initialization or another input source changes the mechanic.

A plain UnityEvent connection only sends the action; it does not automatically observe external changes. Add your own binding if the control must follow changes made by keyboard, AI or save restoration, following the :ref:`binding contract <uvs-scripting-interior--gear-and-switch-bindings>`.

.. _uvs-interiorcontrols--anchored-contacts-and-lever-driven-finger-closure:

Anchored contacts and lever-driven finger closure
-------------------------------------------------

AnchorHandle and its derived control handles expose these settings independently of the animator that moves the model:

+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                          | Default              | Behavior                                                                                                                                                                 |
+=================================+======================+==========================================================================================================================================================================+
| Mode                            | Follow               | Normal contact following. Closure Change adds finger flexion from anchor distance.                                                                                       |
+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Anchor                          | Unassigned           | Palm or ankle target. In Closure Change, parent it to the stationary grip frame.                                                                                         |
+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Follow Anchor Rotation          | Enabled              | Disable to retain the initial resolved contact orientation relative to the vehicle while following anchor position. Applies to physical and Animator IK, including feet. |
+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Control Anchor                  | Unassigned           | Moving contact on the lever; used only for Closure Change.                                                                                                               |
+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Open Distance / Closed Distance | 0.06 / 0.03 m        | Distance at zero/full additional closure with multiplier 1. Open must be greater than Closed.                                                                            |
+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Closure Multiplier              | 1                    | Scales normalized closure before clamping to 0–1.                                                                                                                        |
+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Closure Angles                  | (20, 35, 25) degrees | Additional base/middle/tip flexion for index, middle, ring and little fingers. Thumb is excluded.                                                                        |
+---------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

To configure a brake lever, enable **Adaptive Grip**, place **Anchor** on the stationary handlebar and **Control Anchor** on the moving lever. Measure their released and pressed distances and enter them as Open and Closed Distance. Set the released finger pose in :doc:`Hands </HandPositions>`, then tune Closure Angles and Multiplier for the pressed pose. Disable Follow Anchor Rotation if the palm must retain its initial orientation relative to the vehicle.

Closure is ``clamp01((Open Distance - distance) / (Open Distance - Closed Distance) * Closure Multiplier)``. Missing anchors or an invalid distance range/multiplier produce zero closure. The adaptive finger pose adds flexion before its usual speed limit without refitting the grip on every lever movement. This is runtime closure, separate from the Hands editor's Closure authoring helper. The mode does not animate the lever or move Anchor to a stationary parent automatically.

The demo Motorcycle front brake uses ``FrontBrakeLever`` in Closure Change mode with Follow Anchor Rotation disabled. Its stationary palm contact and moving lever contact use Open Distance 0.0604152 m, Closed Distance 0.051 m, Multiplier 1 and angles (20, 35, 25). Service Brake requests the right hand; Anchored Control Animator waits for physical arrival before pressing. Outbound travel is 0.1 s, return 0.22 s and finger blend 0.1 s. The left hand stays on the bar; releasing the brake returns the right hand to its throttle grip. Both development and packaged sample prefabs carry this setup.

This handle option differs from the similarly named **Follow Anchor Rotation** on passenger transform supports, documented in :doc:`Seats </Seats>`: anchored handle contacts preserve orientation in the vehicle frame when disabled.

.. _uvs-interiorcontrols--choose-who-updates-the-control:

Choose who updates the control
------------------------------

+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| Component                                                      | Update owner                                                                                             |
+================================================================+==========================================================================================================+
| RotaryAnimator / InstrumentNeedle                              | Render update reads the optional value source and advances the visible angle                             |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| PedalAnimator                                                  | Module step samples demand; render update smooths pedal travel                                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| SwitchAnimator                                                 | Render update advances requested visual detents                                                          |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| GearPaddleAnimator                                             | Render update advances a triggered press/return                                                          |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| GearLeverAnimator / AnchoredControlAnimator / ThrottleAnimator | Presentation module step updates the model                                                               |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| SteeringWheelAnimator / YokeAnimator / SteeringStickAnimator   | Presentation module step owns steering geometry                                                          |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| IK handles                                                     | Supply contact/pose geometry, publish interaction values and let vehicle.handles schedule limb ownership |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

Do not call a second animation tick on an automatically updated component. Automatic Motion belongs to animators and can be disabled when Timeline or another animation system owns the model. SetInput on VehicleHandle is an IK-only hook for custom contact targets such as aiming; it does not animate instruments.

.. _uvs-interiorcontrols--add-player-interaction:

Add player interaction
----------------------

.. _uvs-interiorcontrols--ui-mouse-keyboard-and-raycasts:

UI, mouse, keyboard and raycasts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package controls expose actions; they do not automatically make a cockpit clickable. Use your UI, input action or raycast selector to identify a control, then call its public method or ``ControlInteraction.Begin``. A world-space canvas Button can call a parameterless method directly. A 3D raycast interaction needs suitable scene colliders and your selection code.

For a binary switch without a hand gesture, connect a Button's **On Click** to ``SwitchAnimator.Toggle``. For a knob, connect a Slider to the appropriate value method. For an interaction with an occupant, connect to ``ControlInteraction.Begin`` and put the vehicle action at its commit point.

.. _uvs-interiorcontrols--example-cockpit-sliders-that-actually-drive-the-vehicle:

Example: cockpit sliders that actually drive the vehicle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a UI-operated cockpit, add ``ExternalController`` to the vehicle and select it as the vehicle's **Input Source**. Keep the existing mechanical modules configured. This source receives the complete command from the UI; selecting it replaces the keyboard/action source as the vehicle's current input owner. For mixing several devices into one source, use the :doc:`custom input guide </Input>`.

Attach this example to a UI helper and assign that same ``ExternalController``. Connect three Sliders' dynamic **On Value Changed (float)** events to its setters: throttle range 0–1, steering range −1–1 with initial value 0, and brake range 0–1. Connect gear Buttons to ShiftUp/ShiftDown if a gearbox is installed. Set initial Slider values to zero. Start the vehicle's engine through your existing ignition control before testing propulsion.

**Example:** ``CockpitDrivingSliders.cs``

.. raw:: html

   <!-- example: CockpitDrivingSliders.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CockpitDrivingSliders : MonoBehaviour
       {
           public ExternalController input;
           private float throttle, steering, brake;

           public void SetThrottle(float value)
           {
               throttle = Mathf.Clamp01(value);
               Publish();
           }
           public void SetSteering(float value)
           {
               steering = Mathf.Clamp(value, -1, 1);
               Publish();
           }
           public void SetBrake(float value)
           {
               brake = Mathf.Clamp01(value);
               Publish();
           }
           public void ShiftUp() { if (input) input.ShiftGear(1); }
           public void ShiftDown() { if (input) input.ShiftGear(-1); }

           private void Publish()
           {
               if (input) input.SetAnalogAxes(throttle, steering, brake);
           }
           private void OnDisable()
           {
               throttle = steering = brake = 0;
               Publish();
           }
       }
   }

The buffer retains continuous axes until updated and consumes a queued shift once. These setters publish all three retained axes together, so moving the steering slider preserves the current throttle/brake request. Configure the visible pedals, steering animator and gear binding as above to show the result. Do not also call a separate visual lever setter as the only driving action: the input source is what delivers commands to the vehicle.

.. _uvs-interiorcontrols--gestures-and-action-timing:

Gestures and action timing
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``ControlInteraction`` when an action should wait for a hand reach or an animation contact frame. The complete :doc:`interaction guide </ControlInteractions>` covers Immediate, IK, Animator and Custom modes, a wiper-switch reach example, UI button code, animation events, cancellation and custom drivers. Configure the switch/mechanic binding here first, then add that gesture layer.

.. _uvs-interiorcontrols--aircraft-sticks-yokes-and-throttle-levers:

Aircraft sticks, yokes and throttle levers
------------------------------------------

.. _uvs-interiorcontrols--joystick:

Joystick
~~~~~~~~

Create a stationary hinge and moving stick hierarchy. Add ``SteeringStickAnimator``, configure its Motion, pitch/roll axes and ranges, and assign the owning vehicle. Add ``JoystickHandle`` to supply authored grip contacts and assign it to the animator's Handle and the relevant seat hand. Configure hand geometry only on the IK handle.

The animator samples pitch/roll commands and smooths them with Control Response. During fixed-wing taxiing, sideways motion follows resolved wheel steering without additional visual smoothing. Pitch retains its response. Rotation Pivot / Steering Wheel support a direct pivot rig; both paths are animator-owned and neither writes through the IK handle.

.. _uvs-interiorcontrols--yoke:

Yoke
~~~~

Use a sliding column with a rotating wheel beneath it. Add ``YokeAnimator``, assign **Vehicle**, **Steering Wheel** and **Pitch Slide**. Set the wheel's local rotation axis and **Invert** as necessary, then choose the column's **Local Pitch Travel Axis**, **Pitch Travel** in metres at unit scale, and **Control Response**.

Calibrate the rest pose with the yoke centred and the column neutral. Pitch moves the column; roll rotates the wheel. With an ``AirplaneGroundContact`` module, the yoke follows resolved steering without additional visual smoothing while grounded, and smooths roll commands while airborne. Pitch keeps its configured response. Without that ground-contact reference, roll remains the rotation source.

Add ``YokeHandle`` to the moving yoke when hand contacts are needed and assign it to the seat limbs. Keep the handle attached to geometry that follows both column translation and wheel rotation. It supplies contacts; ``YokeAnimator`` owns the movement.

.. _uvs-interiorcontrols--throttle-lever:

Throttle lever
~~~~~~~~~~~~~~

Create a moving lever, an independent hinge frame and a palm target under the lever. Add ``ThrottleAnimator`` and configure its Motion (rotation or translation), endpoints and Response. Add ``ThrottleHandle``, set its Anchor to the palm target, and assign it to the animator's Handle. Set Driver Seat / Use Left Hand and the seat's hand Handle as appropriate.

ThrottleAnimator owns displayed travel. ThrottleHandle owns grip, limb permission and contact only. SetThrottle supplies an external visual value; FollowVehicle restores command following. These presentation APIs do not drive the engine. Feed the input source to control the vehicle, then let the animator display the resulting command.

.. _uvs-interiorcontrols--digital-instruments-and-related-interior-systems:

Digital instruments and related interior systems
------------------------------------------------

For a panel rather than a physical needle, use :ref:`digital displays <uvs-interiorsystems--carhud>`. That guide owns screen setup, material/texture assignment, telemetry readouts and refresh rates, together with mirrors and individual wiper blades. Configure the control that requests their state here; configure the system that performs it there.

.. _uvs-interiorcontrols--verify-and-troubleshoot-a-finished-cockpit:

Verify and troubleshoot a finished cockpit
------------------------------------------

Check these stages in order: the vehicle mechanic works; the instrument receives the correct value; geometry moves correctly; the player action reaches the mechanic; external state changes resynchronize the control; the passenger can reach it throughout its travel.

+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Symptom                                       | Check                                                                                                                                                    |
+===============================================+==========================================================================================================================================================+
| A moving part snaps away on first update      | Motion convention, carrier position and neutral anchor; ``HandleMotion`` places the carrier on the anchor frame                                          |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Control does not move                         | Missing/invalid anchor, anchor beneath moving part, disabled component, missing value source, missing module registration or missing handle update owner |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Needle points to the wrong number             | Source units, value range, angle endpoints and signed-speed option                                                                                       |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Needle ignores a manual value                 | An assigned active source replaces it each update                                                                                                        |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lever moves but vehicle state does not change | Add a binding or connect the action; visual motion alone does not generate input                                                                         |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Switch state changes but mesh stays still     | Check the enabled vehicle and switch, same-vehicle hierarchy and vehicle.handles.Refresh after runtime additions                                         |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Switch animation is too fast                  | Both Passengers and a binding/application are advancing it                                                                                               |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Switch changes the mechanic twice             | Duplicate UnityEvent and callback actions, or a request wired to both changed and reached events                                                         |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Switch returns to its previous position       | Binding resynchronized a failed/unaccepted request, disabled mechanic, invalid profile ID or external state change                                       |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Steering wheel jitters                        | Two transform writers, uncalibrated rest pose, or animation clip also controlling the wheel                                                              |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Paddle never reacts                           | Working active gearbox, binding's engine/gearbox reference, accepted GearChanged event, matching direction and enabled handle                            |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

For exact signatures and individual fields, use the :doc:`Interior API </API/Interior>`, :doc:`handle API </API/Handles>`, :doc:`interaction API </API/Interactions>`, :doc:`Inspector reference </InspectorReference>` and :doc:`scripting guide </Scripting/Interior>`.

.. _uvs-interiorcontrols--alternative-motion-implementations:

Alternative motion implementations
----------------------------------

Control geometry supports Rotation, Translation, Animation and Custom through **Motion > Mode** (steering-wheel visuals: **Motion Mode**). Configure clips under **Motion > Animation**, or an ``ICustomPartMotion`` component under **Motion > Custom Driver**. Motion lifecycle callbacks are grouped with the existing control callbacks in **Signals and callbacks**, above **Gizmos**. Custom does not write a pose or run a built-in movement timer; report progress and completion from your implementation. Keep contact/input ownership on the control animator and geometry ownership on one implementation. See :ref:`four-mode setup <uvs-movingparts--choose-how-the-part-moves>` and :ref:`custom driver <uvs-scripting-movingparts--custom-motion-driver>`.

GearLeverAnimator has the same four modes under **Mode**. In Animation, set the shared **Animation > Animator**, then optionally assign **Gear positions > Element > Clip** for each gear; an empty per-gear clip falls back to **Animation > Clip**. Each selected clip plays from its start pose to the target gear pose. In Custom, **Signals and callbacks > On Gear Requested** reports the signed gear number, and ``RequestedGear`` exposes it in code. The normalized Custom target corresponds to the position's list index divided by count minus one (a single entry uses 1); a driver can instead read ``((GearLeverAnimator)motion.Owner).RequestedGear``. Report progress and completion through the same component APIs as other control animators.
