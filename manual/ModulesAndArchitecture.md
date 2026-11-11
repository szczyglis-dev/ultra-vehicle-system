# Modules and architecture

A vehicle is built around one **Vehicle Controller** and a set of components called **modules**. The controller brings them together; each module handles a particular responsibility, such as steering, engine power, cockpit instruments or sound. Start with the components added by your vehicle preset, then add the optional systems your vehicle needs.

## Start from the Inspector

Select the root and open **Vehicle Controller > Modules**. Choose a category, expand an installed module or use **Add module...** at the bottom. Fill its references before pressing **Apply vehicle configuration**. Components added directly through Unity's Add Component can be picked up with **Discover and order vehicle modules**. Model-mounted helpers still need their specific registry/parent connections.

Use [Basic Inspector workflow](InspectorConfiguration.md#basic-inspector-workflow) for the complete add/assign/save sequence and a table of subsystem entry points. Continue with a system's practical guide before using its API reference; installing a module alone does not place lights, exhaust outlets, hinges or seat anchors on the model.

## The main controller

`VehicleController` is the entry point for configuring and controlling one vehicle. It owns the vehicle settings, selected drive profile, wheel setup and module registry. It receives driving commands, coordinates the registered systems and exposes the resulting vehicle state through telemetry.

The root GameObject normally contains the controller, a Rigidbody and body colliders. Modules may live on that root or appropriate children: an instrument animator can sit on the dashboard, for example. The hierarchy defines which vehicle owns these components; a nested Vehicle Controller starts a separate vehicle.

The **drive profile** defines the movement family, such as Wheeled, Motorcycle, Airplane or Boat. Modules provide the mechanics and equipment used by that profile. Changing the profile changes the movement behavior; the vehicle still needs the corresponding geometry, references and supporting modules.

## Module categories

The controller groups modules by their responsibility. These categories organize the Inspector and the code; you do not need to create a separate GameObject for each category.

| Category | What belongs here | Examples |
| --- | --- | --- |
| Controller | Driving input and selection of the active movement mode | Keyboard or Input System adapters, external control, profile switching |
| Physics | Wheel contact, tire friction and physical damage | Wheel dynamics, tire collision, damage and mesh deformation |
| Drive | Steering, braking, suspension and movement behavior | Drive, steering, brakes, anti-roll, motorcycle balance and tracks |
| Engine | Power generation and transmission to the driven wheels | Engine, gearbox, clutch, differential and traction control |
| Interior | Cockpit controls, instruments and displays | Steering wheel and pedal animators, switches, needles, HUDs and mirrors |
| Exterior | Moving equipment and visible mechanisms on the vehicle | Doors, windows, lights, wipers, landing gear, propellers and rotors |
| World | Interaction with occupants, other vehicles and the environment | Seats and passengers, cameras, towing, water interaction and weapons |
| Effects | TireFeedback presented through sound, particles and marks | Audio, tire smoke, exhaust, water effects and skid marks |

A feature can involve several categories. Brakes in **Drive** calculate braking, a pedal animator in **Interior** moves the visible pedal, and components in **Effects** produce tire sound or smoke from the resulting contact state. Tune the mechanical behavior in its owning module and the appearance in the relevant presentation components.

## Animators, handles and subsystem owners

An interior **animator** moves a control or instrument. An IK **handle** defines how a passenger's hand or foot uses it. For example, a steering wheel animator rotates the wheel, while its handle supplies hand contacts and grip settings. The Interior view lists **Animators** and **Handles** separately. Handles are coordinated by the vehicle's handle controller, which manages limb transfers and returns between controls.

Some systems also group their own components. **Audio** manages audio channels, **Passengers** manages seats and occupants, and **Cameras** manages camera submodules. Add and configure these components through their owning system. Model helpers, such as a wiper blade, provide geometry for their owner rather than acting as a complete vehicle system on their own.

## How the systems work together

During driving, input becomes a shared command. The controller advances mechanics in dependency order, then makes the resolved state available to instruments, passengers and effects. A steering request, the actual wheel angle and the visible cockpit rotation are different stages of this flow.

Use the controller Inspector to add modules, assign their references and apply vehicle configuration. Configure optional systems independently; adding a component does not supply your model's hinges, light objects, seats or control anchors. The setup chapters describe those bindings for each system.

For code integration and execution details, continue with [Architecture and update ownership](Architecture.md) and [Extend and integrate](Scripting.md). For choosing equipment, see [Choose systems](ChoosingSystems.md).

## Modules list

Use this catalog to choose the components to add to a vehicle. Categories describe responsibilities; they do not determine fixed-step order. A **Module** is registered with VehicleController and participates through Configure/Step. The **Helpers** groups also include the root controller and nested audio, camera and passenger components driven by their own owners; adding one of these components to the hierarchy does not turn it into a standalone scheduled mechanic. **Assets** are reusable configuration, not components to attach.

Start with VehicleController, Rigidbody, body colliders, an input provider and a compatible drive profile. Add only the capabilities required by the model. For modules, discover/register the instance and apply configuration after assigning references. Dependency names below identify built-in component contracts or referenced collaborators; assign geometry, clips, materials and limits as described in the linked Inspector reference. Optional references do not all have to be filled. A component can also require the profile/capability described by its setup guide.

### Controller

Select one active input source for the vehicle. Input providers require a VehicleController assignment/selection; buffering and gating adapt that command flow.

#### Modules

- `ActionInput`: Reads configured Unity Input System actions. Requirements / collaborators: VehicleController input selection; Input System actions or configured default bindings. [Settings](InspectorReference/Controller.md#actioninput).

- `DirectController`: Replaceable buffered input source with optional direct world-pose control. See the direct-mode guide. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Controller.md#directcontroller).

- `ExternalController`: Provides the buffered command API for external control. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Controller.md#externalcontroller).

- `InputBuffer`: Buffers axes and pending one-shot actions for fixed-step consumption. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Controller.md#inputbuffer).

- `InputGate`: Controls permission to pass input to the vehicle. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Controller.md#inputgate).

- `KeyboardBoatInput`: Reads keyboard commands for boat operation; select as the vehicle input provider when using the built-in keyboard controls. Requirements / collaborators: VehicleController registration; ActionInput (analogInput). [Settings](InspectorReference/Controller.md#keyboardboatinput).

- `KeyboardDriveInput`: Reads keyboard commands for drive operation; select as the vehicle input provider when using the built-in keyboard controls. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Controller.md#keyboarddriveinput).

- `KeyboardFlightInput`: Reads keyboard commands for flight operation; select as the vehicle input provider when using the built-in keyboard controls. Requirements / collaborators: VehicleController registration; ActionInput (analogInput). [Settings](InspectorReference/Controller.md#keyboardflightinput).

- `KeyboardSubmarineInput`: Reads keyboard commands for submarine operation; select as the vehicle input provider when using the built-in keyboard controls. Requirements / collaborators: VehicleController registration; ActionInput (analogInput). [Settings](InspectorReference/Controller.md#keyboardsubmarineinput).

- `ProfileSwitcher`: Owns an ordered list of registered drive strategies and selects optional pair-specific transitions. Inherits ControllerModule. Requirements / collaborators: VehicleController registration; registered profile assets and optional transition routes. [Settings](InspectorReference/Drive.md#profileswitcher).

#### Helpers

- `VehicleController`: Owns one vehicle: its root body, input sampling, wheel configuration, registry and fixed-step pipeline. Requirements / collaborators: Root Rigidbody and body collider; selected input source/profile; authored wheel setup when wheels are used. [Settings](InspectorReference/Controller.md#vehiclecontroller).

### Drive

Use these for steering, brakes, ground support and drive-profile execution. Wheel mechanics need configured Wheel adapters/native WheelColliders. Visual linkages need authored pivots and anchors.

#### Modules

- `AntiRoll`: Optional, manually added module; default vehicle presets and full setup do not install it. Adds cross-wheel roll support for the configured wheel relationships. Requirements / collaborators: VehicleController registration; Wheel (left); Wheel (right). [Settings](InspectorReference/Drive.md#antiroll).

- `Brakes`: Applies service and handbrake demand to configured wheel roles; add for wheeled braking. Requirements / collaborators: VehicleController registration; Engine (engine). [Settings](InspectorReference/Drive.md#brakes).

- `Burnout`: Included by vehicle creation and Full setup. Produces wheelspin on wheel/track vehicles and held propulsion boost on boats, submarines and rotor/hover vehicles; fixed-wing aircraft boost native thrust directly. Requires registration, a running Engine and active Drive; wheelspin also requires driven-wheel contact. [Settings](InspectorReference/Drive.md#burnout).

- `ContactEnvelope`: Samples tire-shaped support and adjusts effective native support radius. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#contactenvelope).

- `Drive`: Runs the active drive profile and retains its movement state; add for profile-based wheel, air or water movement. Requirements / collaborators: VehicleController registration and selected compatible DriveProfile. [Settings](InspectorReference/Drive.md#drive).

- `DrivingAssists`: Coordinates configured driving-assistance settings; add when those assists need one control surface. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#drivingassists).

- `MotorcycleBalance`: Applies motorcycle balance assistance; add for a supported two-wheel setup. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#motorcyclebalance).

- `ParkingHold`: Holds the vehicle under its configured parking conditions; add for stationary parking assistance. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#parkinghold).

- `Steering`: Resolves steering input and wheel steering angles; add for steerable wheel assemblies. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#steering).

- `Suspension`: Configures native wheel support and suspension-related response. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#suspension).

- `Tracks`: Owns explicit side membership and tracked support policy. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#tracks).

#### Helpers

- `ControlArm`: Resolves a visual control arm against its authored geometry. Requirements / collaborators: Wheel (wheelAdapter); SteeringTieRod (steeringLinkage). [Settings](InspectorReference/Drive.md#controlarm).

- `HalfShaft`: Presents axle articulation and shaft rotation. Requirements / collaborators: Authored inner/outer attachment transforms, shaft mesh/axes and wheel motion reference. [Settings](InspectorReference/Drive.md#halfshaft).

- `HoverDriveTransition`: Coordinates hover/ground profile transition geometry and contact readiness; assign the transition route and wheel/hover setup. Requirements / collaborators: ProfileSwitcher route; compatible wheeled/hover profiles and configured wheels. [Settings](InspectorReference/Drive.md#hoverdrivetransition).

- `ProfileTransition`: A route component for one source/destination ID pair, optionally bidirectional. Inherits MonoBehaviour. Requirements / collaborators: ProfileSwitcher and exact source/destination profile IDs; authored transition behavior. [Settings](InspectorReference/Drive.md#profiletransition).

- `ShockAbsorber`: Animates a telescoping shock and optionally overrides one wheel's physics. Requirements / collaborators: Chassis/wheel attachment transforms, casing/piston geometry; native WheelCollider for optional physical override. [Settings](InspectorReference/Drive.md#shockabsorber).

- `SteeringTieRod`: Tracks steering-link endpoints and geometry. Requirements / collaborators: Authored rack/knuckle anchors, rod geometry and steering/wheel reference. [Settings](InspectorReference/Drive.md#steeringtierod).

- `SuspensionAxle`: Solves the visual axle assembly from its wheel/anchor geometry; add for an axle mesh spanning suspension movement. Requirements / collaborators: Authored axle transform, left/right endpoint geometry and wheel references. [Settings](InspectorReference/Drive.md#suspensionaxle).

- `SuspensionHub`: Provides hub/kingpin geometry for the wheel assembly. Requirements / collaborators: Wheel (wheelAdapter); SteeringTieRod (steeringLinkage). [Settings](InspectorReference/Drive.md#suspensionhub).

### Effects

Use for sound, particles, decals and feedback. Assign sources/profiles/prefabs. AudioModule channels belong to Audio rather than the controller schedule; surface effects use contact feedback.

#### Modules

- `Audio`: Owns channel discovery, common audio settings and render-frame dispatch. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); Engine (engine); TireFeedback (tireFeedback). [Settings](InspectorReference/Effects.md#audio).

- `BoatWaterParticles`: Uses hull-water contact for surface-water presentation. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); Engine (engine). [Settings](InspectorReference/Effects.md#boatwaterparticles).

- `CommercialAudio`: Adds commercial-vehicle audio behavior; add when the vehicle needs its configured auxiliary sounds. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); Gearbox (gearbox). [Settings](InspectorReference/Effects.md#commercialaudio).

- `DamageAudio`: Renders damage-related audio feedback; add for configured impact sounds and damage state. Requirements / collaborators: VehicleController registration; Damage (damage); DamageImpactProfile (fallbackProfile). [Settings](InspectorReference/Effects.md#damageaudio).

- `Events`: Publishes application-defined custom effect notifications. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Effects.md#events).

- `ExhaustSmoke`: Controls emission from configured exhaust outlets. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); Engine (engine). [Settings](InspectorReference/Effects.md#exhaustsmoke).

- `TireFeedback`: Builds per-wheel presentation state after mechanics. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); TireSurfaceProfile (defaultSurface). [Settings](InspectorReference/Effects.md#tirefeedback).

- `PropulsionJets`: Presents propulsion exhaust/jet outlets. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); Engine (engine). [Settings](InspectorReference/Effects.md#propulsionjets).

- `Skidmarks`: Consumes contact state and controls trail history. Requirements / collaborators: VehicleController registration; TireFeedback (tireFeedback); TireSurfaceProfile (profile). [Settings](InspectorReference/Effects.md#skidmarks).

- `TireSmoke`: Manages wheel smoke and granular emission. Requirements / collaborators: VehicleController registration; TireFeedback (tireFeedback). [Settings](InspectorReference/Effects.md#tiresmoke).

- `WeaponEffects`: Presents shot sound, flash and smoke. Requirements / collaborators: VehicleController registration; WeaponBarrel (weapon). [Settings](InspectorReference/Effects.md#weaponeffects).

- `WeaponRecoil`: Presents configured visual/hull recoil. Requirements / collaborators: VehicleController registration; WeaponBarrel (weapon). [Settings](InspectorReference/Effects.md#weaponrecoil).

#### Helpers

- `BoatWaterAudio`: Renders hull/water feedback audio; add an audio channel for a boat with water-contact sampling. Requirements / collaborators: Audio channel owner. [Settings](InspectorReference/Effects.md#boatwateraudio).

- `BrakeAudio`: Renders brake-related audio; add to the audio owner with the relevant clips and braking state. Requirements / collaborators: Audio channel owner. [Settings](InspectorReference/Effects.md#brakeaudio).

- `EngineAudio`: Renders engine sounds; add under the Audio channel owner and assign its recordings/state references. Requirements / collaborators: Audio channel owner; Engine (engine). [Settings](InspectorReference/Effects.md#engineaudio).

- `EventAudio`: Routes configured application-defined Events notifications to audio playback; add to the audio owner. Requirements / collaborators: Audio channel owner. [Settings](InspectorReference/Effects.md#eventaudio).

- `HornAudio`: Renders horn sounds; add under the Audio channel owner and assign its recordings/state references. Requirements / collaborators: Audio channel owner. [Settings](InspectorReference/Effects.md#hornaudio).

- `IndicatorAudio`: Renders indicator sounds; add under the Audio channel owner and assign its recordings/state references. Requirements / collaborators: Audio channel owner; Lights (lights). [Settings](InspectorReference/Effects.md#indicatoraudio).

- `SwitchAudio`: Renders switch sounds; add under the Audio channel owner and assign its recordings/state references. Requirements / collaborators: Audio channel owner; SwitchAnimator (switchAnimator). [Settings](InspectorReference/Effects.md#switchaudio).

- `TireAudio`: Renders tire sounds; add under the Audio channel owner and assign its recordings/state references. Requirements / collaborators: Audio channel owner. [Settings](InspectorReference/Effects.md#tireaudio).

- `TireSurface`: Maps a collider/hierarchy or Terrain layers to effect profiles. Requirements / collaborators: TireSurfaceProfile (profile). [Settings](InspectorReference/Effects.md#tiresurface).

### Engine

Add the drivetrain capabilities required by your propulsion model. Gearbox, clutch and differential cooperate with Engine/Transmission and configured driven wheels; they do not create wheel geometry.

#### Modules


- `AutomaticGearbox`: Makes automatic shift decisions from operating conditions. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Engine.md#automaticgearbox).

- `Clutch`: Models coupling and finite rotational energy transfer. Requirements / collaborators: VehicleController registration; Engine (engine). [Settings](InspectorReference/Engine.md#clutch).

- `Differential`: Distributes driven axle torque. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Engine.md#differential).

- `Engine`: Resolves running state, RPM and propulsion torque/power. Requirements / collaborators: VehicleController registration; Gearbox (gearbox); Clutch (clutch). [Settings](InspectorReference/Engine.md#engine).

- `FuelTank`: Stores fuel, consumption and refueling state; add when engine operation should depend on available fuel. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Engine.md#fueltank).

- `ManualGearbox`: Provides the manually selected gearbox implementation. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Engine.md#manualgearbox).

- `Nitro`: Provides configured temporary power boost and consumable charge; add to a compatible engine setup. Requirements / collaborators: VehicleController registration; Engine (engine). [Settings](InspectorReference/Engine.md#nitro).

- `TractionControl`: Limits propulsion according to contact capacity and slip. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Engine.md#tractioncontrol).

- `Transmission`: Selects Direct, Manual or Automatic transmission operation. Requirements / collaborators: VehicleController registration; Engine (engine); AutomaticGearbox (automatic); ManualGearbox (manual). [Settings](InspectorReference/Engine.md#transmission).

#### Helpers

No standalone helpers in this category.

### Exterior

Use for bodywork, lights, moving geometry and aircraft/track presentation. Assign each owner its part entries and model pivots; visible motion alone does not create propulsion or ground support.

#### Modules

- `AircraftControlSurfaces`: Presents the configured control-surface motion. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Exterior.md#aircraftcontrolsurfaces).

- `Body`: Finds and operates authored `VehicleBodyPart` entries. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Exterior.md#body).

- `HoverVisuals`: Presents hover-mode visual posture; add when the model needs hover-specific visual motion. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Exterior.md#hovervisuals).

- `LandingGear`: Owns deployment sequencing and physical gear-contact availability. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Exterior.md#landinggear).

- `LandingGearSuspension`: Schedules load-driven hinged landing-leg response; add with LandingGear and configured suspension-part entries. Requirements / collaborators: VehicleController registration; LandingGearSuspensionPart (config). [Settings](InspectorReference/Exterior.md#landinggearsuspension).

- `Lights`: Owns beam/indicator requests, automatic outputs and timing. Requirements / collaborators: VehicleController registration; Engine (engine). [Settings](InspectorReference/Exterior.md#lights).

- `MovingPart`: Owns rotation/translation requests, constraints and scheduled motion. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Exterior.md#movingpart).

- `Propulsion`: Animates propellers and rotors for aircraft, boats and submarines. Requirements / collaborators: VehicleController registration; Engine (engine). [Settings](InspectorReference/Exterior.md#propulsion).

- `TrackVisuals`: Moves visible links and rollers from wheel motion. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Exterior.md#trackvisuals).

- `Wipers`: Owns wiper cycle timing, running state and blade dispatch. Requirements / collaborators: VehicleController registration; WiperBlade (helper). [Settings](InspectorReference/Exterior.md#wipers).

#### Helpers

- `AircraftControlSurface`: Defines one control-surface motion binding; add to an aileron, elevator or rudder pivot. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Exterior.md#aircraftcontrolsurface).

- `VehicleBodyPart`: Defines a named opening/moving body element. Requirements / collaborators: Body owner and authored hinge pivot; suitable collider/body setup for optional physical hinge. [Settings](InspectorReference/Exterior.md#vehiclebodypart).

- `DamagePart`: Defines one mesh/collider damage boundary and its release/repair state; add per damageable panel or assembly. Requirements / collaborators: Damage registry; owned render meshes/colliders; retained original parent for repair. [Settings](InspectorReference/Exterior.md#damagepart).

- `LandingGearPart`: Maps deployment progress to a door/strut pose. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Exterior.md#landinggearpart).

- `LandingGearSuspensionPart`: Defines one hinged leg, wheel link, angular limits and spring response; add per bending landing leg. Requirements / collaborators: LandingGearPart (gearPart). [Settings](InspectorReference/Exterior.md#landinggearsuspensionpart).

- `TrackPathBuilder`: Prepares reusable closed paths during authoring. Requirements / collaborators: TrackVisuals (visuals). [Settings](InspectorReference/Exterior.md#trackpathbuilder).

- `WheelPart`: Specializes DamagePart for wheel debris, wheel disconnection and repair; add on the visual wheel root and link its Wheel adapter. Requirements / collaborators: Wheel (wheel). [Settings](InspectorReference/Exterior.md#wheelpart).

- `WiperBlade`: Maps normalized stroke to authored blade geometry. Requirements / collaborators: Wipers owner, blade pivot and authored stroke geometry. [Settings](InspectorReference/Exterior.md#wiperblade).

- `WiperSwitchBinding`: Connects switch positions to Wipers mode/speed and synchronizes the displayed state; add for a working wiper control. Requirements / collaborators: Wipers (wipers); SwitchAnimator (switchAnimator). [Settings](InspectorReference/Exterior.md#wiperswitchbinding).

### Interior

Use for cockpit readouts and visible controls. Assign the owning vehicle, value source and visual/UI target; animation helpers move models while passenger handles provide limb targets.

#### Modules

- `AircraftHud`: Presents aircraft telemetry and gear state; add for a flight display with assigned UI targets. Requirements / collaborators: VehicleController registration; VehicleController (vehicle). [Settings](InspectorReference/Interior.md#aircrafthud).

- `AnchoredControlAnimator`: Animates a control around authored anchor frames; use when its pivot/contact frame must remain stable while the visible control moves. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#anchoredcontrolanimator).

- `CarHud`: Presents road-vehicle telemetry; add for a dashboard with assigned UI targets. Requirements / collaborators: VehicleController registration; VehicleController (vehicle). [Settings](InspectorReference/Interior.md#carhud).

- `GearLeverAnimator`: Animates gear-lever positions from gearbox state and coordinates the operating hand; assign the lever poses, gearbox and interaction bindings. Requirements / collaborators: VehicleController registration; Engine (engine); Gearbox (gearbox). [Settings](InspectorReference/Interior.md#gearleveranimator).

- `GearPaddleAnimator`: Animates accepted paddle shifts and the associated hand gesture; use for steering-wheel shift paddles. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#gearpaddleanimator).

- `GearShiftAnimator`: Provides the gear-change animation implementation for gearbox-driven controls; bind to the engine/gearbox and authored motion. Requirements / collaborators: VehicleController registration; Engine (engine); Gearbox (gearbox). [Settings](InspectorReference/Interior.md#gearshiftanimator).

- `InstrumentNeedle`: Specializes value-driven rotation for instruments. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#instrumentneedle).

- `PedalAnimator`: Animates pedal travel from a bound vehicle value; add for brake, clutch or accelerator pedals. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#pedalanimator).

- `RearMirrors`: Owns mirror eligibility, camera rendering and generated textures. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#rearmirrors).

- `RotaryAnimator`: Rotates a control through its configured value range; add for dials and rotary instruments with an assigned value source. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#rotaryanimator).

- `SteeringStickAnimator`: Animates aircraft stick motion from steering/pitch state; use with the corresponding pilot handle and optional throttle binding. Requirements / collaborators: VehicleController registration; JoystickHandle (handle); PassengerSeat (driverSeat); ThrottleAnimator (throttle). [Settings](InspectorReference/Interior.md#steeringstickanimator).

- `SteeringWheelAnimator`: Animates an interior steering wheel from the vehicle actuator state, independently of input hardware. Requirements / collaborators: VehicleController registration; VehicleController (vehicle). [Settings](InspectorReference/Interior.md#steeringwheelanimator).

- `SwitchAnimator`: Animates a discrete control between authored switch positions; connect a binding when it should invoke a vehicle action. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#switchanimator).

- `ThrottleAnimator`: Animates a throttle lever from its bound value; assign the control geometry and range. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); PassengerSeat (driverSeat). [Settings](InspectorReference/Interior.md#throttleanimator).

- `TwistThrottleAnimator`: Animates a rotating motorcycle throttle around its anchored grip axis; add to the grip model with its throttle value binding. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#twistthrottleanimator).

- `YokeAnimator`: Animates yoke steering/pitch motion; assign its model pivots and vehicle/control bindings. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Interior.md#yokeanimator).

#### Helpers

- `AircraftControlMotion`: Maps normalized motion to an authored exterior aircraft-part pose; shared by control surfaces and landing-gear parts. Requirements / collaborators: Owning aircraft/control component and authored neutral/target pose. [Settings](InspectorReference/Exterior.md#aircraftcontrolmotion).

- `ClutchSource`: Exposes clutch as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#clutchsource).

- `CommandValueSource`: Exposes command value as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#commandvaluesource).

- `ControlInteraction`: Owns a timed character/control interaction and its commit/cancel lifecycle; add for controls operated through an interaction sequence. Requirements / collaborators: PassengerSeat (seat); VehicleHandle (target). [Settings](InspectorReference/Interior.md#controlinteraction).

- `ControlInteractionAnimationEvents`: Relays Animator events to the active interaction. Requirements / collaborators: ControlInteraction (interaction). [Settings](InspectorReference/Interior.md#controlinteractionanimationevents).

- `EngineRpmSource`: Exposes engine RPM to an interior value binding; assign the engine/vehicle used by the instrument. Requirements / collaborators: Engine (engine). [Settings](InspectorReference/Interior.md#enginerpmsource).

- `GasSource`: Exposes gas as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#gassource).

- `HandbrakeSource`: Exposes handbrake as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#handbrakesource).

- `IndicatorSwitchBinding`: Connects a switch animator to Lights indicator requests and current state; use for a working indicator stalk. Requirements / collaborators: Lights (lights); SwitchAnimator (switchAnimator). [Settings](InspectorReference/Interior.md#indicatorswitchbinding).

- `PitchSource`: Exposes pitch as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#pitchsource).

- `ProfileSwitchBinding`: Connects switch positions to registered drive-profile selection; use for a cockpit mode selector. Requirements / collaborators: VehicleController (vehicle); ProfileSwitcher (profileSwitcher); SwitchAnimator (switchAnimator). [Settings](InspectorReference/Interior.md#profileswitchbinding).

- `RollSource`: Exposes roll as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#rollsource).

- `ServiceBrakeSource`: Exposes service brake as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#servicebrakesource).

- `SpeedValueSource`: Exposes vehicle speed to interior instruments; configure the desired units and vehicle binding. Requirements / collaborators: VehicleController (vehicle). [Settings](InspectorReference/Interior.md#speedvaluesource).

- `SteeringSource`: Exposes steering as a value for control/instrument animation; bind to the relevant vehicle state. Requirements / collaborators: Assign the geometry and owning system described in the linked settings. [Settings](InspectorReference/Interior.md#steeringsource).

### Physics

Use for contact, grip, collision or damage support. Wheel-dependent features need native contact wheels; deformation requires supported readable meshes and damage requires registered part boundaries.

#### Modules

- `AirplaneGroundContact`: Tracks ground support and ground/air authority blending. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Drive.md#airplanegroundcontact).

- `Coasting`: Releases native low-speed sticky wheel behavior on slopes under its torque and brake limits. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Physics.md#coasting).

- `Damage`: Routes accepted collisions and scripted hits to damage boundaries, deformation and detachment; add for damageable vehicles. Requirements / collaborators: VehicleController registration; VehicleMeshDeformation; registered DamagePart/WheelPart boundaries; optional impact profiles. [Settings](InspectorReference/Physics.md#damage).

- `Friction`: Reads physical grip and writes native tire friction behavior. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Physics.md#friction).

- `VehicleMeshDeformation`: Owns readable mesh instances, dent buffers and geometry restoration. Requirements / collaborators: VehicleController registration; readable MeshFilter meshes belonging to prepared damage boundaries. [Settings](InspectorReference/Physics.md#vehiclemeshdeformation).

- `TireCollision`: Adds supplemental solid tire contacts. Requirements / collaborators: VehicleController registration; Wheel (wheel). [Settings](InspectorReference/Physics.md#tirecollision).

- `WheelDynamics`: Applies wheel rotational behavior including airborne losses. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/Physics.md#wheeldynamics).

#### Helpers

- `DamageCollisionRelay`: Relays relevant native collisions into damage handling. Requirements / collaborators: Owning Damage component and collider/contact source; normally installed by damage setup. [Settings](InspectorReference/Physics.md#damagecollisionrelay).

- `Surface`: Stores the physical grip multiplier on a contact collider. Requirements / collaborators: Collider on the contacted world surface; grip multiplier for Friction. [Settings](InspectorReference/Physics.md#surface).

- `Wheel`: Adapts a native WheelCollider and presents the assigned wheel/caliper geometry; one per configured contact wheel. Requirements / collaborators: Native WheelCollider; owning controller wheel setup; visual wheel/caliper roots as needed. [Settings](InspectorReference/Physics.md#wheel).

### World

Use for occupants, cameras, weapons, towing and water. Assign seats/characters, camera anchors, payloads, hitch partners or water providers according to the feature. Nested helpers belong to their local owner.

#### Modules

- `Cameras`: Optional vehicle camera owner. It moves an explicitly assigned camera only while the selected submodule is Active. It releases ownership when inactive, detached or disabled. Requirements / collaborators: VehicleController registration; CameraModule (customModule). [Settings](InspectorReference/World.md#cameras).

- `Coupler`: Validates and owns one hitch relationship, joint and changed collision pairs. Requirements / collaborators: VehicleController registration; VehicleController (vehicle); Trailer (initialTrailer). [Settings](InspectorReference/World.md#coupler).

- `ObjectDropper`: Validates selected payload release and cooldown. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/World.md#objectdropper).

- `Passengers`: Discovers owned handles and supplies input before seat work. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/World.md#passengers).

- `RocketLauncher`: Selects and launches configured mounted rocket stores. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/World.md#rocketlauncher).

- `Trailer`: Stores the towed-body connection and brake-following behavior. Requirements / collaborators: VehicleController registration. [Settings](InspectorReference/World.md#trailer).

- `WaterInteraction`: Connects vehicle water sampling and hull contact state. Requirements / collaborators: VehicleController registration; WaterProvider and authored hull/sample points. [Settings](InspectorReference/World.md#waterinteraction).

- `WeaponBarrel`: Owns muzzle aiming, trigger/cooldown admission and projectile initialization. Requirements / collaborators: VehicleController registration; WeaponEffects; WeaponRecoil; MovingPart (movement). [Settings](InspectorReference/World.md#weaponbarrel).

#### Helpers

- `AccessAnimationEvents`: Relays animation access markers into the sequence. Requirements / collaborators: PassengerAccess/motion owner and Animator event configuration. [Settings](InspectorReference/World.md#accessanimationevents).

- `AdaptiveHandGrip`: Binds a character to a surface and applies fitted finger poses. Requirements / collaborators: SteeringWheelHandle (wheel); VehicleHandle (Handle). [Settings](InspectorReference/World.md#adaptivehandgrip).

- `AnchorHandle`: Exposes authored hand/foot anchors without control animation. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#anchorhandle).

- `BalanceRider`: Configurable foot poses and optional physical rider support for seated or standing riders on motorcycles, bicycles, scooters and other vehicles. Requirements / collaborators: Passenger behavior owner, seat/character and configured foot/support targets. [Settings](InspectorReference/World.md#balancerider).

- `CustomPassengerBody`: Minimal body for application-owned Custom occupancy. Requirements / collaborators: PassengerSeat/Passengers ownership; application-provided occupancy behavior. [Settings](InspectorReference/World.md#custompassengerbody).

- `DroppableObject`: Detaches the actual payload and establishes released physics. Requirements / collaborators: ObjectDropper payload entry; releasable object with suitable physics geometry. [Settings](InspectorReference/World.md#droppableobject).

- `GearLeverHandle`: Defines an IK palm contact on a moving gear lever; pair with the lever animator when a passenger should operate it. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#gearleverhandle).

- `GearPaddleHandle`: Defines an IK palm contact on a moving shift paddle; pair with the paddle animator for passenger hand motion. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#gearpaddlehandle).

- `HandGrip`: Stores character hand frames and fallback finger poses. Requirements / collaborators: Character hand/finger transforms and authored fallback poses. [Settings](InspectorReference/World.md#handgrip).

- `HandleAnimatorBinding`: Binds animation or Timeline values to a passenger handle before the normal IK overlay; use when a clip controls handle feedback. Requirements / collaborators: PassengerSeat (seat); VehicleHandle (handle); VehicleHandle (ResolvedHandle). [Settings](InspectorReference/World.md#handleanimatorbinding).

- `HumanoidAccessMotion`: Built-in Animator-based humanoid access implementation. Requirements / collaborators: AccessAnimationProfile (defaultProfile). [Settings](InspectorReference/World.md#humanoidaccessmotion).

- `HumanoidIK`: Uses character frames to resolve limb targets. Requirements / collaborators: Humanoid character rig and passenger-owned limb/handle targets. [Settings](InspectorReference/World.md#humanoidik).

- `HumanoidPassenger`: Connects humanoid rig, pose and physical passenger behavior. Requirements / collaborators: HumanoidIK (ik). [Settings](InspectorReference/World.md#humanoidpassenger).

- `InteriorCamera`: Exact cabin-anchor follow with bounded mouse look and configurable camera lens. Requirements / collaborators: Cameras owner, explicit camera and cabin anchor. [Settings](InspectorReference/World.md#interiorcamera).

- `JoystickHandle`: Defines aircraft-stick hand contacts; pair with SteeringStickAnimator for stick motion and passenger IK. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#joystickhandle).

- `MotorcycleHandle`: Supplies fixed left/right contacts with prepared finger poses. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#motorcyclehandle).

- `OrbitCamera`: Mouse orbit, scroll zoom, smoothed framing and obstruction avoidance around an explicit anchor. Requirements / collaborators: Cameras owner, explicit camera and follow anchor; collision settings for obstruction checks. [Settings](InspectorReference/World.md#orbitcamera).

- `PassengerAccess`: Owns the entry/exit state machine, reservation and cancellation. Requirements / collaborators: PassengerBody (passenger); AccessMotion (motion). [Settings](InspectorReference/World.md#passengeraccess).

- `PassengerSeat`: Owns one occupant slot and its controller/pose bindings; add per usable seat and register with Passengers. Requirements / collaborators: PassengerBody (bodyPrefab); PassengerBody (body). [Settings](InspectorReference/World.md#passengerseat).

- `PedalHandle`: Defines the passenger foot/ankle contact for a pedal; pair with its pedal animator. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#pedalhandle).

- `RagdollCollisionHelper`: Supports collision policy for physical passenger bodies; use with the owning ragdoll configuration. Requirements / collaborators: HumanoidPassenger ragdoll bodies/colliders and configured collision ownership. [Settings](InspectorReference/World.md#ragdollcollisionhelper).

- `RagdollCollisionRelay`: Forwards physical passenger contacts to the owning passenger system; use on configured ragdoll bodies. Requirements / collaborators: Owning physical passenger and the ragdoll collision source. [Settings](InspectorReference/World.md#ragdollcollisionrelay).

- `Rocket`: Owns launched-rocket motor, collision and lifetime behavior. Requirements / collaborators: RocketLauncher store/prefab setup; Rigidbody/collider and configured motor/lifetime. [Settings](InspectorReference/World.md#rocket).

- `RotaryHandle`: Defines hand contact on a rotary control; pair with a rotary animator for an operated dial. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#rotaryhandle).

- `SeatAccess`: Describes the seat endpoint, outside marker, door and admission settings. Requirements / collaborators: PassengerSeat (seat); VehicleBodyPart (door); AccessAnimationProfile (animationProfile). [Settings](InspectorReference/World.md#seataccess).

- `SteeringHandRegrip`: Coordinates steering contacts, availability and external reservations. Requirements / collaborators: Passenger behavior owner; steering-wheel surface, animator and hand configuration. [Settings](InspectorReference/World.md#steeringhandregrip).

- `SteeringWheelHandle`: Describes steering contacts, surface geometry and hand participation. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#steeringwheelhandle).

- `SwitchHandle`: Defines hand contact on a discrete switch; pair with its switch animator and interaction. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#switchhandle).

- `ThrottleHandle`: Defines hand contact on a throttle lever; pair with ThrottleAnimator for the visible lever motion. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#throttlehandle).

- `WaterSurface`: Built-in water-surface provider implementation. Requirements / collaborators: Authored water geometry/level and sampling settings; optional WaterSurfaceProfile. [Settings](InspectorReference/World.md#watersurface).

- `YokeHandle`: Describes steering contacts, surface geometry and hand participation. Requirements / collaborators: Passengers / seat handle owner. [Settings](InspectorReference/World.md#yokehandle).

### Shared assets and extension bases

DriveProfile assets select movement algorithms; the built-in profiles cover wheeled, motorcycle, tracked, free, hover, air/airplane/aerobatic/jet/helicopter, boat and submarine movement. ProfileTransition and HoverDriveTransition are route components rather than additional drive profiles.

- `AccessAnimationProfile`: Stores animation states, references and timing configuration.
- `DamageImpactProfile`: Reusable immutable-at-playback configuration; cooldown/pool state belongs to each vehicle.
- `EngineSoundProfile`: Stores engine sound behavior and asset configuration.
- `HandleHandPositionProfile`: ScriptableObject created with **Create > UltraVehicleSystem > Controls > Hand Position Profile**. Its `left` and `right` HandleHandPose blocks are shared by every referencing handle; **Local** makes an independent copy. See Reusable hand positions.
- `TireSurfaceProfile`: Stores presentation assets and effect multipliers.
- `WaterSurfaceProfile`: Stores shared water presentation configuration; assign to water presentation components.

Abstract category bases, AudioModule, CameraModule, PassengerBehaviour, PassengerBody, VehicleHandle, ControlAnimator, value-source bases and WaterProvider are extension contracts. Derive a concrete implementation; do not install a second generic base to make a helper run. See Architecture and the scripting reference for their nested ownership and lifecycle.

## Optional presentation receivers

- `NitroAudio` observes Nitro output sessions, including internal gear changes.
- `DamageFeedback` observes accepted Damage hits and owns its visual pool.
- `VehicleMeshDeformation` receives pre-detachment deformation requests and observes repairs, including while deformation is disabled.
- `MovingPartAudio` follows an `IPartMotionSource`, including MovingPart and VehicleBodyPart.
- `WipersAudio` receives stroke notifications with stable blade IDs and resolved speed.
- `ProfileTransitionAudio` receives admitted transition requests.

`IVehicleResetHandler` receives synchronous `Respawn` or `ForceStateChanged` resets. `IVehicleInputReset` clears optional source state during respawn. These contracts keep reset ordering explicit while allowing custom modules. `IHandAvailabilitySource` answers whether a particular seat/hand can be used; interaction animators do not depend on a particular regrip implementation.
