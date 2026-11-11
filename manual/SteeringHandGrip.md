# Fit hand grips

This page owns the fit between a character's palm/fingers and a control surface. Start after [seat limb binding](Handles.md#bind-a-limb-to-a-control) can bring the wrist within reach. It does not configure vehicle steering, build the character ragdoll or define an interaction's action timing.

A good fit has three independent parts: correct character finger/palm calibration, correct handle dimensions and a reachable contact pose. Tune them in that order before increasing physical tracking forces.

## Prepare the character's hands

Use a valid Humanoid mapping where possible and review every finger chain. The grip solver needs the actual deforming phalanges in the correct order, not an arm twist bone or an extra metacarpal substituted for the whole finger. For custom mappings, assign the corresponding bones/calibration explicitly.

`HandGrip` represents the palm contact relative to the wrist and saved relaxed/grip finger poses. A compatible `AdaptiveHandGrip` can fit those fingers to a surface. The wrist-bone origin is not usually the palm contact point, so an apparently correct target can still leave the mesh intersecting the rim if palm calibration is wrong.

For the standard setup, assign a pre-placed humanoid to the seat and use the configured handle's seated-grip preview. Supported adaptive binding creates/enables the hand's `AdaptiveHandGrip` and `HandGrip` helpers as needed and calibrates an uncalibrated valid Humanoid from its Animator. Inspect those components on the actual hand bones after preview, rather than adding duplicate solvers to a cabin object. Existing calibration is not automatically replaced merely because a reference changed; intentionally recalibrate/reprepare when replacing the skeleton.

Check both hands independently. Keep positive uniform scale on solving pivots and put mesh-specific import scale on a child where appropriate. A mirrored negative-scale contact frame can reverse approach/curl direction. Complete [anatomical preparation](HumanAnatomy.md) before judging physical wrist limits.

## Steering wheel or yoke

### Describe the surface

1. Add `SteeringWheelHandle` or `YokeHandle` to the animated wheel/yoke pivot.
2. Assign it to the intended seat hands as described in the seat guide.
3. Set **Steering Wheel Handle > Behaviour > Center** and **Steering Wheel Handle > Behaviour > Rim Radius** for the centreline of the ring, not its outside diameter.
4. Set **Steering Wheel Handle > Behaviour > Tube Radius** for half the rim-tube thickness. **Steering Wheel Handle > Behaviour > Tube Depth Radius** allows an oval section; zero uses the circular tube radius.
5. Set **Left Angle** and **Right Angle** for hand contact locations and inspect the approach direction. **Reverse Approach** corrects a backwards-facing pivot.
6. For a flat-bottomed or irregular ring, configure **Steering Wheel Handle > Behaviour > Custom Rim** with at least three centreline samples and appropriate tube radii.

Do not inflate the rim radius to move the fingers outward: that also moves the hand contact around the wheel. Describe the real surface first, then adjust palm/finger calibration if the fit is still wrong.

### Tune fingers and thumbs

Use the handle's universal **Hand Positions** list for independent left/right palm offsets, XYZ joint rotations, saved finger curl angles and surface IK blending. Wheels have separate grip, pressure and pinch configurations; sticks and handlebars use the same data model. Copy/paste a finger, hand or whole position, or link a reusable preset asset. See [Reusable hand positions](HandPositions.md) for the controls, defaults and shared-asset workflow.

### Preview and refine

Use a scene instance or Prefab Mode with a pre-placed **HumanoidPassenger** assigned to the seat. In the handle Inspector's **Hand position preview**, select **Seat / character** and **Position to preview**, then use these controls:

| Control | What it does |
| --- | --- |
| Place hands on anchors and preview | Places the wrists on the configured contacts and applies the selected finger pose once. |
| Live preview | Automatically refreshes after pose edits, selection changes and Undo/Redo. Starts off by default; waits 0.25 s after an edit and until a slider drag ends before solving. |
| Restore character pose | Returns the character transforms to their pre-preview pose and turns Live preview off. |
| Bake pose | Keeps the displayed pose as the mannequin's authored Transform pose, records prefab overrides and turns Live preview off. Supports Undo/Redo; save the scene/prefab to persist it. |

**Position to preview** selects what you see, not which fields you edit. Expand the matching entry under **Hands** to change that pose. Inspect the palm, thumb, finger tips and clearance around spokes from several angles.

Restore and Bake require an active preview and are unavailable in Play Mode. Without baking, closing the Inspector or entering Play restores the temporary pose. After Bake, click **Place hands on anchors and preview** or re-enable **Live preview** to continue; the baked pose becomes the next restore baseline. Bake does not create an animation clip or modify a hand-position preset asset. See [hand position preview](HandPositions.md#preview-in-edit-mode) for the full editing workflow.

Correct wrist reach/target orientation first. Then adjust **Palm Thickness**, finger **Pad Radius** and calibrated contact placement. Finger flexion limits constrain how much a finger can wrap; increasing solver iterations cannot create reach beyond those bounds. The adaptive solver's penetration/contact-gap readings help diagnose fit but do not replace inspection of the visible mesh.

Save intended grip/calibration changes on the reusable character/vehicle prefabs. Recheck after changing the character proportions, wheel geometry or mesh scale. A preview at centred steering does not prove the hand can follow full lock.

Set `steeringWheelRotationAtFullLock` on the vehicle for steering-column travel per side. Road-wheel steering angle remains separate; its [angle conversion contract](Scripting/GripSolving.md#steering-angle-mapping) is useful for custom controls.

## Sticks, throttles and fixed grips

For a joystick, throttle or another cylindrical handle, enable **Steering Wheel Handle > Behaviour > Adaptive Grip**, set **Steering Wheel Handle > Behaviour > Grip Diameter** to the full tube thickness and orient the hand anchor for the desired palm contact. The grip-cylinder axis follows anchor local X; local +Y points from the palm toward the tube centre.

Put moving palm targets under the grip geometry. A joystick's explicit-target/stick-grip arrangement retains explicit left/right contact targets instead of regenerating circular wheel contacts. Configure the handle's contact frame before adding an arm animation; moving a finger solver to compensate for a wrongly oriented target leaves the wrist incorrect.

Use the relevant seated-grip preview where offered. For a fixed rest that should not wrap fingers around a tube, configure a direct relaxed rest in [Handles](Handles.md#hands-grips-rests-and-free-arms), rather than enabling an artificial grip on a flat surface.

## Motorcycle handlebar

### Prepare the geometry

Add `MotorcycleHandle` to the animated handlebar, assign **Left Grip** and **Right Grip** centre Transforms, and configure **Grip Radius** and **Grip Length**. These are tube dimensions; the radius is half its diameter. Local X runs along each grip and +Y points from the palm toward its centre.

Assign the handle to both seat hands and use a pre-placed humanoid for preparation. In its Inspector, run **Prepare hand grip** after fitting geometry/calibration. The editor creates/updates palm contacts and saves the prepared finger pose. Review both sides and save the relevant prefab overrides.

### Runtime and character variants

Motorcycle fitting is an editor preparation operation. Play Mode evaluates the shared Hand Positions configuration over the saved surface fit instead of refitting the cylinder continuously. If the warning says the grip is unprepared, check both grip references, seat/body assignment and the prepared character's hand components.

Prepare each character variant that uses different hand proportions. A vehicle prefab with one prepared character does not automatically create an equally good pose for every unrelated spawned rig. After changing grip radius or character calibration, prepare and save again before testing runtime.

Motorcycle grip fitting is separate from rider head support, pelvis support and hip anatomy. Those are documented in [Seat support](Seats.md#motorcycle-rider-support) and [Human anatomy](HumanAnatomy.md).

## Regrip and hand availability

**Steering Wheel Handle > Grip Mode** selects Both Hands, Left Hand, Right Hand or Released. **Steering Wheel Handle > Behaviour > Allow Hand Regrip** permits repositioning during steering. **Steering Wheel Handle > Behaviour > Vary Grip With Steering** blends the saved pressure pose and rotates the wrist; disable it when you want a continuously wrapped finger appearance.

Where automatic hand regrip is needed, use the handle Inspector's **Add automatic hand regrip** setup for the intended seat and inspect its animator/seat references. Repositioning is useful for large wheel rotations, while a fixed motorcycle grip or stick usually needs a different contact policy.

A hand can temporarily belong to an interaction or rest. Do not fight that ownership with a second script continually reassigning the original grip. Use the [interaction guide](ControlInteractions.md) for temporary transfers and the [handle contract](Scripting/Handles.md#runtime-handover) for deliberate handovers.

With automatic regrip enabled, a hand returning from a switch or handbrake aims for its preferred side grip in the unturned wheel plane, adjusted for safe separation from the other hand. It does not resume the old wheel-material contact. The returning palm lands with a wrapped grip. The substitute retains steering leadership and pressure after the return by default. The private `switchLeadershipAfterControllerReturn` flag (default `false`) optionally restores steering roles after the returning palm has rebound to the wheel and regained support; a substitute still at its lower stop then resumes the supporting pinch.

Automatic gearbox paddle gestures do not borrow the leading steering hand while the visible wheel is turned at least 90 degrees. This prevents braking downshifts from unexpectedly swapping steering roles. Explicit paddle presses and command-requested shifts remain eligible; mechanical gear selection proceeds normally.

## Physical tracking versus finger appearance

Handle **Position Spring/Damper**, maximum palm force, angular support and arm support affect how a dynamic hand/arm follows the target. Finger curl and surface geometry affect appearance around that contact. Increasing physical force does not remove a finger mesh intersection caused by incorrect diameter or palm thickness.

Conversely, perfectly fitted fingers can still lag behind the control if physical support is too weak or the target is outside reach. Verify target position, anatomy and contact availability before changing spring strength. Nonphysical Animator + IK and physical ragdolls have different pose ownership; tune the controller you actually use.

## Regrip and troubleshooting

| Symptom | Check |
| --- | --- |
| Entire hand cannot reach | Seat/target distance and arm anatomy, before finger settings |
| Palm lies inside the wheel | Contact calibration, rim/tube dimensions and palm thickness |
| Fingers curl away from the grip | Bone order, curl axes, left/right mapping and target orientation |
| Thumb looks wrong only after a handle change | Animate Thumb policy and saved/custom thumb pose |
| Hand floats but fingers wrap plausibly | Wrist-to-palm frame, not just curl strength |
| One hand fits and the other does not | Separate target orientation/mapping and negative scale |
| Wheel fits at centre but fails at lock | Full-lock travel, regrip availability and anatomical wrist range |
| Motorcycle runtime pose differs from preview | Unsaved preparation or a different spawned character variant |
| Hand trembles between poses | Competing pose writers or overconstrained physical reach |

For fitting algorithms, diagnostics and custom surfaces, see [Grip scripting](Scripting/GripSolving.md). For field-by-field definitions, use the [Inspector reference](InspectorReference.md).

## Vibration while holding full steering lock

Check that palm targets are reachable and that shoulder, torso and hand supports are not pulling against one another. Test repeated full-left/full-right turns from rest and while driving. Inspect the resolved hand target, including saved hand-position offsets, rather than only the raw wheel anchor.

Tune contact geometry and the seated pose before increasing stiffness or solver iterations. Re-enter the seat or restart Play after structural seating changes. For timestep and native constraint accuracy, see [seated recovery](Seats.md#seated-recovery-without-pose-resets).

### Repeated turns and hand reach sectors

Automatic regrip keeps moving palms within their column-space reach sectors using **Left Rest Angle**, **Right Rest Angle** and **Minimum Hand Separation**. At a reach limit, the palm can slip relative to the rim instead of crossing into the other hand's sector. **Palm Return Time** controls the guide hand's return trajectory and its transition from Pinch to Wrapped.

Temporary controls return the hand to its saved contact on the rotating rim, subject to reach and separation limits. See [smooth return to a wheel contact](Handles.md#smooth-return-to-a-wheel-contact) for return and finger-blend behavior. Fixed joystick targets use their authored contact policy.
