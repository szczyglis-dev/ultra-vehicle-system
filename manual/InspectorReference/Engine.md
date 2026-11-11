# Engine, fuel and transmission

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [AutomaticGearbox](#automaticgearbox) | 4 |
| [Clutch](#clutch) | 7 |
| [Differential](#differential) | 7 |
| [Differential.Axle](#differentialaxle) | 4 |
| [Engine](#engine) | 22 |
| [EngineModule](#enginemodule) | 0 |
| [FuelTank](#fueltank) | 6 |
| [Gearbox](#gearbox) | 9 |
| [ManualGearbox](#manualgearbox) | 0 |
| [Nitro](#nitro) | 25 |
| [TractionControl](#tractioncontrol) | 8 |
| [Transmission](#transmission) | 4 |

## AutomaticGearbox

Makes automatic shift decisions from operating conditions.

**Source:** `Runtime/Engine/Gearbox/AutomaticGearbox.cs`. Component / asset.

**Inherited settings:** [Gearbox](Engine.md#gearbox). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `downshiftRpm` | `float` | Engine RPM below which the automatic gearbox requests a lower gear. It avoids shifts that would raise RPM too far. Raise this to downshift sooner as the vehicle slows. | `2500`; Minimum: 500 |
| `minimumGearTime` | `float` | Minimum seconds before automatic upshifts and direction changes. Low-RPM downshifts bypass this dwell and may skip ratios to catch up with braking, while retaining shift duration and safe RPM. | `0.7`; Minimum: 0 |
| `reverseEngageSpeedKph` | `float` | Maximum speed treated as standstill for automatic reverse selection (km/h); allows small suspension/creep motion on slopes. | `.5`; Speed field; stored in km/h, displayed in the selected speed unit |
| `upshiftRpm` | `float` | Engine RPM above which the automatic gearbox requests the next higher gear. A shift is skipped if the next gear would leave RPM too low. Raise this to hold gears longer. | `7000`; Minimum: 1000 |

## Clutch

Models coupling and finite rotational energy transfer.

**Source:** `Runtime/Engine/Gearbox/Clutch.cs`. Component / asset.

**Inherited settings:** [EngineModule](Engine.md#enginemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `allowLaunchWheelspin` | `bool` | Let stored flywheel energy briefly exceed traction control's propulsion budget on a clutch launch. | `true` |
| `automatic` | `bool` | Assist normal launches/coasting. Touching the clutch pedal always gives the driver direct control. | `true` |
| `engagementRate` | `float` | Speed at which automatic clutch assistance changes engagement. Higher values couple/disconnect faster. Direct driver pedal/button input bypasses this smoothing. | `5`; Minimum: .1f |
| `engine` | `Engine` ([fields](Engine.md#engine)) | Engine whose RPM and drivetrain connection this clutch uses. If empty, setup looks for the vehicle's Engine module. | `None / unassigned` |
| `engineBrakingTorque` | `float` | Base braking torque in N·m when the throttle is released and the assisted clutch is engaged. Gear ratio and shaft RPM scale the wheel braking. Higher values slow the vehicle more strongly; this does not hold a stopped vehicle on a slope. | `35`; Minimum: 0 |
| `manualEngagement` | `float` | Manual clutch engagement fraction: 0 disconnects the drivetrain and 1 requests full engagement. | `1`; Range: 0 to 1 |
| `torqueCapacity` | `float` | Maximum crankshaft torque transmitted by a fully engaged clutch, in Nm. | `650`; Minimum: 0 |

## Differential

Distributes driven axle torque.

**Source:** `Runtime/Engine/Drivetrain/Differential.cs`. Component / asset.

**Inherited settings:** [EngineModule](Engine.md#enginemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `axles` | `Axle[]` ([fields](Engine.md#differentialaxle)) | Pairs of driven wheel colliders that share torque through this differential. Add one entry for each driven axle; a wheel should belong to only one pair. | `Empty list` |
| `lockedCoupling` | `float` | Strength of the RPM-equalizing coupling in locked differential mode. | `4`; Minimum: 0 |
| `maximumLockTorque` | `float` | Maximum N·m transferred from the faster wheel to the slower wheel in Locked mode. Increase for stronger locking; reduce to let wheel speeds differ more while turning. | `1000`; Minimum: 0 |
| `mode` | `DifferentialMode` | Open splits torque equally but limits both wheels to the weaker wheel's grip. LimitedSlip shifts more torque toward the slower, better-supported wheel. Locked adds opposing torque to reduce the wheel RPM difference. Options: `Open`, `LimitedSlip`, `Locked`. | `DifferentialMode.LimitedSlip` |
| `slipRpmRange` | `float` | Wheel RPM difference that produces the full speed-based limited-slip bias. | `150`; Minimum: 1 |
| `torqueBiasRatio` | `float` | Largest torque split allowed in LimitedSlip mode. At 3, one wheel can receive up to three times the other's share. At 1, both receive equal shares. | `3`; Range: 1 to 8 |
| `tractionCoefficient` | `float` | Scales the traction estimate used to distribute differential torque. | `1`; Range: .1f to 3 |

## Differential.Axle

Configuration/implementation type for axle within engine and drivetrain.

**Source:** `Runtime/Engine/Drivetrain/Differential.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `enabled` | `bool` | Enables torque redistribution for this wheel pair. When off, the differential leaves this pair's existing motor torques alone. | `true` |
| `first` | `WheelCollider` | One driven wheel collider in this axle pair, normally the left wheel. The differential compares its RPM and grip with Second and redistributes their combined motor torque. | `None / unassigned` |
| `label` | `string` | Readable name for this wheel pair, such as Rear Axle. Torque behaviour comes from its wheel assignments and differential settings, not this label. | `"Axle"` |
| `second` | `WheelCollider` | The other driven wheel collider in this axle pair, normally the right wheel. Assign a different wheel from First; an incomplete or duplicate pair is skipped. | `None / unassigned` |

## Engine

Resolves running state, RPM and propulsion torque/power.

**Source:** `Runtime/Engine/Engine.cs`. Component / asset.

**Inherited settings:** [EngineModule](Engine.md#enginemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `airborneTorqueWeight` | `float` | Relative torque weight of airborne wheels when other driven wheels have contact. One disables contact-based redistribution. | `.1`; Range: 0 to 1 |
| `clutch` | `Clutch` ([fields](Engine.md#clutch)) | Clutch controlling how engine torque reaches the gearbox. Setup finds the vehicle's Clutch module when empty. Without an active clutch, the engine uses its simpler torque-transfer path. | `None / unassigned` |
| `directSpeedLimiterRangeKph` | `float` | Speed band below the direct-drive limit over which propulsion fades out. A larger band softens the approach to top speed but starts reducing torque earlier. | `15`; Speed field; stored in km/h, displayed in the selected speed unit |
| `engineRunning` | `bool` | Start with the engine running. Can also be changed during Play Mode. | `true` |
| `gearbox` | `Gearbox` ([fields](Engine.md#gearbox)) | Gearbox converting engine RPM and torque into wheel speed and torque. If missing or disabled, propulsion uses the simpler direct-drive path without selectable gear ratios. | `None / unassigned` |
| `idleRpm` | `float` | RPM the running engine settles toward with no load or throttle. It is also the lower end of normalized RPM used by the torque curve and related effects. | `900`; Minimum: 0 |
| `internalFriction` | `float` | Fraction of peak torque lost to internal friction at maximum RPM with a driver-controlled clutch. | `.12`; Range: 0 to 1 |
| `invertDriveDirection` | `bool` | Reverse longitudinal wheel torque and propulsion without changing throttle input, gears or ignition. | `false` |
| `launchBlendSpeed` | `float` | Forward speed in m/s by which assisted launch-RPM support has fully faded. Increase to keep launch rev support through a longer pull-away. | `8`; Speed field; stored in m/s, displayed in the selected speed unit |
| `launchRpm` | `float` | Assisted engine RPM target when pulling away. Higher values let the engine rev more during launch before coupling to road speed. | `3200`; Minimum: 0 |
| `maximumDriveAcceleration` | `float` | Propulsion acceleration budget in m/s²; zero disables the limit. Compensate Drive Resistance additionally admits opposing load within available torque/power. | `11`; Minimum: 0 |
| `compensateDriveResistance` | `bool` | Include opposing gravity and measured native drivetrain resistance in the acceleration-limit budget, without exceeding engine torque or power. | `true` |
| `maximumPowerKw` | `float` | Maximum output power in kW; zero disables the power cap. | `350`; Minimum: 0 |
| `maxRpm` | `float` | Upper engine RPM used to limit revs and evaluate the torque curve. Gear shifting and clutch calculations use this limit too; increasing it lets the engine rev higher. | `8000`; Minimum: 1000 |
| `peakTorque` | `float` | Peak engine torque in N·m before gearbox and final-drive multiplication. Raise for a stronger geared engine; power and acceleration caps can still limit what reaches the wheels. | `500`; Minimum: 0 |
| `response` | `float` | Maximum change of normalized drive demand per second in the smoothed engine path. Higher values make power respond faster; lower values make throttle build up gradually. Active service braking cuts demand immediately. | `3`; Minimum: 0 |
| `reverseSpeedRatio` | `float` | Reverse speed limit as a fraction of the configured forward top speed. For example, 0.3 allows reverse up to 30% of forward top speed. | `0.3`; Range: 0.1f to 1 |
| `revLimiterRange` | `float` | RPM band below the coupled engine's rev limit where propulsion fades out. A wider band softens the limiter but starts reducing torque sooner. | `400`; Minimum: 1 |
| `rotationalInertia` | `float` | Engine/flywheel rotational inertia in kg·m² for driver-controlled clutch physics. Higher values store more rotational energy and make revs harder to change. | `.3`; Minimum: .01f |
| `rpmResponse` | `float` | How quickly displayed/simulated RPM approaches its target outside a gear change. Higher values make revs rise and fall faster; lower values make the engine feel slower to respond. | `10`; Minimum: 0 |
| `shiftRpmResponse` | `float` | RPM response per second while shifting. Lower values give a slower RPM drop, independently of vehicle type. | `24`; Minimum: 0 |
| `speedLimiterRangeKph` | `float` | Road-speed band below top speed where propulsion is reduced. Increase for a smoother approach to the speed cap; decrease for stronger pull until nearer the limit. | `12`; Speed field; stored in km/h, displayed in the selected speed unit |
| `torqueCurve` | `AnimationCurve` | Torque multiplier over normalized engine RPM: horizontal 0 is idle and 1 is Max RPM. Shape it to choose where the engine pulls hardest; Peak Torque supplies the geared torque scale. | `new AnimationCurve(new Keyframe(0, .75, .5, .5), new Keyframe(.5, 1, .16666666, .16666666), new Keyframe(.8, .95, -.83333343, -.83333343), new Keyframe(1, .65, -1.5000001, -1.5000001))` |

## EngineModule

Configuration/implementation type for engine module within engine and drivetrain.

**Source:** `Runtime/Engine/Core/EngineModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [VehicleModule](Common.md#vehiclemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## FuelTank

Quantity change, empty transition and actual fuel increase

**Source:** `Runtime/Engine/FuelTank.cs`. Component / asset.

**Inherited settings:** [EngineModule](Engine.md#enginemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `capacityLitres` | `float` | Most fuel the tank can hold, in litres. Increase for longer range at the same consumption rates; existing fuel is kept within this capacity. | `60`; Minimum: .01f |
| `consumeFuel` | `bool` | Consume fuel while the engine is running. Disable for an unlimited driving range while retaining the gauge and refuelling API. | `true` |
| `fuelLitres` | `float` | Fuel currently in the tank, in litres. Consumption reduces it while the engine runs; an empty tank prevents fuel-dependent engine operation. The value cannot exceed tank capacity. | `60`; Minimum: 0 |
| `fullLoadLitresPerHour` | `float` | Litres consumed per hour at full engine load. Together with the idle rate it determines how much faster hard driving empties the tank. | `35`; Minimum: 0 |
| `idleLitresPerHour` | `float` | Litres consumed per hour at idle/no load. Increase to make idling use more fuel even when the vehicle is stationary. | `.8`; Minimum: 0 |
| `stopEngineWhenEmpty` | `bool` | Stop the engine and block ignition when the tank is empty. | `true` |

## Gearbox

Shared validated selection, ratios and shift state.

**Source:** `Runtime/Engine/Gearbox/Gearbox.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [EngineModule](Engine.md#enginemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `currentGear` | `int` | Gear selected at startup: -1 is reverse, 0 is neutral, and 1 or above selects a forward gear. The gearbox clamps this to the gears it actually has. | `1` |
| `directionChangeSpeed` | `float` | Maximum vehicle speed in m/s at which a forward/reverse selection is accepted. Lower it to require the vehicle to be closer to a stop before changing direction. | `0.6`; Speed field; stored in m/s, displayed in the selected speed unit |
| `efficiency` | `float` | Fraction of transmitted torque retained after drivetrain losses. At 0.9, 90% reaches the output before other limits; lower values reduce wheel torque. | `0.9`; Range: 0 to 1 |
| `finalDrive` | `float` | Reduction multiplying every forward and reverse gear ratio. A larger value gives more wheel torque and higher engine RPM at the same road speed, reducing speed per engine revolution. | `3.4`; Minimum: 0.1f |
| `forwardRatios` | `float[]` | Forward gear ratios, first gear at index 0. Used directly with no custom speed ranges. | `{4.7949967, 2.833407, 2.010805, 1.5203648, 1.222254, 1.0054024}` |
| `gearSpeedLimitsKph` | `float[]` | Optional road speed at engine redline per forward gear, in km/h. Empty uses the authored Forward Ratios directly. Non-empty values derive ratios from wheel radius and engine RPM. | `Empty list`; Speed field; stored in km/h, displayed in the selected speed unit |
| `reverseRatio` | `float` | Positive reverse gear reduction before final drive. | `8.904994`; Minimum: 0.1f |
| `reverseSpeedLimitKph` | `float` | Optional reverse road speed at redline; zero preserves the authored Reverse Ratio. | `0`; Speed field; stored in km/h, displayed in the selected speed unit |
| `shiftDuration` | `float` | Seconds spent changing gears, during which drive transfer is interrupted/blended. Increase for a slower shift with a more noticeable power gap. | `.14`; Minimum: 0 |

## ManualGearbox

Provides the manually selected gearbox implementation.

**Source:** `Runtime/Engine/Gearbox/ManualGearbox.cs`. Component / asset.

**Inherited settings:** [Gearbox](Engine.md#gearbox). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## Nitro

**Source:** `Runtime/Engine/Boost/Nitro.cs`. Optional component; excluded from Full setup.

**Inherited settings:** [EngineModule](Engine.md#enginemodule).

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `suspensionKick` | `BoostSuspensionSettings` | Supported spring kick; see [configuration](../DrivingActions.md#suspension-kick-and-departure-wheelspin). | Enabled; front 0.035 m, rear 0.02 m; rise 0.15 s, return 0.3 s; maximum tilt 20 degrees |
| `launchWheelspin` | `bool` | Extra driven-tire grip pulse on departure. | `true` |
| `launchSpeed` | `float` | Departure trigger speed in m/s. | `1`, minimum 0 |
| `launchGripDuration` | `float` | Smooth launch grip recovery in seconds. | `.65f`, minimum .01 |
| `launchForwardGrip` | `float` | Longitudinal launch grip fraction. | `.35f`, range .05–1 |
| `launchSidewaysGrip` | `float` | Lateral launch grip fraction. | `.65f`, range .05–1 |
| `accelerationMultiplier` | `float` | Multiplier for the finite wheel-drive acceleration cap. Default 3. | `3f` |
| `additionalAcceleration` | `float` | Additional grounded chassis acceleration in m/s², independent of tire torque limits. Default 10; zero uses engine torque only. Stops immediately on release, braking or loss of eligibility; fades near boosted top speed. | `10` |
| `additionalMaxRpmPercent` | `float` | Extra engine redline as a percentage during boost. Default 25 raises 8000 RPM to 10000; zero preserves the normal limit. Scales with final partial boost strength and stays available through an internal shift. | `25`, minimum 0 |
| `additionalPowerKw` | `float` | Extra engine power allowance in kW. Default 350; an uncapped engine remains uncapped. | `350` |
| `allowPitchAboveMaxRpm` | `bool` | Default true. Controls RPM-driven Engine Audio pitch above its ordinary maximum when actual RPM exceeds this engine base redline. Applies per Nitro component to sounds following its engine; constant/motion/fixed-pitch sounds remain unchanged. Unity pitch ceiling remains 3. | true |
| `allowReverse` | `bool` | Permit boost in reverse. Default true. | `true` |
| `forceForwardDirection` | `bool` | Request forward drive during boost; disable to retain the selected direction. | `true` |
| `amount` | `float` | Starting/current charge, clamped to capacity. Use SetAmount/AddNitro/Refill at runtime. | `100` |
| `automaticRefill` | `bool` | Refill automatically after release and refillDelay. Default false; demo Car enables it. | `false` |
| `buildUpTime` | `float` | Seconds for boost power to build from zero to full. Default 0.2; zero gives immediate full power. Release/braking removes assistance immediately. Consumption follows the resolved power fraction. Internal shifts preserve the existing build-up level. | `.2f`, minimum 0 |
| `capacity` | `float` | Maximum charge in arbitrary consistent units. Default 100; minimum 0.01. | `100` |
| `consumesNitro` | `bool` | Consume supply while boosting. Default true; false permits unlimited boost even with zero charge. | `true` |
| `cooldown` | `float` | Seconds before a new activation after boost stops. Default 0.25. | `.25f` |
| `engine` | `Engine` | Registered engine receiving the boost; leave unassigned to resolve it from the owning vehicle. | `None / unassigned` |
| `fullTankDuration` | `float` | Seconds of full boost supplied by a full tank. Default 15; consumption is capacity / duration per second. | `15` |
| `lockAutomaticGearChanges` | `bool` | Default true. Suppresses automatic gear selection while boost is actually active, including an internal shift interruption. Explicit manual gear requests still use normal safety guards. Disabling this restores the usual automatic shift behavior. | true |
| `minimumActivationAmount` | `float` | Minimum charge needed to begin a new activation. Default 1; an active use may consume its remaining partial charge. | `1` |
| `minimumThrottle` | `float` | Minimum requested throttle magnitude required for boost. Default 0.1; nonzero propulsion demand is always required. | `.1f` |
| `refillDelay` | `float` | Seconds since last boost before automatic refill; a held request also blocks refill. Default 1. | `1` |
| `refillPerSecond` | `float` | Automatic refill rate in charge units per second. Default 25. | `25` |
| `requested` | `bool` | Explicit held API/Inspector request combined with Command.Nitro. | `false` |
| `requireGroundContact` | `bool` | Require at least one supported driven tire. Default false. | `false` |
| `shiftSpeedMultiplier` | `float` | Gear-change and automatic gear dwell speed multiplier during boost. Default 4; preserves authored gearbox settings. | `4` |
| `topSpeedMultiplier` | `float` | Multiplier for the engine road-speed envelope. Default 1.35. | `1.35f` |
| `torqueMultiplier` | `float` | Engine combustion/direct-drive torque multiplier. Default 3. | `3f` |

## TractionControl

Limits propulsion according to contact capacity and slip.

**Source:** `Runtime/Engine/Drivetrain/TractionControl.cs`. Component / asset.

**Inherited settings:** [EngineModule](Engine.md#enginemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `corneringFreedom` | `float` | Allow power-dependent wheelspin during tight powered turns, while retaining straight-line launch control. | `.65`; Range: 0 to 1 |
| `launchReferenceSpeed` | `float` | Low-speed reference in m/s used to stabilize slip/traction calculations during launch. | `3`; Speed field; stored in m/s, displayed in the selected speed unit |
| `minimumTorqueScale` | `float` | Lowest fraction of requested propulsion that traction control can leave during wheelspin. Lower values allow a deeper torque cut; higher values keep more drive even while slipping. | `.08`; Range: 0 to 1 |
| `recoveryRate` | `float` | Rate at which allowed drive torque recovers after excess slip subsides. | `1.8`; Minimum: 0 |
| `reductionRate` | `float` | Rate at which allowed drive torque decreases when wheel slip exceeds the target. | `12`; Minimum: 0 |
| `reserveGripForCornering` | `bool` | Reduces propulsion when the tires need grip for turning. This helps avoid sliding wide under power, at the cost of acceleration through a corner. | `false` |
| `targetSlip` | `float` | Desired longitudinal slip magnitude while applying propulsion torque. | `.22`; Minimum: .01f |
| `tractionReserve` | `float` | Fraction of estimated traction kept available when limiting drive torque. | `.9`; Range: .1f to 1 |

## Transmission

Selects Direct, Manual or Automatic transmission operation.

**Source:** `Runtime/Engine/Gearbox/Transmission.cs`. Component / asset.

**Inherited settings:** [EngineModule](Engine.md#enginemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `automatic` | `AutomaticGearbox` ([fields](Engine.md#automaticgearbox)) | Gearbox used in Automatic mode. It selects gears from RPM and driving conditions; setup finds the vehicle's AutomaticGearbox when empty. | `None / unassigned` |
| `engine` | `Engine` ([fields](Engine.md#engine)) | Engine whose gearbox connection changes when selecting Automatic, Manual or Direct. Setup searches the vehicle's modules if this is empty. | `None / unassigned` |
| `manual` | `ManualGearbox` ([fields](Engine.md#manualgearbox)) | Gearbox used in Manual mode. It responds to the driver's gear commands; setup finds the vehicle's ManualGearbox when empty. | `None / unassigned` |
| `mode` | `TransmissionMode` | Automatic connects the automatic gearbox; Manual connects the manual gearbox; Direct disconnects the gearbox and uses direct propulsion. Switching mode applies the matching connection to Engine. Options: `Automatic`, `Manual`, `Direct`. | `TransmissionMode.Automatic` |
