.. _uvs-lights--vehicle-lighting:

Vehicle lighting
================

``Lights`` owns independent headlight, high-beam, tail, brake, reverse and indicator channels, plus named custom groups. Each channel can control road illumination, emissive lenses and separate lens halos. Configure these outputs here; physical stalks, cockpit switches and gesture timing belong to :doc:`Interior controls </InteriorControls>`.

Lamp appearance and output assignments are applied on configuration/state changes. After changing them in Play Mode, call ``Lights.RefreshLightingConfiguration()`` once; beam, brake, reverse and indicator actions remain live. See :ref:`runtime appearance changes <uvs-scripting-lights--changing-lamp-appearance>`.

.. _uvs-lights--inspector-quick-start-add-one-headlight-pair:

Inspector quick start: add one headlight pair
---------------------------------------------

1. Outside Play Mode, select the vehicle root and open **Vehicle Controller > Modules > Exterior**. Expand **Lights**, or use **Add module...** to add it. Work on this module rather than adding another Lights controller for each bulb.
2. In the Hierarchy, create a Unity **Light** child at each headlight position. Choose a suitable light type (normally Spot for a forward beam), aim it down the road, and fit its range/spot angle. Keep these children with the corresponding bodywork if it moves.
3. Back in **Lights**, expand **Headlights**. Expand its **Lights** array, press **+** twice, and drag the two Unity Light components into the slots. Enable the channel and set its **Color** and **Intensity**.
4. If the lens should glow, expand **Lenses**, add the appropriate lens Renderers and set **Emission**. Enable emission in the assigned lens material/shader as required. A Renderer reference is the visible lens; a Light reference is the actual illumination source.
5. For a visible halo, open the **Lights** component menu and choose **Add lamp glows**. This creates and connects the saved **Lens glow** children. Adjust each child's **Vehicle Lamp Glow > Radius** and **Brightness**; its local Z axis points out of the lamp. The halo does not illuminate the road or need bloom.
6. Configure **High Beams**, **Brake Lights**, **Reverse Lights** and the left/right indicator channels in the same way using their own outputs. Assign the vehicle's Engine for automatic reverse behavior where required; leave unused output lists empty.
7. Press **Apply vehicle configuration** and save the scene/prefab. Enter Play Mode and use the lighting buttons in **Vehicle Controller > Live**, or the vehicle's configured light input, to test low beams, high beams and indicators. Brake/reverse channels should also respond to the actual mechanics.
8. For a roof beacon, add an entry in **Custom Lights**, assign its outputs, set a unique **Id**, enable **On** and optionally **Blinking**. Check its authored initial request in Play Mode before adding an application toggle.

For the shared add/reference/save workflow, see :ref:`Basic Inspector workflow <uvs-inspectorconfiguration--basic-inspector-workflow>`. Continue below for automatic states, channel sharing and material requirements.

.. _uvs-lights--configure-channels:

Configure channels
------------------

1. Add/register Lights on the vehicle and assign Engine where automatic reverse behavior needs it.
2. Separate independently controlled lens geometry into independently addressable Renderers. Create/position actual Light components for illumination where needed.
3. Assign the relevant **Lights** and **Lenses** arrays on each channel.
4. Set channel **Enabled**, Color, Intensity and Emission. Intensity controls physical Light output; Emission controls the lens shader value.
5. Configure automatic brake/reverse behavior and the indicator Blink Interval.
6. Test each channel separately from the intended camera at day/night exposure, then connect the input actions.

The demo reserves strong illumination for low/high beams. Tail, brake, reverse and indicator lamps use emissive lenses and directional halos with weak, short-range illumination. Tune **Lights > [channel] > Intensity** for the environment and the connected **Vehicle Lamp Glow > Brightness** for the visible lamp. The halo follows the channel and is depth-tested against the scene.

A physical Light can illuminate the road without making the lens material glow. An emissive lens can look lit without casting light onto the road. Use both where the model needs both; a distant small marker may need only emission.

.. _uvs-lights--lens-materials-and-shared-output:

Lens materials and shared output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The channel writes ``_EmissionColor`` through a Renderer property block. Use a shader/material that reads that property and enable any emission feature/keyword required by that shader. Bloom/exposure is a render-pipeline setting, not another lighting channel.

A property-block emission write applies to its assigned Renderer. Separate lenses when they need independent states. Assigning the same Light/Renderer to conflicting channels lets the last applied output win; it does not combine independent stop/tail signals automatically.

The module manages its assigned Light color/intensity/enabled state. Edit the channel settings rather than a live Light value that the next output refresh will replace. Fit each Light's beam geometry, range and shadow policy separately for the render pipeline/hardware.

.. _uvs-lights--control-lighting:

Control lighting
----------------

+---------------------------------------------------------+------------------------------------------------------------------+
| Action                                                  | Role                                                             |
+=========================================================+==================================================================+
| SetBeamMode                                             | Select Off, Low or High beam request                             |
+---------------------------------------------------------+------------------------------------------------------------------+
| SetHeadlights / SetHighBeams                            | Convenience beam actions                                         |
+---------------------------------------------------------+------------------------------------------------------------------+
| SetIndicators                                           | Off, Left, Right or Hazard                                       |
+---------------------------------------------------------+------------------------------------------------------------------+
| SetHazards                                              | Explicit hazard request                                          |
+---------------------------------------------------------+------------------------------------------------------------------+
| SetChannelEnabled                                       | Availability of a built-in channel, independently of its request |
+---------------------------------------------------------+------------------------------------------------------------------+
| SetBrakeOverride / SetReverseOverride / SetTailOverride | Explicit state or null to return to automatic behavior           |
+---------------------------------------------------------+------------------------------------------------------------------+

Tail lights normally follow the requested beam state. Brake lights follow resolved service-brake demand above **Brake Light Threshold** when automatic response is enabled; **Handbrake Activates Brake Lights** adds that policy. Reverse lights follow the appropriate selected-gear/direct-drive mechanics rather than a visual lever animation.

Overrides are useful for scripted sequences, but restore automatic ownership with ``null`` when the sequence ends. A false override forces off; it does not mean “automatic”. Channel availability can also keep a requested lamp dark, for example after application-controlled damage.

The controller's Live view calls public actions too. Use the :doc:`input guide </Input>` for keyboard/actions and the :ref:`switch binding guide <uvs-interiorcontrols--indicator-stalk>` for a physical stalk. Avoid two input listeners both toggling the same channel on one button press.

.. _uvs-lights--requested-state-and-actual-illumination:

Requested state and actual illumination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beam/indicator state records what was requested. ``LightChannel.IsLit`` and ``LitChanged`` report the applied channel output, including availability. A hazard request alternates both indicator channels on the shared phase; a dark half-cycle is not another off request.

``BeamModeChanged``, ``IndicatorsChanged`` and ``IndicatorPhaseChanged`` serve different purposes. Use request changes for UI/logic and phase changes for timed relay feedback. Do not trigger an expensive gameplay operation on every blink merely because the lamp toggled visually.

.. _uvs-lights--custom-lights:

Custom lights
-------------

1. Expand **Custom Lights**, add an entry and give it a unique nonblank case-sensitive **Id**, such as ``roof`` or ``WorkRear``.
2. Assign its physical Lights and optional Lenses. A group can contain one source or several.
3. Set Color, Intensity, Emission and Enabled, then **On** for its initial request.
4. Enable **Blinking** and set **Blink Interval** for a beacon/warning group. Each custom group has its own blink clock.
5. Test the custom ID action independently from beam/indicator input.

These groups do not automatically follow the main beams or brake state. Use ``SetCustomLight``, ``ToggleCustomLight``, ``SetCustomLightEnabled`` or ``SetAllCustomLights``. A disabled group/module retains its custom request while remaining dark. ``GetCustomLight(id)`` exposes configuration and applied IsLit.

For runtime membership use ``RegisterCustomLight``/``UnregisterCustomLight``; invalid/duplicate IDs are rejected. ``RefreshCustomLights()`` applies changed group parameters immediately. This example creates one runtime work-light group; the ordinary Inspector workflow needs no script.

**Example:** ``CustomWorkLights.cs``

.. raw:: html

   <!-- example: CustomWorkLights.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CustomWorkLights : MonoBehaviour
       {
           public Lights vehicleLights;
           public Light workLamp;
           public bool Register()
           {
               return vehicleLights && workLamp && vehicleLights.RegisterCustomLight(new CustomLightGroup {
                   id = "WorkRear", lights = new[] { workLamp }, color = Color.white, intensity = 5
               });
           }
           public void TurnOn() { if (vehicleLights) vehicleLights.SetCustomLight("WorkRear", true); }
           public void TurnOff() { if (vehicleLights) vehicleLights.SetCustomLight("WorkRear", false); }
       }
   }

.. _uvs-lights--indicator-sound:

Indicator sound
---------------

Install ``Audio`` and its ``IndicatorAudio`` channel on the same GameObject, assign Lights and configure relay volume/spatial/mixer settings. Use generated relay clicks or assign Tick On/Tick Off. Disable **Use Default Clicks** when missing clips should be silent.

The channel follows indicator phase; do not also replay a click from your input handler unless that additional sound is intentional. Other audio-channel setup is centralized in :doc:`Audio </Audio>`.

.. _uvs-lights--damage-and-application-policies:

Damage and application policies
-------------------------------

Use the damage system's accepted events to change channel availability or custom requests according to your game rules. Material classification alone does not decide that a headlight is broken. Repair must restore the requested application state explicitly; restoring mesh shape is not the same operation.

For custom renderer backends or exact event timing, see :doc:`Lighting scripting </Scripting/Lights>` and :doc:`API </API/Lights>`.

.. _uvs-lights--diagnose-lighting:

Diagnose lighting
-----------------

+-----------------------------------+-----------------------------------------------------------+
| Symptom                           | Check                                                     |
+===================================+===========================================================+
| Road is lit but lens is black     | Lens assignment, shader emission support and Emission     |
+-----------------------------------+-----------------------------------------------------------+
| Lens glows but casts no light     | Physical Light assignment and its range/beam              |
+-----------------------------------+-----------------------------------------------------------+
| Light edits are reverted          | The channel owns those assigned Light values              |
+-----------------------------------+-----------------------------------------------------------+
| Brake/reverse lamp stays forced   | Explicit nullable override not restored to null           |
+-----------------------------------+-----------------------------------------------------------+
| Two lenses always change together | Shared Renderer/channel assignments                       |
+-----------------------------------+-----------------------------------------------------------+
| Custom beacon does not toggle     | Exact ID, group/module availability and output references |
+-----------------------------------+-----------------------------------------------------------+
| Indicator click doubles           | Duplicate phase/input sound listeners                     |
+-----------------------------------+-----------------------------------------------------------+
