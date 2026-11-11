.. _uvs-input--input-setup:

Input setup
===========

Assign a component implementing ``IVehicleInput`` to VehicleController's input source. Built-in adapters support keyboard, Input Actions and externally supplied commands. For the supplied scene's keyboard bindings, see :doc:`Demo </Demo>`.

.. _uvs-input--inspector-quick-start:

Inspector quick start
---------------------

1. Select the root and open **Setup > Input Source**. Drag the intended keyboard, ActionInput or external-input component into this field; merely adding it does not choose it as the vehicle's source.
2. For the demo-style keyboard adapter, open its panel under **Modules > Controller**, enable **Enable Controls**, expand **Keyboard Bindings**, and choose the needed keys. Use the adapter appropriate to the drive family.
3. For Input Actions, add/select **Action Input** and assign the required InputAction references as described below. Use one source/route per action so a press does not toggle the same feature twice.
4. Apply/save and test throttle, steering and brakes in Play Mode before lighting, gears and profile switching. Inspect **Live** to check whether the command reaches the controller before tuning the mechanic.

.. _uvs-input--keyboard-bindings:

Keyboard bindings
-----------------

The keyboard adapters expose an **Enable controls** checkbox, enabled by default, and a collapsed **Keyboard bindings** group. Expand it to choose keys for every action supported by that adapter. Defaults match the supplied controls; existing ignition, profile and airplane-brake assignments are preserved.

1. Select the vehicle's ``KeyboardDriveInput``, ``KeyboardFlightInput``, ``KeyboardBoatInput`` or ``KeyboardSubmarineInput`` component. It is also available in the vehicle Inspector's module view.
2. Expand **Keyboard bindings** and change the action's key dropdown. Alternate keys trigger the same action; choose ``None`` to leave a binding unassigned.
3. For ``KeyboardDriveInput``, **Gear Keys** and **Alternate Gear Keys** map array index 0 to neutral and subsequent indices to forward gears. Configure reverse gear separately.
4. Disable **Enable controls** to release this source's continuous controls and queued actions. The optional analog fallback is also blocked. Re-enabling does not replay old button presses; flight input clears its retained airplane throttle.

Drive input includes pedals, steering, clutch, direct gear selection, shifting, transmission mode, lights, ignition/profile switching, optional Nitro/Burnout requests and hover movement. **Nitro Key** defaults to Enter; **Burnout Key** defaults to Left Ctrl. They require the optional :ref:`Nitro module <uvs-drivingactions--nitro-boost>` or enabled :ref:`Burnout module <uvs-drivingactions--burnout-launch>`, respectively. ActionInput exposes optional Nitro/Burnout action references, and InputBuffer provides held setters. Flight input includes independent pitch/roll/yaw, steering, lift, hover strafe, airplane throttle increase/decrease and brakes. Boat and submarine inputs expose their supported movement and action keys. Camera/vehicle-selection reservations and profile-specific restrictions still apply.

The Demo controls panel reads these assignments for its keyboard hints. Demo-only actions such as camera movement and vehicle selection are configured by their own demo components.

**Keyboard Spaceship Input** uses Shift/Ctrl to increase/decrease retained forward thrust, arrows for local strafe/lift, S/W for nose-up/down, Q/E for yaw, A/D for roll and Z for reverse thrust. Space clears retained thrust and brakes momentum. Bindings are configurable in the :ref:`input settings <uvs-inspectorreference-controller--keyboardspaceshipinput>`; custom sources submit the normal Throttle, Strafe, Lift, Pitch, Yaw and Roll command fields.

.. _uvs-input--input-actions-and-gamepads:

Input Actions and gamepads
--------------------------

1. Add ``ActionInput`` and choose **Use as vehicle input**, or assign it as the controller's input source.
2. Use the built-in gamepad bindings or assign your own ``InputActionReference`` fields.
3. Use **Value / Axis** actions for pedals and steering. Pedals use 0..1; steering uses -1..1. A Vector2 source reads X for steering and Y for throttle.
4. Choose Auto, Analog or Digital per axis. Auto detects standard keyboard/buttons and analog controls.
5. If using ``PlayerInput``, assign it so references resolve against that player's action asset.

======================= =========================
Action                  Built-in gamepad binding
======================= =========================
Throttle / brake        Right / left trigger
Steering                Left stick X
Handbrake               West face button
Reverse / forward       North / south face button
Shift up / down         Right / left shoulder
Ignition / profile      Start / Select
Clutch                  Left-stick press
Headlights / high beams D-pad up / down
Indicators              D-pad left / right
Hazards                 Right-stick press
======================= =========================

Use **Refresh action bindings** after changing references during play. Configure action enabling and shared ownership as described in the :doc:`input reference </Scripting/Input>`.

.. _uvs-input--digital-and-analog-response:

Digital and analog response
---------------------------

Use ``Brakes.progressiveDigitalBraking`` and ``brakeRiseTime`` for a gradual digital brake response. Analog channels preserve continuous pedal/steering values. Configure deadzones and processors in the Input Action asset.

For custom providers, mark continuous axes in ``Command.AnalogControls`` and buttons in ``DigitalControls``. Use ``InputBuffer.SetAnalogAxes`` for analog commands. See the :ref:`channel policy <uvs-scripting-input--progressive-keyboard-braking-and-analog-controllers>` for the corresponding mechanical response.

.. _uvs-input--writing-your-own-input-source:

Writing your own input source
-----------------------------

Create a ``MonoBehaviour`` implementing ``UltraVehicleSystem.IVehicleInput``. Its ``ReadCommand()`` returns the driver's current intentions: throttle, steering, brake and optional one-shot actions. Vehicle Controller calls this method once per physics tick. Your code supplies commands; the existing vehicle modules apply the forces.

For an immediately playable starting point, use the keyboard or gamepad script below. The helicopter example maps flight axes to keys; the later providers accept values from your own UI or device adapter. For handbrake, pitch, yaw, gears and every other available control, see the :ref:`complete Command field tables <uvs-input--all-command-fields-control-mapping-reference>` at the end of this page.

.. _uvs-input--ready-to-drive-keyboard-example:

Ready-to-drive keyboard example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This custom source reads WASD and common car controls directly. It also buffers ignition, shifts, transmission mode and headlights so a press is consumed once, even when several physics ticks run in one rendered frame. No UI callbacks or extra adapter are needed.

1. Save the script as ``SimpleKeyboardCarInput.cs`` and add it to a vehicle that already drives correctly.
2. Drag this component into **Vehicle Controller → Input Source**. Use a configured engine and gearbox, or direct drive. Press I if the engine is off. For a manual gearbox, hold Left Shift to press the clutch and press E to select first gear from neutral, then release the clutch; the gearbox still applies its shift admission rules.
3. Enter Play Mode and click the Game view to give it keyboard focus. Hold **W** to accelerate, **A/D** to steer, **Left Ctrl** for the service brake and **Space** for the handbrake. **S** sends negative drive demand: the vehicle's direction/brake logic handles braking and reverse. On an automatic gearbox, release and press S again at standstill if reverse engagement requires a fresh press.

**Example:** ``SimpleKeyboardCarInput.cs``

.. raw:: html

   <!-- example: SimpleKeyboardCarInput.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.InputSystem;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SimpleKeyboardCarInput : MonoBehaviour, IVehicleInput
       {
           public bool holdReverseUntilStopped = false;
           private bool ignitionPending, transmissionPending, headlightsPending;
           private int shiftPending;

           private void Update()
           {
               var keys = Keyboard.current;
               if (keys == null || !Application.isFocused) { ClearPending(); return; }

               if (keys.iKey.wasPressedThisFrame) ignitionPending = true;
               if (keys.tKey.wasPressedThisFrame) transmissionPending = true;
               if (keys.lKey.wasPressedThisFrame) headlightsPending = true;
               if (keys.qKey.wasPressedThisFrame) shiftPending = -1;
               if (keys.eKey.wasPressedThisFrame) shiftPending = 1;
           }

           public Command ReadCommand()
           {
               var keys = Keyboard.current;
               if (keys == null || !Application.isFocused) { ClearPending(); return default; }

               float throttle = (keys.wKey.isPressed ? 1f : 0f)
                              - (keys.sKey.isPressed ? 1f : 0f);
               float steering = (keys.dKey.isPressed ? 1f : 0f)
                              - (keys.aKey.isPressed ? 1f : 0f);

               var result = new Command(throttle, steering)
               {
                   Handbrake = keys.spaceKey.isPressed,
                   HoldReverseRequest = holdReverseUntilStopped && throttle < -.1f,
                   ServiceBrake = keys.leftCtrlKey.isPressed ? 1f : 0f,
                   Clutch = keys.leftShiftKey.isPressed ? 1f : 0f,
                   Horn = keys.cKey.isPressed,
                   Nitro = keys.enterKey.isPressed,
                   ToggleIgnition = ignitionPending,
                   ToggleTransmission = transmissionPending,
                   ToggleHeadlights = headlightsPending,
                   Shift = shiftPending,
                   DigitalControls = InputChannels.Throttle | InputChannels.Steering |
                                     InputChannels.ServiceBrake | InputChannels.Clutch
               };
               ClearPending(); // Keep held keys; consume only the queued button presses.
               return result;
           }

           private void ClearPending()
           {
               ignitionPending = transmissionPending = headlightsPending = false;
               shiftPending = 0;
           }

           private void OnDisable() => ClearPending();
           private void OnApplicationFocus(bool focused)
           {
               if (!focused) ClearPending();
           }
       }
   }

+------------+-------------------------------+--------------------------------------------------------+
| Key        | Command                       | How to use it                                          |
+============+===============================+========================================================+
| W / S      | ``Throttle = 1 / -1``         | Hold for forward/reverse demand.                       |
+------------+-------------------------------+--------------------------------------------------------+
| A / D      | ``Steering = -1 / 1``         | Hold to steer left/right.                              |
+------------+-------------------------------+--------------------------------------------------------+
| Left Ctrl  | ``ServiceBrake = 1``          | Hold the service brake.                                |
+------------+-------------------------------+--------------------------------------------------------+
| Space      | ``Handbrake = true``          | Hold the handbrake.                                    |
+------------+-------------------------------+--------------------------------------------------------+
| Left Shift | ``Clutch = 1``                | Hold to disconnect the optional clutch.                |
+------------+-------------------------------+--------------------------------------------------------+
| I          | ``ToggleIgnition = true``     | Press once to switch ignition.                         |
+------------+-------------------------------+--------------------------------------------------------+
| Q / E      | ``Shift = -1 / 1``            | Press once to shift down/up.                           |
+------------+-------------------------------+--------------------------------------------------------+
| T          | ``ToggleTransmission = true`` | Press once to switch the configured transmission mode. |
+------------+-------------------------------+--------------------------------------------------------+
| L          | ``ToggleHeadlights = true``   | Press once to toggle headlights.                       |
+------------+-------------------------------+--------------------------------------------------------+
| H          | ``Horn = true``               | Hold to sound the optional horn audio.                 |
+------------+-------------------------------+--------------------------------------------------------+
| Enter      | ``Nitro = true``              | Hold to request the optional Nitro module.             |
+------------+-------------------------------+--------------------------------------------------------+

Assign the matching modules for optional features: a command alone does not install lights, a horn, a clutch or Nitro. In the demo, choose a vehicle before assigning this source, because demo selection can restore its configured input source.

Releasing the keys immediately releases their command; A and D together cancel steering. Marking these channels digital lets the existing engine, steering and brake modules apply their configured button response. For softer button braking, enable **Brakes → Progressive Digital Braking** and adjust **Brake Rise Time**. To change a key in this example, replace its ``keys.…Key`` reference.

.. _uvs-input--ready-to-drive-analog-gamepad-example:

Ready-to-drive analog gamepad example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version reads a connected gamepad directly. It needs no Input Action asset and no setter calls: the **left stick X** steers, **right trigger** accelerates, **left trigger** brakes, and the **west face button** (X on an Xbox-style pad, Square on a PlayStation-style pad) applies the handbrake.

Save it as ``SimpleGamepadCarInput.cs``, add it to the vehicle and assign it to **Vehicle Controller → Input Source** instead of the keyboard example. Use the same running-engine/automatic-first-gear or direct-drive setup, connect the pad, then focus the Game view. This short example drives forward; it leaves reverse selection, ignition and manual shifting to your game or the fuller providers below.

**Example:** ``SimpleGamepadCarInput.cs``

.. raw:: html

   <!-- example: SimpleGamepadCarInput.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.InputSystem;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SimpleGamepadCarInput : MonoBehaviour, IVehicleInput
       {
           public Command ReadCommand()
           {
               var pad = Gamepad.current;
               if (pad == null || !Application.isFocused) return default;

               return new Command(Mathf.Clamp01(pad.rightTrigger.ReadValue()), Mathf.Clamp(pad.leftStick.ReadValue().x, -1f, 1f))
               {
                   Handbrake = pad.buttonWest.isPressed,
                   ServiceBrake = Mathf.Clamp01(pad.leftTrigger.ReadValue()),
                   AnalogControls = InputChannels.Throttle |
                                    InputChannels.Steering | InputChannels.ServiceBrake
               };
           }
       }
   }

Moving the stick halfway requests half steering; pressing a trigger halfway requests half the corresponding pedal. Returning the stick to centre sends zero steering. The analog flags preserve those proportional requests, bypassing keyboard ramps. The Input System's device processors, including the stick deadzone, still apply.

Both scripts read continuous held values inside ``ReadCommand()``, exactly when Vehicle Controller samples them. They return released controls if the device is missing or the application is unfocused. New-press actions such as ignition toggles or gear shifts need buffering in ``Update()`` so a short press between physics ticks is not missed; the keyboard script above demonstrates that buffer. If several shift presses arrive before the next physics sample, it retains the latest direction. The examples use the Unity Input System already required by the package. With a custom assembly definition, reference ``UltraVehicleSystem.Runtime`` and ``Unity.InputSystem``.

.. _uvs-input--ready-to-fly-helicopter-keyboard-example:

Ready-to-fly helicopter keyboard example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a helicopter using ``HelicopterProfile``, save this as ``SimpleKeyboardHelicopterInput.cs``, attach it to the configured helicopter and assign it to **Vehicle Controller → Input Source**. Start with the engine running and let the rotor spool up. Enable the profile's vertical lift, horizontal drive, automatic leveling and yaw controls for this mapping. This source replaces the car source; it does not combine with it.

Hold **W/S** to tilt forward/backward, **A/D** to tilt left/right, **Q/E** to turn left/right and **R/F** to request climb/descent. Releasing a pair returns its axis to zero. Neutral lift follows the profile's altitude-hold settings; it does not necessarily cut lift or land the helicopter.

**Example:** ``SimpleKeyboardHelicopterInput.cs``

.. raw:: html

   <!-- example: SimpleKeyboardHelicopterInput.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UnityEngine.InputSystem;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SimpleKeyboardHelicopterInput : MonoBehaviour, IVehicleInput
       {
           public Command ReadCommand()
           {
               var keys = Keyboard.current;
               if (keys == null || !Application.isFocused) return default;

               return new Command(0f, 0f)
               {
                   Pitch = (keys.wKey.isPressed ? 1f : 0f)
                         - (keys.sKey.isPressed ? 1f : 0f),
                   Roll = (keys.dKey.isPressed ? 1f : 0f)
                        - (keys.aKey.isPressed ? 1f : 0f),
                   Yaw = (keys.eKey.isPressed ? 1f : 0f)
                       - (keys.qKey.isPressed ? 1f : 0f),
                   Lift = (keys.rKey.isPressed ? 1f : 0f)
                        - (keys.fKey.isPressed ? 1f : 0f),
                   DigitalControls = InputChannels.Flight
               };
           }
       }
   }

For an airplane, supply a separate 0..1 throttle request and use negative ``Pitch`` to raise the nose. For hover lateral movement, fill ``Strafe``. The command fields below describe these differences; use the profile matching your vehicle rather than copying the helicopter mapping unchanged.

.. _uvs-input--providers-driven-by-your-own-ui-or-device-code:

Providers driven by your own UI or device code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following longer examples when another script or UI already reads the controls and should pass values into your provider. For a quick keyboard/gamepad test, the two scripts above are sufficient.

.. _uvs-input--connect-a-custom-source:

Connect a custom source
~~~~~~~~~~~~~~~~~~~~~~~

1. Save the chosen script using its example filename and add it to your configured vehicle.
2. Assign that component to **Vehicle Controller → Input Source**. Keep the source enabled. Only the selected source is sampled, even if a keyboard adapter is also present.
3. Connect your UI or device adapter to its public methods as described below. Setting a value retains it until you change it or call ``ClearControls()``.
4. Start with the engine running and an automatic gearbox or direct drive. For a manual gearbox, send gear/clutch commands yourself. ``SelectGear(1)`` requests first, ``SelectGear(0)`` neutral, and ``SelectGear(-1)`` reverse; the gearbox still validates each request.
5. At a player/AI ownership change, clear the outgoing source, choose the next source with ``vehicle.SetInputSource(nextSource)``, and clear any stale values in the incoming source. See :ref:`runtime ownership <uvs-scripting-input--external-controller-and-runtime-ownership>` for a complete handover pattern.

.. _uvs-input--analog-proportional-steering-and-pedals:

Analog: proportional steering and pedals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Save this as ``CustomAnalogCarInput.cs``. A small steering value produces a small steering request; half a brake pedal produces a 0.5 brake request. The ``AnalogControls`` flags tell the mechanics to preserve these proportions instead of applying keyboard ramps.

**Example:** ``CustomAnalogCarInput.cs``

.. raw:: html

   <!-- example: CustomAnalogCarInput.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CustomAnalogCarInput : MonoBehaviour, IVehicleInput
       {
           private Command pending;

           // UI sliders or your device-reading code can call these methods.
           public void SetThrottle(float value) => pending.Throttle = Signed(value);
           public void SetSteering(float value) => pending.Steering = Signed(value);
           public void SetBrake(float value) => pending.ServiceBrake = Mathf.Clamp01(Signed(value));
           public void SetClutch(float value) => pending.Clutch = Mathf.Clamp01(Signed(value));
           public void SetHandbrake(bool held) => pending.Handbrake = held;

           // Call on a press/event, not on every frame while a button is held.
           public void ToggleIgnition() => pending.ToggleIgnition = true;
           public void ShiftUp() => pending.Shift = 1;
           public void ShiftDown() => pending.Shift = -1;
           public void SelectGear(int gear) => pending.RequestedGear = gear;

           public Command ReadCommand()
           {
               Command result = pending;
               result.AnalogControls = InputChannels.Throttle | InputChannels.Steering |
                                       InputChannels.ServiceBrake | InputChannels.Clutch;
               result.DigitalControls = InputChannels.None;

               // Keep held axes; consume each queued action only once.
               pending.ToggleIgnition = false;
               pending.Shift = 0;
               pending.RequestedGear = null;
               return result;
           }

           public void ClearControls() => pending = default;
           private void OnDisable() => ClearControls();
           private void OnApplicationFocus(bool focused)
           {
               if (!focused) ClearControls();
           }

           private static float Signed(float value) =>
               float.IsFinite(value) ? Mathf.Clamp(value, -1, 1) : 0;
       }
   }

For a slider-based test, connect each Slider's **On Value Changed → Dynamic float** to the corresponding method:

+-----------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Control         | Range                  | Method and effect                                                                                         |
+=================+========================+===========================================================================================================+
| Steering slider | -1 to 1, starting at 0 | ``SetSteering``: -1 left, 0 straight, 1 right.                                                            |
+-----------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Throttle slider | 0 to 1, starting at 0  | ``SetThrottle``: released to full accelerator. Signed -1..1 is also accepted for direction-based driving. |
+-----------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Brake slider    | 0 to 1, starting at 0  | ``SetBrake``: released to full service brake.                                                             |
+-----------------+------------------------+-----------------------------------------------------------------------------------------------------------+
| Clutch slider   | 0 to 1, starting at 0  | ``SetClutch``: 0 couples the engine; 1 fully presses/disconnects the clutch. Requires a Clutch module.    |
+-----------------+------------------------+-----------------------------------------------------------------------------------------------------------+

Connect an ignition button's **On Click** to ``ToggleIgnition``, gear buttons to ``ShiftUp``/``ShiftDown`` or ``SelectGear``, and a Toggle's value change to ``SetHandbrake``. A normal slider retains its position: centring steering and releasing the accelerator are your UI/device adapter's responsibility. Device axes can call these same setters whenever a new sample arrives; map a physical wheel's range to -1..1 and separate pedals to 0..1 before submission.

.. _uvs-input--digital-held-buttons-with-keyboard-response:

Digital: held buttons with keyboard response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Save this as ``CustomDigitalCarInput.cs``. This version stores pressed/released states and builds axes from them. Opposing direction buttons cancel each other. Its ``DigitalControls`` flags enable the vehicle's configured digital handling, such as steering slew and progressive braking. The ramp settings still belong to the vehicle mechanics: for example, enable ``Brakes.progressiveDigitalBraking`` and set ``brakeRiseTime`` if you want the brake to build up gradually.

**Example:** ``CustomDigitalCarInput.cs``

.. raw:: html

   <!-- example: CustomDigitalCarInput.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CustomDigitalCarInput : MonoBehaviour, IVehicleInput
       {
           private bool forward, reverse, left, right, brake, clutch, handbrake;
           private bool ignitionPending;
           private int shiftPending;
           private int? gearPending;

           public void SetForward(bool held) => forward = held;
           public void SetReverse(bool held) => reverse = held;
           public void SetLeft(bool held) => left = held;
           public void SetRight(bool held) => right = held;
           public void SetBrake(bool held) => brake = held;
           public void SetClutch(bool held) => clutch = held;
           public void SetHandbrake(bool held) => handbrake = held;

           public void ToggleIgnition() => ignitionPending = true;
           public void ShiftUp() => shiftPending = 1;
           public void ShiftDown() => shiftPending = -1;
           public void SelectGear(int gear) => gearPending = gear;

           public Command ReadCommand()
           {
               var result = new Command((forward ? 1 : 0) - (reverse ? 1 : 0), (right ? 1 : 0) - (left ? 1 : 0))
               {
                   Handbrake = handbrake,
                   ServiceBrake = brake ? 1 : 0,
                   Clutch = clutch ? 1 : 0,
                   DigitalControls = InputChannels.Throttle | InputChannels.Steering |
                                     InputChannels.ServiceBrake | InputChannels.Clutch,
                   AnalogControls = InputChannels.None,
                   ToggleIgnition = ignitionPending,
                   Shift = shiftPending,
                   RequestedGear = gearPending
               };
               ignitionPending = false;
               shiftPending = 0;
               gearPending = null;
               return result;
           }

           public void ClearControls()
           {
               forward = reverse = left = right = brake = clutch = handbrake = false;
               ignitionPending = false;
               shiftPending = 0;
               gearPending = null;
           }

           private void OnDisable() => ClearControls();
           private void OnApplicationFocus(bool focused)
           {
               if (!focused) ClearControls();
           }
       }
   }

For touch controls, add an Event Trigger to each UI button. Connect **Pointer Down** to its setter with a fixed ``true`` argument and **Pointer Up** to the same setter with ``false``. For example, the left button calls ``SetLeft(true)`` while pressed and ``SetLeft(false)`` on release. Also clear held values if the UI closes or a pointer interaction is cancelled, so a hidden button cannot leave the car accelerating. **On Click** alone is appropriate for ignition and gear changes, but does not represent a held accelerator or steering button.

For your own keyboard adapter, call the setters with the key's current held state in ``Update()``. Queue ``ToggleIgnition``, ``ShiftUp``, ``ShiftDown`` and direct gear selection only on a new press. The provider keeps those one-shot requests until the next physics sample, then clears them. If several shift requests arrive before that sample, these minimal examples retain the latest direction rather than queuing multiple shifts.

.. _uvs-input--mixing-analog-and-digital-controls:

Mixing analog and digital controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The flags apply per channel. For a steering wheel plus a brake button, mark **Steering** analog and **ServiceBrake** digital. Do not mark a channel both ways: analog takes precedence. Handbrake is a held boolean and does not need an axis flag. Use one source to combine all your input before returning a command; the vehicle does not automatically merge two assigned adapters.

You can also subclass ``InputBuffer`` instead of implementing ``IVehicleInput`` from scratch. It already stores axes and consumes one-shot actions; use ``SetAnalogAxes`` for proportional controls, or ``SetAxes`` with the appropriate ``digitalControls`` flags for buttons. The examples above show the full contract when you want to own the implementation yourself. See :ref:`digital and analog response <uvs-input--digital-and-analog-response>` and :ref:`command sampling <uvs-scripting-input--sampling-contract>` for the mechanics and timing.

.. _uvs-input--ai-replay-and-external-control:

AI, replay and external control
-------------------------------

Use ``InputBuffer`` or ``ExternalController`` to submit axes and one-shot actions. Select it with ``vehicle.SetInputSource(source)`` and call ``ClearControls()`` when the producer disconnects or relinquishes control. ``SetInputSource(null)`` releases the source.

The :ref:`input reference <uvs-scripting-input--external-controller-and-runtime-ownership>` includes a source handover example and describes retained commands, focus behavior and sampling. :doc:`Scripting </Scripting>` lists command and event APIs.

Use ``SetControlsEnabled``, ``TrySetBinding``, ``TryGetBinding`` and ``ResetBindings`` from your scripts; see :ref:`runtime keyboard configuration <uvs-scripting-input--runtime-keyboard-configuration>`.

.. _uvs-input--direct-pose-control-for-ai-and-scripted-traffic:

Direct pose control for AI and scripted traffic
-----------------------------------------------

Use **Direct Controller** when your AI, route follower, replay or networking system already knows the car's world position and rotation. In this mode the source places the chassis; the package derives movement speed, rolls the tire visuals, turns steering wheels/calipers and the cabin steering wheel, updates RPM and publishes telemetry from that movement. Ordinary input sources still drive the physical car through throttle, braking and steering.

.. _uvs-input--setup-and-switching:

Setup and switching
~~~~~~~~~~~~~~~~~~~

1. Add **Input → Sources → Direct Controller** to a configured vehicle and assign it as **Vehicle Controller → Input Source**. Its **Use as vehicle input** context action does the same assignment.
2. Leave **Direct Control** enabled. Supply poses through ``SetPose(position, rotation)``, or assign an independent **Pose Target** transform that your AI moves. Keep that target outside the vehicle hierarchy. A target belonging to the vehicle is ignored to prevent a self-follow loop.
3. Leave **Automatic Steering** enabled to estimate steering from the change in heading and signed travel. Wheel spacing supplies the approximate wheelbase; a vehicle with no usable axle span falls back to 2.5 m. Each wheel's steering role/multiplier and the configured full-lock angle still apply.
4. For explicit steering, disable **Automatic Steering** and call the inherited ``SetAnalogAxes(throttle, steering, brake)``. Steering is -1..1 and works at standstill. Throttle/brake in direct mode drive presentation; they do not override the supplied trajectory. If throttle is zero, moving speed supplies a fallback engine demand; measured deceleration can also light the brakes.
5. To return to physical driving, select the usual keyboard/action/external source with ``SetInputSource``. Alternatively, call ``direct.SetDirectControl(false)``: the same component then works as an ordinary ``ExternalController``, using buffered throttle/steering/brake commands. A flag change is applied at the next physics tick; replacing the source releases existing direct ownership immediately.

Only the selected, enabled source can activate direct mode. Merely adding this component does not change the vehicle. The optional ``IDirectInput`` capability exposes ``DirectControl``, ``AutomaticSteering`` and ``ReadPose(currentPose, deltaTime)`` alongside the existing ``IVehicleInput.ReadCommand()``.

.. _uvs-input--example-move-a-car-directly-toward-a-point:

Example: move a car directly toward a point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Save this as ``DirectCarToPoint.cs``, add it beside the controller and assign Vehicle, Direct and a target point outside the vehicle. Start with the vehicle already on a drivable, level surface. This script demonstrates authoritative movement; your navigation code can replace its ``MoveTowards``/``RotateTowards`` decisions with a spline, path, traffic simulation or replay sample.

**Example:** ``DirectCarToPoint.cs``

.. raw:: html

   <!-- example: DirectCarToPoint.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       // Produce this tick's pose before VehicleController samples its source.
       [DefaultExecutionOrder(-100)]
       public class DirectCarToPoint : MonoBehaviour
       {
           public VehicleController vehicle;
           public DirectController direct;
           public Transform destination;
           [Min(0)] public float speedMetresPerSecond = 5;
           [Min(0)] public float turnDegreesPerSecond = 90;
           private MonoBehaviour previousInput;
           private bool ownsInput;

           private void OnEnable()
           {
               if (!vehicle || !direct || !direct.isActiveAndEnabled) return;
               previousInput = vehicle.inputSource == direct ? null : vehicle.inputSource;
               direct.ClearControls();
               direct.ClearPose();
               direct.SetDirectControl(true);
               vehicle.SetInputSource(direct);
               ownsInput = true;
           }

           private void FixedUpdate()
           {
               if (!ownsInput || !vehicle || !direct || !direct.isActiveAndEnabled ||
                   !vehicle.isActiveAndEnabled || vehicle.inputSource != direct || !vehicle.Body) return;
               if (!destination) { direct.ClearPose(); return; }

               Vector3 position = vehicle.Body.position;
               Quaternion rotation = vehicle.Body.rotation;
               Vector3 next = Vector3.MoveTowards(position, destination.position,
                   Mathf.Max(0, speedMetresPerSecond) * Time.fixedDeltaTime);
               Vector3 direction = Vector3.ProjectOnPlane(destination.position - position, Vector3.up);
               if (direction.sqrMagnitude > 0.001f)
                   rotation = Quaternion.RotateTowards(rotation,
                       Quaternion.LookRotation(direction, Vector3.up),
                       Mathf.Max(0, turnDegreesPerSecond) * Time.fixedDeltaTime);
               direct.SetPose(next, rotation);
           }

           private void OnDisable()
           {
               if (!ownsInput) return;
               if (direct) { direct.ClearControls(); direct.ClearPose(); }
               if (vehicle && vehicle.inputSource == direct)
                   vehicle.SetInputSource(previousInput ? previousInput : null);
               ownsInput = false;
           }
       }
   }

An assigned **Pose Target** takes precedence over ``SetPose``; leave it empty for the script above. ``SetPose`` takes world metres and a world-space quaternion, normalizes valid rotations and returns ``false`` for invalid values. ``ClearPose()`` stops using a stored pose and holds the last applied position until another pose or independent target is supplied. Repeating the same pose produces zero measured speed and stops wheel spin. Disabling DirectController clears its stored commands/pose; its assigned Pose Target remains configured.

.. _uvs-input--what-remains-physical:

What remains physical
~~~~~~~~~~~~~~~~~~~~~

The chassis temporarily becomes kinematic and is moved through ``Rigidbody.MovePosition``/``MoveRotation``. Engine/drive/brake/traction/suspension force modules do not determine its path. Collisions do not stop or deflect this authoritative car; the navigation/traffic producer must provide an unobstructed trajectory and any collision-avoidance decisions. Existing body colliders can still contact other dynamic objects. Direct motion works with the engine off; engine state only affects its presentation in this mode.

Wheel rotation comes from signed hub travel divided by tire radius, including different travel on the inside/outside of a turn. Ground queries position the wheel visuals along their configured suspension travel; they do not lift, bank or ground the chassis for you. Supply the root's height, pitch and roll in the pose. Automatic steering is an approximation for ordinary forward/reverse paths; for sliding, turning on the spot or a special axle layout, supply steering explicitly. The inferred contacts have no physically simulated tire slip, so they do not invent burnouts or skid forces.

Interior, exterior and effects modules keep stepping. Engine/fuel presentation, cameras and the passenger core also opt in; supplemental solid-tire force proxies are suspended. Other modules are skipped by default in direct mode. A custom module can override ``SupportsDirectControl`` when its step is safe for authoritative motion. Independent custom ``Update``/``FixedUpdate`` scripts are still your application's responsibility.

Use ``VehicleController.Velocity``, ``AngularVelocity`` and ``GetPointVelocity`` when consuming the current direct step's measured motion. Raw native Rigidbody velocity/contact values can reflect the previous physics solve. For wheel consumers, ``Wheel.Rpm``, ``GetWorldPose`` and ``GetGroundHit`` work in both modes; native ``WheelCollider.rpm``/contacts remain physics-only data. Reported direct contact force is an approximate static mass share for presentation, not a solved suspension force.

On release, the original kinematic/collision-detection state is restored. A previously dynamic chassis inherits the last measured linear/angular velocity so physical driving can continue from its current motion. Large pose jumps therefore imply large speeds: use ``VehicleController.Teleport`` for a respawn/cut, then clear/update the source's pose/target before the next tick. The teleport resets direct motion history rather than treating the jump as wheel travel. Turning off VehicleController also releases its direct state.

.. _uvs-input--implementing-an-ai-driver:

Implementing an AI driver
-------------------------

The AI decides **where to go and how much to accelerate, steer and brake**. Send those decisions through ``ExternalController``; the normal engine, gearbox, steering, tires and suspension still move the vehicle. You do not need a separate vehicle simulation or to write directly to wheel torque or the Rigidbody.

.. _uvs-input--1-connect-ai-to-a-vehicle:

1. Connect AI to a vehicle
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Start with a configured wheeled vehicle that already drives correctly with keyboard input. Keep its engine running and use an automatic gearbox for this first example. Direct drive also works; a manual gearbox needs your own shift decisions.
2. Add **External Controller** to the vehicle root. Leave the normal keyboard/action adapter assigned as **Vehicle Controller → Input Source** before starting; the example temporarily takes over and remembers that source.
3. Save the script below as ``AIFollowTarget.cs``, add it to the vehicle and assign **Vehicle**, **Controls** (the External Controller) and **Target** in its Inspector.
4. Put Target on a clear, flat test area ahead of the vehicle. Start with **Cruise Speed Kph = 20** and **Stop Distance = 3**. The vehicle approaches the target and brakes near it. A moving target can be another vehicle or a point updated by your navigation system.
5. Disable ``AIFollowTarget`` to clear its held controls and restore the previous input source. Give each vehicle its own External Controller; do not share one buffer between several AI drivers.

**Example:** ``AIFollowTarget.cs``

.. raw:: html

   <!-- example: AIFollowTarget.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       // Run before VehicleController samples its input in FixedUpdate.
       [DefaultExecutionOrder(-100)]
       public class AIFollowTarget : MonoBehaviour
       {
           public VehicleController vehicle;
           public ExternalController controls;
           public Transform target;
           [Min(1)] public float cruiseSpeedKph = 20;
           [Min(0.1f)] public float stopDistance = 3;
           [Range(1, 90)] public float fullSteeringAtAngle = 45;
           [Min(0.1f)] public float plannedDeceleration = 3;

           private MonoBehaviour previousInput;
           private bool ownsInput;

           private void OnEnable()
           {
               if (!vehicle || !controls || !controls.isActiveAndEnabled) return;
               previousInput = vehicle.inputSource == controls ? null : vehicle.inputSource;
               controls.ClearControls();
               controls.SelectGear(1); // One request on takeover, not a shift every tick.
               vehicle.SetInputSource(controls);
               ownsInput = true;
           }

           private void FixedUpdate()
           {
               // Never take the slot back from a player or another possession system.
               if (!ownsInput || !vehicle || !controls || vehicle.inputSource != controls)
                   return;
               if (!vehicle.isActiveAndEnabled || !controls.isActiveAndEnabled)
               {
                   controls.ClearControls();
                   return;
               }
               if (!target)
               {
                   controls.SetAnalogAxes(0, 0, 1);
                   return;
               }

               Vector3 offset = Vector3.ProjectOnPlane(
                   target.position - vehicle.transform.position, Vector3.up);
               float remaining = Mathf.Max(0, offset.magnitude - stopDistance);
               if (remaining <= 0)
               {
                   controls.SetAnalogAxes(0, 0, 1);
                   return;
               }

               Vector3 forward = Vector3.ProjectOnPlane(vehicle.transform.forward, Vector3.up);
               float angle = Vector3.SignedAngle(forward, offset, Vector3.up);
               float steering = Mathf.Clamp(angle / fullSteeringAtAngle, -1, 1);

               // Slow for a turn and leave room to brake before the stopping radius.
               float turnFactor = Mathf.Lerp(1, 0.25f, Mathf.Abs(steering));
               float cruise = Mathf.Max(1, cruiseSpeedKph) / 3.6f;
               float stoppingSpeed = Mathf.Sqrt(2 * Mathf.Max(0.1f, plannedDeceleration) * remaining);
               float desiredSpeed = Mathf.Min(cruise * turnFactor, stoppingSpeed);
               float error = desiredSpeed - vehicle.ForwardSpeed; // Both in m/s.
               float brake = error < -0.5f ? Mathf.Clamp01(-error / 3) : 0;
               float throttle = brake > 0 ? 0 : Mathf.Clamp01(error / 3);
               controls.SetAnalogAxes(throttle, steering, brake);
           }

           private void OnDisable()
           {
               if (!ownsInput) return;
               if (controls) controls.ClearControls();
               if (vehicle && vehicle.inputSource == controls)
                   vehicle.SetInputSource(previousInput ? previousInput : null);
               ownsInput = false;
           }
       }
   }

``SetAnalogAxes(throttle, steering, brake)`` expects normalized controls: throttle from -1 to 1, steering from -1 (left) to 1 (right), and brake from 0 to 1. This example uses positive throttle and a separate brake, so it only drives forward. It marks the values as analog, preserving partial steering/pedal requests instead of adding keyboard shaping. The engine must already be running; repeatedly calling ``ToggleIgnition()`` would switch it on and off.

**Cruise Speed Kph** is the speed the AI tries to maintain. **Full Steering At Angle** is the heading error that requests full lock: lower values turn more sharply. **Stop Distance** is the stopping radius around the target. **Planned Deceleration**, in m/s², is an estimate used to reduce target speed near the destination, not an extra physical braking force. Lower it to plan braking earlier; actual stopping distance still depends on grip, brakes and slope.

.. _uvs-input--2-drive-through-waypoints:

2. Drive through waypoints
~~~~~~~~~~~~~~~~~~~~~~~~~~

Keep ``AIFollowTarget`` as the driver and change its Target to the next point along a route. Save this second script as ``AIWaypointRoute.cs``, add it to the same vehicle, assign **Driver**, and fill **Points** in route order. Set **Arrival Distance** larger than the driver's Stop Distance (for example 6 m versus 3 m), so the driver changes target before it stops at each point.

**Example:** ``AIWaypointRoute.cs``

.. raw:: html

   <!-- example: AIWaypointRoute.cs -->

.. code-block:: csharp

   using UnityEngine;

   namespace VehicleDocumentationExamples
   {
       // Update the route before AIFollowTarget generates this tick's controls.
       [DefaultExecutionOrder(-200)]
       public class AIWaypointRoute : MonoBehaviour
       {
           public AIFollowTarget driver;
           public Transform[] points;
           [Min(0.1f)] public float arrivalDistance = 6;
           public bool loop = true;
           private int index;

           private void FixedUpdate()
           {
               if (!driver || !driver.isActiveAndEnabled || !driver.vehicle) return;
               if (points == null || points.Length == 0)
               {
                   driver.target = null; // The driver brakes when there is no target.
                   return;
               }
               index = Mathf.Clamp(index, 0, points.Length - 1);
               Transform point = points[index];
               if (!point)
               {
                   driver.target = null; // Fix missing route entries in the Inspector.
                   return;
               }
               Vector3 offset = Vector3.ProjectOnPlane(
                   point.position - driver.vehicle.transform.position, Vector3.up);
               float radius = Mathf.Max(arrivalDistance, driver.stopDistance + 0.5f);
               if (offset.sqrMagnitude <= radius * radius)
               {
                   if (index < points.Length - 1) index++;
                   else if (loop) index = 0;
                   // A non-looping route keeps its final target so the driver stops there.
               }
               driver.target = points[index];
           }
       }
   }

For a moving convoy target, use only the first script and assign the leading vehicle as Target. For patrols, use both scripts and enable Loop. For a one-way delivery route, disable Loop so the vehicle brakes at the last point. Place route points on a drivable path with room for the vehicle's turning radius; these examples do not find roads, avoid obstacles, recover from getting stuck or reverse toward a target behind the vehicle. A navigation/traffic system can perform those decisions and feed its next reachable steering point or its own axes to the same External Controller.

The shipped demo includes ``WaypointAIDemo``, ``DirectWaypointAIDemo`` and ``ExternalControlDemo`` under ``Demo/Scripts``. Press P to compare manual control, physical AI and direct AI on the same checkpoint route. The physical follower smooths steering and uses overspeed braking; the direct follower supplies poses through DirectController. See :ref:`the demo comparison <uvs-demo--compare-physical-and-direct-ai>`. Demo vehicle selection can change Input Source, so coordinate it with your AI ownership instead of having both systems repeatedly take control.

See :ref:`external input ownership <uvs-scripting-input--external-controller-and-runtime-ownership>` for reusable takeover/release logic and :ref:`command sampling <uvs-scripting-input--sampling-contract>` for continuous values and one-shot requests.

.. _uvs-input--reverse-engagement:

Reverse engagement
------------------

Enable **Hold Reverse Until Stopped** on your input source (default off) to brake and reverse with one continuous key hold. For aircraft, also enable :ref:`Allow Ground Reverse <uvs-aircraft--airplanes-and-jets>` and use **Ground Reverse Key** (default Z).

.. _uvs-input--all-command-fields-control-mapping-reference:

All Command fields: control mapping reference
---------------------------------------------

Use this table when implementing ``IVehicleInput.ReadCommand()`` or submitting a complete command to an ``ExternalController``. These are all public data fields of ``Command``. Continuous axes and held buttons must be supplied for every physics sample; one-shot requests must be buffered until read, then reset. A field has an effect only when the active drive profile and configured modules support it.

.. _uvs-input--continuous-axes-and-held-buttons:

Continuous axes and held buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                  | Type / range     | Meaning and mapping                                                                                                                                                                          |
+========================+==================+==============================================================================================================================================================================================+
| ``Throttle``           | ``float``, -1..1 | Signed drive demand: +1 forward, 0 released, -1 backward. Road direction/brake logic decides braking and reverse; aircraft propulsion normally uses 0..1. Example: W minus S.                |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Steering``           | ``float``, -1..1 | -1 left, 0 centred, +1 right. Wheel/rudder/yaw response depends on the profile. Example: D minus A.                                                                                          |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ServiceBrake``       | ``float``, 0..1  | Service brake pedal, released to full braking. Separate from negative throttle and handbrake.                                                                                                |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Clutch``             | ``float``, 0..1  | 0 couples the engine; 1 fully presses/disconnects the clutch. Requires the optional clutch mechanic.                                                                                         |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Handbrake``          | ``bool``         | Hold ``true`` to apply the handbrake/parking-brake request; return ``false`` on release.                                                                                                     |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``HoldReverseRequest`` | ``bool``         | Keep requesting reverse while ``Throttle`` is negative. Set ``true`` for brake-then-reverse with one continuous hold; the drivetrain still checks speed and shift safety. Default ``false``. |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Pitch``              | ``float``, -1..1 | Forward/backward attitude demand: +1 tilts a helicopter forward; for an airplane +1 lowers the nose, -1 raises it. This is normalized input, not degrees.                                    |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Roll``               | ``float``, -1..1 | -1 banks/tilts left, +1 right. Example: D minus A in the helicopter script.                                                                                                                  |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Yaw``                | ``float``, -1..1 | -1 turns the nose left, +1 right. Example: E minus Q. Some profiles combine this with ``Steering``; do not duplicate the same turn demand in both unintentionally.                           |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Lift``               | ``float``, -1..1 | -1 requests downward movement, +1 upward movement in supporting helicopter, hover or submarine profiles. Zero follows that profile's neutral/hold policy.                                    |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Strafe``             | ``float``, -1..1 | -1 requests lateral movement left, +1 right in profiles supporting lateral thrust.                                                                                                           |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Horn``               | ``bool``         | Held horn request; requires a configured horn consumer such as Horn Audio.                                                                                                                   |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Nitro``              | ``bool``         | Held boost request; the optional Nitro module validates availability and applies its settings.                                                                                               |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Burnout``            | ``bool``         | Held Burnout action request; the optional module/profile determines its effect and eligibility.                                                                                              |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``WheelLift``          | ``bool``         | Held wheel-lift request for a supporting vehicle with the optional Wheel Lift module.                                                                                                        |
+------------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-input--one-shot-requests:

One-shot requests
~~~~~~~~~~~~~~~~~

For booleans below, return ``true`` once per press and then ``false``. Return ``Shift = 0``, ``RequestedGear = null`` and ``RequestedIndicators = null`` after consuming those requests. Sending a toggle as a held key can toggle it repeatedly on successive physics ticks. Direct gear selection and relative shifting are alternative requests: send one per sample.

+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                    | Type / values        | Meaning and mapping                                                                                                                                                                     |
+==========================+======================+=========================================================================================================================================================================================+
| ``ToggleIgnition``       | ``bool``             | Switch engine ignition once. Example: I pressed this frame, buffered in Update.                                                                                                         |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ToggleProfile``        | ``bool``             | Request the next registered drive profile, where profile switching is configured.                                                                                                       |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``RequestedGear``        | ``int?``             | ``null``: no request; -1: reverse; 0: neutral; 1 and above: forward gear. The gearbox validates the requested gear and shift conditions.                                                |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Shift``                | ``int``, -1 / 0 / +1 | Request one downshift / no shift / one upshift. Example: Q / E presses.                                                                                                                 |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ToggleTransmission``   | ``bool``             | Switch the configured automatic/manual transmission mode.                                                                                                                               |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ToggleHeadlights``     | ``bool``             | Toggle headlights once through the configured lighting system.                                                                                                                          |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ToggleHighBeams``      | ``bool``             | Toggle the high-beam request once.                                                                                                                                                      |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ToggleHazards``        | ``bool``             | Toggle hazard warning lights once.                                                                                                                                                      |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ToggleLeftIndicator``  | ``bool``             | Toggle the left turn indicator once.                                                                                                                                                    |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ToggleRightIndicator`` | ``bool``             | Toggle the right turn indicator once.                                                                                                                                                   |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``RequestedIndicators``  | ``IndicatorState?``  | ``null``: no request; ``IndicatorState.Off``, ``.Left``, ``.Right`` or ``.Hazard``: select that state directly. Prefer either a direct state or an indicator toggle in the same sample. |
+--------------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-input--channel-metadata:

Channel metadata
~~~~~~~~~~~~~~~~

+---------------------+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field               | Type                    | What to assign                                                                                                                                                                                                    |
+=====================+=========================+===================================================================================================================================================================================================================+
| ``AnalogControls``  | ``InputChannels`` flags | Mark proportional device channels so their values keep analog response. Example: ``InputChannels.Throttle`` combined with ``InputChannels.Steering`` and ``InputChannels.ServiceBrake`` for triggers and a stick. |
+---------------------+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``DigitalControls`` | ``InputChannels`` flags | Mark button-driven axes so supporting mechanics can use digital response/ramping. Example: throttle, steering, brake and clutch in the WASD script.                                                               |
+---------------------+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Available flags are ``None``, ``Throttle``, ``Steering``, ``ServiceBrake``, ``Clutch``, ``Flight`` and ``All``; combine flags with the C# bitwise OR operator. ``Flight`` groups ``Pitch``, ``Roll``, ``Yaw``, ``Lift`` and ``Strafe``. ``All`` combines every group. The ``InputChannels.ServiceBrake`` flag classifies the ``ServiceBrake`` axis. These masks describe the device response, not which mechanics are enabled. If both masks contain a channel, analog takes precedence. Held booleans such as Handbrake and one-shot requests need no channel flag. With neither flag set, that channel has no explicit analog/digital classification.

``new Command(throttle, steering)`` takes only the two main axes. Set additional controls in its object initializer: for example, ``new Command(throttle, steering) { Handbrake = true, ServiceBrake = 0.5f }``. All other fields initially default to zero, false, null or ``InputChannels.None``. ``default(Command)`` releases every axis/button and sends no one-shot requests. Keep held state in your provider and clear only the one-shot fields after reading, as in the examples above.
