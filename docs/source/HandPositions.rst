.. _uvs-handpositions--configure-reusable-hand-positions:

Configure reusable hand positions
=================================

Every ``VehicleHandle`` uses the same **Hands** list. Each named ``HandleHandPosition`` contains independent left/right ``HandleHandPose`` data and five ``HandleFingerPosition`` blocks, stored locally or in a shared ``HandleHandPositionProfile`` asset. The pose contains no character bone or anchor references, so it can be reused on wheels, yokes, sticks, throttles and handlebars. Character calibration supplies bone lengths and neutral bone frames.

.. _uvs-handpositions--configure-a-handle:

Configure a handle
------------------

1. Bind the seat's hands to the handle and assign its palm anchors. Enable **Adaptive Grip** to pose the fingers.
2. Expand **Hands** in the handle Inspector. Wheels start with **Wrapped grip**, **Palm pressure** and **Thumb / index pinch**. Other handles receive defaults for their surface type.
3. Choose **Grip position** for the normal gameplay grip. A wheel also has **Pressure position** and **Pinch position** selectors for its automatic steering gestures.
4. Expand the named entry you want to edit, then its **Left** or **Right** hand. With a shared preset, the headings include the position name and **shared**. Changes affect every handle linked to that asset.
5. Set the hand's **Position** in anchor-local metres and **Rotation** in anchor-local XYZ degrees. These configure the target used by arm IK and physical palm tracking; they do not edit the original anchor or wheel geometry.
6. Configure fingers with the Closure helpers, saved Curl Angles, Surface Fit and extra joint rotations described below. **Advanced pose options** contains finger speed, thumb fitting limits and procedural thumb aiming controls.

The demo's **HandPositions** folder contains shared presets linked from its vehicle prefabs. A handle without saved positions receives local defaults.

.. _uvs-handpositions--closure-helpers-and-auto-apply-closure:

Closure helpers and Auto-apply closure
--------------------------------------

**Auto-apply closure** is enabled by default. For a shared preset it appears directly below the shared-preset information box; for a local position it appears below **Preset**. The setting is saved with the preset or local position and applies to both hands and all their Closure sliders.

+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Auto-apply closure | Changing a Closure slider                                                                                                                                                                                                           |
+====================+=====================================================================================================================================================================================================================================+
| Enabled            | Saves the slider value and writes a starting pose: Curl Angles, zero extra XYZ offsets and Surface Fit = 0 for the affected fingers. The thumb helper also selects Thumb Aim = Surface Fit to disable additional procedural aiming. |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Disabled           | Saves only that slider's helper value. Finger angles, XYZ offsets, Surface Fit, Thumb Aim, axis selections and other Closure values remain unchanged.                                                                               |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Re-enabling the checkbox does not reapply saved helper values. Move a Closure slider to apply it. Manual editing of Curl Angles and Rotation remains available in either mode. The checkbox and helper values are authoring metadata: gameplay does not use them to close fingers or scale a pose.

**Closure (four fingers)** presets Index, Middle, Ring and Little together. It leaves the thumb, its Closure value and its aiming settings untouched. Each finger also has its own **Closure (editor)** slider. The separate **Thumb closure (editor)** slider presets only the thumb.

With auto-apply enabled, Closure scales the following Base/Middle/Tip starting angles from zero to full closure:

========================================== ==== ====== ===
Helper                                     Base Middle Tip
========================================== ==== ====== ===
Four fingers / individual non-thumb finger 85°  110°   80°
Thumb                                      35°  45°    35°
========================================== ==== ====== ===

The resulting angles remain editable. All helper values are saved independently in the preset/asset. Moving the whole-hand helper also updates the four affected finger helper values. Helpers support Undo.

.. _uvs-handpositions--curl-axis-selection:

Curl axis selection
-------------------

The **Curl axis** selector under the whole-hand Closure slider selects ``Default``, ``X``, ``Y`` or ``Z`` for Index, Middle, Ring and Little. Their individual Closure helpers and manual Base/Middle/Tip Curl Angles use that same hand axis. ``Default`` uses each bone's calibrated anatomical flexion axis.

The thumb has an independent **Curl axis** selector under its own Closure slider. Its selected axis belongs to **Base**. Middle and Tip derive their local axes from their saved neutral rotations relative to Base, so differently oriented bones bend about the same hinge direction. ``Default`` uses Base local Z, positive for the left hand and negative for the right. The calculation uses neutral frames rather than the changing rendered pose, preventing axis drift.

Explicit X/Y/Z choices are relative to the saved open bone frame; X retains its sign between hands, while Y and Z mirror. Axis selections are saved with the pose and used in both editor preview and gameplay when evaluating saved curl angles. Changing an axis does not rewrite the saved angles or extra XYZ offsets. **Auto-apply closure** gates only the Closure helpers, not axis evaluation.

.. _uvs-handpositions--fingers-and-thumbs:

Fingers and thumbs
------------------

+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Control                          | Effect                                                                                                                                                                                                                              |
+==================================+=====================================================================================================================================================================================================================================+
| Surface Fit                      | 1 uses the adaptive surface IK fit, 0 uses the authored curl/aim pose, and intermediate values blend the two. Extra XYZ rotations are applied afterwards.                                                                           |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Curl Angles: Base / Middle / Tip | Signed flexion angles in degrees, bounded by anatomical limits. They use the selected Curl axis; thumb Middle/Tip inherit the Base hinge through their neutral frames.                                                              |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Base / Middle / Tip Rotation     | Extra XYZ degree sliders for each segment, applied after curl/IK in that segment's calibrated bone-local frame. These do not use the Curl axis selector.                                                                            |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Thumb Aim                        | Surface Fit adds no procedural base aiming; the Surface Fit weight still determines whether authored curl or fitted geometry is used. Palm Forward and Index Direction aim the thumb base using the index finger and palm geometry. |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Thumb Aim Limit / Inward Angle   | Bound the procedural base aim and optionally turn it towards the wheel centre.                                                                                                                                                      |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Constrain Thumb To Rim           | Adds geometric depth/inward constraints to procedural thumb aiming on a wheel.                                                                                                                                                      |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum Finger Speed             | Limits visible finger rotation speed in Play, in degrees per second.                                                                                                                                                                |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For a wholly authored finger, set **Surface Fit** to zero and edit its Curl Angles and extra XYZ rotations. For an adaptive grasp, use Surface Fit = 1 and add saved XYZ offsets over the fitted pose. These controls do not stretch bones or extend arm reach.

Manually changing a thumb Base/Middle/Tip **Curl Angle** sets its Surface Fit to zero and Thumb Aim to Surface Fit, making the authored curl visible without procedural base aiming. Existing extra XYZ offsets remain. To replace those offsets with a helper-generated pose, enable Auto-apply closure and move the thumb Closure slider.

.. _uvs-handpositions--copy-paste-and-shared-assets:

Copy, paste and shared assets
-----------------------------

Each position, hand and finger foldout has **Copy**, **Paste** and **Paste mirrored**. The clipboard is typed: paste a finger onto a finger, a hand onto a hand or a complete position onto a position. Copies are independent resolved values. **Copy all hand positions / Paste all hand positions** also transfers the list and selected gameplay gesture indices.

**Paste mirrored** uses the same reflection as **Copy to other hand**, with Undo support. It accepts the same typed clipboard as Paste, including copies from another component:

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Destination       | Mirrored result                                                                                                                       |
+===================+=======================================================================================================================================+
| Finger            | Reflects the base, middle and tip extra rotations: X stays unchanged, Y/Z reverse. Curl values and axis selections stay unchanged.    |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Hand              | Reflects anchor-local position X and all extra rotations, including finger rotations. Curl values and axis selections stay unchanged. |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Complete position | Mirrors both hands and swaps left/right, producing independent local data even when copied from a shared preset.                      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------+

The list-level **Paste all hand positions** remains a normal paste. Copying a hand or finger does not change the destination position's Auto Apply Closure setting.

**Copy to left hand / Copy to right hand** mirrors the expanded hand, including shared preset data, with Undo support. Position reflects across anchor-local X; extra XYZ rotations retain X and reverse Y/Z. Curl values and axis choices are retained; the evaluator handles mirrored directions. Custom rigs may still require manual adjustments.

**Save** creates a ``HandleHandPositionProfile`` asset from a local entry and links it. Alternatively use **Create > UltraVehicleSystem > Controls > Hand Position Profile**, **Tools > UltraVehicleSystem > Create Asset > Controls > Hand Position Profile** or **Component > UltraVehicleSystem > Create Asset > Controls > Hand Position Profile**. Assign an asset in **Preset** to edit its left/right data inline.

**Local** detaches the preset and makes an independent editable copy. Copying a complete linked position likewise produces local resolved data. The Auto-apply closure flag, Closure values and axis selections are preserved by whole-position copy, Save and Local. Copying just a hand or finger leaves the destination position's Auto-apply closure setting unchanged.

.. _uvs-handpositions--preview-in-edit-mode:

Preview in Edit Mode
--------------------

Use a scene instance or open the vehicle in Prefab Mode with a pre-placed ``HumanoidPassenger`` assigned to the seat. The preview uses hands already assigned to the handle, or temporarily borrows the preferred supported hand for an action control.

1. In **Hand position preview**, choose **Seat / character**. Action handles automatically use the seat from their action rule. Preview temporarily uses the preferred supported hand, keeping the seat’s home bindings unchanged (for example, the other hand stays on the steering wheel).
2. Choose **Position to preview**.
3. Click **Place hands on anchors and preview**. The editor prepares the hands, solves the wrists onto the configured anchors and then applies the selected finger pose. A wheel's pressure preview includes its pressure wrist contact frame.
4. Enable **Live preview** for automatic refresh. It starts disabled for a new handle. Changes refresh after a 0.25-second quiet period; dragging a slider postpones solving until it is released. Repeated notifications for the same edit do not restart that delay. Shared asset edits and Undo/Redo are also detected.

**Position to preview changes only the displayed pose, not the expanded fields you are editing.** To modify Pressure, expand **Hands → Palm pressure → Left/Right** as well as selecting Palm pressure for preview. Editing Wrapped while previewing Pressure changes Wrapped's saved data, so the displayed hand does not move. The shared Left/Right headings show the edited entry's name. The explicit preview selection and Live preview toggle are remembered per handle for the Editor session, including Inspector recreation.

.. _uvs-handpositions--restore-or-bake-the-mannequin-pose:

Restore or bake the mannequin pose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The two buttons below the preview controls determine what happens to the character transforms:

+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Button                 | Result                                                                                                                                                    |
+========================+===========================================================================================================================================================+
| Restore character pose | Restores the transforms from before the preview and disables Live preview.                                                                                |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bake pose              | Keeps the current preview as the mannequin's authored Transform pose, records prefab instance overrides and disables Live preview. It supports Undo/Redo. |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

Both buttons require an active preview and are disabled during Play. Without baking, closing the Inspector, recompiling or entering Play restores the temporary character pose. After baking, closing the Inspector preserves the baked pose; a later preview uses it as its restore baseline. To continue editing after Bake, enable **Live preview** again or click **Place hands on anchors and preview**. Save the scene or prefab to persist it to disk. Bake does not modify the hand-position preset asset or create an animation clip.

Save handle/preset settings separately when editing their data. Preview is unavailable on persistent Project assets; use a scene or Prefab Mode instance. Check reach and intersections from multiple angles.

Motorcycle handlebars require **Prepare hand grip** after changes to tube geometry or character calibration. This saves the surface fit. Changing saved pose angles does not require preparing that fit again; runtime evaluates the pose over the prepared geometry.

.. _uvs-handpositions--palm-offsets-and-fitting-controls:

Palm offsets and fitting controls
---------------------------------

The pose is the source of palm Position/Rotation, finger speed, thumb fitting/aiming limits, curl angles, Surface Fit and extra XYZ rotations. Character components retain skeleton calibration, palm thickness, surface-fit iteration budgets and physical tracking settings.

A handle keeps the same configured palm target Transform while blending poses, including zero-offset poses. Pose changes update this target rather than rebinding the physical limb. The raw contact frame describes geometry; the configured pose is applied on top. Position/Rotation does not modify the rim or original authored anchors.

.. _uvs-handpositions--public-runtime-api:

Public runtime API
------------------

Use ``HandleHandSide``, ``HandleFinger`` and ``HandleFingerSegment`` for typed access. ``GetHandPosition`` accepts an index or an exact name; ``TryGetHandPosition`` handles missing names without throwing. ``GetHandPose`` and ``GetFingerPosition`` return the actual resolved configuration. A linked preset is shared, so call ``MakeHandPositionLocal`` first when the change should apply to only one handle. ``Copy`` on positions, hand poses or fingers produces independent values.

.. raw:: html

   <!-- example: HandleHandConfigurationExample.cs -->

.. code-block:: csharp

   using UltraVehicleSystem;
   using UnityEngine;

   public sealed class HandleHandConfigurationExample : MonoBehaviour
   {
       public SteeringWheelHandle wheel;

       private void Start()
       {
           wheel.MakeHandPositionLocal(0);
           var thumb = wheel.GetFingerPosition(0, HandleHandSide.Right, HandleFinger.Thumb);
           thumb.surfaceFit = 0;
           thumb.curlAngles = new Vector3(10, 15, 10);
           thumb.SetRotation(HandleFingerSegment.Base, new Vector3(23, 0, 0));
           thumb.SetRotation(HandleFingerSegment.Middle, new Vector3(-13, 0, 0));
           thumb.SetRotation(HandleFingerSegment.Tip, new Vector3(-24, 0, 0));
           wheel.GetHandPose(0, HandleHandSide.Right).maximumFingerSpeed = 300;
       }

       public void SelectRightPose(int index)
       {
           wheel.SetHandPositionOverride(HandleHandSide.Right, index);
       }

       public void ResumeAutomaticRightPose()
       {
           wheel.ClearHandPositionOverride(HandleHandSide.Right);
       }
   }

``SetHandPose`` and ``SetFingerPosition`` replace whole configuration blocks; passing null is rejected. ``SetDefaultHandPosition`` changes the normal grip selector. ``SetHandPositionOverride`` selects pose data for just one hand without pressure/pinch blending; contact geometry, hand ownership and physical contact continue to be controlled by the handle and steering system. ``ResolveHandPositions(HandleHandSide, ...)`` reads the current sources and blend. Strict indexed access and invalid enum values throw ``ArgumentOutOfRangeException``; named lookup throws ``KeyNotFoundException`` when absent. Normal runtime edits are data changes; editor scripts should record Undo/asset dirty state when persisting them.

.. _uvs-handpositions--editorruntime-boundary:

Editor/runtime boundary
-----------------------

Closure helpers, Auto-apply closure, copy/paste, asset creation, preview and Bake are implemented in the Editor assembly. Saved helper values do not drive gameplay. Runtime evaluates saved curl angles, selected axes, extra XYZ rotations and Surface Fit, and blends the selected grip/pressure/pinch configurations. It does not randomly relax fingers or scale their curl by palm distance or physical contact.

Preview uses public per-hand pose selection overrides and restores the prior selections when cleared. Bake releases that temporary selection while keeping the mannequin transforms. Missing palm targets and neutral contact preparation remain runtime responsibilities because gameplay binding also needs them.

.. _uvs-handpositions--steering-wheel-starting-anchors-and-regrip:

Steering wheel starting anchors and regrip
------------------------------------------

**Use Anchor Start Position**, next to **Authored Targets**, makes the assigned raw palm anchors the exact starting and return frames. Regrip carries their captured position/rotation offsets around the rim. It skips Reach Adjustment; Left Angle/Right Angle do not replace those assigned starts. It defaults to false and takes precedence over Authored Targets. With only Authored Targets enabled, targets remain manual. The configured pose offsets and finger settings are applied after the raw frame in every mode, including preview.

The guide hand blends Pinch back to Wrapped using **Palm Return Time**. Its contact also takes up wheel motion smoothly, including a catch beginning exactly at a full-turn boundary. The leading hand transitions between Wrapped and Pressure. These transitions keep the native palm mounts and springs; they do not add limb pose motors. See :doc:`Steering hand grip </SteeringHandGrip>` for the steering workflow.
