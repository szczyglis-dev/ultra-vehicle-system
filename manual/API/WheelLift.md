# Wheel lift API

See [Wheel Lift](../DrivingActions.md#wheel-lift-wheelie) for setup, units, defaults and activation behavior.

## Types

- [WheelLift](WheelLift.md#wheellift)

## WheelLift

**Runtime/Physics/Wheels/WheelLift.cs**

See [Wheel Lift](../DrivingActions.md#wheel-lift-wheelie) for defaults, units and activation guards.

**Inherits / implements:** [PhysicsModule](Modules.md#physicsmodule), [IVehicleResetHandler](Modules.md#ivehicleresethandler).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<bool> StateChanged` | New assistance state. |
| `public event Action WheelLiftStarted` | Assistance begins. |
| `public event Action WheelLiftStopped` | Assistance ends after controlled lowering, or immediately on reset/disable/excessive tilt. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public float angleDamping` | Pitch angular velocity damping. |
| `public float angleStrength` | Pitch feedback gain. |
| `public float AppliedForce { get; private set; }` | Most recent lift force in newtons. |
| `public bool compensateGravity` | Feed-forward gravity moment compensation. |
| `public float CurrentAngle { get; private set; }` | Pitch relative to gravity in degrees. |
| `public override int ExecutionOrder { get; }` | Default order 660. |
| `public AnimationCurve forceCurve` | Normalized ramp shaping curve. |
| `public float groundContactGraceTime` | Brief support-loss recovery interval in seconds; default .75. |
| `public bool IsActive { get; }` | Enabled with positive assistance strength. |
| `public bool IsLanding { get; }` | Controlled lowering is in progress. |
| `public float landingTime` | Pitch-target lowering interval in seconds, default 1. |
| `public float landingTimeout` | Maximum landing interval in seconds, default 3. |
| `public Transform liftPoint` | Optional world-space force point override. |
| `public Vector3 localLiftPoint` | Vehicle-local fallback force point. |
| `public float maximumForce` | Upward force cap in newtons. |
| `public float maximumLiftAcceleration` | Additional upward force cap per chassis mass, in m/s²; default 8. |
| `public float maximumRecoveryAcceleration` | Corrective pitch acceleration limit in rad/s²; default 300. |
| `public float maximumRoll` | Roll activation limit in degrees. |
| `public float maximumSpeed` | Maximum absolute forward speed in m/s. |
| `public float maximumSupportDampingAcceleration` | Maximum chassis acceleration from support rebound damping in m/s²; default 15. |
| `public float minimumSpeed` | Minimum absolute forward speed in m/s. |
| `public override ExecutionPhase Phase { get; }` | Balance phase. |
| `public float releaseTime` | Force-request fade in seconds; necessary touchdown support can outlast it. |
| `public bool Requested { get; private set; }` | API held request; combined with Command.WheelLift. |
| `public bool requireGroundContact` | Require support to start lifting and apply upward force. |
| `public bool requireRunningEngine` | Require an enabled, running engine. |
| `public float riseTime` | Ramp-up duration in seconds. |
| `public float safetyAngle` | Absolute pitch activation limit in degrees. |
| `public float Strength { get; private set; }` | Shaped lifting assistance; full pitch authority during controlled lowering. |
| `public float supportReboundDamping` | Contact-relative upward rebound damping response in 1/s; default 10, zero disables it. |
| `public override bool SupportsDirectControl { get; }` | Runs cleanup while direct control owns motion; applies no force. |
| `public float targetAngle` | Target pitch in degrees. |
| `public Wheel[] wheels` | Lift wheel selection; empty selects steering wheels. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Reset transient state during configuration. | — |
| `public void ResetState()` | Clear request, ramp and telemetry; stop event if previously active. | — |
| `public virtual void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |
| `public void SetStrength(float value)` | Set normalized request intensity, ignoring non-finite input. | — |
| `public void SetTargetAngle(float degrees)` | Set pitch target, clamped to 0–75 degrees. | — |
| `public void SetWheelLift(bool held)` | Hold/release the API request. | — |
| `public override void Step(VehicleController vehicle, Command command, float dt)` | Resolve guards and ramp; apply bounded force at selected point. | — |
| `public override bool SupportsProfile(DriveProfile profile)` | Wheel profiles only (also accepts null). | — |
