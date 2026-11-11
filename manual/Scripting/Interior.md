# Interior presentation contracts

Interior presentation translates mechanical state into instruments, cockpit controls and driver-visible systems. A value source reads a mechanic; a needle or rotary control maps that value to a pose; a binding connects accepted actions to the appropriate presentation. Mirrors add their own rendering lifecycle. Exterior blade motion is covered in [Wipers](MovingParts.md#wipers).

The central design rule is one owner for each value and transform. A bound instrument follows its source. An API-driven instrument follows explicit requests. A moving pivot follows one animator. Keeping these ownership choices explicit makes it possible to replace a dashboard or integrate another UI without changing the mechanics.

## Configure in the Inspector first

Use the [cockpit-control workflow](../InteriorControls.md#inspector-quick-start-add-one-cockpit-control) for moving geometry, value sources and bindings, or [interior systems](../InteriorSystems.md#inspector-quick-start) for screens/mirrors/fuel. Add the components on the intended model objects, assign their references and test the display before building custom value sources or rendering code.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `AnchoredRotation` | Preserves a neutral pose relative to an independent pivot frame. |
| `FuelTank` | Owns fuel quantity, consumption and ignition-empty policy. |
| `GearShiftAnimator` | Synchronizes shift presentation with accepted mechanical gear changes. |
| `InstrumentNeedle` | Specializes value-driven rotation for instruments. |
| `InteriorValueSource` | Base adapter for an `IInteriorValueSource` value producer. |
| `RearMirrors` | Owns mirror eligibility, camera rendering and generated textures. |
| `RotaryAnimator` | Maps requested/source values to rotary presentation. |
| `WiperBlade` | Maps normalized stroke to authored blade geometry. |

## Neutral frames and value sources

A neutral frame describes what “zero” means for a particular model. Capture it with the part in its authored neutral position, before any runtime control has turned it. If configuration recaptured the current animated pose as neutral, each reconfiguration could move the baseline and accumulate an offset.

A source value should have a clear unit. A speed source may report a physical speed range; the fuel source below reports a fraction from zero to one. Configure the consumer's value range to that unit, then configure its angle range from the mesh. Keeping units explicit avoids putting dashboard-specific angle conversions inside the fuel mechanic.

`AnchoredRotation` stores a moving part's neutral position/orientation in an independent anchor frame. Both position and orientation orbit that anchor. The anchor must not be the part or its descendant. Capture neutral poses while authored neutral; repeated enable/configure must not recapture a turned control.

`InstrumentNeedle` and `RotaryAnimator` map a physical value range to signed degrees. `SetValue` requests a smoothed value; `SetNormalizedValue` maps a fraction; `SetImmediate` bypasses smoothing. A bound `IInteriorValueSource` owns ongoing values. `Bind`(`null`) releases it for API control. `ValueChanged` reports the requested value, not arrival.

## Add a fuel needle source

Derive from `InteriorValueSource` when the missing piece is only a reading. `ReadValue()` should read and return a value without changing the underlying mechanic. The needle owns smoothing and angle mapping, so the source does not need another `Update` or its own rotation code.

This sample returns zero when the tank reference is absent. An application that must distinguish “empty” from “unavailable” can add its own display status alongside the numeric source rather than assigning special out-of-range values to the needle.

Put this source beside the instrument, assign `FuelTank`, then drag it into the needle Data Source field. Set the needle range to 0–1 and its angle range for the model.

**Example: `FuelNeedleSource.cs`**

<!-- example: FuelNeedleSource.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class FuelNeedleSource : InteriorValueSource
    {
        public FuelTank tank;
        public override float ReadValue() => tank ? tank.Fraction : 0;
    }
}
```

This source only reads fuel. Turning a presentation knob does not refuel the tank unless application code explicitly connects that action.

## Gear and switch bindings

ProfileSwitchBinding selects explicit On Profile Id and Off Profile Id registrations from ProfileSwitcher. SetOn(true) selects the on ID; SetOn(false) selects the off ID. It supports any two entries from a larger profile list.

A binding keeps a presentation control synchronized with a mechanic. It sits between two owners: the mechanic knows the accepted state, and the handle knows how the model moves. The binding should translate between them without taking over either simulation.

`GearShiftAnimator` resolves a gearbox and drives an `IGearShiftAnimator`; a paddle can animate an accepted up/down shift without becoming the gearbox itself. `IndicatorSwitchBinding`, `WiperSwitchBinding` and `ProfileSwitchBinding` connect their corresponding switches. Their `Synchronize` operations display the current mechanic state without issuing another user request, preventing a feedback loop between a switch event and its own display update.

For a custom binding, subscribe to the mechanic that owns the result, retain the exact subscribed instance, and release it when rebinding or disabling. Use silent/immediate presentation synchronization when restoring a pooled vehicle. Put player intent in the request path, and let the mechanic's result bring the displayed state back into agreement.

Observe the accepted mechanic state when the display should tell the driver what actually happened. Animating a gear paddle from input can show the driver's gesture; animating the gear indicator from accepted gearbox state shows the selected gear. They are useful but different signals.

When replacing a control animator, preserve its neutral-frame convention and remove the old transform writer. A correct custom animation can still jitter if a passenger binding or another animator writes the same pivot later in the frame.

Vehicle Handles advances each switch once. Bindings own synchronization and never tick switch motion separately.

## RearMirrors

A mirror needs a camera view, an output texture and a visible surface using that texture. The module manages eligibility and refresh so every mirror does not need a full camera render every frame. Choose texture dimensions and refresh budget for the screen area and number of simultaneously visible mirrors.

Ownership matters for pooling: a texture created by the module can be released with it, while a supplied texture may be shared by another application system. Do not destroy supplied resources when replacing the mirror implementation. For a custom render pipeline, provide the compatible rendering path rather than changing the mirror's physical surface geometry.

Each `RearMirror` entry has one dedicated camera, surface and optional caller-owned texture. The observer/frustum/range and refresh budget decide eligibility. This is not occlusion checking; application knowledge can disable a hidden mirror explicitly.

Generated textures/sources are module-owned. Supplied textures remain caller-owned. Disabling restores captured camera state/property blocks. Re-enable after changing dimensions. Camera.Render is used on Built-in; supported SRPs use `StandardRequest`. The module reuses a request per channel and cached shader property IDs; changing the texture property or supplied target remains supported. Frustum planes are only calculated when a channel passes the activity, refresh, mask and distance checks. Unsupported rendering pipelines need an integration.

### Gate mirror rendering from a quality policy

An application quality setting can disable mirror work through the module rather than disabling individual cameras behind its back. The action updates eligibility while preserving the module's ownership and events. When enabled again, normal observer/frustum/range policy still decides whether a mirror renders.

**Example: `MirrorQualityPolicy.cs`**

<!-- example: MirrorQualityPolicy.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class MirrorQualityPolicy : MonoBehaviour
    {
        public RearMirrors mirrors;

        public void SetMirrorRendering(bool allowed)
        {
            if (mirrors) mirrors.SetMirrorsEnabled(allowed);
        }
    }
}
```

Use `SetMirrorEnabled(index, value)` for one configured mirror. Its index belongs to the current mirror array; if the application rebuilds that array, resolve its own stable entry identity first. Camera pose authoring and texture-size changes remain separate configuration operations.


## Fuel and assists

`FuelTank` is the quantity and consumption mechanic. It stores fuel independently of a gauge, so replacing a dashboard does not change available fuel. Consumption uses running state and engine activity; an instrument source only reads the resulting quantity or fraction.

`consumeFuel` chooses whether running consumes fuel, using idle/load/RPM consumption rates in litres per hour. `stopEngineWhenEmpty` separately chooses whether an empty tank stops/blocks the engine. Configure both deliberately for a vehicle that should have an actual fuel constraint. A decorative gauge can read a tank even when consumption is disabled.

`DrivingAssists` is a different responsibility: it coordinates traction/stability assist choices. Its public setters are the preferred application boundary when it owns those settings. Disabling it stops synchronization; it does not reconstruct whatever values the underlying modules had before. A workshop or save system should therefore store its intended assist configuration rather than infer a previous state from enable/disable.

`DrivingAssists` writes its shared TCS/steering settings while enabled; disabling stops synchronization but does not roll values back. Stability is bounded yaw/lateral assistance, not brake-based ESP.

For controls setup see [Interior controls](../InteriorControls.md); for backend-independent subscriptions see [Events](Events.md).

## Refuel through a service action

Use the actual transferred quantity when connecting a tank to a garage or supply system. `Refuel` can accept less than requested when the tank approaches capacity. The component below exposes that amount so an application can charge for actual litres or subtract the same amount from a supply inventory.

**Example: `FuelServiceAction.cs`**

<!-- example: FuelServiceAction.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class FuelServiceAction : MonoBehaviour
    {
        public FuelTank tank;
        [Min(0)] public float requestedLitres = 10;
        public float LastTransferredLitres { get; private set; }

        public void Refuel()
        {
            LastTransferredLitres = tank ? tank.Refuel(requestedLitres) : 0;
        }
    }
}
```

Refuelling does not itself request ignition. Keep the service operation and engine-start action separate so a vehicle can remain parked after receiving fuel. For a finite supply, calculate the permitted request before the call, then debit only the returned amount.

## Provide custom control data

Implement `IInteriorValueSource` on any application MonoBehaviour, or derive from `InteriorValueSource` for a scalar source base. Assign that component to an animator's Data Source. The consumer calls ReadValue in its existing update phase; do not add a second animation loop. Return normalized values for controls and physical units for instruments. This interface is independent of the vehicle input source and telemetry events.

<!-- example: CustomSteeringDataSource.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class CustomSteeringDataSource : MonoBehaviour, IInteriorValueSource
    {
        [Range(-1, 1)] public float networkSteering;

        public float ReadValue()
        {
            return networkSteering;
        }
    }
}
```

Drag this component into SteeringWheelAnimator.Data Source. Scalar-only sources supply both visible steering and hand intent. Implement ISteeringIntentSource as well when a resolved angle must remain nonzero after input release; this does not steer the road wheels. Assign a source implementing the same interface to a pedal or throttle when the application owns that presentation value. For YokeAnimator and SteeringStickAnimator, Data Source supplies roll and Pitch Source supplies pitch. Both stay independently replaceable.

Sources are sampled, not subscribed. Disable a source to request a neutral visual reading, or clear the field to use the consumer's built-in mapping. For actual gear changes, retain the gearbox event flow rather than synthesizing a numeric polling source.

## Floor-mounted gear lever

`GearLeverAnimator` follows `Engine.ActiveGearbox` (or a directly assigned Gearbox). It displays accepted changes, including automatic shifts, neutral and reverse. It does not issue gear commands or delay mechanical gear engagement. The Bus demo is the only vehicle fitted with this lever; it follows both automatic and manual transmission selections.

Create a stationary **Anchor** at the floor pivot and a separate **Moving Part** with its origin at the same pivot. Put the shaft, grip and palm contact below Moving Part. Assign these to the animator and its `GearLeverHandle`. Choose **Rotation** for a floor-hinged stick, or **Translation** for a sliding selector. Each Positions item has a unique gear number (-1 = R, 0 = N, 1–6 = forward gears) and the appropriate Euler rotation or local position. Values are absolute in the anchor frame, so no recapture is needed after an edit or preview. In the Bus, gears 1/2 are closest to the driver, 3/4 are farther right and 5/6 are farthest right. Odd gears tilt toward the front of the bus, even gears toward the rear; translation follows the same layout. The shipped Bus uses compact pose offsets around the retained first-gear pose, with smaller spacing than the generic component defaults. Neutral is an authored pose and need not be zero.

Each row has **Preview this gear**. The selected row refreshes when **Live preview selected gear** is enabled. Closing the Inspector, restoring the pose, recompiling or entering Play restores the pre-preview transform. Open a scene instance or Prefab Mode; persistent Project assets cannot be previewed. The preview only moves the lever and its child palm contact; use the handle's Hand position preview separately to author the mannequin's grip.

Assign the driver's seat and Right Hand in the handle's Use settings; keep **Use On Action** off because the animator requests ownership directly from gearbox events. Outbound Duration, Return Duration, Return Delay and Finger Blend Duration work as for other handles. Set the steering wheel's Minimum Attachments to 1. The animator calls `TryReachAndHold`, waits for hand arrival, moves the lever with the hand attached, then requests a smooth return. Repeated shifts reuse the held hand and start from the visible pose. **Downshift Delay** defaults to 0.75 seconds: each further reduction between forward gears restarts a quiet-period timer, so a braking sequence such as 6→5→4→2 produces one final lever movement. No new hand reach begins during this wait. Set it to zero to respond immediately. Upshifts, first gear, neutral and reverse cancel/bypass the wait. This affects presentation only; the gearbox changes normally. With Wait For Handle enabled, an occupied busy limb waits for availability and real contact; there is no timeout bypass. Disabling Wait For Handle allows independent visual motion. Startup and transmission rebinding synchronize without requesting a limb.

## Hands on steering-wheel gear paddles

The Car's left paddle is configured for downshifts and Left Hand; the right paddle is configured for upshifts and Right Hand. Each `GearPaddleAnimator.handle` references a `GearPaddleHandle` with its palm contact under the moving paddle. Vehicle-local IDs are `LeftGearPaddle` and `RightGearPaddle`.

`GearShiftAnimator` continues to report accepted gearbox changes. With a grip assigned, a paddle requests a reach-and-hold operation through the central controller, waits for arrival, presses and returns its mesh with the palm attached, then releases the hand after the grip's Return Delay. The controller handles the slower return to the steering wheel and retains the other steering hand. Same-side retriggers reuse the held hand; opposite-side gestures wait for availability without a timeout bypass. By default busy hands retain ownership; an explicitly configured higher-priority timed request can interrupt a paddle gesture through Interrupt Lower Priority. Disabling/resetting the paddle releases ownership. Without a grip or occupant, existing visual paddle motion remains available. The `onPressed` callback fires when visual pressing actually starts, after any limb wait; `IsMoving` describes mesh motion rather than the initial hand wait.

Use the grip component's hand-position preview to author fingers, and its Allowed Limbs, preferred limb and seat to select the correct hand. Keep Use On Action disabled: gearbox-driven paddle events coordinate ownership directly. The demo uses a .06-second outbound reach, .28-second return and .10-second finger blend.

Paddles use their own **Downshift Delay**, defaulting to **0.25 seconds** from the latest reduction. Each further reduction restarts it; only the final request presses the left paddle. Upshifts cancel a pending left-paddle press, and first gear, N and R bypass the delay. Set zero for immediate response. This wait precedes requesting a hand; direct `Press()` calls remain immediate requests. The Bus gear lever retains its separate 0.75-second setting.

## Twist grips, hand levers and parking brakes

`AnchoredControlAnimator` displays service-brake, clutch and handbrake levers using an `AnchoredRotation`. Add a separate instance for each lever and choose its Input: ServiceBrake, Clutch or Handbrake. `TwistThrottleAnimator` inherits the shared motion directly and displays resolved propulsion; its Inspector hides the lever Input selector because it overrides sampling. Assign a stationary Anchor outside Moving Part, choose the local axis and endpoint angles, then set independent Press Duration and Release Duration. These components only present existing mechanics; they do not apply braking or propulsion itself. The Inspector Preview slider temporarily shows any normalized value and restores the original local transform on Inspector closure, Restore Preview, recompilation or entering Play.

The Motorcycle demo has a rotating right throttle sleeve (32 degrees), a right front-brake lever driven by resolved ServiceBrake, and a left clutch lever driven by Clutch. The prepared right grip surface and palm contact are children of the sleeve, so the hand follows its rotation without being transferred away from the handlebar. The handbrake input remains the existing motorcycle parking/rear-wheel brake; the front hand lever displays the normal service brake. Left Shift operates clutch; W and S use the existing forward/braking input flow. The clutch and brake lever meshes move independently of the held grip; this does not add per-finger reaching to those levers.

Car includes a visible parking-brake lever following Space/Handbrake. These controls use shipped metal/rubber materials. Use an AnchoredControlAnimator instance with Input = Handbrake. Motorcycle brake and clutch use the same concrete component with their corresponding inputs. Shared timing, limb synchronization and reversible preview are preserved.

## Tutorial: provide your own values without replacing the animator

1. Add a built-in control animator matching the model, e.g. Pedal Animator or Throttle Animator. Preview its motion first.
2. Implement `IInteriorValueSource.ReadValue()` on your own MonoBehaviour. Return the value expected by that animator (for a pedal, 0..1). Disabled/invalid or non-finite assigned sources are neutral; they do not silently switch to vehicle input.
3. Assign the component to **[Animator] > Data Source**. Configure its ordinary response/range fields, then **[Animator] > Motion > Moving Part / Anchor / Local Axis** for an anchored control.
4. Connect **[Animator] > IK contact > Handle** and choose **Wait For Handle**. Set the associated handle's **Actions** when it should borrow a limb.
5. Observe **[Animator] > Signals and callbacks > On Value Changed** for the actual animated value. To drive Unity character Animator parameters, use your character script/Handle Animator Binding as appropriate; the vehicle control animator does not select your character's steering Blend Tree states automatically.

**Example: `ApplicationPedalSource.cs`**

<!-- example: ApplicationPedalSource.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public sealed class ApplicationPedalSource : MonoBehaviour, IInteriorValueSource
    {
        [Range(0, 1)] public float demand;
        public float ReadValue() => Mathf.Clamp01(demand);
    }
}
```

## Tutorial: author your own model motion

For a custom mechanical mapping, derive a ControlAnimator from the existing VehicleModule contract. It participates in the Interior presentation phase; it is separate from Unity Animator. Use a dedicated model pivot and keep the contact anchor beneath it.

1. Derive `ControlAnimator`. Override `Configure` and call `base.Configure(vehicle)` so a paired ControlHandle can be connected.
2. Override `Step(vehicle, command, deltaTime)` to capture your target value. The vehicle scheduler calls Step after registration; do not also apply the same input in Update.
3. Evaluate smoothing/model motion once in your chosen update pass. Use `WaitForContact()` to honor the configured handle arrival contract. Respect `automaticMotion` when writing geometry.
4. Override `InteractionValue` if the handle's generic value events should observe your custom motion. Release contact ownership at rest and dispose it on disable; when overriding OnDisable, call the base implementation.
5. If Timeline or another Unity Animator owns the mesh, disable **[Animator] > Automatic Motion** and explicitly supply the interaction value/contact signals your integration requires. Merely moving a mesh does not publish every package action automatically.
6. Register the new module with the vehicle, configure the handle's Animator link, then test missing handle, no passenger, disabled animator, seat exit and an interrupted reach.

### Complete custom control animator

Add this component under the vehicle, register/discover it as an Interior module, and assign **Application Lever Animator > Motion > Moving Part / Anchor / Local Axis**. Pair it with a `ControlHandle` (for example ThrottleHandle) using **Application Lever Animator > IK contact > Handle** and the handle's **Animator** field. It displays throttle magnitude; it does not write throttle commands back to the vehicle.

**Example: `ApplicationLeverAnimator.cs`**

<!-- example: ApplicationLeverAnimator.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public sealed class ApplicationLeverAnimator : ControlAnimator
    {
        public AnchoredRotation motion = new AnchoredRotation();
        [Min(0.01f)] public float responseSeconds = 0.2f;
        public float maximumAngle = 45;
        private float targetValue, value;
        public override Vector3 InteractionValue => new Vector3(value, 0, 0);

        public override void Configure(VehicleController vehicle)
        {
            base.Configure(vehicle);
            // Capture once from the authored neutral model pose before motion begins.
            motion.CaptureRestPose();
        }

        public override void Step(VehicleController vehicle, Command command, float deltaTime)
        {
            targetValue = float.IsFinite(command.Throttle)
                ? Mathf.Clamp01(Mathf.Abs(command.Throttle)) : 0;
        }

        private void LateUpdate()
        {
            if ((targetValue > 0 || value > 0) && !WaitForContact()) return;
            value = Mathf.MoveTowards(value, targetValue,
                Time.deltaTime / Mathf.Max(0.01f, responseSeconds));
            if (automaticMotion) motion.SetAngle(value * maximumAngle);
            if (value == 0 && targetValue == 0) ReleaseContact();
        }

        protected override void OnDisable()
        {
            targetValue = value = 0;
            if (automaticMotion) motion.SetAngle(0);
            base.OnDisable();
        }
    }
}
```

This example exposes its resolved value to the paired handle's generic value tracking. To add a dedicated Inspector value callback, declare a `UnityEvent<float>` and invoke it once when the resolved value changes. The common ControlAnimator Inspector groups such callbacks under **Signals and callbacks**. Supply additional gameplay behavior through your mechanic/input layer rather than making a visual mapping own the engine.

For a simpler variation, subclass a concrete animator and reuse its SetValue/SetImmediate/FollowInput contract rather than duplicating smoothing and contact synchronization. Override only the mapping you can actually customize; private internals of a concrete animator are not independent extension hooks.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed cockpit instruments and bindings API](../API/Interior.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### AircraftHud

- **AircraftHud** — `public event Action<Telemetry> Changed` — After the HUD receives an updated reading. Payload: Telemetry snapshot.
- **AircraftHud** — `public virtual void Bind(VehicleController owner)` — Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription.
- **AircraftHud** — `public override void Configure(VehicleController owner)` — Stores the vehicle whose hover transition geometry should be displayed.

### AnchoredControlAnimator

- **AnchoredControlAnimator** — `public UnityEvent<float> onValueChanged` — After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request.
- **AnchoredControlAnimator** — `public void ResetMotion()` — Restores value zero and the released angle. Disabling also releases.
- **AnchoredControlAnimator** — `public void SetValue(float value)` — Applies a finite normalized preview/API value, clamped to 0..1; does not command a mechanic.
- **AnchoredControlAnimator** — `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle.

### AnchoredRotation

- **AnchoredRotation** — `public virtual void CaptureRestPose()` — Captures the currently authored rest pose for this geometry mapper or blade.
- **AnchoredRotation** — `public virtual Vector3 GetPointAtAngle(Vector3 meshLocalPoint, float degrees)` — Returns the neutral-frame point after applying a specified rotation angle.
- **AnchoredRotation** — `public virtual void SetAngle(float degrees)` — Immediately applies a moving-part/geometry rotation in degrees.
- **AnchoredRotation** — `public virtual bool TryGetPose(float degrees, out Vector3 position, out Quaternion orientation)` — Computes a pose from the captured anchored rest frame when geometry references are valid.

### CarHud

- **CarHud** — `public event Action<Telemetry> Changed` — After the HUD receives an updated reading. Payload: Telemetry snapshot.
- **CarHud** — `public virtual void Bind(VehicleController selected)` — Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription.

### ClutchSource

- **ClutchSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

### CommandValueSource

- **CommandValueSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

### ControlAnimator

- **ControlAnimator** — `public override void Configure(VehicleController vehicle)` — Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy.

### EngineRpmSource

- **EngineRpmSource** — `public override float ReadValue()` — Reads a scalar control or instrument source in its documented normalized or physical unit.

### FuelTank

- **FuelTank** — `public event Action Emptied` — On the transition to empty fuel. No payload.
- **FuelTank** — `public event Action<float> FuelChanged` — After actual fuel quantity changes. Payload: current litres, not the requested transfer amount.
- **FuelTank** — `public event Action Refuelled` — After an actual increase in fuel, including `SetFuel`. No payload; query quantity if needed.
- **FuelTank** — `public virtual float Drain(float litres)` — Removes a finite nonnegative requested number of litres, bounded by available fuel, and returns the actual litres removed.
- **FuelTank** — `public virtual void Fill()` — Sets quantity to capacity through `SetFuel`, with normal actual-change notifications.
- **FuelTank** — `public virtual float Refuel(float litres)` — Adds up to the requested litres, limited by capacity, and returns actual transfer.
- **FuelTank** — `public virtual void SetFuel(float litres)` — Sets fuel quantity within capacity and publishes actual quantity/empty/refuel transitions.
- **FuelTank** — `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle.

### GasSource

- **GasSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

### GearLeverAnimator

- **GearLeverAnimator** — `public bool AnimateGear(int gear)` — Queues the latest accepted visual target without changing the gearbox. Returns false on invalid rig/pose.
- **GearLeverAnimator** — `public override void Configure(VehicleController vehicle)` — Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy.
- **GearLeverAnimator** — `public void RefreshBinding()` — Unsubscribes the old gearbox, releases any hand and silently synchronizes the new source.
- **GearLeverAnimator** — `public bool SetImmediate(int gear)` — Silently applies a configured pose and releases active ownership. Returns false on invalid rig/pose.
- **GearLeverAnimator** — `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle.
- **GearLeverAnimator** — `public void Tick(float deltaTime)` — Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.
- **GearLeverAnimator** — `public bool TryGetPosition(int gear, out GearLeverPosition position)` — Returns a unique finite pose; rejects duplicates, missing gears and values below -1.

### GearPaddleAnimator

- **GearPaddleAnimator** — `public UnityEvent onPressed` — Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction.
- **GearPaddleAnimator** — `public virtual void AnimateShift(int previousGear, int nextGear)` — Requests a presentation gesture for an accepted change from the previous gear to the next gear.
- **GearPaddleAnimator** — `public virtual void Press()` — Requests a paddle presentation press in the selected shift direction.
- **GearPaddleAnimator** — `public virtual void ResetMotion()` — Clears presentation requests and restores the released/default motion state.
- **GearPaddleAnimator** — `public virtual void Tick(float deltaTime)` — Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.

### GearShiftAnimator

[GearShiftAnimator](../API/Interior.md#gearshiftanimator) gives the full declared contract.

- `public virtual void Bind(Engine source)` — Connects the selected source.
- `public override void Configure(VehicleController vehicle)` — Binds the component to its configured owner and selected source.
- `public virtual void RefreshBinding()` — Current refresh binding.

### HandbrakeSource

- **HandbrakeSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

### HandleCommandInput

- **HandleCommandInput** — `public static float Read(Command command, HandleInput input)` — Maps one `HandleInput` choice to the corresponding Command channel for cockpit presentation. Handbrake returns one while held and zero when released.

### HandleMotion

- **HandleMotion** — `public virtual void SetOffset(float offset)` — Resets `movingPart` to the independent anchor and applies rotation in degrees or translation in local units. Invalid/nonfinite/self-descendant frames are ignored.
- **HandleMotion** — `public virtual void SetValue(float value)` — Clamps a fraction to 0–1, maps it between minimum and maximum, then applies `SetOffset`. Rotation uses degrees; translation uses local distance.

### IGearShiftAnimator

- `void AnimateShift(int previousGear, int nextGear)` — Requests a presentation gesture for an accepted change from the previous gear to the next gear.

### IInteriorValueSource

- `float ReadValue()` — Reads a scalar control or instrument source in its documented normalized or physical unit.

### IndicatorSwitchBinding

- **IndicatorSwitchBinding** — `public virtual void Synchronize(bool immediate)` — Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.
- **IndicatorSwitchBinding** — `public virtual void Tick(float deltaTime)` — Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.

### InteriorValueSource

- **InteriorValueSource** — `public abstract float ReadValue()` — Reads a scalar control or instrument source in its documented normalized or physical unit.

### ISteeringIntentSource

- **ISteeringIntentSource** — `float ReadSteeringIntent()` — Reports requested steering independently from the resolved visual angle, so released input starts hand return while the wheel is still self-centering.

### PedalAnimator

- **PedalAnimator** — `public UnityEvent<float> onValueChanged` — After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request.
- **PedalAnimator** — `public virtual void FollowInput()` — Releases a manual selection/value override and resumes configured input following.
- **PedalAnimator** — `public virtual void ResetMotion()` — Clears presentation requests and restores the released/default motion state.
- **PedalAnimator** — `public virtual void SetImmediate(float value)` — Takes external value ownership, clamps normalized travel and applies it immediately; `onValueChanged` reports an actual displayed-value change.
- **PedalAnimator** — `public virtual void SetValue(float value)` — Clamps a fraction to 0–1, maps it between minimum and maximum, then applies `SetOffset`. Rotation uses degrees; translation uses local distance.
- **PedalAnimator** — `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle.
- **PedalAnimator** — `public virtual void Tick(float deltaTime)` — Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.

### PitchSource

- **PitchSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

### ProfileSwitchBinding

- **ProfileSwitchBinding** — `public virtual bool SetOn(bool on)` — Requests onProfileId when on is true, otherwise offProfileId.
- **ProfileSwitchBinding** — `public virtual void Synchronize(bool immediate)` — Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.
- **ProfileSwitchBinding** — `public virtual void Tick(float deltaTime)` — Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.

### RearMirrors

- **RearMirrors** — `public event Action<int, bool> MirrorEnabledChanged` — When one mirror's eligibility changes. Payload: mirror index and bool.
- **RearMirrors** — `public event Action<bool> MirrorsEnabledChanged` — When whole-system mirror eligibility changes. Payload: bool.
- **RearMirrors** — `public virtual void SetCameraPose(int index, Vector3 localPosition, Quaternion localRotation)` — Sets local camera position/rotation for the indexed mirror. The index must be valid; a missing camera is ignored.
- **RearMirrors** — `public virtual void SetMirrorEnabled(int index, bool value)` — Changes eligibility of one mirror entry.
- **RearMirrors** — `public virtual void SetMirrorsEnabled(bool value)` — Changes the whole mirror system's rendering availability.

### RollSource

- **RollSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

### RotaryAnimator

- **RotaryAnimator** — `public UnityEvent<float> onValueChanged` — After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request.
- **RotaryAnimator** — `public event System.Action<float> ValueChanged` — When the requested instrument value changes. Payload: value in configured source units; this is not a motion-arrival notification.
- **RotaryAnimator** — `public virtual void Bind(MonoBehaviour valueSource)` — Sets the ongoing instrument value source; `null` releases source ownership for explicit value API control.
- **RotaryAnimator** — `public virtual void SetImmediate(float value)` — Takes external value ownership, clamps normalized travel and applies it immediately; `onValueChanged` reports an actual displayed-value change.
- **RotaryAnimator** — `public virtual void SetNormalizedValue(float normalized)` — Maps a normalized fraction across an instrument's configured physical value range.
- **RotaryAnimator** — `public virtual void SetValue(float value)` — Clamps a fraction to 0–1, maps it between minimum and maximum, then applies `SetOffset`. Rotation uses degrees; translation uses local distance.
- **RotaryAnimator** — `public virtual void Tick(float deltaTime)` — Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.

### ServiceBrakeSource

- **ServiceBrakeSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

### SpeedValueSource

- **SpeedValueSource** — `public override float ReadValue()` — Reads a scalar control or instrument source in its documented normalized or physical unit.

### SteeringSource

- **SteeringSource** — `public override float ReadValue()` — Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.

- **SteeringSource** — `public virtual float ReadSteeringIntent()` — Returns the owning vehicle's Command.Steering; ReadValue continues to report the configured resolved/raw steering for visible wheel rotation.

### SteeringStickAnimator

- **SteeringStickAnimator** — `public override void CalibrateRestPose()` — Captures the model's current neutral presentation frame for later control animation.
- **SteeringStickAnimator** — `public override void PrepareHandPose()` — Prepares the hand pose associated with this cockpit animator.

### SteeringWheelAnimator

- **SteeringWheelAnimator** — `public virtual void CalibrateRestPose()` — Captures the model's current neutral presentation frame for later control animation.
- **SteeringWheelAnimator** — `public virtual void PrepareHandPose()` — Prepares the hand pose associated with this cockpit animator.
- **SteeringWheelAnimator** — `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle.

### SwitchAnimator

- **SwitchAnimator** — `public UnityEvent<SwitchPosition> onPositionChanged` — After a changed switch detent request. Payload: `SwitchPosition`; silent immediate synchronization does not invoke it.
- **SwitchAnimator** — `public UnityEvent<bool> onValueChanged` — After this control's value changes. Payload: the event's value type; `PedalAnimator` reports displayed travel, `SwitchAnimator` reports a changed bool request.
- **SwitchAnimator** — `public event Action<SwitchPosition> PositionChanged` — When requested switch detent changes. Payload: `SwitchPosition`; distinguish all three positions with this event.
- **SwitchAnimator** — `public event Action<SwitchPosition> PositionReached` — When switch travel settles at its detent. Payload: `SwitchPosition`.
- **SwitchAnimator** — `public event Action<bool> Switched` — When switch presentation settles. Payload: bool `IsOn`; negative and positive three-position states both count as on.
- **SwitchAnimator** — `public event Action<bool> ValueChanged` — When the requested binary `IsOn` state changes. Payload: bool. Moving between negative and positive detents keeps `IsOn` `true` and does not emit this event. Immediate synchronization is silent.
- **SwitchAnimator** — `public virtual void Prepare()` — Initializes the contact or synchronizes its initial state without requesting a limb.
- **SwitchAnimator** — `public virtual void SetImmediate(bool value)` — Silently synchronizes Positive/Neutral, displayed value and motion without request or settlement callbacks.
- **SwitchAnimator** — `public virtual void SetPosition(SwitchPosition position)` — Requests a detent. Invalid enum values throw `ArgumentOutOfRangeException`; Negative in binary mode throws `InvalidOperationException`. A changed request starts travel and emits request events.
- **SwitchAnimator** — `public virtual void SetPositionImmediate(SwitchPosition position)` — Silently synchronizes a switch detent and displayed pose without issuing control events.
- **SwitchAnimator** — `public virtual void SetValue(bool value)` — Requests Positive for `true` and Neutral for `false`. Changed requests emit position/bool notifications and start travel.
- **SwitchAnimator** — `public virtual void Tick(float deltaTime)` — Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.
- **SwitchAnimator** — `public virtual void Toggle()` — Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.

### ThrottleAnimator

- **ThrottleAnimator** — `public event System.Action<float> ValueChanged` — When the requested instrument value changes. Payload: value in configured source units; this is not a motion-arrival notification.
- **ThrottleAnimator** — `public override void Configure(VehicleController owner)` — Stores the vehicle whose hover transition geometry should be displayed.
- **ThrottleAnimator** — `public virtual void FollowVehicle()` — Releases external presentation ownership and resumes vehicle-state following.
- **ThrottleAnimator** — `public virtual bool PrepareHandPose()` — Prepares the hand pose associated with this cockpit animator.
- **ThrottleAnimator** — `public virtual void SetThrottle(float value)` — Takes external ownership of normalized throttle-lever presentation; `FollowVehicle` releases that override.
- **ThrottleAnimator** — `public override void Step(VehicleController owner, Command command, float deltaTime)` — Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle.

### TwistThrottleAnimator

[TwistThrottleAnimator](../API/Interior.md#twistthrottleanimator) gives the full declared contract.

### YokeAnimator

- **YokeAnimator** — `public override void CalibrateRestPose()` — Captures the model's current neutral presentation frame for later control animation.

### Custom mirror rendering and resource ownership

Subclass `RearMirrors` and override `protected virtual bool RenderMirror(RearMirror mirror, RenderTexture target)` to submit your renderer's camera request. Return true only when rendering was submitted successfully. A false result advances the refresh timer but does not consume the successful-render budget for that frame. The built-in implementation supports the built-in pipeline and supported SRP render requests.

The scheduler restores the camera's previous target, enabled state, field of view, near/far planes and culling mask when releasing a mirror. Empty or null mirror lists release owned resources. If entries share a camera or display surface, the first valid entry owns that binding. Assign separate cameras and surfaces for independently rendered mirrors.

Internally created textures follow changes to requested resolution/aspect and are released by the component. A caller-provided texture remains caller-owned and is never resized or destroyed by the mirror component.
