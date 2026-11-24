# Seats, bodies and controller strategies API

Read [the system explanation](../Scripting/PassengerControllers.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [AnimatorIKPassengerController](PassengerControllers.md#animatorikpassengercontroller)
- [AnimatorPassengerController](PassengerControllers.md#animatorpassengercontroller)
- [AttachOnlyPassengerController](PassengerControllers.md#attachonlypassengercontroller)
- [BalanceRider](PassengerControllers.md#balancerider)
- [CustomPassengerBody](PassengerControllers.md#custompassengerbody)
- [CustomPassengerController](PassengerControllers.md#custompassengercontroller)
- [HumanoidPassenger](PassengerControllers.md#humanoidpassenger)
- [IPassengerModule](PassengerControllers.md#ipassengermodule)
- [PassengerAnimatorLayers](PassengerControllers.md#passengeranimatorlayers)
- [PassengerAnimatorLayers.Layer](PassengerControllers.md#passengeranimatorlayerslayer)
- [PassengerAttachmentMode](PassengerControllers.md#passengerattachmentmode)
- [PassengerBehaviour](PassengerControllers.md#passengerbehaviour)
- [PassengerBody](PassengerControllers.md#passengerbody)
- [PassengerController](PassengerControllers.md#passengercontroller)
- [PassengerControllerType](PassengerControllers.md#passengercontrollertype)
- [PassengerExitReason](PassengerControllers.md#passengerexitreason)
- [PassengerHandleVariant](PassengerControllers.md#passengerhandlevariant)
- [PassengerJointSupport](PassengerControllers.md#passengerjointsupport)
- [PassengerJointSupportState](PassengerControllers.md#passengerjointsupportstate)
- [PassengerModule](PassengerControllers.md#passengermodule)
- [PassengerPhysicalAnimationSettings](PassengerControllers.md#passengerphysicalanimationsettings)
- [Passengers](PassengerControllers.md#passengers)
- [PassengerSeat](PassengerControllers.md#passengerseat)
- [PassengerSeatContext](PassengerControllers.md#passengerseatcontext)
- [PassengerTransformSupport](PassengerControllers.md#passengertransformsupport)
- [PassengerType](PassengerControllers.md#passengertype)
- [PassengerVariant](PassengerControllers.md#passengervariant)
- [PassengerVariants](PassengerControllers.md#passengervariants)
- [RagdollPhysicsPassengerController](PassengerControllers.md#ragdollphysicspassengercontroller)
- [RiderAirControl](PassengerControllers.md#rideraircontrol)
- [RiderAnimationRule](PassengerControllers.md#rideranimationrule)
- [RiderAnimator](PassengerControllers.md#rideranimator)
- [RiderBlendSource](PassengerControllers.md#riderblendsource)
- [RiderCorneringPosture](PassengerControllers.md#ridercorneringposture)
- [RiderFootMode](PassengerControllers.md#riderfootmode)
- [RiderKneeLean](PassengerControllers.md#riderkneelean)
- [RiderMotionCondition](PassengerControllers.md#ridermotioncondition)
- [RiderMotionState](PassengerControllers.md#ridermotionstate)
- [RiderPushFeet](PassengerControllers.md#riderpushfeet)
- [RiderReverseMode](PassengerControllers.md#riderreversemode)

## AnimatorIKPassengerController

**Runtime/World/Passengers/Controllers/AnimatorIKPassengerController.cs**

Configuration/implementation type for animator ikpassenger controller within seats, bodies and controller strategies.

**Inherits / implements:** [PassengerController](PassengerControllers.md#passengercontroller).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override PassengerControllerType Type { get; }` | Read-only/resolved type for `AnimatorIKPassengerController`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `body` — Character or rigidbody context, according to the declared type. `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |

## AnimatorPassengerController

**Runtime/World/Passengers/Controllers/AnimatorPassengerController.cs**

Configuration/implementation type for animator passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** [PassengerController](PassengerControllers.md#passengercontroller).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override PassengerControllerType Type { get; }` | Read-only/resolved type for `AnimatorPassengerController`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `body` — Character or rigidbody context, according to the declared type. `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |

## AttachOnlyPassengerController

**Runtime/World/Passengers/Controllers/AttachOnlyPassengerController.cs**

Configuration/implementation type for attach only passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** [PassengerController](PassengerControllers.md#passengercontroller).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override PassengerControllerType Type { get; }` | Read-only/resolved type for `AttachOnlyPassengerController`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `body` — Character or rigidbody context, according to the declared type. `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |

## BalanceRider

**Runtime/World/Passengers/Seats/BalanceRider.cs**

Configurable foot poses and optional physical rider support for seated or standing riders on motorcycles, bicycles, scooters and other vehicles.

**Inherits / implements:** [PassengerBehaviour](PassengerControllers.md#passengerbehaviour).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<Vector2> BodyLeanChanged` | Requested torso lean changes: X forward, Y sideways, in degrees. |
| `public event Action<PassengerBodyPart> FootLifted` | A foot leaves its support phase, including riding, flight, damage, disable or loss of occupancy. |
| `public event Action<PassengerBodyPart> FootPlanted` | Resolved support-phase entry at rest, while stepping, or in inside/fallen support; emitted once on the edge. |
| `public event Action<bool> FootPushingChanged` | Rider motion configuration or signal; see the setup guide. |
| `public event Action<RiderMotionState> MotionUpdated` | Rider motion configuration or signal; see the setup guide. |
| `public event Action<float> RidingBlendChanged` | Effective ground-to-riding target blend changes. |
| `public UnityEvent<Vector2> onBodyLeanChanged` | Inspector counterpart of BodyLeanChanged. |
| `public UnityEvent<PassengerBodyPart> onFootLifted` | Inspector counterpart of FootLifted. |
| `public UnityEvent<PassengerBodyPart> onFootPlanted` | A foot reaches its resolved support phase at rest, while stepping, or during turn/recovery support. These are target-state signals, not foot collision reports. |
| `public UnityEvent<bool> onFootPushingChanged` | Foot propulsion begins or stops; false is also published on disable or loss of occupancy. |
| `public UnityEvent<RiderMotionState> onMotionUpdated` | Current motion state after rider targets update. Suitable for custom animation integrations. |
| `public UnityEvent<float> onRidingBlendChanged` | Inspector counterpart of RidingBlendChanged. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public RiderAirControl airControl` | Optional driver weight transfer in flight. Uses dedicated Command.AirRoll and Command.AirPitch inputs, independently of throttle, steering and aircraft controls. Initial value: `new RiderAirControl()`. |
| `public bool allowFootPushing` | Let this occupied driver provide ground foot targets and provide foot propulsion in Foot Pushing mode with any wheel-driven profile. Passengers never propel the vehicle. |
| `public float balanceDamper` | Relative pelvis/chassis angular damping in Nm per rad/s. Nonnegative; default 25. |
| `public float balanceSpring` | Torso support stiffness in Nm/rad. Nonnegative; default 250. |
| `public RiderBlendSource blendSource` | Choose speed-driven posture transition or a manual blend value. Default Speed. |
| `public float blendSpeed` | Rate of the normalized transition between feet-down and riding poses per second. Initial value: `4`. |
| `public virtual bool CanPushWithFeet { get; }` | Whether the occupied driver can use the selected ground feet after lowering the legs. False during active wheel lift and controlled lowering. |
| `public RiderCorneringPosture corneringPosture` | Smooth torso transfer into riding turns and counterbalance during slow parking turns. Requires Support Balance; enabled by default. Published through rider motion/lean notifications. |
| `public float fallenFootMaximumSpeed` | Maximum road speed in m/s for falling/recovery foot support, with fading through the upper quarter of the range. Default `3`. |
| `public float fallenFootStartLean` | World side bank in degrees where recovery-foot support starts, reaching full weight twenty degrees later. Established recovery keeps the foot available until the bank falls below ten degrees. Default `40`. |
| `public bool fallenFootSupport` | Extend the lower-side foot during grounded falls and recovery, independently of insideFootSupport. Reuses tire contacts or a fresh chassis ground contact; remains inactive in free flight. Riding feet may lower during recovery; Unchanged and handle-owned bindings remain untouched. Default `true`. |
| `public float footGroundClearance` | Ankle offset above the sampled ground plane in metres. |
| `public float footGroundSmoothTime` | Shared wheel support plane smoothing time in seconds; default 0.08, zero disables smoothing. |
| `public float footMotionSmoothTime` | Physical target smoothing time in seconds; default 0.06, zero disables smoothing. |
| `public float footPushTorque` | Total backward wheel torque in Nm representing the driver's foot pushes, independent of engine power. |
| `public float footReverseEngageSpeed` | Maximum ground speed in m/s for starting foot pushing. Sideways or backward coasting must finish braking first. |
| `public float footReverseSpeed` | Maximum foot-propelled reverse speed in metres per second. |
| `public float footStartBlendTime` | Seconds to blend the supported foot pose into walking; default 0.12. |
| `public float footStepDistance` | Recovery step distance in metres, relative to the ground pose. |
| `public float footStepHeight` | Foot lift in metres during the recovery part of each step. |
| `public float footStepPeriod` | Maximum seconds for a full left/right pair of steps; shortens at higher reverse speed to keep planted feet within reach. Shared by physical targets and animation signals. |
| `public float forwardLean` | Forward/backward target stance lean relative to the pelvis/backrest frame, degrees; clamped -60..60. Default 0. |
| `public float fullyRaisedAtKph` | Fully raised at in km/h (stored value); Speed fields display the selected speed unit. Initial value: `8`. |
| `public float insideFootBlendTime` | Seconds to deploy or withdraw support; the old foot withdraws before the opposite one deploys. Default `.2`. |
| `public float insideFootBrakingMaximumSpeed` | Higher inside-foot support speed in m/s during braking into a banked turn; blends from the ordinary limit between 8 and 20 degrees of bank. Default `12`. |
| `public float insideFootMaximumSpeed` | Maximum ground speed in m/s; support fades through the upper quarter of the range. Default `8`. |
| `public float insideFootSteeringThreshold` | Steering magnitude at which inside-foot support begins. Default `.25`. |
| `public bool insideFootSupport` | Enable compliant inside-foot support during slow tight braking turns and burnouts; demo motorcycle driver enables it. Requires SpeedBlend ground and riding anchors; excludes flight, reverse, wheel lift and foot pushing. Default `true`. |
| `public RiderKneeLean kneeLean` | Optional smooth inside-knee extension into the banked turn. Enabled by default; physical joint supports and IK poles use the same target. |
| `public Transform leftFootGround` | Assign the left foot ground reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public RiderFootMode leftFootMode` | Left-foot pose policy: SpeedBlend, Riding, Ground or Unchanged. Default SpeedBlend. |
| `public Transform leftFootRiding` | Assign the left foot riding reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float liftStartsAtKph` | Lift starts at in km/h (stored value); Speed fields display the selected speed unit. Initial value: `1`. |
| `public bool lowerFeetWhenStopped` | Allows ground support for this driver or passenger; default true. Disabled overrides Ground/SpeedBlend with Riding. Does not enable passenger propulsion. |
| `public float manualRidingBlend` | Requested Ground-to-Riding progress, clamped 0..1, when the source is Manual. Transition rate remains Blend Speed. |
| `public float maximumBalanceTorque` | Cap on the added pelvis torque in Nm. Nonnegative; default 120. Zero applies no torque. |
| `public RiderMotionState MotionState { get; }` | Current resolved rider motion. |
| `public bool motorcycleProfileOnly` | Run this rider behaviour only while the vehicle uses `MotorcycleProfile`. Disable to use it with another drive profile. Default false on new components; existing serialized restrictions are preserved. |
| `public bool PushesLeftFoot { get; }` | Whether left foot propulsion is selected. |
| `public bool PushesRightFoot { get; }` | Whether right foot propulsion is selected. |
| `public RiderPushFeet pushFeet` | Both alternates the feet. Left or Right lets a scooter keep the other foot on its riding/deck target. Disabled prevents foot propulsion. |
| `public bool releaseFootPinsOnGround` | Use spring support while feet are lowered, keeping authored position pins for fully raised riding/pedal targets. Prevents planted legs from rigidly pulling against the seated pelvis. |
| `public RiderReverseMode reverseMode` | Reverse Gear keeps normal transmission behavior. Foot Pushing selects neutral and uses bounded human-effort wheel torque while an occupied driver can reach the ground. |
| `public virtual float RidingBlend { get; protected set; }` | Read-only/resolved riding blend for `BalanceRider`. |
| `public Transform rightFootGround` | Assign the right foot ground reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public RiderFootMode rightFootMode` | Independent right-foot policy. Default SpeedBlend. |
| `public Transform rightFootRiding` | Assign the right foot riding reference used by BalanceRider. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public float steeringLean` | Additional signed rider side lean at full steering input, degrees; clamped -45..45. Default 0. |
| `public bool supportBalance` | Apply bounded upper-torso support to an occupied humanoid ragdoll. Uses the chest harness goal when present, otherwise physical torque. Default false; does not balance the vehicle. |
| `public bool useWheelGroundPlane` | Project walking targets onto the existing wheel support plane, without additional raycasts. |
| `public float wheelieSteeringLeanScale` | Fraction of additional rider steering lean retained during wheel lift and controlled lowering. Initial value: `.2f`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool AppliesTo(VehicleController vehicle)` | Checks whether this passenger behavior should run for the supplied seat/role. | `vehicle` — Vehicle context/owner receiving the operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public override void ResetPassenger(Passengers core)` | Resets this passenger behavior's state for the supplied seat. | `core` — Owning audio or passenger core supplying shared context. |
| `public virtual void SetBalanceSupport(bool enabled)` | Enables/disables the existing bounded ragdoll torso support and clears its previous reference when the policy changes. | — |
| `public virtual void SetBodyLean(float forward, float steering)` | Sets desired forward lean (-60..60 degrees) and steering lean (-45..45 degrees), ignoring non-finite components. Uses existing support; does not directly rotate the vehicle. | — |
| `public virtual void SetFootModes(RiderFootMode left, RiderFootMode right)` | Chooses ground/riding/speed-blend/unchanged policy independently for both feet. Invalid enum values leave both unchanged. | — |
| `public virtual void SetFootTargets(Transform leftGround, Transform rightGround, Transform leftRiding, Transform rightRiding)` | Releases old borrowed foot targets, assigns separate ground/riding anchors and binds the current rider again. Null anchors disable the corresponding optional target. | — |
| `public virtual void SetGroundSupport(bool enabled)` | Enables ground foot support or keeps the feet on riding supports; refreshes current targets immediately. | `enabled` — Per-occupant ground-support policy. |
| `public virtual void SetRidingBlend(float value)` | Selects Manual source and clamps the requested riding blend to 0..1. Existing Blend Speed still smooths the actual transition; ignores non-finite input. | — |
| `public virtual void UseSpeedBlend()` | Returns foot positioning to the authored speed-dependent blend policy. | — |

## CustomPassengerBody

**Runtime/World/Passengers/Bodies/CustomPassengerBody.cs**

Minimal body for application-owned Custom occupancy.

**Inherits / implements:** [PassengerBody](PassengerControllers.md#passengerbody).

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Attach(PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public override bool CanEnter(PassengerSeat seat)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. | `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. | `seat` — Seat context whose admission/occupancy rules remain authoritative. `controller` — Controller, interpreted by this operation in the declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public override void Detach(PassengerExitReason reason)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | `reason` — Reason for occupancy release, used by controller/body cleanup policy. |

## CustomPassengerController

**Runtime/World/Passengers/Controllers/CustomPassengerController.cs**

Configuration/implementation type for custom passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** [PassengerController](PassengerControllers.md#passengercontroller).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override PassengerControllerType Type { get; }` | Read-only/resolved type for `CustomPassengerController`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `body` — Character or rigidbody context, according to the declared type. `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public override void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | `body` — Character or rigidbody context, according to the declared type. `reason` — Reason for occupancy release, used by controller/body cleanup policy. `preservePose` — Whether this handover must retain the current character pose. |

## HumanoidPassenger

**Runtime/World/Passengers/Bodies/HumanoidPassenger.cs**

Connects humanoid rig, pose and physical passenger behavior.

**Inherits / implements:** [PassengerBody](PassengerControllers.md#passengerbody).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<HumanoidPassenger> AfterSeatedIK` | Immediately after seated IK work. Payload: `HumanoidPassenger`. |
| `public event System.Action<HumanoidPassenger> BeforeSeatedIK` | Immediately before seated IK work. Payload: `HumanoidPassenger`; custom pose inputs must respect the selected character owner. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public HumanoidJointDefinition[] anatomicalJoints` | Configured skeletal joints and reference data used by IK. Tune axes, anchors and limits on each `ConfigurableJoint` component. |
| `public Animator animator` | Inspector configuration. |
| `public virtual ConfigurableJoint[] authoredRagdollJoints { get; }` | Joint components from the anatomical configuration. |
| `public bool automaticSeatedIK` | Apply seated IK in `LateUpdate`: all configured limbs in Animator + IK, or only forced limbs in Animator. Disable to call `SolveSeatedIK` from your own animation pipeline. |
| `public float exitCollisionClearance` | Keep the previous vehicle excluded until the departing character clears its combined collider bounds by this distance. Prevents animated kinematic limbs from blocking the doors/chassis. |
| `public float freeRagdollAngularDamping` | Passive rotational damping while falling or lying down. Does not hold a pose or freeze bones. |
| `public CollisionDetectionMode freeRagdollCollisionDetection` | Collision detection used by released ragdoll bodies. Defaults to Continuous Dynamic; restored to the previous mode on attachment. |
| `public float freeRagdollInertiaScale` | Rotational inertia multiplier while released. Defaults to `4`; reduces abrupt limb rotation without changing mass or linear momentum and restores the original inertia on attachment. |
| `public float freeRagdollJointDamping` | Passive damping of relative bone rotation. The pose spring stays zero, so joints never return to a riding/idle pose. |
| `public float freeRagdollMaximumAngularSpeed` | Maximum angular speed of released bones in radians/second. Defaults to `18`; preserves lower per-body limits and restores previous limits on attachment. |
| `public float freeRagdollMaximumDampingTorque` | Force/torque budget for free ragdoll maximum damping torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `20`. |
| `public float freeRagdollMaximumDepenetrationVelocity` | Maximum separation speed for overlapping free-ragdoll colliders, in m/s. Defaults to `3`; preserves lower per-body limits and restores previous limits on attachment. |
| `public bool freeRagdollPreprocessing` | Enable joint preprocessing for free ragdolls. Leave off when impacts pin bones against the ground: preprocessing incompatible contact/joint constraints can sustain head oscillations. |
| `public int freeRagdollSolverIterations` | Minimum position solver iterations while the character is a free ragdoll. Initial value: `24`. |
| `public int freeRagdollSolverVelocityIterations` | Minimum velocity solver iterations while the character is a free ragdoll. Initial value: `8`. |
| `public Transform headCameraAnchor` | Optional eye-level child of the head bone, +Z forward and +Y up, used by Interior Camera pinning. Demo mannequins assign an explicit Head Camera Anchor. |
| `public HumanoidIK ik` | Assign the ik HumanoidIK component/asset used by HumanoidPassenger. |
| `public virtual bool IsRagdollActive { get; protected set; }` | Current is ragdoll active predicate; read it instead of maintaining a second application flag. |
| `public Transform pelvis` | Character pelvis bone used to place and support the seated body. |
| `public PassengerPhysicalAnimationSettings physicalAnimation` | Blending and finite muscle forces for Animator-driven limbs while the passenger is physically simulated. Animator layers and Avatar Masks compose the target pose. |
| `public bool physicalWhileSeated` | Keeps the seated skeleton physically simulated rather than attaching it as a kinematic character. |
| `public Rigidbody[] ragdollBodies` | Assign the ragdoll bodies references used by HumanoidPassenger. Entries are processed in list order. Initial value: `System.Array.Empty<Rigidbody>()`. |
| `public virtual int RestraintCount { get; }` | Read-only/resolved restraint count for `HumanoidPassenger`. |
| `public virtual Animator SeatedAnimator { get; }` | Read-only/resolved seated animator for `HumanoidPassenger`. |
| `public virtual bool SoftHarness { get; }` | Read-only/resolved soft harness for `HumanoidPassenger`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ActivateRagdoll()` | Hands the character to free skeletal physics, releasing seated pose ownership. | — |
| `public override void AddVelocity(Vector3 velocityChange)` | Adds the supplied velocity change to the character bodies used by this body implementation. | — |
| `public override bool Attach(PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | — |
| `public virtual void BlendIntoPhysics(float seconds, Transform referenceFrame = null)` | Blend the captured animated pose into physical ownership over the requested seconds, optionally relative to a reference frame. | — |
| `public override bool CanEnter(PassengerSeat seat)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. | — |
| `public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. | — |
| `public override void Detach(PassengerExitReason reason)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | — |
| `public override void DetachForTransition()` | Releases seated ownership for an animated character handover while preserving the required transition pose. | — |
| `public virtual ConfigurableJoint GetAnatomicalJoint(string jointId)` | Returns the native ConfigurableJoint for a unique live ID, or null when unresolved/ambiguous. | — |
| `public virtual void PrepareRagdollCollisions()` | Prepares the character's skeletal collision exclusions and collision relays. | — |
| `public virtual void PreviewAccessPose(PassengerSeat seat)` | Applies an access reference pose for character/seat authoring or transition preparation. | — |
| `public virtual void ReadAnatomicalJointSettings()` | Reads saved native joint configuration into the character's runtime anatomical references. | — |
| `public virtual void RefreshSeatSettings()` | Rebuilds seated limb physics/tuning in place or solves controlled seated IK. Does not teleport or reset the whole body. No-op while unseated. | — |
| `public override void ResetSeatedPose()` | Restores the character's seated pose/support through the selected physical/animation path. | — |
| `public virtual void RestoreAccessReferencePose()` | Restores the character pose retained for an access-motion handover. | — |
| `public virtual void SolveSeatedIK()` | Applies the seated character's configured limb IK targets. | — |
| `public override void StepSeated(Passengers core, float deltaTime)` | Advances this body's seated behavior through its selected character path. | — |
| `public virtual bool TryGetAnatomicalJoint(string jointId, out ConfigurableJoint joint)` | Returns true and the native ConfigurableJoint for a unique live ID; otherwise false and null. Lookup allocates no managed memory. | — |
| `public virtual bool TryGetAnatomicalJointDefinition(string jointId, out HumanoidJointDefinition definition)` | Returns the unique definition with a live joint for the case-sensitive ID; false/null for empty, missing, duplicate or destroyed entries. | — |
| `public virtual bool UpdateAnatomicalJoint(string jointId, System.Action<ConfigurableJoint> update)` | Runs the callback on a uniquely resolved joint, then refreshes its cached anatomy/IK data. False for unresolved ID or null callback. Callback exceptions propagate after cache refresh. | — |

## IPassengerModule

**Runtime/Contracts/Passengers/IPassengerModule.cs**

Configuration/implementation type for ipassenger module within seats, bodies and controller strategies.

**Inherits / implements:** [IWorldModule](Modules.md#iworldmodule).

## PassengerAnimatorLayers

**Runtime/World/Passengers/Controllers/PassengerAnimatorLayers.cs**

Seat-scoped ownership of configured Animator overlay weights. Masks remain controller authoring assets. [Inspector setup](../HandleAnimation.md#masked-animator-layers).

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public RuntimeAnimatorController controller` | Controller edited by Inspector authoring actions; does not switch the occupant's controller. |
| `public List<Layer> layers` | Configured overlay names, masks, enabled flags and weights. |
| `public PassengerSeat seat` | Seat whose humanoid supplies the active Animator, including its physical pose source. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void Apply()` | Resolves the current occupant and applies weights. Missing occupants/layers and Base Layer are skipped. | No result. Automatically called during Update while enabled. |
| `public void RefreshBindings()` | Restores previous weights and rebuilds the binding immediately. | No result. |
| `public bool SetLayerEnabled(string layerName, bool value)` | Mutes a configured overlay or restores its requested weight. | Returns false for an unknown configuration name. |
| `public bool SetWeight(string layerName, float weight)` | Sets a configured request, clamped to 0..1, and applies it when possible. | Returns false for an unknown configuration or non-finite weight; does not imply an occupant is present. |

## PassengerAnimatorLayers.Layer

**Runtime/World/Passengers/Controllers/PassengerAnimatorLayers.cs**

Serializable configuration entry owned by PassengerAnimatorLayers.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool enabled` | True by default; false mutes this overlay without losing its requested weight. |
| `public AvatarMask mask` | Authoring mask saved with the Inspector Apply action. Null permits the whole body. |
| `public string name` | Existing overlay layer name; Base Layer is excluded. |
| `public float weight` | Requested blend weight, initially 1. |

## PassengerAttachmentMode

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Main attachment policy on PassengerSeat. `Spring = 0` retains selected controller behavior and is the default. `Parent = 1` attaches the main origin to Spine Anchor independently of ragdoll state. Physical humanoids retain their ragdoll with only the pelvis held. Custom retains automatic main attachment ownership.

## PassengerBehaviour

**Runtime/World/Passengers/Core/PassengerBehaviour.cs**

Configuration/implementation type for passenger behaviour within seats, bodies and controller strategies.

**Inherits / implements:** [PassengerModule](PassengerControllers.md#passengermodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public PassengerSeat seat` | Assign the seat PassengerSeat component/asset used by PassengerBehaviour. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool AppliesTo(VehicleController vehicle)` | Checks whether this passenger behavior should run for the supplied seat/role. | `vehicle` — Vehicle context/owner receiving the operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public sealed override void StepPassenger(Passengers core, float deltaTime)` | Advances passenger work in the supplied seat/core context. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## PassengerBody

**Runtime/World/Passengers/Bodies/PassengerBody.cs**

Base character adapter used by seats and controller strategies.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual bool IsCustomControlled { get; protected set; }` | Current is custom controlled predicate; read it instead of maintaining a second application flag. |
| `public virtual bool IsExternallyControlled { get; protected set; }` | Current is externally controlled predicate; read it instead of maintaining a second application flag. |
| `public virtual PassengerSeat Seat { get; protected set; }` | Read-only/resolved seat for `PassengerBody`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void AddVelocity(Vector3 velocityChange)` | Adds the supplied velocity change to the character bodies used by this body implementation. | `velocityChange` — World velocity change in m/s. |
| `public abstract bool Attach(PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual bool CanEnter(PassengerSeat seat)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. | `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual bool CanEnter(PassengerSeat seat, PassengerControllerType controller)` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements. | `seat` — Seat context whose admission/occupancy rules remain authoritative. `controller` — Controller, interpreted by this operation in the declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public abstract void Detach(PassengerExitReason reason)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | `reason` — Reason for occupancy release, used by controller/body cleanup policy. |
| `public virtual void DetachForTransition()` | Releases seated ownership for an animated character handover while preserving the required transition pose. | No arguments; no returned value. |
| `public virtual void ResetSeatedPose()` | Restores the character's seated pose/support through the selected physical/animation path. | No arguments; no returned value. |
| `public virtual void StepSeated(Passengers core, float deltaTime)` | Advances this body's seated behavior through its selected character path. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## PassengerController

**Runtime/World/Passengers/Controllers/PassengerController.cs**

Per-seat strategy for body attachment, detachment and stepping; the seat retains occupancy authority.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public abstract PassengerControllerType Type { get; }` | Read-only/resolved type for `PassengerController`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public abstract bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `body` — Character or rigidbody context, according to the declared type. `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public static PassengerController Create(PassengerControllerType type)` | Creates the built-in strategy for a `PassengerControllerType`; seat factory overrides can substitute application strategies. | `type` — Type, interpreted by this operation in the declared type. **Returns:** Returned `PassengerController`; ownership remains as specified by the creating/lookup operation. |
| `public virtual void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | `body` — Character or rigidbody context, according to the declared type. `reason` — Reason for occupancy release, used by controller/body cleanup policy. `preservePose` — Whether this handover must retain the current character pose. |
| `public virtual void Step(PassengerBody body, Passengers core, float deltaTime)` | Empty base passenger strategy step; derived strategies decide which body work they own. | `body` — Character or rigidbody context, according to the declared type. `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## PassengerControllerType

**Runtime/World/Passengers/Controllers/PassengerController.cs**

Defines the allowed passenger controller type choices used by this topic.

### Values

- `RagdollPhysics = 0`
- `Animator = 1`
- `[InspectorName("Animator + IK")] AnimatorIK = 2`
- `AttachOnly = 3`
- `Custom = 4`

## PassengerExitReason

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Defines the allowed passenger exit reason choices used by this topic.

### Values

- `Exit`
- `Ejected`
- `Disabled`
- `Destroyed`

## PassengerHandleVariant

**Runtime/World/Passengers/Presentation/PassengerVariant.cs**

Per-handle animation/IK policy borrowed by one presentation. Shared handles affect all of their users.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleHandle handle` | Shared vehicle handle whose presentation policy changes with this variant. Control values and physical model motion are retained. |
| `public HandleControlMode mode` | Handle animation/IK policy for this presentation. |

## PassengerJointSupport

**Runtime/World/Passengers/Seats/PassengerJointSupport.cs**

Serializable seat-owned support settings. Anatomical constraints remain active; these settings add forces rather than editing limits or creating another native joint.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool active` | Enables this entry, default true. Inactive entries exert no force or torque. |
| `public Transform anchor` | Target world pose, normally an empty child of the vehicle. Missing target means no support. |
| `public float damper` | Relative point velocity damping in N/(m/s), default 30. Includes target movement. |
| `public bool holdRotation` | Also aligns the joint body to the target orientation. Default false; point-only support leaves angular freedom. |
| `public string jointId` | Exact Anatomical Joints ID of the occupant. Case-sensitive; duplicates in the seat or occupant are skipped. |
| `public Vector3 localOffset` | Body-local offset added to the native joint anchor. Zero holds the anatomical pivot itself. |
| `public float maximumForce` | Combined position spring/damping force cap in N, default 300. Zero disables positional support. |
| `public float maximumTorque` | Combined angular spring/damping torque cap in Nm, default 40. Zero disables angular support. |
| `public float rotationDamper` | Relative angular velocity damping in Nm/(rad/s), default 10. |
| `public Vector3 rotationOffset` | Desired body rotation relative to the anchor in degrees; default zero. |
| `public float rotationSpring` | Angular stiffness in Nm/rad, default 100. |
| `public float spring` | Position stiffness in N/m, default 500. Pulls the supported point toward the target. |

## PassengerJointSupportState

**Runtime/World/Passengers/Seats/PassengerJointSupport.cs**

Read-only snapshot of the last applied calculation; positions use metres and vectors use world axes. Read with PassengerSeat.TryGetJointSupportState. It is not an accumulated impulse or measured joint reaction.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public readonly Rigidbody Body` | Dynamic body on the anatomical joint’s GameObject. |
| `public readonly Vector3 Force` | Clamped world force in N passed to AddForceAtPosition. |
| `public readonly ConfigurableJoint Joint` | Resolved anatomical joint; never replaced or reconfigured by the support. |
| `public readonly Vector3 Point` | Supported world point at calculation time, including the joint anchor and local offset. |
| `public readonly Vector3 TargetPosition` | Target world position used by the last support calculation. |
| `public readonly Vector3 Torque` | Clamped world torque in Nm passed to AddTorque; zero when rotation support is off. |

## PassengerModule

**Runtime/World/Passengers/Core/PassengerModule.cs**

Configuration/implementation type for passenger module within seats, bodies and controller strategies.

**Inherits / implements:** [WorldModule](Modules.md#worldmodule), [IPassengerModule](PassengerControllers.md#ipassengermodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void PreparePassenger(Passengers core, PassengerSeat seat)` | Prepares this passenger behavior for an occupied seat. | `core` — Owning audio or passenger core supplying shared context. `seat` — Seat context whose admission/occupancy rules remain authoritative. |
| `public virtual void RenderPassenger(Passengers core)` | Advances render-time passenger presentation owned by this behavior/core. | `core` — Owning audio or passenger core supplying shared context. |
| `public virtual void ResetPassenger(Passengers core)` | Resets this passenger behavior's state for the supplied seat. | `core` — Owning audio or passenger core supplying shared context. |
| `public sealed override void Step(VehicleController vehicle, Command command, float deltaTime)` | Intentionally empty sealed module-pipeline entry point. Passenger-local work runs through `StepPassenger`/`RenderPassenger` under Passengers. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void StepPassenger(Passengers core, float deltaTime)` | Advances passenger work in the supplied seat/core context. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## PassengerPhysicalAnimationSettings

**Runtime/World/Passengers/Bodies/PassengerPhysicalAnimationSettings.cs**

Muscle strength, damping and blend settings for Animator-driven limbs on a physical passenger.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float blendDuration` | Seconds used to blend from the current physical limb pose when animation takes ownership. |
| `public float jointDamper` | Anatomical joint pose damping. |
| `public float jointSpring` | Anatomical joint pose spring strength. |
| `public float maximumForce` | Maximum muscle force in newtons per axis. The reaction acts on the passenger pelvis, not an immovable world anchor. |
| `public float maximumJointTorque` | Maximum anatomical joint muscle torque in newton metres. |
| `public float maximumTorque` | Maximum end-orientation muscle torque in newton metres per axis. |
| `public float positionDamper` | End-position muscle damping. |
| `public float positionSpring` | End-position muscle spring strength. |
| `public float rotationDamper` | End-orientation muscle damping. |
| `public float rotationSpring` | End-orientation muscle spring strength. |
| `public float weight` | Contribution of the composed Animator pose to physical limbs. Zero releases animation muscle drives; it does not change IK or free limbs. |

## Passengers

**Runtime/World/Passengers/Core/Passengers.cs**

Discovers owned handles and supplies input before seat work.

**Inherits / implements:** [WorldModule](Modules.md#worldmodule).

### Vehicle shortcut

Use `vehicle.passengers` for the first registered `Passengers` module. It can be null and does not automatically enable a disabled module. `Seats` is a cloned array snapshot; cache it for repeated enumeration. Immediate TryEnter/TryExit on this core do not play access motion; see [the usage and boarding distinction](../Passengers.md#access-the-passenger-system-from-a-vehicle).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<PassengerSeatContext> AfterEject` | After ejected detachment and the requested built-in velocity change. Custom controllers retain their application-owned physics. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterEnter` | After successful attachment and existing Entered notifications. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterExit` | After detachment and existing Exited notifications. During ejection this precedes the extra velocity change. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeEject` | Before any ejection detachment, while the seat is still occupied. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeEnter` | After admission validation, before occupancy assignment and controller attachment. Occupant and Passenger.Seat are still empty. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeExit` | While the passenger still owns the seat, before detachment. Includes ordinary exit, ejection, disable and destruction. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeat, PassengerBody> Entered` | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat. |
| `public event Action<PassengerSeat, PassengerBody, PassengerExitReason> Exited` | After occupancy is released. Payload identifies occupant and `PassengerExitReason`; the core delegate also includes the seat. |
| `public event Action<PassengerSeat, PassengerBody, PassengerBody> OccupantReplaced` | After a committed swap, without occupancy entry/exit. Payload: seat, previous body, replacement body. |
| `public UnityEvent<PassengerSeatContext> onBeforeEject` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerSeatContext> onBeforeEnter` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerSeatContext> onBeforeExit` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerSeatContext> onEjected` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerSeat, PassengerBody> onEntered` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerSeat, PassengerBody, PassengerExitReason> onExited` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual PassengerModule[] PassengerModules { get; }` | Read-only/resolved passenger modules for Passengers. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public virtual PassengerSeat[] Seats { get; }` | Read-only/resolved seats for Passengers. |
| `public bool spawnOnStart` | Creates/adopts the configured occupant(s) at startup when the owning seat/hub is enabled. Initial value: `true`. |
| `public override bool SupportsDirectControl { get; }` | Opts into direct-mode stepping; keeps seated passenger updates available. |
| `public override bool SupportsReleasedForces { get; }` | Keeps passive maintenance/observation active during release; Drive and Engine suppress force output, and TireCollision keeps native solid proxies without supplemental tread forces. |
| `public virtual VehicleController Vehicle { get; protected set; }` | Read-only/resolved vehicle for Passengers. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Rebuilds the owned passenger seats, ordered handles and passenger-local behaviors. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void PrepareOccupant(PassengerSeat seat)` | Prepares a seat's occupant and its local handles/passenger behaviors. | `seat` — Seat context whose admission/occupancy rules remain authoritative. |
| `public virtual void RefreshPassengers()` | Rebuilds the owned seat and passenger-behavior snapshot. Handles use vehicle.handles.Refresh(). | No arguments; no returned value. |
| `public virtual void ResetOccupants()` | Resets eligible owned seated/released occupants through their seat lifecycle. | No arguments; no returned value. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Supplies commands to handles in order, then advances passenger modules and seats from the owned snapshot. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual bool TryEnter(PassengerBody body, PassengerSeat seat = null)` | Routes an entry request through an owned seat/passenger selection and that seat's validation. | `body` — Character or rigidbody context, according to the declared type. `seat` — Seat context whose admission/occupancy rules remain authoritative. Default: `null`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TryExit(PassengerBody body, PassengerExitReason reason = PassengerExitReason.Exit)` | Requests immediate exit or starts animated departure, depending on the declaring owner. | `body` — Character or rigidbody context, according to the declared type. `reason` — Reason for occupancy release, used by controller/body cleanup policy. Default: `PassengerExitReason.Exit`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## PassengerSeat

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

`Entered`, `Exited`, `ControllerChanged` and custom `ResetRequested`

**Inherits / implements:** `MonoBehaviour`.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<PassengerSeatContext> AfterEject` | After ejected detachment and the requested built-in velocity change. Custom controllers retain their application-owned physics. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterEnter` | After successful attachment and existing Entered notifications. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> AfterExit` | After detachment and existing Exited notifications. During ejection this precedes the extra velocity change. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeEject` | Before any ejection detachment, while the seat is still occupied. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeEnter` | After admission validation, before occupancy assignment and controller attachment. Occupant and Passenger.Seat are still empty. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerSeatContext> BeforeExit` | While the passenger still owns the seat, before detachment. Includes ordinary exit, ejection, disable and destruction. Payload: immutable PassengerSeatContext. |
| `public event Action<PassengerBodyPart> BodyPartChanged` | After a supported limb edit or individual damage-release recovery. Payload: affected hand/foot. |
| `public event Action<PassengerSeat, PassengerControllerType, PassengerControllerType> ControllerChanged` | After a successful seat strategy handover. Payload: seat, previous controller type, new controller type; no extra entry/exit is synthesized. |
| `public event Action<PassengerBody> Entered` | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat. |
| `public event Action<PassengerBody, PassengerExitReason> Exited` | After occupancy is released. Payload identifies occupant and `PassengerExitReason`; the core delegate also includes the seat. |
| `public event Action<PassengerBody, PassengerBody> OccupantReplaced` | After a committed swap, without occupancy entry/exit. Payload: previous body and replacement body. Former body is parked inactive; replacement owns the seat. |
| `public event Action<PassengerBody> ResetRequested` | When Custom occupancy receives a reset request. Payload: `PassengerBody`; application owns the actual custom-character reset. |
| `public event Action<Pose> SpinePoseChanged` | After SetSpinePose commits the new anchor-local pose. Payload: position in metres and normalized rotation. |
| `public UnityEvent<PassengerBody> onBeforeEject` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBody> onBeforeEnter` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBody> onBeforeExit` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerControllerType> onControllerChanged` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBody> onEjected` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBody> onEntered` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBody, PassengerExitReason> onExited` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBody> onFeetReleased` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBody> onHandsReleased` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |
| `public UnityEvent<PassengerBodyPart> onLimbReleased` | One callback per newly damage-released limb, under Passenger Seat > Signals and callbacks. |
| `public UnityEvent<PassengerBody> onResetRequested` | Inspector callback under Signals and callbacks; see the lifecycle guide for payload and ordering. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual PassengerControllerType ActiveController { get; }` | Read-only/resolved active controller for `PassengerSeat`. |
| `public bool affectVehiclePhysics` | Allow seated passenger supports to push and rotate the vehicle. Disable for one-way support: the vehicle still drives the passenger, but seat/limb/head joints do not react on the chassis. Passenger-to-vehicle contacts are also excluded while seated; ejection restores normal contact rules. |
| `public float attachmentDamper` | Main non-physical Spring damping; default 20. Captured on refresh. |
| `public PassengerAttachmentMode AttachmentMode { get; }` | Current main attachment mode; default Spring. Set through SetAttachmentMode. |
| `public float attachmentSpring` | Main non-physical Spring stiffness; default 120. Captured on refresh. |
| `public PassengerBody body` | Optional pre-placed body. Leave empty to spawn the prefab. |
| `public PassengerBody bodyPrefab` | Assign the body prefab PassengerBody component/asset used by PassengerSeat. |
| `public virtual PassengerControllerType Controller { get; }` | Read-only/resolved controller for `PassengerSeat`. |
| `public string customTypeId` | Application-defined type for Custom occupants; avoids changing the enum. |
| `public PassengerCollisionSurface[] ejectColliders` | Selected surfaces admitted for the whole ejected passenger. Each entry contains a collider and world/vehicle ignore policies. Call RefreshCollisionSettings after runtime edits. |
| `public bool enableSelfCollidersOnRelease` | Enable self contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. Neighboring skeletal bodies keep collisions disabled. |
| `public bool enableVehicleCollidersOnRelease` | Enable vehicle contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. |
| `public bool excludeSelfCollisionsOnEnter` | Exclude self contacts on entry and while held. Release options may restore them. Disable to keep self contacts enabled, including after regrip and reseating. Native joint collision settings still apply. |
| `public bool excludeVehicleCollisionsOnEnter` | Exclude contacts with the vehicle on entry and while held. Release options may restore them. Disable to keep vehicle contacts enabled, including after regrip and reseating. |
| `public Transform exitAnchor` | Assign the exit anchor reference used by PassengerSeat. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public virtual bool FeetReleasedByDamage { get; }` | Read-only/resolved feet released by damage for `PassengerSeat`. |
| `public PassengerGForceLimits gForceLimits` | Enabled-by-default, live emergency acceleration limits; independent per-seat history. See [G-force limits](../Seats.md#g-force-limits). |
| `public bool GForceProtectionActive { get; }` | Whether temporary overload protection is active for this seat. |
| `public virtual bool HandsReleasedByDamage { get; }` | Read-only/resolved hands released by damage for `PassengerSeat`. |
| `public float headDamper` | Damping relative to chassis angular velocity in Nm per rad/s; default 20. |
| `public float headPitch` | Desired head pitch relative to seat-forward in degrees: negative looks up, positive looks down. Clamped to -60..60; default 0. |
| `public Transform headPositionAnchor` | Optional vehicle-mounted target; empty captures the seated head position relative to the seat. An anchor below the occupant is rejected to avoid self-follow. |
| `public float headPositionDampingRatio` | Head-mass-scaled spring damping ratio; one is critical damping. Initial value: `1`. |
| `public float headPositionFrequency` | Position spring frequency in Hz; higher values resist displacement more strongly. Initial value: `6`. |
| `public float headSpring` | Support stiffness in Nm/rad; default 250. |
| `public bool holdHeadForward` | Enable artificial head support for this occupied Ragdoll Physics seat, independently of drive profile. Default false. |
| `public bool holdHeadPosition` | Add a damped, force-limited head-position spring while an active humanoid occupies a Ragdoll Physics seat. Released on exit/ejection; does not make the head kinematic. Initial value: `false`. |
| `public List<PassengerJointSupport> jointSupports` | Optional extra supports for this seat; empty by default. One entry per anatomical Joint ID. Settings are live and are retained across occupants. |
| `public PassengerFootConfig leftFoot` | Left-foot bone/contact configuration used by the character or seat. Initial value: `new PassengerFootConfig()`. |
| `public PassengerHandConfig leftHand` | Left-hand bone/contact configuration used by the character or handle. Initial value: `new PassengerHandConfig()`. |
| `public float maximumHeadAcceleration` | Maximum support force per kilogram of head mass, in m/s². Initial value: `100`. |
| `public float maximumHeadTorque` | Support torque cap in Nm; default 80. Zero applies no torque. |
| `public virtual PassengerBody Occupant { get; protected set; }` | Body currently admitted to this seat, or `null` when empty. |
| `public bool parentMakeKinematic` | Parent mode temporarily makes the held pelvis Rigidbody kinematic; default true. Other bones keep simulating. |
| `public Vector3 parentPositionOffset` | Parent mode Spine Anchor local position offset. |
| `public Vector3 parentRotationOffset` | Parent mode Spine Anchor local Euler degrees. |
| `public bool parentWhileSeated` | Parents the occupant to the seat hierarchy while attached; physics still follows the selected passenger controller. Initial value: `true`. |
| `public float PassengerGForce { get; }` | Latest sampled gravity-compensated seat acceleration in standard G; cleared on reset/exit. |
| `public virtual bool PassengerReleasedByDamage { get; }` | Read-only/resolved passenger released by damage for `PassengerSeat`. |
| `public PassengerType passengerType` | Chooses the package occupant type to create for the seat. Options: `HumanoidDriver`, `HumanoidPassenger`, `Custom`. Initial value: `PassengerType.HumanoidPassenger`. |
| `public virtual PassengerAccess Reservation { get; protected set; }` | Current seat-access/request reservation identity; reservation does not itself mean occupancy. |
| `public PassengerRestraints restraints` | Pelvis/chest support, damping, release and ejection settings. Expand to configure each policy. Initial value: `new PassengerRestraints()`. |
| `public PassengerFootConfig rightFoot` | Right-foot bone/contact configuration used by the character or seat. Initial value: `new PassengerFootConfig()`. |
| `public PassengerHandConfig rightHand` | Right-hand bone/contact configuration used by the character or handle. Initial value: `new PassengerHandConfig()`. |
| `public string seatId` | Application-facing identifier for this seat. Initial value: `"Passenger"`. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public bool spawnOnStart` | Creates/adopts the configured occupant(s) at startup when the owning seat/hub is enabled. Initial value: `true`. |
| `public Transform spineAnchor` | Pelvis / seated spine origin, facing forward, Y up. |
| `public List<PassengerTransformSupport> transformSupports` | Initially empty independent Spring/Parent binding list. Direct edits require RefreshTransformSupports. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool AddJointSupport(PassengerJointSupport support)` | Adds settings without requiring an occupant. Rejects null, blank IDs and duplicate IDs; an unresolved anatomical ID can be configured before entry. | — |
| `public virtual bool AddTransformSupport(PassengerTransformSupport support)` | Adds a non-null entry with both references, rejects duplicate bodyTransform or nonblank ID, refreshes; true means accepted configuration, not necessarily a resolved binding. | — |
| `public virtual bool Eject(Vector3 velocityChange)` | Requests whole-occupant release through the seat's controller/body lifecycle. | — |
| `public virtual bool EjectFromImpact(Vector3 velocityChange)` | Eject through the standard seat lifecycle and retain automatic reset/reseat ownership. | — |
| `public virtual PassengerBodyPartConfig GetBodyPart(PassengerBodyPart part)` | Returns the seat configuration for a selected limb/body part. | — |
| `public virtual PassengerJointSupport GetJointSupport(string jointId)` | Returns the editable support settings, or null for an unresolved or ambiguous ID. | — |
| `public virtual PassengerTransformSupport GetTransformSupport(string id)` | Returns live settings for a unique ID, otherwise null. | — |
| `public virtual PassengerTransformSupport GetTransformSupport(Transform bodyTransform)` | Returns live settings matching the configured reference, or null for missing/duplicate references. Use the prefab reference for prefab-authored entries. | — |
| `public virtual bool PrepareExitPresentation(PassengerExitReason reason = PassengerExitReason.Exit)` | Applies configured presentation restoration before an exit/ejection. Call before reservation or custom motion, then resolve Occupant again. Does not detach. Lifecycle disable/destroy never activates a parked body. | **Returns:** false if restoration is busy or rejected; true if prepared or no restoration is required. |
| `public virtual void RefreshCollisionSettings()` | Reapplies the seat's collision policy to its current occupant. | — |
| `public virtual void RefreshPassengerSettings()` | Reapplies directly edited limb support settings and transform/collision bindings without detaching or resetting the whole occupant. Busy transactions defer this operation. | — |
| `public virtual void RefreshTransformSupports()` | Restores existing bindings, resolves the current list and applies eligible entries. Empty seats retain settings; all occupied controller/physics combinations can apply explicit bindings. | — |
| `public virtual bool ReleaseLimb(PassengerBodyPart part)` | Releases one eligible limb; false for invalid/already released/ineligible requests. Keeps authored mode/anchor/handle. | — |
| `public virtual void ReleaseReservation(PassengerAccess owner)` | Releases a seat reservation belonging to the supplied reservation owner. | — |
| `public virtual bool RemoveJointSupport(string jointId)` | Removes the uniquely identified support and clears runtime support state. Returns false if unresolved. | — |
| `public virtual bool RemoveTransformSupport(string id)` | Removes a uniquely identified entry and refreshes; false for unresolved IDs. | — |
| `public virtual bool RemoveTransformSupport(Transform bodyTransform)` | Removes all matching configured references and refreshes; false when none match. | — |
| `public virtual void RestoreDamageFeedback()` | Restores the eligible seated limb supports released by damage feedback. | — |
| `public virtual bool RestoreLimb(PassengerBodyPart part)` | Clears damage release for one hand/foot and refreshes its configured support without resetting the other limbs. Returns false if not released, invalid or busy. | — |
| `public virtual bool SetAttachmentMode(PassengerAttachmentMode mode)` | Reattaches an occupied built-in body without occupancy events; returns false for invalid modes, busy access/reservation, transitions or incompatible attachment. Rolls back a rejected attach. Custom only stores the mode. | — |
| `public virtual bool SetAttachmentOffsets(Vector3 position, Vector3 rotation)` | Sets Parent seating-origin position/metre and rotation/degree offsets, then resets that attachment pose. Rejects non-finite values and busy state. | — |
| `public virtual bool SetBodyPartMode(PassengerBodyPart part, PassengerBodyPartMode mode)` | Sets an arbitrary hand/foot control mode and refreshes the current occupant; false for invalid values or busy state. | — |
| `public virtual bool SetBodyPartTarget(PassengerBodyPart part, Transform anchor, VehicleHandle handle = null)` | Replaces one limb anchor and optional handle. Does not change its authored mode; returns false for invalid part or busy state. | — |
| `public virtual void SetCollisionExclusions(bool self, bool vehicle)` | Sets seated self/vehicle collision exclusion policy and updates the occupied character. | — |
| `public virtual void SetHeadSupport(bool enabled, float pitch = 0)` | Enables/disables physical head support and sets pitch clamped to -60..60 degrees. Uses the existing seat head spring, damping and torque limits. | — |
| `public virtual bool SetJointSupportActive(string jointId, bool active)` | Pauses/resumes one support without disabling the seat or changing anatomical joints. Changed state takes effect on the next physics step; deactivation invalidates diagnostics immediately. | — |
| `public virtual bool SetPassengerController(PassengerControllerType type)` | Requests a validated strategy handover for the seat; an incompatible/busy handover can be rejected. | — |
| `public virtual void SetReleaseCollisions(bool self, bool vehicle)` | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb. | — |
| `public virtual void SetReleaseCollisions(PassengerBodyPart part, bool self, bool vehicle)` | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb. | — |
| `public virtual bool SetSpineAnchor(Transform anchor)` | Replaces the seating origin and resets/rebuilds the current seated pose. Rejects null/self/descendant occupant anchors and busy state. Use moving existing anchors for continuous physical adjustment. | — |
| `public virtual bool SetSpinePose(Vector3 localPosition, Quaternion localRotation)` | Sets the existing Spine Anchor local position/rotation, preserving its identity for physical supports. Rejects non-finite/zero quaternion values. Controlled occupants are repositioned immediately; dynamic supports follow their moved anchor. | — |
| `public virtual bool SetTransformSupportActive(string id, bool active)` | Changes active state and refreshes when changed; false for unresolved IDs. | — |
| `public virtual bool SetTransformSupportActive(Transform bodyTransform, bool active)` | Enables/disables a unique entry and refreshes when changed; false if unresolved/duplicate. | — |
| `public virtual bool Spawn()` | Creates/requests the configured passenger representation through the seat's spawn policy. | — |
| `public virtual void StepPassenger(Passengers core, float deltaTime)` | Advances passenger work in the supplied seat/core context. | — |
| `public virtual bool TryEnter(PassengerBody passenger)` | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. | — |
| `public virtual bool TryEnter(PassengerBody passenger, PassengerAccess reservation)` | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. | — |
| `public virtual bool TryExit(PassengerExitReason reason = PassengerExitReason.Exit, bool preservePose = false)` | Releases current occupancy through its active strategy and exit reason; it does not run an animated access sequence. | — |
| `public virtual bool TryGetJointSupport(string jointId, out PassengerJointSupport support)` | Finds exactly one seat support for the case-sensitive anatomical ID. Empty, missing or duplicate IDs return false and null. | — |
| `public virtual bool TryGetJointSupportState(string jointId, out PassengerJointSupportState state)` | Returns the last applied support calculation while the same valid physical occupant, joint and anchor remain available. False/default before the first step, after removal/release or when disabled, invalid or ambiguous. | — |
| `public virtual bool TryGetTransformSupport(string id, out PassengerTransformSupport support)` | Resolves one exact ordinal ID; false and null for blank, missing or duplicate IDs. | — |
| `public virtual bool TryReplaceOccupant(PassengerBody replacement)` | Synchronously replaces the seated body without Entered/Exited events. Replacement must be active, unseated and compatible. Returns false while boarding/reserved/busy or on rejected admission; the previous occupant remains. On success the former body is inactive and unseated. Overload selects controller/attachment; the shorter overload retains current policies. Caller owns both body lifetimes. | — |
| `public virtual bool TryReplaceOccupant(PassengerBody replacement, PassengerControllerType controller, PassengerAttachmentMode attachment)` | Synchronously replaces the seated body without Entered/Exited events. Replacement must be active, unseated and compatible. Returns false while boarding/reserved/busy or on rejected admission; the previous occupant remains. On success the former body is inactive and unseated. Overload selects controller/attachment; the shorter overload retains current policies. Caller owns both body lifetimes. | — |
| `public virtual bool TryReserve(PassengerAccess owner)` | Reserves a seat for an identified access/request owner without establishing occupancy. | — |
| `public virtual bool UpdateBodyPart(PassengerBodyPart part, Action<PassengerBodyPartConfig> update)` | Edits the selected hand/foot configuration, cancels borrowed handle use and refreshes supports/collisions in place. Returns false for invalid part, null edit or a busy transaction. Edit exceptions propagate after refresh. | — |
| `public virtual bool UpdateJointSupport(string jointId, Action<PassengerJointSupport> update)` | Invokes the callback on uniquely resolved settings. Null callbacks or unresolved IDs return false. Clears runtime tracking even if the callback throws; exceptions propagate. Changes apply on the next step. | — |
| `public virtual bool UpdateTransformSupport(string id, Action<PassengerTransformSupport> update)` | Edits a unique entry and refreshes in finally; false for unresolved IDs or null callbacks. Exceptions propagate. Renaming the ID changes subsequent lookup; duplicate edits make ID lookup ambiguous. | — |
| `public virtual bool UpdateTransformSupport(Transform bodyTransform, Action<PassengerTransformSupport> update)` | Updates a unique entry and refreshes in finally; false for missing/duplicate entries or null callback. Callback exceptions propagate. | — |

## PassengerSeatContext

**Runtime/World/Passengers/Seats/PassengerSeatContext.cs**

Immutable value snapshot for seat/core/access lifecycle notifications. References identify the original operation even after detachment or access Target cleanup. Vehicle can be null for a standalone passenger core. Referenced Unity objects can subsequently be destroyed; this is not a deep copy.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public PassengerExitReason? ExitReason { get; }` | Null for entry; release reason for exit/ejection. |
| `public PassengerBody Passenger { get; }` | Original actor. |
| `public bool PreservePose { get; }` | Requested preserve-pose policy; true for animated exit's seat-release operation. |
| `public PassengerSeat Seat { get; }` | Original seat, retained after the actor leaves. |
| `public VehicleController Vehicle { get; }` | Original owning vehicle, or null for a standalone core. |
| `public Vector3 VelocityChange { get; }` | Requested world-space ejection velocity change; zero for ordinary exits and direct TryExit(Ejected). Custom mode does not apply it automatically. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public PassengerSeatContext(VehicleController vehicle, PassengerBody passenger, PassengerSeat seat, PassengerExitReason? exitReason = null, Vector3 velocityChange = default, bool preservePose = false)` | Captures operation identities and release parameters without a managed event-argument allocation. | vehicle/passenger/seat identify the operation; exitReason is null for entry; velocityChange is the world-space ejection delta in m/s; preservePose reports the requested detachment policy. |

## PassengerTransformSupport

Serializable settings in **Runtime/World/Passengers/Seats/PassengerTransformSupport.cs**. Each binding independently chooses Spring or Parent with any controller or physics state. See [setup and lifecycle](../Seats.md#main-attachment-and-rigid-transform-supports).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool active` | Enable this binding; default true. |
| `public Transform anchor` | Vehicle anchor outside the passenger hierarchy. |
| `public Transform bodyTransform` | Root or child transform from Body or Body Prefab; prefab references resolve on the occupant. |
| `public float damper` | Position damping; default 20. |
| `public bool followAnchorRotation` | Default true: follow the live anchor rotation. False: capture the target world rotation on bind/refresh and hold/spring toward it, while position still follows. Preserve World Pose and Rotation Offset still apply. |
| `public string id` | Optional unique ID / Label, also shown in the Inspector entry header. Ordinal case-sensitive API lookup; blank keeps transform-only access. |
| `public bool makeKinematic` | Parent mode temporarily parks only this transform's Rigidbody; default true. |
| `public PassengerAttachmentMode mode` | Independent binding mode; default Parent. |
| `public Vector3 positionOffset` | Anchor-local position offset; default zero. |
| `public bool preserveWorldPose` | Capture current anchor-relative pose before adding offsets; default false. |
| `public float rotationDamper` | Angular damping; default 20. |
| `public Vector3 rotationOffset` | Anchor-local Euler rotation offset in degrees; default zero. |
| `public float rotationSpring` | Angular stiffness; default 120. |
| `public float spring` | Position stiffness; N/m on dynamic rigidbodies, unit virtual mass for transform simulation. Default 120. |

## PassengerType

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Defines the allowed passenger type choices used by this topic.

### Values

- `HumanoidDriver`
- `HumanoidPassenger`
- `Custom`

## PassengerVariant

**Runtime/World/Passengers/Presentation/PassengerVariant.cs**

Serializable presentation configuration. A prefab or registered instance must support its controller. Transform/joint supports remain authored on the seat; unmatched bones/IDs are skipped. Custom controller implementations own their posing/animation/physics.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public PassengerAttachmentMode attachment` | Attachment policy for the variant. Parent offsets are used only with Parent. |
| `public PassengerControllerType controller` | Passenger controller for this variant, independent of the original seat controller. |
| `public PassengerHandleVariant[] handles` | Optional per-handle animation/IK overrides, restored on leaving this variant. Shared handles affect every user of that handle. |
| `public PassengerBodyPartMode leftFoot` | Left foot policy when Override Limb Modes is enabled. |
| `public PassengerBodyPartMode leftHand` | Left hand policy when Override Limb Modes is enabled. |
| `public bool overrideLimbModes` | Override all four limb modes below. Otherwise retain the seat's current limb configuration. |
| `public Vector3 positionOffset` | Variant seating-origin offset in Spine Anchor coordinates, for Parent attachment. |
| `public PassengerBody prefab` | PassengerBody prefab for this presentation, for example an animated arms-only rig. Must support the selected controller. |
| `public PassengerBodyPartMode rightFoot` | Right foot policy when Override Limb Modes is enabled. |
| `public PassengerBodyPartMode rightHand` | Right hand policy when Override Limb Modes is enabled. |
| `public Vector3 rotationOffset` | Variant rotation in Spine Anchor degrees, for Parent attachment. |

## PassengerVariants

**Runtime/World/Passengers/Presentation/PassengerVariants.cs**

Optional presentation coordinator, also available in Add module and Tools > Add Component > Passengers > Presentation. Stores inactive alternative rigs and changes actual seat ownership through the guarded replacement API. Camera automation is optional. Exit and ejection restoration are independently configurable; if off, the departing variant becomes application-owned and the original remains parked for the next Spawn. Persistent vehicle/character identity should live outside interchangeable presentation bodies. If that same variant re-enters the same seat before the parked original is reused by Spawn, its presentation identity and controller/attachment policies are restored inside the entry transaction. FPP/TPP switching then continues to use the same two bodies. Outside lifetime remains application-owned; an unrelated entrant is never adopted as that variant.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<PassengerVariant, PassengerVariant> VariantChanged` | After a successful presentation commit. Payload: previous and current variant; null denotes the original. A variant-owned exit also reports returning to the original policy, without respawning its parked body. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Cameras cameras` | Optional UVS camera core. Empty resolves the seat's vehicle camera core. Custom camera systems call SetFirstPerson/SetVariant directly. |
| `public PassengerVariant CurrentVariant { get; }` | Current profile, or null for the original presentation. |
| `public PassengerVariant firstPerson` | Optional first-person presentation. Empty prefab leaves the ordinary occupant unchanged. |
| `public bool IsFirstPerson { get; }` | True when the current profile is the configured First Person instance. |
| `public bool IsSwitching { get; }` | True during this helper's synchronous swap/restore transaction. |
| `public PassengerBody OriginalBody { get; }` | Original or parked character, otherwise the currently seated body. The helper never owns its lifetime. |
| `public bool restoreOriginalOnEject` | Restore the original body before ejection. Disable only when the variant itself supports your desired outside/ragdoll behavior. |
| `public bool restoreOriginalOnExit` | Optional original-body restoration before ordinary exit; defaults to false. Off lets the active variant leave and parks the original for the next Spawn. |
| `public override bool SupportsDirectControl { get; }` | Presentation selection also works when vehicle motion is application-owned. |
| `public bool swapOnInteriorCamera` | Automatically select First Person while the assigned/vehicle UVS Cameras core owns an active Interior view. Off leaves all switching to your code. |
| `public Func<PassengerVariants, PassengerVariant> VariantSelector { get; set; }` | Optional application condition evaluated each Update or immediately by EvaluateCondition. Takes this helper and returns a profile; null result restores the original. Has priority over built-in camera selection. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool ApplyVariantSettings()` | Reapplies the edited active profile using cached rigs, restoring through the original without a render/physics step. Returns true if already original, false on blocked/invalid settings; a rejected new policy leaves the original safely restored. Use SetFirstPersonPrefab for source-prefab changes. | No arguments; returns success. |
| `public virtual void ClearCachedVariants()` | Destroys only unseated helper-created/explicitly owned instances. Retains the current seated variant and leaves application-owned bodies alive. | — |
| `public virtual bool EvaluateCondition()` | Evaluates VariantSelector immediately, or the built-in active UVS Interior condition when no selector is assigned. Returns success; false means no available/accepted switch. | — |
| `public virtual bool PrepareVariant(PassengerVariant variant)` | Prewarms an inactive cached prefab instance without changing occupancy. Returns false outside Play, with invalid policy or without a prefab/registered instance. | — |
| `public virtual void RefreshCameraBinding()` | Rebinds the optional/vehicle camera core and immediately reevaluates built-in camera selection. Custom cameras use SetFirstPerson, SetVariant or VariantSelector instead. | — |
| `public virtual bool RestoreOriginal()` | Restores the parked original and its borrowed controller, attachment, limb-mode and handle-mode policies in one transaction. True if already original; false if busy, original unavailable or admission rejected. | — |
| `public virtual bool SetFirstPerson(bool enabled)` | Selects the configured FPP profile when enabled is true; restores original when false. Returns whether the operation succeeded. | — |
| `public virtual bool SetFirstPersonPrefab(PassengerBody prefab)` | Restores active FPP first, replaces its optional source and clears inactive caches. Returns false if restoration is blocked. Null disables prefab-based automatic FPP. | — |
| `public virtual bool SetSeat(PassengerSeat value)` | Restores any active original first, then rebinds the target seat. False if restoration is currently blocked. | — |
| `public virtual bool SetVariant(PassengerVariant variant)` | Selects any valid profile synchronously; null restores original. Retains the currently visible variant if the replacement is rejected. Supports cached registered instances without prefab. Requires an enabled helper and occupied seat. No rendered or physics step occurs between body handovers. | — |
| `public virtual bool SetVariantInstance(PassengerVariant variant, PassengerBody instance, bool takeOwnership = false)` | Registers an unseated application-created body for a profile, allowing prefab to be null. Optional takeOwnership lets cache cleanup destroy it; default keeps caller ownership. Rejects original, duplicate, seated and currently active-profile replacements. | — |
| `public virtual bool TryGetVariantBody(PassengerVariant variant, out PassengerBody body)` | Returns the cached/registered body for the profile, or false if unavailable. Does not spawn or activate it. | — |

## RagdollPhysicsPassengerController

**Runtime/World/Passengers/Controllers/RagdollPhysicsPassengerController.cs**

Configuration/implementation type for ragdoll physics passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** [PassengerController](PassengerControllers.md#passengercontroller).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override PassengerControllerType Type { get; }` | Read-only/resolved type for `RagdollPhysicsPassengerController`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool Attach(PassengerBody body, PassengerSeat seat)` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | `body` — Character or rigidbody context, according to the declared type. `seat` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public override void Step(PassengerBody body, Passengers core, float deltaTime)` | Calls the admitted body's `StepSeated` through the physical passenger path. | `body` — Character or rigidbody context, according to the declared type. `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## RiderAirControl

**Runtime/World/Passengers/Riding/Control/RiderAirControl.cs**

Small airborne rider weight shifts from dedicated AirRoll/AirPitch inputs, limited by contact delay, smoothing and angular-speed settings.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float contactDelay` | Airborne time before weight-shift torque becomes available. Filters brief contact chatter. Initial value: `.03f`. |
| `public bool enabled` | Controls enabled for this mechanism. |
| `public bool IsActive { get; private set; }` | Controls is active for this mechanism. |
| `public float maximumAngularSpeed` | Pitch angular speed in radians per second above which input cannot accelerate farther in that direction. Opposite input can still counter rotation. Initial value: `.25f`. |
| `public float maximumRollAngularSpeed` | Independent sideways rotation-speed limit in radians per second; zero disables lateral correction. Initial value: `1.2f`. |
| `public float pitchAcceleration` | Maximum nose-down/up correction in radians per second squared. Forward input moves weight toward the front. Initial value: `.8f`. |
| `public float pitchBodyLean` | Additional ragdoll torso forward/backward lean at full airborne input, in degrees. Initial value: `6`. |
| `public float responseTime` | Seconds to build or release the weight-shift input. Initial value: `.06f`. |
| `public float rollAcceleration` | Maximum sideways correction in radians per second squared. Initial value: `2.5f`. |
| `public float rollBodyLean` | Additional ragdoll torso sideways lean at full airborne input, in degrees. Initial value: `4`. |
| `public Vector2 WeightShift { get; }` | X is rightward weight, Y is forward weight; both range from minus one to one. |

## RiderAnimationRule

**Runtime/World/Passengers/Riding/RiderAnimator.cs**

See [rider setup](../Seats.md#motorcycle-foot-reversing-and-rider-animations) for configuration and examples.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public UnityEvent onEntered` | Condition began, including angle-range transitions. Can call custom animation code. |
| `public UnityEvent onExited` | Condition ended or the occupant/binding was released. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public string actionName` | Unique action name for a Custom condition. Control it with SetActionActive, PlayAction and StopAction. |
| `public float angleHysteresis` | Extra degrees retained around an active angle range, preventing repeated events at its boundary. |
| `public string boolParameter` | Optional Animator bool held while the condition is active. |
| `public RiderMotionCondition condition` | Rider condition controlling this rule. Angle conditions use the signed range below. |
| `public string enterTrigger` | Optional Animator trigger fired once when this condition begins. |
| `public string exitTrigger` | Optional Animator trigger fired once when this condition ends. |
| `public float fadeSeconds` | Crossfade duration in seconds for the optional state. |
| `public float feetBlendThreshold` | Feet Raised is true above this blend; Feet Lowered below it. |
| `public int layer` | Animator layer for the optional state. |
| `public float maximumAngle` | Inclusive maximum signed steering/lean angle in degrees. |
| `public float minimumAngle` | Inclusive minimum signed steering/lean angle in degrees. |
| `public string state` | Optional full Animator state path crossfaded on entry. Empty leaves state selection to your controller. |

## RiderAnimator

**Runtime/World/Passengers/Riding/RiderAnimator.cs**

See [rider setup](../Seats.md#motorcycle-foot-reversing-and-rider-animations) for configuration and examples.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Animator animator` | Optional explicit Animator. Empty follows the occupant's seated animation source, including ragdoll animation sampling. |
| `public string feetParameter` | Optional feet Ground-to-Riding blend float from zero to one. |
| `public string leanParameter` | Optional motorcycle lean float in degrees. |
| `public string phaseParameter` | Optional normalized alternating step phase float. |
| `public BalanceRider rider` | Balance Rider supplying steering, lean, foot and occupancy signals. |
| `public RiderAnimationRule[] rules` | Independent conditions, angle bands, bools, triggers, state crossfades and custom callbacks. |
| `public string speedParameter` | Optional float parameter for forward speed in m/s. |
| `public string steeringParameter` | Optional signed steering angle float in degrees. |
| `public string weightPitchParameter` | Optional signed forward/backward airborne weight-shift float, from minus one to one. Initial value: `"RiderWeightPitch"`. |
| `public string weightRollParameter` | Optional signed left/right airborne weight-shift float, from minus one to one. Initial value: `"RiderWeightRoll"`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public bool PlayAction(string actionName)` | Retrigger the named custom action. | — |
| `public bool PlayAnimation(string stateName, int layer = 0, float fadeSeconds = .2f)` | Crossfade to an existing Animator state; false for missing Animator/state/layer. | — |
| `public void RefreshBindings()` | Rebind after changing names, rules, controller or rider. | — |
| `public bool SetActionActive(string actionName, bool active)` | Set a named Custom condition without restarting unchanged state. Returns false if unavailable or unknown. | — |
| `public bool StopAction(string actionName)` | End the named custom action. | — |

## RiderBlendSource

**Runtime/World/Passengers/Seats/BalanceRider.cs**

Select the source of the rider’s Ground-to-Riding transition. It affects only feet using SpeedBlend.

- `Speed`: Speed magnitude between Lift Starts At and Fully Raised At requests progress from zero to one.
- `Manual`: Manual Riding Blend requests progress from zero to one. Your animation/input logic can update it at runtime.

## RiderCorneringPosture

**Runtime/World/Passengers/Riding/RiderCorneringPosture.cs**

Smooth torso weight transfer, separate from chassis torque and anatomical joint solving. Requires Support Balance and an occupied seat. Slow turns counterbalance the steering; riding turns combine the resolved bank with modest steering anticipation. Air control suppresses the extra posture, while wheelie scales it through the rider's steering-lean setting.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool enabled` | Enable automatic weight transfer; explicit rider steering lean remains independently configured. Initial value: `true`. |
| `public float maximumLean` | Additional torso bank at full riding lean, in degrees. Initial value: `10`. |
| `public float maximumRate` | Maximum torso transfer speed in degrees per second. Initial value: `65`. |
| `public float responseTime` | Seconds to ease weight transfer into and out of a turn. Initial value: `.22f`. |
| `public float slowCounterLean` | Outward counterbalance during slow parking turns, in degrees. Initial value: `4`. |

## RiderFootMode

**Runtime/World/Passengers/Seats/BalanceRider.cs**

Select how one foot follows the rider’s authored transforms. An assigned foot Handle retains priority, and missing required transforms leave the ordinary Seat binding intact.

- `SpeedBlend`: Blend between Ground and Riding using the resolved RidingBlend. Requires both poses.
- `Riding`: Follow the Riding transform directly, including a moving pedal or deck anchor.
- `Ground`: Follow the Ground transform directly.
- `Unchanged`: Leave the foot’s ordinary Seat binding intact.

## RiderKneeLean

**Runtime/World/Passengers/Riding/RiderKneeLean.cs**

Shared inside-knee target policy for physical support and IK. Existing targets are restored after release.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool enabled` | Enable inside-knee extension; disabling smoothly withdraws it and restores authored poles and support anchors. Initial value: `true`. |
| `public float fullExtensionAngle` | Requested riding bank in degrees for maximum knee extension. Initial value: `35`. |
| `public float maximumOffset` | Maximum outward displacement of the inside knee in metres. Initial value: `.2f`. |
| `public float responseTime` | Seconds to ease knee deployment and withdrawal. Initial value: `.2f`. |
| `public float steeringThreshold` | Steering input deadzone below which both knees return inward. Initial value: `.05f`. |

## RiderMotionCondition

**Runtime/World/Passengers/Riding/RiderMotionState.cs**

`Seated`, `Grounded`, `Airborne`, `SteeringAngle`, `LeanAngle`, `FeetRaised`, `FeetLowered`, `FootPushing`, `Reversing`, `LeftFootPlanted`, `RightFootPlanted`, `Custom`. See [rider setup](../Seats.md#motorcycle-foot-reversing-and-rider-animations).

## RiderMotionState

**Runtime/World/Passengers/Riding/RiderMotionState.cs**

See [rider setup](../Seats.md#motorcycle-foot-reversing-and-rider-animations) for configuration and examples.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Vector2 bodyLean` | Requested forward and side torso lean in degrees. |
| `public bool footPushing` | Rider motion configuration or signal; see the setup guide. |
| `public bool grounded` | Rider motion configuration or signal; see the setup guide. |
| `public Vector2 kneeOffset` | Outward extension in metres: X left knee, Y right knee. |
| `public float leanAngle` | Rider motion configuration or signal; see the setup guide. |
| `public bool leftFootPlanted` | Rider motion configuration or signal; see the setup guide. |
| `public Pose leftFootPose` | Resolved left foot target in world space; consume only while seated. |
| `public bool leftFootTargetValid` | Whether the corresponding world-space foot target is available for animation. |
| `public bool reversing` | Rider motion configuration or signal; see the setup guide. |
| `public float ridingBlend` | Rider motion configuration or signal; see the setup guide. |
| `public bool rightFootPlanted` | Rider motion configuration or signal; see the setup guide. |
| `public Pose rightFootPose` | Resolved right foot target in world space; consume only while seated. |
| `public bool rightFootTargetValid` | Whether the corresponding world-space foot target is available for animation. |
| `public bool seated` | Rider motion configuration or signal; see the setup guide. |
| `public float speed` | Rider motion configuration or signal; see the setup guide. |
| `public float steeringAngle` | Rider motion configuration or signal; see the setup guide. |
| `public float stepPhase` | Rider motion configuration or signal; see the setup guide. |
| `public Vector2 weightShift` | Airborne rider weight: X rightward, Y forward; zero when flight control is inactive. |

## RiderPushFeet

**Runtime/World/Passengers/Riding/RiderMotionState.cs**

`Both`, `Left`, `Right`, `Disabled`. See [rider setup](../Seats.md#motorcycle-foot-reversing-and-rider-animations).

## RiderReverseMode

**Runtime/World/Passengers/Riding/RiderFootDrive.cs**

`ReverseGear`, `FootPushing`. See [rider setup](../Seats.md#motorcycle-foot-reversing-and-rider-animations).
