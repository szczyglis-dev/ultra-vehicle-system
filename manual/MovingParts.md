# Move a model part

Use this guide for bodywork geometry, doors, hatches, sliding windows and articulated axes. Configure movement first, then add [damage boundaries](Damage.md), [boarding](PassengerAccess.md) or [weapon operation](Weapons.md) where needed. Those systems use the moving parts but do not replace their geometry setup.

## Choose a part component

| Component | Responsibility | Typical use |
| --- | --- | --- |
| `MovingPart` | Procedural rotation/translation, clip playback or custom motion, with rate/target control | Window, slider, turret yaw or barrel elevation |
| `VehicleBodyPart` | Identified open/closed bodywork, four motion modes, optional physical rotation hinge and release state | Door, hood, trunk or hatch |
| `Body` | Vehicle registry and ID-based actions for BodyParts | Open/close a named door from gameplay |
| `DamagePart` | Damage accumulation and detachment boundary | A panel/group that can become debris |

A door can have VehicleBodyPart without collision damage. A fixed panel can have DamagePart without any opening motion. Add both only when both behaviors are needed; one is not a replacement for the other.

## Prepare the model hierarchy

Separate every independently moving group from the fixed chassis. A useful door arrangement is a vehicle root, stationary door-frame geometry and a Door Pivot containing its panel, glass and simple collision proxies. Keep unrelated structural colliders out of that moving group.

Put the pivot at the real hinge where possible. Keep mesh import orientation/scale corrections on child objects. An independent reference anchor must not be the moving Transform or its descendant. Check the whole movement path, not just the open and closed endpoints.

Use one movement owner per Transform. Do not simultaneously assign the same pivot to MovingPart, VehicleBodyPart, an Animator clip and a custom rotation script. A separate recoil/child visual is appropriate when another system needs relative movement beneath an aiming pivot.

## Choose how the part moves

The motion selector offers **Rotation**, **Translation**, **Animation** and **Custom**. Rotation remains the default. `MovingPart` uses **Motion**; `VehicleBodyPart` places **Motion** directly below **Part Type**. Control animators expose **Motion > Mode**; aircraft/landing-gear helpers use **Mode**, and steering visuals use **Motion Mode**. Geometry fields are shown for the selected mode.

| Mode | Pose owner | Progress |
| --- | --- | --- |
| Rotation | UVS procedural axis/pivot motion; VehicleBodyPart may use a physical hinge | Actual procedural travel |
| Translation | UVS procedural travel along the configured frame | Actual procedural travel |
| Animation | An UVS clip player targeting the assigned Animator | Normalized clip position |
| Custom | Your callback, driver, tween, Timeline or external system | Only what your implementation reports |

Animation and Custom do not also apply procedural axis/pivot transforms. Use one pose owner for a given Transform/bone hierarchy. Physical hinge controls on VehicleBodyPart apply to Rotation; its Translation, Animation and Custom modes do not create a hinge.

### Play a transform or skeletal animation

1. Set **Motion** / **Motion > Mode** to **Animation**.
2. Add a dedicated `Animator` at the root matching the animation clip's transform/bone paths. A controller asset is unnecessary. For Humanoid clips assign a compatible valid Humanoid Avatar; generic transform clips need no Humanoid Avatar.
3. Assign **Animation > Animator** and **Animation > Clip** (inside **Motion** on control animators). Use a non-Legacy clip. Keep the animated child/bone paths relative to that Animator root.
4. Author the main clip from the closed/start pose at progress 0 to the open/end pose at progress 1. For signed steering controls, 0 and 1 mean opposite extremes, with neutral at 0.5. For LandingGearPart, 0 means deployed and 1 retracted.
5. Optionally assign **Animation > Closing Clip**. It plays forwards while progress decreases; otherwise the main clip plays backwards. The two clips should have compatible endpoints to avoid a jump when reversing partway through travel.
6. For an independently commanded MovingPart or VehicleBodyPart, **Animation > Duration** sets a full-trip duration; zero uses the selected clip length. Controls already driven by a pedal, switch, steering or landing-gear controller sample the clip at that controller's normalized value and retain its response/transition timing.
7. Use **Clip preview** in Edit Mode to inspect the complete hierarchy, then **Restore preview**. Scene guides show the animation root/bounds, rather than a procedural rotation arc. Selection changes and entering Play Mode restore the preview automatically.
8. Request travel using existing open/close or normalized APIs. A missing/unsupported clip leaves an independently requested operation pending, without claiming successful completion. Stopping/cancelling releases the clip player; disabling/destroying the component also disposes it.

A dedicated Animator prevents an unrelated controller, root-motion system or second clip player from competing for the same bones. The clip player samples absolute time; it does not accumulate animation deltas. A completed animation keeps its endpoint until another request or cleanup.

### Supply your own movement

1. Select **Custom**. Procedural geometry and clip fields disappear.
2. Either assign **Custom Driver** to a component implementing `ICustomPartMotion`, or leave it empty and connect **Signals and callbacks > On Move Requested** to your own method accepting a normalized target.
3. In your implementation, start or retarget your movement when that request arrives. Custom never advances progress or writes transforms itself. Repeated streamed control targets can update an active request without starting a new lifecycle every frame.
4. Connect **On Stop Requested** to stop your tween/animation/task when interrupted. **On Tick** optionally supplies elapsed seconds while a Custom request is active; a driver receives the same tick through `TickMotion`.
5. Call the owner's `ReportProgress(float)` (`ReportMotionProgress(float)` on control animators) as your motion progresses. Call `CompleteCustomMotion()` after reaching the target. Nested helpers also expose `playback.ReportProgress`, `Complete`, `Stop` and `Cancel` directly from code.
6. Use **On End** for successful arrival, **On Cancel** for interruption and **On Stop** for cleanup after any termination. A Stop/Cancel does not fire On End. Do not call Complete as the response to On Stop: the request has already terminated.

MovingPart retains `SetNormalizedPosition` / `StartMotion`, `SetInput` and `Stop` as the request interface. In Custom, signed rate input requests an endpoint and reports input changes; zero stops the request. It does not integrate a position. Control animators still decide when input/contact admits a request; their Custom pose/progress comes from your implementation. See [custom driver example](Scripting/MovingParts.md#custom-motion-driver).

### Lifecycle and Inspector callbacks

At the bottom of the Inspector, existing **Motion Events** (where supported) retain opening/closing/audio bindings, followed by **Signals and callbacks**, then **Gizmos**. The latter exposes mode-appropriate guide toggles. Control-specific events share the callback section with the motion lifecycle.

| Callback | Meaning |
| --- | --- |
| On Begin (float) | Accepted normalized target; may cancel the operation before any pose update |
| On Move Requested (float) | Target request for an external implementation, including retargeting streamed controls |
| On Move (float) | Actual/reported normalized value changed |
| On Input Changed (float) | Signed rate demand changed, where rate input is supported |
| On Tick (float) | Elapsed seconds for active Custom playback |
| On End | Successful completion only |
| On Stop Requested | Stop/cancel an external operation |
| On Cancel | Cancelled, replaced or disabled operation |
| On Stop | Final cleanup after completion, stop or cancellation |

The equivalent C# events live on `PartMotionSignals` (`Began`, `Moved`, `MoveRequested`, `InputChanged`, `TickRequested`, `Ended`, `StopRequested`, `Cancelled`, `Stopped`). Obtain them through `Signals`, a helper's `Signals`, or a control animator's `MotionPlayback.signals`. Unsubscribe when your listener is disabled/destroyed. A callback may stop or replace an operation; the old operation must not overwrite the replacement.

## Configure motion

**Reverse** mirrors rotation or translation around the neutral pose without changing input, normalized progress or opening/closing meaning. Limits remain logical offsets, so a positive-only range can move in either direction. Aiming still follows the requested world target within the mirrored limits. The same setting is available on aircraft motion, handle/anchored motion, propellers and track belts/rollers; steering animators retain their existing **Reverse**/**Invert** controls.

### Rotation with MovingPart

1. Add/register `MovingPart` under the vehicle and assign **Part** to the moving carrier.
2. Set the model to its intended neutral pose before initialization; the helper captures that baseline. Use `CaptureNeutralPose()` in code when deliberately rebasing an already initialized helper at rest.
3. Set **Motion** to Rotation, **Local Axis** to the rotation axis and optional **Anchor** to the independent hinge position and local axis frame.
4. Set **Angle Limits**, **Limit Rotation** and **Speed** in degrees/second.
5. Test both endpoints and the neutral pose before connecting player input.

Local Forward defines the direction used for aiming around the permitted axis. An off-centre mesh can rotate around the configured hinge rather than requiring its imported origin to sit exactly there. Capture the neutral pose before applying gameplay offsets, not repeatedly while the axis is moving.

With Limit Rotation off, the component can keep an unwrapped angle. Shortest-path target selection uses the current angular state; it is useful for a turret but different from forcing a particular number of complete revolutions.

### Translation with MovingPart

Choose Translation, set **Translation Limits** in metres relative to the captured neutral pose and **Translation Speed** in metres/second. Select the direction frame:

| Space | Use |
| --- | --- |
| Part | Travel along Anchor axes when assigned; otherwise along the captured part frame |
| Parent | A slider that follows its parent, such as a window mounted in a moving door |
| World | A fixed world-direction travel axis |
| Anchor | Translation Anchor axes when assigned, otherwise Anchor axes; invalid references fall back to the part frame |

**Translation Direction Angles** rotate the travel axis in that selected frame. Keep the Anchor frame independent of the part. Imported mesh scale is not a reason to interpret metre travel as arbitrary model units; verify motion using the intended real-world distance.

### Example: lower a window along an inclined guide

1. Leave the window in its authored closed pose. Create an empty `Window Guide` beside the moving window under the door, rather than inside the moving window hierarchy.
2. Rotate `Window Guide` until its local Z axis follows the intended rail. The window mesh itself does not need matching import axes.
3. In **Moving Part > Part**, assign the moving window; in **Moving Part > Anchor**, assign `Window Guide`.
4. Set **Moving Part > Motion** to Translation, **Translation Space** to Part, and **Local Axis** to `(0, 0, 1)`.
5. Set **Translation Limits** to the required metre travel, such as `(0, 0.35)`, and **Translation Speed** to the desired metres/second. Use **Reverse** if the guide points in the opposite direction.
6. Inspect the Scene view travel line and both endpoints. They use the same anchor direction and neutral origin as runtime motion. Assigning the direction anchor preserves the window's neutral position and orientation.

For body panels, **Vehicle Body Part > Anchor** optionally replaces the numeric **Hinge Anchor** with an independent hinge transform. **Hinge Axis** is then expressed in that transform's local axes. Both directly animated panels and physical HingeJoint panels use that same point and direction. Leave Anchor empty for the existing mesh-local hinge configuration.

Translation is a constrained axis, not a navigation path or a force-driven hydraulic simulation. Provide suitable collision clearance; the component does not automatically stop at every world obstacle.

## Shape movement speed with curves

Both components expose independent **AnimationCurve** fields:

| Component | Direction curves |
| --- | --- |
| MovingPart | Increasing Motion Curve for higher angle/position targets; Decreasing Motion Curve for lower targets. Applies to rotation and translation, including normalized target commands and ReturnToNeutral. |
| VehicleBodyPart | Opening Motion Curve and Closing Motion Curve. These follow the open/closed request even when Open Angle is negative. |

The horizontal axis is normalized elapsed travel time: 0 starts the movement and 1 finishes it. The vertical axis is normalized travel progress: 0 is the starting pose and 1 is the requested endpoint. The curve's slope controls speed. A straight line from (0,0) to (1,1) gives constant speed and is the default. Flattening the tangent at (1,1) makes the part slow down near the end; flatten both endpoint tangents for a gentle start and stop. Use the Inspector curve editor or assign AnimationCurve values in code.

Speed (degrees/second) or Translation Speed (metres/second) sets the average speed of a complete move. For example, 90 degrees at 90 degrees/second takes one second; changing the curve redistributes that travel within the second, so instantaneous speed can exceed the average. A shorter interrupted movement uses its remaining distance to calculate a new duration. Changing the target or reversing direction starts at the current actual pose. Repeating the same target does not restart its clock.

Curve endpoints are normalized internally. Null/empty curves, equal endpoint values or invalid samples fall back to linear progress. Outputs are bounded to the requested travel and cannot make the part move backward. A flat section can hold position temporarily, but the endpoint is reached when normalized time reaches 1. Speed zero pauses the commanded trajectory until speed becomes positive again.

MovingPart curves apply to fixed-target movement. Continuous SetInput rate commands and AimAt tracking keep their direct speed-limited behavior because they have no fixed travel duration. SetAngle/SetPosition remain immediate; Stop and zero rate input cancel pending target travel.

Animated VehicleBodyPart movement follows the curve directly. For a physical VehicleBodyPart, the curve animates the HingeJoint spring target; Spring, Damper, collisions and load determine the actual angle and arrival time. Speed controls the rate of the physical hinge's spring-target travel. Release ends movement ownership.

## Operate it

Use `vehicle.parts` to access the registered `Body` module directly, just as `vehicle.passengers` resolves the passenger module. The shortcut returns `null` if no Body module is registered and does not add one. It also resolves a disabled Body module for configuration/read access; its operation methods still enforce the module's enabled state. Runtime registration/removal takes effect on the next access.

```csharp
if (vehicle.parts is Body body)
{
    body.Open("LeftDoor");             // Uses VehicleBodyPart > Part Id.
    var door = body.GetPart("LeftDoor");
    var registeredParts = body.parts;   // VehicleBodyPart[] configured on Body > Parts.
}
```

The shortcut returns the controller, rather than an array: `vehicle.parts.Open(...)`, `Close(...)`, `Toggle(...)`, `GetPart(...)`, `OpenAll()` and `CloseAll()` use the same Body API. `vehicle.parts.parts` accesses its configured body-part array; `vehicle.parts.damageParts` accesses its damage-boundary array. These registries do not automatically include every MovingPart or suspension helper. Read `vehicle.parts` once into a local when making several calls.


| API action | Intended control |
| --- | --- |
| `SetInput(-1…1)` | Held rate-control demand |
| `SetTargetAngle` / `SetTargetPosition` | Travel toward a target at the configured speed |
| `SetAngle` / `SetPosition` | Set the corresponding pose immediately |
| `AimAt` | Track a point/Transform around the allowed rotational axis |
| `Stop` | Cancel outstanding rate/target tracking at the current pose |
| `SetMotionEnabled` | Enable/disable model motion without removing its component |

For a hold-button window, combine lower/raise input into one signed demand. Send zero when the button is released; this cancels outstanding travel at the current position. A click-to-open UI instead uses a target endpoint. Do not keep sending zero rate input after issuing a target command, since that also stops it.

Disabling the component stops retained motion; disabling through SetMotionEnabled also clears pending movement. Detached damage debris stops accepting model motion. A visual pause does not reconnect a physically released part.

For a complete UI binding and exact method arguments, see [Moving-part scripting](Scripting/MovingParts.md) and [API](API/MovingParts.md).

## Add a door or hatch

1. Add `VehicleBodyPart` on the independent hinge pivot, with geometry/colliders below it.
2. Set a stable case-sensitive **Part Id** such as `DoorLeft` and the descriptive **Part Type**.
3. Set **Hinge Axis**, optional **Hinge Anchor** offset and signed **Open Angle** relative to the closed pose. Enable **Reverse** to mirror opening, including physical hinge limits and boarding readiness.
4. Add/register `Body` and assign the helper in **Parts**. Use distinct IDs so application actions address the intended part.
5. Start with animated movement, test `Body.Open(id)`/`Close(id)`/`Toggle(id)`, then select a physical hinge if needed.

### Inspector steps for the Body Parts list

1. Outside Play Mode, select the door/panel pivot in the Hierarchy. Choose **Add Component > UltraVehicleSystem > Exterior > Parts > Body Part**. Configure **Part Id**, **Part Type**, **Hinge Axis**, **Hinge Anchor** and **Open Angle** on this component. The panel's geometry and collision shapes should move with this pivot, while the fixed door frame stays on the chassis.
2. Select the vehicle root and open **Vehicle Controller > Modules > Exterior > Body**. If Body is missing, use **Add module...** to add it.
3. Expand **Body > Parts**, press **+**, and drag the pivot's **Body Part** component header into the new element. Repeat for each door, hood or trunk. This is an explicit list: creating a VehicleBodyPart child does not itself add that reference to Body > Parts.
4. Press **Apply vehicle configuration**, save the scene/prefab and test the vehicle's open/close action. In the demo, the vehicle controls show the key for opening/closing doors, hood and trunk. Check motion with **Use Physics** off first; enable it when a simulated hinge is required and tune **Mass**, **Spring** and **Damper** for that panel.
5. If the panel should also dent or detach from impacts, add and register a separate **Damage Part** as described in [Inspector workflow and part registries](Damage.md#inspector-workflow-and-part-registries).

**Body > Parts** accepts VehicleBodyPart and controls opening. **Body > Damage Parts** accepts DamagePart/WheelPart and contributes additional registrations to **Physics > Damage > Parts**. These lists serve different purposes; Body > Damage Parts does not display every damageable part on the vehicle.

In animated mode, Speed and the direction curve control angular travel toward the requested endpoint. In physical mode, Speed and the curve move the spring target while Mass, Spring and Damper determine the actual hinge response. The closed latch constrains the physical hinge near closed; an open request releases that latch so the spring follows its opening target.

Do not judge a physical hinge solely by its speed field: contact/load can change arrival timing. **IsOpen** is the requested open state, while **CurrentAngle** describes actual position. Boarding waits for a door angle tolerance rather than assuming the request means the door is already clear.

Use `Body.SetPhysics(id, bool)` or the helper's corresponding action to select hinge behavior through the supported path. When released, the part is permanently physics-owned for that instance: issuing Open does not reattach it. Debris collision-delay/clearance and reconstruction belong to [Damage](Damage.md).

## Connect other systems

`SeatAccess` references the actual VehicleBodyPart door for opening/readiness during entry/exit; configure its animation markers in [Passenger access](PassengerAccess.md). A cockpit button can call a body action directly or through [ControlInteraction](ControlInteractions.md).

A turret typically uses a MovingPart for yaw and a separate child MovingPart for elevation. `WeaponBarrel` references the elevation helper; its muzzle/effects setup belongs to [Weapons](Weapons.md). This hierarchy keeps aiming and cosmetic recoil from fighting over one Transform.

## Verify and troubleshoot

| Symptom | Check |
| --- | --- |
| Part jumps on first movement | Captured neutral pose, correct Part and reference frame |
| Window drifts after the door rotates | Translation space should follow its parent/anchor as intended |
| Rate movement continues after releasing a button | Send zero on input release and interruption |
| Target never completes | Repeated zero rate input, disabled motion or zero speed |
| Door reports open but still blocks entry | Requested state versus CurrentAngle and physical clearance |
| Hinge jitters | Collider overlap, mass/spring/damping and competing Transform writers |
| Open action no longer works after a crash | Part is released; ordinary motion cannot reconstruct it |

Save the neutral source configuration outside Play Mode and test a fresh prefab instance before integrating damage or boarding.

## Motion events and four audio cues

Both VehicleBodyPart and MovingPart expose **Opening Started**, **Opening Completed**, **Closing Started** and **Closing Completed**. Expand **Motion Events** to assign Inspector callbacks, or subscribe to the component’s matching C# events. Started runs before the operation changes the pose. Completed runs once after actual arrival, never merely because a request was accepted. Reversing, stopping, disabling MovingPart or releasing VehicleBodyPart cancels the interrupted completion. Repeated identical requests do not restart a running operation.

For VehicleBodyPart, Open/Close accepts the operation immediately; even a disabled component can retain a request, but it cannot arrive until it resumes stepping. IsOpen represents the requested endpoint. **IsOpening/IsClosing** describes the pending operation. **Completion Tolerance** is measured in actual hinge degrees (default 1), including physical hinges: a blocked door does not complete merely because its spring target reached the open angle. Negative Open Angle still means opening. Collision-induced swinging does not create opening/closing operations; an explicit Close after impact unlatching can start a closing operation.

For MovingPart, Started runs on the first actual motion step or direction reversal, before applying the new position/rotation. **Increasing Is Opening** maps increasing angle/position to opening; turn it off for mechanisms that open toward decreasing values. Fixed-target operations complete at their requested target, including a partial opening. Rate input completes at a travel limit, not at the small per-frame input target. Aim tracking completes when the current aim target is reached; subsequent target movement may begin another operation. Stop, zero input and immediate SetAngle/SetPosition cancel the operation without start/completion cues. A zero timestep or zero speed pauses movement; a curve’s flat section does not imply completion.

### Opening and closing sounds

Expand **Movement Audio** and assign the four lists:

| Clips | When played |
| --- | --- |
| Opening Clips | Opening Started |
| Opening Completed Clips | Actual opening arrival |
| Closing Clips | Closing Started |
| Closing Completed Clips | Actual closing arrival |

A random valid clip is selected; empty lists are silent and allocate no source. Opening Clips and Closing Clips are start cues. Shared **Enabled**, **Volume**, **Pitch Range**, **Cooldown**, **Output**, **Spatial Blend**, distance, rolloff, Doppler, spread and priority fields configure playback. Start cues share a cooldown to suppress direction chatter; completion cues have independent cooldowns so a short movement can still play its arrival sound. Suppressed cues are dropped, not queued. These are one-shots; continuous motor loops remain separate.

Each event also has an expandable settings group. Enable **Override Settings** there to give that cue its own enable switch, source, **Audio Anchor**, volume, pitch, cooldown, mixer and spatial settings. Shared Enabled remains a master switch. With overrides off, the event uses the common settings.

An explicit **Source** takes precedence. Otherwise an AudioSource already attached to **Audio Anchor** is reused; if none exists, an owned child source is created at that anchor. An empty anchor creates the source under the moving part. Existing sources retain their mixer/spatial configuration; playback changes pitch and applies the one-shot volume. Generated sources are configured by the selected settings and reused. Disabling or releasing the owner stops its generated sources; destruction removes them even when they are attached outside its hierarchy. Existing assigned/anchor sources remain user-owned and are not stopped or destroyed by the part.

Configure movement sounds on a separate **Moving Part Audio** component, with **Motion Source** assigned to the part. Inspector callbacks remain on the mechanism under motionEvents. The receiver exposes movementAudio and typed PartMotionEvent accessors. PlayMotionAudio plays a cue without issuing a movement event; GetMotionAudioSource reads an existing/resolved source without creating one; StopMotionAudio stops owned audio. See [Moving-part scripting](Scripting/MovingParts.md) for a complete example and [API reference](API/MovingParts.md).

### Demo door and hood recordings

The demo car includes opening latch and closing impact sounds for both doors, the hood and the trunk. Reusable mono clips are in `Resources/Audio/Interior/`. `MovingPartAudio.movementAudio.openingClips` plays when opening starts. `closingCompletedClips` plays only when the actual hinge reaches its closed pose, including physics-driven hinges. Closing-start and opening-completion lists are intentionally empty. Replace clips and adjust volume in each Moving Part Audio component's settings.
