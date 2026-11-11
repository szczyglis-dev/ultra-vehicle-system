# Movement strategies and transitions API

Read [the system explanation](../Scripting/DriveProfiles.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [AirProfile](DriveProfiles.md#airprofile)
- [Drive](DriveProfiles.md#drive)
- [DriveCore](DriveProfiles.md#drivecore)
- [DriveDefaults](DriveProfiles.md#drivedefaults)
- [DriveModule](DriveProfiles.md#drivemodule)
- [DriveProfile](DriveProfiles.md#driveprofile)
- [DriveProfileSlot](DriveProfiles.md#driveprofileslot)
- [FreeProfile](DriveProfiles.md#freeprofile)
- [HoverDriveTransition](DriveProfiles.md#hoverdrivetransition)
- [HoverProfile](DriveProfiles.md#hoverprofile)
- [MotorcycleProfile](DriveProfiles.md#motorcycleprofile)
- [ProfileSwitcher](DriveProfiles.md#profileswitcher)
- [ProfileTransition](DriveProfiles.md#profiletransition)
- [SpaceshipProfile](DriveProfiles.md#spaceshipprofile)
- [WheeledProfile](DriveProfiles.md#wheeledprofile)

## AirProfile

**Runtime/Drive/Profiles/AirProfile.cs**

Configuration/implementation type for air profile within movement strategies and transitions.

**Inherits / implements:** [FreeProfile](DriveProfiles.md#freeprofile).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override string Medium { get; }` | Movement-family label used by the profile contract. |

## Drive

**Runtime/Drive/Drive.cs**

Retains the vehicle's boat motion and sampling history.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule), [IVehicleResetHandler](Modules.md#ivehicleresethandler).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public override bool SupportsReleasedForces { get; }` | Keeps passive maintenance/observation active during release; Drive and Engine suppress force output, and TireCollision keeps native solid proxies without supplemental tread forces. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Rebinds teleport reset, clears hold/boat/hover history and configures the current profile. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Clears inapplicable hold state, then invokes the active `DriveProfile.Step` for this vehicle. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## DriveCore

**Runtime/Drive/Core/DriveCore.cs**

Configuration/implementation type for drive core within movement strategies and transitions.

**Inherits / implements:** [CategoryCore](Modules.md#categorycore).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public DriveCore()` | Constructs `DriveCore` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## DriveDefaults

**Runtime/Drive/DriveDefaults.cs**

Builds initial settings for supported movement families.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public static DriveProfile Create(System.Type type)` | Creates a concrete built-in or custom DriveProfile type through its public parameterless constructor. | `type` — Type, interpreted by this operation in the declared type. **Returns:** Returned `DriveProfile`; ownership remains as specified by the creating/lookup operation. |
| `public static Settings CreateSettings(DriveProfile profile)` | Returns a fresh initial shared settings object for explicit creation/profile selection. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** Returned Settings; ownership remains as specified by the creating/lookup operation. |

## DriveModule

**Runtime/Drive/Core/DriveModule.cs**

Configuration/implementation type for drive module within movement strategies and transitions.

**Inherits / implements:** [VehicleModule](Modules.md#vehiclemodule), [IDriveModule](Modules.md#idrivemodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |

## DriveProfile

**Runtime/Drive/DriveProfile.cs**

Defines settings creation, configuration, stepping and drive-demand resolution.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual string Medium { get; }` | Movement-family label used by the profile contract. |
| `public bool releaseAllForcesOnIgnitionOff` | Default false. Release profile forces/shared assistance while an installed engine is not running; ignition on clears only the automatic reason. |
| `public virtual bool RequiresWheels { get; }` | Whether this profile requires valid wheel definitions during configuration. |
| `public bool steeringSpeedLimitEnabled` | Shared master switch for Steering speed-sensitive and lateral-acceleration steering limits. Default: enabled; Airplane/Aerobatic/Jet presets default to disabled. Existing per-module options retain their behavior when this master is on. Minimum radius and Ackermann geometry remain independent. |
| `public bool speedSensitiveRotation` | Enable per-axis km/h-based response curves; default false in all built-in profiles. |
| `public AnimationCurve pitchRateBySpeed` | X: actual speed in km/h. Y: axis response multiplier; initial linear (0, 1) to (300, 0.65). Yaw also scales steering. |
| `public AnimationCurve yawRateBySpeed` | X: actual speed in km/h. Y: axis response multiplier; initial linear (0, 1) to (300, 0.65). Yaw also scales steering. |
| `public AnimationCurve rollRateBySpeed` | X: actual speed in km/h. Y: axis response multiplier; initial linear (0, 1) to (300, 0.65). Yaw also scales steering. |
| `public float rotationReleaseDuration` | Soft released-control settling time in seconds; default 0 preserves existing handling. Spaceship overrides the new-profile default to 1.1 s. |
| `public Vector3 ResolveRotationMultipliers(float speedKph)` | Returns pitch/yaw/roll curve multipliers, or ones when disabled. |
| `public virtual bool UsesWheelPropulsion { get; }` | True for wheel/track drive; false for native thrust profiles, including aircraft with support wheels. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool AreForcesReleased(VehicleController vehicle)` | Query the target vehicle effective force-release state. | Returns false for a missing vehicle; includes both manual and ignition-policy release. |
| `public virtual bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public virtual DriveProfile Clone()` | Creates an independent serialized profile-configuration copy; configure it on its destination vehicle before use. | **Returns:** Returned `DriveProfile`; ownership remains as specified by the creating/lookup operation. |
| `public virtual void Configure(VehicleController vehicle)` | Empty base strategy setup hook; family implementations may ensure helpers and apply profile-owned settings. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual Settings CreateSettings()` | Returns a fresh initial shared settings object for explicit creation/profile selection. | **Returns:** Returned Settings; ownership remains as specified by the creating/lookup operation. |
| `public virtual void ReleaseAllForces(VehicleController vehicle)` | Release the supplied vehicle through its controller API. | vehicle: target owner; runtime state stays on that vehicle, not the serialized profile. |
| `public virtual float ResolveBoostDemand(VehicleController vehicle, Command command)` | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public virtual float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual float ResolveExternalDriveIntent(VehicleController vehicle)` | Returns signed non-wheel propulsion intent used by shared coasting/contact policy. | `vehicle` — Vehicle context/owner receiving the operation. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual float ResolvePropulsionBoostMultiplier(VehicleController vehicle)` | Returns the resolved native-thrust multiplier; custom profiles consume it in their own force law. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public virtual void RestoreAllForces(VehicleController vehicle)` | Clear the target vehicle manual release through its controller API. | Overrides the current ignition-off interval; the next running/off cycle can release again. Preserves pose and velocity. |
| `public abstract void Step(VehicleController vehicle, Command command, float deltaTime)` | Abstract movement-strategy step called by Drive; apply the selected family's movement using this vehicle context. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## DriveProfileSlot

**Runtime/Drive/ProfileSwitcher.cs**

Serializable registration descriptor. Each slot stores an independent strategy configuration.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public string Id { get; }` | Stable, case-sensitive registration ID. Edit the serialized ID when authoring the list. |
| `public DriveProfile Profile { get; internal set; }` | Per-slot managed-reference configuration. The switcher rebinds the serialized active slot to the controller's current profile. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public DriveProfileSlot(string id, DriveProfile profile)` | Creates a descriptor for registering or replacing a list; does not switch the vehicle. | — |

## FreeProfile

**Runtime/Drive/Profiles/FreeProfile.cs**

Configuration/implementation type for free profile within movement strategies and transitions.

**Inherits / implements:** [DriveProfile](DriveProfiles.md#driveprofile).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float acceleration` | Propulsion acceleration applied while the corresponding input is requested. Initial value: `12`. |
| `public float angularDamping` | Strength of resistance opposing angular motion. Initial value: `3`. |
| `public float drag` | Strength of resistance opposing movement. Initial value: `.4f`. |
| `public override bool RequiresWheels { get; }` | Whether this profile requires valid wheel definitions during configuration. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override float ResolveDriveDemand(VehicleController vehicle, Command command)` | Maps the command and strategy state to propulsion demand for surrounding mechanics. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |

## HoverDriveTransition

**Runtime/Drive/Profiles/HoverDriveTransition.cs**

Configuration/implementation type for hover drive transition within movement strategies and transitions.

**Inherits / implements:** [ProfileTransition](DriveProfiles.md#profiletransition).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float landingClearance` | Extra clearance above fully extended tires while unfolding near the ground. Zero disables landing assistance. |
| `public float landingLiftAcceleration` | Maximum upward correction acceleration during low hover-to-drive deployment, in m/s². |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Begin(VehicleController vehicle, DriveProfile previous, DriveProfile target)` | Starts the owning operation or adapter; its parameters identify the request, seat or transition being owned. | `vehicle` — Vehicle context/owner receiving the operation. `previous` — Prior buffer segment/state. `target` — Configured target object/point; see declared type and owner. |
| `public override void Complete(VehicleController vehicle)` | Completes hover/wheel transition geometry and its inherited transition cleanup. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public override void Progress(VehicleController vehicle, float progress)` | Returns normalized progress for the active profile transition. | `vehicle` — Vehicle context/owner receiving the operation. `progress` — Normalized transition progress in 0–1. |
| `public override void Step(VehicleController vehicle, float progress, float remainingTime, float deltaTime)` | Applies configured landing-clearance support while returning from hover to wheel drive. | `vehicle` — Vehicle context/owner receiving the operation. `progress` — Normalized transition progress in 0–1. `remainingTime` — Estimated transition time remaining in seconds. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## HoverProfile

**Runtime/Drive/Profiles/HoverProfile.cs**

Configuration/implementation type for hover profile within movement strategies and transitions.

**Inherits / implements:** [AirProfile](DriveProfiles.md#airprofile).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float attitudeStrength` | Attitude strength. Initial value: `12`. |
| `public bool automaticLeveling` | Automatic leveling. Initial value: `true`. |
| `public float bodyTiltDegrees` | Maximum combined hull lean toward forward/sideways thrust and steering, in degrees. |
| `public bool bodyTiltEnabled` | Lean the leveling target with movement/steering demand. Disable for a level target; Automatic Leveling still owns restoring torque. Default: enabled. |
| `public float bodyTiltResponse` | Hull lean response per second, including return to level. |
| `public bool compensateGravity` | Compensate gravity. Initial value: `true`. |
| `public float damping` | Damping. Initial value: `6f`. |
| `public LayerMask groundMask` | Ground mask. Initial value: `-1`. |
| `public float height` | Height. Initial value: `2.5f`. |
| `public bool horizontalDriveEnabled` | Allow forward and sideways thrust from commands. Default: enabled. |
| `public bool linearDragEnabled` | Apply inherited velocity-proportional resistance. Default: enabled. |
| `public float maximumAscentAcceleration` | Maximum ascent acceleration. Initial value: `25`. |
| `public float maximumDescentAcceleration` | Maximum descent acceleration. Initial value: `15`. |
| `public float spring` | Spring. Initial value: `12f`. |
| `public bool surfaceSupport` | Surface support. Initial value: `true`. |
| `public float verticalDamping` | Vertical damping. Initial value: `2f`. |
| `public bool verticalSupportEnabled` | Allow collective, clearance spring, vertical damping and gravity compensation channel. Default: enabled. |
| `public float wheelSteeringTilt` | Wheel steering tilt. Initial value: `12f`. |
| `public float wheelThrustTilt` | Wheel thrust tilt. Initial value: `10f`. |
| `public float wheelTiltResponse` | Visual wheel tilt response per second. Lower values make acceleration, braking and steering tilt settle more slowly. |
| `public float yawAcceleration` | Yaw acceleration. Initial value: `4`. |
| `public bool yawControlEnabled` | Allow commanded steering/yaw torque, independently of yaw damping. Default: enabled. |
| `public float yawDamping` | Yaw damping. Initial value: `2`. |
| `public bool yawDampingEnabled` | Allow passive damping around the vertical yaw axis. Default: enabled. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public override void Configure(VehicleController vehicle)` | Ensures a `HoverVisuals` helper exists for the hover family. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public HoverProfile()` | Constructs `HoverProfile` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
| `public override float ResolveBoostDemand(VehicleController vehicle, Command command)` | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Applies powered vertical support, horizontal drive, attitude response and resistance. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## MotorcycleProfile

**Runtime/Drive/Profiles/MotorcycleProfile.cs**

Configuration/implementation type for motorcycle profile within movement strategies and transitions.

**Inherits / implements:** [DriveProfile](DriveProfiles.md#driveprofile).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool automaticBalance` | Enable fallback balance when no Motorcycle Balance module is installed. |
| `public float balanceDamping` | Damping applied to roll while maintaining motorcycle balance. Initial value: `14f`. |
| `public float balanceStrength` | Strength of the restoring torque toward the requested motorcycle lean. Initial value: `80f`. |
| `public float maximumAngularAcceleration` | Upper bound on the profile's applied angular acceleration. Initial value: `100f`. |
| `public float maximumLean` | Largest requested motorcycle lean angle in degrees. Initial value: `28f`. |
| `public float wheelbase` | Motorcycle axle span used to convert steering to lean, in metres. Initial value: `1.45f`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Provides fallback family balance only when enabled and no dedicated `MotorcycleBalance` owns that responsibility. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## ProfileSwitcher

**Runtime/Drive/ProfileSwitcher.cs**

Owns an ordered list of registered drive strategies and selects optional pair-specific transitions. Inherits ControllerModule.

**Inherits / implements:** [ControllerModule](Input.md#controllermodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public UnityEvent completed` | Inspector callback after animated route completion. |
| `public event Action<DriveProfile> ProfileChanged` | After an accepted change has configured the target. Payload: target strategy. For animated routes, this precedes transition completion. |
| `public event Action ProfilesChanged` | After successful registration, removal or list replacement. Does not imply a strategy change. |
| `public UnityEvent<float> progressed` | Inspector callback with normalized animation progress. |
| `public UnityEvent started` | Inspector callback when an animated route starts. |
| `public event Action TransitionAudioStopped` | Requests stopping transition presentation. |
| `public event Action<ProfileTransition, string, string> TransitionBegan` | Reports the admitted transition component, source profile ID and destination profile ID. |
| `public event Action TransitionCompleted` | After animation, target contacts and final presentation are restored. |
| `public event Action TransitionInterrupted` | On disable during a transition, after finalizing the selected target and presentation. |
| `public event Action<float> TransitionProgressed` | During animation, with normalized progress. |
| `public event Action TransitionStarted` | After target configuration and matching route initialization. Not emitted for immediate changes. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public string ActiveProfileId { get; }` | Registered ID represented by VehicleController.driveProfile, or an empty string if unregistered. Serialized for correct reload even with several profiles of the same class. |
| `public virtual ProfileTransition ActiveTransition { get; protected set; }` | Selected route during animation; null when idle. |
| `public virtual bool IsTransitioning { get; protected set; }` | Whether a coordinated change is in progress. |
| `public IReadOnlyList<DriveProfileSlot> Profiles { get; }` | Registrations in Toggle order. Use registration methods to mutate the list at runtime. |
| `public virtual float Progress { get; }` | Animation progress in 0–1; 1 when idle. Duration is captured from the route when the change starts. |
| `public ProfileTransition[] transitions` | Enabled route components to consider. Exactly one matching route is allowed per pair; no matching route means immediate switching. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool ClearProfiles()` | Clears all registrations without replacing the current vehicle strategy. Rejected during switching/transition. | — |
| `public override void Configure(VehicleController vehicle)` | Binds the owner and reconnects its current profile to the saved active ID. Does not recreate removed registrations. | — |
| `public virtual DriveProfile GetProfile(string id)` | Finds a registered profile by case-sensitive ID, or returns null. | — |
| `public virtual bool RegisterProfile(string id, DriveProfile profile)` | Appends a non-null profile with a unique nonblank ID and unique instance. Rejects changes during switching or transition. | — |
| `public virtual bool SetProfiles(IEnumerable<DriveProfileSlot> slots)` | Atomically replaces/reorders the list after validation. Duplicate IDs, shared instances, null entries and blank IDs reject the entire replacement. Preserves the active ID only when its current instance is included. | — |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Consumes ToggleProfile, advances the selected route and restores target contacts at completion. | — |
| `public virtual bool SwitchTo(DriveProfile target)` | Selects an already registered instance; does not implicitly register it. | — |
| `public virtual bool SwitchTo(string id)` | Requests a registered profile by ID. Rejects disabled/unconfigured switchers, overlapping changes, invalid wheel requirements and ambiguous/rejected routes. A pair without a matching enabled route changes immediately. | — |
| `public virtual bool SwitchToNext()` | Requests the next list entry and wraps at the end. With no registered active ID, requests the first entry. Empty lists and requests for the same current instance return false. | — |
| `public virtual void Toggle()` | Requests the next profile in list order. Suitable for UnityEvent bindings. | — |
| `public virtual bool UnregisterProfile(string id)` | Removes a slot. Removing the active registration leaves the vehicle strategy running and clears ActiveProfileId; no automatic switch occurs. | — |

## ProfileTransition

**Runtime/Drive/ProfileTransition.cs**

A route component for one source/destination ID pair, optionally bidirectional. Inherits MonoBehaviour.

**Inherits / implements:** `MonoBehaviour`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool bidirectional` | Also match toProfileId → fromProfileId; default false. |
| `public float duration` | Animation duration in seconds; minimum .01 when starting. |
| `public string fromProfileId` | Source registration ID in the owning switcher. |
| `public float takeoffVelocity` | Upward velocity change in m/s when leaving a wheel-required strategy; zero disables it. |
| `public string toProfileId` | Destination registration ID in the owning switcher. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Begin(VehicleController vehicle, DriveProfile from, DriveProfile to)` | Initializes presentation after the target is configured. Base implementation optionally supplies a takeoff impulse. | — |
| `public virtual bool CanBegin(VehicleController vehicle, DriveProfile from, DriveProfile to)` | Checks admission before any target configuration; receives the actual source and destination strategies. | — |
| `public virtual void Complete(VehicleController vehicle)` | Finalizes presentation after target contacts are restored; also called when disabling an active switcher. | — |
| `public virtual bool Matches(string fromId, string toId)` | Matches the configured pair of registration IDs and optional reverse direction. | — |
| `public virtual void Progress(VehicleController vehicle, float progress)` | Applies presentation for the supplied normalized progress; base implementation is empty. | — |
| `public virtual void Step(VehicleController vehicle, float progress, float remainingTime, float deltaTime)` | Physics-only assistance per fixed step, using progress and remaining time; base implementation is empty. | — |

## SpaceshipProfile

**Runtime/Drive/Profiles/SpaceshipProfile.cs**

**Inherits / implements:** `FreeProfile`.

| Member | Meaning |
| --- | --- |
| `public bool compensateGravity` | Cancel native gravity while this profile is active, including with ignition off. Explicit Release All Forces also releases this compensation. |
| `public float strafeAcceleration` | Sideways acceleration relative to the spacecraft, in m/s². |
| `public float liftAcceleration` | Up/down acceleration relative to the spacecraft, in m/s². |
| `public Vector3 angularRates` | Maximum local pitch, yaw and roll rates in degrees per second. |
| `public Vector3 ResolveAngularRates(float speedKph)` | Returns configured angular rates scaled by enabled speed curves, in degrees/s. |
| `public bool stopRotationOnRelease` | Smooth rotational braking after releasing input; enabled by default. |
| `public bool bankDriftEnabled` | Enable bank-dependent sideways bank drift, including coasting; no automatic yaw; optional downward component. |
| `public float maximumBankDriftAngle` | Maximum assisted flight-path offset in degrees; default 20. |
| `public float bankDriftResponse` | Blend response in inverse seconds; default 1.5. |
| `public float bankDriftExponent` | Bank response exponent; default 1.5 gives gentler drift at small banks. |
| `public float bankDriftSpeedMultiplier` | Drift-speed ratio multiplier; default 1. |
| `public bool bankDriftDownwards` | Include downward drift through inverted flight; default false. |
| `public float bankDriftDownwardMultiplier` | Independent downward-component multiplier; default 1. |
| `public bool alignFlightPath` | Redirect travel toward the nose with powered steering; enabled by default. |
| `public float flightPathTurnRate` | Maximum flight-path redirection rate in degrees/s, with smooth convergence toward the nose. |
| `public float maximumFlightPathAcceleration` | Maximum acceleration for travel redirection in m/s². |
| `public float angularResponse` | Rotational thruster response toward commanded angular rates. Uncommanded axes retain spin unless Stop Rotation On Release is enabled. |
| `public float maximumAngularAcceleration` | Maximum angular correction in rad/s². Does not restrict native collision impulses. |
| `public float brakeAcceleration` | Powered braking acceleration opposing current world velocity, in m/s². |
| `public override string Medium { get; }` | Returns Space. |
| `public override float ResolveDriveDemand(VehicleController vehicle, Command command)` | Engine demand from the combined translation axes. |
| `public override float ResolveBoostDemand(VehicleController vehicle, Command command)` | Boost demand from the combined translation axes. |
| `public SpaceshipProfile()` | Creates an independent profile with default resistance and six-axis handling. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances this mechanism through the vehicle physics pipeline. |

## WheeledProfile

**Runtime/Drive/Profiles/WheeledProfile.cs**

Reusable wheeled strategy used by the inheritance example.

**Inherits / implements:** [DriveProfile](DriveProfiles.md#driveprofile).

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty family step: ordinary wheel propulsion, steering, braking and support are already owned by the surrounding modules. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
