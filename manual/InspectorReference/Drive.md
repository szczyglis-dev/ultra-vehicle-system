# Drive profiles, steering and suspension

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [AirplaneGroundContact](#airplanegroundcontact) | 0 |
| [AirplaneProfile](#airplaneprofile) | 86 |
| [AirplaneWaterLandingSettings](#airplanewaterlandingsettings) | 8 |
| [AirProfile](#airprofile) | 0 |
| [AntiLockBrakes](#antilockbrakes) | 7 |
| [AntiRoll](#antiroll) | 2 |
| [AntiRoll.Axle](#antirollaxle) | 2 |
| [BoatProfile](#boatprofile) | 53 |
| [BoostSuspensionSettings](#boostsuspensionsettings) | 6 |
| [Brakes](#brakes) | 8 |
| [Burnout](#burnout) | 23 |
| [BurnoutSuspensionSettings](#burnoutsuspensionsettings) | 1 |
| [ContactEnvelope](#contactenvelope) | 14 |
| [ControlArm](#controlarm) | 23 |
| [Drive](#drive) | 0 |
| [DriveModule](#drivemodule) | 0 |
| [DriveProfile](#driveprofile) | 7 |
| [DriveProfileSlot](#driveprofileslot) | 2 |
| [DrivingAssists](#drivingassists) | 15 |
| [FreeProfile](#freeprofile) | 3 |
| [HalfShaft](#halfshaft) | 13 |
| [HelicopterProfile](#helicopterprofile) | 13 |
| [HoverDriveTransition](#hoverdrivetransition) | 2 |
| [HoverProfile](#hoverprofile) | 24 |
| [MotorcycleBalance](#motorcyclebalance) | 34 |
| [MotorcycleGroundAssist](#motorcyclegroundassist) | 32 |
| [MotorcycleProfile](#motorcycleprofile) | 6 |
| [MotorcycleWheelieControl](#motorcyclewheeliecontrol) | 17 |
| [ParkingHold](#parkinghold) | 3 |
| [ProfileSwitcher](#profileswitcher) | 6 |
| [ProfileTransition](#profiletransition) | 5 |
| [ShockAbsorber](#shockabsorber) | 20 |
| [SpaceshipProfile](#spaceshipprofile) | 14 |
| [Steering](#steering) | 14 |
| [SteeringTieRod](#steeringtierod) | 19 |
| [SubmarineProfile](#submarineprofile) | 13 |
| [Suspension](#suspension) | 53 |
| [SuspensionAxle](#suspensionaxle) | 8 |
| [SuspensionHub](#suspensionhub) | 8 |
| [SuspensionRotationLimits](#suspensionrotationlimits) | 4 |
| [TrackedProfile](#trackedprofile) | 12 |
| [Tracks](#tracks) | 2 |
| [WheeledProfile](#wheeledprofile) | 0 |

## AirplaneGroundContact

`Tracks` ground support and ground/air authority blending.

**Source:** `Runtime/Drive/Air/AirplaneGroundContact.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## AirplaneProfile

Owns the configurable fixed-wing flight pipeline, including assisted attitude, body rates and relative-airflow aerodynamics.

**Source:** `Runtime/Drive/Profiles/AirplaneProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [AirProfile](Drive.md#airprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `aerodynamics` | `AircraftAerodynamics` | Simplified lift/alignment or relative-airflow forces with pressure and induced drag. Independent of Simple Steering. Options: `Simplified`, `RelativeAirflow`. | `AircraftAerodynamics.RelativeAirflow` |
| `airspeedControlAuthorityEnabled` | `bool` | Scale control torque with airspeed/attached flow. Disable to retain full commanded control authority at low speed. Enabled by default. | `true` |
| `allowGroundReverse` | `bool` | Allow powered reverse only on supported landing gear with positive reverse speed and acceleration limits. Enabled by default in the Jet-based preset. | `true` |
| `angularDampingEnabled` | `bool` | Apply angular velocity damping inside profile attitude/rate control; disabling retains commanded control torque. Enabled by default. | `true` |
| `attitudeControlEnabled` | `bool` | Master switch for profile pitch/roll/yaw control torque; leaves aerodynamic forces active. Enabled by default. | `true` |
| `attitudeDamping` | `float` | Damping of angular motion inside aircraft attitude control. Higher values reduce overshoot and rotational oscillation. | `6`; Minimum: 0 |
| `attitudeSpringEnabled` | `bool` | Assisted attitude mode: angle-to-target restoring torque, including pitch/roll input response. Enabled by default. | `true` |
| `attitudeStrength` | `float` | Strength of restoring angular acceleration toward the assisted target attitude. Higher values correct pitch and bank errors more quickly. | `14`; Minimum: 0 |
| `bankCompensationEnabled` | `bool` | Simplified aerodynamics: increase lift to compensate for bank. Disabled by default. | `false` |
| `coordinatedTurn` | `float` | Bank-derived heading-turn assistance in the simplified model. Higher values turn the flight path more strongly for the same bank. | `1.8`; Minimum: 0 |
| `coordinatedTurnAssist` | `float` | Fraction of automatic bank-to-heading coordination applied to Body Rates control. Zero leaves turn coordination to the pilot. | `0.8`; Range: 0 to 1 |
| `coordinatedTurnEnabled` | `bool` | Add bank-derived automatic turn demand. Body-rate mode also requires Rate Coordinated Turn Enabled. Enabled by default. | `true` |
| `dragEnabled` | `bool` | Apply profile air resistance, including parasite, induced and pressure drag in relative-airflow mode. Enabled by default. | `true` |
| `engineIdleRpm` | `float` | Aircraft engine idle speed in revolutions per minute, used for propulsion and RPM presentation. | `1800`; Minimum: 0 |
| `engineMaximumRpm` | `float` | Aircraft engine speed at full spool in revolutions per minute, used for propulsion and RPM presentation. | `12000`; Minimum: 1 |
| `enginePowerKw` | `float` | Configured shaft power in kilowatts used by the aircraft propulsion calculation. Propeller efficiency and available engine spool determine delivered thrust. | `12000`; Minimum: 1 |
| `enginePowerLimitEnabled` | `bool` | Limit thrust acceleration by engine power, speed and mass. Disabling retains throttle and spool response. Enabled by default. | `true` |
| `flightAlignmentEnabled` | `bool` | Apply flight-path alignment toward the airframe. In relative-airflow mode gates pitch/yaw crossflow correction, independently of lift trim. Enabled by default. | `true` |
| `flightPathResponse` | `float` | Response of simplified flight-path alignment. Higher values make velocity follow the aircraft heading more quickly. | `3`; Minimum: 0 |
| `flightTransitionTime` | `float` | Seconds used to blend from supported ground motion into flight forces after takeoff. | `0.35`; Minimum: .01f |
| `gLimiterEnabled` | `bool` | Apply G-derived pitch-rate and aerodynamic normal-force limits. Other configured control-acceleration limits remain active. Enabled by default. | `true` |
| `groundAcceleration` | `float` | Maximum forward ground-roll acceleration in metres per second squared before airborne propulsion takes over. | `5`; Minimum: 0 |
| `groundFriction` | `float` | Hull-contact friction for wheel-free aircraft only. Gear tires use the shared Friction module. | `0.02`; Range: 0 to 1 |
| `groundHandlingAssistance` | `float` | Shared steering yaw and lateral grip assistance, only while tires touch the ground. | `0.3`; Range: 0 to 1 |
| `groundLateralResponse` | `float` | Lateral ground-roll damping response. Higher values reduce sideways sliding while the landing gear has support. | `5`; Minimum: 0 |
| `groundReverseAcceleration` | `float` | Maximum powered reverse acceleration during ground maneuvering, in metres per second squared. | `2`; Minimum: 0 |
| `groundReverseSpeed` | `float` | Ground-only reverse speed in m/s. Zero disables reverse thrust. | `3`; Speed field; stored in m/s, displayed in the selected speed unit |
| `groundRotationAuthority` | `float` | Fraction of aircraft attitude control available while supported by landing gear. Zero relies on ground steering only. | `0.7`; Range: 0 to 1 |
| `groundRotationEnabled` | `bool` | Allow pitch control for rotation while still grounded. Airborne pitch control remains independent. Enabled by default. | `true` |
| `groundSteeringAngle` | `float` | Maximum assisted landing-gear steering angle in degrees during ground maneuvering. | `30`; Range: 1 to 60 |
| `groundSteeringRate` | `float` | Maximum rate at which aircraft ground steering changes angle, in degrees per second. | `60`; Minimum: 1 |
| `groundYawResponse` | `float` | Response of the ground-steering yaw assist. Higher values reach the requested turn rate more quickly. | `4`; Minimum: 0 |
| `inducedDrag` | `float` | Induced drag acceleration at one G; grows with aerodynamic load squared. | `0.12`; Minimum: 0 |
| `inducedDragEnabled` | `bool` | Allow aerodynamic-load induced drag when the inherited Drag Enabled master is on. Enabled by default. | `true` |
| `landingTransitionTime` | `float` | Seconds used to blend from airborne forces back into supported ground motion after touchdown. | `0.08`; Minimum: .01f |
| `liftEnabled` | `bool` | Apply aerodynamic lift. Disabling does not remove gravity, drag or attitude control. Enabled by default. | `true` |
| `liftMultiplier` | `float` | Scale of aerodynamic lift in the simplified model. Raising this supports the aircraft more strongly at the same airspeed. | `1.18`; Range: 1 to 2 |
| `liftSpeed` | `float` | Minimum forward airspeed for ground rotation/takeoff, in m/s. | `40`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumAlignmentAcceleration` | `float` | Maximum velocity-alignment acceleration in metres per second squared, limiting how abruptly the aircraft redirects its flight path. | `55`; Minimum: 0 |
| `maximumBank` | `float` | Maximum assisted target bank angle in degrees. Body Rates mode can still perform unrestricted rolls. | `45`; Range: 5 to 85 |
| `maximumControlAcceleration` | `float` | Maximum angular acceleration produced by aircraft attitude/rate assistance, in radians per second squared. | `8`; Minimum: .1f |
| `maximumG` | `float` | Maximum assisted aerodynamic load in multiples of gravity when the G limiter is enabled. Limits pitch-rate demand and normal force. | `4.5`; Range: 1.1f to 9 |
| `maximumGroundLateralAcceleration` | `float` | Maximum assisted lateral acceleration during ground turns, in metres per second squared. | `6`; Minimum: .1f |
| `maximumLiftAcceleration` | `float` | Upper bound on aircraft lift acceleration in metres per second squared. Limits lift forces without removing native gravity. | `70`; Minimum: 1 |
| `maximumPitch` | `float` | Pitch attitude limit in the assisted profile. Body-rate mode uses angular rates instead. | `30`; Range: 5 to 85 |
| `maximumSpeed` | `float` | Forward airspeed limit in m/s. Thrust fades out near this speed. | `200`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumThrustNewtons` | `float` | Full-spool static thrust in newtons. A positive value replaces the ground/flight acceleration settings with a mass-independent engine force. Zero retains acceleration-based propulsion. Throttle, spool, speed envelope and optional power limit still apply. | `90000`; Minimum: 0 |
| `maximumTurnRate` | `float` | Upper bound on the assisted heading turn rate in degrees per second. | `70`; Minimum: 1 |
| `minimumAirControlAuthority` | `float` | Optional low-speed / thrust-vectoring control assistance. Zero requires airflow; higher values allow fighter-style recovery near a stall. | `0.05`; Range: 0 to 1 |
| `minimumGroundTurnRadius` | `float` | Minimum requested ground turn radius in metres. Prevents aircraft steering assistance from demanding an excessively tight turn. | `12`; Minimum: 0 |
| `parasiteDrag` | `float` | Forward parasite drag acceleration / speed squared, in 1/metres. | `0.00022`; Minimum: 0 |
| `parasiteDragEnabled` | `bool` | Allow forward-speed parasite drag when the inherited Drag Enabled master is on. Enabled by default. | `true` |
| `parkingBrakeTorque` | `float` | Native landing-gear wheel parking-brake torque in newton metres. | `45000`; Minimum: 0 |
| `pitchControlEnabled` | `bool` | Allow profile control torque around the local pitch axis. Does not suppress aerodynamic torque from other systems. Enabled by default. | `true` |
| `pitchPathResponse` | `float` | Pitch flight-path tracking response in Relative Airflow mode. Higher values align pitch control with the requested flight path more quickly. | `5`; Minimum: .1f |
| `pitchRate` | `float` | Maximum commanded pitch rate in degrees per second in Body Rates mode. | `30`; Minimum: 1 |
| `pressureDragEnabled` | `bool` | Allow crossflow pressure drag when the inherited Drag Enabled master is on. Enabled by default. | `true` |
| `progressiveThrustEnvelope` | `bool` | Use a progressive fourth-power thrust envelope instead of the linear speed-limit fade. | `true` |
| `propulsionEnabled` | `bool` | Apply engine/propeller thrust, including supported ground reverse. Engine and propeller presentation remain independent. Enabled by default. | `true` |
| `rateCoordinatedTurnEnabled` | `bool` | Coordinate body-rate turns. Relative Airflow aligns the nose with the flight path; Simplified uses bank-derived heading assistance. | `true` |
| `rateResponse` | `float` | Angular-rate tracking response in Body Rates mode. Higher values reach the requested pitch, roll and yaw rates faster. | `6`; Minimum: .1f |
| `referenceAirspeed` | `float` | Reference airspeed in metres per second for aerodynamic control authority. Authority decreases below this speed. | `100`; Speed field; stored in m/s, displayed in the selected speed unit |
| `rollControlEnabled` | `bool` | Allow profile control torque around the local roll axis. Enabled by default. | `true` |
| `rollRate` | `float` | Maximum commanded roll rate in degrees per second in Body Rates mode. | `75`; Minimum: 1 |
| `rudderEnabled` | `bool` | Allow commanded yaw/rudder input in profile attitude control. Enabled by default. | `true` |
| `rudderRate` | `float` | Maximum requested rudder-driven heading rate in degrees per second in assisted control. | `35`; Minimum: 0 |
| `serviceBrakeTorque` | `float` | Native landing-gear wheel service-brake torque in newton metres while aircraft braking is requested. | `25000`; Minimum: 0 |
| `sideForceEnabled` | `bool` | Allow sideways aerodynamic normal force; inherited Lift Enabled controls the lift-axis force. Enabled by default. | `true` |
| `sidePressureDrag` | `float` | Quadratic aerodynamic resistance to sideways airflow in Relative Airflow mode. Higher values dissipate sideslip more strongly. | `0.008`; Minimum: 0 |
| `simpleSteering` | `bool` | Assisted attitude holds pitch/bank targets; body rates allow unrestricted rolls and inverted flight. | `false` |
| `speedLimiterEnabled` | `bool` | Fade thrust near configured forward/reverse speed limits; does not directly clamp Rigidbody velocity. Enabled by default. | `true` |
| `stallAngle` | `float` | Angle of attack in degrees at which attached-flow lift/control authority fades in Relative Airflow mode. | `35`; Range: 10 to 60 |
| `stallEnabled` | `bool` | Reduce lift/support near low airspeed; Relative-airflow mode also reduces attached flow at excessive angle of attack. Disable for full aerodynamic support. Enabled by default. | `true` |
| `stallSpeedRatio` | `float` | Fraction of the configured speed envelope used as the simplified model stall threshold. | `0.65`; Range: .1f to .95f |
| `suspensionDamper` | `float` | Landing-gear suspension damping in newton seconds per metre for the profile-provided wheel setup. | `28050`; Minimum: 0 |
| `suspensionSpring` | `float` | Landing-gear suspension spring stiffness in newtons per metre for the profile-provided wheel setup. | `375000`; Minimum: 1 |
| `suspensionTravel` | `float` | Landing-gear suspension travel in metres for the profile-provided native wheel setup. | `0.28`; Minimum: .05f |
| `takeoffContactGrace` | `float` | Seconds without tire contact before entering flight. Touchdown is detected on the first tire contact. | `0.12`; Minimum: 0 |
| `tireGrip` | `float` | Grip multiplier used for aircraft landing-gear tire friction. | `1.6`; Minimum: .1f |
| `useLandingGear` | `bool` | Keep native tires active in flight to detect touchdown without rebuilding wheel actors. Disable only for a wheel-free aircraft. | `true` |
| `waterLanding` | `AirplaneWaterLandingSettings` ([fields](Drive.md#airplanewaterlandingsettings)) | Optional floats, boat handling and automatic flight/water control handover. | `new AirplaneWaterLandingSettings()` |
| `wingPressureDrag` | `float` | Additional quadratic pressure drag for airflow across the wings / across the fuselage. | `0.012`; Minimum: 0 |
| `yawControlEnabled` | `bool` | Allow profile control torque around the local yaw axis. Enabled by default. | `true` |
| `yawLimiterEnabled` | `bool` | Limit commanded yaw rate according to airspeed and gravity. | `true` |
| `yawPathResponse` | `float` | Yaw flight-path tracking response in Relative Airflow mode. Higher values reduce the heading error more quickly. | `4`; Minimum: .1f |
| `yawRate` | `float` | Maximum commanded yaw rate in degrees per second in Body Rates mode. | `20`; Minimum: 1 |

## AirplaneWaterLandingSettings

Optional water support and a separate boat force controller. Transient state belongs to Drive, not the serialized settings.

**Source:** `Runtime/Drive/Water/AirplaneWaterLandingSettings.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `boat` | `BoatProfile` ([fields](Drive.md#boatprofile)) | Independent boat handling for flotation, immersion depth, resistance, rocking, waves and water taxi. It never overwrites aircraft mass, engine or landing-gear configuration. | `Default collection/object defined in source` |
| `boatControls` | `bool` | Use Boat Profile thrust, rudder and hull handling at low water speed. Off retains aircraft control with passive flotation and water resistance. | `true` |
| `enabled` | `bool` | Enable flotation, water taxi and takeoff from sampled water. Does not affect ordinary runway aircraft when off. | `false` |
| `floatOffset` | `Vector3` | Buoyancy reference offset in the aircraft's local axes from its centre of mass. Place at the floats' intended waterline; a negative Y keeps the fuselage above water. | `Vector3.zero` |
| `landingSpeedRatio` | `float` | Enter water controls below this fraction of Lift Speed after touching water. Separate from takeoff speed to prevent repeated switching. | `.8`; Range: .1f to 1 |
| `minimumControlHold` | `float` | Minimum time between automatic control changes. Losing water contact or disabling flotation returns aircraft control immediately. | `.25`; Minimum: 0 |
| `takeoffPitch` | `float` | Minimum nose-up pitch request required for the water takeoff handover. Negative Pitch requests nose-up. | `.05`; Range: 0 to 1 |
| `takeoffSpeedRatio` | `float` | Return to aircraft control at this fraction of Lift Speed while requesting nose-up pitch. Continue accelerating in boat control until then. | `1`; Minimum: 1 |

## AirProfile

Configuration/implementation type for air profile within movement strategies and transitions.

**Source:** `Runtime/Drive/Profiles/AirProfile.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [FreeProfile](Drive.md#freeprofile). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## AntiLockBrakes

Optional per-wheel service-brake pressure modulation after Brakes. Detects impending lock-up from contact-relative tire speed; parking brakes, low-speed holding and airborne wheels remain independent.

**Source:** `Runtime/Drive/Brakes/AntiLockBrakes.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `minimumPressure` | `float` | Lowest retained fraction of requested service-brake torque. Zero allows complete pressure release. | `0`; Range: 0 to 1 |
| `minimumReleaseDuration` | `float` | Minimum duration of a pressure-release pulse, giving the tire time to recover rotation. | `.04`; Minimum: 0 |
| `minimumSpeedKph` | `float` | Minimum contact speed in km/h for pressure modulation. Below this speed normal brakes can stop and hold the vehicle. | `5`; Speed field; stored in km/h, displayed in the selected speed unit |
| `recoverySlip` | `float` | Braking-slip ratio below which pressure builds again. Kept below Target Slip to avoid rapid switching. | `.1`; Range: 0 to 1 |
| `recoveryTime` | `float` | Seconds to rebuild full pressure once the tire rolls again. | `.12`; Minimum: .001f |
| `releaseTime` | `float` | Seconds to release full service-brake pressure after detecting a locking tire. | `.035`; Minimum: .001f |
| `targetSlip` | `float` | Longitudinal braking-slip ratio that starts pressure release. A locked tire has a ratio near one. | `.2`; Range: .01f to 1 |

## AntiRoll

Adds cross-wheel roll support for the configured wheel relationships.

**Source:** `Runtime/Drive/Suspension/AntiRoll.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `axles` | `Axle[]` ([fields](Drive.md#antirollaxle)) | Left/right wheel pairs linked by anti-roll support. Add one entry per axle so compression on one side can produce a balancing force on the other. | `None / unassigned` |
| `stiffness` | `float` | Anti-roll force scale applied from left/right suspension compression difference; increase it to resist body roll. | `4500`; Minimum: 0 |

## AntiRoll.Axle

Value data for axle; its fields are listed below.

**Source:** `Runtime/Drive/Suspension/AntiRoll.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `left` | `Wheel` ([fields](Physics.md#wheel)) | Left Wheel on this axle. Its suspension compression is compared with Right to calculate the force opposing body roll. | `None / unassigned` |
| `right` | `Wheel` ([fields](Physics.md#wheel)) | Right Wheel on this axle. Assign its matching left wheel in Left; both wheels must be operational and grounded for this axle's anti-roll force. | `None / unassigned` |

## BoatProfile

Owns authored boat movement parameters and the profile behavior.

**Source:** `Runtime/Drive/Profiles/BoatProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [FreeProfile](Drive.md#freeprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `accelerationTilt` | `Vector2` | Pitch/roll degrees per m/s² of measured acceleration. | `new Vector2(0.25, 1.1)` |
| `ambientWaveDegrees` | `float` | Continuous rhythmic pitch/roll amplitude, degrees; active while idle and moving. Zero disables background sway. | `0.6`; Range: 0 to 2 |
| `ambientWaveInterval` | `Vector2` | Seconds between subtle random changes in wave amplitude and pitch phase; the side-to-side rhythm remains continuous. | `new Vector2(2.5, 5)` |
| `ambientWavePeriod` | `float` | Seconds for a complete side-to-side water rocking cycle. | `5.5`; Minimum: 2 |
| `ambientWavesEnabled` | `bool` | Allow continuous background pitch/roll sway. Does not disable occasional wave impulses. Enabled by default. | `true` |
| `brakingThrustEnabled` | `bool` | Allow the Brake command to request opposing propeller thrust while powered. Enabled by default. | `true` |
| `buoyancyDepth` | `float` | Vertical distance in metres over which fallback hull immersion builds from dry to supported. Changes the waterline response and buoyancy transition. | `0.85`; Minimum: .1f |
| `buoyancyEnabled` | `bool` | Apply gravity-derived upward buoyancy. Vertical damping remains a separate force contribution. Enabled by default. | `true` |
| `forwardDragScale` | `float` | Scales the inherited Drag setting along the hull; lower values retain momentum longer. | `0.3`; Minimum: 0 |
| `forwardResistanceEnabled` | `bool` | Apply linear and speed-squared resistance along the hull. Enabled by default. | `true` |
| `idleWaveDegrees` | `float` | Occasional wave impulse strength. Zero disables these impulses independently of background sway. | `1.2`; Range: 0 to 3 |
| `idleWaveInterval` | `Vector2` | Random interval between occasional stronger wave impulses, seconds; also active while moving. | `new Vector2(8, 16)` |
| `lateralResistance` | `float` | Sideways resistance: lower values preserve sideways drift longer. | `1.8`; Minimum: 0 |
| `lateralResistanceEnabled` | `bool` | Apply sideways hull resistance and its forward-speed contribution. Enabled by default. | `true` |
| `loadedRockingDampingRatio` | `float` | Fraction of normal pitch/roll damping retained at full maneuver excitation. Lower values allow more rocking under load. | `0.85`; Range: .1f to 1 |
| `maneuverRockingEnabled` | `bool` | Excite pitch/roll from measured hull acceleration; does not disable ambient waves or powered bow lift. Enabled by default. | `true` |
| `maximumHullTilt` | `float` | Maximum assisted hull tilt from world up, degrees. Soft restoring torque opposes excess tilt without overriding collision motion. | `35`; Range: 10 to 80 |
| `maximumManeuverTilt` | `float` | Maximum pitch/roll target offset in degrees caused by measured hull acceleration. | `6`; Range: 0 to 20 |
| `maximumYawRate` | `float` | Maximum assisted underway yaw rate in radians per second. | `0.75`; Minimum: .1f |
| `pitchMotionEnabled` | `bool` | Allow all profile-generated hull pitch torque, including wave impulses. Does not freeze native Rigidbody rotation. Enabled by default. | `true` |
| `poweredPitchDegrees` | `float` | Sustained bow/stern lift at full propeller load, degrees; builds gradually with squared throttle demand and forward motion. | `5.5`; Range: 0 to 8 |
| `poweredPitchEnabled` | `bool` | Allow sustained throttle-induced bow/stern pitch. Disabling clears stored powered-pitch response. Enabled by default. | `true` |
| `poweredPitchReleaseTime` | `float` | Seconds for sustained lift to settle after releasing/reversing throttle. | `0.7`; Minimum: .1f |
| `poweredPitchRiseTime` | `float` | Seconds for sustained throttle lift to approach its target; longer values make the bow rise more gradually. | `1.2`; Minimum: .1f |
| `powerPitchBoost` | `float` | Additional sustained propeller-induced pitch response while maneuver rocking energy is elevated. | `0.2`; Minimum: 0 |
| `propulsionEnabled` | `bool` | Allow throttle-driven hull thrust. Braking thrust is independent; engine ownership is unchanged. Enabled by default. | `true` |
| `rockingDamping` | `float` | Passive damping opposing hull pitch and roll angular velocity. Higher values reduce oscillation after maneuvers and waves. | `0.65`; Minimum: 0 |
| `rockingDampingEnabled` | `bool` | Apply passive pitch/roll damping, including propeller/low-speed pitch damping. Enabled by default. | `true` |
| `rockingMemorySeconds` | `float` | Seconds over which measured maneuver excitation decays. Longer values let rocking settle more gradually after throttle or steering changes. | `2.5`; Minimum: .1f |
| `rockingSpring` | `float` | Restoring strength returning the hull pitch and roll toward their current equilibrium attitude in water. | `3.5`; Minimum: .1f |
| `rockingStrength` | `float` | Strength of maneuver, continuous water sway and wave rocking. Zero disables excitation while retaining upright stability and momentum. | `1`; Range: 0 to 2 |
| `rollMotionEnabled` | `bool` | Allow all profile-generated hull roll torque, including wave impulses. Does not freeze native Rigidbody rotation. Enabled by default. | `true` |
| `rudderEnabled` | `bool` | Apply steering-generated yaw torque while powered, independently of forward thrust. Enabled by default. | `true` |
| `speedLateralResistance` | `float` | Extra sideways grip per m/s of forward speed; keeps the hull tracking its heading under power. | `0.09`; Minimum: 0 |
| `speedResistance` | `float` | Quadratic forward hull resistance coefficient. Higher values remove more speed as water-relative forward velocity increases. | `0.006`; Minimum: 0 |
| `stationaryTurnAcceleration` | `float` | Additional yaw angular acceleration available for powered low-speed maneuvering, in radians per second squared. | `0.12`; Minimum: 0 |
| `stationaryTurningEnabled` | `bool` | Allow the additional stationary turning authority; underway rudder authority remains speed-dependent. Enabled by default. | `true` |
| `stationaryYawRate` | `float` | Maximum requested yaw rate in radians per second for powered low-speed turning assistance. | `0.18`; Minimum: .01f |
| `steeringReturnTime` | `float` | Seconds for digital rudder demand to return to neutral after steering is released. | `0.22`; Minimum: .01f |
| `steeringRiseTime` | `float` | Seconds for digital rudder demand to build toward a new steering request. Analog steering remains direct. | `0.35`; Minimum: .01f |
| `steeringSmoothingEnabled` | `bool` | Smooth digital steering demand. Disable for immediate steering; analog input is already direct. Enabled by default. | `true` |
| `steeringYawResponse` | `float` | Rudder response to desired turn rate. Countersteering first arrests the current turn instead of building unchecked opposing torque. | `3`; Minimum: .1f |
| `tiltLimitEnabled` | `bool` | Limit total hull tilt in water and reduce thrust near the limit. Requires upright stabilization and both pitch/roll motion switches. | `true` |
| `uprightStabilizationEnabled` | `bool` | Apply the hull spring returning pitch/roll toward upright, independently of rocking excitation. Enabled by default. | `true` |
| `verticalDamping` | `float` | Water-relative vertical velocity damping in the upward flotation force. Higher values reduce bobbing; independent of the buoyancy switch. | `1.8`; Minimum: 0 |
| `verticalDampingEnabled` | `bool` | Apply the vertical water-relative damping term inside the nonnegative buoyancy force. Enabled by default. | `true` |
| `waterCenter` | `Vector2` | World-space X/Z center of the rectangular fallback water area. Ignored when Water Size defines an infinite plane. | `new Vector2(-280, 80)` |
| `waterCurrentEnabled` | `bool` | Use provider water velocity for drag and vertical damping. Surface height still controls immersion. Enabled by default. | `true` |
| `waterLevel` | `float` | World-space height in metres of the flat fallback water surface. | `2.3` |
| `waterSize` | `Vector2` | Zero size means an infinite flat water plane. Otherwise bounds are world-space X/Z. | `new Vector2(400, 640)` |
| `waveImpulsesEnabled` | `bool` | Allow occasional wave torque impulses. Disabled timers reset to prevent a queued impulse on re-enable. Enabled by default. | `true` |
| `yawDampingEnabled` | `bool` | Apply passive damping around world up. Rudder response remains independent. Enabled by default. | `true` |
| `yawDampingScale` | `float` | Scales inherited Angular Damping for yaw; pitch/roll use Rocking Damping. | `0.22`; Minimum: 0 |

## BoostSuspensionSettings

Shared physical suspension kick configuration. See [setup and behavior](../DrivingActions.md#suspension-kick-and-departure-wheelspin).

**Source:** `Runtime/Drive/Suspension/BoostSuspensionSettings.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `enabled` | `bool` | Enable a bounded physical suspension kick. Requires an active Suspension module and supported wheels. | `true` |
| `frontLift` | `float` | Front suspension extension in metres, limited to available wheel travel. | `.035`; Minimum: 0 |
| `maximumTilt` | `float` | Chassis tilt from gravity-up in degrees that cancels the suspension kick. After cancellation, release and press the boost again to rearm it. Applies to pitch and roll; does not cancel propulsion. | `20`; Range: 0 to 89 |
| `rearCompression` | `float` | Rear suspension compression in metres, limited to available wheel travel. | `.02`; Minimum: 0 |
| `returnTime` | `float` | Seconds to smoothly restore the authored spring rest positions. | `.3`; Minimum: .01f |
| `riseTime` | `float` | Seconds to smoothly build the suspension displacement. | `.15`; Minimum: .01f |

## Brakes

Configuration/implementation type for brakes within engine and drivetrain.

**Source:** `Runtime/Drive/Brakes/Brakes.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `brakeEventMinimumSpeedKph` | `float` | Minimum vehicle speed in km/h for moving-brake events. Does not change physical braking. | `3`; Speed field; stored in km/h, displayed in the selected speed unit |
| `brakeEventThreshold` | `float` | Minimum resolved service-brake demand for moving-brake events. Does not change physical braking. | `.1`; Range: 0 to 1 |
| `brakeRiseTime` | `float` | Seconds for a held digital brake to reach full service-brake strength. Zero is immediate. | `.5`; Minimum: 0 |
| `engine` | `Engine` ([fields](Engine.md#engine)) | Optional explicit link when engine and brakes live on different objects. | `None / unassigned` |
| `handbrakeTorque` | `float` | Braking torque in N·m applied to each handbrake-enabled wheel while the handbrake is held. Higher values lock those wheels more readily. | `6000`; Minimum: 0 |
| `progressiveDigitalBraking` | `bool` | Ramp button/keyboard service braking. Analog pedals always use their exact input strength. | `true` |
| `rollingBrakeTorque` | `float` | Equivalent rolling-resistance torque per braked wheel while coasting. Opposes travel without holding a stopped vehicle on a slope; service and parking brakes remain separate. | `0`; Minimum: 0 |
| `slopeReverseReleaseGrace` | `float` | Seconds to recognize a fresh reverse press after releasing a stopped brake on a slope. Does not engage reverse from a continuously held brake. | `.3`; Minimum: 0 |

## Burnout

### State and configuration

**Source:** `Runtime/Drive/Grounded/Burnout.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `automaticThrottle` | `bool` | Supply a forward throttle request before brakes/gearbox/clutch while the held launch request is eligible. Default true. | `true` |
| `boatBowLiftDegrees` | `float` | Extra supported hull bow lift during boat boost, in degrees; respects the boat pitch and tilt switches. | `2`; Range: 0 to 5 |
| `bypassStabilityControl` | `bool` | Temporarily skip Steering arcade yaw/lateral stabilization and slide speed hold during burnout. Default true; authored assist settings are preserved. | `true` |
| `bypassTractionControl` | `bool` | Let intentional wheelspin pass through the optional TCS while assistance is nonzero. Default true; normal TCS resumes after recovery. | `true` |
| `cooldown` | `float` | Seconds before starting another cycle after release/abort. Default 0.4. | `.4`; Minimum: 0 |
| `forceForwardDirection` | `bool` | Request forward acceleration while boosting, even when reversing. Applies forward wheel torque immediately while the body may still be moving backwards. | `true` |
| `forwardGrip` | `float` | Driven tire longitudinal grip scale during wheelspin. Default 0.55, allowing forward motion while spinning. | `.55`; Range: .05f to 1 |
| `gripRecoveryTime` | `float` | Recovery interval after spin or release. Default 0.4 seconds. | `.4`; Minimum: .01f |
| `holdBrakeTorque` | `float` | Maximum per-wheel holding torque in N m before wheel brake multipliers. Default 8000. | `8000`; Minimum: 0 |
| `holdDuration` | `float` | Seconds at full non-driven-wheel hold. Default 0.6. | `.6`; Minimum: 0 |
| `holdNonDrivenWheels` | `bool` | Optional non-driven-wheel brake hold; disabled by default so the vehicle moves during wheelspin. | `false` |
| `holdReleaseTime` | `float` | Seconds to smoothly release that hold. Default 0.4. | `.4`; Minimum: .01f |
| `maximumSpinSpeed` | `float` | Safety speed cutoff for wheelspin assistance, independent of sustained steering. Default 60 m/s (216 km/h). | `60`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumStartSpeed` | `float` | Highest speed at which a new burnout may start. Default 40 m/s (144 km/h), including starts while already driving. | `40`; Speed field; stored in m/s, displayed in the selected speed unit |
| `minimumEndSpeed` | `float` | Minimum road speed in m/s required for timed recovery while held. Default 12 (43.2 km/h); zero uses duration alone. Clamped to maximumSpinSpeed. Key release always begins recovery immediately. | `12`; Speed field; stored in m/s, displayed in the selected speed unit |
| `sidewaysGrip` | `float` | Driven tire lateral grip scale during wheelspin. Default 0.4 for drifting and donuts; normal grip returns during recovery. | `.4`; Range: .05f to 1 |
| `spinDuration` | `float` | Minimum held wheelspin duration before recovery. Default 3 seconds; recovery also requires minimumEndSpeed and no sustained steering. | `3`; Minimum: .01f |
| `suspensionKick` | `BurnoutSuspensionSettings` ([fields](Drive.md#burnoutsuspensionsettings)) | Physical spring rest-position shift during a supported launch; front extends and rear compresses. Does not move transforms or add chassis torque. | `new BurnoutSuspensionSettings{returnTime = .9}` |
| `sustainSteeringThreshold` | `float` | Steering magnitude required to retain a held powered slide. Default 0.15. | `.15`; Range: 0 to 1 |
| `sustainWhileSteering` | `bool` | Hold wheelspin while steering beyond sustainSteeringThreshold, even after the duration and minimum end speed. Default true; releasing Ctrl or the safety cutoff still ends assistance. | `true` |
| `throttle` | `float` | Automatic forward pedal strength. Default 1; range 0.1 to 1. | `1`; Range: .1f to 1 |
| `torqueMultiplier` | `float` | Maximum temporary combustion/direct torque and finite power/acceleration-cap multiplier. Default 2.5; minimum 1. | `2.5`; Minimum: 1 |
| `wheelSpeedMultiplier` | `float` | Bounded native wheel overspeed allowance during wheelspin. Default 1.5; range 1–2; prevents runaway wheel energy. | `1.5`; Range: 1 to 2 |

## BurnoutSuspensionSettings

**Source:** `Runtime/Drive/Suspension/BoostSuspensionSettings.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [BoostSuspensionSettings](Drive.md#boostsuspensionsettings). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `maximumForwardActivationSpeed` | `float` | Maximum signed forward road speed for starting the suspension kick, in m/s. Reverse movement is always eligible. Does not stop an already accepted kick or limit burnout propulsion. A refused start requires releasing and pressing burnout again. | `5`; Speed field; stored in m/s, displayed in the selected speed unit |

## ContactEnvelope

Samples tire-shaped support and adjusts effective native support radius.

**Source:** `Runtime/Drive/Suspension/ContactEnvelope.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `edgeRefinementIterations` | `int` | Binary-search iterations at tread edges and height discontinuities. Fewer iterations reduce raycasts but approximate curbs/gaps more coarsely. Default 7 preserves existing precision. | `7`; Range: 0 to 10 |
| `groundLayers` | `LayerMask` | Layers accepted by tire-envelope ground probes. Exclude vehicle colliders to avoid self-support. | `~0` |
| `longitudinalSamples` | `int` | Number of ground samples along the tire's rolling direction. More samples detect short steps more smoothly but require more ground queries; an odd count from 3 to 15 is used. | `9`; Range: 3 to 15 |
| `maximumLiftRadius` | `float` | Maximum upward support correction as a fraction of tire radius. At 0.8 the correction cannot exceed 80% of the radius. Reduce to limit how far edge samples can lift the wheel. | `1`; Range: 0 to 1 |
| `minimumGroundNormal` | `float` | Minimum dot product between a sampled normal and vehicle up for that sample to count as supporting ground. | `.35`; Range: 0 to 1 |
| `optimizeWhenStationary` | `bool` | Reduce scheduled probes while an awake vehicle is stationary. Movement, driving/steering demand, wake-up and mode/interval changes force a fresh probe. Sleeping Probe Interval remains a separate sleep-only control. | `true` |
| `probeEveryFixedSteps` | `int` | Probe moving-vehicle ground every N fixed steps. Intermediate steps reuse support samples while suspension damping still updates each step. Default 2 halves scheduled probe batches; active radius corrections and Rigidbody supports are checked every step, including while stationary. Unchanged box support may reuse the previous result after current geometry validation. Use 1 for fast vehicles or sharp curbs. Higher values can miss narrow obstacles. Teleport forces a fresh probe. | `2`; Range: 1 to 8 |
| `reuseNativeGroundContact` | `bool` | Reuse WheelCollider contact only after current corner rays and an overlap query certify the same unobstructed box face. Curbs, meshes, gaps, changed layers and stale/missing contacts use a fresh centre ray. | `true` |
| `sleepingProbeInterval` | `float` | Seconds between probes while the Rigidbody sleeps with no throttle/steering request. Longer intervals reduce idle queries but delay terrain/support changes; zero probes every fixed step. Default 0.2 seconds. | `.2`; Minimum: 0 |
| `stationaryAngularSpeedThreshold` | `float` | Maximum angular speed considered stationary, in radians/s. Default 0.02 rad/s; rotating in place above this threshold probes at the moving rate. | `.02`; Minimum: 0 |
| `stationaryLinearSpeedThreshold` | `float` | Maximum total chassis speed considered stationary, in m/s; includes vertical motion. Default 0.05 m/s. | `.05`; Minimum: 0 |
| `stationaryProbeEveryFixedSteps` | `int` | Fixed steps between stationary probe batches; never faster than the moving interval. Default 10 = 0.2 seconds at a 0.02-second timestep. Terrain changes between probes can be detected later. | `10`; Range: 1 to 120 |
| `tireHalfWidth` | `float` | Half of the tire sampling width in metres; per-wheel geometry can supply the actual width during configuration. | `.12`; Minimum: 0 |
| `widthSamples` | `int` | Number of sample strips across the tire width, from 1 to 3. More strips help detect support near tire edges but add ground queries. | `3`; Range: 1 to 3 |

## ControlArm

Resolves a visual control arm against its authored geometry.

**Source:** `Runtime/Drive/Suspension/ControlArm.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `armLength` | `float` | Distance from hinge centre to outer ball joint, in metres. Pivot local X points outward; local Z is the hinge axis. | `1.4`; Minimum: .01f |
| `constrainHubToArc` | `bool` | Constrain the hub to this fixed-length arm's circular path. Disable to follow the native wheel suspension axis without changing track width; the visual linkage follows the supplied hub position. | `true` |
| `constrainNativeWheel` | `bool` | Allows the linkage to constrain the native wheel mount; turn off for a visual-only control arm. | `true` |
| `frontLeg` | `Transform` | Mesh for the wishbone's front branch. It is aligned between Inner Front Anchor and the outer joint as the suspension moves. | `None / unassigned` |
| `hub` | `Transform` | Hub transform whose position is adjusted to follow the wishbone path. Place it at the wheel centre and keep the fixed pivot outside its moving hierarchy. | `None / unassigned` |
| `hubOffset` | `Vector3` | Offset in metres from the arm's outer joint to the wheel centre, in Pivot's axes. Use it to account for the height and sideways offset of the upright. | `new Vector3(0, .25, 0)` |
| `innerFrontAnchor` | `Transform` | Chassis attachment for the front branch of the wishbone. The Front Leg mesh is placed between this point and the outer joint. | `None / unassigned` |
| `innerRearAnchor` | `Transform` | Chassis attachment for the rear branch of the wishbone. The Rear Leg mesh is placed between this point and the outer joint. | `None / unassigned` |
| `localLengthAxis` | `Vector3` | Axis running lengthwise through the wishbone branches in the mesh's own coordinates. The placement helper aligns this axis with the line between the attachments. | `Vector3.up` |
| `maximumAngle` | `float` | Highest arm angle in degrees around the pivot's hinge axis. Tightening this range limits how far the hub can follow the wishbone's arc. | `30`; Range: 0 to 89 |
| `meshLength` | `float` | Original length in metres of the wishbone branches along its length axis before scaling. The placement helper uses it to fit the model between its calculated endpoints; use the actual mesh length to avoid stretching errors. | `2`; Minimum: .001f |
| `minimumAngle` | `float` | Lowest arm angle in degrees around the pivot's hinge axis. Together with Maximum Angle it bounds the circular path available to the outer joint. | `-30`; Range: -89 to 0 |
| `outerJoint` | `Transform` | Optional marker moved to the wishbone's outer ball-joint position. Other visible suspension parts can use this point as an attachment. | `None / unassigned` |
| `pivot` | `Transform` | Fixed chassis-side reference for the wishbone's circular movement. Its position and orientation define the path that constrains the hub sideways as suspension moves. | `None / unassigned` |
| `rearLeg` | `Transform` | Mesh for the wishbone's rear branch. It is aligned between Inner Rear Anchor and the outer joint as the suspension moves. | `None / unassigned` |
| `rotationLimits` | `SuspensionRotationLimits` ([fields](Drive.md#suspensionrotationlimits)) | Additional local-axis permissions and angle stops for the arm's rotation. Use these to keep a visible/solved linkage from articulating on impossible axes. | `new SuspensionRotationLimits()` |
| `shockAnchor` | `Transform` | Optional moving shock attachment placed along the wishbone between Pivot and the solved outer joint. Shock Mount Fraction chooses its position. | `None / unassigned` |
| `shockMountFraction` | `float` | Position of Shock Anchor along the arm: 0 is the chassis pivot and 1 is the outer joint. Moving it inward makes the shock attachment travel less for the same wheel movement. | `.7`; Range: .05f to 1 |
| `showGizmos` | `bool` | Shows pivot, outer joint and travel guides in the Scene view for setup. It does not enable physics, move the vehicle or change the visible game model. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `steeringLinkage` | `SteeringTieRod` ([fields](Drive.md#steeringtierod)) | Optional tie-rod setup supplying the steering pivot and wheel-centre offset. This keeps wishbone movement consistent with the wheel's steering arc. | `None / unassigned` |
| `upright` | `Transform` | Optional upright mesh joining the outer arm joint to the hub. It follows the solved hub position and configured mesh axis. | `None / unassigned` |
| `wheel` | `WheelCollider` | Native wheel whose suspension supplies wheel height. When Constrain Native Wheel is on, the collider mount is corrected sideways to follow the arm's path. | `None / unassigned` |
| `wheelAdapter` | `Wheel` ([fields](Physics.md#wheel)) | UVS Wheel used to place its tire visual at the solved hub centre. If empty, the component checks the assigned Wheel Collider for an adapter. | `None / unassigned` |

## Drive

Retains the vehicle's boat motion and sampling history.

**Source:** `Runtime/Drive/Drive.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## DriveModule

Configuration/implementation type for drive module within movement strategies and transitions.

**Source:** `Runtime/Drive/Core/DriveModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [VehicleModule](Common.md#vehiclemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## DriveProfile

Defines settings creation, configuration, stepping and drive-demand resolution.

**Source:** `Runtime/Drive/DriveProfile.cs`. Abstract base; settings are inherited by derived components.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `pitchRateBySpeed` | `AnimationCurve` | X: actual speed in km/h. Y: pitch response multiplier; 1 preserves the base value. Missing/empty curves use 1. | `AnimationCurve.Linear(0, 1, 300, .65)` |
| `releaseAllForcesOnIgnitionOff` | `bool` | Release profile forces and shared driving/stability assistance while the installed engine is not running. Gravity, native collisions and passive wheel suspension remain physical. Ignition on restores automatic operation; a manual ReleaseAllForces request remains until RestoreAllForces. | `false` |
| `rollRateBySpeed` | `AnimationCurve` | X: actual speed in km/h. Y: roll response multiplier; 1 preserves the base value. Missing/empty curves use 1. | `AnimationCurve.Linear(0, 1, 300, .65)` |
| `rotationReleaseDuration` | `float` | Soft release time in seconds to approximately 95% settling. Zero preserves existing handling. Ground/water/hover profiles ease released steering/rotation input; aircraft and spacecraft use their dedicated rotation controller. Does not affect throttle or braking. | `0`; Minimum: 0 |
| `speedSensitiveRotation` | `bool` | Enable km/h-based pitch, yaw/steering and roll curves. Off preserves the profile's existing handling. Only axes used by the profile have an effect. | `false` |
| `steeringSpeedLimitEnabled` | `bool` | Allow the shared Steering module to reduce steering range with speed using its configured speed-sensitive and lateral-acceleration limits. Disabling retains minimum turning radius and Ackermann geometry. | `true` |
| `yawRateBySpeed` | `AnimationCurve` | X: actual speed in km/h. Y: yaw/steering response multiplier; 1 preserves the base value. Missing/empty curves use 1. | `AnimationCurve.Linear(0, 1, 300, .65)` |

## DriveProfileSlot

Serializable registration descriptor. Each slot stores an independent strategy configuration.

**Source:** `Runtime/Drive/ProfileSwitcher.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `id` | `string` | Name used to request this driving setup and match transition rules. Use exactly this ID in profile-switch commands and transitions. | `None / unassigned` |
| `profile` | `DriveProfile` ([fields](Drive.md#driveprofile)) | Movement setup activated when this slot is selected. Choose its concrete type, then tune how that mode accelerates, steers and supports the vehicle. | `None / unassigned`; Polymorphic configuration; choose a concrete type |

## DrivingAssists

Configuration/implementation type for driving assists within engine and drivetrain.

**Source:** `Runtime/Drive/Core/DrivingAssists.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `corneringFreedom` | `float` | Amount of cornering freedom retained while allocating traction between propulsion and turning. | `.65`; Range: 0 to 1 |
| `lateralResponse` | `float` | Strength of stability assistance opposing sideways vehicle velocity. Increase to suppress slides sooner; reduce for a looser, more drift-friendly response. | `5`; Minimum: 0 |
| `launchReferenceSpeed` | `float` | Low-speed reference in m/s used to stabilize slip/traction calculations during launch. | `3`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumYawRate` | `float` | Maximum target turning rate for stability assistance, in radians per second. Lower values restrain fast rotation; higher values permit tighter, faster turns. | `1.1`; Minimum: .1f |
| `minimumTorqueScale` | `float` | Minimum fraction of requested engine torque retained by traction control. Lower values allow stronger power cuts during wheelspin; higher values keep more power available. | `.2`; Range: 0 to 1 |
| `recoveryRate` | `float` | Rate at which allowed drive torque recovers after excess slip subsides. | `4`; Minimum: 0 |
| `reductionRate` | `float` | Rate at which allowed drive torque decreases when wheel slip exceeds the target. | `8`; Minimum: 0 |
| `reserveGripForCornering` | `bool` | Tells traction control to leave some tire grip for turning instead of using it all for acceleration. Enable to reduce power-induced understeer or slides. | `false` |
| `stabilityControlEnabled` | `bool` | Enables Steering's assisted yaw and sideways-motion corrections. Turn off to let tire forces and driver input determine slides without those corrections. | `true` |
| `stabilityStrength` | `float` | Overall blend/strength of the stability corrections; zero removes this assistance contribution. | `.72`; Range: 0 to 1 |
| `stabilizePoweredSlides` | `bool` | Allows stability assistance to correct powered sliding instead of leaving it entirely to driver input. | `true` |
| `targetSlip` | `float` | Desired longitudinal slip magnitude while applying propulsion torque. | `.24`; Minimum: .01f |
| `tractionControlEnabled` | `bool` | Enables the TractionControl module through this shared assist panel. It reduces drive torque when driven wheels spin faster than their available grip permits. | `true` |
| `tractionReserve` | `float` | Fraction of estimated traction kept available when limiting drive torque. | `.98`; Range: .1f to 1 |
| `yawResponse` | `float` | Speed of stability assistance turning the chassis toward the requested yaw rate. Higher values correct heading errors faster; lower values let rotation build more freely. | `7.5`; Minimum: 0 |

## FreeProfile

Configuration/implementation type for free profile within movement strategies and transitions.

**Source:** `Runtime/Drive/Profiles/FreeProfile.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [DriveProfile](Drive.md#driveprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `acceleration` | `float` | Acceleration in m/s² applied along the requested free-movement direction. Increase to reach speed faster in this mode. | `12`; Minimum: 0 |
| `angularDamping` | `float` | Resistance slowing rotation in free-movement mode. Increase to stop turning sooner after rotational input is removed. | `3`; Minimum: 0 |
| `drag` | `float` | Resistance slowing linear motion in free-movement mode. Increase to coast less after releasing input; reduce to retain momentum. | `.4`; Minimum: 0 |

## HalfShaft

Presents axle articulation and shaft rotation.

**Source:** `Runtime/Drive/Suspension/HalfShaft.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `articulation` | `SuspensionRotationLimits` ([fields](Drive.md#suspensionrotationlimits)) | Swing permissions in the neutral mesh frame. For a Y cylinder along chassis X, Z permits vertical articulation. | `new SuspensionRotationLimits()` |
| `innerAnchor` | `Transform` | Gearbox/differential-side end of the drive shaft. Its orientation supplies the shaft's reference frame and the direction used to check joint angle. | `None / unassigned` |
| `localRotationAxis` | `Vector3` | Cardinal mesh axis used for both length and rotation (Unity cylinder: Y). | `Vector3.up` |
| `maximumJointAngle` | `float` | Angle in degrees beyond which the shaft's Scene guide turns red. This is a setup warning for excessive articulation; it does not physically stop the shaft. | `45`; Range: 0 to 89 |
| `meshLength` | `float` | Original length in metres of the drive-shaft mesh along its length axis before scaling. The placement helper uses it to fit the model between its calculated endpoints; use the actual mesh length to avoid stretching errors. | `2`; Minimum: .001f |
| `outerAnchor` | `Transform` | Wheel-side end of the drive shaft. The visible shaft follows the line between this point and Inner Anchor as suspension and steering move. | `None / unassigned` |
| `rotationOffset` | `Vector3` | Mesh orientation correction in degrees relative to Inner Anchor. Use it when the shaft model's axes do not match the attachment frame. | `Zero-initialized Vector3` |
| `shaft` | `Transform` | Visible drive-shaft mesh aligned between the two anchors. If empty, this component's own transform is used. | `None / unassigned` |
| `showGizmos` | `bool` | Shows shaft endpoints and excessive joint angle guides in the Scene view for setup. It does not enable physics, move the vehicle or change the visible game model. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `spinAxes` | `SuspensionRotationAxes` | Permitted spin axes in mesh-local space. Enable the selected localRotationAxis to retain wheel spin. Options: `None`, `X`, `Y`, `Z`, `All`. Multiple flags can be combined. | `SuspensionRotationAxes.All` |
| `spinMultiplier` | `float` | Multiplies the wheel rotation applied to the shaft visual. Use 1 for matching speed, 0 for no spin, or a negative value to reverse it. | `1` |
| `spinOffset` | `float` | Extra shaft rotation in degrees added to the wheel-driven spin. Use it to align the shaft's starting orientation without changing its attachment points. | `0` |
| `wheel` | `WheelCollider` | Wheel collider supplying shaft spin. Assign the driven wheel at the shaft's outer end so the shaft rotates with that wheel. | `None / unassigned` |

## HelicopterProfile

Configuration/implementation type for helicopter profile within flight and landing gear.

**Source:** `Runtime/Drive/Profiles/HelicopterProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [AirProfile](Drive.md#airprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `attitudeInputScale` | `float` | Pitch/roll input contribution to the target up vector. | `.45`; Range: 0 to 1 |
| `attitudeStrength` | `float` | Strength of pitch/roll restoring angular acceleration toward the helicopter target attitude. | `18`; Minimum: 0 |
| `automaticLeveling` | `bool` | Apply restoring pitch/roll control toward the commanded helicopter attitude. Disabling leaves native angular motion unconstrained by this assist. | `true` |
| `compensateGravity` | `bool` | Include gravity compensation in powered rotor lift. Support scales with rotor spool and fades as the rotor stops. | `true` |
| `holdAltitude` | `bool` | Hold height after releasing ascend/descend and brake horizontal drift after releasing movement, without returning to a position. Requires a running engine and fully spooled rotor. Disable for the original vertical damping behavior. | `true` |
| `horizontalDriveEnabled` | `bool` | Allow horizontal thrust from rotor tilt and automatic drift braking. Enabled by default. | `true` |
| `hoverDriftBrakingEnabled` | `bool` | Brake horizontal drift in neutral powered hover when altitude hold and automatic leveling are active. Enabled by default. | `true` |
| `linearDragEnabled` | `bool` | Apply inherited velocity-proportional air resistance. Enabled by default. | `true` |
| `tiltAccelerationMultiplier` | `float` | Multiplier for horizontal acceleration from rotor tilt. | `2`; Minimum: 0 |
| `verticalDamping` | `float` | Vertical velocity damping applied through powered rotor lift. Higher values reduce climb/descent overshoot. | `1.5`; Minimum: 0 |
| `verticalLiftEnabled` | `bool` | Allow the vertical rotor-support/collective channel, including altitude hold and gravity compensation. Enabled by default. | `true` |
| `yawAcceleration` | `float` | Commanded yaw angular acceleration in radians per second squared before configured damping. | `5`; Minimum: 0 |
| `yawControlEnabled` | `bool` | Apply commanded yaw torque independently of horizontal thrust. Enabled by default. | `true` |

## HoverDriveTransition

Configuration/implementation type for hover drive transition within movement strategies and transitions.

**Source:** `Runtime/Drive/Profiles/HoverDriveTransition.cs`. Component / asset.

**Inherited settings:** [ProfileTransition](Drive.md#profiletransition). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `landingClearance` | `float` | Extra clearance above fully extended tires while unfolding near the ground. Zero disables landing assistance. | `.2`; Minimum: 0 |
| `landingLiftAcceleration` | `float` | Maximum upward correction acceleration during low hover-to-drive deployment, in m/s². | `25`; Minimum: 0 |

## HoverProfile

Configuration/implementation type for hover profile within movement strategies and transitions.

**Source:** `Runtime/Drive/Profiles/HoverProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [AirProfile](Drive.md#airprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `attitudeStrength` | `float` | Strength of restoring pitch/roll angular acceleration toward the hover target attitude. | `12`; Minimum: 0 |
| `automaticLeveling` | `bool` | Apply restoring torque toward the hover target attitude, including configured thrust/steering lean. | `true` |
| `bodyTiltDegrees` | `float` | Maximum combined hull lean toward forward/sideways thrust and steering, in degrees. | `5`; Range: 0 to 15 |
| `bodyTiltEnabled` | `bool` | Lean the leveling target with movement/steering demand. Disable for a level target; Automatic Leveling still owns restoring torque. Enabled by default. | `true` |
| `bodyTiltResponse` | `float` | Hull lean response per second, including return to level. | `2`; Minimum: .1f |
| `compensateGravity` | `bool` | Include upward gravity compensation in powered hover support. Disable to require manual collective or surface spring support. | `true` |
| `damping` | `float` | Damping of vertical movement in the ground-clearance spring. Higher values reduce hover-height oscillation. | `6`; Minimum: 0 |
| `groundMask` | `LayerMask` | Physics layers eligible for hover ground-support queries. Exclude the vehicle and non-supporting scenery as needed. | `-1` |
| `height` | `float` | Requested clearance above detected ground in metres. The hover spring regulates this distance while surface support is enabled. | `2.5`; Minimum: .2f |
| `horizontalDriveEnabled` | `bool` | Allow forward and sideways thrust from commands. Enabled by default. | `true` |
| `linearDragEnabled` | `bool` | Apply inherited velocity-proportional resistance. Enabled by default. | `true` |
| `maximumAscentAcceleration` | `float` | Maximum upward acceleration requested by hover support in metres per second squared. | `25`; Minimum: 0 |
| `maximumDescentAcceleration` | `float` | Maximum downward acceleration requested by hover support in metres per second squared. Does not cap native gravity or collision impulses. | `15`; Minimum: 0 |
| `spring` | `float` | Clearance spring response converting ground-distance error into vertical support acceleration. | `12`; Minimum: 0 |
| `surfaceSupport` | `bool` | Use ground-distance queries and the clearance spring to maintain the requested hover height. | `true` |
| `verticalDamping` | `float` | Additional powered vertical velocity damping, independent of the clearance spring. | `2`; Minimum: 0 |
| `verticalSupportEnabled` | `bool` | Allow collective, clearance spring, vertical damping and gravity compensation channel. Enabled by default. | `true` |
| `wheelSteeringTilt` | `float` | Maximum visual wheel tilt in degrees caused by steering demand. Does not change wheel collision geometry. | `12`; Range: 0 to 30 |
| `wheelThrustTilt` | `float` | Maximum visual wheel tilt in degrees caused by forward/sideways thrust demand. | `10`; Range: 0 to 30 |
| `wheelTiltResponse` | `float` | Visual wheel tilt response per second. Lower values make acceleration, braking and steering tilt settle more slowly. | `8`; Minimum: .1f |
| `yawAcceleration` | `float` | Commanded hover yaw angular acceleration in radians per second squared. | `4`; Minimum: 0 |
| `yawControlEnabled` | `bool` | Allow commanded steering/yaw torque, independently of yaw damping. Enabled by default. | `true` |
| `yawDamping` | `float` | Passive damping opposing hover yaw angular velocity. Higher values stop rotation more quickly after steering is released. | `2`; Minimum: 0 |
| `yawDampingEnabled` | `bool` | Allow passive damping around the vertical yaw axis. Enabled by default. | `true` |

## MotorcycleBalance

Configuration/implementation type for motorcycle balance within engine and drivetrain.

**Source:** `Runtime/Drive/Grounded/MotorcycleBalance.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `accelerationSmoothTime` | `float` | Seconds to smooth measured cornering acceleration. Suppresses contact spikes without adding yaw or steering torque. | `.2`; Minimum: 0 |
| `assistBrakingTurns` | `bool` | Keep supported braking turns aligned with steering using bounded physical torque; yields during wheel lift. | `true` |
| `assistBurnoutTurns` | `bool` | Assist slow powered circles with bounded heading torque while both tires support the motorcycle. Leaves tire forces, wheelspin and chassis velocity under physics control. | `true` |
| `balanceDamping` | `float` | Resistance to roll motion while balancing. Increase to reduce side-to-side wobble; excessive damping can make lean changes sluggish. | `65`; Minimum: 0 |
| `balanceStrength` | `float` | Strength of the roll correction toward the requested lean. Increase to hold/recover the bike's balance more firmly; too much can make corrections abrupt. | `1200`; Minimum: 0 |
| `brakingYawDamping` | `float` | Fallback heading-rate damping during braking slides without ground assistance, per second. Assisted turns use the shared yaw controller. | `6`; Minimum: 0 |
| `burnoutTurnAcceleration` | `float` | Maximum heading acceleration during a supported burnout turn, in radians per second squared. | `3`; Minimum: 0 |
| `burnoutTurnLean` | `float` | Maximum low-speed inside bank during a powered circle. Existing obstacle clearance and roll response still apply. | `14`; Range: 0 to 35 |
| `burnoutTurnMaximumSpeed` | `float` | Speed at which burnout turn assistance fully fades out. It already fades through the upper quarter of this range. | `8`; Speed field; stored in m/s, displayed in the selected speed unit |
| `burnoutTurnRate` | `float` | Maximum assisted burnout heading rate in radians per second. Zero disables the heading correction. | `1.1`; Minimum: 0 |
| `coordinateSteering` | `bool` | Limit actual wheel steering at speed to the cornering acceleration supported by Maximum Lean. Full parking-speed steering remains available. When Ground Assist is enabled its coordinated envelope also applies. Disable both options for unrestricted wheel steering and deliberate slides. | `false` |
| `disableBalanceOnDriverEject` | `bool` | Stop assisted riding balance and Stabilization angular damping/righting when the driver is ejected, allowing native falling and tumbling. A new driver or vehicle respawn restores balance. Ordinary passenger ejection does not affect it. | `true` |
| `fullLeanSpeed` | `float` | Speed in m/s at which the full calculated cornering lean is allowed. Between Lean Start Speed and this value, banking is blended in gradually. | `5.5`; Speed field; stored in m/s, displayed in the selected speed unit |
| `groundAssist` | `MotorcycleGroundAssist` ([fields](Drive.md#motorcyclegroundassist)) | Optional ground-contact assistance for hard turns and boost. Does not act in flight or during requested wheelies. | `new MotorcycleGroundAssist()` |
| `groundLeanBrakingAcceleration` | `float` | Maximum acceleration opposing outward roll near the world bank limit, in radians per second squared. | `30`; Minimum: 0 |
| `groundLeanLimit` | `float` | Base maximum assisted side bank relative to gravity, in degrees. Slope bank reduction scales this bound on inclined terrain. | `55`; Range: 30 to 85 |
| `groundLeanLimitMargin` | `float` | Minimum anticipation margin before the world bank limit, in degrees. Fast outward roll is braked earlier when its stopping distance requires it. | `10`; Range: 1 to 30 |
| `leanObstacleClearance` | `float` | Safety distance in metres retained before the first blocked bank angle. | `.08`; Minimum: 0 |
| `leanObstacleLayers` | `LayerMask` | Solid obstacle layers considered by the rider bank-clearance check. Triggers and this vehicle are ignored. | `~0` |
| `leanRate` | `float` | Maximum rate at which requested motorcycle lean changes, in degrees per second. | `170`; Minimum: 1 |
| `leanRateDamping` | `float` | Damping accounting for how quickly the desired lean itself changes. Increase to soften overshoot during fast direction changes. | `.35`; Range: 0 to 1 |
| `leanStartSpeed` | `float` | Speed in m/s below which turning-related lean fades toward upright. Increase to keep the bike upright through more low-speed manoeuvres. | `1.4`; Speed field; stored in m/s, displayed in the selected speed unit |
| `limitGroundLean` | `bool` | Limit bank against both gravity and the existing tire-support plane. Brakes further outward roll and yields to inward recovery without new ground probes. | `true` |
| `maximumAngularAcceleration` | `float` | Limit in rad/s² on the balance correction. Raise only if the bike should recover or lean more sharply under strong input. | `150`; Minimum: 0 |
| `maximumBrakingYawAcceleration` | `float` | Maximum heading deceleration for fallback braking slides and excessive powered-burnout spin, in radians per second squared. | `12`; Minimum: 0 |
| `maximumLean` | `float` | Greatest requested bank angle in degrees during a turn. Lower values keep the bike more upright; higher values allow deeper cornering lean. | `45`; Range: 0 to 50 |
| `measuredAccelerationWeight` | `float` | Blend from predicted cornering acceleration toward measured sideways acceleration when calculating lean. Increase to make lean follow actual motion more closely. | `.25`; Range: 0 to 1 |
| `nativeCollisionResponseAfterDriverEject` | `bool` | After driver ejection, use native collider friction and restitution instead of additional Collisions body-friction, rebound and crash-transfer impulses. Requires Disable Balance On Driver Eject. Driver re-entry or respawn restores configured collision assistance. | `true` |
| `preventObstacleLean` | `bool` | Limit assisted bank near solid obstacles using one approximate torso capsule per occupant. Does not disable wheel steering or native impacts. | `true` |
| `recoveryAngle` | `float` | Largest tilt from upright, in degrees, at which grounded balance assistance will still try to recover the motorcycle. Beyond this angle it stops righting an already fallen bike. | `65`; Range: 30 to 85 |
| `reversalLeanRate` | `float` | Maximum lean target rate in degrees per second when steering asks for the opposite bank. Lets the rider transfer weight promptly while braking into an opposite turn. | `335`; Minimum: 1 |
| `steeringBalanceMargin` | `float` | Fraction of Maximum Lean cornering capacity available to Steering path assistance and optional wheel-angle coordination. Leaves room for roll response; 1 uses the full equilibrium bank. | `.95`; Range: .1f to 1 |
| `steeringPrediction` | `float` | Blend toward the driver's requested steering instead of waiting for the current wheel angle. Increase to begin leaning earlier when steering changes. | `.75`; Range: 0 to 1 |
| `wheelieControl` | `MotorcycleWheelieControl` ([fields](Drive.md#motorcyclewheeliecontrol)) | Separate bank and turn response while Wheel Lift owns the maneuver, including controlled lowering. | `new MotorcycleWheelieControl()` |

## MotorcycleGroundAssist

Bounded ground-contact, cornering and braking assistance for MotorcycleBalance.

**Source:** `Runtime/Drive/Grounded/Assistance/MotorcycleGroundAssist.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `angularDamping` | `float` | Damping of pitch departure from the support plane. Roll damping belongs to Motorcycle Balance. | `12`; Minimum: 0 |
| `bankResponseTime` | `float` | Seconds for a critically damped bank-target response. Smooths both pickup and reversal without reducing wheel steering. | `.17`; Minimum: .01f |
| `bankTurnInfluence` | `float` | Contribution of actual bank to the supported turn, including coasting with neutral steering. | `.35`; Range: 0 to 1 |
| `brakeRecoveryTime` | `float` | Seconds to restore full service-brake pressure after a load/slip intervention. | `.15`; Minimum: .01f |
| `brakeReleaseTime` | `float` | Seconds to release service-brake pressure after detecting excessive tire slip. | `.04`; Minimum: .01f |
| `brakeSlipLimit` | `float` | Tread/road speed slip ratio above which service-brake pressure is eased. Reduced while banked to retain lateral grip. | `.25`; Range: .05f to .8f |
| `brakingLeanScale` | `float` | Fraction of normal maximum bank retained under full braking. One preserves the steering envelope; smaller values deliberately widen braking turns. | `1`; Range: .2f to 1 |
| `brakingResponseMultiplier` | `float` | Response-time multiplier when reversing a turn while braking. Lower values admit the opposite turn sooner. | `.65`; Range: .1f to 1 |
| `brakingSupport` | `bool` | Reserve service-brake grip for steering and ease front pressure when the rear tire unloads. Does not change handbrake or standstill holding. | `true` |
| `brakingYawStrength` | `float` | Correction of persistent unwanted yaw while braking into a requested turn. Zero uses proportional steering response only. | `40`; Minimum: 0 |
| `contactAcceleration` | `float` | Maximum contact rebound damping acceleration in m/s² while at least two tires support the chassis. No steady downforce is applied. | `15`; Minimum: 0 |
| `corneringStrength` | `float` | Multiplier for the supported cornering envelope. Higher values allow tighter assisted turns without raising the rider's maximum bank. | `1.85`; Minimum: 1 |
| `enabled` | `bool` | Controls enabled for this mechanism. | `true` |
| `fullSpeed` | `float` | Ground speed in m/s where full assistance is available. | `12`; Minimum: 0 |
| `handbrakeSlideDeceleration` | `float` | Extra road-plane deceleration in m/s² during a tight handbrake slide. Reduces slide radius without adding heading rotation; zero disables it. | `5`; Minimum: 0 |
| `maximumAngularAcceleration` | `float` | Maximum added pitch angular acceleration in rad/s². | `60`; Minimum: 0 |
| `maximumBankRate` | `float` | Maximum bank-target speed in degrees per second. Bank Response Time smooths acceleration and reversal around this limit. | `140`; Minimum: 1 |
| `maximumBrakingYawAcceleration` | `float` | Maximum requested yaw correction under full service braking, in rad/s². Applied through the current chassis inertia. | `25`; Minimum: 0 |
| `minimumContactAuthority` | `float` | Minimum turn-assist contact authority with at least two supported tires. Incidental single-tire contact uses reduced authority; manual wheelie has separate settings. | `.65`; Range: 0 to 1 |
| `pitchSupport` | `float` | Restoring pitch acceleration toward the supporting surface, in rad/s² per radian. Inactive without tire contact or during wheelie. | `40`; Minimum: 0 |
| `rearLoadReserve` | `float` | Rear share of total contact load below which front brake pressure is eased to discourage stoppies. | `.12`; Range: 0 to .4f |
| `reduceLeanOnSlopes` | `bool` | Reduce the bank request and physical world-bank boundary as terrain gets steeper, retaining ordinary handlebar steering instead. | `true` |
| `responseTime` | `float` | Seconds for the assistance strength to approach a changed steering/boost demand. | `.12`; Minimum: 0 |
| `slopeLeanFullAngle` | `float` | Terrain inclination in degrees where Minimum Slope Lean Scale is reached. | `45`; Range: 1 to 85 |
| `slopeLeanMinimumScale` | `float` | Fraction of the normal bank request and world-bank boundary retained on steep terrain. Wheel steering is preserved. | `.2`; Range: 0 to 1 |
| `slopeLeanResponseTime` | `float` | Seconds for terrain bank reduction to follow a changed slope. Filters short bumps and prevents abrupt tightening of the physical bank boundary; zero is immediate. | `.35`; Minimum: 0 |
| `slopeLeanStartAngle` | `float` | Terrain inclination in degrees where steering-induced bank starts reducing. | `5`; Range: 0 to 80 |
| `startSpeed` | `float` | Ground speed in m/s where assistance begins fading in. | `3`; Minimum: 0 |
| `steeringResponseTime` | `float` | Seconds to ease steering into a new turn while the bank target anticipates the input. Zero disables this easing. | `.12`; Minimum: 0 |
| `stoppiePitchAngle` | `float` | Nose-down pitch relative to the supporting surface, in degrees, at which rear unloading receives full front-pressure relief. | `6`; Range: 1 to 20 |
| `supportDamping` | `float` | Damping of separating support-point velocity, in 1/s. Does not compress resting suspension. | `10`; Minimum: 0 |
| `turnEntrySupport` | `float` | Cornering authority before the chassis banks into a new turn. The rest arrives smoothly with actual lean; parking steering stays unchanged. | `.45`; Range: .2f to 1 |

## MotorcycleProfile

Configuration/implementation type for motorcycle profile within movement strategies and transitions.

**Source:** `Runtime/Drive/Profiles/MotorcycleProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [DriveProfile](Drive.md#driveprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `automaticBalance` | `bool` | Enable fallback balance when no Motorcycle Balance module is installed. | `true` |
| `balanceDamping` | `float` | Roll damping of the fallback balance. Increase to reduce rocking when no MotorcycleBalance module provides balance control. | `14`; Minimum: 0 |
| `balanceStrength` | `float` | Roll-restoring strength of the fallback balance. Increase for firmer upright/lean support; a separate MotorcycleBalance module takes over when present. | `80`; Minimum: 0 |
| `maximumAngularAcceleration` | `float` | Maximum fallback balance correction in rad/s². This bounds how sharply the profile can rotate the bike toward its desired lean. | `100`; Minimum: 0 |
| `maximumLean` | `float` | Maximum lean in degrees used by the profile's fallback balance. Increase for deeper cornering bank when no MotorcycleBalance module supplies the balance logic. | `28`; Range: 0 to 45 |
| `wheelbase` | `float` | Distance in metres between front and rear axles, used to convert steering and speed into the fallback target lean. | `1.45`; Minimum: .1f |

## MotorcycleWheelieControl

Lean and yaw limits while a motorcycle is supported by its rear wheel, with smooth recovery after landing.

**Source:** `Runtime/Drive/Grounded/Assistance/MotorcycleWheelieControl.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `accelerationMultiplier` | `float` | Powered acceleration multiplier while riding on one supporting driven wheel with the steering wheel raised. Does not raise top speed or add propulsion without engine torque. | `1.08`; Range: 1 to 2 |
| `balanceDamping` | `float` | Roll damping for rear-wheel balance. | `200`; Minimum: 0 |
| `balanceStrength` | `float` | Roll spring for rear-wheel balance; separate from the stiffer two-wheel cornering response. | `1200`; Minimum: 0 |
| `enabled` | `bool` | Controls enabled for this mechanism. | `true` |
| `highSpeedLeanScale` | `float` | Fraction of wheelie lean retained at high speed. Reduces single-tire camber wobble. | `.65`; Range: 0 to 1 |
| `leanFadeEndSpeed` | `float` | Speed at which High Speed Lean Scale is fully applied. | `25`; Speed field; stored in m/s, displayed in the selected speed unit |
| `leanFadeStartSpeed` | `float` | Speed above which the small wheelie bank is reduced further. | `12`; Speed field; stored in m/s, displayed in the selected speed unit |
| `leanResponseTime` | `float` | Seconds to ease wheelie bank changes. Does not set the body's rotation. | `.2`; Minimum: 0 |
| `maximumLateralAcceleration` | `float` | Arcade sideways acceleration budget in m/s² during wheelie. Allows a useful turn without requiring a large body bank. | `3`; Minimum: 0 |
| `maximumLean` | `float` | Maximum sideways lean in degrees during wheel lift and controlled lowering. | `12`; Range: 0 to 20 |
| `maximumRollAcceleration` | `float` | Maximum wheelie roll correction in radians per second squared. | `300`; Minimum: 0 |
| `maximumSteeringAngle` | `float` | Maximum wheel angle during wheelie, capped by the vehicle steering lock but independent of speed. Recovery blends back to normal steering after lowering. | `90`; Range: 0 to 90 |
| `maximumYawAcceleration` | `float` | Maximum wheelie yaw correction in radians per second squared. | `8`; Minimum: 0 |
| `maximumYawRate` | `float` | Requested wheelie heading rate in radians per second at full steering. Separate from body lean; also limited by Maximum Lateral Acceleration. | `.22`; Minimum: 0 |
| `minimumContactAuthority` | `float` | Minimum steering-assist authority on the supporting tire. One rear tire is the expected wheelie support, not half of normal support. | `1`; Range: 0 to 1 |
| `releaseRecoveryTime` | `float` | Seconds to hand stance, steering and damping back to normal riding after the front wheel settles. | `.9`; Minimum: 0 |
| `turnResponse` | `float` | Response toward the requested wheelie turn rate. | `8`; Minimum: 0 |

## ParkingHold

Configuration/implementation type for parking hold within engine and drivetrain.

**Source:** `Runtime/Drive/Brakes/ParkingHold.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `assistParkingBrake` | `bool` | Counter gravity-driven slope creep while the handbrake or detached-trailer parking brake is active. Native tires retain braking and external-push response. | `true` |
| `assistServiceBrake` | `bool` | Counter gravity-driven slope creep while the service brake is active. Does not add planar braking resistance on level ground. | `true` |
| `captureSpeed` | `float` | Maximum vehicle speed in m/s at which the stationary parking/service hold can capture the body. | `.5`; Speed field; stored in m/s, displayed in the selected speed unit |

## ProfileSwitcher

Owns an ordered list of registered drive strategies and selects optional pair-specific transitions. Inherits ControllerModule.

**Source:** `Runtime/Drive/ProfileSwitcher.cs`. Component / asset.

**Inherited settings:** [ControllerModule](Controller.md#controllermodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `activeProfileId` | `string` | ID of the slot represented by VehicleController's current profile. Leave empty when the current profile is not registered. | `""` |
| `onCompleted` | `UnityEvent` | Event invoked after the animated transition finishes and the destination profile is applied. Use it to clear transition UI or enable mode-specific presentation. | `No listeners` |
| `onProgressed` | `UnityEvent<float>` | Event reporting transition progress from 0 at the start to 1 at completion. Connect a listener to synchronize UI or another animation. | `No listeners` |
| `onStarted` | `UnityEvent` | Event invoked when an animated profile transition begins. Use it to show a changing-mode indicator or start accompanying presentation. | `No listeners` |
| `profiles` | `List<DriveProfileSlot>` ([fields](Drive.md#driveprofileslot)) | Named driving setups available for switching, such as road driving and flight. Each entry combines an ID used by requests/transitions with the movement profile to activate. | `Empty list` |
| `transitions` | `ProfileTransition[]` ([fields](Drive.md#profiletransition)) | Optional animations and timing for specific source/target profile pairs. | `Empty list` |

## ProfileTransition

A route component for one source/destination ID pair, optionally bidirectional. Inherits MonoBehaviour.

**Source:** `Runtime/Drive/ProfileTransition.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `bidirectional` | `bool` | Also allows this route to handle a switch from To Profile ID back to From Profile ID. Turn off when the reverse change needs a different transition. | `false` |
| `duration` | `float` | Seconds over which the mode-change animation runs. Increase for a slower transformation; switching uses a minimum of 0.01 seconds. | `1`; Minimum: .01f |
| `fromProfileId` | `string` | ID of the profile this transition starts from. It must match a slot in ProfileSwitcher, for example drive. | `"Drive"` |
| `takeoffVelocity` | `float` | Upward velocity change in m/s when leaving a wheel-based mode. Zero disables the takeoff impulse. | `2`; Minimum: 0 |
| `toProfileId` | `string` | ID of the profile this transition leads to. It must match a registered slot, for example hover; the matching transition controls that mode change. | `"Hover"` |

## ShockAbsorber

Animates a telescoping shock and optionally overrides one wheel's physics.

**Source:** `Runtime/Drive/Suspension/ShockAbsorber.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `articulation` | `SuspensionRotationLimits` ([fields](Drive.md#suspensionrotationlimits)) | Local rotation axes and angle limits allowed for the shock bodies relative to the neutral mesh frame. Restrict only impossible swivel directions; the attachments still determine the requested pose. | `new SuspensionRotationLimits()` |
| `casing` | `Transform` | Outer shock body mesh. It stays at Chassis Anchor and points toward Wheel Anchor while the piston slides into it. | `None / unassigned` |
| `casingLength` | `float` | Visible outer shock body length in metres. Sets where that fixed-length piece ends; it does not set native suspension travel. | `.65`; Minimum: .01f |
| `chassisAnchor` | `Transform` | Upper/fixed shock attachment on the chassis. Together with Wheel Anchor it determines the shock's length and direction. | `None / unassigned` |
| `damper` | `float` | Shock damping in N·s/m when overriding wheel physics. Increase to reduce suspension oscillation; Motion Ratio squared scales the effective wheel damping. | `2295`; Minimum: 0 |
| `localLengthAxis` | `Vector3` | Axis running lengthwise through the shock casing and piston in the mesh's own coordinates. The placement helper aligns this axis with the line between the attachments. | `Vector3.up` |
| `maximumLength` | `float` | Upper attachment distance in metres used for the shock's travel warning. Set it to the shock's fully extended length; it does not stretch the casing/piston meshes. | `1.25`; Minimum: .01f |
| `meshLength` | `float` | Original length in metres of the shock casing and piston along its length axis before scaling. The placement helper uses it to fit the model between its calculated endpoints; use the actual mesh length to avoid stretching errors. | `2`; Minimum: .001f |
| `minimumLength` | `float` | Lower shock attachment distance in metres used to flag an out-of-travel setup. The guide turns red outside the range; this does not replace native wheel suspension stops. | `.7`; Minimum: .01f |
| `motionRatio` | `float` | Shock travel / wheel travel. Wheel-equivalent spring and damping scale with this ratio squared. | `1`; Range: .01f to 1 |
| `overrideWheelPhysics` | `bool` | Overrides this wheel's native spring, damper and travel through the UVS Suspension module. Use one active override per wheel. | `false` |
| `piston` | `Transform` | Inner sliding rod mesh. It follows Wheel Anchor, overlapping the casing as the shock compresses; the rod is not stretched to simulate travel. | `None / unassigned` |
| `pistonLength` | `float` | Visible inner rod length in metres. Sets how far the fixed-length piston extends back from Wheel Anchor into the casing. | `.65`; Minimum: .01f |
| `rotationOffset` | `Vector3` | Orientation correction in degrees relative to Chassis Anchor. Use it to align the shock model's axes with the line between the attachments. | `Zero-initialized Vector3` |
| `showGizmos` | `bool` | Shows attachment points and shock travel limits guides in the Scene view for setup. It does not enable physics, move the vehicle or change the visible game model. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `spring` | `float` | Shock stiffness in N/m when Override Wheel Physics is enabled. Higher values resist compression more; Motion Ratio squared converts it to the wheel's effective spring strength. | `26250`; Minimum: 1 |
| `suspensionTravel` | `float` | Suspension travel in metres represented by this shock. | `.65`; Minimum: .001f |
| `targetPosition` | `float` | Normalized suspension rest position represented by the shock. | `.5`; Range: 0 to 1 |
| `wheel` | `WheelCollider` | Wheel collider receiving this shock's optional spring, damper and travel override. Without Override Native Suspension, the reference alone does not replace its suspension tuning. | `None / unassigned` |
| `wheelAnchor` | `Transform` | Moving shock attachment on the wheel or suspension arm. The piston follows this point as the suspension compresses and extends. | `None / unassigned` |

## SpaceshipProfile

### Methods

**Source:** `Runtime/Drive/Profiles/SpaceshipProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [FreeProfile](Drive.md#freeprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `alignFlightPath` | `bool` | Use powered steering thrusters to remove sideways and opposing motion while forward/backward thrust is requested. Coasting and explicit strafe/lift input remain independent. Does not rotate the hull. | `true` |
| `angularRates` | `Vector3` | Maximum local pitch, yaw and roll rates in degrees per second. | `new Vector3(42, 55, 75)` |
| `angularResponse` | `float` | Rotational thruster response toward commanded angular rates. Uncommanded axes retain spin unless Stop Rotation On Release is enabled. | `5`; Minimum: 0 |
| `bankTurnAcceleration` | `float` | Maximum horizontal turning acceleration at 90 degrees of bank, in m/s². Requires forward motion; does not create vertical lift. | `14`; Minimum: 0 |
| `bankTurnCoordination` | `float` | Response for smoothly acquiring the bank-induced turn rate, in inverse seconds. Zero leaves coordination to the pilot. Manual pitch, yaw or roll suspends nose coordination; strafe, lift and braking suspend all bank-turn assistance. | `5`; Minimum: 0 |
| `bankTurnEnabled` | `bool` | Use steering thrusters to curve horizontal travel with bank and coordinate the nose with the path. Configurable flight assistance, not aerodynamic lift in vacuum. | `false` |
| `brakeAcceleration` | `float` | Powered braking acceleration opposing current world velocity, in m/s². | `15`; Minimum: 0 |
| `compensateGravity` | `bool` | Cancel native gravity while this profile is active, including with ignition off. Explicit Release All Forces also releases this compensation. | `true` |
| `flightPathTurnRate` | `float` | Powered flight-path alignment response, expressed in degrees per second. Higher values remove unwanted momentum faster; correction eases smoothly toward the requested forward/backward path. | `360`; Minimum: 0 |
| `liftAcceleration` | `float` | Up/down acceleration relative to the spacecraft, in m/s². | `8`; Minimum: 0 |
| `maximumAngularAcceleration` | `float` | Maximum angular correction in rad/s². Does not restrict native collision impulses. | `12`; Minimum: 0 |
| `maximumFlightPathAcceleration` | `float` | Maximum acceleration used to redirect the flight path, in m/s². | `100`; Minimum: 0 |
| `stopRotationOnRelease` | `bool` | Use rotational thrusters to stop spin after releasing rotation controls. Off retains angular momentum in vacuum. | `true` |
| `strafeAcceleration` | `float` | Sideways acceleration relative to the spacecraft, in m/s². | `8`; Minimum: 0 |

## Steering

Configuration/implementation type for steering within engine and drivetrain.

**Source:** `Runtime/Drive/Steering/Steering.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `ackermann` | `float` | Blend toward Ackermann inner/outer wheel steering geometry; zero uses parallel steering. | `1`; Range: 0 to 1 |
| `advancedSteeringGeometry` | `bool` | Optional radius/grip limits and Ackermann geometry. Off uses the configured steering angle directly. | `false` |
| `arcadeHandling` | `bool` | Game-oriented yaw and lateral grip assistance while tires touch the ground. | `true` |
| `arcadeLateralAcceleration` | `float` | Maximum sideways correction in m/s² used by arcade handling to oppose unwanted lateral motion. Increase for stronger slide correction; reduce for freer drifting. | `35`; Minimum: 1 |
| `assistanceStrength` | `float` | Overall strength of the optional yaw/lateral steering assistance. | `.72`; Range: 0 to 1 |
| `highSpeedAngleRatio` | `float` | Fraction of the normal steering angle retained at high speed. At 0.3 the high-speed limit is 30% of full lock, making sudden high-speed turns less sharp. | `0.3`; Range: 0.1f to 1 |
| `lateralResponse` | `float` | How strongly arcade assistance removes unwanted sideways velocity. Increase for a grippier assisted feel; reduce to let the chassis slide longer. | `4`; Minimum: 0 |
| `maximumLateralAcceleration` | `float` | Steering authority at speed is limited to this requested lateral acceleration (m/s²). | `6`; Minimum: .1f |
| `maximumYawRate` | `float` | Maximum target rotation speed for arcade turning assistance, in radians per second. Reduce to make assisted turns less abrupt. | `1.1`; Minimum: .1f |
| `minimumTurnRadius` | `float` | Minimum rear-axle centre turning radius in metres; zero disables the low-speed radius cap. | `6`; Minimum: 0 |
| `speedSensitiveSteering` | `bool` | Optional reduction of steering angle with speed. Off preserves full steering authority. | `false` |
| `stabilizePoweredSlides` | `bool` | Keep a powered full-lock slide near its entry speed instead of accelerating into an expanding circle. | `true` |
| `useGroundGripLimit` | `bool` | Further limits the requested wheel angle to what the sampled ground grip can support. This reduces steering demands that would immediately make the tires slide; handbrake turns bypass it. | `true` |
| `yawResponse` | `float` | How strongly arcade assistance corrects the difference between actual and requested turning rate. Increase for quicker assisted rotation, while Maximum Yaw Rate still caps the target. | `7.5`; Minimum: 0 |

## SteeringTieRod

`Tracks` steering-link endpoints and geometry.

**Source:** `Runtime/Drive/Suspension/SteeringTieRod.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `knuckle` | `Transform` | Moving wheel carrier turned by the tie rod. Its pose drives the visible wheel and the steering-arm attachment. | `None / unassigned` |
| `localLengthAxis` | `Vector3` | Axis running lengthwise through the tie-rod mesh in the mesh's own coordinates. The placement helper aligns this axis with the line between the attachments. | `Vector3.up` |
| `maximumRackTravel` | `float` | Maximum rack displacement in metres to either side of Rack Reference. Increase for more available steering travel; total travel is twice this value. | `.25`; Minimum: 0 |
| `maximumSteeringAngle` | `float` | Maximum knuckle turn in degrees to either side. Both the requested and solved wheel angle are restricted to this range. | `40`; Range: 1 to 80 |
| `meshLength` | `float` | Original length in metres of the tie-rod mesh along its length axis before scaling. The placement helper uses it to fit the model between its calculated endpoints; use the actual mesh length to avoid stretching errors. | `2`; Minimum: .001f |
| `previewSteeringAngle` | `float` | Steering demand in degrees used to preview the linkage in Edit Mode. During play the native wheel's steer angle is used instead. | `0`; Range: -80 to 80 |
| `rackEnd` | `Transform` | Moving end of the steering rack. It slides along Rack Local Axis, limited by Maximum Rack Travel, and forms one end of the tie rod. | `None / unassigned` |
| `rackLocalAxis` | `Vector3` | Direction the rack slides, expressed in Rack Reference's local axes. Normally its local X axis; changing it rotates the rack's line of travel. | `Vector3.right` |
| `rackReference` | `Transform` | Fixed reference for the steering rack's centred position and local movement axis. Keep it separate from the moving Rack End. | `None / unassigned` |
| `rod` | `Transform` | Tie-rod mesh placed between Rack End and Steering Arm Anchor. If empty, this component's transform is used for the rod visual. | `None / unassigned` |
| `rodArticulation` | `SuspensionRotationLimits` ([fields](Drive.md#suspensionrotationlimits)) | Rod swivel permissions relative to the rack frame, with its mesh axis pointing across the chassis. | `new SuspensionRotationLimits()` |
| `rodLength` | `float` | Physical length in metres used to solve the fixed-length tie rod. A mismatched length can make parts of the requested steering range unreachable. | `1.2`; Minimum: .01f |
| `showGizmos` | `bool` | Shows rack travel and tie-rod reachability guides in the Scene view for setup. It does not enable physics, move the vehicle or change the visible game model. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `steeringArmAnchor` | `Transform` | Tie-rod attachment on the steering knuckle. Its offset from the steering pivot determines the leverage and angle produced by rack movement. | `None / unassigned` |
| `steeringLever` | `Transform` | Optional steering-arm mesh placed between the knuckle and Steering Arm Anchor so it follows the solved steering geometry. | `None / unassigned` |
| `steeringPivot` | `Transform` | Independent kingpin anchor on the suspension carrier. Keep it outside the steered knuckle hierarchy. | `None / unassigned` |
| `steeringRotation` | `SuspensionRotationLimits` ([fields](Drive.md#suspensionrotationlimits)) | Knuckle rotation permissions in the native wheel frame. Native steering uses local Y. | `new SuspensionRotationLimits()` |
| `wheel` | `WheelCollider` | Native wheel whose steer angle is solved from the rack and tie-rod geometry. This also keeps physical tire contact aligned with the visible knuckle. | `None / unassigned` |
| `wheelCenterOffset` | `Vector3` | Neutral wheel centre relative to the steering pivot, in the native wheel frame (metres). | `Zero-initialized Vector3` |

## SubmarineProfile

Consumes water state for underwater movement.

**Source:** `Runtime/Drive/Profiles/SubmarineProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [FreeProfile](Drive.md#freeprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `holdDepth` | `bool` | Hold the current world height after releasing ascend/dive controls. Requires propulsion power; disable for passive vertical drift. | `true` |
| `hullHalfHeight` | `float` | Half of the hull vertical extent in metres, used to blend buoyancy and underwater forces as the hull crosses the water surface. | `1.5`; Minimum: .1f |
| `lateralResistance` | `float` | Water-relative lateral velocity damping. Higher values reduce sideways underwater drift. | `1.8`; Minimum: 0 |
| `levelingStrength` | `float` | Restoring angular acceleration toward the submarine pitch/roll target. Higher values recover the desired attitude more strongly. | `4`; Minimum: 0 |
| `maximumPitch` | `float` | Maximum target pitch in degrees while ascending or diving under power. | `18`; Range: 0 to 40 |
| `quadraticResistance` | `float` | Additional water resistance proportional to speed squared. Increases drag at high underwater speeds. | `.025`; Minimum: 0 |
| `turnResponse` | `float` | Response of underwater yaw-rate tracking. Higher values accelerate into or out of a turn more quickly. | `2`; Minimum: 0 |
| `verticalAcceleration` | `float` | Maximum powered ascend/dive acceleration in metres per second squared before immersion and propulsion scaling. | `2`; Minimum: 0 |
| `verticalResistance` | `float` | Water-relative vertical velocity damping. Higher values resist ascent and descent more strongly. | `2`; Minimum: 0 |
| `waterCenter` | `Vector2` | World-space X/Z center of the rectangular fallback water region. | `new Vector2(-280, 80)` |
| `waterLevel` | `float` | World-space height in metres of the flat fallback water surface. | `2.3` |
| `waterSize` | `Vector2` | Width and length of the fallback water region in metres. A nonpositive dimension selects an infinite water plane. | `new Vector2(400, 640)` |
| `yawRate` | `float` | Maximum commanded underwater yaw rate in radians per second. | `.42`; Minimum: 0 |

## Suspension

Configures native wheel support and suspension-related response.

**Source:** `Runtime/Drive/Suspension/Suspension.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `allowLandingRebound` | `bool` | Temporarily release the expansion limiter during landing response, allowing the springs to push the chassis back upward. | `true` |
| `arcadeBumpDamping` | `bool` | Game-oriented damping of excessive upward body motion while most wheels remain supported. | `false` |
| `automaticForceApplication` | `bool` | Calculates wheel force application points from the chassis centre of mass instead of the manual height. It changes how tire forces roll/pitch the body, not the wheel mount or suspension travel. | `true` |
| `bodySwayTravelRatio` | `float` | Additional force lever arm as a fraction of suspension travel, allowing body pitch and roll. | `.24`; Range: 0 to 1 |
| `bumpDampingResponse` | `float` | Strength of the extra correction that removes excessive upward chassis speed after a bump. Higher values settle the body faster when Bump Damping is enabled; zero removes this correction. | `10`; Minimum: 0 |
| `damper` | `float` | Native suspension damping in N·s/m. Increase to reduce repeated bouncing after a bump; too much can make the wheel slow to follow road changes. | `2652`; Minimum: 0 |
| `damperBlowoffSpeed` | `float` | Suspension stroke speed in m/s where degressive damping begins limiting the force increase. Lower values soften fast bumps sooner; higher values retain stronger damping through faster strokes. | `.75`; Minimum: .05f |
| `degressiveDamping` | `bool` | Reduces the damper's growth at fast suspension strokes while retaining damping for slower body motion. Enable to soften sharp bumps without making the chassis float after them. | `true` |
| `directionalLandingBounce` | `bool` | Apply landing rebound at the supporting wheels rather than only the centre of mass, allowing directional pitch and roll on angled landings. | `true` |
| `directionalLandingResponse` | `bool` | Retain the approach speed while airborne so an angled chassis touch cannot instantly cancel the following wheel compression response. Assisted bounce energy still uses actual wheel contact speed. | `true` |
| `forceApplicationHeight` | `float` | Manual wheel-force application distance in metres above the tire's base at rest. Used when Automatic Force Application is off; changing it changes the lever arm that pitches/rolls the chassis. | `0.15`; Minimum: 0 |
| `forceOffsetBelowCenterOfMass` | `float` | Metres below the centre of mass used for automatic force application. Increasing the separation changes the tire-force lever arm and the body's roll/pitch response. | `.3`; Minimum: .05f |
| `landingAngularBrakingTime` | `float` | Near the support plane, reduce the allowed approach speed using the remaining tilt divided by this time in seconds. Zero disables this final braking zone. | `.06`; Minimum: 0 |
| `landingAngularContactGrace` | `float` | Seconds to fade angular touchdown damping after every wheel ray finds support, allowing the last axle to compress before assistance ends. Zero ends it immediately at full ray contact. | `.12`; Minimum: 0 |
| `landingAngularDamping` | `float` | Angular damping rate in 1/s during partial wheel touchdown. With the speed limit enabled, only rotation above the allowed approach speed is damped. | `26`; Minimum: 0 |
| `landingAngularMaximumDeceleration` | `float` | Maximum requested relative angular deceleration during partial touchdown, in degrees/s squared. | `3600`; Minimum: 0 |
| `landingAngularMaximumSpeed` | `float` | Soft maximum relative approach rotation in degrees/s during angled touchdown. Faster rotation is progressively damped rather than clamped. | `60`; Minimum: 0 |
| `landingAngularSpeedLimit` | `bool` | Only brake excessive rotation toward the support plane. Ordinary axle descent remains free; disable to restore continuous angular damping. | `true` |
| `landingBounceMaximumCount` | `int` | Maximum assisted bounce count in legacy mode. Progressive mode assists only the first release; later oscillations use native springs and dampers. | `3`; Range: 1 to 5 |
| `landingBounceMaximumRotation` | `float` | Maximum angular speed change from an assisted landing rebound in degrees/s. Bounds partial-wheel leverage without clamping native collision rotation. | `35`; Minimum: 0 |
| `landingBounceMaximumSpeed` | `float` | Upper limit on requested upward speed remaining after the tires clear full suspension travel, relative to the landing surface, in m/s. The push also accounts for the travel still to extend. | `2`; Minimum: 0 |
| `landingBounceMaximumTilt` | `float` | Maximum gravity-relative chassis tilt in degrees for assisted wheel rebound. Side and roof landings remain passive. | `55`; Range: 0 to 70 |
| `landingBounceRestitution` | `float` | Fraction of incoming landing speed retained for the next airborne bounce. Each subsequent bounce retains only this fraction again. | `.45`; Range: 0 to .8f |
| `landingBumpStopMultiplier` | `float` | Progressive end-of-travel spring stiffness relative to the authored spring during landing. Prevents a soft initial stroke from losing its energy against the hard travel stop. | `1.5`; Range: 1 to 3 |
| `landingContactLeverage` | `float` | Blend the rebound application point from the centre of mass to the average supporting wheel contact. Higher values produce more pitch/roll from partial axle support. | `.75`; Range: 0 to 1 |
| `landingDamperMultiplier` | `float` | Fraction of the normal damper retained at full landing response. Without Landing Ground Bounce, applies to compression only; extension retains normal damping. Lower values allow more body bounce. | `.2`; Range: .05f to 1 |
| `landingEventFullSpeed` | `float` | Surface-relative touchdown speed in m/s producing full LandingEvent intensity and landing event audio gain. Independent of physical landing assistance; minimum uses Landing Minimum Speed. | `15`; Minimum: .1f |
| `landingFullResponseSpeed` | `float` | Downward landing speed producing the full configured response, in m/s. | `4.5`; Minimum: .1f |
| `landingGroundBounce` | `bool` | Add a bounded elastic push during wheel rebound so the whole vehicle briefly leaves the ground. Only upright wheel landings after genuine flight can start it. Requires Landing Response. Enabled by default for grounded profiles. | `true` |
| `landingImpactCompressionSpeed` | `float` | Requested normal compression speed after a predicted hard touchdown, in m/s. Lower values give the suspension more time to compress. | `1.5`; Minimum: .1f |
| `landingImpactLeverage` | `float` | Impact impulse lever from chassis centre of mass to the weighted tire contacts. Lower values distribute more of the hard landing load through the chassis instead of instantly pitching it about the first axle. | `.15`; Range: 0 to 1 |
| `landingImpactMinimumSpeed` | `float` | Minimum genuine airborne approach speed toward the contacted surface in m/s that arms predictive impact absorption. Includes horizontal flight into slopes. Lower-speed landings retain the normal spring response. | `8`; Minimum: 0 |
| `landingImpactReserveTravel` | `float` | Fraction of suspension travel reserved before the rigid compression stop. Protects against crossing the full stroke in one physics step. | `.15`; Range: 0 to .5f |
| `landingMinimumAirTime` | `float` | Minimum continuous time without wheel support before a landing can activate the response, in seconds. | `.15`; Minimum: 0 |
| `landingMinimumCycles` | `float` | Natural suspension cycles allowed at full landing strength. Weaker impacts use fewer cycles and recover sooner. Uses the configured wheel springs and chassis mass. Zero keeps the speed-scaled fixed-duration response. | `2.5`; Minimum: 0 |
| `landingMinimumSpeed` | `float` | Minimum downward contact speed relative to the landing surface, in m/s. | `1.5`; Minimum: 0 |
| `landingResponse` | `bool` | Temporarily soften springs and damping after a genuine airborne wheel landing, allowing compression, rebound and a gradual settling of the chassis. | `true` |
| `landingResponseDuration` | `float` | Full-strength landing recovery time in seconds. Weaker impacts recover sooner. The spring period and Minimum Landing Cycles can extend it for softer/heavier vehicles. | `.9`; Minimum: .05f |
| `landingSettlingDampingRatio` | `float` | Target damping ratio while progressive landing oscillations settle. 1 is critical damping, smaller values allow natural decaying oscillation. Never increases authored damping; normal settings return after the suspension becomes quiet. | `.25`; Range: .05f to 1 |
| `landingSpringMultiplier` | `float` | Fraction of authored spring stiffness retained at full landing response. Temporarily softens every wheel, including shock overrides, then smoothly restores its original stiffness. | `.6`; Range: .25f to 1 |
| `limitExpansionVelocity` | `bool` | Enables the native limit on how rapidly suspension can extend. This helps avoid an unloaded spring snapping the wheel downward too quickly. | `true` |
| `predictiveLandingCompression` | `bool` | Predict tire contact within the next physics step and absorb excessive approach speed before suspension hard-stop correction can flatten or displace the chassis. Requires Landing Response. Does not change the body pose. | `true` |
| `progressiveAngularLanding` | `bool` | Dissipate chassis rotation toward the support plane while only some wheels have landed after genuine flight. Uses torque, leaving yaw and rotation away from the ground free. Requires Landing Response. | `true` |
| `progressiveLandingBounce` | `bool` | Release landing rebound progressively through the loaded spring stroke instead of one impulse. Disable to use the previous landing bounce. | `true` |
| `progressiveLandingRecovery` | `float` | Recovery duration multiplier with progressive landing bounce. Lower values restore normal damping sooner after the initial rebound. | `.5`; Range: .1f to 1 |
| `showGizmos` | `bool` | Preview wheel spring travel, rest position for the selected vehicle. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `spring` | `float` | Native wheel suspension spring stiffness in N/m. Increase to support more weight with less compression; decrease for softer suspension. Reapply configuration after editing. | `35250`; Minimum: 1 |
| `supportedRiseSpeed` | `float` | Upward body speed in m/s allowed before optional arcade bump damping acts while most wheels are supported. | `.75`; Minimum: .1f |
| `targetPosition` | `float` | Normalized spring target within suspension travel: zero at full extension and one at full compression. | `0.5`; Range: 0 to 1 |
| `wheelDampingRate` | `float` | Native resistance to each wheel's rotation. Increase to make free wheel spin decay faster; too much also resists rolling. | `.02`; Minimum: 0 |
| `wheelSubstepsAboveThreshold` | `int` | Native suspension/tire force substeps above the speed threshold. Lower counts trade contact stability for less simulation work. Apply configuration after editing. Default 15. | `15`; Range: 1 to 32 |
| `wheelSubstepsBelowThreshold` | `int` | Native suspension/tire force substeps below the speed threshold. Lower counts reduce simulation work but can increase jitter or reduce contact stability. Apply configuration after editing. Default 12. | `12`; Range: 1 to 32 |
| `wheelSubstepSpeedThreshold` | `float` | Vehicle speed threshold in m/s for choosing native WheelCollider substep counts. Applies to the whole vehicle, not separate wheels. Apply configuration after editing. Default 5 m/s. | `5`; Minimum: 0 |

## SuspensionAxle

Configuration/implementation type for suspension axle within suspension and linkage.

**Source:** `Runtime/Drive/Suspension/SuspensionAxle.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `articulation` | `SuspensionRotationLimits` ([fields](Drive.md#suspensionrotationlimits)) | Local rotation axes and angle limits allowed for the axle housing relative to the neutral mesh frame. Restrict only impossible swivel directions; the attachments still determine the requested pose. | `new SuspensionRotationLimits()` |
| `housing` | `Transform` | Axle housing mesh aligned between Left Anchor and Right Anchor. If empty, this component's transform is used. This visual linkage adds no tire forces. | `None / unassigned` |
| `leftAnchor` | `Transform` | Non-spinning attachment at the left hub. The axle housing is placed along the line from this point to Right Anchor. | `None / unassigned` |
| `localLengthAxis` | `Vector3` | Axis running lengthwise through the axle housing in the mesh's own coordinates. The placement helper aligns this axis with the line between the attachments. | `Vector3.up` |
| `meshLength` | `float` | Original length in metres of the axle housing along its length axis before scaling. The placement helper uses it to fit the model between its calculated endpoints; use the actual mesh length to avoid stretching errors. | `2`; Minimum: .001f |
| `rightAnchor` | `Transform` | Non-spinning attachment at the right hub. Moving either anchor changes the visible axle housing's position, angle and length. | `None / unassigned` |
| `rotationOffset` | `Vector3` | Mesh alignment correction in degrees relative to Left Anchor. Use it to match the housing model's axes to the axle direction. | `Zero-initialized Vector3` |
| `showGizmos` | `bool` | Shows axle attachment points guides in the Scene view for setup. It does not enable physics, move the vehicle or change the visible game model. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |

## SuspensionHub

Provides hub/kingpin geometry for the wheel assembly.

**Source:** `Runtime/Drive/Suspension/SuspensionHub.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `followSteering` | `bool` | Also turns the hub with the wheel's steer angle. Turn off for a carrier that should move with suspension but remain unsteered. | `true` |
| `positionOffset` | `Vector3` | Offset in metres from the solved hub position, in the hub-follow frame's axes. Use it to align the carrier model without moving the collider. | `Zero-initialized Vector3` |
| `rotationLimits` | `SuspensionRotationLimits` ([fields](Drive.md#suspensionrotationlimits)) | Rotation axes and angle stops allowed for this visible hub relative to its neutral pose. Disable unwanted axes to prevent the carrier following inappropriate rotations. | `new SuspensionRotationLimits()` |
| `rotationOffset` | `Vector3` | Mesh alignment correction in degrees added to the hub-follow orientation. It changes the visible carrier's pose, not the native wheel's steering demand. | `Zero-initialized Vector3` |
| `showGizmos` | `bool` | Shows hub position and orientation guides in the Scene view for setup. It does not enable physics, move the vehicle or change the visible game model. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `steeringLinkage` | `SteeringTieRod` ([fields](Drive.md#steeringtierod)) | Optional tie rod used to remove the wheel centre's steering arc from the carrier position. Use it for an unsteered suspension carrier behind a separate steering knuckle. | `None / unassigned` |
| `wheel` | `WheelCollider` | Wheel collider providing suspension position for this hub. The hub follows its solved travel without inheriting tire spin. | `None / unassigned` |
| `wheelAdapter` | `Wheel` ([fields](Physics.md#wheel)) | Optional UVS wheel: follows its smoothed visual position after Wheel.LateUpdate. | `None / unassigned` |

## SuspensionRotationLimits

Configuration/implementation type for suspension rotation limits within suspension and linkage.

**Source:** `Runtime/Drive/Suspension/SuspensionRotationLimits.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `allowedAxes` | `SuspensionRotationAxes` | Axes allowed to rotate away from the linkage's neutral orientation. An unchecked axis stays at its neutral angle; combine axes to permit multi-axis articulation. Options: `None`, `X`, `Y`, `Z`, `All`. Multiple flags can be combined. | `SuspensionRotationAxes.All` |
| `limitAngles` | `bool` | Restricts each permitted rotation axis to Minimum Angles and Maximum Angles. When off, permitted axes can use their full solved rotation. | `false` |
| `maximumAngles` | `Vector3` | Highest rotation in degrees on each local X, Y and Z axis relative to the neutral pose. Tighten these bounds to stop a visible linkage from rotating too far. | `new Vector3(180, 180, 180)` |
| `minimumAngles` | `Vector3` | Lowest rotation in degrees on each local X, Y and Z axis relative to the neutral pose. Used only when Limit Angles is enabled. | `new Vector3(-180, -180, -180)` |

## TrackedProfile

Maps tracked propulsion/turning intent into movement behavior.

**Source:** `Runtime/Drive/Profiles/TrackedProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [DriveProfile](Drive.md#driveprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `insideTrackSpeedRatio` | `float` | Inside belt target speed relative to the outside belt during a moving turn. | `0.2`; Range: .05f to 1 |
| `lateralGrip` | `float` | Lateral tire grip relative to ordinary tires, allowing the road wheels to skid sideways during turns. | `0.2`; Range: .05f to 1 |
| `lateralStability` | `float` | Grounded chassis lateral-velocity damping per second. Keeps the hull following its heading while road wheels scrub during turns. Zero disables it. | `5`; Minimum: 0 |
| `lowSpeedTurnGrip` | `float` | Lateral grip during a powered brake-steer launch. Blends to Lateral Grip between 1 and 4 m/s; use the same value to disable the release. | `0.01`; Range: 0 to 1 |
| `maximumLateralStabilityAcceleration` | `float` | Maximum lateral stability acceleration in m/s², additionally limited by tire contact load and surface grip. | `6`; Minimum: 0 |
| `pivotTrackSpeed` | `float` | Equal and opposite belt speed during a stationary turn, in m/s at full steering. | `1.5`; Speed field; stored in m/s, displayed in the selected speed unit |
| `pivotTransitionTime` | `float` | Seconds spent blending into or out of turning on the spot. Increase for a gentler change between rolling turns and opposite track rotation. | `0.3`; Minimum: .01f |
| `redistributeSteeringTorque` | `bool` | Route unused inside-track drive torque to the outside track within the existing engine torque and power limits. | `true` |
| `steeringBrakeTorque` | `float` | Maximum per-wheel braking for inside belt speed regulation; shared service/parking brakes take priority. | `25000`; Minimum: 0 |
| `steeringMix` | `float` | Steering strength applied to the configured inside-track speed reduction. | `1`; Range: 0 to 1 |
| `trackSpeedResponse` | `float` | How quickly track speed approaches its requested value. Higher values make track acceleration and steering speed changes more immediate. | `2`; Minimum: .1f |
| `turnSpeedCompensation` | `float` | Speed compensation during moving turns: accelerates the outside belt to preserve the mean belt-speed target. Zero uses brake-steer speed loss. | `1`; Range: 0 to 1 |

## Tracks

Owns explicit side membership and tracked support policy.

**Source:** `Runtime/Drive/Grounded/Tracks.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `leftWheels` | `WheelCollider[]` | Wheel colliders belonging to the left track. Steering applies the left track's drive/brake demand to this group; use explicit groups when automatic side detection is unsuitable. | `Empty list` |
| `rightWheels` | `WheelCollider[]` | Wheel colliders belonging to the right track. Steering varies this group's drive/brake demand against the left track to turn or pivot the vehicle. | `Empty list` |

## WheeledProfile

Reusable wheeled strategy used by the inheritance example.

**Source:** `Runtime/Drive/Profiles/WheeledProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [DriveProfile](Drive.md#driveprofile). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.
