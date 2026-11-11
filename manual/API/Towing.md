# Coupling and trailers API

Read [the system explanation](../Scripting/Towing.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [Coupler](Towing.md#coupler)
- [Trailer](Towing.md#trailer)

## Coupler

**Runtime/World/Towing/Coupler.cs**

Validates and owns one hitch relationship, joint and changed collision pairs.

**Inherits / implements:** [WorldModule](Modules.md#worldmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<Trailer> Attached` | After coupler admission creates the relationship. Payload: Trailer. |
| `public event Action<Trailer> Detached` | After explicit detachment/cleanup of this hitch relationship. Payload: the formerly connected Trailer. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool allowJointBreak` | Allow physical forces to break the hitch. Disable for an unbreakable connection. |
| `public float attachDistance` | Attach distance in metres in the owning system's space. Initial value: `1.2f`. |
| `public virtual Trailer AttachedTrailer { get; protected set; }` | Trailer currently connected to this coupler, or `null` when detached. |
| `public float attachmentAlignmentTime` | Seconds to bring accepted nearby hitches together without an instantaneous correction impulse. |
| `public bool attachOnStart` | Attach Initial Trailer at startup. Manual `TryAttach` remains available when disabled. |
| `public float breakForce` | Force/torque budget for break force; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `200000`. |
| `public float breakTorque` | Force/torque budget for break torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `200000`. |
| `public Transform hitch` | World-space coupling point used to align the trailer connection. |
| `public Trailer initialTrailer` | Assign the initial trailer Trailer component/asset used by Coupler. |
| `public float longitudinalDamper` | Fore/aft hitch damping in N·s/m. |
| `public float longitudinalSpring` | Fore/aft hitch stiffness in N/m. A compliant drawbar prevents parked tire constraints from fighting a perfectly rigid longitudinal lock. |
| `public float pitchLimit` | Maximum hitch pitch articulation in degrees. Initial value: `30`. |
| `public float rollLimit` | Maximum hitch roll articulation in degrees. Initial value: `20`. |
| `public VehicleController vehicle` | Assign the vehicle VehicleController component/asset used by Coupler. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Detach()` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | No arguments; no returned value. |
| `public virtual bool TryAttach(Trailer trailer)` | Requests a nearby valid trailer relationship, creating owned hitch constraints only when admitted. | `trailer` — Explicit candidate trailer; selection/proximity UI remains application-owned. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## Trailer

**Runtime/World/Towing/Trailer.cs**

Stores the towed-body connection and brake-following behavior.

**Inherits / implements:** [WorldModule](Modules.md#worldmodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action ConnectionBroken` | When a trailer's active hitch relationship breaks. No payload. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual ConfigurableJoint Connection { get; internal set; }` | Read-only/resolved connection for Trailer. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public bool followHandbrake` | Forward the towing vehicle's handbrake. Detached parking is controlled separately. |
| `public bool followServiceBrake` | Forward the towing vehicle's resolved service brake to this trailer. |
| `public Transform hitch` | World-space coupling point used to align the trailer connection. |
| `public bool parkWhenDetached` | When checked, park when detached is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public float serviceBrakeMultiplier` | Multiplier for forwarded service braking; final demand is clamped to 0–1. |
| `public virtual VehicleController TowingVehicle { get; internal set; }` | Read-only/resolved towing vehicle for Trailer. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Forwards configured towing brake requests, clears trailer propulsion and applies detached-parking policy. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
