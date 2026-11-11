# Burnout, nitro, wheelie and other actions

## Inspector starting points

| Action | Vehicle-root Inspector | First references/settings to check |
| --- | --- | --- |
| Burnout / propulsion boost | Modules > Drive > Burnout | Working Engine/Drive and compatible profile; grip/hold policy for wheel propulsion |
| Nitro | Modules > Engine > Nitro | Engine, amount/capacity, boost response, optional audio and exhaust-flame assets |
| Wheelie | Modules > Physics > Wheel Lift | Wheel/profile eligibility, selected lift wheels, target angle and force/response |

Add the chosen module through **Modules > Add module...**, expand its settings and enable the desired behavior. Configure the matching held input on the selected keyboard/ActionInput source, then apply/save. Test a short request and release before raising force/multipliers. The API snippets below are optional application control paths; no script is needed merely to configure the built-in action. Smoke/sound still require their separate consumers and references.

## Burnout launch

`Burnout` is a **Drive module** included when creating powered vehicles and by Full setup. Wheel propulsion uses a powered launch with tire/track spin, optional non-driven brake hold and timed grip recovery; Motorcycle uses the same wheel path as Wheeled. Other profiles use a held propulsion boost, with a modest extra bow lift for boats or increased native thrust for aircraft. WheelCollider slip remains the source of tire smoke and squeal.

- `WheeledProfile`, `MotorcycleProfile` and `TrackedProfile`: the wheel drivetrain keeps its RPM/gear/traction behavior. Enable non-driven brake hold for a stationary motorcycle burnout; a fully driven axle has no non-driven contact to hold.
- `BoatProfile`: stronger native hull thrust; Burnout also adds `boatBowLiftDegrees` through the existing powered-pitch spring. Water presence, propulsion/pitch switches, maneuver-angle and hull-tilt limits still apply. A dry hull cannot activate boost.
- `SubmarineProfile`: stronger forward and manually requested vertical propulsion while immersed; depth hold, drag and buoyancy keep their own behavior.
- `HoverProfile` and `HelicopterProfile`: greater requested thrust/collective authority. Neutral gravity compensation is not multiplied, rotor spool and configured support caps remain active.
- `AirplaneProfile` and its Jet/Aerobatic presets: Nitro directly increases thrust, native power capacity, forward speed envelope and engine RPM; no additional component is required. Burnout also increases native thrust.

On non-wheel profiles, Burnout provides a held propulsion boost rather than a timed wheelspin cycle. It supplies throttle and stops on release or braking. **Force Forward Direction** selects forward propulsion without changing existing momentum; disable it to retain the selected drive direction. Simultaneous Nitro and Burnout use the stronger non-wheel multiplier rather than multiplying both.

### Enable on a vehicle

1. Start with a working Wheeled or Motorcycle setup, with `Engine`, driven wheels, `Brakes` and `Friction` registered. A car with non-driven front wheels can use those wheels to hold its position during the initial spin.
2. Add **UltraVehicleSystem > Drive > Grounded > Burnout**, or use **Tools > UltraVehicleSystem > Add Component > Drive > Grounded > Burnout**. Vehicle creation and Full setup already include it; when adding it manually, register it in Vehicle Controller Modules.
3. Set **Spin Duration**, **Minimum End Speed**, **Grip Recovery Time**, **Torque Multiplier**, **Forward Grip** and **Sideways Grip**. The default forward/lateral scales are 0.55/0.4. Lateral grip reduction affects driven wheels only, retaining steering grip on non-driven front wheels. A lower Forward Grip allows more driven-wheel slip during the spin; it returns to the ordinary tire/surface grip as the cycle finishes.
4. If wanted, enable **Hold Non Driven Wheels** and tune **Hold Brake Torque**, **Hold Duration** and **Hold Release Time**. Only operational, non-driven wheels with the service-brake role are held. All-wheel drive has no eligible non-driven holding wheels.
5. Choose **Automatic Throttle** and **Throttle**. With automatic throttle on, holding the burnout request supplies a forward pedal before the brake, gearbox and clutch stages. With it off, supply the throttle yourself.
6. Configure **Burnout Key** on `KeyboardDriveInput`; its default is **Left Ctrl**. `ActionInput.burnout` accepts a custom action or the `Burnout` action in PlayerInput. Gamepad bindings are application-defined.

### Timing and guards

**Maximum Start Speed** defaults to 40 m/s (144 km/h), allowing activation while already driving. A supported, operational driven wheel is required to start. **Maximum Spin Speed** defaults to 60 m/s (216 km/h) and ends the wheelspin assistance early when the vehicle is already moving fast enough. Reverse demand, reverse gear, service braking, handbrake, a pressed clutch, a stopped engine and direct-pose control do not start the maneuver.

A held request starts one cycle. The minimum spin duration defaults to 3 seconds. Recovery starts only after that interval and reaching **Minimum End Speed**, default 12 m/s (43.2 km/h). Set the speed to zero for timing alone. **Sustain While Steering** (default on) retains wheelspin while steering exceeds **Sustain Steering Threshold** (default 0.15), allowing continued drifting/donuts while Ctrl stays held. The safety maximum speed always takes priority. Straightening the steering allows recovery once the other conditions are met. The non-driven brake hold has its own, normally shorter release interval, so the vehicle can start moving before the driven tires regain full grip. Holding the request after recovery does not restart another burnout; automatic throttle can continue as an ordinary forward pedal. Release and press again to request another low-speed launch, respecting **Cooldown**.

Releasing early immediately removes extra torque, automatic throttle and the brake hold; grip begins recovering over the configured interval. Service brake/handbrake and disabling the feature restore normal grip immediately. Releasing without a normal throttle pedal clears the automatic pedal rather than leaving hidden acceleration behind. `Burnout.ResetState()`, engine shutdown and component disable also reset the burnout request and state.

**Bypass Traction Control** prevents the optional TCS module from removing the intentional wheelspin while the burnout strength is nonzero. TCS resumes after recovery. Turning this option off leaves its normal intervention active. This option does not permanently change TCS settings, grip settings or the engine's authored torque/power/acceleration caps.

**Bypass Stability Control** skips Steering arcade handling and the powered-slide speed hold during burnout so those assists do not fight the drift. Both stability and traction settings are restored naturally when assistance ends; saved settings are not changed.

### API and effects

Use `Command.Burnout` or `InputBuffer.SetBurnout(bool)` for held input; `ExternalController` inherits the latter. `Burnout.SetBurnout(bool)` provides an independent API request. The module must be installed and enabled. `ResetState()` clears the request, cycle, brake hold and cooldown.

Read `IsActive`, `Strength`, `Progress` and `CooldownRemaining` for feedback. `Requested` reports the explicit module API request, while a Command can independently request a launch. Subscribe to `StateChanged` for transitions into/out of nonzero assistance. Settings live directly on the Burnout component.

Tire smoke and squeal need the normal `TireFeedback`, `TireSmoke` and `TireAudio`/Audio configuration. They use actual driven-wheel contact slip. Merely holding Ctrl with burnout disabled does not synthesize smoke or sound.

### Burnout demo

All powered Demo prefabs and scene vehicles include this Drive module. Select Car in the demo and hold **Left Ctrl** from standstill or while driving: Ctrl alone supplies throttle, spins the driven wheels while moving forward, and returns to full grip. The example uses a 3-second minimum spin, 0.4-second recovery, with the wheel hold disabled so the car moves while spinning. **Enter** independently requests the optional [Nitro](DrivingActions.md#nitro-boost) boost, which also supplies throttle.

See the exact [Burnout API](API/DriveDynamics.md#burnout), [clutch](Clutch.md) and [traction control](TractionControl.md) configuration.

## Nitro boost

`Nitro` supplies temporary charge-controlled boost while its input is held. Holding Nitro supplies full throttle automatically; `forceForwardDirection` defaults to true and immediately requests forward torque even while reversing, without waiting for standstill. Disable it to boost in the selected drive direction; no separate accelerator input is required. Releasing Nitro, braking or losing boost eligibility removes the automatic pedal. Wheel vehicles receive drivetrain output and optional grounded acceleration; boats, submarines, hovercraft and helicopters boost their native propulsion. Fixed-wing aircraft boost their native thrust directly through Nitro. Nitro remains optional and is not installed by Full setup.

For non-wheel profiles, Nitro boosts native propulsion; aircraft also use **Additional Power** and **Top Speed Multiplier**. Wheel-only acceleration and gearbox settings do not apply. Simultaneous Nitro and Burnout use the stronger non-wheel multiplier. A running engine, active Drive module and compatible profile are required.

### Add and configure

1. Add **Engine > Boost > Nitro** through Add Component or **Tools > UltraVehicleSystem > Add Component**. Register it on Vehicle Controller and apply configuration.
2. Leave **Engine** empty to resolve the registered engine, or assign it explicitly.
3. Tune **Torque Multiplier**, **Additional Power Kw**, **Acceleration Multiplier**, **Additional Acceleration** and **Top Speed Multiplier**. Zero Additional Acceleration uses engine torque alone.
4. Set **Build Up Time**, **Additional Max Rpm Percent**, **Allow Pitch Above Max Rpm** and **Lock Automatic Gear Changes**. Defaults are 0.2 seconds, +25% RPM and both switches enabled. The RPM increase is available headroom; boost does not force the engine to a target RPM. Manual gear requests retain their normal safety guards.
5. Under **Effects > Audio > Nitro Audio**, replace **Nitro On Clip**, **Nitro Loop Clip**, **Nitro Off Clip** or their **Audio Settings** as needed. Components added in the editor receive serialized defaults from the package Resources/Audio/Nitro folder; runtime-created components need explicit clip assignments. The loop follows RPM while boosting; gear changes do not replay the transition cues. Clear a clip or disable its Audio Settings to mute it.
6. Configure flames under **Effects > Exhaust Smoke > Nitro**. Import Demo for the optional default **Nitro Particle Prefab**, or assign your own. It uses the module's **Exhaust Points**. Aircraft retain Nitro flames even though ordinary exhaust smoke is suppressed; Propulsion Jets also increases emission using Nitro Rate Multiplier. See [exhaust particles](Particles.md#exhaust).
7. Hold the configured Nitro input; Nitro supplies throttle automatically and requests forward drive by default. `KeyboardDriveInput` defaults to **Enter**; `ActionInput.nitro` accepts an action reference or a PlayerInput action named `Nitro`.

Boost requires a running engine and propulsion demand. Wheel propulsion also requires operational driven wheels and an engaged drivetrain; aircraft landing gear is not a driven-wheel requirement. Braking, handbrake, depletion and direct-pose control stop it. **Require Ground Contact** and **Allow Reverse** retain their optional guards. Release removes assistance immediately; engine RPM continues to follow its normal load and clutch contracts.

### Supply and refilling

| Setting | Behavior |
| --- | --- |
| Capacity / Amount | Maximum and starting charge in consistent units. |
| Consumes Nitro | Disable for unlimited supply. |
| Full Tank Duration | Full-boost seconds per tank; consumption also scales with the current build-up fraction. |
| Minimum Activation Amount | Charge required to begin a use; an active use can spend its final partial charge. |
| Cooldown | Delay before another activation. An internal shift does not start a new cooldown. |
| Automatic Refill | Refill after release and Refill Delay, at Refill Per Second units/second. |

The Inspector shows charge and provides Refill/Empty buttons. The last partial charge scales that tick's output. Zero engine power/acceleration caps remain unlimited; temporary output never overwrites their saved settings.

### Input and scripting

Use `Command.Nitro`, `InputBuffer.SetNitro(bool)` or `Nitro.SetBoost(bool)` for held input, releasing it when input ends. `ExternalController` inherits the buffer API. Use `SetAmount`, `AddNitro` and `Refill` to supply charge. `ResetState()` clears transient state; `ResetState(true)` also refills. Assigned clips and particles remain customizable after initialization.

`Remaining`, `NormalizedAmount`, `Strength`, `IsBoosting` and `CooldownRemaining` expose state; `AmountChanged`, `BoostStateChanged` and `Depleted` provide notifications. See the [Nitro API](API/DriveDynamics.md#nitro) and [Inspector reference](InspectorReference/Engine.md#nitro).

<!-- example: NitroPickup.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

public class NitroPickup : MonoBehaviour
{
    public Nitro nitro;
    public float refillAmount = 25;

    public void Collect()
    {
        if (nitro) nitro.AddNitro(refillAmount);
    }
}
```

### Nitro demo

Both Car prefabs include Nitro with 15 seconds of supply and automatic refill (1-second delay, 25 units/second; four seconds to refill an empty 100-unit tank). Hold **W + Enter** for boost. The Exhaust Smoke module supplies flames at both outlets. **Left Ctrl** independently requests [burnout](DrivingActions.md#burnout-launch).

Demo Airplane and Jet use the same Nitro component: hold **Right Alt** for automatic forward throttle and additional native thrust, RPM and nozzle flames; **Comma** requests Burnout / propulsion boost. No separate afterburner component is required. Reset releases boost, clears retained flight throttle and engine output, and stops native wheel spin.

### Suspension kick and departure wheelspin

Optional launch effects are enabled by default:

- **Modules > Engine > Nitro > Suspension Kick** and **Modules > Drive > Burnout > Suspension Kick** lift the front and compress the rear. Adjust **Front Lift**, **Rear Compression**, **Rise Time** and **Return Time**. Nitro holds the pose during boost; burnout holds it until grip recovers.
- Burnout's **Suspension Kick > Maximum Forward Activation Speed** limits starting the effect (default 18 km/h); reverse movement is unrestricted. An active effect continues above this speed.
- **Modules > Engine > Nitro > Launch Wheelspin** configures a short grip reduction when accelerating.

Suspension kick requires wheel support and an active **Modules > Drive > Suspension**. Losing support or exceeding **Suspension Kick > Maximum Tilt** cancels it until the boost is released and pressed again.

## Wheel lift (wheelie)

`WheelLift` is an optional Physics module. It applies a bounded upward force at a configurable position and uses pitch feedback, angular damping, corrective torque and optional gravity compensation to raise and hold the front of a vehicle. It never assigns Rigidbody rotation, velocity or suspension settings. Pitch correction uses the gravity-level lateral axis, while Motorcycle Balance applies roll around the pitched longitudinal axis. This keeps bank corrections from becoming a heading change during wheelie. Pitch is measured across the full rotation, so passing vertical is not interpreted as a smaller angle. Without a request, a fresh/reset module applies no force.

Motorcycle profile creation automatically adds and registers this enabled, idle module. The Demo Motorcycle and Quad prefabs contain it; scene instances inherit it from their prefab. Keyboard input and the controls HUD detect an enabled, supported WheelLift component independently of Motorcycle Profile. Hold **Z** to lift and hold the front wheel; release to smoothly lower the pitch target and return to both wheels. Downshift/upshift remain **Q / E**, reset remains **R**, and burnout remains **Left Ctrl**.

Add manually via **UltraVehicleSystem > Physics > Wheels > Wheel Lift** or **Tools > UltraVehicleSystem > Add Component > Physics > Wheels > Wheel Lift** and connect available modules on the Vehicle Controller.

### Configuration

- `wheels`: lift at the average position of operational selected wheels; empty automatically selects steering wheels. Grounded wheels outside this selection supply support. Assign wheels belonging to this vehicle.
- `liftPoint`: optional Transform overrides the force application point. With no selected wheels, `localLiftPoint` is the fallback, relative to the vehicle.
- `targetAngle`: nose-up pitch in degrees relative to gravity (default 30). Place the force point ahead of the support axle. This component assists front-wheel lift, including several front wheels on a car.
- `maximumForce`: upward force cap in newtons, default 12000. `maximumLiftAcceleration` additionally limits upward force per chassis mass (default 8 m/s²) to help keep the support wheel loaded. `angleStrength` and `angleDamping` tune the inertia-aware pitch spring and damping. Bounded corrective torque arrests excessive rise or a forward dive; `maximumRecoveryAcceleration` limits this correction (default 300 rad/s²). `compensateGravity` offsets the weight moment about the supporting axle.
- `supportReboundDamping`, `maximumSupportDampingAcceleration`: suppress separation at the supporting tire after touchdown, using the actual contact normal and velocity relative to the road. Defaults are 10 1/s and 15 m/s². The impulse cannot reverse contact separation velocity; airborne motion, descent and pitching about a planted rear wheel are unaffected. Zero damping disables this response.
- `riseTime`, `releaseTime`: seconds to build or fade the force request. `forceCurve` shapes this ramp. `landingTime` (default 1 second) lowers the pitch target smoothly to zero; pitch control and necessary weight support remain until touchdown settles. `landingTimeout` bounds this phase (default 3 seconds). `ResetState` and disabling the component stop immediately.
- `minimumSpeed`, `maximumSpeed`: absolute forward speed bounds in m/s. `maximumRoll`, `safetyAngle`, `requireGroundContact` and `requireRunningEngine` control activation guards. Ground support is required on wheels outside the lifted selection by default. `groundContactGraceTime` (default .75 seconds) retains the wheelie angle through brief contact loss, then levels the active chassis for landing. There is no upward force without support. Braking, handbrake, stopped engine and speed guards initiate controlled lowering; a held request blocked by a guard must be released before restarting. Excessive tilt, direct control, reset and disabling clear assistance immediately. The effective target stays ten degrees below `safetyAngle`. There is no extra forward propulsion; use the normal throttle to travel on the rear wheel.

### Public API

<!-- example: WheelLiftControlGuide.cs -->
```csharp
using UltraVehicleSystem;
using UnityEngine;

public class WheelLiftControlGuide : MonoBehaviour
{
    public VehicleController vehicle;
    private WheelLift lift;

    private void Awake()
    {
        if (vehicle) vehicle.TryGetModule<WheelLift>(out lift);
    }

    public void StartLift()
    {
        if (!lift) return;
        lift.SetTargetAngle(30);
        lift.SetStrength(1); // Normalized request intensity, 0..1.
        lift.SetWheelLift(true); // Hold until ReleaseLift is called.
    }

    public void ReleaseLift()
    {
        if (lift) lift.SetWheelLift(false); // Controlled lowering.
    }

    public void StopImmediately()
    {
        if (lift) lift.ResetState(); // Clear request and assistance immediately.
    }
}
```

All public tuning fields can also be changed at runtime. `Command.WheelLift` and `InputBuffer.SetWheelLift(bool)` provide input-independent held control. `ActionInput.wheelLift` accepts an action reference or the PlayerInput action `WheelLift`; no default gamepad button is reserved. Keyboard requests are limited to Motorcycle profiles with an enabled registered WheelLift module. API requests support any wheel profile.

Telemetry: `Requested` (API request), `IsActive`, `IsLanding`, `Strength` (shaped assistance during lifting, full pitch authority while lowering), `CurrentAngle` (degrees), `AppliedForce` (newtons).

Events, declared at the top of the class: `WheelLiftStarted`, `WheelLiftStopped`, `StateChanged(bool)`. Start/stop describe assistance, so normal release stops after controlled lowering; disabling/reset ends it immediately. Repeated held requests do not repeat the start event.
