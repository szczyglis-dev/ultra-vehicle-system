# Timed control interactions

Use `ControlInteraction` to coordinate one gameplay action with an optional character gesture. This page owns action admission, hand transfer, Animator timing, completion and cancellation. Build the physical control and its mechanic binding in [Interior controls](InteriorControls.md) first; assign the seat's ordinary limb targets in [Seats](Seats.md).

For custom Animator/Timeline gestures, independent arm/finger weights and common contact/value events, follow [Custom handle animation and IK](HandleAnimation.md).

## Inspector quick start: wire a UI action

1. Build a working control and its binding first, such as a wiper switch that actually operates Wipers. Select its control/helper object and add **Control Interaction** through Unity's Add Component search.
2. Choose the immediate mode for the first test. Expand **Control Interaction > On Commit**, press **+**, drag the target control/binding into the object slot and select the intended compatible action from Unity's function menu.
3. On your UI Button's **On Click**, add the ControlInteraction component and select **Begin()**. Keep the same gameplay action out of On Click itself when On Commit already runs it, or it will happen twice.
4. Apply/save the vehicle setup as needed and test one click in Play Mode. Then select IK/Animator presentation and assign Seat, target handle, motion/animation requirements using the sections below.
5. Test a rejected request and cancellation too. Adding the component does not create mouse picking or a world-space interaction prompt; supply that UI/input path in the application.

## Configure the action

1. Confirm that the underlying action works directly: for example, calling the wiper switch's Toggle changes the wiper request.
2. Add `ControlInteraction` to a cockpit helper or the control object.
3. Select the presentation mode and supply its prerequisites below.
4. Put the gameplay action in **Control Interaction > On Commit**, or pass it as the callback to `TryBegin`. Use one path for the same action.
5. Connect your UI/input/raycast selection to `Begin`, then test a successful action, a rejected start and cancellation.

The component does not provide mouse picking, keyboard bindings or automatic nearest-control selection. Those belong to the application input layer. A UI Button can call the void `Begin()` entry point without a custom script.

## ControlInteraction modes

Add `ControlInteraction` beside the control or on a cockpit interaction object. Its **Control Interaction > On Commit** UnityEvent is the point at which the actual action should happen.

| Mode | Setup | Commit and completion |
| --- | --- | --- |
| Immediate | No occupied seat required | Begin commits and completes immediately |
| IK | Occupied enabled Seat, LeftHand/RightHand, target `VehicleHandle`, available limb admitted by `vehicle.handles` | Arrival commits; the controller's return completes the interaction |
| Animator | Occupied Seat, a valid Animator/controller and Trigger | Timings or Animation Events commit and complete |
| IK then Animator | Animator + IK or physical humanoid seat, available IK hand, target handle and valid Animator Trigger | IK reaches first; the clip commits; completion starts the IK return; On Completed fires after returning |
| Custom | Occupied Seat and an enabled component implementing `IControlInteractionDriver` | Custom driver owns request commit/completion |

Non-immediate interactions require an occupant and an enabled target that allows the selected hand. They reserve the hand through `vehicle.handles`; a Custom driver receives the ownership token in `request.Use`. The driver controls presentation/commit timing, and the controller restores the home binding when the interaction ends. **Hand** must be LeftHand or RightHand. The target is a handle component, not the moving mesh or neutral motion anchor. **On Started**, **On Completed** and **On Cancelled** can drive UI feedback; keep the gameplay action at **Control Interaction > On Commit**.

`Begin()` is a void entry point for UnityEvents. Code can use `TryBegin()` to learn whether the interaction started. A false result means no action started, for example because the interaction/transfer is busy or references are missing. Starting another action does not queue it automatically.

## Example: reach for the wiper switch

1. First configure the `SwitchAnimator` and `WiperSwitchBinding` and verify that calling Toggle controls the wipers.
2. Add SwitchHandle, parent its Anchor under the moving lever and orient it for the driver's hand. Assign it to SwitchAnimator.Handle.
3. On the SwitchHandle contact, assign a unique ID and allow the intended hand. Configure **Switch Handle > Actions > Release Duration / Outbound Duration / Return Duration / Return Delay**.
4. Add `ControlInteraction`, set **Mode** to IK, assign the driver's **Seat**, **Hand**, SwitchHandle **Target**.
5. Ensure that hand currently has a valid controlled handle/anchor in the seat configuration; the transfer needs an existing source pose and a valid destination.
6. Add `SwitchAnimator.Toggle` to the interaction's **Control Interaction > On Commit** event.
7. Connect a UI Button or your cockpit-selection code to `ControlInteraction.Begin`.
8. Test with an occupant: the hand releases its regular contact, reaches the switch, commits the action, waits briefly and returns.

Tune **Release Duration**, **[Handle component] > Actions > Outbound Duration** and **Return Delay** on the destination handle's **Actions** settings. Tune the switch's Transition Duration independently. Vehicle Handles advances the request in the vehicle Feedback phase. Several controls may use different limbs concurrently; the same limb has one owner.

## Animator-driven interaction

Choose Animator mode when a clip should own the gesture. Assign the seat, hand and target handle, and either an explicit Animator or let the interaction use the humanoid occupant's `SeatedAnimator`. The Animator must have a runtime controller and contain the configured Trigger parameter. A physical humanoid prepares its isolated seated Animator when the hand is acquired; its source Animator may remain disabled so it does not overwrite the ragdoll torso.

With **Animation Events** off, **Commit Time** commits the action and **Duration** finishes it, in seconds since the interaction started. Choose values matching the clip; completion is not earlier than commit. The interaction temporarily gives that hand to Animator mode and restores its saved ownership on cleanup when that binding is still unchanged.

**Animation Layer** blends a gesture over the underlying pose. **Animation Enter Blend** and **Animation Return Blend** control its fades; zero makes that direction immediate. The hand stays reserved through the return fade. In IK then Animator mode, the layer fades out before IK return begins; IK travel uses the destination handle's duration settings. Disable, damage or invalid bindings cancel immediately.

With **Animation Events** on, add `ControlInteractionAnimationEvents` on the GameObject receiving the clip events, assign its **Interaction**, and put `CommitAnimation` at the contact frame and `CompleteAnimation` at the end of the gesture. `CancelInteraction` is available for cancellation. For reusable characters, bind the receiver to the current vehicle/seat interaction when changing occupants. Put this relay on the source Animator before starting physical limb animation: the isolated ragdoll animation rig forwards its clip events to the same live receiver. It does not copy arbitrary scripts or component animation curves.

**Timeout** cancels an unfinished request, including a clip missing its completion event; zero disables this timeout. Occupant changes, disabled targets or an interrupted hand ownership can also cancel. Cancellation after commit does not undo a vehicle action that has already happened.

## Inspector: reach with IK, then animate a switch gesture

1. Use **Animator + IK** or **Ragdoll Physics** on the seat. Keep the selected hand in **IK Handle** with a valid home handle/anchor. A plain **Animator** seat can also solve the requested limb when the target handle uses **Control Mode > IK / Animator + IK**, or an explicit temporary IK request is used.
2. On **Control Interaction**, select **IK then Animator** and assign **Seat**, **Hand** and the switch's **Target** handle. Fit the target to a reachable position. Configure its **Use** release, travel and return durations.
3. Prepare a Trigger-driven gesture in the passenger's Animator Controller. Mask its layer to the intended arm/fingers so animation leaves the rest of the character alone. Fit the clip's initial/final hand pose to the switch contact; the package does not retarget an arbitrary clip to a new switch position.
4. Assign **Trigger**. Leave **Animator** empty for the humanoid's built-in seated animation source, including a physical ragdoll. Choose timed **Commit Time / Duration**, or configure the relay and **Animation Events** above. Timed gesture durations start after IK arrival, rather than counting the reach.
5. Wire the vehicle action once in **Control Interaction > On Commit**. The hand reaches without committing, changes to Animator ownership for the gesture, then returns through IK. **On Completed** runs after the return. **Timeout** covers the complete sequence, including travel.
6. Test cancellation, a moving vehicle, reset and controller handover. Cancellation releases the token and restores its saved binding; an external replacement binding/mode is preserved. Changing the passenger controller cancels active handle uses. Changing/disabling the gesture Animator/controller also cancels the interaction.

With **Keep Hand On Target While Animating** enabled, use a layer masked to fingers only. IK or the existing physical wrist support keeps the palm on the switch throughout the clip; Animator supplies finger motion. This avoids handing the whole arm to a contact pose authored for a different torso position. The hand returns through IK after the gesture. The option is captured when the request starts and is released on return or cancellation. It is off by default.

Without that option, a physical seated passenger keeps a simulated torso while the animated limb is temporarily kinematic. After the gesture, that limb resumes its original physical/IK settings. This path adds no extra physics queries or simulation steps. Use one clip-event interaction per receiving Animator; an untagged Animation Event addresses the currently bound interaction, so stop/transition old clips before rebinding the relay to another request. For asynchronous callbacks, retain the `ControlInteractionRequest` instead.

## Select gesture animations at runtime

`ControlInteraction.mode`, `trigger`, `animationLayer`, `animationLayerWeight` and `keepHandOnTargetWhileAnimating` are public script settings. When `IsBusy` is false, choose them for the current `PassengerSeat.ActiveController`, then call `TryBegin()`. Animator Controller trigger transitions select the clips; replacing the whole controller is unnecessary.

| Passenger mode | Interaction mode | Clip | Keep Hand On Target While Animating |
| --- | --- | --- | --- |
| Animator | `Animator` | Complete reach, press and return | Off |
| Animator + IK or Ragdoll Physics | `IKThenAnimator` | Press only; finger-only layer | On |

Set **Animation Layer** and **Animation Layer Weight** in the Inspector, or call `TrySetAnimationLayer("LeftContact")` / `TrySetAnimationLayer(4)` while idle. `TrySetAnimationLayer(-1)` clears the override. Missing layers are rejected before a gesture begins. The request captures its layer and weight, then restores the previous weight on completion or cancellation; an external weight change is preserved.

CarAnimator has separate `LeftSwitch`, `RightSwitch`, `Wave`, `LeftContact` and `RightContact` layers above its base steering layer. The contact masks enable only the appropriate fingers. Its public layer setter selects the matching variant before each interaction.

CarAnimator uses `LeftSwitch` / `RightSwitch` for complete gestures and `LeftSwitchContact` / `RightSwitchContact` for contact-only gestures. The handle Animator controller settings select triggers for built-in modes; the Custom demo path selects them from its script. The latter clips have no arm reach or return: the target handle owns those movements. Put commit/completion events on both clip variants. Changing the seat controller cancels the current interaction before another variant starts.

For lower-level handle integration, `HandleUse.BeginAnimation(true)` retains the held hand's IK/physical support and plays animated fingers. The existing parameterless method retains whole-limb animation behaviour. Both paths restore finger ownership on return/cancellation.

## Code-driven actions without duplicate execution

Use either **Control Interaction > On Commit** for the action or supply a callback to `TryBegin`. If the same action is connected through both, both will execute. The example below provides two parameterless methods for UI Buttons. It also supplies Left/Centre/Right methods for a three-position stalk, whose enum argument is easier to wrap than to configure on an ordinary Button.

**Example: `CockpitInteractionButtons.cs`**

<!-- example: CockpitInteractionButtons.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class CockpitInteractionButtons : MonoBehaviour
    {
        public ControlInteraction interaction;
        public SwitchAnimator binarySwitch;
        public SwitchAnimator indicatorStalk;

        // Use without a hand gesture. The binding sends the state to its mechanic.
        public void ToggleDirectly()
        {
            if (binarySwitch) binarySwitch.Toggle();
        }

        // Leave interaction.OnCommit empty when this callback owns the same action.
        public void ToggleWithGesture()
        {
            if (!interaction || !binarySwitch) return;
            interaction.TryBegin(() =>
            {
                if (binarySwitch) binarySwitch.Toggle();
            });
        }

        // Configure the stalk as three-position, with Negative meaning left.
        public void Left() { SetStalk(SwitchPosition.Negative); }
        public void Centre() { SetStalk(SwitchPosition.Neutral); }
        public void Right() { SetStalk(SwitchPosition.Positive); }

        private void SetStalk(SwitchPosition position)
        {
            if (indicatorStalk && indicatorStalk.threePosition)
                indicatorStalk.SetPosition(position);
        }
    }
}
```

Attach this script to a cockpit helper, assign the fields and connect each Button to one method. `ToggleWithGesture` uses the interaction's configured mode and prerequisites. Configure `IndicatorSwitchBinding.LeftPosition` as Negative to match this example. Calling these methods from another input handler works the same way; no particular UI package is required by the script itself.

For a custom asynchronous animation driver, implement `IControlInteractionDriver`. Retain the `ControlInteractionRequest` passed to `Begin` and call its `Commit`, `Complete` or `Cancel`. Check `IsActive` before delayed work: callbacks from an old request must not act on a newer interaction. The [interaction API](API/Interactions.md#controlinteraction) describes the request and driver contracts.

## Request lifecycle and interruption

An interaction has one active request at a time. Admission creates that request; **On Started** reports its beginning. Commit performs its gameplay action at most once. Complete commits first if necessary, restores temporary interaction state and raises **On Completed**. Cancel restores temporary ownership and raises **On Cancelled** without rolling back an action that already committed.

`TryBegin` returning true means a request started, not that the mechanic accepted its eventual action. For example, an occupied hand can successfully reach a switch whose profile transition is later rejected. Read the mechanic's own result/state for gameplay success.

The request records the seat occupant that started it. Exiting, replacing or disabling that occupant/seat invalidates the ongoing gesture. A disabled target, an interrupted Animator hand binding or a disabled custom driver can cancel it too. Do not retain a previous occupant's request when assigning the interaction to another seat.

Set a timeout long enough for travel, contact and return at the slowest supported playback. A very short timeout can cancel a valid gesture. A zero timeout requires your animation/custom integration to guarantee completion or cancellation. When changing scenes or abandoning a control, call `Cancel` or disable the interaction.

## Share or separate interaction components

Use separate components for controls that need independent targets, timings or event listeners. Reusing one component is suitable when the application deliberately serializes all gestures through one hand: reject/defer a new action while `IsBusy` is true, configure its destination before starting, and leave its in-progress configuration alone.

A limb cannot run two operations simultaneously. Admission respects the source handle's Minimum Attachments unless the requesting handle explicitly enables Allow Unsupported Departure. Ownership is independent per seat and limb; this support rule is the only reason a request on another limb can prevent leaving a shared home handle. Rejected starts return false; the application decides whether to defer, retry or apply immediately. Active operations wait by default. A timed request can be interrupted by a handle with **Interrupt Lower Priority** enabled and a strictly higher Priority; persistent and Animator ownership remain protected. Automatic handle rules retry while the action stays active, in descending priority order.

For Animator gestures, use an arm/hand Avatar Mask and suitable layer blending when the clip should affect only that limb. Triggering a full-body clip can disturb a seated pose even if the control's action timing is correct. Commit Time and Duration are elapsed seconds and do not automatically follow changes to clip speed; Animation Events are preferable when contact must follow the clip's actual phase.

## Verify an interaction

| Test | Expected behavior |
| --- | --- |
| Immediate action without an occupant | Commits once and completes |
| IK/Animator/Custom without an occupant | Start is rejected |
| Second start while busy | Rejected; no second action is queued |
| Cancel before contact | No commit; temporary ownership is restored |
| Cancel after contact | Existing action remains; gesture cleanup still runs |
| Missing Animator completion event | Timeout cancels if enabled |
| Passenger leaves during the gesture | Gesture cancels and does not act on the replacement occupant |
| Delayed callback after cancellation | Inactive captured request refuses to commit a newer action |

For signatures, event payloads and a complete custom-driver example, see [interaction contracts](Scripting/Interactions.md) and the [API](API/Interactions.md). For entry/exit animations that change seat occupancy, use [Passenger access](PassengerAccess.md) instead of a cockpit interaction.
