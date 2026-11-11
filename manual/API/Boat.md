# Boat movement API

Read [the system explanation](../Scripting/Boat.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [BoatProfile](Boat.md#boatprofile)

## BoatProfile

**Runtime/Drive/Profiles/BoatProfile.cs**

Owns authored boat movement parameters and the profile behavior.

**Inherits / implements:** [FreeProfile](DriveProfiles.md#freeprofile).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<bool> SinkingChanged` | Raised once when sinking is started or stopped. The argument is the new sinking state; repeated requests for the same state do not raise another event. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Vector2 accelerationTilt` | Pitch/roll degrees per m/s² of measured acceleration. |
| `public float ambientWaveDegrees` | Continuous rhythmic pitch/roll amplitude, degrees; active while idle and moving. Zero disables background sway. |
| `public Vector2 ambientWaveInterval` | Seconds between subtle random changes in wave amplitude and pitch phase; the side-to-side rhythm remains continuous. |
| `public float ambientWavePeriod` | Seconds for a complete side-to-side water rocking cycle. |
| `public bool ambientWavesEnabled` | Allow continuous background pitch/roll sway. Does not disable occasional wave impulses. Default: enabled. |
| `public bool brakingThrustEnabled` | Allow the Brake command to request opposing propeller thrust while powered. Default: enabled. |
| `public float buoyancyDepth` | Buoyancy depth. Initial value: `0.85f`. |
| `public bool buoyancyEnabled` | Apply gravity-derived upward buoyancy. Vertical damping remains a separate force contribution. Default: enabled. |
| `public float forwardDragScale` | Scales the inherited Drag setting along the hull; lower values retain momentum longer. |
| `public bool forwardResistanceEnabled` | Apply linear and speed-squared resistance along the hull. Default: enabled. |
| `public float idleWaveDegrees` | Occasional wave impulse strength. Zero disables these impulses independently of background sway. |
| `public Vector2 idleWaveInterval` | Random interval between occasional stronger wave impulses, seconds; also active while moving. |
| `public virtual bool IsSinking { get; }` | Whether explicit sinking currently suspends upward buoyancy and vertical water damping. |
| `public float lateralResistance` | Sideways resistance: lower values preserve sideways drift longer. |
| `public bool lateralResistanceEnabled` | Apply sideways hull resistance and its forward-speed contribution. Default: enabled. |
| `public float loadedRockingDampingRatio` | Loaded rocking damping ratio. Initial value: `0.85f`. |
| `public bool maneuverRockingEnabled` | Excite pitch/roll from measured hull acceleration; does not disable ambient waves or powered bow lift. Default: enabled. |
| `public float maximumHullTilt` | Total assisted hull tilt limit in degrees, default 35. |
| `public float maximumManeuverTilt` | Maximum maneuver tilt. Initial value: `6f`. |
| `public float maximumYawRate` | Upper requested yaw rate used by turning assistance, in rad/s. |
| `public override string Medium { get; }` | Movement-family label used by the profile contract. |
| `public bool pitchMotionEnabled` | Allow all profile-generated hull pitch torque, including wave impulses. Does not freeze native Rigidbody rotation. Default: enabled. |
| `public float poweredPitchDegrees` | Sustained bow/stern lift at full propeller load, degrees; builds gradually with squared throttle demand and forward motion. |
| `public bool poweredPitchEnabled` | Allow sustained throttle-induced bow/stern pitch. Disabling clears stored powered-pitch response. Default: enabled. |
| `public float poweredPitchReleaseTime` | Seconds for sustained lift to settle after releasing/reversing throttle. |
| `public float poweredPitchRiseTime` | Seconds for sustained throttle lift to approach its target; longer values make the bow rise more gradually. |
| `public float powerPitchBoost` | Power pitch boost. Initial value: `0.2f`. |
| `public bool propulsionEnabled` | Allow throttle-driven hull thrust. Braking thrust is independent; engine ownership is unchanged. Default: enabled. |
| `public float rockingDamping` | Rocking damping. Initial value: `0.65f`. |
| `public bool rockingDampingEnabled` | Apply passive pitch/roll damping, including propeller/low-speed pitch damping. Default: enabled. |
| `public float rockingMemorySeconds` | Rocking memory seconds. Initial value: `2.5f`. |
| `public float rockingSpring` | Rocking spring. Initial value: `3.5f`. |
| `public float rockingStrength` | Strength of maneuver, continuous water sway and wave rocking. Zero disables excitation while retaining upright stability and momentum. |
| `public bool rollMotionEnabled` | Allow all profile-generated hull roll torque, including wave impulses. Does not freeze native Rigidbody rotation. Default: enabled. |
| `public bool rudderEnabled` | Apply steering-generated yaw torque while powered, independently of forward thrust. Default: enabled. |
| `public float speedLateralResistance` | Extra sideways grip per m/s of forward speed; keeps the hull tracking its heading under power. |
| `public float speedResistance` | Speed resistance. Initial value: `0.006f`. |
| `public float stationaryTurnAcceleration` | Stationary turn acceleration. Initial value: `0.12f`. |
| `public bool stationaryTurningEnabled` | Allow the additional stationary turning authority; underway rudder authority remains speed-dependent. Default: enabled. |
| `public float stationaryYawRate` | Maximum requested low-speed boat yaw rate, in rad/s. |
| `public float steeringReturnTime` | Steering return time. Initial value: `0.22f`. |
| `public float steeringRiseTime` | Steering rise time. Initial value: `0.35f`. |
| `public bool steeringSmoothingEnabled` | Smooth digital steering demand. Disable for immediate steering; analog input is already direct. Default: enabled. |
| `public float steeringYawResponse` | Rudder response to desired turn rate. Countersteering first arrests the current turn instead of building unchecked opposing torque. |
| `public bool tiltLimitEnabled` | Enables the immersed assisted hull tilt guard. |
| `public bool uprightStabilizationEnabled` | Apply the hull spring returning pitch/roll toward upright, independently of rocking excitation. Default: enabled. |
| `public float verticalDamping` | Vertical damping. Initial value: `1.8f`. |
| `public bool verticalDampingEnabled` | Apply the vertical water-relative damping term inside the nonnegative buoyancy force. Default: enabled. |
| `public Vector2 waterCenter` | Water center. Initial value: `new Vector2(-280f, 80f)`. |
| `public bool waterCurrentEnabled` | Use provider water velocity for drag and vertical damping. Surface height still controls immersion. Default: enabled. |
| `public float waterLevel` | Flat fallback water-surface height in world metres. |
| `public Vector2 waterSize` | Zero size means an infinite flat water plane. Otherwise bounds are world-space X/Z. |
| `public bool waveImpulsesEnabled` | Allow occasional wave torque impulses. Disabled timers reset to prevent a queued impulse on re-enable. Default: enabled. |
| `public bool yawDampingEnabled` | Apply passive damping around world up. Rudder response remains independent. Default: enabled. |
| `public float yawDampingScale` | Scales inherited Angular Damping for yaw; pitch/roll use Rocking Damping. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public BoatProfile()` | Constructs `BoatProfile` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
| `public override bool CanUsePropulsionBoost(VehicleController vehicle)` | Checks the profile propulsion switch and required water/support context before activation. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public virtual bool ContainsWater(Vector3 position)` | Checks whether a position lies inside this profile's fallback water region. | `position` — Requested point or switch detent; see its declared type and owning operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual void SetBuoyancyEnabled(bool enabled)` | Toggles gravity-derived flotation; vertical water damping remains independently configured. | `enabled` — Whether ordinary buoyancy is allowed. Sinking overrides this switch while active. |
| `public virtual void SetSinking(bool enabled)` | Starts or stops sinking without overwriting the authored buoyancy/damping switches. Native Rigidbody gravity supplies the downward force. | `enabled` — True suspends both upward flotation terms; false resumes configured behavior at the current position. Does not teleport, reset momentum or enable Rigidbody gravity. |
| `public virtual void StartSinking()` | Suspends upward buoyancy and vertical water damping. Equivalent to `SetSinking(true)`. | Idempotent; preserves hull drag and all authored mechanics switches. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Resolves steering, samples water and applies buoyancy, water-relative resistance, thrust and trim/rocking. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void StopSinking()` | Resumes configured flotation at the current position. Equivalent to `SetSinking(false)`. | Does not force buoyancy on if it was disabled separately. |
