# Grip fitting and steering ownership API

Read [the system explanation](../Scripting/GripSolving.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [AdaptiveHandGrip](GripSolving.md#adaptivehandgrip)
- [AdaptiveHandGrip.Finger](GripSolving.md#adaptivehandgripfinger)
- [HandGrip](GripSolving.md#handgrip)
- [HandGrip.FingerPose](GripSolving.md#handgripfingerpose)
- [IHandAvailabilitySource](GripSolving.md#ihandavailabilitysource)
- [IPassengerHandPose](GripSolving.md#ipassengerhandpose)
- [SteeringHandPhase](GripSolving.md#steeringhandphase)
- [SteeringHandRegrip](GripSolving.md#steeringhandregrip)
- [SteeringHandRegripSettings](GripSolving.md#steeringhandregripsettings)

## AdaptiveHandGrip

**Runtime/World/Passengers/IK/AdaptiveHandGrip.cs**

Binds a character to a surface and applies fitted finger poses.

**Inherits / implements:** `MonoBehaviour`, [IPassengerHandPose](GripSolving.md#ipassengerhandpose).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Finger[] digits` | Generated from Mecanim mapping or assigned explicitly for a custom skeleton. |
| `public VehicleHandle Handle { get; }` | Current source used by the shared hand-position evaluator. |
| `public virtual bool IsCalibrated { get; }` | Current is calibrated predicate; read it instead of maintaining a second application flag. |
| `public int iterations` | Finger/contact fitting iteration count. Higher values increase fitting work. Initial value: `6`. |
| `public bool leftHand` | Selects the left hand for this grip configuration. |
| `public virtual float MaximumPenetration { get; protected set; }` | Largest measured finger intrusion into the grip surface, in metres. |
| `public virtual float MeanContactGap { get; protected set; }` | Mean positive distance between fitted fingers and the grip, in metres. |
| `public float palmThickness` | Palm clearance thickness in metres used when fitting the hand to the handle surface. Initial value: `.009f`. |
| `public float poseRefitAngle` | Pose refit angle in degrees, relative to the owning mechanism's reference frame. Initial value: `2`. |
| `public float poseRefitDistance` | Ignore small physical wrist compliance instead of repeatedly re-optimizing finger curls. |
| `public int refitFingersPerFrame` | Maximum count/resolution for refit fingers per frame. Larger values increase detail or work performed by this system. Initial value: `2`. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public SteeringWheelHandle wheel` | Assign the wheel SteeringWheelHandle component/asset used by AdaptiveHandGrip. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool ApplyGrip()` | Applies the currently prepared adaptive grip to the mapped hand. | **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual void Bind(VehicleHandle surface, Animator animator, bool left)` | Binds this character hand to a `VehicleHandle` surface, calibrates the selected side and prepares adaptive surface fitting. | `surface` — Surface, interpreted by this operation in the declared type. `animator` — Character Animator providing mapped bones/animation context. `left` — `true` selects the left hand; `false` selects the right. |
| `public virtual bool Calibrate(Animator animator)` | Builds hand measurements/reference frames from the supplied character Animator. | `animator` — Character Animator providing mapped bones/animation context. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual void Release()` | Releases this part or hand pose through its declaring type's ownership boundary. | No arguments; no returned value. |
| `public virtual bool TryApplyPose(bool gripping)` | Applies the prepared gripping/released hand pose when this hand-pose provider can supply it. | `gripping` — `true` requests a gripping pose; `false` requests released/relaxed presentation. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual void Unbind()` | Releases the current source/hand association and its owned state. | No arguments; no returned value. |

## AdaptiveHandGrip.Finger

**Runtime/World/Passengers/IK/AdaptiveHandGrip.cs**

[Grip solving](GripSolving.md)

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Vector3 angles` | Angles. |
| `public float arcRatio` | Runtime arc ratio data retained by Finger; it is not serialized authoring configuration. |
| `public Transform[] bones` | Assign the bones references used by AdaptiveHandGrip.Finger. Entries are processed in list order. Initial value: `new Transform[3]`. |
| `public Vector3 boundAngles` | Runtime bound angles data retained by Finger; it is not serialized authoring configuration. |
| `public float boundOpposition` | Runtime bound opposition data retained by Finger; it is not serialized authoring configuration. |
| `public float boundSpread` | Runtime bound spread data retained by Finger; it is not serialized authoring configuration. |
| `public Quaternion[] fixedGrip` | Runtime fixed grip data retained by Finger; it is not serialized authoring configuration. |
| `public Vector3[] flexionAxes` | Local bending axes for the finger joints, in bone order. Initial value: `new Vector3[3]`. |
| `public Vector3 maximumFlexion` | Maximum finger-joint flexion angles in degrees for the proximal, intermediate and distal joints. Initial value: `new Vector3(85, 110, 80)`. |
| `public float minimumWrapDepth` | Runtime minimum wrap depth data retained by Finger; it is not serialized authoring configuration. |
| `public string name` | Text identifier/name for name. Keep it consistent with the referenced animation, profile or application setting. |
| `public Quaternion[] openRotations` | Reference local rotations for the open finger joints, in bone order. Initial value: `new Quaternion[3]`. |
| `public float opposition` | Opposition. |
| `public Vector3 oppositionAxis` | Direction vector defining opposition axis in the local frame used by this mechanism; it is not an absolute world position. |
| `public float padRadius` | Pad radius in metres in the owning system's space. Initial value: `.006f`. |
| `public Vector3 referenceAngles` | Runtime reference angles data retained by Finger; it is not serialized authoring configuration. |
| `public float referenceOpposition` | Runtime reference opposition data retained by Finger; it is not serialized authoring configuration. |
| `public float referenceSpread` | Runtime reference spread data retained by Finger; it is not serialized authoring configuration. |
| `public Quaternion[] rendered` | Runtime rendered data retained by Finger; it is not serialized authoring configuration. |
| `public bool renderedReady` | Runtime rendered ready data retained by Finger; it is not serialized authoring configuration. |
| `public float spread` | Spread. |
| `public Vector3 spreadAxis` | Direction vector defining spread axis in the local frame used by this mechanism; it is not an absolute world position. |
| `public Quaternion[] surfaceGrip` | Nonserialized raw surface-fit rotations, distinct from the final authored pose; populated by editor preparation or motorcycle binding. |
| `public bool thumb` | Uses thumb-specific opposition/spread fitting instead of ordinary finger bending. |
| `public Vector3 tipOffset` | Local-space tip offset vector used to place or size the corresponding geometry. |

## HandGrip

**Runtime/World/Passengers/IK/HandGrip.cs**

Stores character hand frames and fallback finger poses.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float angularDamper` | Damping for angular damper. Higher values oppose relative motion more strongly. Initial value: `35`. |
| `public float angularSpring` | Restoring stiffness for angular spring. Higher values resist displacement more strongly. Initial value: `1200`. |
| `public Transform contactPoint` | Assign the contact point reference used by HandGrip. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public FingerPose[] fingers` | Ordered fingers configuration entries. Expand each item; see HandGrip.FingerPose for its individual settings. Initial value: `Array.Empty<FingerPose>()`. |
| `public float maximumTorque` | Force/torque budget for maximum torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `250`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ApplyPose(bool gripping)` | Applies the configured character hand pose without creating a new seat occupancy. | `gripping` — `true` requests a gripping pose; `false` requests released/relaxed presentation. |
| `public virtual void ConfigureJoint(ConfigurableJoint joint, Rigidbody vehicle, VehicleHandle handle)` | Configures a physical hand joint using the prepared grip frame and drive policy. | `joint` — Joint, interpreted by this operation in the declared type. `vehicle` — Vehicle context/owner receiving the operation. `handle` — Handle, interpreted by this operation in the declared type. |
| `public virtual void DriveRotation(ConfigurableJoint joint, Rigidbody vehicle, Transform target, VehicleHandle handle, bool left, float contact = 1)` | Applies the physical wrist rotational drive in the prepared hand/contact frame. | `joint` — Joint, interpreted by this operation in the declared type. `vehicle` — Vehicle context/owner receiving the operation. `target` — Configured target object/point; see declared type and owner. `handle` — Handle, interpreted by this operation in the declared type. `left` — `true` selects the left hand; `false` selects the right. `contact` — Normalized physical contact participation. Default: `1`. |
| `public virtual Vector3 WristPosition(Transform target)` | Returns the wrist position corresponding to a prepared palm/contact frame. | `target` — Configured target object/point; see declared type and owner. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation. |
| `public virtual Quaternion WristRotation(Transform target)` | Returns wrist orientation from the prepared hand/contact frame. | `target` — Configured target object/point; see declared type and owner. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation. |

## HandGrip.FingerPose

**Runtime/World/Passengers/IK/HandGrip.cs**

Value data for finger pose; its fields are listed below.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform bone` | Assign the bone reference used by HandGrip.FingerPose. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public Quaternion gripRotation` | Reference/orientation rotation for grip rotation. Identity adds no rotation. |
| `public Quaternion relaxedRotation` | Reference/orientation rotation for relaxed rotation. Identity adds no rotation. |

## IHandAvailabilitySource

**Runtime/World/Passengers/IK/IHandAvailabilitySource.cs**

Presentation or lifecycle contract for independent vehicle components.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `bool CanUseHand(PassengerSeat seat, PassengerBodyPart hand)` | Reports whether the requested seat and hand are available for an interaction. | — |

## IPassengerHandPose

**Runtime/World/Passengers/IK/IPassengerHandPose.cs**

Configuration/implementation type for ipassenger hand pose within grip fitting and steering ownership.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void Release()` | Releases this part or hand pose through its declaring type's ownership boundary. | No arguments; no returned value. |
| `bool TryApplyPose(bool gripping)` | Applies the prepared gripping/released hand pose when this hand-pose provider can supply it. | `gripping` — `true` requests a gripping pose; `false` requests released/relaxed presentation. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `void Unbind()` | Releases the current source/hand association and its owned state. | No arguments; no returned value. |

## SteeringHandPhase

**Runtime/World/Passengers/IK/Regrip/SteeringHandRegrip.cs**

Defines the allowed steering hand phase choices used by this topic.

### Values

- `Held`
- `Opening`
- `Transferring`
- `Closing`
- `Parked`
- `Approaching`
- `Released`
- `External`

## SteeringHandRegrip

**Runtime/World/Passengers/IK/Regrip/SteeringHandRegrip.cs**

Coordinates steering contacts, availability and external reservations.

**Inherits / implements:** [PassengerBehaviour](PassengerControllers.md#passengerbehaviour), [IHandAvailabilitySource](GripSolving.md#ihandavailabilitysource).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual int CompletedTransfers { get; protected set; }` | Read-only/resolved completed transfers for `SteeringHandRegrip`. |
| `public virtual int LeadingHand { get; }` | -1: no leader, 0: left, 1: right. |
| `public virtual bool LeftHandAvailable { get; }` | Read-only/resolved left hand available for `SteeringHandRegrip`. |
| `public virtual SteeringHandPhase LeftPhase { get; }` | Read-only/resolved left phase for `SteeringHandRegrip`. |
| `public virtual int PoseGeneration { get; protected set; }` | Read-only/resolved pose generation for `SteeringHandRegrip`. |
| `public virtual bool RightHandAvailable { get; }` | Read-only/resolved right hand available for `SteeringHandRegrip`. |
| `public virtual SteeringHandPhase RightPhase { get; }` | Read-only/resolved right phase for `SteeringHandRegrip`. |
| `public SteeringWheelHandle surface` | Assign the surface SteeringWheelHandle component/asset used by SteeringHandRegrip. |
| `public SteeringWheelAnimator wheelAnimator` | Assign the wheel animator SteeringWheelAnimator component/asset used by SteeringHandRegrip. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool CanUseHand(PassengerSeat requestedSeat, PassengerBodyPart hand)` | Reports whether the requested seat and hand are available for an interaction. | — |
| `public virtual Transform ColumnSupport(bool left)` | Returns the steering hand's current column-support contribution. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Returned `Transform`; ownership remains as specified by the creating/lookup operation. |
| `public virtual Object HandOwner(bool left)` | Returns the external Unity object that currently reserves the selected steering hand. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Returned Object; ownership remains as specified by the creating/lookup operation. |
| `public virtual bool IsFirmlySupported(bool left)` | Reports whether the selected steering hand has firm support in the current contact state. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual bool IsHandAvailable(bool left)` | Checks whether the selected steering hand is available under current reservation rules. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual bool IsHandOnWheel(bool left)` | Reports whether the selected hand is currently attached to the steering control. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** `true` when the described condition holds; `false` otherwise. |
| `public virtual float MaterialAngle(bool left)` | Returns the selected hand's coordinate on the steering-wheel material. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Computed float in the operation's documented unit/domain. |
| `public override void PreparePassenger(Passengers core, PassengerSeat passengerSeat)` | Prepares this passenger behavior for an occupied seat. | `core` — Owning audio or passenger core supplying shared context. `passengerSeat` — Seat whose occupied hand is temporarily controlled. |
| `public virtual void PreparePose()` | Prepares steering hand pose state for the current passenger/control binding. | No arguments; no returned value. |
| `public virtual bool ReleaseHand(bool left, Object owner)` | Releases a steering-hand reservation only for the matching owner. | `left` — `true` selects the left hand; `false` selects the right. `owner` — Unity/application owner whose identity controls this relationship or resource. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual bool ReleaseSteeringHand(bool left)` | Temporarily releases steering attachment for the selected hand under the regrip policy. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public override void RenderPassenger(Passengers core)` | Advances render-time passenger presentation owned by this behavior/core. | `core` — Owning audio or passenger core supplying shared context. |
| `public override void ResetPassenger(Passengers core)` | Resets this passenger behavior's state for the supplied seat. | `core` — Owning audio or passenger core supplying shared context. |
| `public virtual bool TakeSteeringHand(bool left)` | Requests steering-hand attachment under the regrip/ownership policy. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual bool TryReserveHand(bool left, Object owner, Transform palmTarget = null)` | Reserves a steering hand for a live owner and optional external palm frame. | `left` — `true` selects the left hand; `false` selects the right. `owner` — Unity/application owner whose identity controls this relationship or resource. `palmTarget` — Optional stable external palm frame for the reserved hand. Default: `null`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TrySetLeadingHand(bool left)` | Requests which hand leads steering regrip while respecting the current control state. | `left` — `true` selects the left hand; `false` selects the right. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## SteeringHandRegripSettings

**Runtime/World/Passengers/IK/Regrip/SteeringHandRegripSettings.cs**

Configuration/implementation type for steering hand regrip settings within grip fitting and steering ownership.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float guideAdjustmentSpeed` | Maximum guide grasp adjustment along the rim, in degrees per second. Wheel-following itself is never filtered. |
| `public float leftRestAngle` | Lower rim angles for the relaxed thumb/index support; measured in the unturned wheel plane. |
| `public float minimumHandSeparation` | Minimum angular spacing in degrees kept between hand contacts around the rim. Initial value: `75`. |
| `public float palmReturnTime` | Minimum time for a full palm-pressure-to-wrapped-grip blend while the released wheel unwinds. |
| `public float reachAdjustment` | Search around each preferred angle for a reachable wrist pose. |
| `public float reachMargin` | Safety margin subtracted from the hand's measured arm reach, in metres. |
| `public float rightRestAngle` | Right rest angle in degrees, relative to the owning mechanism's reference frame. Initial value: `290`. |
