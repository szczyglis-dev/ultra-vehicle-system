# Drive profile configuration and extension

A drive profile describes how a movement family turns resolved commands into vehicle motion. A wheeled vehicle distributes propulsion through wheels; a boat responds to water support and drag; an aircraft applies flight forces. Shared modules still own the engine, input, passengers and presentation around that movement strategy.

Use a profile subclass to change a movement algorithm or its family-specific parameters. Use a module for an optional capability that should remain independently installable. This distinction keeps a custom movement mode from becoming a container for unrelated lights, sounds and interactions.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `Drive` | Executes the active strategy and holds per-vehicle movement history. |
| `DriveDefaults` | Builds initial settings for supported movement families. |
| `DriveProfile` | Defines settings creation, configuration, stepping and drive-demand resolution. |
| `ProfileSwitcher` | Owns two authored profiles and coordinates requests to change between them. |
| `ProfileTransition` | Component contract for geometry/contact changes during a transition. |
| `WheeledProfile` | Reusable wheeled strategy used by the inheritance example. |

For the built-in mode list, see [Drive profiles](../DriveProfiles.md).

## Ownership and lifecycle

The profile is stored in `VehicleController.driveProfile` through managed-reference serialization. It is a serializable object rather than a component with its own Unity `Update`. The `Drive` module supplies the vehicle context and timestep when calling its behavior.

Separate authored configuration from temporary simulation history. A drag coefficient belongs to the profile; the previous velocity used to estimate acceleration belongs to that vehicle's runtime state. This prevents a configuration copy or mode selection from accidentally importing another vehicle's momentum history. Treat repeated `Configure` calls as a supported operation.

`DriveProfile` is a serializable managed-reference strategy owned by a vehicle. `Drive` invokes its `Step` in the `Drive` phase. `Configure` may repeat; use it for local references, not implicit resetting of authored settings. Per-vehicle transient boat, hover and height-hold history belongs to `Drive`.

The extension hooks serve different stages:

| Hook | Responsibility |
| --- | --- |
| `CreateSettings()` | Returns initial shared `Settings` for explicit creation/mode selection. It does not run every tick or every configuration. |
| `Configure(vehicle)` | Resolves/applies profile setup for this vehicle. It must tolerate repeated calls. |
| `Step(vehicle, command, deltaTime)` | Applies movement behavior for one fixed tick. `deltaTime` is in seconds. |
| `RequiresWheels` | Declares whether wheel-definition validation must require wheels for this mode. |
| `ResolveDriveDemand(vehicle, command)` | Resolves the profile's propulsion intent for the surrounding mechanics. |
| `ResolveExternalDriveIntent(vehicle)` | Supplies signed intent from a non-wheel actuator. Shared coasting uses it to release native zero-torque tire holding. |
| `Clone()` | Copies profile configuration. `Configure` the result on its destination vehicle before using it. |

Override only the hooks needed by the new behavior. A subclass that retains the movement family can usually retain its settings and demand resolution while extending `Step`.

## Release forces without replacing a profile

The built-in controller API provides `ReleaseAllForces()`, `RestoreAllForces()` and `ForcesReleased`. Profiles expose corresponding methods taking a VehicleController, keeping transient release state on the vehicle. Use [the Inspector setup and full behavior contract](../DriveProfiles.md#release-and-restore-all-vehicle-forces) before adding application crash/recovery rules.

Release suspends both the profile and scheduled shared force assists, not just engine thrust. Restore resumes from current motion without clearing velocity. Explicit restore overrides the current automatic ignition-off interval; the next ignition cycle can release again. ResetVehicle remains independent; the demo invokes RestoreAllForces explicitly from its reset handler.

## Derive from a movement family

The example keeps the base wheel mechanics by calling `base.Step` before adding a separate force. `ForceMode.Acceleration` expresses the additional downward acceleration independently of mass. The speed threshold is a design rule for this example; it does not replace tire grip, aerodynamic drag or the engine's torque limit.

`CreateSettings` returns defaults for a newly chosen profile. Editing an already configured vehicle's settings remains a separate operation. Returning a fresh object prevents settings changes in one vehicle from unintentionally changing another vehicle's configuration.

This serializable mode retains wheel behavior and adds speed-dependent downforce. Return a fresh `Settings` object from `CreateSettings`. Add the script to a runtime assembly; it can then appear in the managed-reference selector.

**Example: `UtilityWheeledProfile.cs`**

<!-- example: UtilityWheeledProfile.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    [System.Serializable]
    public class UtilityWheeledProfile : WheeledProfile
    {
        [Min(0)] public float downforceAcceleration = 1;

        public override Settings CreateSettings()
        {
            var settings = base.CreateSettings();
            settings.mass = 1800;
            return settings;
        }

        public override void Step(VehicleController vehicle, Command command, float dt)
        {
            base.Step(vehicle, command, dt);
            if (vehicle.SpeedKph > 30)
                vehicle.Body.AddForce(-vehicle.transform.up * downforceAcceleration,
                    ForceMode.Acceleration);
        }
    }
}
```

Family checks are type-based: a Wheeled subclass remains a wheeled mode, an Airplane subclass retains aircraft integration, and a Submarine subclass retains its water behavior. Override the contract deliberately when creating another family.

## Create an independent profile from scratch

A new movement family can inherit directly from `DriveProfile`. It does not need to inherit from `WheeledProfile`, `FreeProfile` or any other built-in implementation. The Inspector discovers concrete descendants through `TypeCache.GetTypesDerivedFrom<DriveProfile>()`; there is no registration list to edit in the package.

### Make the class available in the selector

1. Save the example below as `Assets/VehicleProfiles/ThrusterProfile.cs`, outside any `Editor` folder. If you use an assembly definition, reference `UltraVehicleSystem.Runtime` and include the assembly on your target platforms.
2. Use a public, non-abstract, non-generic class marked `[System.Serializable]`. Keep a public parameterless constructor; the example gets one implicitly. Constructors and field initializers should only initialize managed configuration, since selection calls `DriveDefaults.Create` and Unity also reconstructs serialized objects. `[Preserve]` retains the custom type in builds that strip unused code.
3. Let Unity compile and reload scripts. Select the vehicle root and open **VehicleController → Setup → Drive mode**. The example appears as **Thruster**, because the selector removes `Profile` from class names and formats the result. It also appears in other fields using the same profile drawer, including `ProfileSwitcher` registered profile slots.
4. Select **Thruster** and expand it to edit its serialized fields. Choosing a profile in the root Drive mode field creates a new instance and initializes shared vehicle settings through `CreateSettings()`. Choosing a profile in a registered slot stores that slot's configuration; it does not replace current vehicle settings immediately. Give each slot a unique ID.

The **Tools → UltraVehicleSystem → Add Vehicle** commands remain built-in setup presets. Automatic discovery extends the Drive mode selector; it does not generate a new preset command or install supporting components. Use a distinct class name so the displayed name can be distinguished from other profiles.

### Implement the movement contract

Only `Step` is abstract. Override `RequiresWheels` when the profile can work without wheel definitions: the default is `true`. Override `CreateSettings` to supply this family's initial shared settings; its default for an unknown family is a fresh ordinary `Settings` object. `Medium` is descriptive metadata and does not opt the class into built-in aircraft or water mechanics.

This example owns simple forward/reverse thrust, yaw, linear resistance and braking. It uses the existing sampled command and vehicle rigidbody, without depending on a built-in movement family, engine, gearbox or wheel modules. Its speed setting is stored in m/s and can be edited using the [speed unit selector](../SpeedUnits.md). The speed limiter fades thrust in the direction of travel; it does not clamp collision impulses or externally imposed velocity.

<!-- example: ThrusterProfile.cs -->
```csharp
using UnityEngine;
using UnityEngine.Scripting;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    [System.Serializable, Preserve]
    public sealed class ThrusterProfile : DriveProfile
    {
        [Min(0)] public float acceleration = 8;
        [Speed(SpeedUnit.MetresPerSecond, .1f)] public float maximumSpeed = 20;
        [Min(0)] public float linearResistance = .15f;
        [Min(0)] public float brakeResistance = 3;
        [Min(0)] public float yawAcceleration = 1;
        [Min(0)] public float yawDamping = .8f;

        public override string Medium => "Custom";
        public override bool RequiresWheels => false;

        public override Settings CreateSettings() => new Settings {
            mass = 1000,
            topSpeedKph = SpeedUnits.Convert(maximumSpeed,
                SpeedUnit.MetresPerSecond, SpeedUnit.Kph),
            centerOfMass = Vector3.zero
        };

        public override float ResolveDriveDemand(VehicleController vehicle, Command command)
            => Mathf.Clamp(command.Throttle, -1, 1);

        public override void Step(VehicleController vehicle, Command command, float deltaTime)
        {
            var body = vehicle.Body;
            if (!body || body.isKinematic) return;

            float throttle = Mathf.Clamp(command.Throttle, -1, 1);
            float speedAlongDemand = vehicle.ForwardSpeed * Mathf.Sign(throttle);
            float limit = Mathf.Max(.1f, maximumSpeed);
            float fade = Mathf.Clamp01((limit - speedAlongDemand) / Mathf.Max(.1f, limit * .1f));
            body.AddForce(vehicle.transform.forward * vehicle.DriveDirectionSign * throttle * Mathf.Max(0, acceleration) * fade,
                ForceMode.Acceleration);

            float resistance = Mathf.Max(0, linearResistance)
                + Mathf.Clamp01(command.ServiceBrake) * Mathf.Max(0, brakeResistance);
            body.AddForce(-body.linearVelocity * resistance, ForceMode.Acceleration);
            body.AddTorque(vehicle.transform.up * Mathf.Clamp(command.Steering, -1, 1)
                * Mathf.Max(0, yawAcceleration) - body.angularVelocity * Mathf.Max(0, yawDamping),
                ForceMode.Acceleration);
        }
    }
}
```

`Step` already runs once per fixed physics tick. Unity integrates these `ForceMode.Acceleration` calls, so they are not multiplied by `deltaTime` again. Use the supplied timestep when integrating your own timers, filters or other state. The example has no transient state. If your implementation caches references in `Configure`, tolerate repeated configuration and keep temporary history nonserialized and isolated per vehicle. Return a new `Settings` object on every `CreateSettings` call.

### Put the profile on a vehicle

For a minimal setup, create a new GameObject with a collider, a dynamic Rigidbody and `VehicleController`. Select **Thruster**, leave Wheel Setup empty, and add an enabled `Drive` component on the root. Use **Connect available modules** from the controller's context menu to discover and register its modules, then **Apply vehicle configuration**. Setting `driveProfile` alone is insufficient: the registered `Drive` module invokes its `Configure` and `Step` hooks.

Disable **Use Gravity** on this Rigidbody so it can demonstrate free motion without a support surface. Assign a keyboard input source or `ExternalController` to the controller's **Input Source**. For external input, feed `SetAnalogAxes(throttle, steering, brake)` from your application. In Play Mode, positive/negative throttle applies forward/reverse thrust, steering turns the body and brake adds resistance. Restoring gravity makes the body fall; this example does not implement hover support, buoyancy or attitude stabilization.

Use a clean object for the initial setup. Existing engine, stability, suspension or custom modules may independently apply forces or enforce family-specific rules. Review each module's `SupportsProfile` contract when combining it with a new movement family. A direct `DriveProfile` subclass does not satisfy `is AirplaneProfile` or `is BoatProfile` checks merely by returning the same `Medium`. Supply any custom support, fuel/ignition or actuator behavior explicitly; the example's propulsion does not consume fuel or check engine ignition. The handbrake has no special behavior in this example.

### Select the custom type from code

Create it with `new ThrusterProfile()` or `DriveDefaults.Create(typeof(ThrusterProfile))`. For an initial authored setup, assign a fresh instance to `vehicle.driveProfile`, assign `vehicle.settings = DriveDefaults.CreateSettings(vehicle.driveProfile)`, then apply configuration after its required input, geometry and modules are installed.

For an existing running vehicle, use `TrySetDriveProfile(profile, out error)` and inspect the result. This preserves current shared settings and does not call `CreateSettings`; explicitly manage any settings changes your application requires. Profile-owned fields such as the example's `maximumSpeed` remain independent from shared settings after initial selection. For coordinated transitions, register the custom instance in a `ProfileSwitcher` with an ID and configure the desired source/destination route.

## Immediate change versus animated transition

Choose an immediate change when the vehicle already has compatible geometry and no presentation needs to travel between poses. Choose a transition when contacts or visible geometry must be coordinated over time, such as changing between wheel support and hover.

An accepted request starts that process; it is not permission for another system to toggle wheel colliders halfway through it. Keep contact ownership with the transition until it completes. UI should reflect the active/transitioning state rather than assuming that a button press always succeeds.

`TrySetDriveProfile(profile, out error)` validates the target with the current vehicle settings and wheel definitions. It rejects `null` targets, invalid wheel requirements and changes during an active `ProfileSwitcher` transition. It does not run the complete editor preset or call the initial-settings factory. A built-in profile `Configure` may ensure its family-specific helpers; author required engine/input, geometry and assets explicitly.

`ProfileSwitcher` stores an ordered list of `DriveProfileSlot` registrations. Each has a unique, case-sensitive ID and a separate serialized strategy. There is no fixed slot count. The serialized `ActiveProfileId` identifies which registration represents the controller's current strategy, even when several registrations use the same profile class.

`Toggle()` requests the next entry (use `SwitchToNext()` to read whether it was accepted), wrapping to the start; it does not skip entries whose switch request is rejected. `SwitchTo(id)` requests a specific registration, while `SwitchTo(profile)` accepts only an already registered instance. `RegisterProfile`, `UnregisterProfile`, `SetProfiles` and `ClearProfiles` manage membership. Registration changes are rejected during a switch or animated transition. List replacement validates every entry before changing anything, rejecting blank/duplicate IDs, null profiles and reuse of the same strategy instance under several IDs.

Removing an active registration or clearing the list leaves the controller's current strategy running and clears its active ID. The next Toggle selects the first remaining registration. Replacing a list retains the active ID when the exact running instance remains registered, even if its position changes. It does not automatically choose a different strategy. In the Inspector, set Active Profile Id to the slot represented by the controller's authored Drive mode. Configuration reconnects that slot to the controller's instance; do not identify active slots by class type.

Each component in `transitions` declares `fromProfileId`, `toProfileId` and optional `bidirectional` matching. Duration, volume and forward/reverse clips belong to that route. No matching enabled route means an immediate profile change; more than one matching route rejects the request. Disabled route components are ignored. Route IDs must use the registrations from the same vehicle. For Car/Porsche, a bidirectional HoverDriveTransition maps drive ↔ hover, preserving wheel folding, deployment and landing assistance.

Before applying a target, the selected route receives `CanBegin(vehicle, from, to)`. On acceptance, the controller applies the target configuration, the switcher suspends wheel contact, and `Begin(vehicle, from, to)` initializes the route. Step/Progress advance it; completion restores target contacts and finalizes presentation. Progress is tied to the route's duration captured at the start. `ProfileChanged` reports target configuration, whereas `TransitionCompleted` reports finished animation. Immediate changes emit ProfileChanged without transition callbacks. Disabling an animated switch finalizes its target and emits TransitionInterrupted.

Use `InputGate.Route.profileId` to associate any number of registrations with input providers. A two-position `ProfileSwitchBinding` maps explicit `onProfileId` and `offProfileId` values; it can select any two registrations without assuming either is a HoverProfile.

Assign a `ProfileTransition` component for geometry/contact rules. Configure recordings separately under **Profile Transition Audio > Sounds**, assigning the transition and forward/reverse clips. Add a multi-mode switch with `ProfileSwitcher`; use the example below for registration and UI button bindings. Configure supporting modules and transition components separately.

**Example: `DriveModeButtons.cs`**

<!-- example: DriveModeButtons.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class DriveModeButtons : MonoBehaviour
    {
        public ProfileSwitcher switcher;
        public VehicleController vehicle;

        public bool RegisterModes()
        {
            if (!vehicle || !switcher) return false;
            return switcher.SetProfiles(new[] {
                new DriveProfileSlot("Drive", vehicle.driveProfile),
                new DriveProfileSlot("Hover", new HoverProfile()),
                new DriveProfileSlot("boat", new BoatProfile()),
                new DriveProfileSlot("helicopter", new HelicopterProfile()),
                new DriveProfileSlot("submarine", new SubmarineProfile())
            });
        }

        public bool SelectDrive() => switcher && switcher.SwitchTo("Drive");
        public bool SelectHover() => switcher && switcher.SwitchTo("Hover");
        public bool SelectBoat() => switcher && switcher.SwitchTo("boat");
        public bool Next() => switcher && switcher.SwitchToNext();
        public bool RemoveBoat() => switcher && switcher.UnregisterProfile("boat");
    }
}
```

Call RegisterModes once during setup on a vehicle whose current profile is its road configuration. Registering a list does not configure the owner: add/register the ProfileSwitcher and Drive modules, then apply the vehicle configuration. To append another independent mode later, call RegisterProfile with a unique ID and a new profile instance. To remove all registrations, use ClearProfiles.

Support modules and geometry stay independently authored. A strategy change alone does not create a water provider, gear wheels or control pivots.

## Toggle flight and water mechanics

The public boolean fields on the built-in profiles gate individual force/assistance channels without modifying their numeric tuning. These switches are read each Step and do not require ApplyConfiguration. Wheel ownership and other configuration-time settings retain their normal configuration contract. Change the active profile instance; when switching profiles later, the newly selected profile has its own switch values.

<!-- example: VehicleMechanicsSwitches.cs -->
```csharp
using UltraVehicleSystem;
using UnityEngine;

public sealed class VehicleMechanicsSwitches : MonoBehaviour
{
    public VehicleController vehicle;

    public void SetFlightAssistance(bool enabled)
    {
        if (vehicle && vehicle.driveProfile is AirplaneProfile aircraft) {
            aircraft.flightAlignmentEnabled = enabled;
            aircraft.coordinatedTurnEnabled = enabled;
            aircraft.bankCompensationEnabled = enabled;
        }
    }

    public void SetBoatWaves(bool enabled)
    {
        if (vehicle && vehicle.driveProfile is BoatProfile boat) {
            boat.ambientWavesEnabled = enabled;
            boat.waveImpulsesEnabled = enabled;
        }
    }
}
```

Switches gate profile contributions rather than freezing the Rigidbody or disabling gravity. Parent channels and the existing powered/immersion conditions still apply. Individual switches and their dependencies are listed in the Inspector reference for [fixed-wing flight](../InspectorReference/Drive.md#airplaneprofile), [helicopter](../InspectorReference/Drive.md#helicopterprofile), [hover](../InspectorReference/Drive.md#hoverprofile) and [boat](../InspectorReference/Drive.md#boatprofile).

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed movement strategies and transitions API](../API/DriveProfiles.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### Drive

[Drive](../API/DriveProfiles.md#drive) gives the full declared contract.

- `public override void Configure(VehicleController vehicle)` — Binds the component to its configured owner and selected source.
- `public virtual void ResetVehicleState(VehicleResetReason reason)` — Clears transient state for the supplied reset reason without changing persistent configuration.
- `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Current step.

### DriveDefaults

[DriveDefaults](../API/DriveProfiles.md#drivedefaults) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public static DriveProfile Create(System.Type type)` | Creates a concrete built-in or custom DriveProfile type through its public parameterless constructor. |
| `public static Settings CreateSettings(DriveProfile profile)` | Returns a fresh initial shared settings object for explicit creation/profile selection. |

### DriveProfile

[DriveProfile](../API/DriveProfiles.md#driveprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void ReleaseAllForces(VehicleController vehicle)` | Release the supplied vehicle through its controller API. vehicle: target owner; runtime state stays on that vehicle, not the serialized profile. |
| `public virtual void RestoreAllForces(VehicleController vehicle)` | Clear the target vehicle manual release through its controller API. Overrides the current ignition-off interval; the next running/off cycle can release again. Preserves pose and velocity. |
| `public virtual bool AreForcesReleased(VehicleController vehicle)` | Query the target vehicle effective force-release state. Returns false for a missing vehicle; includes both manual and ignition-policy release. |
| `public abstract void Step(VehicleController vehicle, Command command, float deltaTime)` | Abstract movement-strategy step called by Drive; apply the selected family's movement using this vehicle context. |
| `public virtual bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. |
| `public virtual DriveProfile Clone()` | Creates an independent serialized profile-configuration copy; configure it on its destination vehicle before use. |
| `public virtual float ResolveBoostDemand(VehicleController vehicle, Command command)` | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. |
| `public virtual float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. |
| `public virtual float ResolveExternalDriveIntent(VehicleController vehicle)` | Returns signed non-wheel propulsion intent used by shared coasting/contact policy. |
| `public virtual float ResolvePropulsionBoostMultiplier(VehicleController vehicle)` | Returns the resolved native-thrust multiplier; custom profiles consume it in their own force law. |
| `public virtual Settings CreateSettings()` | Returns a fresh initial shared settings object for explicit creation/profile selection. |
| `public virtual void Configure(VehicleController vehicle)` | Empty base strategy setup hook; family implementations may ensure helpers and apply profile-owned settings. |

### FreeProfile

[FreeProfile](../API/DriveProfiles.md#freeprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. |

### HoverDriveTransition

[HoverDriveTransition](../API/DriveProfiles.md#hoverdrivetransition) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Begin(VehicleController vehicle, DriveProfile previous, DriveProfile target)` | Starts the owning operation or adapter; its parameters identify the request, seat or transition being owned. |
| `public override void Step(VehicleController vehicle, float progress, float remainingTime, float deltaTime)` | Applies configured landing-clearance support while returning from hover to wheel drive. |
| `public override void Complete(VehicleController vehicle)` | Completes hover/wheel transition geometry and its inherited transition cleanup. |
| `public override void Progress(VehicleController vehicle, float progress)` | Returns normalized progress for the active profile transition. |

### HoverProfile

[HoverProfile](../API/DriveProfiles.md#hoverprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. |
| `public override float ResolveBoostDemand(VehicleController vehicle, Command command)` | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. |
| `public override void Configure(VehicleController vehicle)` | Ensures a `HoverVisuals` helper exists for the hover family. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Applies powered vertical support, horizontal drive, attitude response and resistance. |

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### MotorcycleProfile

[MotorcycleProfile](../API/DriveProfiles.md#motorcycleprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Provides fallback family balance only when enabled and no dedicated `MotorcycleBalance` owns that responsibility. |

### ProfileSwitcher

[ProfileSwitcher](../API/DriveProfiles.md#profileswitcher) gives the full declared contract.

- `public UnityEvent completed` — Invoked when the transition finishes and the destination profile is active.
- `public event Action<DriveProfile> ProfileChanged` — Current profile changed.
- `public event Action ProfilesChanged` — Current profiles changed.
- `public UnityEvent<float> progressed` — Invoked as transition progress changes; use it to update an animation or progress display.
- `public UnityEvent started` — Invoked when an admitted profile transition starts.
- `public event Action TransitionAudioStopped` — Requests stopping transition presentation.
- `public event Action<ProfileTransition, string, string> TransitionBegan` — Reports the admitted transition component, source profile ID and destination profile ID.
- `public event Action TransitionCompleted` — Current transition completed.
- `public event Action TransitionInterrupted` — Current transition interrupted.
- `public event Action<float> TransitionProgressed` — Current transition progressed.
- `public event Action TransitionStarted` — Current transition started.
- `public virtual bool ClearProfiles()` — Current clear profiles.
- `public override void Configure(VehicleController vehicle)` — Binds the component to its configured owner and selected source.
- `public virtual DriveProfile GetProfile(string id)` — Current get profile.
- `public virtual bool RegisterProfile(string id, DriveProfile profile)` — Current register profile.
- `public virtual bool SetProfiles(IEnumerable<DriveProfileSlot> slots)` — Current set profiles.
- `public override void Step(VehicleController vehicle, Command command, float deltaTime)` — Current step.
- `public virtual bool SwitchTo(DriveProfile target)` — Current switch to.
- `public virtual bool SwitchTo(string id)` — Current switch to.
- `public virtual bool SwitchToNext()` — Current switch to next.
- `public virtual void Toggle()` — Current toggle.
- `public virtual bool UnregisterProfile(string id)` — Current unregister profile.

### ProfileTransition

[ProfileTransition](../API/DriveProfiles.md#profiletransition) gives the full declared contract.

- `public virtual void Begin(VehicleController vehicle, DriveProfile from, DriveProfile to)` — Current begin.
- `public virtual bool CanBegin(VehicleController vehicle, DriveProfile from, DriveProfile to)` — Current can begin.
- `public virtual void Complete(VehicleController vehicle)` — Current complete.
- `public virtual bool Matches(string fromId, string toId)` — Current matches.
- `public virtual void Progress(VehicleController vehicle, float progress)` — Current progress.
- `public virtual void Step(VehicleController vehicle, float progress, float remainingTime, float deltaTime)` — // Physics-only transition assistance; never called by render-frame presentation updates.

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

### WheeledProfile

[WheeledProfile](../API/DriveProfiles.md#wheeledprofile) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty family step: ordinary wheel propulsion, steering, braking and support are already owned by the surrounding modules. |
