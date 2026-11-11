# Drive profiles, steering and suspension

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [AerobaticAirplaneProfile](#aerobaticairplaneprofile) | 0 |
| [AirplaneGroundContact](#airplanegroundcontact) | 0 |
| [AirplaneProfile](#airplaneprofile) | 84 |
| [AirProfile](#airprofile) | 0 |
| [AntiRoll](#antiroll) | 2 |
| [AntiRoll.Axle](#antirollaxle) | 2 |
| [BoatProfile](#boatprofile) | 53 |
| [Brakes](#brakes) | 8 |
| [Burnout](#burnout) | 22 |
| [ContactEnvelope](#contactenvelope) | 14 |
| [ControlArm](#controlarm) | 22 |
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
| [JetProfile](#jetprofile) | 0 |
| [MotorcycleBalance](#motorcyclebalance) | 17 |
| [MotorcycleProfile](#motorcycleprofile) | 6 |
| [ParkingHold](#parkinghold) | 3 |
| [ProfileSwitcher](#profileswitcher) | 6 |
| [ProfileTransition](#profiletransition) | 5 |
| [ShockAbsorber](#shockabsorber) | 20 |
| [Steering](#steering) | 14 |
| [SteeringTieRod](#steeringtierod) | 19 |
| [SubmarineProfile](#submarineprofile) | 13 |
| [Suspension](#suspension) | 50 |
| [SuspensionAxle](#suspensionaxle) | 8 |
| [SuspensionHub](#suspensionhub) | 8 |
| [SuspensionRotationLimits](#suspensionrotationlimits) | 4 |
| [TrackedProfile](#trackedprofile) | 12 |
| [Tracks](#tracks) | 2 |
| [WheeledProfile](#wheeledprofile) | 0 |
| [SpaceshipProfile](#spaceshipprofile) | 18 |

## AerobaticAirplaneProfile

Defines body-rate airplane control without auto-leveling.

**Source:** `Runtime/Drive/Profiles/AerobaticAirplaneProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [AirplaneProfile](Drive.md#airplaneprofile). These settings also appear on this type.

Body-rate preset for the shared AirplaneProfile model. Its constructor selects BodyRates, disables bank compensation and sets Minimum Air Control Authority to 0.2, along with higher engine/thrust/speed defaults. No additional Inspector fields are declared here; edit the inherited settings. See [fixed-wing model selection](../Aircraft.md#one-configurable-fixed-wing-model).

## AirplaneGroundContact

`Tracks` ground support and ground/air authority blending.

**Source:** `Runtime/Drive/Air/AirplaneGroundContact.cs`. Component / asset.

**Inherited settings:** [PhysicsModule](Physics.md#physicsmodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## AirplaneProfile

Defines assisted airplane movement and aircraft configuration.

**Source:** `Runtime/Drive/Profiles/AirplaneProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [AirProfile](Drive.md#airprofile). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `airspeedControlAuthorityEnabled` | `bool` | Scale control torque with airspeed/attached flow. Disable to retain full commanded control authority at low speed. Enabled by default. | `true` |
| `allowGroundReverse` | `bool` | Enable powered reverse only on supported landing gear. Requires positive Ground Reverse Speed/Acceleration. | `false` |
| `angularDampingEnabled` | `bool` | Apply angular velocity damping inside profile attitude/rate control; disabling retains commanded control torque. Enabled by default. | `true` |
| `attitudeControlEnabled` | `bool` | Master switch for profile pitch/roll/yaw control torque; leaves aerodynamic forces active. Enabled by default. | `true` |
| `attitudeDamping` | `float` | Attitude damping. | `6`; Minimum: 0 |
| `attitudeSpringEnabled` | `bool` | AssistedAttitude mode: angle-to-target restoring torque, including pitch/roll input response. BodyRates uses rate control instead. Enabled by default. | `true` |
| `attitudeStrength` | `float` | Attitude strength. | `14`; Minimum: 0 |
| `bankCompensationEnabled` | `bool` | Simplified aerodynamics: increase lift to compensate for bank. Disabled by the Aerobatic/Jet preset constructors. Enabled by default. | `true` |
| `coordinatedTurn` | `float` | Coordinated turn. | `1.8`; Minimum: 0 |
| `coordinatedTurnEnabled` | `bool` | Add bank-derived automatic turn demand. BodyRates also requires Rate Coordinated Turn Enabled. Enabled by default. | `true` |
| `dragEnabled` | `bool` | Apply profile air resistance. In RelativeAirflow mode this also gates parasite, induced and pressure drag. Enabled by default. | `true` |
| `engineIdleRpm` | `float` | Engine idle rpm. | `700`; Minimum: 0 |
| `engineMaximumRpm` | `float` | Engine maximum rpm. | `2700`; Minimum: 1 |
| `enginePowerKw` | `float` | Engine power kw. | `180`; Minimum: 1 |
| `maximumThrustNewtons` | `float` | Full-spool static thrust in N, independent of mass. Positive overrides Ground Acceleration and Acceleration; zero retains them. Throttle/spool/envelope/power limits remain active. | `0`; Jet: `90000` |
| `enginePowerLimitEnabled` | `bool` | Limit thrust acceleration by engine power, speed and mass. Disabling retains throttle and spool response. Enabled by default. | `true` |
| `flightAlignmentEnabled` | `bool` | Apply flight-path alignment toward the airframe. In RelativeAirflow mode gates pitch/yaw crossflow correction, independently of lift trim. Enabled by default. | `true` |
| `flightPathResponse` | `float` | Flight path response. | `2`; Minimum: 0 |
| `flightTransitionTime` | `float` | Flight transition time. | `0.35`; Minimum: .01f |
| `groundAcceleration` | `float` | Ground acceleration. | `6`; Minimum: 0 |
| `groundFriction` | `float` | Hull-contact friction for wheel-free aircraft only. Gear tires use the shared Friction module. | `0.02`; Range: 0 to 1 |
| `groundHandlingAssistance` | `float` | Shared steering yaw and lateral grip assistance, only while tires touch the ground. | `0.3`; Range: 0 to 1 |
| `groundLateralResponse` | `float` | Ground lateral response. | `5`; Minimum: 0 |
| `groundReverseAcceleration` | `float` | Ground reverse acceleration. | `2`; Minimum: 0 |
| `groundReverseSpeed` | `float` | Ground-only reverse speed in m/s. Zero disables reverse thrust. | `3`; Speed field; stored in m/s, displayed in the selected speed unit |
| `groundRotationAuthority` | `float` | Ground rotation authority. | `0.7`; Range: 0 to 1 |
| `groundRotationEnabled` | `bool` | Allow pitch control for rotation while still grounded. Airborne pitch control remains independent. Enabled by default. | `true` |
| `groundSteeringAngle` | `float` | Ground steering angle. | `35`; Range: 1 to 60 |
| `groundSteeringRate` | `float` | Ground steering rate. | `75`; Minimum: 1 |
| `groundYawResponse` | `float` | Ground yaw response. | `4`; Minimum: 0 |
| `landingTransitionTime` | `float` | Landing transition time. | `0.08`; Minimum: .01f |
| `liftEnabled` | `bool` | Apply aerodynamic lift. Disabling does not remove gravity, drag or attitude control. Enabled by default. | `true` |
| `liftMultiplier` | `float` | Lift multiplier. | `1.12`; Range: 1 to 2 |
| `liftSpeed` | `float` | Minimum forward airspeed for ground rotation/takeoff, in m/s. | `18`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumAlignmentAcceleration` | `float` | Maximum alignment acceleration. | `18`; Minimum: 0 |
| `maximumBank` | `float` | Maximum bank. | `45`; Range: 5 to 85 |
| `maximumControlAcceleration` | `float` | Maximum control acceleration. | `20`; Minimum: .1f |
| `maximumGroundLateralAcceleration` | `float` | Maximum ground lateral acceleration. | `5`; Minimum: .1f |
| `maximumLiftAcceleration` | `float` | Maximum lift acceleration. | `35`; Minimum: 1 |
| `maximumPitch` | `float` | Pitch attitude limit in the assisted profile. Aerobatic profiles use angular rates instead. | `30`; Range: 5 to 85 |
| `maximumSpeed` | `float` | Forward airspeed limit in m/s. Thrust fades out near this speed. | `65`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumTurnRate` | `float` | Maximum turn rate. | `70`; Minimum: 1 |
| `minimumGroundTurnRadius` | `float` | Minimum ground turn radius. | `6`; Minimum: 0 |
| `parkingBrakeTorque` | `float` | Parking brake torque. | `5000`; Minimum: 0 |
| `pitchControlEnabled` | `bool` | Allow profile control torque around the local pitch axis. Does not suppress aerodynamic torque from other systems. Enabled by default. | `true` |
| `propulsionEnabled` | `bool` | Apply engine/propeller thrust, including supported ground reverse. Engine and propeller presentation remain independent. Enabled by default. | `true` |
| `rollControlEnabled` | `bool` | Allow profile control torque around the local roll axis. Enabled by default. | `true` |
| `rudderEnabled` | `bool` | Allow commanded yaw/rudder input in profile attitude control. Enabled by default. | `true` |
| `rudderRate` | `float` | Rudder rate. | `35`; Minimum: 0 |
| `serviceBrakeTorque` | `float` | Service brake torque. | `3000`; Minimum: 0 |
| `speedLimiterEnabled` | `bool` | Fade thrust near configured forward/reverse speed limits; does not directly clamp Rigidbody velocity. Enabled by default. | `true` |
| `stallEnabled` | `bool` | Reduce lift/support near low airspeed; RelativeAirflow mode also reduces attached flow at excessive angle of attack. Disable for full aerodynamic support. Enabled by default. | `true` |
| `stallSpeedRatio` | `float` | Stall speed ratio. | `0.55`; Range: .1f to .95f |
| `suspensionDamper` | `float` | Suspension damper. | `1785`; Minimum: 0 |
| `suspensionSpring` | `float` | Suspension spring. | `24000`; Minimum: 1 |
| `suspensionTravel` | `float` | Suspension travel. | `0.18`; Minimum: .05f |
| `takeoffContactGrace` | `float` | Seconds without tire contact before entering flight. Touchdown is detected on the first tire contact. | `0.12`; Minimum: 0 |
| `tireGrip` | `float` | Tire grip. | `1.3`; Minimum: .1f |
| `useLandingGear` | `bool` | Keep native tires active in flight to detect touchdown without rebuilding wheel actors. Disable only for a wheel-free aircraft. | `true` |
| `yawControlEnabled` | `bool` | Allow profile control torque around the local yaw axis. Enabled by default. | `true` |

| `pitchRate` | `float` | `110`; Minimum: 1 | Pitch rate. |
| `rollRate` | `float` | `200`; Minimum: 1 | Roll rate. |
| `yawRate` | `float` | `45`; Minimum: 1 | Yaw rate. |
| `rateResponse` | `float` | `6`; Minimum: .1f | Rate response. |
| `minimumAirControlAuthority` | `float` | `0`; Range: 0 to 1 | Optional low-speed / thrust-vectoring control assistance. Zero requires airflow; higher values allow fighter-style recovery near a stall. |
| `parasiteDragEnabled` | `bool` | `true` | Allow forward-speed parasite drag when the inherited Drag Enabled master is on. Enabled by default. |
| `inducedDragEnabled` | `bool` | `true` | Allow aerodynamic-load induced drag when the inherited Drag Enabled master is on. Enabled by default. |
| `pressureDragEnabled` | `bool` | `true` | Allow crossflow pressure drag when the inherited Drag Enabled master is on. Enabled by default. |
| `sideForceEnabled` | `bool` | `true` | Allow sideways aerodynamic normal force; inherited Lift Enabled controls the lift-axis force. Enabled by default. |
| `gLimiterEnabled` | `bool` | `false` | Apply G-derived pitch-rate and aerodynamic normal-force limits. Other configured control-acceleration limits remain active. Disabled in the base preset; enabled by the Jet preset. |
| `parasiteDrag` | `float` | `0.00022`; Minimum: 0 | Forward parasite drag acceleration / speed squared, in 1/metres. |
| `wingPressureDrag` | `float` | `0.012`; Minimum: 0 | Additional quadratic pressure drag for airflow across the wings / across the fuselage. |
| `sidePressureDrag` | `float` | `0.008`; Minimum: 0 | Side pressure drag. |
| `inducedDrag` | `float` | `0.12`; Minimum: 0 | Induced drag acceleration at one G; grows with aerodynamic load squared. |
| `referenceAirspeed` | `float` | `100`; Speed field; stored in m/s, displayed in the selected speed unit | Reference airspeed. |
| `pitchPathResponse` | `float` | `5`; Minimum: .1f | Pitch path response. |
| `yawPathResponse` | `float` | `4`; Minimum: .1f | Yaw path response. |
| `maximumG` | `float` | `4.5`; Range: 1.1f to 9 | Maximum g. |
| `stallAngle` | `float` | `35`; Range: 10 to 60 | Stall angle. |
| `coordinatedTurnAssist` | `float` | `0.8`; Range: 0 to 1 | Coordinated turn assist. |
| `controlMode` | `AircraftControlMode` | `AssistedAttitude` | Assisted pitch/bank targets or unrestricted BodyRates; available on every fixed-wing preset. |
| `aerodynamics` | `AircraftAerodynamics` | `Simplified` | Simplified lift/alignment or RelativeAirflow forces; independent of Control Mode and preset class. |
| `progressiveThrustEnvelope` | `bool` | `false` | Use fourth-power thrust fade instead of linear fade near the speed limit. |
| `yawLimiterEnabled` | `bool` | `false` | Limit commanded yaw rate by airspeed and gravity. |
| `rateCoordinatedTurnEnabled` | `bool` | `false` | Permit bank-derived turn assistance in BodyRates; also requires Coordinated Turn Enabled. |

## AirProfile

Configuration/implementation type for air profile within movement strategies and transitions.

**Source:** `Runtime/Drive/Profiles/AirProfile.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [FreeProfile](Drive.md#freeprofile). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

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
| `buoyancyDepth` | `float` | Buoyancy depth. | `0.85`; Minimum: .1f |
| `buoyancyEnabled` | `bool` | Apply gravity-derived upward buoyancy. Vertical damping remains a separate force contribution. Enabled by default. | `true` |
| `forwardDragScale` | `float` | Scales the inherited Drag setting along the hull; lower values retain momentum longer. | `0.3`; Minimum: 0 |
| `forwardResistanceEnabled` | `bool` | Apply linear and speed-squared resistance along the hull. Enabled by default. | `true` |
| `idleWaveDegrees` | `float` | Occasional wave impulse strength. Zero disables these impulses independently of background sway. | `1.2`; Range: 0 to 3 |
| `idleWaveInterval` | `Vector2` | Random interval between occasional stronger wave impulses, seconds; also active while moving. | `new Vector2(8, 16)` |
| `lateralResistance` | `float` | Sideways resistance: lower values preserve sideways drift longer. | `1.8`; Minimum: 0 |
| `lateralResistanceEnabled` | `bool` | Apply sideways hull resistance and its forward-speed contribution. Enabled by default. | `true` |
| `loadedRockingDampingRatio` | `float` | Loaded rocking damping ratio. | `0.85`; Range: .1f to 1 |
| `maneuverRockingEnabled` | `bool` | Excite pitch/roll from measured hull acceleration; does not disable ambient waves or powered bow lift. Enabled by default. | `true` |
| `maximumHullTilt` | `float` | Maximum total assisted hull tilt in degrees; thrust fades above half this angle. | `35`; Range: 10 to 80 |
| `maximumManeuverTilt` | `float` | Maximum maneuver tilt. | `6`; Range: 0 to 20 |
| `maximumYawRate` | `float` | Upper requested yaw rate used by turning assistance, in rad/s. | `0.55`; Minimum: .1f |
| `pitchMotionEnabled` | `bool` | Allow all profile-generated hull pitch torque, including wave impulses. Does not freeze native Rigidbody rotation. Enabled by default. | `true` |
| `poweredPitchDegrees` | `float` | Sustained bow/stern lift at full propeller load, degrees; builds gradually with squared throttle demand and forward motion. | `5.5`; Range: 0 to 8 |
| `poweredPitchEnabled` | `bool` | Allow sustained throttle-induced bow/stern pitch. Disabling clears stored powered-pitch response. Enabled by default. | `true` |
| `poweredPitchReleaseTime` | `float` | Seconds for sustained lift to settle after releasing/reversing throttle. | `0.7`; Minimum: .1f |
| `poweredPitchRiseTime` | `float` | Seconds for sustained throttle lift to approach its target; longer values make the bow rise more gradually. | `1.2`; Minimum: .1f |
| `powerPitchBoost` | `float` | Power pitch boost. | `0.2`; Minimum: 0 |
| `propulsionEnabled` | `bool` | Allow throttle-driven hull thrust. Braking thrust is independent; engine ownership is unchanged. Enabled by default. | `true` |
| `rockingDamping` | `float` | Rocking damping. | `0.65`; Minimum: 0 |
| `rockingDampingEnabled` | `bool` | Apply passive pitch/roll damping, including propeller/low-speed pitch damping. Enabled by default. | `true` |
| `rockingMemorySeconds` | `float` | Rocking memory seconds. | `2.5`; Minimum: .1f |
| `rockingSpring` | `float` | Rocking spring. | `3.5`; Minimum: .1f |
| `rockingStrength` | `float` | Strength of maneuver, continuous water sway and wave rocking. Zero disables excitation while retaining upright stability and momentum. | `1`; Range: 0 to 2 |
| `rollMotionEnabled` | `bool` | Allow all profile-generated hull roll torque, including wave impulses. Does not freeze native Rigidbody rotation. Enabled by default. | `true` |
| `rudderEnabled` | `bool` | Apply steering-generated yaw torque while powered, independently of forward thrust. Enabled by default. | `true` |
| `speedLateralResistance` | `float` | Extra sideways grip per m/s of forward speed; keeps the hull tracking its heading under power. | `0.09`; Minimum: 0 |
| `speedResistance` | `float` | Speed resistance. | `0.006`; Minimum: 0 |
| `stationaryTurnAcceleration` | `float` | Stationary turn acceleration. | `0.12`; Minimum: 0 |
| `stationaryTurningEnabled` | `bool` | Allow the additional stationary turning authority; underway rudder authority remains bank-dependent. Enabled by default. | `true` |
| `stationaryYawRate` | `float` | Maximum requested low-speed boat yaw rate, in rad/s. | `0.18`; Minimum: .01f |
| `steeringReturnTime` | `float` | Steering return time. | `0.22`; Minimum: .01f |
| `steeringRiseTime` | `float` | Steering rise time. | `0.35`; Minimum: .01f |
| `steeringSmoothingEnabled` | `bool` | Smooth digital steering demand. Disable for immediate steering; analog input is already direct. Enabled by default. | `true` |
| `steeringYawResponse` | `float` | Rudder response to desired turn rate. Countersteering first arrests the current turn instead of building unchecked opposing torque. | `2.5`; Minimum: .1f |
| `tiltLimitEnabled` | `bool` | Assisted water hull tilt guard; requires upright stabilization and both attitude axes. | `true` |
| `uprightStabilizationEnabled` | `bool` | Apply the hull spring returning pitch/roll toward upright, independently of rocking excitation. Enabled by default. | `true` |
| `verticalDamping` | `float` | Vertical damping. | `1.8`; Minimum: 0 |
| `verticalDampingEnabled` | `bool` | Apply the vertical water-relative damping term inside the nonnegative buoyancy force. Enabled by default. | `true` |
| `waterCenter` | `Vector2` | Water center. | `new Vector2(-280, 80)` |
| `waterCurrentEnabled` | `bool` | Use provider water velocity for drag and vertical damping. Surface height still controls immersion. Enabled by default. | `true` |
| `waterLevel` | `float` | Flat fallback water-surface height in world metres. | `2.3` |
| `waterSize` | `Vector2` | Zero size means an infinite flat water plane. Otherwise bounds are world-space X/Z. | `new Vector2(400, 640)` |
| `waveImpulsesEnabled` | `bool` | Allow occasional wave torque impulses. Disabled timers reset to prevent a queued impulse on re-enable. Enabled by default. | `true` |
| `yawDampingEnabled` | `bool` | Apply passive damping around world up. Rudder response remains independent. Enabled by default. | `true` |
| `yawDampingScale` | `float` | Scales inherited Angular Damping for yaw; pitch/roll use Rocking Damping. | `0.22`; Minimum: 0 |

## Brakes

Configuration/implementation type for brakes within engine and drivetrain.

**Source:** `Runtime/Drive/Brakes/Brakes.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `brakeEventMinimumSpeedKph` | `float` | Minimum road speed for reporting service-braking activity. It filters brake events while stationary; it does not weaken the actual brakes. | `3`; Speed field; stored in km/h, displayed in the selected speed unit |
| `brakeEventThreshold` | `float` | Service-brake input above which a moving vehicle counts as braking for feedback events. Brake Event Minimum Speed must also be reached; this does not change physical brake strength. | `.1`; Range: 0 to 1 |
| `brakeRiseTime` | `float` | Seconds for a held digital brake to reach full service-brake strength. Zero is immediate. | `.5`; Minimum: 0 |
| `engine` | `Engine` ([fields](Engine.md#engine)) | Optional explicit link when engine and brakes live on different objects. | `None / unassigned` |
| `handbrakeTorque` | `float` | Braking torque in N·m applied to each handbrake-enabled wheel while the handbrake is held. Higher values lock those wheels more readily. | `6000`; Minimum: 0 |
| `progressiveDigitalBraking` | `bool` | Ramp button/keyboard service braking. Analog pedals always use their exact input strength. | `true` |
| `rollingBrakeTorque` | `float` | Optional constant brake torque while coasting. Zero allows natural downhill rolling. | `0`; Minimum: 0 |
| `slopeReverseReleaseGrace` | `float` | Seconds to recognize a fresh reverse press after releasing a stopped brake on a slope. Does not engage reverse from a continuously held brake. | `.3`; Minimum: 0 |

## Burnout

**Source:** `Runtime/Drive/Grounded/Burnout.cs`. Optional component; excluded from Full setup.

**Inherited settings:** [DriveModule](Drive.md#drivemodule).

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `suspensionKick` | `BurnoutSuspensionSettings` | Front/rear spring shift: Enabled, Front Lift, Rear Compression, Rise Time, Return Time, Maximum Tilt (20 degrees), Maximum Forward Activation Speed (5 m/s; reverse unrestricted). See [configuration](../DrivingActions.md#suspension-kick-and-departure-wheelspin). | Enabled; 0.035 m / 0.02 m; 0.15 / 0.9 s |
| `automaticThrottle` | `bool` | Supply a throttle request in the selected drive direction before brakes/gearbox/clutch while the held launch request is eligible. Default true. | `true` |
| `forceForwardDirection` | `bool` | Request forward drive during boost; disable to retain the selected direction. | `true` |
| `boatBowLiftDegrees` | `float` | Extra boat powered-pitch target degrees while Burnout is active; default 2, range 0–5; existing tilt/pitch guards remain. | `2` |
| `bypassStabilityControl` | `bool` | Temporarily skip Steering arcade yaw/lateral stabilization and slide speed hold during burnout. Default true; authored assist settings are preserved. | `true` |
| `bypassTractionControl` | `bool` | Let intentional wheelspin pass through the optional TCS while assistance is nonzero. Default true; normal TCS resumes after recovery. | `true` |
| `cooldown` | `float` | Seconds before starting another cycle after release/abort. Default 0.4. | `.4f` |
| `forwardGrip` | `float` | Driven tire longitudinal grip scale during wheelspin. Default 0.55, allowing forward motion while spinning. | `.55f` |
| `gripRecoveryTime` | `float` | Recovery interval after spin or release. Default 0.4 seconds. | `.4f` |
| `holdBrakeTorque` | `float` | Maximum per-wheel holding torque in N m before wheel brake multipliers. Default 8000. | `8000` |
| `holdDuration` | `float` | Seconds at full non-driven-wheel hold. Default 0.6. | `.6f` |
| `holdNonDrivenWheels` | `bool` | Optional non-driven-wheel brake hold; disabled by default so the vehicle moves during wheelspin. | `false` |
| `holdReleaseTime` | `float` | Seconds to smoothly release that hold. Default 0.4. | `.4f` |
| `maximumSpinSpeed` | `float` | Safety speed cutoff for wheelspin assistance, independent of sustained steering. Default 60 m/s (216 km/h). | `60` |
| `maximumStartSpeed` | `float` | Highest speed at which a new burnout may start. Default 40 m/s (144 km/h), including starts while already driving. | `40` |
| `minimumEndSpeed` | `float` | Minimum road speed in m/s required for timed recovery while held. Default 12 (43.2 km/h); zero uses duration alone. Clamped to maximumSpinSpeed. Key release always begins recovery immediately. | `12` |
| `sidewaysGrip` | `float` | Driven tire lateral grip scale during wheelspin. Default 0.4 for drifting and donuts; normal grip returns during recovery. | `.4f` |
| `spinDuration` | `float` | Minimum held wheelspin duration before recovery. Default 3 seconds; recovery also requires minimumEndSpeed and no sustained steering. | `3f` |
| `sustainSteeringThreshold` | `float` | Steering magnitude required to retain a held powered slide. Default 0.15. | `.15f` |
| `sustainWhileSteering` | `bool` | Hold wheelspin while steering beyond sustainSteeringThreshold, even after the duration and minimum end speed. Default true; releasing Ctrl or the safety cutoff still ends assistance. | `true` |
| `throttle` | `float` | Automatic forward pedal strength. Default 1; range 0.1 to 1. | `1` |
| `torqueMultiplier` | `float` | Maximum temporary combustion/direct torque and finite power/acceleration-cap multiplier. Default 2.5; minimum 1. | `2.5f` |
| `wheelSpeedMultiplier` | `float` | Bounded native wheel overspeed allowance during wheelspin. Default 1.5; range 1–2; prevents runaway wheel energy. | `1.5f` |

## ContactEnvelope

Samples tire-shaped support and adjusts effective native support radius.

**Source:** `Runtime/Drive/Suspension/ContactEnvelope.cs`. Component / asset.

Probe, idle, sleep, refinement and native-contact reuse controls are in the collapsible **Performance / Optimization** group in both the standalone and embedded module Inspector. The stationary checkbox defaults on; the original sleep-only gate is independent.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `edgeRefinementIterations` | `int` | Binary-search iterations at tread edges and height discontinuities. Fewer iterations reduce raycasts but approximate curbs/gaps more coarsely. Default 7 preserves existing precision. | `7`; Range: 0 to 10 |
| `groundLayers` | `LayerMask` | Layers sampled as rolling/supporting ground by this system. | `~0` |
| `longitudinalSamples` | `int` | Number of ground samples along the tire's rolling direction. More samples detect short steps more smoothly but require more ground queries; an odd count from 3 to 15 is used. | `9`; Range: 3 to 15 |
| `maximumLiftRadius` | `float` | Maximum upward support correction as a fraction of tire radius. At 0.8 the correction cannot exceed 80% of the radius. Reduce to limit how far edge samples can lift the wheel. | `.8`; Range: 0 to 1 |
| `minimumGroundNormal` | `float` | Minimum dot product between a sampled normal and vehicle up for that sample to count as supporting ground. | `.35`; Range: 0 to 1 |
| `optimizeWhenStationary` | `bool` | Enable additional probe throttling for awake stationary vehicles. Driving/steering/flight demand, movement, wake-up and mode or interval changes force a fresh sample. Sleeping Probe Interval remains independent. | `true` |
| `probeEveryFixedSteps` | `int` | Probe moving-vehicle ground every N fixed steps. Default 2 halves scheduled probe batches; while moving, corrections above 3% of tire radius still sample each tick; intermediate steps reuse support while suspension damping still advances. Use 1 for fast vehicles, sharp curbs or rapidly changing ground. Higher intervals can miss narrow obstacles or delay support changes. Vehicle Teleport forces a fresh sample. | `2`; Range: 1 to 8 |
| `reuseNativeGroundContact` | `bool` | Use the native wheel contact as a box-face hint, then certify the current plane with corner rays and a full overlap prism. An eligible default grid needs four rays instead of five; stale/unsupported hints, meshes, gaps, masks, curbs and overlaps retain fresh centre sampling. | `true` |
| `sleepingProbeInterval` | `float` | Seconds between probes while the Rigidbody sleeps with no throttle/steering request. Longer intervals reduce idle queries but delay terrain/support changes; zero probes every fixed step. Default 0.2 seconds. | `.2`; Minimum: 0 |
| `stationaryAngularSpeedThreshold` | `float` | Maximum angular speed considered stationary, in radians/s. Default 0.02 rad/s; includes rotation in place. | `.02` |
| `stationaryLinearSpeedThreshold` | `float` | Maximum total 3D speed considered stationary, in m/s. Uses VehicleController.IsMoving; default 0.05 m/s. | `.05` |
| `stationaryProbeEveryFixedSteps` | `int` | Stationary probe interval in fixed steps, clamped to 1–120 and never faster than the moving interval. Default 10 gives 0.2 s at a 0.02 s timestep; dynamic terrain/support changes can be detected later. | `10` |
| `tireHalfWidth` | `float` | Half of the tire sampling width in metres; per-wheel geometry can supply the actual width during configuration. | `.12`; Minimum: 0 |
| `widthSamples` | `int` | Number of sample strips across the tire width, from 1 to 3. More strips help detect support near tire edges but add ground queries. | `3`; Range: 1 to 3 |

## ControlArm

Resolves a visual control arm against its authored geometry.

**Source:** `Runtime/Drive/Suspension/ControlArm.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `armLength` | `float` | Distance from hinge centre to outer ball joint, in metres. Pivot local X points outward; local Z is the hinge axis. | `1.4`; Minimum: .01f |
| `constrainHubToArc` | `bool` | Constrains the hub to the fixed-length wishbone arc. Disable to follow native wheel travel without lateral track-width changes; the visual branches fit the attachment points. | `true` |
| `constrainNativeWheel` | `bool` | Allows the linkage to constrain the native wheel mount when Constrain Hub To Arc is enabled; turn off for a visual-only control arm. | `true` |
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

No additional Inspector settings are declared on this type.

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
| `releaseAllForcesOnIgnitionOff` | `bool` | Release profile forces and shared driving/stability assistance while an installed engine is off. Gravity, native contacts and passive wheel suspension remain; restarting clears only the automatic release. | `false` |
| `steeringSpeedLimitEnabled` | `bool` | Shared master for speed-sensitive and lateral-acceleration steering limits. Minimum turning radius and Ackermann geometry remain active. | `true`; Airplane/Aerobatic/Jet constructors set `false` |
| `speedSensitiveRotation` | `bool` | Enable per-axis speed response curves inherited by every profile. | `false` |
| `pitchRateBySpeed` | `AnimationCurve` | X: km/h. Y: axis response multiplier; yaw also scales steering. | Linear: (0, 1) to (300, 0.65) |
| `yawRateBySpeed` | `AnimationCurve` | X: km/h. Y: axis response multiplier; yaw also scales steering. | Linear: (0, 1) to (300, 0.65) |
| `rollRateBySpeed` | `AnimationCurve` | X: km/h. Y: axis response multiplier; yaw also scales steering. | Linear: (0, 1) to (300, 0.65) |
| `rotationReleaseDuration` | `float` | Approximate seconds to 95% released-control settling. Zero preserves handling; Space uses dedicated spin braking, aircraft use mode-specific handling. | `0`; Spaceship: `1.1`; Minimum: 0 |

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
| `lateralResponse` | `float` | Strength of stability assistance opposing sideways vehicle velocity. Increase to suppress slides sooner; reduce for a looser, more drift-friendly response. | `4`; Minimum: 0 |
| `launchReferenceSpeed` | `float` | Low-speed reference in m/s used to stabilize slip/traction calculations during launch. | `3`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumYawRate` | `float` | Maximum target turning rate for stability assistance, in radians per second. Lower values restrain fast rotation; higher values permit tighter, faster turns. | `1`; Minimum: .1f |
| `minimumTorqueScale` | `float` | Minimum fraction of requested engine torque retained by traction control. Lower values allow stronger power cuts during wheelspin; higher values keep more power available. | `.08`; Range: 0 to 1 |
| `recoveryRate` | `float` | Rate at which allowed drive torque recovers after excess slip subsides. | `1.8`; Minimum: 0 |
| `reductionRate` | `float` | Rate at which allowed drive torque decreases when wheel slip exceeds the target. | `12`; Minimum: 0 |
| `reserveGripForCornering` | `bool` | Tells traction control to leave some tire grip for turning instead of using it all for acceleration. Enable to reduce power-induced understeer or slides. | `false` |
| `stabilityControlEnabled` | `bool` | Enables Steering's assisted yaw and sideways-motion corrections. Turn off to let tire forces and driver input determine slides without those corrections. | `true` |
| `stabilityStrength` | `float` | Overall blend/strength of the stability corrections; zero removes this assistance contribution. | `.70`; Range: 0 to 1 |
| `stabilizePoweredSlides` | `bool` | Allows stability assistance to correct powered sliding instead of leaving it entirely to driver input. | `true` |
| `targetSlip` | `float` | Desired longitudinal slip magnitude while applying propulsion torque. | `.22`; Minimum: .01f |
| `tractionControlEnabled` | `bool` | Enables the TractionControl module through this shared assist panel. It reduces drive torque when driven wheels spin faster than their available grip permits. | `true` |
| `tractionReserve` | `float` | Fraction of estimated traction kept available when limiting drive torque. | `.9`; Range: .1f to 1 |
| `yawResponse` | `float` | Speed of stability assistance turning the chassis toward the requested yaw rate. Higher values correct heading errors faster; lower values let rotation build more freely. | `7`; Minimum: 0 |

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
| `attitudeStrength` | `float` | Attitude strength. | `18`; Minimum: 0 |
| `automaticLeveling` | `bool` | Automatic leveling. | `true` |
| `compensateGravity` | `bool` | Compensate gravity. | `true` |
| `holdAltitude` | `bool` | Hold height after releasing ascend/descend and brake horizontal drift after releasing movement, without returning to a position. Requires a running engine and fully spooled rotor. Disable for the original vertical damping behavior. | `true` |
| `horizontalDriveEnabled` | `bool` | Allow horizontal thrust from rotor tilt and automatic drift braking. Enabled by default. | `true` |
| `hoverDriftBrakingEnabled` | `bool` | Brake horizontal drift in neutral powered hover when altitude hold and automatic leveling are active. Enabled by default. | `true` |
| `linearDragEnabled` | `bool` | Apply inherited velocity-proportional air resistance. Enabled by default. | `true` |
| `tiltAccelerationMultiplier` | `float` | Multiplier for horizontal acceleration from rotor tilt. | `2`; Minimum: 0 |
| `verticalDamping` | `float` | Vertical damping. | `1.5`; Minimum: 0 |
| `verticalLiftEnabled` | `bool` | Allow the vertical rotor-support/collective channel, including altitude hold and gravity compensation. Enabled by default. | `true` |
| `yawAcceleration` | `float` | Yaw acceleration. | `5`; Minimum: 0 |
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
| `attitudeStrength` | `float` | Attitude strength. | `12`; Minimum: 0 |
| `automaticLeveling` | `bool` | Automatic leveling. | `true` |
| `bodyTiltDegrees` | `float` | Maximum combined hull lean toward forward/sideways thrust and steering, in degrees. | `5`; Range: 0 to 15 |
| `bodyTiltEnabled` | `bool` | Lean the leveling target with movement/steering demand. Disable for a level target; Automatic Leveling still owns restoring torque. Enabled by default. | `true` |
| `bodyTiltResponse` | `float` | Hull lean response per second, including return to level. | `2`; Minimum: .1f |
| `compensateGravity` | `bool` | Compensate gravity. | `true` |
| `damping` | `float` | Damping. | `6`; Minimum: 0 |
| `groundMask` | `LayerMask` | Ground mask. | `-1` |
| `height` | `float` | Height. | `2.5`; Minimum: .2f |
| `horizontalDriveEnabled` | `bool` | Allow forward and sideways thrust from commands. Enabled by default. | `true` |
| `linearDragEnabled` | `bool` | Apply inherited velocity-proportional resistance. Enabled by default. | `true` |
| `maximumAscentAcceleration` | `float` | Maximum ascent acceleration. | `25`; Minimum: 0 |
| `maximumDescentAcceleration` | `float` | Maximum descent acceleration. | `15`; Minimum: 0 |
| `spring` | `float` | Spring. | `12`; Minimum: 0 |
| `surfaceSupport` | `bool` | Surface support. | `true` |
| `verticalDamping` | `float` | Vertical damping. | `2`; Minimum: 0 |
| `verticalSupportEnabled` | `bool` | Allow collective, clearance spring, vertical damping and gravity compensation channel. Enabled by default. | `true` |
| `wheelSteeringTilt` | `float` | Wheel steering tilt. | `12`; Range: 0 to 30 |
| `wheelThrustTilt` | `float` | Wheel thrust tilt. | `10`; Range: 0 to 30 |
| `wheelTiltResponse` | `float` | Visual wheel tilt response per second. Lower values make acceleration, braking and steering tilt settle more slowly. | `8`; Minimum: .1f |
| `yawAcceleration` | `float` | Yaw acceleration. | `4`; Minimum: 0 |
| `yawControlEnabled` | `bool` | Allow commanded steering/yaw torque, independently of yaw damping. Enabled by default. | `true` |
| `yawDamping` | `float` | Yaw damping. | `2`; Minimum: 0 |
| `yawDampingEnabled` | `bool` | Allow passive damping around the vertical yaw axis. Enabled by default. | `true` |

## JetProfile

Adds jet-specific aerodynamic response and limits.

**Source:** `Runtime/Drive/Profiles/JetProfile.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [AerobaticAirplaneProfile](Drive.md#aerobaticairplaneprofile). These settings also appear on this type.

Relative-airflow fighter preset for the shared AirplaneProfile model. Its constructor selects RelativeAirflow and enables Progressive Thrust Envelope, G Limiter, Yaw Limiter and Rate Coordinated Turn. It also tunes engine, landing gear and body-rate settings. No additional Inspector fields are declared here; edit the inherited settings. See [fixed-wing model selection](../Aircraft.md#one-configurable-fixed-wing-model).

## MotorcycleBalance

Configuration/implementation type for motorcycle balance within engine and drivetrain.

**Source:** `Runtime/Drive/Grounded/MotorcycleBalance.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `disableBalanceOnDriverEject` | `bool` | Stop balance after driver ejection; resume on driver entry or respawn. Enabled on the demo motorcycle. | `false` |
| `nativeCollisionResponseAfterDriverEject` | `bool` | After driver ejection, use native body contact response without extra body friction, rebound or crash-transfer impulses. Requires Disable Balance On Driver Eject. Driver entry or respawn restores assistance. | `true` |
| `balanceDamping` | `float` | Resistance to roll motion while balancing. Increase to reduce side-to-side wobble; excessive damping can make lean changes sluggish. | `65`; Minimum: 0 |
| `balanceStrength` | `float` | Strength of the roll correction toward the requested lean. Increase to hold/recover the bike's balance more firmly; too much can make corrections abrupt. | `1200`; Minimum: 0 |
| `fullLeanSpeed` | `float` | Ground speed in m/s at which the full calculated cornering lean is allowed. Between Lean Start Speed and this value, banking is blended in gradually. | `4`; Speed field; stored in m/s, displayed in the selected speed unit |
| `leanRate` | `float` | Maximum rate at which requested motorcycle lean changes, in degrees per second. | `140`; Minimum: 1 |
| `leanRateDamping` | `float` | Damping accounting for how quickly the desired lean itself changes. Increase to soften overshoot during fast direction changes. | `.35`; Range: 0 to 1 |
| `leanStartSpeed` | `float` | Ground speed in m/s below which turning-related lean fades toward upright. Increase to keep the bike upright through more low-speed manoeuvres. | `.8`; Speed field; stored in m/s, displayed in the selected speed unit |
| `maximumAngularAcceleration` | `float` | Limit in rad/s² on the balance correction. Raise only if the bike should recover or lean more sharply under strong input. | `150`; Minimum: 0 |
| `maximumLean` | `float` | Greatest requested bank angle in degrees during a turn. Lower values keep the bike more upright; higher values allow deeper cornering lean. | `35`; Range: 0 to 50 |
| `measuredAccelerationWeight` | `float` | Blend steering anticipation with smoothed world-velocity acceleration. Yaw spin is not treated as cornering; contact noise cannot request lean against the steering direction. | `.25`; Range: 0 to 1 |
| `recoveryAngle` | `float` | Largest tilt from upright, in degrees, at which grounded balance assistance will still try to recover the motorcycle. Beyond this angle it stops righting an already fallen bike. | `65`; Range: 30 to 85 |
| `steeringPrediction` | `float` | Blend toward the driver's requested steering instead of waiting for the current wheel angle. Increase to begin leaning earlier when steering changes. | `.75`; Range: 0 to 1 |
| `accelerationSmoothTime` | `float` | Seconds to smooth actual path acceleration. Airborne motion and resets clear the sample. | `.2`; Minimum: 0 |
| `coordinateSteering` | `bool` | Optional wheel-angle limit based on Maximum Lean. Full parking-speed lock remains available. Disabled by default so steering retains its configured range. | `false` |
| `steeringBalanceMargin` | `float` | Fraction of Maximum Lean cornering capacity available to Steering path assistance and the optional wheel-angle limit. | `.85`; Range: .1 to 1 |
| `reversalLeanRate` | `float` | Maximum bank-target rate during an opposite-steering transition, in degrees/s. Uses at least Lean Rate. | `280`; Minimum: 1 |

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
| `wheelbase` | `float` | Motorcycle axle span used to convert steering to lean, in metres. | `1.45`; Minimum: .1f |

## ParkingHold

Configuration/implementation type for parking hold within engine and drivetrain.

**Source:** `Runtime/Drive/Brakes/ParkingHold.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `assistParkingBrake` | `bool` | Counter gravity-driven slope creep while the handbrake or detached-trailer parking brake is active; native tires handle braking and external pushes. | `true` |
| `assistServiceBrake` | `bool` | Counter gravity-driven slope creep while the service brake is active; no added planar braking resistance on level ground. | `true` |
| `captureSpeed` | `float` | Maximum vehicle speed in m/s at which the stationary parking/service hold can capture the body. | `.5`; Speed field; stored in m/s, displayed in the selected speed unit |

## ProfileSwitcher

Owns an ordered list of registered drive strategies and selects optional pair-specific transitions. Inherits ControllerModule.

**Source:** `Runtime/Drive/ProfileSwitcher.cs`. Component / asset.

**Inherited settings:** [ControllerModule](Controller.md#controllermodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `activeProfileId` | `string` | ID of the slot represented by VehicleController's current profile. Leave empty when the current profile is not registered. | `""` |
| `completed` | `UnityEvent` | Event invoked after the animated transition finishes and the destination profile is applied. Use it to clear transition UI or enable mode-specific presentation. | `No listeners` |
| `profiles` | `List<DriveProfileSlot>` ([fields](Drive.md#driveprofileslot)) | Named driving setups available for switching, such as road driving and flight. Each entry combines an ID used by requests/transitions with the movement profile to activate. | `Empty list` |
| `progressed` | `UnityEvent<float>` | Event reporting transition progress from 0 at the start to 1 at completion. Connect a listener to synchronize UI or another animation. | `No listeners` |
| `started` | `UnityEvent` | Event invoked when an animated profile transition begins. Use it to show a changing-mode indicator or start accompanying presentation. | `No listeners` |
| `transitions` | `ProfileTransition[]` ([fields](Drive.md#profiletransition)) | Enabled route components to consider. Exactly one matching route is allowed per pair; no matching route means immediate switching. | `Empty list` |

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
| `suspensionTravel` | `float` | Available wheel suspension travel in metres. Align the collider mount for this travel rather than setting travel to zero to align a mesh. | `.65`; Minimum: .001f |
| `targetPosition` | `float` | Normalized suspension spring rest position: 0 is fully extended and 1 is fully compressed. Loaded height also depends on mass and spring strength. | `.5`; Range: 0 to 1 |
| `wheel` | `WheelCollider` | Wheel collider receiving this shock's optional spring, damper and travel override. Without Override Native Suspension, the reference alone does not replace its suspension tuning. | `None / unassigned` |
| `wheelAnchor` | `Transform` | Moving shock attachment on the wheel or suspension arm. The piston follows this point as the suspension compresses and extends. | `None / unassigned` |

## SpaceshipProfile

**Source:** `Runtime/Drive/Profiles/SpaceshipProfile.cs`. Serializable drive profile. Inherited Drag and Angular Damping are both initialized to zero; fresh Spaceship setup also sets native Rigidbody damping to zero.

Inherited settings are documented with `FreeProfile`.

| Setting | Type | Description | Declared default |
| --- | --- | --- | --- |
| `compensateGravity` | `bool` | Cancel native gravity while this profile is active, including with ignition off. Explicit Release All Forces also releases this compensation. | `true` |
| `strafeAcceleration` | `float` | Sideways acceleration relative to the spacecraft, in m/s². | `8` |
| `liftAcceleration` | `float` | Up/down acceleration relative to the spacecraft, in m/s². | `8` |
| `angularRates` | `Vector3` | Maximum local pitch, yaw and roll rates in degrees per second. | `new Vector3(55, 55, 75)` |
| `angularResponse` | `float` | Rotational thruster response toward commanded angular rates. Uncommanded axes retain spin unless Stop Rotation On Release is enabled. | `5` |
| `maximumAngularAcceleration` | `float` | Maximum angular correction in rad/s². Does not restrict native collision impulses. | `12` |
| `brakeAcceleration` | `float` | Powered braking acceleration opposing current world velocity, in m/s². | `15` |

| `stopRotationOnRelease` | `bool` | Smooth rotational braking after releasing controls. | `true` |

| `alignFlightPath` | `bool` | Powered steering redirects travel toward the nose, except during explicit strafe/lift. | `true` |
| `flightPathTurnRate` | `float` | Maximum flight-path redirection rate in degrees/s, with smooth convergence toward the nose. | `180` |
| `maximumFlightPathAcceleration` | `float` | Maximum acceleration for travel redirection, in m/s². | `100` |
| `bankDriftEnabled` | `bool` | Bank-dependent sideways bank drift, including coasting; no automatic yaw; optional downward component. | `true` |
| `maximumBankDriftAngle` | `float` | Maximum assisted flight-path offset at full bank, in degrees. | `20`; Range: 0–30 |
| `bankDriftResponse` | `float` | How gradually drift builds and releases, in inverse seconds. | `1.5`; Minimum: 0 |
| `bankDriftExponent` | `float` | Shapes bank response: 2 gives very small drift at small banks and progressively stronger drift at large banks. | `1.5`; Range: 1–4 |
| `bankDriftSpeedMultiplier` | `float` | Scales the drift-speed ratio. | `1`; Range: 0–5 |
| `bankDriftDownwards` | `bool` | Include downward drift through inverted flight. | `false` |
| `bankDriftDownwardMultiplier` | `float` | Independently scales downward drift. | `1`; Minimum: 0 |

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
| `assistanceStrength` | `float` | Overall strength of the optional yaw/lateral steering assistance. | `.70`; Range: 0 to 1 |
| `highSpeedAngleRatio` | `float` | Fraction of the normal steering angle retained at high speed. At 0.3 the high-speed limit is 30% of full lock, making sudden high-speed turns less sharp. | `0.3`; Range: 0.1f to 1 |
| `lateralResponse` | `float` | How strongly arcade assistance removes unwanted sideways velocity. Increase for a grippier assisted feel; reduce to let the chassis slide longer. | `4`; Minimum: 0 |
| `maximumLateralAcceleration` | `float` | Steering authority at speed is limited to this requested lateral acceleration (m/s²). | `6`; Minimum: .1f |
| `maximumYawRate` | `float` | Maximum target rotation speed for arcade turning assistance, in radians per second. Reduce to make assisted turns less abrupt. | `1`; Minimum: .1f |
| `minimumTurnRadius` | `float` | Minimum rear-axle centre turning radius in metres; zero disables the low-speed radius cap. | `6`; Minimum: 0 |
| `speedSensitiveSteering` | `bool` | Optional reduction of steering angle with speed. Off preserves full steering authority. | `false` |
| `stabilizePoweredSlides` | `bool` | Keep a powered full-lock slide near its entry speed instead of accelerating into an expanding circle. | `true` |
| `useGroundGripLimit` | `bool` | Further limits the requested wheel angle to what the sampled ground grip can support. This reduces steering demands that would immediately make the tires slide; handbrake turns bypass it. | `true` |
| `yawResponse` | `float` | How strongly arcade assistance corrects the difference between actual and requested turning rate. Increase for quicker assisted rotation, while Maximum Yaw Rate still caps the target. | `7`; Minimum: 0 |

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
| `hullHalfHeight` | `float` | Hull half height. | `1.5`; Minimum: .1f |
| `lateralResistance` | `float` | Lateral resistance. | `1.8`; Minimum: 0 |
| `levelingStrength` | `float` | Leveling strength. | `4`; Minimum: 0 |
| `maximumPitch` | `float` | Maximum pitch. | `18`; Range: 0 to 40 |
| `quadraticResistance` | `float` | Quadratic resistance. | `.025`; Minimum: 0 |
| `turnResponse` | `float` | Turn response. | `2`; Minimum: 0 |
| `verticalAcceleration` | `float` | Vertical acceleration. | `2`; Minimum: 0 |
| `verticalResistance` | `float` | Vertical resistance. | `2`; Minimum: 0 |
| `waterCenter` | `Vector2` | Water center. | `new Vector2(-280, 80)` |
| `waterLevel` | `float` | Flat fallback water-surface height in world metres. | `2.3` |
| `waterSize` | `Vector2` | Water size. | `new Vector2(400, 640)` |
| `yawRate` | `float` | Yaw rate. | `.42`; Minimum: 0 |

## Suspension

Configures native wheel support and suspension-related response.

**Source:** `Runtime/Drive/Suspension/Suspension.cs`. Component / asset.

**Inherited settings:** [DriveModule](Drive.md#drivemodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `allowLandingRebound` | `bool` | Temporarily release the expansion limiter during landing response, allowing the springs to push the chassis back upward. | `true` |
| `arcadeBumpDamping` | `bool` | Game-oriented damping of excessive upward body motion while most wheels remain supported. | `false` |
| `automaticForceApplication` | `bool` | Calculates wheel force application points from the chassis centre of mass instead of the manual height. It changes how tire forces roll/pitch the body, not the wheel mount or suspension travel. | `true` |
| `bodySwayTravelRatio` | `float` | Additional force lever arm as a fraction of suspension travel, allowing body pitch and roll. | `.28`; Range: 0 to 1 |
| `bumpDampingResponse` | `float` | Strength of the extra correction that removes excessive upward chassis speed after a bump. Higher values settle the body faster when Bump Damping is enabled; zero removes this correction. | `10`; Minimum: 0 |
| `damper` | `float` | Native suspension damping in N·s/m. Increase to reduce repeated bouncing after a bump; too much can make the wheel slow to follow road changes. | `2295`; Minimum: 0 |
| `damperBlowoffSpeed` | `float` | Suspension stroke speed in m/s where degressive damping begins limiting the force increase. Lower values soften fast bumps sooner; higher values retain stronger damping through faster strokes. | `.75`; Minimum: .05f |
| `degressiveDamping` | `bool` | Reduces compression damper growth at fast strokes while retaining rebound damping and slower body control. Enable to soften sharp bumps without making the chassis float after them. | `true` |
| `directionalLandingBounce` | `bool` | Apply landing rebound at the supporting wheels rather than only the centre of mass, allowing directional pitch and roll on angled landings. | `true` |
| `directionalLandingResponse` | `bool` | Retain the approach speed while airborne so an angled chassis touch cannot instantly cancel the following wheel compression response. Assisted bounce energy still uses actual wheel contact speed. | `true` |
| `forceApplicationHeight` | `float` | Manual wheel-force application distance in metres above the tire's base at rest. Used when Automatic Force Application is off; changing it changes the lever arm that pitches/rolls the chassis. | `0.15`; Minimum: 0 |
| `forceOffsetBelowCenterOfMass` | `float` | Metres below the centre of mass used for automatic force application. Increasing the separation changes the tire-force lever arm and the body's roll/pitch response. | `.3`; Minimum: .05f |
| `landingAngularBrakingTime` | `float` | Near the support plane, reduce the allowed approach speed using the remaining tilt divided by this time in seconds. Zero disables this final braking zone. | `.06f` |
| `landingAngularContactGrace` | `float` | Seconds to fade angular touchdown damping after every wheel ray finds support, allowing the last axle to compress before assistance ends. Zero ends it immediately at full ray contact. | `.12f` |
| `landingAngularDamping` | `float` | Angular damping rate in 1/s during partial wheel touchdown. With the speed limit enabled, only rotation above the allowed approach speed is damped. | `26` |
| `landingAngularMaximumDeceleration` | `float` | Maximum requested relative angular deceleration during partial touchdown, in degrees/s squared. | `3600` |
| `landingAngularMaximumSpeed` | `float` | Soft maximum relative approach rotation in degrees/s during angled touchdown. Faster rotation is progressively damped rather than clamped. | `60` |
| `landingAngularSpeedLimit` | `bool` | Only brake excessive rotation toward the support plane. Ordinary axle descent remains free; disable to restore continuous angular damping. | `true` |
| `landingBounceMaximumCount` | `int` | Maximum assisted releases in legacy mode. Progressive mode assists only the first rebound; subsequent motion uses native springs and dampers. | `3` |
| `landingBounceMaximumRotation` | `float` | Maximum angular speed change from an assisted landing rebound in degrees/s. Bounds partial-wheel leverage without clamping native collision rotation. | `35` |
| `landingBounceMaximumSpeed` | `float` | Upper limit on requested upward speed after the tires clear full suspension travel, relative to the surface, in m/s. | `2` |
| `landingBounceMaximumTilt` | `float` | Maximum gravity-relative chassis tilt in degrees for assisted wheel rebound. Side and roof landings remain passive. | `55` |
| `landingBounceRestitution` | `float` | Fraction of impact speed retained for the next hop. Each following hop is also bounded by the previous speed budget multiplied by this fraction. | `.45f` |
| `landingBumpStopMultiplier` | `float` | Progressive end-of-travel spring stiffness during landing, relative to the authored spring. Prevents the soft initial stroke from losing its energy against the rigid travel stop. | `1.5f`; Range: 1 to 3 |
| `landingContactLeverage` | `float` | Blend the rebound application point from the centre of mass to the average supporting wheel contact. Higher values produce more pitch/roll from partial axle support. | `.75f` |
| `landingDamperMultiplier` | `float` | Fraction of the normal damper retained at full landing response. Lower values allow more body bounce. | `.2f` |
| `landingEventFullSpeed` | `float` | Surface-relative touchdown speed in m/s producing full LandingEvent intensity and landing event audio gain. Independent of physical landing assistance; minimum uses Landing Minimum Speed. | `15` |
| `landingFullResponseSpeed` | `float` | Downward landing speed producing the full configured response, in m/s. | `4.5f` |
| `landingSettlingDampingRatio` | `float` | Target damping ratio during progressive landing settling, estimated from chassis mass and total wheel stiffness/damping. Normal damping returns after motion becomes quiet. Lower values allow more oscillation; 1 is critical damping. Does not increase authored damping. | `.25f` |
| `progressiveLandingRecovery` | `float` | Multiplies the landing recovery duration while progressive bounce is enabled. Smaller values restore normal damping sooner. | `.5f` |
| `progressiveLandingBounce` | `bool` | Releases bounded rebound assistance over the loaded spring extension stroke. Disable to restore the previous single-impulse response. Requires Landing Ground Bounce. | `true` |
| `landingGroundBounce` | `bool` | Enables bounded whole-vehicle rebound after qualifying upright wheel landings. Progressive mode scales smoothly with impact strength; legacy mode retains its upper-half strength gate. Requires Landing Response. Enabled by default for grounded profiles. | `true` |
| `landingImpactCompressionSpeed` | `float` | Requested normal compression speed after a predicted hard touchdown, in m/s. Lower values give the suspension more time to compress. | `1.5f` |
| `landingImpactLeverage` | `float` | Impact impulse lever from chassis centre of mass to the weighted tire contacts. Lower values distribute more of the hard landing load through the chassis instead of instantly pitching it about the first axle. | `.15f` |
| `landingImpactMinimumSpeed` | `float` | Minimum genuine airborne downward approach speed in m/s that arms predictive impact absorption. Lower-speed landings retain the normal spring response. | `8` |
| `landingImpactReserveTravel` | `float` | Fraction of suspension travel reserved before the rigid compression stop. Protects against crossing the full stroke in one physics step. | `.15f` |
| `landingMinimumAirTime` | `float` | Minimum continuous time without wheel support before a landing can activate the response, in seconds. | `.15f` |
| `landingMinimumCycles` | `float` | Natural suspension cycles at full landing strength. Weaker impacts use fewer cycles. Uses chassis mass and softened spring rates; zero uses only the speed-scaled duration. | `2.5f`; Minimum: 0 |
| `landingMinimumSpeed` | `float` | Minimum downward contact speed relative to the landing surface, in m/s. | `1.5f` |
| `landingResponse` | `bool` | Temporarily soften springs and damping after a genuine airborne wheel landing, allowing compression, rebound and a gradual settling of the chassis. | `true` |
| `landingResponseDuration` | `float` | Full-strength recovery time in seconds; the natural spring period and Landing Minimum Cycles can extend it. Weaker impacts use a shorter smooth recovery. | `.9f` |
| `landingSpringMultiplier` | `float` | Fraction of each authored spring retained during a full landing response. Applies to active per-wheel shock overrides too, and returns smoothly to the authored stiffness. | `.6f`; Range: .25 to 1 |
| `limitExpansionVelocity` | `bool` | Enables the native limit on how rapidly suspension can extend. This helps avoid an unloaded spring snapping the wheel downward too quickly. | `true` |
| `predictiveLandingCompression` | `bool` | Predict tire contact within the next physics step and absorb excessive approach speed before suspension hard-stop correction can flatten or displace the chassis. Requires Landing Response. Does not change the body pose. | `true` |
| `progressiveAngularLanding` | `bool` | Dissipate chassis rotation toward the support plane while only some wheels have landed after genuine flight. Uses torque, leaving yaw and rotation away from the ground free. Requires Landing Response. | `true` |
| `showGizmos` | `bool` | Preview wheel spring travel, rest position for the selected vehicle. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `spring` | `float` | Native wheel suspension spring stiffness in N/m. Increase to support more weight with less compression; decrease for softer suspension. Reapply configuration after editing. | `26250`; Minimum: 1 |
| `supportedRiseSpeed` | `float` | Upward body speed in m/s allowed before optional arcade bump damping acts while most wheels are supported. | `.75`; Minimum: .1f |
| `targetPosition` | `float` | Normalized suspension spring rest position: 0 is fully extended and 1 is fully compressed. Loaded height also depends on mass and spring strength. | `0.5`; Range: 0 to 1 |
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
