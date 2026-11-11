# Entering and exiting vehicles

Use `PassengerAccess` for a character that approaches a seat, coordinates a door, plays entry/exit motion and changes occupancy at the correct point. This page owns the boarding lifecycle. Immediate occupancy is described in [Passengers](Passengers.md); a gesture performed while already seated belongs to [Timed control interactions](ControlInteractions.md).

## Choose the integration level

| Goal | Use | Who owns motion and occupancy? |
| --- | --- | --- |
| Built-in Humanoid boarding with doors | PassengerAccess + HumanoidAccessMotion + SeatAccess + profile | Package coordinates motion, door, reservation and occupancy |
| Your animation/navigation framework, standard boarding lifecycle | PassengerAccess + your AccessMotion subclass + SeatAccess | Your adapter owns motion; package owns reservation, doors and seat handover |
| Customize access admission/coordination | A PassengerAccess subclass and/or SeatAccess subclass | Override public virtual operations deliberately; preserve cleanup and outcome contracts |
| Immediate entry/exit with your own complete sequence | PassengerSeat or vehicle.passengers | Your code owns movement, door timing, exclusivity and cancellation; seat owns occupancy |
| External character framework with no package attachment | CustomPassengerBody + Passenger Seat > Passenger Controller = Custom | Application owns character pose/physics; seat records occupancy and publishes hooks |

The access coordinator requires **Seat Access > Outside**. The built-in humanoid motion additionally requires **Passenger Seat > Spine Anchor** and a valid pelvis. A custom `AccessMotion` owns its own geometry requirements and can use Custom seat ownership without a spine anchor. See [the custom setup steps](Scripting/PassengerAccess.md#tutorial-custom-motion-with-the-built-in-coordinator).

Controller choice and boarding adapter choice are independent. A custom AccessMotion can board an Animator, Animator + IK or Custom character if its body/seat contracts are satisfied. A custom motion adapter must not call TryEnter/TryExit itself when PassengerAccess already owns the operation.

## Tutorial: built-in humanoid boarding

1. Prepare one vehicle with an enabled **Passengers** module and one **Passenger Seat**. Validate immediate entry/exit and the seated fit first, using [Passengers](Passengers.md) and [Seats](Seats.md).
2. For a player who starts outside, disable **Passengers > Spawn On Start** and **Passenger Seat > Spawn On Start**. Keep the player in the scene; do not spawn another driver into their destination. For the demo's initially seated driver, retain the authored startup policy instead.
3. On the character root add **Humanoid Passenger**, **Humanoid IK**, **Humanoid Access Motion** and **Passenger Access**. Use **Humanoid Passenger > Animator / Pelvis / Ik**, then map the IK bones. **Humanoid IK > Match Target Rotation** is above **Auto-fill**. Review auto-filled references rather than assuming every character uses the demo skeleton.
4. Set **Passenger Access > Passenger** to that Humanoid Passenger and **Passenger Access > Motion** to that Humanoid Access Motion. Save these references on the prefab; runtime auto-discovery is a fallback.
5. Add **Seat Access** to the destination seat. Assign **Seat Access > Seat** and, optionally, **Seat Access > Door**. The seat's **Passenger Seat > Spine Anchor** is the seated pelvis endpoint, not the standing feet endpoint.
6. Assign **Seat Access > Per-seat animation and side > Side / Animation Profile / Open Door Animation Profile**. A profile selects clips/controller/timing; Side does not mirror animations. Use separate left/right profiles when required. See [Bind animations](#bind-animations).
7. Create standing and doorway markers outside the character hierarchy. Assign **Seat Access > Per-seat animation and side > Outside / Doorway** below the profiles. Set **Seat Access > Settings > Use Outside Rotation**, ground projection and clearance settings. Use **Seat Access > Select outside marker (move / rotate in Scene view)** below Gizmos to edit the marker.
8. Optionally assign **Humanoid Access Motion > Default Profile** as a fallback. For an Animator/Animator + IK seated pose, assign **Humanoid Access Motion > Seated Pose Controller** to the seated controller. A seat-specific profile takes precedence; the adapter handles initially open doors separately.
9. Prepare the profile's actual clips, states and door markers. Verify playback speed and useful clip ranges before testing alignment. Missing/mistimed markers or an invalid played state can prevent door opening and completion; increasing seat speed limits will not repair that.
10. From your input script call `passengerAccess.TryEnter(seatAccess)`. After seating call `passengerAccess.TryExit()`. A true return admits the sequence; wait for Finish/Cancelled before restoring walking or deciding vehicle possession.
11. Connect **Passenger Access > Signals and callbacks > On Enter Begin / On Exit Begin** to your movement/input lock. Connect **On Enter Finish / On Exit Finish / On Enter Cancelled / On Exit Cancelled** to outcome handling. Check actual `passenger.Seat` in that handling. The seat-side equivalents are under **Seat Access > Signals and callbacks**.
12. Test cancellation, obstructed exit, an already-open door and two characters requesting the same seat before extending the setup. Keep ordinary locomotion and the access adapter from moving the root simultaneously.

Demo manikin prefabs already carry Passenger Access and Humanoid Access Motion with their body/motion/profile references. PassengerAccessDemo retains runtime creation only as a fallback for custom/unconfigured characters; its demo input is not a requirement of the runtime system. Seat/core spawning, player selection, camera/input possession and access animation remain separate responsibilities.

## Inspector paths for access

| Configure | Full Inspector path |
| --- | --- |
| Character and adapter | Passenger Access > Passenger / Motion |
| Character-side lifecycle | Passenger Access > Signals and callbacks > [event] |
| Vehicle seat and door | Seat Access > Seat / Door |
| Side and profiles | Seat Access > Per-seat animation and side > Side / Animation Profile / Open Door Animation Profile |
| Outside/doorway references | Seat Access > Per-seat animation and side > Outside / Doorway |
| Ground, admission, timeout and clearance | Seat Access > Settings > [option] |
| Vehicle-side lifecycle | Seat Access > Signals and callbacks > [event] |
| Select outside marker | Seat Access > Select outside marker (move / rotate in Scene view), below Gizmos |
| Fallback profile and seated controller | Humanoid Access Motion > Default Profile / Seated Pose Controller |

For API definitions and complete custom implementations, continue with [Access scripting](Scripting/PassengerAccess.md#tutorial-custom-motion-with-the-built-in-coordinator).

## Components and prerequisites

| Component | Place it on | Responsibility |
| --- | --- | --- |
| `SeatAccess` | The seat object | Vehicle-side endpoints, door, clearance and admission limits |
| `AccessAnimationProfile` | A project asset assigned to SeatAccess | Clips, Animator bindings, timing and spatial adaptation |
| `PassengerAccess` | The character root beside PassengerBody | Request/reservation and entry/exit state machine |
| `HumanoidAccessMotion` | The character | Built-in Humanoid Animator motion adapter |
| Custom `AccessMotion` | The character, when using another framework | Application-specific playback, movement and completion |

First verify that the character can enter the seat through immediate occupancy and that its seated pose fits. Boarding cannot fix an invalid seat anchor or incompatible body controller. Test your character's ordinary walking/standing animation separately before adapting it to the vehicle.

Use an existing character for player boarding rather than spawning a new driver into the same seat. Disable the seat/core startup spawning policy where automatic occupancy would compete with that player.

## Configure access

### Seat endpoints

1. Add `SeatAccess` on the `PassengerSeat` object and assign **Seat**.
2. Create an **Outside** marker at standing feet level beside the vehicle, clear of its bodywork. Orient it toward the desired standing heading and enable **Seat Access > Settings > Use Outside Rotation** when that heading should be used.
3. Keep the marker under the stationary seat/vehicle hierarchy, not under an animated door or the moving character.
4. Assign **Doorway** if you want a doorway reference/gizmo and **Seat Access > Settings > Standing Offset** for a seat-local correction to the outside position. Do not treat the guide line through markers as a navigation path; actual motion comes from the adapter/profile.
5. Assign the correct animation profile for this seat and side. **Side** is a descriptive label; it does not mirror clips automatically.

**Passenger Seat > Spine Anchor** is the seated pelvis endpoint; **Outside** is a standing feet endpoint. They are not interchangeable coordinate origins. Prepare each for its purpose rather than placing both at the seat Transform.

### Ground projection

With **Seat Access > Settings > Project Outside To Ground** enabled, the outside position can be projected onto suitable support. Configure probe height/distance, allowed rise/drop, minimum ground normal and **Seat Access > Settings > Outside Ground Clearance**. The query ignores the owning vehicle and passenger bodies when finding support.

Use the clearance mask to include actual walkable support. The authored Outside Transform remains unchanged; `OutsidePosition` is the resolved result. Restrict rise/drop to avoid selecting a roof or a different floor. For a fixed indoor boarding platform, disabling projection can be more predictable than probing nearby geometry.

### Admission and clearance

**Seat Access > Settings > Interaction Distance** limits where an entering character can begin relative to Outside. **Seat Access > Settings > Maximum Speed** is vehicle point speed in m/s and **Seat Access > Settings > Maximum Angular Speed** is rad/s. A slowly translating vehicle rotating rapidly can therefore still reject access.

Set **Seat Access > Settings > Clearance Radius**, **Clearance Height** and **Clearance Mask** for the standing character. The destination capsule ignores the occupant, but can be blocked by chassis geometry and obstacles; place Outside clear of the vehicle. During an admitted exit, only that access point's own animated door is excluded from the destination recheck. This is destination clearance, not whole-path navigation.

A compatible enabled seat/core, valid body, empty/unreserved seat for entry and usable outside/animation references are required. A free detached ragdoll is not treated as a walking character ready to board.

### Optional door

Assign a configured `VehicleBodyPart` door or leave Door empty for a doorless vehicle. Set its opening range in the body-part system first, then configure **Seat Access > Settings > Open Door Tolerance**, **Seat Access > Settings > Closed Door Tolerance** and **Seat Access > Settings > Door Timeout** on SeatAccess.

The access system requests door state and waits for readiness; a disabled/released door is unavailable. A door that never reaches its target within tolerance can time out. With the built-in animation profile, door requests come from the clip markers described below. A custom motion adapter can use the ordinary timed door coordination contract.

The operation remembers whether the door was already open. It does not blindly close a door that was open before boarding. Assign **Seat Access > Per-seat animation and side > Open Door Animation Profile** on SeatAccess to use different entry/exit clips when the door starts open; leave it empty to reuse the standard profile. The choice is captured when access begins. Open-door clips can omit the handle-reaching/opening/closing gestures; the door stays open. See [Moving parts](MovingParts.md) for door geometry and operation, rather than rebuilding that setup here.

## Bind animations

### Create a profile asset

Create **UltraVehicleSystem > Passengers > Access Animation Profile** from the Project asset creation menu. Assign it to SeatAccess. Configure:

| Binding | Purpose |
| --- | --- |
| Controller and Layer | Animator controller and numeric layer used by access |
| Standing State / Seated State | Full state paths for the terminal poses |
| Enter State / Exit State | Full state paths playing the access motion |
| Enter Trigger / Exit Trigger | Trigger parameters that start those transitions |
| Standing / Seated / Enter / Exit Clip | Matching Humanoid reference clips for spatial/timing calibration |

The demo profiles reference native `.anim` copies of the existing car entry/exit/idle clips. Their recorded keyframes, root motion, durations and door events are preserved. The original six FBX source assets remain available with animation import disabled, avoiding redundant Humanoid retargeting and its discarded-channel warnings. Edit the referenced native clips when changing playback; importing new source motion requires explicitly updating its native clips and profile/controller references.

Use the full paths from your controller, such as `Base Layer.Enter In`, not a display label copied from a different controller. The built-in adapter expects single-clip access states matching the reference clips. A Blend Tree or a different clip in the played state cannot be assumed to match that calibration.

The four clips must be valid Humanoid clips. Keep their import orientation, position/root settings and the played state's offsets/speed consistent with the references. The Animator owns playback; the reference clips are not a second independent animation player.

### Useful ranges and timing

**Enter Range** and **Exit Range** select normalized useful clip ranges between 0 and 1, with the end strictly after the start. Keep door markers within the used ranges. **Playback Speed** changes access playback timing, **Transition Allowance** accounts for Animator handovers and **Completion Timeout** bounds a clip/state sequence that fails to finish.

**Exit Blend Seconds** blends from the passenger's current seated pose into the exit animation (default **0.2 seconds**, zero disables it). This includes the actual steering-hand pose rather than switching abruptly to the access controller's seated reference. It preserves animated ankle rotation.

**Handover Blend Seconds** adds a short final blend into the seated destination before entry releases control (default **0.2 seconds**, zero disables it). Entry respects the seat's Parent Position/Rotation Offset settings. Keep the Animator transitions smooth as well; this setting controls the final entry handover. Exit uses the Animator's rotation transition into standing; the same duration only softens the final positional support release, without rotating the feet.

Confirm that your Animator can reach both access states and their terminal standing/seated states. A correct trigger name alone does not guarantee a transition is allowed from the current state. Avoid transitions that interrupt access before its required markers/handover.

### Door animation markers

For a door that starts closed, the built-in humanoid adapter requires matching door events in the played entry/exit clips. Doorless seats and doors already open at admission do not require these markers. Repeated or out-of-order markers cannot repeat a door command. Put `AccessOpenDoor` and `AccessCloseDoor` Animation Events at the intended points in both used entry/exit clips. Events must fall in their useful ranges and be delivered from the Animator object actually playing the clips. Its access event receiver is managed by the humanoid adapter.

Optionally place `AccessWaitForOpenDoor` after the open marker and before the character passes through the doorway. It holds the current pose until the physical door reaches Open Door Tolerance; Door Timeout cancels a blocked/too-slow door and releases the reservation. The held time extends the animation completion deadline. Calibration does not execute door markers. The demo uses this marker in closed-door clips.

Do not use `ControlInteractionAnimationEvents` for these markers: that relay commits a seated cockpit action, whereas access events coordinate the boarding door. Test opening, passage and closing against the actual door's travel time; a visually timed marker does not make the physical door move instantaneously.

### Adapt a clip to the cabin

**Horizontal Scale** adjusts motion adaptation across the cabin. **Enter Placement** and **Exit Placement** control how strongly the outside alignment contributes over the clip. **Seat Pose** blends toward the configured seated pose before physical seat handover. Make it reach its final seated weight before handing the character to seat physics.

For an Animator or Animator + IK passenger, set **Humanoid Access Motion > Seated Pose Controller** to the controller used after seating. Entry samples its default seated state, blends into that pose (including steering hands) and restores this controller on seating. Leave it empty for the existing IK/reference target. The CarAnimator example supplies its seated controller through this public field.

Use these after the seat and outside markers are correct. Large adaptation values should not compensate for a clip designed for the opposite side or a very different vehicle. Separate profiles are appropriate for left/right doors or substantially different cabin geometries.

**Use Animator Root Motion** selects the motion source. For clips imported with Root Transform movement baked into pose, leave it off. For clips that export translation/turning as root motion, enable it and disable the corresponding Bake Into Pose import flags. Keep the reference clips identical to the controller motions. **Root Motion Scale** adjusts stride per local axis; **Root Motion Rotation Weight** adjusts turning. Outside/seat anchors and placement curves still align the endpoints. Root trajectory extraction happens once at admission, not as extra physics work each frame.

**Use Foot IK** plants feet independently of root motion; disable it when another system owns foot placement. Automatic detection uses plant height/speed and blend settings. For manual timing, enable **Manual Foot Contacts** and edit the entry/exit curves: X is normalized clip time, Y is contact weight (0 released, 1 planted). Use short ramps and release each foot before lift-off.

Foot-contact settings blend planted standing feet and release them during entry. During the exit-to-idle transition, contact locks fade out even when a manual contact curve ends at one. Foot assistance only adjusts position: ankle rotation follows the animation, including while feet are held in idle. It does not lock ankle orientation or add a final foot-turning correction. **Hold Feet While Idle** can be disabled when the application's locomotion/ground IK owns standing feet. Avoid both systems pulling the same foot to different ground targets.

For import/root-motion details and the adapter contract, read [Access scripting](Scripting/PassengerAccess.md). The SeatAccess Inspector reports binding problems; resolve those before testing player input.

## Request and observe access

Assign PassengerBody and motion on `PassengerAccess`, then call `TryEnter(seatAccess)` on the character. `TryExit()` uses the access configuration of its occupied seat. A true result means the request was admitted and its seat reserved, not that the character is already seated or standing outside.

| State | What to expect |
| --- | --- |
| Idle | No access operation owns the character |
| Opening | Validate/admit and coordinate the doorway; exit can still be blocked |
| Moving | Adapter plays/samples the entry or exit sequence |
| Closing | Motion has handed over; finish the required door state |
| Idle after outcome | Reservation and operation ownership have been released |

During entry, occupancy is committed after successful motion and required door markers. During exit, ordinary occupancy is released before motion, with controlled rollback possible if that exit fails before final commitment. Consequently, an empty seat alone does not prove the character has finished leaving.

Use **Started**, **Completed**, **Cancelled**, `StateChanged` or `Finished` to drive application UI/movement ownership. Disable/reassign your locomotion as part of your integration and restore it on both success and cancellation as appropriate. Do not infer player identity or switch vehicle input authority from the seat's descriptive role.

### Before and after the whole access sequence

`PassengerAccess.BeforeEnter` / `BeforeExit` run after admission and reservation, before collision preparation, door requests and motion. `AfterEnter` / `AfterExit` run only after the whole sequence succeeds, after Target and the reservation are cleared. `Cancelled` carries the same original context for unsuccessful prepared/started operations. These are C# `Action<PassengerSeatContext>` events in addition to the existing Inspector UnityEvents and `Finished`.

The context retains Vehicle, Passenger and Seat after cleanup. It is not necessary to read `PassengerAccess.Target` in an After/Cancelled callback. `BeforeExit` still sees an occupied seat; the seat's own AfterExit occurs earlier, when ownership is released for the movement. A cancelled unfinished exit can reseat the actor and emit seat entry hooks during rollback; an already committed change is not undone automatically.

A request rejected before admission/reservation emits no access callbacks. Calling Cancel from a Before access callback rejects the prepared start and releases the reservation. Recursive Begin requests are rejected while starting or delivering outcome callbacks. See [seat lifecycle hooks](Passengers.md#before-and-after-hooks) for collision preparation and synchronous-callback considerations.

### Cancellation

Call `Cancel()` when the player abandons the request or when your character framework interrupts it. Disabling PassengerAccess also cancels. Changed occupants, unavailable seats/doors, excessive motion and a failed animation/clearance check can cancel too.

Cancellation releases the reservation and adapter state. It may restore only its own ordinary unfinished exit when still safe; it does not undo an external ejection or overwrite a new occupant. An already committed occupancy change is different from a request rejected before motion. Observe the outcome and actual seat/body state rather than always forcing the character to one fixed fallback.

## Test a boarding setup

| Case | What to verify |
| --- | --- |
| Enter/exit stationary | Pose alignment, one occupancy transition and completion |
| Door already open | Correct motion without an unintended final close |
| Door blocked or disabled | Rejection/timeout and released reservation |
| Outside destination obstructed | Exit rejected rather than placing the body inside the obstacle |
| Vehicle accelerates or spins | Admission/continuation limits behave as intended |
| Animation event missing | Clear failure instead of silent successful boarding |
| Cancel during opening/moving/closing | Character/framework ownership and door cleanup are consistent |
| Two characters request one seat | Reservation prevents both entering it |

For navigation, another animation system or more extensive clearance, implement `AccessMotion` rather than adding a second seat state machine. See [API](API/PassengerAccess.md) and [cancellation/extension contracts](Scripting/PassengerAccess.md#cancellation-and-extension).

## Connect events in the Inspector

On the character's **Passenger Access**, expand **Signals and callbacks > On Enter Begin / On Enter In Progress / On Enter Finish / On Enter Cancelled** or the corresponding **On Exit** callback. Press **+**, assign the receiver object and select its method. For progress, select a **Dynamic float** method to receive the changing 0..1 value; a static float entry passes only its configured constant. **Finish** runs after successful motion and required door cleanup; **Cancelled** is the failure/interruption path. Begin can be used to lock application controls, progress to drive a UI indicator, and either outcome to restore controls. Progress reaching one alone does not mean the operation succeeded.

Existing **Passenger Access > Signals and callbacks > Started / Completed / Cancelled** callbacks apply to both directions. Avoid binding the same action to both the generic and directional callback unless it should execute twice. Rejected requests do not start an operation or invoke these callbacks. A reserved attempt vetoed by a Before callback is cancelled even if Begin was not reached.

For a complete C# subscription example, request methods and context properties, see [Handle boarding and leaving from your own code](Scripting/PassengerAccess.md#handle-boarding-and-leaving-from-your-own-code). [Inspector reference](InspectorReference/World.md#passengeraccess) lists all callback and configuration fields.
