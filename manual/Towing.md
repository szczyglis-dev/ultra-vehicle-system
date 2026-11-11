# Tow a trailer

A trailer is an independent vehicle root with its own Rigidbody, wheel contacts and suspension. `Coupler` creates the physical connection on the towing vehicle; `Trailer` receives resolved braking without needing a keyboard or engine. Do not parent a dynamic trailer under the tractor as a substitute for the hitch.

## Inspector quick start

1. Prepare towing vehicle and trailer as separate roots, each with its own Vehicle Controller, Rigidbody, colliders and wheel setup. Do not make the dynamic trailer a child of the tow car.
2. Add **Modules > World > Coupler** on the towing vehicle and **Trailer** on the trailer. Create one hitch Transform on each model at the intended attachment point and drag each into its module's **Hitch** field.
3. Fit the points/headings and configure attachment distance, articulation/break settings and forwarded trailer braking below. Keep detached parking enabled if the trailer should hold itself when unhitched.
4. For a connection at startup, drag the trailer's Trailer component into the coupler's **Initial Trailer** and enable **Attach On Start**. Position the hitches within the admission/alignment limits. Discover/apply and save both vehicles, then test braking, a turn, a bump and detachment. Later attach/detach requests use the application/demo input.

## Prepare the two vehicles

1. Verify the towing vehicle drives/brakes correctly on its own.
2. Build the trailer root with its mass/centre of mass, hull colliders and Wheel Setup. Use the [suspension guide](Suspension.md) for static support and the [surface guide](Surfaces.md) for grip/effects.
3. Add/enable/register `Trailer` on that root. Keep it unpowered; the Trailer step clears drive demand/motor torque and supplies its braking policy.
4. Set wheel service-brake/handbrake roles and brake multipliers on the trailer itself.
5. Verify detached support and the intended parking state before making the connection.

Keep each vehicle's WheelColliders owned by its own Rigidbody. The towing vehicle's Wheel Setup must not include trailer colliders. Do not let an ordinary trailer input/Brakes policy compete with the forwarded brake result; use the intended trailer setup and inspect resolved demand.

## Configure the connection

1. Create a trailer **Hitch** Transform at its coupling point and assign it to Trailer.
2. Add `Coupler` to the towing vehicle, assign **Vehicle** and a rear **Hitch** Transform.
3. Keep hitches rigidly attached to their respective vehicle frames and close enough to couple.
4. Set **Attach Distance**, **Attachment Alignment Time**, articulation and drawbar settings below.
5. For startup coupling, assign **Initial Trailer** and enable **Attach On Start**. Otherwise request attachment from gameplay with `TryAttach(trailer)`.
6. Test slow forward/reverse travel and braking before tight turns or high-speed impacts.

Attach On Start controls only the startup request; manual attachment remains available when off. `TryAttach` rejects missing bodies/hitches, occupied connections, self-attachment, cycles and excessive distance. It is not a search for any nearby trailer and does not teleport a distant body to the hitch.

### Alignment and articulation

**Attachment Alignment Time** gradually converges accepted nearby anchor positions. Start with the models already reasonably aligned, with clearance for the drawbar and bodywork. A very short alignment time can produce a strong correction; a long time is not a replacement for an unreachable initial arrangement.

The joint locks lateral/vertical separation and uses a damped longitudinal drive for fore/aft compliance. **Longitudinal Spring** (N/m) and **Longitudinal Damper** (N·s/m) tune that connection. Perfectly rigid competing constraints can fight parked tire contacts, so avoid assuming infinite stiffness is always more stable.

**Pitch Limit** and **Roll Limit** bound those articulations. Yaw remains free for normal turning. Choose travel consistent with the real hitch and bodywork; a valid angular limit does not prevent rendered or unrelated colliders from intersecting at a tight turn.

The coupler manages its connection's collision exclusions and restores what it owned on detach/break. It does not disable every collider in either vehicle or authorize replacing another system's unrelated collision policy.

## Braking and detachment

| Trailer setting | Result |
| --- | --- |
| Follow Service Brake | Uses towing vehicle's resolved service-brake demand |
| Service Brake Multiplier | Scales that demand before clamping to 0–1 |
| Follow Handbrake | Forwards the towing command's handbrake request |
| Park When Detached | Applies the trailer's parking policy without a towing vehicle |

Brake torque strength and each wheel's role remain the trailer's own settings. A parking request cannot act on wheels that have no handbrake role. A higher multiplier increases demand only up to 1; it does not increase the trailer's configured maximum brake torque indefinitely.

Use `Detach()` for an explicit disconnect. **Allow Joint Break** independently allows native forces to break the connection; when enabled, Break Force and Break Torque set the thresholds. Turning breaking off makes those limits effectively unbreakable while explicit detach remains available.

Observe `Attached`, `Detached` and the trailer's connection-break event to update UI or gameplay. Do not infer a valid connection merely from two hitch Transforms being close. After detach/break, check parking, residual physical motion and collision restoration.

## Road trains

A trailer can also carry a rear Coupler for another independent Trailer. Build and test one connection before extending the train. Cyclic attachment is rejected, including an indirect loop that would lead back to an already connected vehicle.

Each additional joint/body adds stability and braking requirements. Test low-speed reversing, the tightest bend, an incline and emergency braking with representative masses. Steering and driver input remain on the intended powered vehicle, while each Trailer forwards the resolved demand along its configured relationship.

## Tire presentation

Add TireFeedback plus desired tire audio, particles and marks to the trailer so it uses its own wheel contacts. It does not need an engine loop. Configure visible wheel movement in its Wheel Setup; a static mesh attached to the tractor cannot represent the trailer's suspension.

Use the [surface classification guide](Surfaces.md) for ground-dependent effects and the relevant effect modules for output. Hitch sounds/gameplay prompts can subscribe to attachment events rather than poll every frame.

## Verify the combination

| Symptom | Inspect |
| --- | --- |
| Attachment returns false | Distance, valid hitches/bodies, existing connection and cycle guards |
| Large impulse on coupling | Initial geometry, alignment time and compliance |
| Trailer drags/brakes continuously | Detached parking, handbrake roles and conflicting input/brake policy |
| Trailer does not brake with tractor | Follow flags, multiplier, own brake strength and wheel roles |
| Vehicle pitches badly while parked | Drawbar compliance, wheel contacts and mass/centre of mass |
| Tight turn intersects bodywork | Hitch placement, model clearance and articulation |
| Detach button stops working when break disabled | Explicit Detach is separate; inspect application binding/connection state |

The [towing reference](Scripting/Towing.md) contains an attach/detach example and collision/constraint ownership details. Exact methods/events are in [API](API/Towing.md).
