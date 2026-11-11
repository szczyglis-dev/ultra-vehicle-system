# Engine and drivetrain API

Read [the system explanation](../Scripting/DriveDynamics.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [AutomaticGearbox](DriveDynamics.md#automaticgearbox)
- [Brakes](DriveDynamics.md#brakes)
- [BoostSuspensionSettings](DriveDynamics.md#boostsuspensionsettings)
- [BurnoutSuspensionSettings](DriveDynamics.md#burnoutsuspensionsettings)
- [Burnout](DriveDynamics.md#burnout)
- [Clutch](DriveDynamics.md#clutch)
- [Differential](DriveDynamics.md#differential)
- [Differential.Axle](DriveDynamics.md#differentialaxle)
- [DifferentialMode](DriveDynamics.md#differentialmode)
- [DrivingAssists](DriveDynamics.md#drivingassists)
- [Engine](DriveDynamics.md#engine)
- [EngineCore](DriveDynamics.md#enginecore)
- [EngineModule](DriveDynamics.md#enginemodule)
- [Gearbox](DriveDynamics.md#gearbox)
- [ManualGearbox](DriveDynamics.md#manualgearbox)
- [MotorcycleBalance](DriveDynamics.md#motorcyclebalance)
- [Nitro](DriveDynamics.md#nitro)
- [ParkingHold](DriveDynamics.md#parkinghold)
- [Steering](DriveDynamics.md#steering)
- [TractionControl](DriveDynamics.md#tractioncontrol)
- [Transmission](DriveDynamics.md#transmission)
- [TransmissionMode](DriveDynamics.md#transmissionmode)

## AutomaticGearbox

**Runtime/Engine/Gearbox/AutomaticGearbox.cs**

Makes automatic shift decisions from operating conditions.

**Inherits / implements:** [Gearbox](DriveDynamics.md#gearbox).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override bool AutomaticDirection { get; }` | Read-only/resolved automatic direction for `AutomaticGearbox`. |
| `public float downshiftRpm` | Downshift in revolutions per minute. Initial value: `2500`. |
| `public float minimumGearTime` | Minimum dwell before automatic upshifts and direction changes (.7 seconds). Low-RPM downshifts bypass this dwell and may skip ratios; shift duration, loaded-road-speed evidence, clutch guards and RPM limits still apply. |
| `public float reverseEngageSpeedKph` | Maximum speed treated as standstill for automatic reverse selection (km/h); allows small suspension/creep motion on slopes. |
| `public float upshiftRpm` | Upshift in revolutions per minute. Initial value: `7000`. |

## Brakes

**Runtime/Drive/Brakes/Brakes.cs**

Configuration/implementation type for brakes within engine and drivetrain.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<bool> BrakingChanged` | Moving service-brake activity changes; payload is active/inactive. Owned by Brakes, independent of TireFeedback. |
| `public event System.Action<bool> HandbrakeChanged` | When resolved handbrake state changes. Payload: bool. |
| `public event System.Action<float> ServiceBrakeChanged` | When resolved service braking changes. Payload: normalized resolved brake demand. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public float brakeEventMinimumSpeedKph` | Brake event minimum speed in km/h (stored value); Speed fields display the selected speed unit. Initial value: `3`. |
| `public float brakeEventThreshold` | Threshold/tolerance for brake event threshold. The corresponding action or transition is admitted only when its comparison condition is satisfied. Initial value: `.1f`. |
| `public float brakeRiseTime` | Seconds for a held digital brake to reach full service-brake strength. Zero is immediate. |
| `public virtual float DigitalBrakeStrength { get; }` | Read-only/resolved digital brake strength for Brakes. |
| `public Engine engine` | Optional explicit link when engine and brakes live on different objects. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public virtual bool Handbrake { get; protected set; }` | Read-only/resolved handbrake for Brakes. |
| `public float handbrakeTorque` | Force/torque budget for handbrake torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `6000`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public bool progressiveDigitalBraking` | Ramp button/keyboard service braking. Analog pedals always use their exact input strength. |
| `public float rollingBrakeTorque` | Optional constant brake torque while coasting. Zero allows natural downhill rolling. |
| `public virtual float ServiceBrake { get; protected set; }` | Resolved service-brake demand consumed by downstream mechanics and pedal presentation. |
| `public float slopeReverseReleaseGrace` | Seconds to recognize a fresh reverse press after releasing a stopped brake on a slope. Does not engage reverse from a continuously held brake. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController v)` | Resolves an Engine reference only when no explicit engine is assigned. | `v` — V, interpreted by this operation in the declared type. |
| `public override void Step(VehicleController v, Command c, float dt)` | Resolves signed-pedal direction/braking policy, publishes actuator demand and applies service/handbrake torques. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## BoostSuspensionSettings

**Runtime/Drive/Suspension/BoostSuspensionSettings.cs**

Shared physical suspension kick configuration. See [setup and behavior](../DrivingActions.md#suspension-kick-and-departure-wheelspin).

| Member | Meaning |
| --- | --- |
| `public bool enabled` | Enable effect; default true. |
| `public float frontLift` | Front extension in metres; default 0.035. |
| `public float rearCompression` | Rear compression in metres; default 0.02. |
| `public float riseTime` | Smooth rise in seconds; default 0.15. |
| `public float maximumTilt` | Gravity-relative pitch/roll cancellation angle; default 20 degrees. A fresh boost press is required after automatic suspension cancellation. |
| `public float returnTime` | Smooth recovery in seconds; default 0.3. |

## BurnoutSuspensionSettings

**Runtime/Drive/Suspension/BoostSuspensionSettings.cs**

**Inherits / implements:** [BoostSuspensionSettings](DriveDynamics.md#boostsuspensionsettings).

| Member | Meaning |
| --- | --- |
| `public float maximumForwardActivationSpeed` | Maximum forward speed for starting suspension kick, default 5 m/s (18 km/h). Reverse movement has no lower bound. An accepted kick remains active above this threshold; a rejected start requires a fresh press. Independent of burnout propulsion limits. |

## Burnout

**Runtime/Drive/Grounded/Burnout.cs**

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule), [IVehicleResetHandler](Modules.md#ivehicleresethandler).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action BurnoutStarted` | Assistance begins. |
| `public event System.Action BurnoutStopped` | Assistance ends, including reset/disable. |
| `public event System.Action<bool> StateChanged` | Reports transitions into and out of active assistance. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public BurnoutSuspensionSettings suspensionKick` | Supported front/rear spring shift; enabled by default, with a 0.9-second return. |
| `public bool automaticThrottle` | Supply a throttle request in the selected drive direction before brakes/gearbox/clutch while the held launch request is eligible. Default true. |
| `public bool forceForwardDirection` | Request forward drive during boost; disable to retain the selected direction. Default true. |
| `public float boatBowLiftDegrees` | Extra boat powered-pitch target degrees while Burnout is active; default 2, range 0–5; existing tilt/pitch guards remain. |
| `public bool bypassStabilityControl` | Temporarily skip Steering arcade yaw/lateral stabilization and slide speed hold during burnout. Default true; authored assist settings are preserved. |
| `public bool bypassTractionControl` | Let intentional wheelspin pass through the optional TCS while assistance is nonzero. Default true; normal TCS resumes after recovery. |
| `public float cooldown` | Seconds before starting another cycle after release/abort. Default 0.4. |
| `public float CooldownRemaining { get; }` | Seconds before another launch can begin. |
| `public override int ExecutionOrder { get; }` | 240; resolves wheelspin before engine torque. |
| `public float forwardGrip` | Driven tire longitudinal grip scale during wheelspin. Default 0.55, allowing forward motion while spinning. |
| `public float gripRecoveryTime` | Recovery interval after spin or release. Default 0.4 seconds. |
| `public float holdBrakeTorque` | Maximum per-wheel holding torque in N m before wheel brake multipliers. Default 8000. |
| `public float holdDuration` | Seconds at full non-driven-wheel hold. Default 0.6. |
| `public bool holdNonDrivenWheels` | Optional non-driven-wheel brake hold; disabled by default so the vehicle moves during wheelspin. |
| `public float holdReleaseTime` | Seconds to smoothly release that hold. Default 0.4. |
| `public bool IsActive { get; }` | Whether the installed module currently assists wheelspin. |
| `public float maximumSpinSpeed` | Safety speed cutoff for wheelspin assistance, independent of sustained steering. Default 60 m/s (216 km/h). |
| `public float maximumStartSpeed` | Highest speed at which a new burnout may start. Default 40 m/s (144 km/h), including starts while already driving. |
| `public float minimumEndSpeed` | Minimum road speed in m/s required for timed recovery while held. Default 12 (43.2 km/h); zero uses duration alone. Clamped to maximumSpinSpeed. Key release always begins recovery immediately. |
| `public override ExecutionPhase Phase { get; }` | Power in the Drive category; native profiles consume the resolved boost during Drive. |
| `public float Progress { get; }` | Elapsed spin and recovery fraction. |
| `public bool Requested { get; }` | Explicit held API request. |
| `public float sidewaysGrip` | Driven tire lateral grip scale during wheelspin. Default 0.4 for drifting and donuts; normal grip returns during recovery. |
| `public float spinDuration` | Minimum held wheelspin duration before recovery. Default 3 seconds; recovery also requires minimumEndSpeed and no sustained steering. |
| `public float Strength { get; }` | Current wheelspin assistance fraction. |
| `public override bool SupportsDirectControl { get; }` | Processes direct mode to clear assistance. |
| `public float sustainSteeringThreshold` | Steering magnitude required to retain a held powered slide. Default 0.15. |
| `public bool sustainWhileSteering` | Hold wheelspin while steering beyond sustainSteeringThreshold, even after the duration and minimum end speed. Default true; releasing Ctrl or the safety cutoff still ends assistance. |
| `public float throttle` | Automatic forward pedal strength. Default 1; range 0.1 to 1. |
| `public float torqueMultiplier` | Maximum temporary combustion/direct torque and finite power/acceleration-cap multiplier. Default 2.5; minimum 1. |
| `public float wheelSpeedMultiplier` | Bounded native wheel overspeed allowance during wheelspin. Default 1.5; range 1–2; prevents runaway wheel energy. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Caches the owning vehicle and resolves missing engine references during repeatable setup. | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
| `public void ResetState()` | Clear launch request, wheelspin, hold and cooldown. | See signature for arguments. |
| `public virtual void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |
| `public void SetBurnout(bool held)` | Set a held launch request; false starts recovery immediately. | See signature for arguments. |
| `public override void Step(VehicleController vehicle, Command command, float dt)` | Advance rolling or standing wheelspin, sustained powered turns and release recovery; apply optional holding brakes. | See signature for arguments. |

## Clutch

**Runtime/Engine/Gearbox/Clutch.cs**

Models coupling and finite rotational energy transfer.

**Inherits / implements:** [EngineModule](DriveDynamics.md#enginemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<bool> AutomaticChanged` | When automatic clutch assistance selection changes. Payload: bool. |
| `public event System.Action<float> EngagementChanged` | When resolved clutch coupling changes. Payload: normalized engagement, distinct from pedal travel. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool allowLaunchWheelspin` | Let stored flywheel energy briefly exceed traction control's propulsion budget on a clutch launch. |
| `public bool automatic` | Assist normal launches/coasting. Touching the clutch pedal always gives the driver direct control. |
| `public virtual bool DriverControlled { get; }` | Whether manual mode or a pedal override currently controls clutch engagement. |
| `public virtual float Engagement { get; protected set; }` | Resolved clutch coupling fraction: zero disconnected, one connected. |
| `public float engagementRate` | Automatic assistance only. Driver pedal/button input is applied immediately. |
| `public Engine engine` | Assign the engine Engine component/asset used by Clutch. |
| `public float engineBrakingTorque` | Force/torque budget for engine braking torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `35`. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public float manualEngagement` | Manual clutch engagement fraction: 0 disconnects the drivetrain and 1 requests full engagement. Initial value: `1`. |
| `public virtual float Pedal { get; protected set; }` | Clutch pedal travel: zero released, one fully pressed; opposite direction to engagement. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public virtual float SlipRpm { get; }` | Engine RPM minus gearbox-reflected wheel RPM; measures coupling slip. |
| `public float torqueCapacity` | Maximum crankshaft torque transmitted by a fully engaged clutch, in Nm. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resolves the engine only when no explicit reference is assigned. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void SetAutomatic(bool value)` | Chooses automatic clutch assistance rather than manual engagement ownership. | `value` — Requested bool state for this operation. |
| `public virtual void SetManualEngagement(float value)` | Requests normalized manual clutch coupling, distinct from clutch pedal travel. | `value` — Requested state/value in this operation's domain; use its configured range/unit. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Advances manual/automatic coupling and publishes `EngagementChanged` after a resolved coupling change. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## Differential

**Runtime/Engine/Drivetrain/Differential.cs**

Distributes driven axle torque.

**Inherits / implements:** [EngineModule](DriveDynamics.md#enginemodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Axle[] axles` | Ordered axles configuration entries. Expand each item; see Differential.Axle for its individual settings. Initial value: `Array.Empty<Axle>()`. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public float lockedCoupling` | Strength of the RPM-equalizing coupling in locked differential mode. Initial value: `4`. |
| `public float maximumLockTorque` | Force/torque budget for maximum lock torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `1000`. |
| `public DifferentialMode mode` | Selects the operating policy; see the listed options and the owning component guide. Options: `Open`, `LimitedSlip`, `Locked`. Initial value: `DifferentialMode.LimitedSlip`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public float slipRpmRange` | Wheel RPM difference that produces the full speed-based limited-slip bias. Initial value: `150`. |
| `public float torqueBiasRatio` | Multiplier/fraction controlling torque bias ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: `3`. |
| `public float tractionCoefficient` | Scales the traction estimate used to distribute differential torque. Initial value: `1`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Step(VehicleController v, Command c, float dt)` | Distributes axle torque and bounded shaft coupling; skips adding propulsion while service/handbraking. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## Differential.Axle

**Runtime/Engine/Drivetrain/Differential.cs**

Configuration/implementation type for axle within engine and drivetrain.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool enabled` | Includes this entry in its owning system's configured behavior. Initial value: `true`. |
| `public WheelCollider first` | Assign the first reference used by Differential.Axle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
| `public string label` | Readable name identifying this entry in configuration lists. Initial value: `"Axle"`. |
| `public WheelCollider second` | Assign the second reference used by Differential.Axle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |

## DifferentialMode

**Runtime/Engine/Drivetrain/Differential.cs**

Defines the allowed differential mode choices used by this topic.

### Values

- `Open`
- `LimitedSlip`
- `Locked`

## DrivingAssists

**Runtime/Drive/Core/DrivingAssists.cs**

Configuration/implementation type for driving assists within engine and drivetrain.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<bool> StabilityControlChanged` | When `DrivingAssists` changes its stability-assistance choice. Payload: bool. |
| `public event System.Action<bool> TractionControlChanged` | When `DrivingAssists` changes its coordinated traction-control choice. Payload: bool. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public float corneringFreedom` | Amount of cornering freedom retained while allocating traction between propulsion and turning. Initial value: `.65f`. |
| `public float lateralResponse` | Strength of sideways-motion correction relative to the vehicle. Initial value: `4`. |
| `public float launchReferenceSpeed` | Low-speed reference in m/s used to stabilize slip/traction calculations during launch. Initial value: `3`. |
| `public float maximumYawRate` | Upper requested yaw rate used by turning assistance, in rad/s. |
| `public float minimumTorqueScale` | Multiplier/fraction controlling minimum torque scale. Increasing it increases this contribution relative to the unscaled value. Initial value: `.08f`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public float recoveryRate` | Rate at which allowed drive torque recovers after excess slip subsides. Initial value: `1.8f`. |
| `public float reductionRate` | Rate at which allowed drive torque decreases when wheel slip exceeds the target. Initial value: `12`. |
| `public bool reserveGripForCornering` | When checked, reserve grip for cornering is active; when unchecked the owning system skips that optional policy. |
| `public bool stabilityControlEnabled` | Enables stability control behavior for this system. Initial value: `true`. |
| `public float stabilityStrength` | Overall blend/strength of the stability corrections; zero removes this assistance contribution. Initial value: `.70f`. |
| `public bool stabilizePoweredSlides` | Allows stability assistance to correct powered sliding instead of leaving it entirely to driver input. Initial value: `true`. |
| `public float targetSlip` | Desired longitudinal slip magnitude while applying propulsion torque. Initial value: `.22f`. |
| `public bool tractionControlEnabled` | Enables traction control behavior for this system. Initial value: `true`. |
| `public float tractionReserve` | Fraction of estimated traction kept available when limiting drive torque. Initial value: `.9f`. |
| `public float yawResponse` | Strength/speed of the yaw response toward the requested heading/turn behavior. Initial value: `7`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Apply()` | Writes coordinated traction/stability assist choices to the connected mechanics. Disabling the coordinator does not restore previous settings. | No arguments; no returned value. |
| `public override void Configure(VehicleController vehicle)` | Caches the vehicle and applies its coordinated assist choices. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void SetAssistsEnabled(bool value)` | Applies the application's combined assist enable choice through `DrivingAssists`. | `value` — Requested bool state for this operation. |
| `public virtual void SetStabilityControl(bool value)` | Changes the coordinated stability-assistance choice. | `value` — Requested bool state for this operation. |
| `public virtual void SetTractionControl(bool value)` | Changes the coordinated traction-control choice through `DrivingAssists`. | `value` — Requested bool state for this operation. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Applies the coordinator's current traction/stability choices to its connected mechanics. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## Engine

**Runtime/Engine/Engine.cs**

Resolves running state, RPM and propulsion torque/power.

**Inherits / implements:** [EngineModule](DriveDynamics.md#enginemodule), [IVehicleResetHandler](Modules.md#ivehicleresethandler).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<Gearbox> ActiveGearboxChanged` | Reports a change of effective gearbox identity, including removal or disable. Read ActiveGearbox when first subscribing. |
| `public event System.Action<bool> EngineStateChanged` | After engine running state changes. Payload: running bool; a rejected start does not report success. |
| `public event System.Action<int> GearChanged` | After accepted gear selection. Payload: signed gear index, with reverse -1, neutral 0 and forward gears positive. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual Gearbox ActiveGearbox { get; }` | Currently enabled connected gearbox, or `null` when no enabled gearbox participates. |
| `public float airborneTorqueWeight` | Relative torque weight of airborne wheels when other driven wheels have contact. One disables contact-based redistribution. |
| `public virtual float AverageWheelRpm { get; protected set; }` | Read-only/resolved average wheel rpm for Engine. |
| `public Clutch clutch` | Assign the clutch Clutch component/asset used by Engine. |
| `public float directSpeedLimiterRangeKph` | Additional speed fade range in km/h used by direct drive. |
| `public virtual float DriveDirectionSign { get; }` | +1 normally, -1 when longitudinal propulsion is inverted. |
| `public virtual float EffectiveMaxRpm { get; }` | Current engine redline including an active Nitro percentage increase. Base maxRpm is preserved; stop/release/depletion/disable restore the normal limit. Used by engine RPM targets, rev limiting, torque curve normalization and gearbox over-rev guards. |
| `public virtual bool EngineRunning { get; }` | Read-only/resolved engine running for Engine. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public virtual float FlywheelEnergyJoules { get; }` | Read-only/resolved flywheel energy joules for Engine. |
| `public Gearbox gearbox` | Optional plugin. Missing or disabled gearbox uses the original direct drive. |
| `public virtual string GearLabel { get; }` | Read-only/resolved gear label for Engine. |
| `public float idleRpm` | Engine idle speed in revolutions per minute. Initial value: `900`. |
| `public virtual float InertialDriveTorque { get; protected set; }` | Read-only/resolved inertial drive torque for Engine. |
| `public float internalFriction` | Fraction of peak torque lost to internal friction at maximum RPM with a driver-controlled clutch. |
| `public bool invertDriveDirection` | Reverses longitudinal propulsion while retaining logical throttle and gear direction. |
| `public virtual bool IsRunning { get; }` | Current is running predicate; read it instead of maintaining a second application flag. |
| `public float launchBlendSpeed` | Forward speed in m/s at which launch RPM support fully fades to idle RPM. |
| `public float launchRpm` | Engine speed target used for initial launch/clutch engagement. Initial value: `3200`. |
| `public float maximumDriveAcceleration` | Propulsion acceleration budget in m/s²; zero disables the limit. Compensate Drive Resistance additionally admits opposing load within available torque/power. |
| `public bool compensateDriveResistance` | Allow available torque to overcome measured opposing load and gravity without spending the acceleration budget; default true. Does not create torque or bypass tire traction. |
| `public float maximumPowerKw` | Maximum output power in `kW`; zero disables the power cap. |
| `public float maxRpm` | Engine upper speed limit in revolutions per minute. Initial value: `8000`. |
| `public virtual float NormalizedRpm { get; }` | Engine RPM normalized between idle and the current EffectiveMaxRpm. |
| `public virtual float OutputTorque { get; protected set; }` | Resolved propulsion torque after direction inversion; downstream allocation/intervention may limit wheel output. |
| `public float peakTorque` | Peak crankshaft combustion torque before ratio multiplication, in N·m. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public float response` | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: `3`. |
| `public float reverseSpeedRatio` | Multiplier/fraction controlling reverse speed ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: `0.3f`. |
| `public float revLimiterRange` | RPM range over which the coupled shaft rev limiter fades propulsion torque. |
| `public float rotationalInertia` | Engine/flywheel rotational inertia in kg m², used when the driver operates the clutch. |
| `public virtual float Rpm { get; protected set; }` | Resolved engine rotational speed in revolutions per minute. |
| `public float rpmResponse` | Response toward rpm response. Higher values follow the requested state faster. Initial value: `10`. |
| `public float shiftRpmResponse` | RPM response per second while shifting. Lower values give a slower RPM drop, independently of vehicle type. |
| `public float speedLimiterRangeKph` | Road-speed range in km/h over which propulsion fades near the top speed. |
| `public override bool SupportsDirectControl { get; }` | Opts into direct-mode stepping; updates RPM and gearbox presentation without propulsion forces. |
| `public override bool SupportsReleasedForces { get; }` | Keeps passive maintenance/observation active during release; Drive and Engine suppress force output, and TireCollision keeps native solid proxies without supplemental tread forces. |
| `public virtual float Throttle { get; }` | Read-only/resolved throttle for Engine. |
| `public AnimationCurve torqueCurve` | Engine torque shape over normalized engine speed. Tune together with the engine torque and RPM limits. |
| `public virtual float TransmittedClutchTorque { get; protected set; }` | Read-only/resolved transmitted clutch torque for Engine. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Caches the owner, synchronizes running state, configures registered gearboxes and resolves missing drivetrain references. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void ResetState()` | Clears the declaring mechanic's retained simulation history at an explicit reset boundary. | No arguments; no returned value. |
| `public virtual void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |
| `public virtual void SetEngineRunning(bool running)` | Requests the engine running state through ignition/fuel policy and transition notifications. | `running` — Requested running state. |
| `public virtual void StartEngine()` | Requests ignition, respecting the active fuel/engine policy. | No arguments; no returned value. |
| `public override void Step(VehicleController v, Command c, float dt)` | Resolves running state, demand, RPM and torque output; stopped engines clear their propulsion state. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |
| `public virtual void StopEngine()` | Requests engine shutdown and running-state notifications. | No arguments; no returned value. |
| `public virtual void ToggleEngine()` | Requests the opposite engine-running state through ignition/shutdown policy. | No arguments; no returned value. |

## EngineCore

**Runtime/Engine/Core/EngineCore.cs**

Configuration/implementation type for engine core within engine and drivetrain.

**Inherits / implements:** [CategoryCore](Modules.md#categorycore).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public EngineCore()` | Constructs `EngineCore` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## EngineModule

**Runtime/Engine/Core/EngineModule.cs**

Configuration/implementation type for engine module within engine and drivetrain.

**Inherits / implements:** [VehicleModule](Modules.md#vehiclemodule), [IEngineModule](Modules.md#ienginemodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |

## Gearbox

**Runtime/Engine/Gearbox/Gearbox.cs**

Shared validated selection, ratios and shift state.

**Inherits / implements:** [EngineModule](DriveDynamics.md#enginemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<int> GearChanged` | After accepted gear selection. Payload: signed gear index, with reverse -1, neutral 0 and forward gears positive. |
| `public event System.Action<int> ShiftCompleted` | When that shift interval completes; a zero-duration shift can complete immediately. Payload: gear index. |
| `public event System.Action<int> ShiftStarted` | When an accepted selection starts its shift interval. Payload: selected gear index. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual bool AutomaticDirection { get; }` | Read-only/resolved automatic direction for Gearbox. |
| `public virtual int CurrentGear { get; }` | Selected signed gear index: -1 reverse, 0 neutral, positive forward. |
| `public float directionChangeSpeed` | Maximum movement speed at which a requested forward/reverse change is admitted. Initial value: `0.6f`. |
| `public float efficiency` | Fraction of drivetrain output retained after transmission losses. Initial value: `0.9f`. |
| `public float finalDrive` | Final-drive ratio multiplying the selected gear ratio. Initial value: `3.4f`. |
| `public float[] forwardRatios` | Forward gear ratios, first gear at index 0. Used directly with no custom speed ranges. |
| `public virtual int GearCount { get; }` | Number of configured forward gears. |
| `public virtual string GearLabel { get; }` | Read-only/resolved gear label for Gearbox. |
| `public float[] gearSpeedLimitsKph` | Optional road speed at engine redline per forward gear, in km/h. Empty uses the authored Forward Ratios directly. Non-empty values derive ratios from wheel radius and engine RPM. |
| `public virtual bool IsShifting { get; }` | Whether the gearbox's configured shift interval is still active. |
| `public virtual float Ratio { get; }` | Current signed transmission ratio including the declaring gearbox's ratio policy. |
| `public float reverseRatio` | Positive reverse gear reduction before final drive. |
| `public float reverseSpeedLimitKph` | Optional reverse road speed at redline; zero preserves the authored Reverse Ratio. |
| `public float shiftDuration` | Time in seconds during which gear-changing torque transfer is interrupted/blended. Initial value: `.14f`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void ConfigureFor(VehicleController vehicle, Engine engine)` | Connects and prepares the gearbox for its vehicle and engine context. | `vehicle` — Vehicle context/owner receiving the operation. `engine` — Engine whose running/RPM/gearbox state supplies the operation. |
| `public virtual void Simulate(VehicleController vehicle, Command command, float wheelRpm, float maxRpm, float dt)` | Advances gearbox shift/selection state for one mechanical timestep. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `wheelRpm` — Wheel rotational speed in revolutions per minute. `maxRpm` — Engine redline used for selection validation. `dt` — Elapsed time in seconds. |
| `public virtual void Synchronize(int gear)` | Synchronizes the gear selector as an explicit helper. It does not replace `TrySelectGear` safety validation for driving input. | `gear` — Signed gear index: -1 reverse, 0 neutral, positive forward. |
| `public virtual bool TrySelectGear(int gear, float forwardSpeed, float wheelRpm, float maxRpm)` | Selects a signed gear (-1 reverse, 0 neutral, positive forward). Rejects invalid/unchanged gears, an active shift, unsafe direction changes or unsafe over-rev. The vehicle overload verifies this is the engine's active gearbox; the numeric overload takes explicit speed/RPM evidence. | `gear` — Signed gear index: -1 reverse, 0 neutral, positive forward. `forwardSpeed` — Signed forward speed in m/s. `wheelRpm` — Wheel rotational speed in revolutions per minute. `maxRpm` — Engine redline used for selection validation. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TrySelectGear(int gear, VehicleController vehicle)` | Selects a signed gear (-1 reverse, 0 neutral, positive forward). Rejects invalid/unchanged gears, an active shift, unsafe direction changes or unsafe over-rev. The vehicle overload verifies this is the engine's active gearbox; the numeric overload takes explicit speed/RPM evidence. | `gear` — Signed gear index: -1 reverse, 0 neutral, positive forward. `vehicle` — Vehicle context/owner receiving the operation. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TryShiftDown(VehicleController vehicle)` | Requests the next lower gear through the gearbox's validated selection path. | `vehicle` — Vehicle context/owner receiving the operation. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TryShiftUp(VehicleController vehicle)` | Requests the next higher gear through the gearbox's validated selection path. | `vehicle` — Vehicle context/owner receiving the operation. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |

## ManualGearbox

**Runtime/Engine/Gearbox/ManualGearbox.cs**

Provides the manually selected gearbox implementation.

**Inherits / implements:** [Gearbox](DriveDynamics.md#gearbox).

## MotorcycleBalance

**Runtime/Drive/Grounded/MotorcycleBalance.cs**

Configuration/implementation type for motorcycle balance within engine and drivetrain.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual void SuspendBalance(float duration)` | Temporarily release assisted roll control for the given seconds without changing authored settings. Respawn or driver entry clears suppression. |
| `public float accelerationSmoothTime` | Smoothing time for measured path acceleration, in seconds. Initial value: `.2`. |
| `public bool coordinateSteering` | Optional wheel-angle limit based on the supported bank at speed. Initial value: `false`. |
| `public float reversalLeanRate` | Opposite-bank target rate in degrees/s, at least Lean Rate. Initial value: `280`. |
| `public virtual float CorneringAccelerationLimit { get; }` | Supported lateral path acceleration in m/s², derived from gravity, Maximum Lean and Steering Balance Margin. |
| `public float steeringBalanceMargin` | Cornering capacity fraction shared by path assistance and optional wheel-angle limiting. Initial value: `.85`. |
| `public virtual float ActualLean { get; protected set; }` | Read-only/resolved actual lean for `MotorcycleBalance`. |
| `public float balanceDamping` | Damping applied to roll while maintaining motorcycle balance. Initial value: `65`. |
| `public float balanceStrength` | Strength of the restoring torque toward the requested motorcycle lean. Initial value: `1200`. |
| `public virtual float CurrentLean { get; protected set; }` | Read-only/resolved current lean for `MotorcycleBalance`. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public float fullLeanSpeed` | Ground speed in m/s at which full banking is available. |
| `public float leanRate` | Maximum rate at which requested motorcycle lean changes, in degrees per second. Initial value: `140`. |
| `public float leanRateDamping` | Feed-forward damping of the requested lean rate. |
| `public float leanStartSpeed` | Ground speed in m/s below which banking fades to zero. |
| `public float maximumAngularAcceleration` | Upper bound on the profile's applied angular acceleration. Initial value: `150`. |
| `public float maximumLean` | Largest requested motorcycle lean angle in degrees. Initial value: `35`. |
| `public float measuredAccelerationWeight` | Blend steering anticipation with actual path acceleration; chassis yaw spin does not count as cornering. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public float recoveryAngle` | Recovery angle in degrees, relative to the owning mechanism's reference frame. Initial value: `65`. |
| `public float steeringPrediction` | Blend from current wheel steering to anticipated driver steering. |
| `public virtual float TargetLean { get; protected set; }` | Requested motorcycle lean after steering and speed resolution, in degrees. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual float ConstrainSteering(VehicleController vehicle, float requestedAngle)` | Resolve a steering demand inside the configured cornering envelope without changing Rigidbody inertia. Low-speed full lock remains available. | `vehicle` — Owning vehicle. `requestedAngle` — Road-wheel angle in degrees. **Returns:** Allowed road-wheel angle in degrees. |
| `public override void Configure(VehicleController vehicle)` | Measures wheelbase and prepares wheel/contact geometry for balance response. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Uses gravity, contact and steering evidence to apply bounded motorcycle lean/balance support. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## Nitro

**Runtime/Engine/Boost/Nitro.cs**

**Inherits / implements:** [EngineModule](DriveDynamics.md#enginemodule), [IVehicleResetHandler](Modules.md#ivehicleresethandler).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<float> AmountChanged` | Reports actual remaining charge after a change; payload is charge units. |
| `public event Action<bool> BoostStateChanged` | Reports transitions into/out of resolved boost; payload is the active flag. |
| `public event Action Depleted` | Raised once when positive charge reaches zero. |
| `public event Action NitroStarted` | Effective boost begins. |
| `public event Action NitroStopped` | Effective boost ends, including reset/disable. |
| `public event Action<bool> OutputStateChanged` | Reports a change of the propulsion-output session. Receivers can be absent without affecting boost. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public BoostSuspensionSettings suspensionKick` | Configurable supported spring displacement, enabled by default. |
| `public bool launchWheelspin` | Enable one departure grip pulse per nitro activation; default true. |
| `public float launchSpeed` | Departure threshold in m/s; default 1. |
| `public float launchGripDuration` | Smooth recovery duration in seconds; default 0.65. |
| `public float launchForwardGrip` | Departure longitudinal grip fraction; default 0.35. |
| `public float launchSidewaysGrip` | Departure lateral grip fraction; default 0.65. |
| `public float accelerationMultiplier` | Multiplier for the finite wheel-drive acceleration cap. Default 3. |
| `public float additionalAcceleration` | Additional grounded chassis acceleration in m/s², independent of tire torque limits. Default 10; zero uses engine torque only. Stops immediately on release, braking or loss of eligibility; fades near boosted top speed. |
| `public float additionalMaxRpmPercent` | Extra engine redline as a percentage during boost. Default 25 raises 8000 RPM to 10000; zero preserves the normal limit. Scales with final partial boost strength and stays available through an internal shift. |
| `public float additionalPowerKw` | Extra engine power allowance in kW. Default 350; an uncapped engine remains uncapped. |
| `public bool allowPitchAboveMaxRpm` | Default true. Controls RPM-driven Engine Audio pitch above its ordinary maximum when actual RPM exceeds this engine base redline. Applies per Nitro component to sounds following its engine; constant/motion/fixed-pitch sounds remain unchanged. Unity pitch ceiling remains 3. |
| `public bool allowReverse` | Permit boost in reverse. Default true. |
| `public bool forceForwardDirection` | Request forward drive during boost; disable to retain the selected direction. Default true. |
| `public bool automaticRefill` | Refill automatically after release and refillDelay. Default false; demo Car enables it. |
| `public float buildUpTime` | Seconds for boost power to build from zero to full. Default 0.2; zero gives immediate full power. Release/braking removes assistance immediately. Consumption follows the resolved power fraction. Internal shifts preserve the existing build-up level. |
| `public float capacity` | Maximum charge in arbitrary consistent units. Default 100; minimum 0.01. |
| `public bool consumesNitro` | Consume supply while boosting. Default true; false permits unlimited boost even with zero charge. |
| `public float cooldown` | Seconds before a new activation after boost stops. Default 0.25. |
| `public virtual float CooldownRemaining { get; protected set; }` | Seconds until a new activation may begin. |
| `public Engine engine` | Registered engine receiving the boost; leave unassigned to resolve it from the owning vehicle. |
| `public override int ExecutionOrder { get; }` | 250, so supply and boost resolve before Engine output. |
| `public float fullTankDuration` | Seconds of full boost supplied by a full tank. Default 15; consumption is capacity / duration per second. |
| `public virtual bool HasOutput { get; private set; }` | Current propulsion-output session, including retained output during internal shifts. Read on subscription to initialize presentation. |
| `public virtual bool IsBoosting { get; }` | Whether an enabled Nitro component currently contributes boost. |
| `public bool lockAutomaticGearChanges` | Default true. Suppresses automatic gear selection while boost is actually active, including an internal shift interruption. Explicit manual gear requests still use normal safety guards. Disabling this restores the usual automatic shift behavior. |
| `public float minimumActivationAmount` | Minimum charge needed to begin a new activation. Default 1; an active use may consume its remaining partial charge. |
| `public float minimumThrottle` | Minimum requested throttle magnitude required for boost. Default 0.1; nonzero propulsion demand is always required. |
| `public virtual float NormalizedAmount { get; }` | Remaining / capacity, from zero to one. |
| `public virtual float OutputStrength { get; }` | Current boost presentation strength, including retained RPM assistance during internal shifts. |
| `public override ExecutionPhase Phase { get; }` | Power phase, before Engine. |
| `public float refillDelay` | Seconds since last boost before automatic refill; a held request also blocks refill. Default 1. |
| `public float refillPerSecond` | Automatic refill rate in charge units per second. Default 25. |
| `public virtual float Remaining { get; }` | Charge clamped to the configured capacity. |
| `public virtual bool Requested { get; }` | Explicit component API/Inspector request; Command.Nitro independently contributes to the held request. |
| `public bool requireGroundContact` | Require at least one supported driven tire. Default false. |
| `public float shiftSpeedMultiplier` | Gear-change and automatic gear dwell speed multiplier during boost. Default 4; preserves authored gearbox settings. |
| `public virtual float Strength { get; protected set; }` | Resolved boost fraction for this tick; the final partial charge may supply less than one. |
| `public override bool SupportsDirectControl { get; }` | True so direct-pose mode can clear the active boost state without consuming supply or producing forces. |
| `public float topSpeedMultiplier` | Multiplier for the engine road-speed envelope. Default 1.35. |
| `public float torqueMultiplier` | Engine combustion/direct-drive torque multiplier. Default 3. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual float AddNitro(float value)` | Adds a positive finite amount, clamps at capacity, and returns the charge actually accepted. | See signature for arguments. |
| `public override void Configure(VehicleController vehicle)` | Resolves an unassigned engine and clamps the starting charge; does not refill automatically. | See signature for arguments. |
| `public virtual void Refill()` | Fills the current capacity through SetAmount. | See signature for arguments. |
| `public virtual void ResetState(bool refill = false)` | Clears API request, boost, cooldown and refill timer. Supply is retained unless refill is true. | See signature for arguments. |
| `public virtual void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |
| `public virtual void SetAmount(float value)` | Sets charge clamped to [0, capacity], notifying amount/depletion transitions. Non-finite values are ignored. | See signature for arguments. |
| `public virtual void SetBoost(bool held)` | Sets the explicit held boost request; pass false on release. Engine throttle and eligibility checks still apply. | See signature for arguments. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Resolve boost eligibility and supply, increase engine output and apply configured extra grounded acceleration. Shifts suspend boost without a new cooldown. | See signature for arguments. |

## ParkingHold

**Runtime/Drive/Brakes/ParkingHold.cs**

Configuration/implementation type for parking hold within engine and drivetrain.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool assistParkingBrake` | Counter gravity-driven slope creep while the handbrake or detached-trailer parking brake is active; native tires handle braking and external pushes. |
| `public bool assistServiceBrake` | Counter gravity-driven slope creep while the service brake is active; no added planar braking resistance on level ground. |
| `public float captureSpeed` | Maximum vehicle speed in m/s at which the stationary parking/service hold can capture the body. Initial value: `.5f`. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resolves the local Trailer used by detached-parking policy. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Adds bounded low-speed support while applicable parking/service braking is active; does nothing for a sleeping body. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## Steering

**Runtime/Drive/Steering/Steering.cs**

Configuration/implementation type for steering within engine and drivetrain.

**Inherits / implements:** [DriveModule](DriveProfiles.md#drivemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<float> AngleChanged` | When resolved road-wheel steering angle changes. Payload: angle in degrees, not column degrees. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public float ackermann` | Blend toward Ackermann inner/outer wheel steering geometry; zero uses parallel steering. Initial value: `1`. |
| `public bool advancedSteeringGeometry` | Optional radius/grip limits and Ackermann geometry. Off uses the configured steering angle directly. |
| `public virtual float Angle { get; }` | Read-only/resolved angle for Steering. |
| `public bool arcadeHandling` | Game-oriented yaw and lateral grip assistance while tires touch the ground. |
| `public float arcadeLateralAcceleration` | Force/torque budget for arcade lateral acceleration; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `35`. |
| `public float assistanceStrength` | Overall strength of the optional yaw/lateral steering assistance. Initial value: `.70f`. |
| `public virtual float CurrentAngleLimit { get; protected set; }` | Read-only/resolved current angle limit for Steering. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public float highSpeedAngleRatio` | Multiplier/fraction controlling high speed angle ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: `0.3f`. |
| `public float lateralResponse` | Strength of sideways-motion correction relative to the vehicle. Initial value: `4`. |
| `public float maximumLateralAcceleration` | Steering authority at speed is limited to this requested lateral acceleration (m/s²). |
| `public float maximumYawRate` | Upper requested yaw rate used by turning assistance, in rad/s. |
| `public float minimumTurnRadius` | Minimum rear-axle centre turning radius in metres; zero disables the low-speed radius cap. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public bool speedSensitiveSteering` | Optional reduction of steering angle with speed. Off preserves full steering authority. |
| `public bool stabilizePoweredSlides` | Keep a powered full-lock slide near its entry speed instead of accelerating into an expanding circle. |
| `public virtual bool StabilizingPoweredSlide { get; }` | Read-only/resolved stabilizing powered slide for Steering. |
| `public bool useGroundGripLimit` | When checked, use ground grip limit is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public virtual float Wheelbase { get; protected set; }` | Measured axle span used by steering geometry, in metres. |
| `public float yawResponse` | Strength/speed of the yaw response toward the requested heading/turn behavior. Initial value: `7`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void RefreshWheelBindings(VehicleController vehicle)` | Rebuilds prepared steering membership, multipliers and tie-rod links while preserving actuator angle; removed steering outputs are cleared. | — |
| `public override void Configure(VehicleController vehicle)` | Discovers owned steering tie rods and measures axle/wheel geometry for its steering model. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public override void Step(VehicleController v, Command c, float dt)` | Advances steering response/native wheel angles, publishes the resolved actuator and emits `AngleChanged` on a change. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## TractionControl

**Runtime/Engine/Drivetrain/TractionControl.cs**

Limits propulsion according to contact capacity and slip.

**Inherits / implements:** [EngineModule](DriveDynamics.md#enginemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<bool> ActiveChanged` | When resolved traction-control intervention changes between active/inactive. Payload: bool; enabled configuration is a separate state. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual bool Active { get; }` | Read-only/resolved active for `TractionControl`. |
| `public float corneringFreedom` | Allow power-dependent wheelspin during tight powered turns, while retaining straight-line launch control. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public float launchReferenceSpeed` | Low-speed reference in m/s used to stabilize slip/traction calculations during launch. Initial value: `3`. |
| `public virtual float MaximumSlip { get; protected set; }` | Read-only/resolved maximum slip for `TractionControl`. |
| `public float minimumTorqueScale` | Multiplier/fraction controlling minimum torque scale. Increasing it increases this contribution relative to the unscaled value. Initial value: `.08f`. |
| `public virtual float MinimumTorqueScale { get; protected set; }` | Read-only/resolved minimum torque scale for `TractionControl`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public float recoveryRate` | Rate at which allowed drive torque recovers after excess slip subsides. Initial value: `1.8f`. |
| `public float reductionRate` | Rate at which allowed drive torque decreases when wheel slip exceeds the target. Initial value: `12`. |
| `public bool reserveGripForCornering` | When checked, reserve grip for cornering is active; when unchecked the owning system skips that optional policy. |
| `public float targetSlip` | Desired longitudinal slip magnitude while applying propulsion torque. Initial value: `.22f`. |
| `public float tractionReserve` | Fraction of estimated traction kept available when limiting drive torque. Initial value: `.9f`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resets retained intervention feedback before later propulsion steps. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void SetTractionControlEnabled(bool value)` | Enables/disables this traction-control module through its module action. | `value` — Requested bool state for this operation. |
| `public override void Step(VehicleController vehicle, Command command, float deltaTime)` | Limits wheel propulsion from contact/slip evidence and emits `ActiveChanged` when intervention state changes. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## Transmission

**Runtime/Engine/Gearbox/Transmission.cs**

Selects Direct, Manual or Automatic transmission operation.

**Inherits / implements:** [EngineModule](DriveDynamics.md#enginemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<TransmissionMode> ModeChanged` | After the declaring component's selected mode changes. Payload: its mode enum. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public AutomaticGearbox automatic` | Assign the automatic AutomaticGearbox component/asset used by Transmission. |
| `public Engine engine` | Assign the engine Engine component/asset used by Transmission. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public ManualGearbox manual` | Assign the manual ManualGearbox component/asset used by Transmission. |
| `public TransmissionMode mode` | Selects the operating policy; see the listed options and the owning component guide. Options: `Automatic`, `Manual`, `Direct`. Initial value: `TransmissionMode.Automatic`. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resolves missing engine/manual/automatic references and applies the selected transmission mode. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void SetMode(TransmissionMode value)` | Changes transmission or camera mode through the declaring component's transition rules. | `value` — Requested state/value in this operation's domain; use its configured range/unit. |
| `public override void Step(VehicleController v, Command c, float dt)` | Consumes a transmission toggle or changed mode field and applies the selected Direct/Manual/Automatic implementation. | `v` — V, interpreted by this operation in the declared type. `c` — C, interpreted by this operation in the declared type. `dt` — Elapsed time in seconds. |

## TransmissionMode

**Runtime/Engine/Gearbox/Transmission.cs**

Defines the allowed transmission mode choices used by this topic.

### Values

- `Automatic`
- `Manual`
- `Direct`
