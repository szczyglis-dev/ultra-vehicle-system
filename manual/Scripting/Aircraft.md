# Aircraft force, controls and landing gear

Aircraft motion combines a flight strategy, shared engine/input mechanics and separately authored control surfaces and landing gear. The flight profile decides how commands become body forces and torques. Exterior components present those decisions and coordinate ground contacts.

Choose the movement family from the intended control behavior before tuning the mesh animation. Assisted flight, body-rate aerobatics and jet response are parameter combinations in one fixed-wing strategy; changing how far a rendered elevator rotates does not change the authority of those strategies.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `AerobaticAirplaneProfile` | Supplies body-rate preset defaults; inherits all behavior. |
| `AircraftControlSurfaces` | Presents the configured control-surface motion. |
| `AirplaneGroundContact` | Tracks ground support and ground/air authority blending. |
| `AirplaneProfile` | Owns all fixed-wing flight logic and editable configuration. |
| `HelicopterProfile` | Supplies rotor-spooled lift, tilt-driven movement and altitude hold. |
| `HoverProfile` | Supplies direct thrust, strafe, clearance support and assisted leveling. |
| `HoverVisuals` | Applies configured hover mount and wheel tilt. |
| `JetProfile` | Supplies relative-airflow fighter preset defaults; inherits all behavior. |
| `LandingGear` | Owns deployment sequencing and physical gear-contact availability. |
| `LandingGearPart` | Maps deployment progress to a door/strut pose. |
| `LandingGearSuspensionPart` | Describes load-driven hinge response for a gear part. |
| `Propulsion` | Supplies rotor/propeller visuals and shared spool state. |

## Flight families

`AircraftControlSurfaces` is the visual control layer for elevators, ailerons, rudders, flaps and airbrakes. Its child `AircraftControlSurface` entries map the resolved axes to authored hinge motion. This makes a surface reusable across models: its axis, sign and travel describe the mesh, while the flight profile describes flight authority.

Normally the module follows vehicle state. `SetControls` takes an external presentation request and `FollowVehicle` returns ownership to the vehicle. `SetFlaps` and `SetAirbrake` set the corresponding normalized channels. Observe `ControlsChanged`, `FlapsChanged`, `AirbrakeChanged` and `ExternalControlChanged` when another presentation must follow these choices.

For a custom surface, extend the geometry/presentation layer rather than encoding mesh names in a flight profile. For a custom flight response, extend the profile and retain or replace surface presentation independently. Check signs at low input first: a reversed hinge axis should be corrected on the surface mapping, not by reversing pilot pitch for the whole aircraft.

The profile is authoritative for the aircraft settings it writes during configuration. For example, `AirplaneProfile.Configure` supplies engine and shared steering/braking/suspension settings from aircraft configuration. Tune those profile values rather than placing competing values on a module that the next configuration pass overwrites.

A propeller or jet mesh is presentation. Physical thrust acts on the root body through the movement implementation; visible spinning parts do not create thrust by their transform motion. This allows the same flight behavior to use another aircraft model, provided its contacts and presentation references are authored appropriately.

Airplane uses assisted pitch/bank and flight-path behavior. `AerobaticAirplane` requests body pitch/roll/yaw rates without auto-leveling. Jet adds directional pressure/parasite/induced drag and G-limited lift/trajectory response. All use native forces/torques and shared ground-wheel mechanics.

`AirplaneGroundContact` records native contact, applies takeoff grace, and blends ground/air authority. Gear wheels are free rolling: set `Drive` off. Tire feedback can include the contact-relative touchdown spin-up difference. Ground steering/brakes apply only through applicable contact handling.

Engine/thrust, flight response and visible control motion are separate responsibilities. `AircraftControlSurfaces` animates hinge references; it does not calculate aerodynamic authority from rendered flap geometry.

## Helicopter and hover movement

`HelicopterProfile` and `HoverProfile` both derive from `AirProfile` and accept a wheel-free configuration. A drone can use either family depending on its control model; see the [aircraft setup guide](../Aircraft.md).

Helicopter lift scales with squared `Propulsion.SpeedNormalized`. Altitude hold captures the current body height while manual lift is active and regulates that target after lift release, provided engine power and rotor spool are sufficient. Neutral horizontal drift braking also requires automatic leveling and no movement demand. Hold state belongs to the vehicle's `Drive` module and is cleared when power/hold conditions cease or the vehicle is teleported.

Hover applies forward thrust from `Throttle`, sideways thrust from `Strafe`, yaw from `Steering + Yaw` and vertical demand from `Lift`. Surface support queries external ground below the body and adds upward clearance correction. It does not capture an absolute altitude target. `HoverVisuals` supplies mount/wheel presentation independently of those forces.

For custom input, submit commands through the vehicle's input provider; do not add another force loop to the visible rotor or mount. Extend the relevant profile for different movement or a direct `DriveProfile` subclass for an independent flight model. See [Custom drive profiles](DriveProfiles.md#create-an-independent-profile-from-scratch), [Helicopter API](../API/Aircraft.md#helicopterprofile) and [Hover API](../API/DriveProfiles.md#hoverprofile).

## Gear states and pose conventions

Deployment is a sequence, not just a normalized animation value. A request may need clearance checks, door timing and suspension alignment before physical contacts can change. Keep ordinary gameplay on `SetDeployed`/`Toggle` so these checks remain meaningful.

The two normalized conventions serve different consumers: retraction grows toward the retracted pose, while deployed fraction grows toward the deployed pose. Name application variables accordingly and convert explicitly. Passing a retraction fraction into a deployed-value consumer reverses the mechanism even though both values are in the range zero to one.

`LandingGear` owns parts and native wheel contacts. Retraction can be rejected by grounded/clearance policy or suspension alignment. Fully deployed gear enables physical wheel contact; hull colliders remain the belly envelope when retracted.

| API | Meaning |
| --- | --- |
| `SetDeployed` / `Toggle` | Requested sequence, returns acceptance |
| `LandingGearPart.SetRetraction` | 0 deployed, 1 retracted |
| `LandingGearPart.SetValue` / `DeployedFraction` | 1 deployed, 0 retracted |
| `CaptureDeployedPose` | Capture the authored model baseline |
| `ResetGear` | Immediate explicit reset, bypassing interlocks |
| `LandingGearSuspension.ResetSuspension` | Clear load-driven hinge displacement/velocity |

A gear part's independent anchor defines the pivot; signed maximum is retraction relative to deployed pose. The part retains its mesh's deployed offset. Extension/retraction delays coordinate doors and struts.

## Request gear from another input system

The adapter returns the gear component's acceptance result. A cockpit switch may display the requested detent, while gear-state lamps should observe actual state. Retain this distinction when connecting an animated switch: a rejected request should not be presented as completed retraction.

A spawn/reset tool can intentionally use the immediate reset API. Use it only for spawning or resetting the vehicle; normal pilot input should retain the grounded and alignment checks.

Assign `LandingGear` and call `SetGear` from an Input Action/UI/AI adapter. Rejected requests leave the mechanic in control of its actual state.

**Example: `LandingGearControl.cs`**

<!-- example: LandingGearControl.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class LandingGearControl : MonoBehaviour
    {
        public LandingGear gear;
        public bool SetGear(bool deployed) => gear && gear.SetDeployed(deployed);
    }
}
```

Observe `StateChanged` for a display. Use `ResetGear` only for spawn/reset rules, not to force an unsafe ordinary request.

## Hinged support

`LandingGearSuspension` coordinates loaded hinge motion for the configured legs. Each `LandingGearSuspensionPart` identifies the `LandingGearPart`, its native wheel and the hinge's physical response. This is how a visual strut can bend under load while the native wheel still supplies primary suspension/contact.

Set the fully deployed geometry and hinge direction before tuning response. `localAxis` defines the allowed rotation; signed travel distinguishes the direction in which load opens the mechanism. Spring and damping coefficients act around that axis, and angular inertia controls response to torque. If the wrong leg/wheel is referenced, tuning coefficients only changes the response to the wrong load.

Use `ResetSuspension()` for an explicit reset of hinge history. Retraction and loaded-leg alignment are coordinated with `LandingGear`; do not continuously rotate the same strut from another animator. A custom load model can replace the hinge behavior while retaining deployment sequencing, provided the deployed pose and alignment contract remain consistent.

Author the fully deployed pose first and capture its baseline. The hinge anchor belongs outside the moving subtree so rotating the part does not also move the frame from which its angle is measured. Signed travel should match the model's actual axis; inspect a small displacement before entering full retraction values.

The load-driven hinge is a reduced model driven by the configured wheel, not an additional native leg rigidbody. Tune inertia, spring torque and damping in their documented angular units. Adding a second physics hinge to the same visual part would introduce another motion owner rather than increasing the fidelity of this model.

`LandingGearSuspensionPart` is a component referencing a gear part, wheel, hinge axis, signed opening and authored opening. Spring torque uses N·m/rad, damping N·m·s/rad, inertia kg·m². Native wheel load drives a reduced hinge model; it does not create a separate `Rigidbody` per leg. Retraction waits for straight alignment.

## Telemetry

AGL is a gravity-aligned probe distinct from world-Y altitude. GForce subtracts gravity from velocity change; rest is 1 G, free fall 0 G. Reset/re-enable clears differentiation history. Use [cached telemetry](Events.md) rather than sampling the body separately in a display.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed flight and landing gear API](../API/Aircraft.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### AerobaticAirplaneProfile

[AerobaticAirplaneProfile](../API/Aircraft.md#aerobaticairplaneprofile) gives the full declared contract.

| Method | Role |
| --- | --- |

### AircraftControlMotion

[AircraftControlMotion](../API/Aircraft.md#aircraftcontrolmotion) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void SetValue(float normalized)` | Applies normalized aircraft-control travel to its authored rotation/translation mapping. |

### AircraftControlSurface

[AircraftControlSurface](../API/Aircraft.md#aircraftcontrolsurface) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void SetControls(float pitch, float roll, float yaw, float flap, float airbrake)` | Applies pitch/roll/yaw/flap/airbrake contributions through this surface's authored axis and motion mapping. |

### AircraftControlSurfaces

[AircraftControlSurfaces](../API/Aircraft.md#aircraftcontrolsurfaces) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Smooths external or command-following pitch/roll/yaw, applies surface geometry and publishes changed presentation. |
| `public virtual void SetControls(float pitch, float roll, float yaw)` | Takes external pitch/roll/yaw presentation ownership for configured control-surface entries; `FollowVehicle` restores mechanic-following. |
| `public virtual void FollowVehicle()` | Releases external presentation ownership and resumes vehicle-state following. |
| `public virtual void SetFlaps(float value)` | Updates normalized flap presentation for the configured aircraft control surfaces. |
| `public virtual void SetAirbrake(float value)` | Updates the normalized aircraft airbrake presentation request. |

| Event / callback | Role |
| --- | --- |
| `public event Action<Vector3> ControlsChanged` | When aircraft surface-control presentation changes. Payload: the component's pitch/roll/yaw Vector3 representation. |
| `public event Action<float> FlapsChanged` | When flap presentation request changes. Payload: normalized flap value. |
| `public event Action<float> AirbrakeChanged` | When airbrake presentation request changes. Payload: normalized airbrake value. |
| `public event Action<bool> ExternalControlChanged` | When aircraft surface presentation changes external/follow-vehicle ownership. Payload: external-control bool. |

### AirplaneGroundContact

[AirplaneGroundContact](../API/Aircraft.md#airplanegroundcontact) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Counts operational gear contacts, including tire-tread support, updates airborne/takeoff grace and blends ground/flight authority. |
| `public override void Configure(VehicleController vehicle)` | Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

### AirplaneProfile

[AirplaneProfile](../API/Aircraft.md#airplaneprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. |
| `public override float ResolveBoostDemand(VehicleController vehicle, Command command)` | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. |
| `public override float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. |
| `public override float ResolveExternalDriveIntent(VehicleController vehicle)` | Returns signed non-wheel propulsion intent used by shared coasting/contact policy. |
| `public override void Configure(VehicleController vehicle)` | Ensures propulsion/ground-contact helpers and writes aircraft-owned engine, steering, braking, grip/travel and suspension settings. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Runs the common fixed-wing physics pipeline using the configured control and aerodynamic models. |
| `public virtual Vector3 PressureDragAcceleration(Transform frame, Vector3 velocity)` | Evaluates jet pressure-drag acceleration from the supplied speed/state. |

### DriveProfile

[DriveProfile](../API/DriveProfiles.md#driveprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual Settings CreateSettings()` | Returns a fresh initial shared settings object for explicit creation/profile selection. |
| `public virtual void Configure(VehicleController vehicle)` | Empty base strategy setup hook; family implementations may ensure helpers and apply profile-owned settings. |
| `public abstract void Step(VehicleController vehicle, Command command, float deltaTime)` | Abstract movement-strategy step called by Drive; apply the selected family's movement using this vehicle context. |
| `public virtual DriveProfile Clone()` | Creates an independent serialized profile-configuration copy; configure it on its destination vehicle before use. |
| `public virtual float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. |
| `public virtual float ResolveExternalDriveIntent(VehicleController vehicle)` | Returns signed non-wheel propulsion intent used by shared coasting/contact policy. |

### FreeProfile

[FreeProfile](../API/DriveProfiles.md#freeprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. |

### HelicopterProfile

[HelicopterProfile](../API/Aircraft.md#helicopterprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. |
| `public override float ResolveBoostDemand(VehicleController vehicle, Command command)` | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. |
| `public override void Configure(VehicleController vehicle)` | Ensures a Propulsion helper exists for helicopter presentation/spool integration. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Applies resistance, spool-dependent powered support, lift/height hold and commanded helicopter motion. |

### HoverVisuals

[HoverVisuals](../API/Aircraft.md#hovervisuals) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController owner)` | Stores the vehicle whose hover transition geometry should be displayed. |
| `public virtual Quaternion GetWheelTilt(WheelSetup wheel, HoverProfile profile)` | Returns the wheel's hover-transition presentation tilt. |

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### JetProfile

[JetProfile](../API/Aircraft.md#jetprofile) gives the full declared contract.

| Method | Role |
| --- | --- |

### LandingGear

[LandingGear](../API/Aircraft.md#landinggear) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Connects suspension, initializes authored deployment once and synchronizes gear-part/contact policy. |
| `public virtual void ResetGear(bool deployed)` | Synchronizes gear state immediately for spawn/reset, bypassing ordinary request interlocks. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances part delays/travel and gear state; retraction waits for unloaded suspension alignment before continuing. |
| `public virtual bool SetDeployed(bool deployed)` | Requests landing-gear deployment/retraction subject to clearance, ground and alignment interlocks. |
| `public virtual bool Toggle()` | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component. |

| Event / callback | Role |
| --- | --- |
| `public event Action<LandingGearState> StateChanged` | When deployment sequencing changes `LandingGearState`. Payload: actual sequence state; use this rather than treating request acceptance as arrival. |

### LandingGearPart

[LandingGearPart](../API/Aircraft.md#landinggearpart) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void CaptureDeployedPose()` | Captures the current gear-part pose as the fully deployed baseline. |
| `public override void SetValue(float normalized)` | Applies deployed fraction: 1 fully deployed, 0 fully retracted, retaining the captured deployed mesh offset and current suspension rotation. |
| `public virtual void SetRetraction(float amount)` | Applies landing-gear travel with zero deployed and one retracted. |
| `public virtual void Animate(bool deployed, float elapsed, float deltaTime)` | Applies gear-part deployment animation using its authored motion mapping. |
| `public virtual void SetImmediate(bool deployed)` | Synchronizes this part immediately to the requested deployed/retracted pose through its gear-part mapping. |

### LandingGearSuspension

[LandingGearSuspension](../API/Aircraft.md#landinggearsuspension) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Connects `LandingGear` and prepares changed runtime leg state while preserving authored deployed geometry in Edit Mode. |
| `public virtual void ResetSuspension()` | Clears load-driven landing-gear hinge displacement and velocity. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Uses native wheel load to advance each leg's bounded angular spring/damper/inertia model. |

### Propulsion

[Propulsion](../API/Aircraft.md#propulsion) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController owner)` | Stores the owner and resolves missing hull/engine references used by spool/propeller presentation. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event Action<float> SpeedChanged` | When resolved propulsion presentation speed changes. Payload: the component's current speed value; it does not set engine power. |

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
