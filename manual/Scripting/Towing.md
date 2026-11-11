# Towing lifecycle

Towing connects two independently simulated bodies through a hitch relationship. `Coupler` owns connection admission and the physical joint; `Trailer` owns how the towed vehicle follows braking and detached-parking policy. The application selects a candidate and decides when attachment is requested.

This separation allows manual hitch interactions, proximity selection or an application-specific trailer inventory to use the same connection mechanic. A successful connection does not transfer ownership of the trailer's lifetime or replace its own wheel setup.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `Coupler` | Validates and owns one hitch relationship, joint and changed collision pairs. |
| `Trailer` | Stores the towed-body connection and brake-following behavior. |
| `VehicleController` | Supplies each body's resolved command/physics lifecycle. |

`Coupler` owns the relationship to one `Trailer` and creates the physical joint on that trailer body. Hitch anchors are in each `Rigidbody`'s local frame. Admission rejects occupied connections, self/cycles and distance outside `attachDistance`.

## Constraint and collision ownership

`Trailer` is the command-following half of towing. It reads the connection's resolved service/handbrake state according to configured follow switches and multiplier. It does not become the towing engine. Detached parking is another explicit policy, useful for a trailer that should not roll away when uncoupled.

The trailer remains its own body with its own wheel definitions and support. Configure its mass, wheel brakes and hitch anchor as a complete vehicle before connecting it. A correct coupler cannot compensate for wheels belonging to the wrong rigidbody or a trailer with no useful braking/support setup.

For a custom brake-following rule, replace the trailer-side behavior while retaining the coupler's relationship and cleanup contract. For another hitch constraint, replace the coupler's constraint implementation while leaving application candidate selection outside it. Observe `ConnectionBroken` to handle unexpected native joint loss as well as deliberate detachment.

Author each hitch anchor in its body's local frame. Incorrect anchor placement produces drawbar load even when the visible hitch appears aligned. First check a close, stationary connection, then introduce articulation, braking and larger accepted gaps.

`attachmentAlignmentTime` spreads closure of an accepted gap over time. It is not a scene-wide trailer teleport or a substitute for selecting a nearby candidate. Native breaking thresholds and explicit detachment are separate exit paths, but both must end the relationship and release only its owned resources.

Brake following is also distinct from propulsion. Configure `followServiceBrake`, `followHandbrake` and `parkWhenDetached` for the intended trailer. Long trains involve several independent bodies and controllers, so the application remains responsible for stable mass ratios, hitch geometry and timestep choices.

The joint locks lateral/vertical translation, permits yaw and bounds pitch/roll. A longitudinal spring/damper carries drawbar load; `attachmentAlignmentTime` closes the accepted gap progressively. Breaking policy controls native break thresholds independently of explicit `Detach`.

Collision suppression covers colliders owned by both connected bodies. `Detach`/break restores only pairs changed by this connection. The application should not rely on vehicle teleport to reproduce coupling state.

`Trailer` forwards resolved service/handbrake requests according to its switches/multiplier, clears propulsion, and can park when detached. A train chains those relationships; fixed-step observation between independent controllers can be one tick apart.

## Attach from gameplay

The example assumes candidate selection is already complete. This keeps scene searching and interaction range UI outside the reusable hitch mechanic. A `false` result means the requested relationship was not admitted; do not update inventory or mark the trailer as attached independently.

Subscribe to relationship events when camera, UI or mission rules depend on coupling. On scene reset, reconstruct or explicitly clear those relationships according to the application's rule. Moving a root transform alone is not a complete restore of hitch state.

Attach this to a hitch interaction object. Assign a coupler and nearby trailer, then call `Attach` or `Detach` from UI/proximity logic. The example does not search the scene or move a distant trailer.

**Example: `TrailerInteraction.cs`**

<!-- example: TrailerInteraction.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class TrailerInteraction : MonoBehaviour
    {
        public Coupler coupler;
        public Trailer trailer;

        public bool Attach() => coupler && trailer && coupler.TryAttach(trailer);
        public void Detach() { if (coupler) coupler.Detach(); }
    }
}
```

Observe Attached, Detached and `Trailer.ConnectionBroken` for game rules. Own inventory/respawn of a trailer outside this connection component.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed coupling and trailers API](../API/Towing.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### Coupler

[Coupler](../API/Towing.md#coupler) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void Detach()` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. |
| `public virtual bool TryAttach(Trailer trailer)` | Requests a nearby valid trailer relationship, creating owned hitch constraints only when admitted. |

| Event / callback | Role |
| --- | --- |
| `public event Action<Trailer> Attached` | After coupler admission creates the relationship. Payload: Trailer. |
| `public event Action<Trailer> Detached` | After explicit detachment/cleanup of this hitch relationship. Payload: the formerly connected Trailer. |

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### Trailer

[Trailer](../API/Towing.md#trailer) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Forwards configured towing brake requests, clears trailer propulsion and applies detached-parking policy. |

| Event / callback | Role |
| --- | --- |
| `public event Action ConnectionBroken` | When a trailer's active hitch relationship breaks. No payload. |

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
