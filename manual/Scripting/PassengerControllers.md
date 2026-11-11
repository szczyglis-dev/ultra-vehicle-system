# Passenger occupancy and controllers

Passenger integration separates the fact that a seat is occupied from the way its character is controlled. `PassengerSeat` validates and owns occupancy. A controller strategy decides how an admitted body is attached, posed and advanced. The body adapter exposes the character that strategy operates on.

This separation lets an application retain its own character framework while using package seats, reservations and events. Choose the controller by ownership needs: native passenger physics, animation with limb overlays, simple attachment or application-owned behavior.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `CustomPassengerBody` | Minimal body for application-owned Custom occupancy. |
| `HumanoidPassenger` | Connects humanoid rig, pose and physical passenger behavior. |
| `PassengerBody` | Base character adapter used by seats and controller strategies. |
| `PassengerController` | Defines per-seat attachment, detachment and stepping behavior. |
| `Passengers` | Discovers owned seats and schedules passenger work after vehicle.handles. |
| `PassengerSeat` | Owns admission, occupancy, reservations and controller handover. |

## Operation hooks

Seat and core Before/After notifications carry [PassengerSeatContext](../API/PassengerControllers.md#passengerseatcontext), including Vehicle, Passenger, Seat and release parameters. See [hook ordering and the collider integration example](../Passengers.md#before-and-after-hooks). Use seat/core hooks for attachment and detachment; use PassengerAccess hooks when the whole door/motion sequence matters.

## Seat versus character

The body adapter is the character-facing half of the integration. It answers whether the body can enter and provides attachment/detachment behavior used by a strategy. The seat-facing half owns who occupies the seat and whether another operation has reserved it. Neither half should silently choose the application's active player.

Use `HumanoidPassenger` when the package should operate its mapped humanoid. Use `CustomPassengerBody` when an external framework keeps character hierarchy, physics and pose. For a new body subclass, inspect both `CanEnter` overloads and the attachment/detachment contract; admission should reject an incompatible strategy before it partially changes the character.

`CustomPassengerBody` accepts Custom, and automatic spawn-on-start skips Custom. Instantiate that body in the application and request entry explicitly. Choose the seat's controller strategy before requesting entry. Runtime `SetPassengerController` is a handover operation and can fail for a busy or incompatible body; check the return instead of assuming the requested enum is already active. `ControllerChanged` reports a successful strategy change with the previous and new choices.

Think of the seat as the authority and the controller as its implementation choice. A strategy should not independently announce a second entry or maintain a competing occupied flag. This is especially important when switching a seated character from animation to physics: ownership changes, but there is still one seat and one occupant.

`PassengerType` describes the seat's role, such as driver or passenger. `PassengerControllerType` describes how its occupant is managed. A custom player character can occupy a driver seat without requiring the package to take over its hierarchy or animation; the application must then connect possession and driving input itself.

`PassengerSeat` owns occupancy, reservation, controller strategy and lifecycle events. `PassengerBody` owns the character-specific attachment/detachment/pose hooks. A new controller strategy instance belongs to each seat. `PassengerType` classifies the role; `PassengerControllerType` selects behavior.

| Controller | Ownership |
| --- | --- |
| `RagdollPhysics` | Physical/IK character path |
| Animator | Application animation on an attached character |
| `AnimatorIK` | Animation with configured limb IK overlays |
| `AttachOnly` | Parenting/alignment without humanoid posing |
| Custom | Occupancy only; application owns character hierarchy, pose and physics |

## Connect a custom character

The example selects the Custom strategy before requesting entry. Either operation can fail, so the result is returned to the caller. Do not update application possession merely because an `Enter` button was pressed; update it after successful admission or from the seat's occupancy event.

For Custom mode, decide explicitly what happens to the character's movement controller, camera, collisions and visible seated representation. The seat supplies occupancy coordination, not assumptions about those application systems. On exit, restore only state that the integration actually took ownership of.

Put `CustomPassengerBody` on your character, select Custom on the seat and assign the body below. Call `Enter`/`Exit` from the application. The boolean return is immediate occupancy admission, not an animated access completion.

**Example: `CustomCharacterOccupancy.cs`**

<!-- example: CustomCharacterOccupancy.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class CustomCharacterOccupancy : MonoBehaviour
    {
        public PassengerSeat seat;
        public CustomPassengerBody character;

        public bool Enter()
        {
            if (!seat || !character || !seat.SetPassengerController(PassengerControllerType.Custom))
                return false;
            return seat.TryEnter(character);
        }

        public bool Exit() => seat && seat.TryExit();
    }
}
```

Handle `Entered`/`Exited`/`ResetRequested` to move or animate your character framework. The package does not add a seated pose, ejection impulse or automatic respawn to a Custom occupant.

## Replace the seat strategy factory

Override `CreatePassengerController` when the existing enum choice should create an application-specific strategy. Returning the base factory result for other choices keeps them available. The created strategy instance belongs to that seat, so counters and captured state are not shared across unrelated seats.

The example calls `base.Attach` before recording success. A failed base attachment must not count as an admitted occupant. For a more extensive implementation, pair any acquired resources or subscriptions with `Detach` cleanup, and account for both ordinary exit and handover to another strategy.

Use a derived seat when a strategy needs application state while retaining occupancy validation/events. This example counts successful Custom attachments. Its controller extends the public Custom implementation, so it does not call package-internal body helpers.

**Example: `ApplicationPassengerSeat.cs`**

<!-- example: ApplicationPassengerSeat.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class ApplicationPassengerSeat : PassengerSeat
    {
        protected override PassengerController CreatePassengerController(PassengerControllerType type)
            => type == PassengerControllerType.Custom
                ? new CountingCustomController()
                : base.CreatePassengerController(type);
    }

    public class CountingCustomController : CustomPassengerController
    {
        public int Attachments { get; private set; }

        public override bool Attach(PassengerBody body, PassengerSeat seat)
        {
            if (!base.Attach(body, seat)) return false;
            Attachments++;
            return true;
        }
    }
}
```

Strategies do not publish seat occupancy events themselves. A complete replacement owns its attachment/cleanup work, while the seat retains admission and event ordering. See [access](PassengerAccess.md) for asynchronous boarding and [physics](PassengerPhysics.md) for dynamic occupants.

## Custom joint support API

Seat `jointSupports` entries are keyed by the occupant’s Anatomical Joint ID. `GetJointSupport` returns live settings; edit their spring, damper, target or caps directly, or use `UpdateJointSupport`. These changes apply on the next passenger physics step, without rebuilding anatomical joints or re-entering the seat. `SetJointSupportActive` pauses one support; `RemoveJointSupport` deletes its configuration. An empty seat can be configured before a body enters.

See [custom joint support setup and example](../Seats.md#custom-ragdoll-joint-supports) for a working knee-target example. `TryGetJointSupportState` reports the last calculated force, torque and world points while that support is valid. It returns false when the seat/occupant is unavailable, the entry is inactive, the target or joint cannot be resolved, or no support step has run. The snapshot is a calculated support contribution, not the ragdoll’s total joint load.

IDs use ordinal, case-sensitive matching. The API rejects blank or duplicate IDs. Direct Inspector/list edits remain supported; duplicate seat IDs, duplicate anatomical IDs, missing joints and missing targets are skipped safely. Changing settings does not require a refresh call. The list is empty by default; no additional position constraints are applied until entries are configured.

## Independent attachment API

Use `SetAttachmentMode(PassengerAttachmentMode.Parent)` before entry or during occupancy. Check its boolean result; busy access or incompatible attachment rejects the handover. Spring is the default. The mode does not change the selected controller or turn off a physical ragdoll. Each transform entry separately selects mode = PassengerAttachmentMode.Spring or Parent; springs also simulate plain/kinematic transforms. Parent can optionally make only the held Rigidbody kinematic. Explicit support lists work with every controller, including Custom. Additional bindings use transform references, not anatomical joint IDs; entries authored on Body Prefab resolve on the spawned occupant.

<!-- example: RigidPassengerAttachment.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class RigidPassengerAttachment : MonoBehaviour
    {
        public PassengerSeat seat;
        public Transform passengerBone;
        public Transform vehicleAnchor;

        public bool Configure()
        {
            if (!seat || !seat.SetAttachmentMode(PassengerAttachmentMode.Parent)) return false;
            return seat.AddTransformSupport(new PassengerTransformSupport {
                id = "passenger.hand",
                followAnchorRotation = true,
                mode = PassengerAttachmentMode.Parent,
                makeKinematic = true,
                bodyTransform = passengerBone,
                anchor = vehicleAnchor,
                positionOffset = new Vector3(0, 0.02f, 0)
            });
        }

        public void ReleaseBone()
        {
            if (seat) seat.SetTransformSupportActive("passenger.hand", false);
        }
    }
}
```

Transform overloads operate on the configured bodyTransform reference; string overloads use the same single ID / Label displayed in the Inspector. Use UpdateTransformSupport("passenger.hand", support => support.followAnchorRotation = false) to capture a fixed world rotation on refresh. See [the detailed API](../API/PassengerControllers.md#passengerseat) and [attachment configuration](../Seats.md#main-attachment-and-rigid-transform-supports).

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed seats, bodies and controller strategies API](../API/PassengerControllers.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### AnimatorIKPassengerController

[AnimatorIKPassengerController](../API/PassengerControllers.md#animatorikpassengercontroller) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |

### AnimatorPassengerController

[AnimatorPassengerController](../API/PassengerControllers.md#animatorpassengercontroller) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |

### AttachOnlyPassengerController

[AttachOnlyPassengerController](../API/PassengerControllers.md#attachonlypassengercontroller) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |

### BalanceRider

[BalanceRider](../API/PassengerControllers.md#balancerider) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void ResetPassenger(Passengers core)` | Resets this passenger behavior's state for the supplied seat. |
| `public override bool AppliesTo(VehicleController vehicle)` | Checks whether this passenger behavior should run for the supplied seat/role. |


| `public event Action<RiderMotionState> MotionUpdated` | Rider motion configuration or signal; see the setup guide. |
| `public event Action<bool> FootPushingChanged` | Rider motion configuration or signal; see the setup guide. |
| `public event Action<PassengerBodyPart> FootPlanted` | Rider motion configuration or signal; see the setup guide. |
| `public UnityEvent<RiderMotionState> onMotionUpdated` | Current motion state after rider targets update. Suitable for custom animation integrations. |
| `public UnityEvent<bool> onFootPushingChanged` | Foot propulsion begins or stops; false is also published on disable or loss of occupancy. |
| `public UnityEvent<PassengerBodyPart> onFootPlanted` | A foot starts its planted phase. The two feet alternate while pushing backward. |

### CustomPassengerBody

[CustomPassengerBody](../API/PassengerControllers.md#custompassengerbody) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool CanEnter(PassengerSeat seat)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. |
| `public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. |
| `public override bool Attach(PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
| `public override void Detach(PassengerExitReason reason)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. |

### CustomPassengerController

[CustomPassengerController](../API/PassengerControllers.md#custompassengercontroller) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
| `public override void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. |

### HumanoidPassenger

[HumanoidPassenger](../API/PassengerControllers.md#humanoidpassenger) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void PrepareRagdollCollisions()` | Prepares the character's skeletal collision exclusions and collision relays. |
| `public override bool Attach(PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
| `public virtual void SolveSeatedIK()` | Applies the seated character's configured limb IK targets. |
| `public override void StepSeated(Passengers core, float deltaTime)` | Advances this body's seated behavior through its selected character path. |
| `public override void ResetSeatedPose()` | Restores the character's seated pose/support through the selected physical/animation path. |
| `public override void DetachForTransition()` | Releases seated ownership for an animated character handover while preserving the required transition pose. |
| `public override void Detach(PassengerExitReason reason)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. |
| `public virtual void ActivateRagdoll()` | Hands the character to free skeletal physics, releasing seated pose ownership. |
| `public override bool CanEnter(PassengerSeat seat)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. |
| `public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. |
| `public virtual void RestoreAccessReferencePose()` | Restores the character pose retained for an access-motion handover. |
| `public virtual void PreviewAccessPose(PassengerSeat seat)` | Applies an access reference pose for character/seat authoring or transition preparation. |
| `public override void AddVelocity(Vector3 velocityChange)` | Adds the supplied velocity change to the character bodies used by this body implementation. |
| `public virtual void ReadAnatomicalJointSettings()` | Reads saved native joint configuration into the character's runtime anatomical references. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<HumanoidPassenger> BeforeSeatedIK` | Immediately before seated IK work. Payload: `HumanoidPassenger`; custom pose inputs must respect the selected character owner. |
| `public event System.Action<HumanoidPassenger> AfterSeatedIK` | Immediately after seated IK work. Payload: `HumanoidPassenger`. |

| Method | Behavior |
| --- | --- |
| `public virtual bool TryGetAnatomicalJointDefinition(string jointId, out HumanoidJointDefinition definition)` | Returns the unique definition with a live joint for the case-sensitive ID; false/null for empty, missing, duplicate or destroyed entries. |
| `public virtual bool TryGetAnatomicalJoint(string jointId, out ConfigurableJoint joint)` | Returns true and the native ConfigurableJoint for a unique live ID; otherwise false and null. Lookup allocates no managed memory. |
| `public virtual ConfigurableJoint GetAnatomicalJoint(string jointId)` | Returns the native ConfigurableJoint for a unique live ID, or null when unresolved/ambiguous. |
| `public virtual bool UpdateAnatomicalJoint(string jointId, System.Action<ConfigurableJoint> update)` | Runs the callback on a uniquely resolved joint, then refreshes its cached anatomy/IK data. False for unresolved ID or null callback. Callback exceptions propagate after cache refresh. |


| Method / event / callback | Role |
| --- | --- |
| `public virtual void BlendIntoPhysics(float seconds, Transform referenceFrame = null)` | See [HumanoidPassenger](../API/PassengerControllers.md#humanoidpassenger) for the declared lifecycle and arguments. |

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### PassengerBehaviour

[PassengerBehaviour](../API/PassengerControllers.md#passengerbehaviour) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public sealed override void StepPassenger(Passengers core, float deltaTime)` | Advances passenger work in the supplied seat/core context. |
| `public virtual bool AppliesTo(VehicleController vehicle)` | Checks whether this passenger behavior should run for the supplied seat/role. |

### PassengerBody

[PassengerBody](../API/PassengerControllers.md#passengerbody) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public abstract bool Attach(PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
| `public abstract void Detach(PassengerExitReason reason)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. |
| `public virtual void DetachForTransition()` | Releases seated ownership for an animated character handover while preserving the required transition pose. |
| `public virtual void StepSeated(Passengers core, float deltaTime)` | Advances this body's seated behavior through its selected character path. |
| `public virtual void ResetSeatedPose()` | Restores the character's seated pose/support through the selected physical/animation path. |
| `public virtual bool CanEnter(PassengerSeat seat)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. |
| `public virtual bool CanEnter(PassengerSeat seat, PassengerControllerType controller)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. |
| `public virtual void AddVelocity(Vector3 velocityChange)` | Adds the supplied velocity change to the character bodies used by this body implementation. |

### PassengerController

[PassengerController](../API/PassengerControllers.md#passengercontroller) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public abstract bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
| `public virtual void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. |
| `public virtual void Step(PassengerBody body, Passengers core, float deltaTime)` | Empty base passenger strategy step; derived strategies decide which body work they own. |
| `public static PassengerController Create(PassengerControllerType type)` | Creates the built-in strategy for a `PassengerControllerType`; seat factory overrides can substitute application strategies. |

### PassengerAnimatorLayers

| Method | Role |
| --- | --- |
| `public void Apply()` | Applies configured overlay weights to the current occupant. |
| `public void RefreshBindings()` | Restores previous weights and resolves bindings again. |
| `public bool SetLayerEnabled(string layerName, bool value)` | Mutes/restores a configured overlay. |
| `public bool SetWeight(string layerName, float weight)` | Sets a finite weight request for a configured overlay. |

### PassengerModule

[PassengerModule](../API/PassengerControllers.md#passengermodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public sealed override void Step(VehicleController vehicle, Command command, float deltaTime)` | Intentionally empty sealed module-pipeline entry point. Passenger-local work runs through `StepPassenger`/`RenderPassenger` under Passengers. |
| `public virtual void PreparePassenger(Passengers core, PassengerSeat seat)` | Prepares this passenger behavior for an occupied seat. |
| `public virtual void ResetPassenger(Passengers core)` | Resets this passenger behavior's state for the supplied seat. |
| `public virtual void RenderPassenger(Passengers core)` | Advances render-time passenger presentation owned by this behavior/core. |
| `public virtual void StepPassenger(Passengers core, float deltaTime)` | Advances passenger work in the supplied seat/core context. |

### Passengers

[Passengers](../API/PassengerControllers.md#passengers) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void RefreshPassengers()` | Rebuilds the owned seat and passenger-behavior snapshot. Handles use vehicle.handles.Refresh(). |
| `public override void Configure(VehicleController vehicle)` | Rebuilds the owned passenger seats, ordered handles and passenger-local behaviors. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Supplies commands to handles in order, then advances passenger modules and seats from the owned snapshot. |
| `public virtual void PrepareOccupant(PassengerSeat seat)` | Prepares a seat's occupant and its local handles/passenger behaviors. |
| `public virtual void ResetOccupants()` | Resets eligible owned seated/released occupants through their seat lifecycle. |
| `public virtual bool TryEnter(PassengerBody body, PassengerSeat seat = null)` | Routes an entry request through an owned seat/passenger selection and that seat's validation. |
| `public virtual bool TryExit(PassengerBody body, PassengerExitReason reason = PassengerExitReason.Exit)` | Requests immediate exit or starts animated departure, depending on the declaring owner. |

| Event / callback | Role |
| --- | --- |
| `public event Action<PassengerSeatContext> BeforeEnter` | After admission validation, before occupancy assignment and controller attachment. Occupant and Passenger.Seat are still empty. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterEnter` | After successful attachment and existing Entered notifications. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeExit` | While the passenger still owns the seat, before detachment. Includes ordinary exit, ejection, disable and destruction. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterExit` | After detachment and existing Exited notifications. During ejection this precedes the extra velocity change. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeEject` | Before any ejection detachment, while the seat is still occupied. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterEject` | After ejected detachment and the requested built-in velocity change. Custom controllers retain their application-owned physics. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeat, PassengerBody> Entered` | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat. |
| `public event Action<PassengerSeat, PassengerBody, PassengerExitReason> Exited` | After occupancy is released. Payload identifies occupant and `PassengerExitReason`; the core delegate also includes the seat. |


| Method / event / callback | Role |
| --- | --- |
| `public UnityEvent<PassengerSeatContext> onBeforeEnter` | See [Passengers](../API/PassengerControllers.md#passengers) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerSeat, PassengerBody> onEntered` | See [Passengers](../API/PassengerControllers.md#passengers) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerSeatContext> onBeforeExit` | See [Passengers](../API/PassengerControllers.md#passengers) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerSeat, PassengerBody, PassengerExitReason> onExited` | See [Passengers](../API/PassengerControllers.md#passengers) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerSeatContext> onBeforeEject` | See [Passengers](../API/PassengerControllers.md#passengers) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerSeatContext> onEjected` | See [Passengers](../API/PassengerControllers.md#passengers) for the declared lifecycle and arguments. |

### PassengerSeat

[PassengerSeat](../API/PassengerControllers.md#passengerseat) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual bool Spawn()` | Creates/requests the configured passenger representation through the seat's spawn policy. |
| `public virtual bool Eject(Vector3 velocityChange)` | Requests whole-occupant release through the seat's controller/body lifecycle. |
| `public virtual void StepPassenger(Passengers core, float deltaTime)` | Advances passenger work in the supplied seat/core context. |
| `public virtual void RestoreDamageFeedback()` | Restores the eligible seated limb supports released by damage feedback. |
| `public virtual bool SetPassengerController(PassengerControllerType type)` | Requests a validated strategy handover for the seat; an incompatible/busy handover can be rejected. |
| `public virtual void SetCollisionExclusions(bool self, bool vehicle)` | Sets seated self/vehicle collision exclusion policy and updates the occupied character. |
| `public virtual void SetReleaseCollisions(bool self, bool vehicle)` | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb. |
| `public virtual void SetReleaseCollisions(PassengerBodyPart part, bool self, bool vehicle)` | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb. |
| `public virtual void RefreshCollisionSettings()` | Reapplies the seat's collision policy to its current occupant. |
| `public virtual PassengerBodyPartConfig GetBodyPart(PassengerBodyPart part)` | Returns the seat configuration for a selected limb/body part. |
| `public virtual bool TryReserve(PassengerAccess owner)` | Reserves a seat for an identified access/request owner without establishing occupancy. |
| `public virtual void ReleaseReservation(PassengerAccess owner)` | Releases a seat reservation belonging to the supplied reservation owner. |
| `public virtual bool TryEnter(PassengerBody passenger)` | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. |
| `public virtual bool TryEnter(PassengerBody passenger, PassengerAccess reservation)` | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. |
| `public virtual bool TryExit(PassengerExitReason reason = PassengerExitReason.Exit, bool preservePose = false)` | Releases current occupancy through its active strategy and exit reason; it does not run an animated access sequence. |

| Event / callback | Role |
| --- | --- |
| `public event Action<PassengerSeatContext> BeforeEnter` | After admission validation, before occupancy assignment and controller attachment. Occupant and Passenger.Seat are still empty. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterEnter` | After successful attachment and existing Entered notifications. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeExit` | While the passenger still owns the seat, before detachment. Includes ordinary exit, ejection, disable and destruction. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterExit` | After detachment and existing Exited notifications. During ejection this precedes the extra velocity change. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeEject` | Before any ejection detachment, while the seat is still occupied. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterEject` | After ejected detachment and the requested built-in velocity change. Custom controllers retain their application-owned physics. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeat, PassengerControllerType, PassengerControllerType> ControllerChanged` | After a successful seat strategy handover. Payload: seat, previous controller type, new controller type; no extra entry/exit is synthesized. |
| `public event Action<PassengerBody> Entered` | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat. |
| `public event Action<PassengerBody> ResetRequested` | When Custom occupancy receives a reset request. Payload: `PassengerBody`; application owns the actual custom-character reset. |
| `public event Action<PassengerBody, PassengerExitReason> Exited` | After occupancy is released. Payload identifies occupant and `PassengerExitReason`; the core delegate also includes the seat. |

- **PassengerSeat** — `public virtual bool AddJointSupport(PassengerJointSupport support)`
- **PassengerSeat** — `public virtual PassengerJointSupport GetJointSupport(string jointId)`
- **PassengerSeat** — `public virtual bool RemoveJointSupport(string jointId)`
- **PassengerSeat** — `public virtual bool SetJointSupportActive(string jointId, bool active)`
- **PassengerSeat** — `public virtual bool TryGetJointSupport(string jointId, out PassengerJointSupport support)`
- **PassengerSeat** — `public virtual bool TryGetJointSupportState(string jointId, out PassengerJointSupportState state)`
- **PassengerSeat** — `public virtual bool UpdateJointSupport(string jointId, Action<PassengerJointSupport> update)`

| Signature | Role |
| --- | --- |
| `public virtual bool SetAttachmentMode(PassengerAttachmentMode mode)` | Change main attachment while retaining occupancy. |
| `public virtual void RefreshTransformSupports()` | Rebuild bindings after direct list/settings edits. |
| `public virtual bool AddTransformSupport(PassengerTransformSupport support)` | Add a unique configuration and refresh. |
| `public virtual PassengerTransformSupport GetTransformSupport(Transform bodyTransform)` | Look up a unique live configuration. |
| `public virtual bool RemoveTransformSupport(Transform bodyTransform)` | Remove matching configurations and refresh. |
| `public virtual bool SetTransformSupportActive(Transform bodyTransform, bool active)` | Toggle and refresh one unique configuration. |
| `public virtual bool UpdateTransformSupport(Transform bodyTransform, Action<PassengerTransformSupport> update)` | Edit settings and refresh even if the callback throws. |

| Signature | Role |
| --- | --- |
| `public virtual bool TryGetTransformSupport(string id, out PassengerTransformSupport support)` | Resolve a unique ID; false for blank, missing or ambiguous names. |
| `public virtual PassengerTransformSupport GetTransformSupport(string id)` | Read live settings by ID / Label. |
| `public virtual bool SetTransformSupportActive(string id, bool active)` | Toggle and refresh a binding by ID. |
| `public virtual bool UpdateTransformSupport(string id, Action<PassengerTransformSupport> update)` | Update and refresh settings by ID. |
| `public virtual bool RemoveTransformSupport(string id)` | Remove and refresh a unique binding by ID. |


| Method / event / callback | Role |
| --- | --- |
| `public UnityEvent<PassengerBody> onBeforeEnter` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody> onEntered` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody> onBeforeExit` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody, PassengerExitReason> onExited` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody> onBeforeEject` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody> onEjected` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerControllerType> onControllerChanged` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody> onResetRequested` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBodyPart> onLimbReleased` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody> onHandsReleased` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public UnityEvent<PassengerBody> onFeetReleased` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |
| `public virtual bool ReleaseLimb(PassengerBodyPart part)` | See [PassengerSeat](../API/PassengerControllers.md#passengerseat) for the declared lifecycle and arguments. |

### RagdollPhysicsPassengerController

[RagdollPhysicsPassengerController](../API/PassengerControllers.md#ragdollphysicspassengercontroller) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
| `public override void Step(PassengerBody body, Passengers core, float deltaTime)` | Calls the admitted body's `StepSeated` through the physical passenger path. |

### VehicleModule

[VehicleModule](../API/Modules.md#vehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void Configure(VehicleController vehicle)` | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
| `public virtual void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it. |
| `public virtual void SetEnabled(bool value)` | Changes module enabled state and publishes an actual requested-flag change. |
| `public virtual bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> EnabledChanged` | After `SetEnabled` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
| `public event System.Action<VehicleController> Configured` | After controller-driven module configuration. Payload: the owning `VehicleController`. |
| `public event System.Action<VehicleController, Command, float> Stepped` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds. |

## Rider actions and foot reversing

Configure the rider on the driver's seat; the same settings work with Motorcycle Profile or Wheeled Profile. Leave Motorcycle Profile Only disabled for other profiles.

```csharp
rider.reverseMode = RiderReverseMode.FootPushing;
rider.pushFeet = RiderPushFeet.Both; // Left or Right for a scooter.
rider.MotionUpdated += state => UpdateMyRiderUI(state.speed, state.footPushing);

// A Custom rule named LookBehind can select your own Animator state/parameters.
riderAnimator.SetActionActive("LookBehind", shouldLookBehind);
riderAnimator.PlayAction("LookBehind"); // Explicitly restart its entry.
riderAnimator.StopAction("LookBehind");

// Or crossfade directly to a state in the assigned controller.
bool played = riderAnimator.PlayAnimation("Upper Body.LookBehind", 1, .2f);
```

Configure masks/layers in the Animator Controller or Passenger Animator Layers. The named action API returns false for an unknown action or disabled bridge; direct playback returns false when the Animator, layer or state is unavailable. Call RefreshBindings after changing the rule definitions. See [rider setup](../Seats.md#motorcycle-foot-reversing-and-rider-animations).

### RiderAnimationRule

| Member | Meaning |
| --- | --- |
| `public UnityEvent onEntered` | Condition began, including angle-range transitions. Can call custom animation code. |
| `public UnityEvent onExited` | Condition ended or the occupant/binding was released. |

### RiderAnimator

| Member | Meaning |
| --- | --- |
| `public void RefreshBindings()` | Rebind after changing names, rules, controller or rider. |
| `public bool SetActionActive(string actionName, bool active)` | Set a named Custom condition without restarting unchanged state. Returns false if unavailable or unknown. |
| `public bool PlayAction(string actionName)` | Retrigger the named custom action. |
| `public bool StopAction(string actionName)` | End the named custom action. |
| `public bool PlayAnimation(string stateName, int layer = 0, float fadeSeconds = .2f)` | Crossfade to an existing Animator state; false for missing Animator/state/layer. |
