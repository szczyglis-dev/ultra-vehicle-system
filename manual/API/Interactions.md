# Committed control interactions API

Read [the system explanation](../Scripting/Interactions.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [ControlInteraction](Interactions.md#controlinteraction)
- [ControlInteractionAnimationEvents](Interactions.md#controlinteractionanimationevents)
- [ControlInteractionMode](Interactions.md#controlinteractionmode)
- [ControlInteractionRequest](Interactions.md#controlinteractionrequest)
- [IControlInteractionDriver](Interactions.md#icontrolinteractiondriver)

## ControlInteraction

**Runtime/Interior/Controls/ControlInteraction.cs**

`Started`, `Commit`, `Completed` and `Cancelled`

**Inherits / implements:** `MonoBehaviour`.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public UnityEvent onCancelled` | After an active interaction is cancelled. No payload; committed gameplay is not rolled back. |
| `public UnityEvent onCommit` | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks. |
| `public UnityEvent onCompleted` | After the interaction completes. No payload; completion commits first if still needed. |
| `public UnityEvent onStarted` | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual ControlInteractionRequest ActiveRequest { get; protected set; }` | Exact active interaction request, or `null` when idle; retain this identity for delayed callbacks. |
| `public bool animationEvents` | Use Animation Events to call `Commit` and `Complete` instead of elapsed time. |
| `public string animationLayer` | Optional Animator layer name. Empty leaves layer weights unchanged; configure a matching trigger transition on the chosen layer. |
| `public float animationLayerWeight` | Layer weight captured for the request, clamped to 0–1. Default 1; restored on completion/cancellation unless externally changed. |
| `public float animationEnterBlend` | Duration of the Animator gesture layer fade in seconds (default 0.2). Starts from the previous weight; zero applies immediately. Gesture timing continues during the fade. |
| `public float animationReturnBlend` | Duration of the completed Animator gesture layer fade in seconds (default 0.2). The interaction retains ownership until the fade finishes; zero restores immediately. Cancellation remains immediate. |
| `public Animator animator` | Optional override. Otherwise use the current occupant's `SeatedAnimator`. |
| `public float commitTime` | Time in seconds used for commit time. Larger values make this phase/wait last longer. Initial value: `.25f`. |
| `public MonoBehaviour customDriver` | A `MonoBehaviour` implementing `IControlInteractionDriver`. |
| `public float duration` | Time in seconds over which this transition/action runs. Initial value: `.7f`. |
| `public PassengerBodyPart hand` | Selects the hand policy for this configuration. Options: `LeftHand`, `RightHand`, `LeftFoot`, `RightFoot`. Initial value: `PassengerBodyPart.LeftHand`. |
| `public virtual bool IsBusy { get; }` | True while an `ActiveRequest` exists, including presentation after gameplay commit. |
| `public bool keepHandOnTargetWhileAnimating` | IKThenAnimator only: retain IK/native wrist support and animate fingers from a finger-only layer. Default false; captured at admission. |
| `public ControlInteractionMode mode` | Selects the operating policy; see the listed options and the owning component guide. Options: `Immediate`, `IK`, `Animator`, `Custom`, `IKThenAnimator`. Initial value: `ControlInteractionMode.IK`. |
| `public PassengerSeat seat` | Assign the seat PassengerSeat component/asset used by ControlInteraction. |
| `public VehicleHandle target` | Assign the target VehicleHandle component/asset used by ControlInteraction. |
| `public float timeout` | Cancels an unfinished Animator or Custom action, including missing animation events. Zero disables timeout. |
| `public string trigger` | Text identifier/name for trigger. Keep it consistent with the referenced animation, profile or application setting. Initial value: `"Interact"`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Begin()` | `UnityEvent`-friendly wrapper around `TryBegin`; it discards the bool result. Use `TryBegin` when the caller must handle refusal. | No arguments; no returned value. |
| `public virtual void Cancel()` | Cancels the active interaction, stops owned driver/transfer/animation state and invokes `onCancelled`. Already committed gameplay is retained. | No arguments; no returned value. |
| `public virtual bool Commit()` | Commits gameplay at most once for the addressed interaction request. | **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual void CommitAnimation()` | Commits the current interaction from an Animation Event entry point. | No arguments; no returned value. |
| `public virtual bool Complete()` | Completes an active request, committing first if necessary; Animator layers fade out before releasing ownership; IKThenAnimator then requests its timed hand return and finishes after that return; after commit rechecks request identity before cleanup/completion notification. | **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual void CompleteAnimation()` | Completes the current interaction from an Animation Event entry point. | No arguments; no returned value. |
| `public virtual void Tick(float deltaTime)` | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual bool TryBegin(Action onCommit = null)` | Requests a control interaction; `true` means admitted, not necessarily committed or completed. | `onCommit` — Optional gameplay callback invoked at most once before the interaction's `onCommit` `UnityEvent`. Default: `null`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TrySetAnimationLayer(int layerIndex)` | Select the next layer by index on the current gesture Animator. Index -1 clears the override. | False while busy, for invalid indices or when no controller is available. |
| `public virtual bool TrySetAnimationLayer(string layerName)` | Configure the next gesture layer while idle. Null/empty preserves controller weights. Rejects missing layers when an Animator controller is available; a name may be configured before an occupant is present. | False while busy or if the resolved controller lacks the layer; no mutation on failure. |

## ControlInteractionAnimationEvents

**Runtime/Interior/Controls/ControlInteractionAnimationEvents.cs**

Relays Animator events to the active interaction.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public ControlInteraction interaction` | Assign the interaction ControlInteraction component/asset used by ControlInteractionAnimationEvents. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void CancelInteraction()` | Relays an Animator cancellation event to the configured control interaction. | No arguments; no returned value. |
| `public virtual void CommitAnimation()` | Commits the current interaction from an Animation Event entry point. | No arguments; no returned value. |
| `public virtual void CompleteAnimation()` | Completes the current interaction from an Animation Event entry point. | No arguments; no returned value. |

## ControlInteractionMode

**Runtime/Interior/Controls/ControlInteraction.cs**

Defines the allowed control interaction mode choices used by this topic.

### Values

- `Immediate`
- `IK`
- `Animator`
- `Custom`
- `IKThenAnimator`

## ControlInteractionRequest

**Runtime/Interior/Controls/ControlInteraction.cs**

Identity of one admitted control interaction; captured callbacks remain tied to this request.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public PassengerBodyPart Hand { get; internal set; }` | Read-only/resolved hand for `ControlInteractionRequest`. |
| `public bool IsActive { get; }` | Whether this request still equals its interaction owner's `ActiveRequest`. |
| `public PassengerBody Occupant { get; internal set; }` | Body currently admitted to this seat, or `null` when empty. |
| `public PassengerSeat Seat { get; internal set; }` | Read-only/resolved seat for `ControlInteractionRequest`. |
| `public VehicleHandle Target { get; internal set; }` | Read-only/resolved target for `ControlInteractionRequest`. |
| `public HandleUse Use { get; internal set; }` | Central limb ownership token for IK, Animator and Custom modes. Null for Immediate. Do not restore seat bindings independently of this token. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void Cancel()` | Cancels only if this exact request remains active; it cannot cancel a newer request. | No arguments; no returned value. |
| `public bool Commit()` | Commits only while this request is still the owner's `ActiveRequest`. A stale request cannot commit a newer interaction. | **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public bool Complete()` | Completes only this still-active request; stale callbacks return `false`. | **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## IControlInteractionDriver

**Runtime/Interior/Controls/ControlInteraction.cs**

Configuration/implementation type for icontrol interaction driver within committed control interactions.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void Begin(ControlInteractionRequest request)` | Accepts ownership of one exact interaction request. Start application presentation and retain that request for delayed commit/completion. | `request` — Exact interaction attempt; retain it for asynchronous callbacks. |
| `void Cancel(ControlInteractionRequest request)` | Stops presentation owned by the supplied request and releases only that request's resources. | `request` — Exact interaction attempt; retain it for asynchronous callbacks. |
