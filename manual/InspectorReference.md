# Complete Inspector settings reference

This final reference covers every editable Inspector field declared by the package runtime components, their base classes, referenced configuration blocks, profile types and the shipped demo components. The tables include serialized private fields as well as public settings. Internal caches hidden from the Inspector, runtime-only properties, methods and development verification tools are outside this reference.

## How to use this reference

- Find a component in the alphabetical index below, or open a system chapter.
- The Setting column gives the serialized field name. Unity normally displays a spaced label; custom inspectors may group or rename it.
- Follow Inherited settings to see fields from base classes. Follow linked types to expand a nested configuration block or inspect a referenced package component.
- Declared defaults are source initializers for a new component/data block, not the tuned values in a saved prefab. Constructors, selected drive profiles, setup commands and runtime binding can replace them. Range/Min entries describe Inspector constraints, not every validation rule.
- Reference fields start unassigned unless initialized in source. Assign required model, body, animation, input and effect references before using the feature.
- Speed fields use the selected Inspector display unit; each row states the stored unit. Other vector/angle frames depend on the component description.
- The component enabled checkbox controls component availability. Additional per-feature switches only change that feature. Active, enabled and camera assignment can be separate states.

## Configuration ownership

Vehicle Controller → Wheels → Wheel Setup owns registered Wheel geometry, roles and visual references. Those copied fields are read-only in Wheel; its local visual smoothing remains editable. Apply Vehicle Configuration copies the authored wheel setup and module tuning to native components.

Suspension owns native WheelCollider spring, damper, travel and force application settings. Configure these in Vehicle Settings/Suspension; an overriding ShockAbsorber can supply per-wheel physical settings. A native WheelCollider edit can be replaced on the next configuration.

Use the [Inspector overview](InspectorConfiguration.md) for grouped tabs, module visibility and subclass configuration, and the [configuration guide](Configuration.md) for the setup workflow.

## Chapters

| System | Reference |
| --- | --- |
| Vehicle controller and input | [Controller](InspectorReference/Controller.md) |
| Engine, fuel and transmission | [Engine](InspectorReference/Engine.md) |
| Drive profiles, steering and suspension | [Drive](InspectorReference/Drive.md) |
| Wheels, contact and damage | [Physics](InspectorReference/Physics.md) |
| Body, lights, wipers and aircraft equipment | [Exterior](InspectorReference/Exterior.md) |
| Interior controls and instruments | [Interior](InspectorReference/Interior.md) |
| Cameras, passengers, water, towing and weapons | [World](InspectorReference/World.md) |
| Audio, particles and feedback | [Effects](InspectorReference/Effects.md) |
| Common settings and base components | [Common](InspectorReference/Common.md) |
| Demo components and examples | [Demo](InspectorReference/Demo.md) |

## Alphabetical component and data index

| Component or data block | Chapter |
| --- | --- |
| [AccessAnimationEvents](InspectorReference/World.md#accessanimationevents) | Cameras, passengers, water, towing and weapons |
| [AccessAnimationProfile](InspectorReference/World.md#accessanimationprofile) | Cameras, passengers, water, towing and weapons |
| [AccessMotion](InspectorReference/World.md#accessmotion) | Cameras, passengers, water, towing and weapons |
| [ActionInput](InspectorReference/Controller.md#actioninput) | Vehicle controller and input |
| [AdaptiveHandGrip](InspectorReference/World.md#adaptivehandgrip) | Cameras, passengers, water, towing and weapons |
| [AdaptiveHandGrip.Finger](InspectorReference/World.md#adaptivehandgripfinger) | Cameras, passengers, water, towing and weapons |
| [AimingHandDemo](InspectorReference/Demo.md#aiminghanddemo) | Demo components and examples |
| [AircraftControlMotion](InspectorReference/Exterior.md#aircraftcontrolmotion) | Body, lights, wipers and aircraft equipment |
| [AircraftControlSurface](InspectorReference/Exterior.md#aircraftcontrolsurface) | Body, lights, wipers and aircraft equipment |
| [AircraftControlSurfaces](InspectorReference/Exterior.md#aircraftcontrolsurfaces) | Body, lights, wipers and aircraft equipment |
| [AircraftHud](InspectorReference/Interior.md#aircrafthud) | Interior controls and instruments |
| [AircraftSystemsDemo](InspectorReference/Demo.md#aircraftsystemsdemo) | Demo components and examples |
| [AirplaneGroundContact](InspectorReference/Drive.md#airplanegroundcontact) | Drive profiles, steering and suspension |
| [AirplaneProfile](InspectorReference/Drive.md#airplaneprofile) | Drive profiles, steering and suspension |
| [AirplaneWaterLandingSettings](InspectorReference/Drive.md#airplanewaterlandingsettings) | Drive profiles, steering and suspension |
| [AirProfile](InspectorReference/Drive.md#airprofile) | Drive profiles, steering and suspension |
| [AnchoredControlAnimator](InspectorReference/Interior.md#anchoredcontrolanimator) | Interior controls and instruments |
| [AnchoredRotation](InspectorReference/Interior.md#anchoredrotation) | Interior controls and instruments |
| [AnchorHandle](InspectorReference/World.md#anchorhandle) | Cameras, passengers, water, towing and weapons |
| [AnimatorCarDemo](InspectorReference/Demo.md#animatorcardemo) | Demo components and examples |
| [AntiLockBrakes](InspectorReference/Drive.md#antilockbrakes) | Drive profiles, steering and suspension |
| [AntiRoll](InspectorReference/Drive.md#antiroll) | Drive profiles, steering and suspension |
| [AntiRoll.Axle](InspectorReference/Drive.md#antirollaxle) | Drive profiles, steering and suspension |
| [Audio](InspectorReference/Effects.md#audio) | Audio, particles and feedback |
| [AudioClipReplacement](InspectorReference/Effects.md#audioclipreplacement) | Audio, particles and feedback |
| [AudioContextProfile](InspectorReference/Effects.md#audiocontextprofile) | Audio, particles and feedback |
| [AudioContextSettings](InspectorReference/Effects.md#audiocontextsettings) | Audio, particles and feedback |
| [AudioEvent](InspectorReference/Effects.md#audioevent) | Audio, particles and feedback |
| [AudioModule](InspectorReference/Effects.md#audiomodule) | Audio, particles and feedback |
| [AudioSettingsOverride](InspectorReference/Effects.md#audiosettingsoverride) | Audio, particles and feedback |
| [AutomaticGearbox](InspectorReference/Engine.md#automaticgearbox) | Engine, fuel and transmission |
| [BalanceRider](InspectorReference/World.md#balancerider) | Cameras, passengers, water, towing and weapons |
| [BoatProfile](InspectorReference/Drive.md#boatprofile) | Drive profiles, steering and suspension |
| [BoatWaterAudio](InspectorReference/Effects.md#boatwateraudio) | Audio, particles and feedback |
| [BoatWaterParticles](InspectorReference/Effects.md#boatwaterparticles) | Audio, particles and feedback |
| [Body](InspectorReference/Exterior.md#body) | Body, lights, wipers and aircraft equipment |
| [BoostSuspensionSettings](InspectorReference/Drive.md#boostsuspensionsettings) | Drive profiles, steering and suspension |
| [BrakeAudio](InspectorReference/Effects.md#brakeaudio) | Audio, particles and feedback |
| [Brakes](InspectorReference/Drive.md#brakes) | Drive profiles, steering and suspension |
| [Burnout](InspectorReference/Drive.md#burnout) | Drive profiles, steering and suspension |
| [BurnoutSuspensionSettings](InspectorReference/Drive.md#burnoutsuspensionsettings) | Drive profiles, steering and suspension |
| [CameraModule](InspectorReference/World.md#cameramodule) | Cameras, passengers, water, towing and weapons |
| [CameraRigDemo](InspectorReference/Demo.md#camerarigdemo) | Demo components and examples |
| [Cameras](InspectorReference/World.md#cameras) | Cameras, passengers, water, towing and weapons |
| [CargoAttachmentSettings](InspectorReference/World.md#cargoattachmentsettings) | Cameras, passengers, water, towing and weapons |
| [CargoCollisionSettings](InspectorReference/World.md#cargocollisionsettings) | Cameras, passengers, water, towing and weapons |
| [CargoParentRestore](InspectorReference/World.md#cargoparentrestore) | Cameras, passengers, water, towing and weapons |
| [CarHud](InspectorReference/Interior.md#carhud) | Interior controls and instruments |
| [CinematicCameraDemo](InspectorReference/Demo.md#cinematiccamerademo) | Demo components and examples |
| [Clutch](InspectorReference/Engine.md#clutch) | Engine, fuel and transmission |
| [ClutchSource](InspectorReference/Interior.md#clutchsource) | Interior controls and instruments |
| [Coasting](InspectorReference/Physics.md#coasting) | Wheels, contact and damage |
| [Collisions](InspectorReference/Physics.md#collisions) | Wheels, contact and damage |
| [CommandValueSource](InspectorReference/Interior.md#commandvaluesource) | Interior controls and instruments |
| [CommercialAudio](InspectorReference/Effects.md#commercialaudio) | Audio, particles and feedback |
| [ContactEnvelope](InspectorReference/Drive.md#contactenvelope) | Drive profiles, steering and suspension |
| [ControlAnimator](InspectorReference/Interior.md#controlanimator) | Interior controls and instruments |
| [ControlArm](InspectorReference/Drive.md#controlarm) | Drive profiles, steering and suspension |
| [ControlHandle](InspectorReference/World.md#controlhandle) | Cameras, passengers, water, towing and weapons |
| [ControlInteraction](InspectorReference/Interior.md#controlinteraction) | Interior controls and instruments |
| [ControlInteractionAnimationEvents](InspectorReference/Interior.md#controlinteractionanimationevents) | Interior controls and instruments |
| [ControllerModule](InspectorReference/Controller.md#controllermodule) | Vehicle controller and input |
| [ControlsHudDemo](InspectorReference/Demo.md#controlshuddemo) | Demo components and examples |
| [Coupler](InspectorReference/World.md#coupler) | Cameras, passengers, water, towing and weapons |
| [CustomLightGroup](InspectorReference/Exterior.md#customlightgroup) | Body, lights, wipers and aircraft equipment |
| [CustomPassengerBody](InspectorReference/World.md#custompassengerbody) | Cameras, passengers, water, towing and weapons |
| [Damage](InspectorReference/Physics.md#damage) | Wheels, contact and damage |
| [DamageAudio](InspectorReference/Effects.md#damageaudio) | Audio, particles and feedback |
| [DamageAudio.PartDetachmentSound](InspectorReference/Effects.md#damageaudiopartdetachmentsound) | Audio, particles and feedback |
| [DamageCollisionRelay](InspectorReference/Physics.md#damagecollisionrelay) | Wheels, contact and damage |
| [DamageContactAudio](InspectorReference/Effects.md#damagecontactaudio) | Audio, particles and feedback |
| [DamageContactEvent](InspectorReference/Effects.md#damagecontactevent) | Audio, particles and feedback |
| [DamageContactLimiter](InspectorReference/World.md#damagecontactlimiter) | Cameras, passengers, water, towing and weapons |
| [DamageContactRelay](InspectorReference/Effects.md#damagecontactrelay) | Audio, particles and feedback |
| [DamageControlsDemo](InspectorReference/Demo.md#damagecontrolsdemo) | Demo components and examples |
| [DamageEffectEvent](InspectorReference/Effects.md#damageeffectevent) | Audio, particles and feedback |
| [DamageFeedback](InspectorReference/Effects.md#damagefeedback) | Audio, particles and feedback |
| [DamageFeedbackProfile](InspectorReference/Effects.md#damagefeedbackprofile) | Audio, particles and feedback |
| [DamageGroundImpactSettings](InspectorReference/Effects.md#damagegroundimpactsettings) | Audio, particles and feedback |
| [DamageHitSoundEvent](InspectorReference/Effects.md#damagehitsoundevent) | Audio, particles and feedback |
| [DamageImpactAudioSequence](InspectorReference/Effects.md#damageimpactaudiosequence) | Audio, particles and feedback |
| [DamageImpactProfile](InspectorReference/Effects.md#damageimpactprofile) | Audio, particles and feedback |
| [DamageLandingAudioResponse](InspectorReference/Effects.md#damagelandingaudioresponse) | Audio, particles and feedback |
| [DamagePart](InspectorReference/Exterior.md#damagepart) | Body, lights, wipers and aircraft equipment |
| [DamageParticles](InspectorReference/Effects.md#damageparticles) | Audio, particles and feedback |
| [DamagePartSoundEvent](InspectorReference/Effects.md#damagepartsoundevent) | Audio, particles and feedback |
| [DamageSoundBank](InspectorReference/Effects.md#damagesoundbank) | Audio, particles and feedback |
| [DamageSoundEvent](InspectorReference/Effects.md#damagesoundevent) | Audio, particles and feedback |
| [DamageSoundGroup](InspectorReference/Effects.md#damagesoundgroup) | Audio, particles and feedback |
| [DamageSurface](InspectorReference/Effects.md#damagesurface) | Audio, particles and feedback |
| [DamageSurfaceResponse](InspectorReference/Effects.md#damagesurfaceresponse) | Audio, particles and feedback |
| [DayNightDemo](InspectorReference/Demo.md#daynightdemo) | Demo components and examples |
| [DebrisMotion](InspectorReference/Physics.md#debrismotion) | Wheels, contact and damage |
| [DefaultParticlePreset](InspectorReference/Effects.md#defaultparticlepreset) | Audio, particles and feedback |
| [Differential](InspectorReference/Engine.md#differential) | Engine, fuel and transmission |
| [Differential.Axle](InspectorReference/Engine.md#differentialaxle) | Engine, fuel and transmission |
| [DirectController](InspectorReference/Controller.md#directcontroller) | Vehicle controller and input |
| [DirectWaypointAIDemo](InspectorReference/Demo.md#directwaypointaidemo) | Demo components and examples |
| [DownforceModuleDemo](InspectorReference/Demo.md#downforcemoduledemo) | Demo components and examples |
| [Drive](InspectorReference/Drive.md#drive) | Drive profiles, steering and suspension |
| [DriveModule](InspectorReference/Drive.md#drivemodule) | Drive profiles, steering and suspension |
| [DriveProfile](InspectorReference/Drive.md#driveprofile) | Drive profiles, steering and suspension |
| [DriveProfileSlot](InspectorReference/Drive.md#driveprofileslot) | Drive profiles, steering and suspension |
| [DrivingAssists](InspectorReference/Drive.md#drivingassists) | Drive profiles, steering and suspension |
| [DroppableObject](InspectorReference/World.md#droppableobject) | Cameras, passengers, water, towing and weapons |
| [DynamicObstacle](InspectorReference/Physics.md#dynamicobstacle) | Wheels, contact and damage |
| [EffectsModule](InspectorReference/Effects.md#effectsmodule) | Audio, particles and feedback |
| [Engine](InspectorReference/Engine.md#engine) | Engine, fuel and transmission |
| [EngineAudio](InspectorReference/Effects.md#engineaudio) | Audio, particles and feedback |
| [EngineAudioItem](InspectorReference/Effects.md#engineaudioitem) | Audio, particles and feedback |
| [EngineAudioModeDemo](InspectorReference/Demo.md#engineaudiomodedemo) | Demo components and examples |
| [EngineModule](InspectorReference/Engine.md#enginemodule) | Engine, fuel and transmission |
| [EngineRpmSource](InspectorReference/Interior.md#enginerpmsource) | Interior controls and instruments |
| [EngineSoundProfile](InspectorReference/Effects.md#enginesoundprofile) | Audio, particles and feedback |
| [EventAudio](InspectorReference/Effects.md#eventaudio) | Audio, particles and feedback |
| [Events](InspectorReference/Effects.md#events) | Audio, particles and feedback |
| [ExhaustSmoke](InspectorReference/Effects.md#exhaustsmoke) | Audio, particles and feedback |
| [ExteriorModule](InspectorReference/Exterior.md#exteriormodule) | Body, lights, wipers and aircraft equipment |
| [ExternalControlDemo](InspectorReference/Demo.md#externalcontroldemo) | Demo components and examples |
| [ExternalControlDemo.GizmoSettings](InspectorReference/Demo.md#externalcontroldemogizmosettings) | Demo components and examples |
| [ExternalController](InspectorReference/Controller.md#externalcontroller) | Vehicle controller and input |
| [FreeCameraDemo](InspectorReference/Demo.md#freecamerademo) | Demo components and examples |
| [FreeCameraMotionDemo](InspectorReference/Demo.md#freecameramotiondemo) | Demo components and examples |
| [FreeParentCameraDemo](InspectorReference/Demo.md#freeparentcamerademo) | Demo components and examples |
| [FreeProfile](InspectorReference/Drive.md#freeprofile) | Drive profiles, steering and suspension |
| [Friction](InspectorReference/Physics.md#friction) | Wheels, contact and damage |
| [FuelTank](InspectorReference/Engine.md#fueltank) | Engine, fuel and transmission |
| [GasSource](InspectorReference/Interior.md#gassource) | Interior controls and instruments |
| [Gearbox](InspectorReference/Engine.md#gearbox) | Engine, fuel and transmission |
| [GearLeverAnimator](InspectorReference/Interior.md#gearleveranimator) | Interior controls and instruments |
| [GearLeverHandle](InspectorReference/World.md#gearleverhandle) | Cameras, passengers, water, towing and weapons |
| [GearLeverPosition](InspectorReference/Interior.md#gearleverposition) | Interior controls and instruments |
| [GearPaddleAnimator](InspectorReference/Interior.md#gearpaddleanimator) | Interior controls and instruments |
| [GearPaddleHandle](InspectorReference/World.md#gearpaddlehandle) | Cameras, passengers, water, towing and weapons |
| [GearShiftAnimator](InspectorReference/Interior.md#gearshiftanimator) | Interior controls and instruments |
| [HalfShaft](InspectorReference/Drive.md#halfshaft) | Drive profiles, steering and suspension |
| [HandbrakeSource](InspectorReference/Interior.md#handbrakesource) | Interior controls and instruments |
| [HandGrip](InspectorReference/World.md#handgrip) | Cameras, passengers, water, towing and weapons |
| [HandGrip.FingerPose](InspectorReference/World.md#handgripfingerpose) | Cameras, passengers, water, towing and weapons |
| [HandleAnimationEvents](InspectorReference/World.md#handleanimationevents) | Cameras, passengers, water, towing and weapons |
| [HandleAnimatorBinding](InspectorReference/World.md#handleanimatorbinding) | Cameras, passengers, water, towing and weapons |
| [HandleAnimatorController](InspectorReference/World.md#handleanimatorcontroller) | Cameras, passengers, water, towing and weapons |
| [HandleAudio](InspectorReference/Effects.md#handleaudio) | Audio, particles and feedback |
| [HandleAudioCue](InspectorReference/Effects.md#handleaudiocue) | Audio, particles and feedback |
| [HandleContactContext](InspectorReference/World.md#handlecontactcontext) | Cameras, passengers, water, towing and weapons |
| [HandleFingerPosition](InspectorReference/World.md#handlefingerposition) | Cameras, passengers, water, towing and weapons |
| [HandleHandPose](InspectorReference/World.md#handlehandpose) | Cameras, passengers, water, towing and weapons |
| [HandleHandPosition](InspectorReference/World.md#handlehandposition) | Cameras, passengers, water, towing and weapons |
| [HandleHandPositionProfile](InspectorReference/World.md#handlehandpositionprofile) | Cameras, passengers, water, towing and weapons |
| [HandleMotion](InspectorReference/Interior.md#handlemotion) | Interior controls and instruments |
| [HandlePoseSettings](InspectorReference/World.md#handleposesettings) | Cameras, passengers, water, towing and weapons |
| [HandleTransitTarget](InspectorReference/World.md#handletransittarget) | Cameras, passengers, water, towing and weapons |
| [HandleUseSettings](InspectorReference/World.md#handleusesettings) | Cameras, passengers, water, towing and weapons |
| [HandleValueContext](InspectorReference/World.md#handlevaluecontext) | Cameras, passengers, water, towing and weapons |
| [HelicopterProfile](InspectorReference/Drive.md#helicopterprofile) | Drive profiles, steering and suspension |
| [HornAudio](InspectorReference/Effects.md#hornaudio) | Audio, particles and feedback |
| [HoverDriveTransition](InspectorReference/Drive.md#hoverdrivetransition) | Drive profiles, steering and suspension |
| [HoverProfile](InspectorReference/Drive.md#hoverprofile) | Drive profiles, steering and suspension |
| [HoverVisuals](InspectorReference/Exterior.md#hovervisuals) | Body, lights, wipers and aircraft equipment |
| [HoverVisuals.TiltMount](InspectorReference/Exterior.md#hovervisualstiltmount) | Body, lights, wipers and aircraft equipment |
| [HudDemo](InspectorReference/Demo.md#huddemo) | Demo components and examples |
| [HumanoidAccessMotion](InspectorReference/World.md#humanoidaccessmotion) | Cameras, passengers, water, towing and weapons |
| [HumanoidIK](InspectorReference/World.md#humanoidik) | Cameras, passengers, water, towing and weapons |
| [HumanoidJointDefinition](InspectorReference/World.md#humanoidjointdefinition) | Cameras, passengers, water, towing and weapons |
| [HumanoidPassenger](InspectorReference/World.md#humanoidpassenger) | Cameras, passengers, water, towing and weapons |
| [IndicatorAudio](InspectorReference/Effects.md#indicatoraudio) | Audio, particles and feedback |
| [IndicatorSwitchBinding](InspectorReference/Interior.md#indicatorswitchbinding) | Interior controls and instruments |
| [InputBuffer](InspectorReference/Controller.md#inputbuffer) | Vehicle controller and input |
| [InputGate](InspectorReference/Controller.md#inputgate) | Vehicle controller and input |
| [InputGate.Route](InspectorReference/Controller.md#inputgateroute) | Vehicle controller and input |
| [InstrumentNeedle](InspectorReference/Interior.md#instrumentneedle) | Interior controls and instruments |
| [InteriorCamera](InspectorReference/World.md#interiorcamera) | Cameras, passengers, water, towing and weapons |
| [InteriorModule](InspectorReference/Interior.md#interiormodule) | Interior controls and instruments |
| [InteriorValueSource](InspectorReference/Interior.md#interiorvaluesource) | Interior controls and instruments |
| [JetBlast](InspectorReference/Effects.md#jetblast) | Audio, particles and feedback |
| [JoystickHandle](InspectorReference/World.md#joystickhandle) | Cameras, passengers, water, towing and weapons |
| [KeyboardBoatInput](InspectorReference/Controller.md#keyboardboatinput) | Vehicle controller and input |
| [KeyboardDriveInput](InspectorReference/Controller.md#keyboarddriveinput) | Vehicle controller and input |
| [KeyboardFlightInput](InspectorReference/Controller.md#keyboardflightinput) | Vehicle controller and input |
| [KeyboardInput](InspectorReference/Controller.md#keyboardinput) | Vehicle controller and input |
| [KeyboardSpaceshipInput](InspectorReference/Controller.md#keyboardspaceshipinput) | Vehicle controller and input |
| [KeyboardSubmarineInput](InspectorReference/Controller.md#keyboardsubmarineinput) | Vehicle controller and input |
| [LandingGear](InspectorReference/Exterior.md#landinggear) | Body, lights, wipers and aircraft equipment |
| [LandingGearPart](InspectorReference/Exterior.md#landinggearpart) | Body, lights, wipers and aircraft equipment |
| [LandingGearSuspension](InspectorReference/Exterior.md#landinggearsuspension) | Body, lights, wipers and aircraft equipment |
| [LandingGearSuspensionPart](InspectorReference/Exterior.md#landinggearsuspensionpart) | Body, lights, wipers and aircraft equipment |
| [LandingGearSwitchDemo](InspectorReference/Demo.md#landinggearswitchdemo) | Demo components and examples |
| [LightChannel](InspectorReference/Exterior.md#lightchannel) | Body, lights, wipers and aircraft equipment |
| [LightLensBinding](InspectorReference/Exterior.md#lightlensbinding) | Body, lights, wipers and aircraft equipment |
| [Lights](InspectorReference/Exterior.md#lights) | Body, lights, wipers and aircraft equipment |
| [ManualGearbox](InspectorReference/Engine.md#manualgearbox) | Engine, fuel and transmission |
| [MotorcycleBalance](InspectorReference/Drive.md#motorcyclebalance) | Drive profiles, steering and suspension |
| [MotorcycleGroundAssist](InspectorReference/Drive.md#motorcyclegroundassist) | Drive profiles, steering and suspension |
| [MotorcycleHandle](InspectorReference/World.md#motorcyclehandle) | Cameras, passengers, water, towing and weapons |
| [MotorcycleProfile](InspectorReference/Drive.md#motorcycleprofile) | Drive profiles, steering and suspension |
| [MotorcycleRidersDemo](InspectorReference/Demo.md#motorcycleridersdemo) | Demo components and examples |
| [MotorcycleWheelieControl](InspectorReference/Drive.md#motorcyclewheeliecontrol) | Drive profiles, steering and suspension |
| [MovingPart](InspectorReference/Exterior.md#movingpart) | Body, lights, wipers and aircraft equipment |
| [MovingPartAudio](InspectorReference/Effects.md#movingpartaudio) | Audio, particles and feedback |
| [Nitro](InspectorReference/Engine.md#nitro) | Engine, fuel and transmission |
| [NitroAudio](InspectorReference/Effects.md#nitroaudio) | Audio, particles and feedback |
| [ObjectDropper](InspectorReference/World.md#objectdropper) | Cameras, passengers, water, towing and weapons |
| [OrbitCamera](InspectorReference/World.md#orbitcamera) | Cameras, passengers, water, towing and weapons |
| [OrbitCameraGround](InspectorReference/World.md#orbitcameraground) | Cameras, passengers, water, towing and weapons |
| [ParkingHold](InspectorReference/Drive.md#parkinghold) | Drive profiles, steering and suspension |
| [PartClipAnimation](InspectorReference/Exterior.md#partclipanimation) | Body, lights, wipers and aircraft equipment |
| [PartMotionAudio](InspectorReference/Exterior.md#partmotionaudio) | Body, lights, wipers and aircraft equipment |
| [PartMotionEvents](InspectorReference/Exterior.md#partmotionevents) | Body, lights, wipers and aircraft equipment |
| [PartMotionPlayback](InspectorReference/Exterior.md#partmotionplayback) | Body, lights, wipers and aircraft equipment |
| [PartMotionSignals](InspectorReference/Exterior.md#partmotionsignals) | Body, lights, wipers and aircraft equipment |
| [PassengerAccess](InspectorReference/World.md#passengeraccess) | Cameras, passengers, water, towing and weapons |
| [PassengerAccessDemo](InspectorReference/Demo.md#passengeraccessdemo) | Demo components and examples |
| [PassengerAnimatorLayers](InspectorReference/World.md#passengeranimatorlayers) | Cameras, passengers, water, towing and weapons |
| [PassengerAnimatorLayers.Layer](InspectorReference/World.md#passengeranimatorlayerslayer) | Cameras, passengers, water, towing and weapons |
| [PassengerBehaviour](InspectorReference/World.md#passengerbehaviour) | Cameras, passengers, water, towing and weapons |
| [PassengerBody](InspectorReference/World.md#passengerbody) | Cameras, passengers, water, towing and weapons |
| [PassengerBodyPartConfig](InspectorReference/World.md#passengerbodypartconfig) | Cameras, passengers, water, towing and weapons |
| [PassengerCollisionEjection](InspectorReference/World.md#passengercollisionejection) | Cameras, passengers, water, towing and weapons |
| [PassengerCollisionSurface](InspectorReference/World.md#passengercollisionsurface) | Cameras, passengers, water, towing and weapons |
| [PassengerFootConfig](InspectorReference/World.md#passengerfootconfig) | Cameras, passengers, water, towing and weapons |
| [PassengerGForceLimits](InspectorReference/World.md#passengergforcelimits) | Cameras, passengers, water, towing and weapons |
| [PassengerHandConfig](InspectorReference/World.md#passengerhandconfig) | Cameras, passengers, water, towing and weapons |
| [PassengerHandleVariant](InspectorReference/World.md#passengerhandlevariant) | Cameras, passengers, water, towing and weapons |
| [PassengerJointSupport](InspectorReference/World.md#passengerjointsupport) | Cameras, passengers, water, towing and weapons |
| [PassengerLimbDamageFeedback](InspectorReference/World.md#passengerlimbdamagefeedback) | Cameras, passengers, water, towing and weapons |
| [PassengerModule](InspectorReference/World.md#passengermodule) | Cameras, passengers, water, towing and weapons |
| [PassengerParentRestore](InspectorReference/World.md#passengerparentrestore) | Cameras, passengers, water, towing and weapons |
| [PassengerPhysicalAnimationSettings](InspectorReference/World.md#passengerphysicalanimationsettings) | Cameras, passengers, water, towing and weapons |
| [PassengerRestraints](InspectorReference/World.md#passengerrestraints) | Cameras, passengers, water, towing and weapons |
| [Passengers](InspectorReference/World.md#passengers) | Cameras, passengers, water, towing and weapons |
| [PassengerSeat](InspectorReference/World.md#passengerseat) | Cameras, passengers, water, towing and weapons |
| [PassengerSeatContext](InspectorReference/World.md#passengerseatcontext) | Cameras, passengers, water, towing and weapons |
| [PassengerTransformSupport](InspectorReference/World.md#passengertransformsupport) | Cameras, passengers, water, towing and weapons |
| [PassengerVariant](InspectorReference/World.md#passengervariant) | Cameras, passengers, water, towing and weapons |
| [PassengerVariants](InspectorReference/World.md#passengervariants) | Cameras, passengers, water, towing and weapons |
| [PedalAnimator](InspectorReference/Interior.md#pedalanimator) | Interior controls and instruments |
| [PedalDrive](InspectorReference/Exterior.md#pedaldrive) | Body, lights, wipers and aircraft equipment |
| [PedalHandle](InspectorReference/World.md#pedalhandle) | Cameras, passengers, water, towing and weapons |
| [PhysicsModule](InspectorReference/Physics.md#physicsmodule) | Wheels, contact and damage |
| [PitchSource](InspectorReference/Interior.md#pitchsource) | Interior controls and instruments |
| [PowerWindowsDemo](InspectorReference/Demo.md#powerwindowsdemo) | Demo components and examples |
| [ProfileSwitchBinding](InspectorReference/Interior.md#profileswitchbinding) | Interior controls and instruments |
| [ProfileSwitcher](InspectorReference/Drive.md#profileswitcher) | Drive profiles, steering and suspension |
| [ProfileTransition](InspectorReference/Drive.md#profiletransition) | Drive profiles, steering and suspension |
| [ProfileTransitionAudio](InspectorReference/Effects.md#profiletransitionaudio) | Audio, particles and feedback |
| [ProfileTransitionAudio.TransitionSound](InspectorReference/Effects.md#profiletransitionaudiotransitionsound) | Audio, particles and feedback |
| [ProjectileDemo](InspectorReference/Demo.md#projectiledemo) | Demo components and examples |
| [Propulsion](InspectorReference/Exterior.md#propulsion) | Body, lights, wipers and aircraft equipment |
| [Propulsion.Propeller](InspectorReference/Exterior.md#propulsionpropeller) | Body, lights, wipers and aircraft equipment |
| [PropulsionJets](InspectorReference/Effects.md#propulsionjets) | Audio, particles and feedback |
| [RagdollCollisionHelper](InspectorReference/World.md#ragdollcollisionhelper) | Cameras, passengers, water, towing and weapons |
| [RagdollCollisionRelay](InspectorReference/World.md#ragdollcollisionrelay) | Cameras, passengers, water, towing and weapons |
| [RearMirror](InspectorReference/Interior.md#rearmirror) | Interior controls and instruments |
| [RearMirrors](InspectorReference/Interior.md#rearmirrors) | Interior controls and instruments |
| [RiderAirControl](InspectorReference/World.md#rideraircontrol) | Cameras, passengers, water, towing and weapons |
| [RiderAnimationRule](InspectorReference/World.md#rideranimationrule) | Cameras, passengers, water, towing and weapons |
| [RiderAnimator](InspectorReference/World.md#rideranimator) | Cameras, passengers, water, towing and weapons |
| [RiderCorneringPosture](InspectorReference/World.md#ridercorneringposture) | Cameras, passengers, water, towing and weapons |
| [RiderKneeLean](InspectorReference/World.md#riderkneelean) | Cameras, passengers, water, towing and weapons |
| [RiderMotionState](InspectorReference/World.md#ridermotionstate) | Cameras, passengers, water, towing and weapons |
| [Rocket](InspectorReference/World.md#rocket) | Cameras, passengers, water, towing and weapons |
| [RocketLauncher](InspectorReference/World.md#rocketlauncher) | Cameras, passengers, water, towing and weapons |
| [RollSource](InspectorReference/Interior.md#rollsource) | Interior controls and instruments |
| [RotaryAnimator](InspectorReference/Interior.md#rotaryanimator) | Interior controls and instruments |
| [RotaryHandle](InspectorReference/World.md#rotaryhandle) | Cameras, passengers, water, towing and weapons |
| [SceneGizmoOptions](InspectorReference/Common.md#scenegizmooptions) | Common settings and base components |
| [SeatAccess](InspectorReference/World.md#seataccess) | Cameras, passengers, water, towing and weapons |
| [SelectedVehicleMirrorsDemo](InspectorReference/Demo.md#selectedvehiclemirrorsdemo) | Demo components and examples |
| [ServiceBrakeSource](InspectorReference/Interior.md#servicebrakesource) | Interior controls and instruments |
| [Settings](InspectorReference/Common.md#settings) | Common settings and base components |
| [ShockAbsorber](InspectorReference/Drive.md#shockabsorber) | Drive profiles, steering and suspension |
| [Skidmarks](InspectorReference/Effects.md#skidmarks) | Audio, particles and feedback |
| [SpaceshipProfile](InspectorReference/Drive.md#spaceshipprofile) | Drive profiles, steering and suspension |
| [SpeedValueSource](InspectorReference/Interior.md#speedvaluesource) | Interior controls and instruments |
| [Stabilization](InspectorReference/Physics.md#stabilization) | Wheels, contact and damage |
| [Steering](InspectorReference/Drive.md#steering) | Drive profiles, steering and suspension |
| [SteeringHandRegrip](InspectorReference/World.md#steeringhandregrip) | Cameras, passengers, water, towing and weapons |
| [SteeringHandRegripSettings](InspectorReference/World.md#steeringhandregripsettings) | Cameras, passengers, water, towing and weapons |
| [SteeringPart](InspectorReference/Exterior.md#steeringpart) | Body, lights, wipers and aircraft equipment |
| [SteeringSource](InspectorReference/Interior.md#steeringsource) | Interior controls and instruments |
| [SteeringStickAnimator](InspectorReference/Interior.md#steeringstickanimator) | Interior controls and instruments |
| [SteeringTieRod](InspectorReference/Drive.md#steeringtierod) | Drive profiles, steering and suspension |
| [SteeringWheelAnimator](InspectorReference/Interior.md#steeringwheelanimator) | Interior controls and instruments |
| [SteeringWheelHandle](InspectorReference/World.md#steeringwheelhandle) | Cameras, passengers, water, towing and weapons |
| [SteeringWheelHandle.RimSample](InspectorReference/World.md#steeringwheelhandlerimsample) | Cameras, passengers, water, towing and weapons |
| [SubmarineProfile](InspectorReference/Drive.md#submarineprofile) | Drive profiles, steering and suspension |
| [Surface](InspectorReference/Physics.md#surface) | Wheels, contact and damage |
| [Suspension](InspectorReference/Drive.md#suspension) | Drive profiles, steering and suspension |
| [SuspensionAxle](InspectorReference/Drive.md#suspensionaxle) | Drive profiles, steering and suspension |
| [SuspensionHub](InspectorReference/Drive.md#suspensionhub) | Drive profiles, steering and suspension |
| [SuspensionRotationLimits](InspectorReference/Drive.md#suspensionrotationlimits) | Drive profiles, steering and suspension |
| [SwitchAnimator](InspectorReference/Interior.md#switchanimator) | Interior controls and instruments |
| [SwitchAudio](InspectorReference/Effects.md#switchaudio) | Audio, particles and feedback |
| [SwitchHandle](InspectorReference/World.md#switchhandle) | Cameras, passengers, water, towing and weapons |
| [TelemetrySettings](InspectorReference/Common.md#telemetrysettings) | Common settings and base components |
| [ThrottleAnimator](InspectorReference/Interior.md#throttleanimator) | Interior controls and instruments |
| [ThrottleHandle](InspectorReference/World.md#throttlehandle) | Cameras, passengers, water, towing and weapons |
| [TireAudio](InspectorReference/Effects.md#tireaudio) | Audio, particles and feedback |
| [TireBurnoutSmokeSettings](InspectorReference/Effects.md#tireburnoutsmokesettings) | Audio, particles and feedback |
| [TireCollision](InspectorReference/Physics.md#tirecollision) | Wheels, contact and damage |
| [TireFeedback](InspectorReference/Effects.md#tirefeedback) | Audio, particles and feedback |
| [TireSmoke](InspectorReference/Effects.md#tiresmoke) | Audio, particles and feedback |
| [TireSurface](InspectorReference/Effects.md#tiresurface) | Audio, particles and feedback |
| [TireSurface.LayerMapping](InspectorReference/Effects.md#tiresurfacelayermapping) | Audio, particles and feedback |
| [TireSurfaceProfile](InspectorReference/Effects.md#tiresurfaceprofile) | Audio, particles and feedback |
| [TowingControlsDemo](InspectorReference/Demo.md#towingcontrolsdemo) | Demo components and examples |
| [TrackedProfile](InspectorReference/Drive.md#trackedprofile) | Drive profiles, steering and suspension |
| [TrackPathBuilder](InspectorReference/Exterior.md#trackpathbuilder) | Body, lights, wipers and aircraft equipment |
| [Tracks](InspectorReference/Drive.md#tracks) | Drive profiles, steering and suspension |
| [TrackVisuals](InspectorReference/Exterior.md#trackvisuals) | Body, lights, wipers and aircraft equipment |
| [TrackVisuals.Belt](InspectorReference/Exterior.md#trackvisualsbelt) | Body, lights, wipers and aircraft equipment |
| [TrackVisuals.Roller](InspectorReference/Exterior.md#trackvisualsroller) | Body, lights, wipers and aircraft equipment |
| [TractionControl](InspectorReference/Engine.md#tractioncontrol) | Engine, fuel and transmission |
| [Trailer](InspectorReference/World.md#trailer) | Cameras, passengers, water, towing and weapons |
| [Transmission](InspectorReference/Engine.md#transmission) | Engine, fuel and transmission |
| [TwistThrottleAnimator](InspectorReference/Interior.md#twistthrottleanimator) | Interior controls and instruments |
| [UnderwaterDemo](InspectorReference/Demo.md#underwaterdemo) | Demo components and examples |
| [VehicleAudioSettings](InspectorReference/Effects.md#vehicleaudiosettings) | Audio, particles and feedback |
| [VehicleBodyPart](InspectorReference/Exterior.md#vehiclebodypart) | Body, lights, wipers and aircraft equipment |
| [VehicleCargo](InspectorReference/World.md#vehiclecargo) | Cameras, passengers, water, towing and weapons |
| [VehicleController](InspectorReference/Controller.md#vehiclecontroller) | Vehicle controller and input |
| [VehicleHandle](InspectorReference/World.md#vehiclehandle) | Cameras, passengers, water, towing and weapons |
| [VehicleHandleAnimator](InspectorReference/Interior.md#vehiclehandleanimator) | Interior controls and instruments |
| [VehicleLampGlow](InspectorReference/Exterior.md#vehiclelampglow) | Body, lights, wipers and aircraft equipment |
| [VehicleMeshDeformation](InspectorReference/Physics.md#vehiclemeshdeformation) | Wheels, contact and damage |
| [VehicleModule](InspectorReference/Common.md#vehiclemodule) | Common settings and base components |
| [VehicleSelectorDemo](InspectorReference/Demo.md#vehicleselectordemo) | Demo components and examples |
| [VehicleValueSource](InspectorReference/Interior.md#vehiclevaluesource) | Interior controls and instruments |
| [VehicleWeaponDemo](InspectorReference/Demo.md#vehicleweapondemo) | Demo components and examples |
| [WaterEntryAudioDemo](InspectorReference/Demo.md#waterentryaudiodemo) | Demo components and examples |
| [WaterInteraction](InspectorReference/World.md#waterinteraction) | Cameras, passengers, water, towing and weapons |
| [WaterProvider](InspectorReference/World.md#waterprovider) | Cameras, passengers, water, towing and weapons |
| [WaterSurface](InspectorReference/World.md#watersurface) | Cameras, passengers, water, towing and weapons |
| [WaterSurfaceProfile](InspectorReference/World.md#watersurfaceprofile) | Cameras, passengers, water, towing and weapons |
| [WaypointAIDemo](InspectorReference/Demo.md#waypointaidemo) | Demo components and examples |
| [WeaponBarrel](InspectorReference/World.md#weaponbarrel) | Cameras, passengers, water, towing and weapons |
| [WeaponEffects](InspectorReference/Effects.md#weaponeffects) | Audio, particles and feedback |
| [WeaponRecoil](InspectorReference/Effects.md#weaponrecoil) | Audio, particles and feedback |
| [Wheel](InspectorReference/Physics.md#wheel) | Wheels, contact and damage |
| [WheelDynamics](InspectorReference/Physics.md#wheeldynamics) | Wheels, contact and damage |
| [WheeledProfile](InspectorReference/Drive.md#wheeledprofile) | Drive profiles, steering and suspension |
| [WheelLift](InspectorReference/Physics.md#wheellift) | Wheels, contact and damage |
| [WheelLiftPitchSupport](InspectorReference/Physics.md#wheelliftpitchsupport) | Wheels, contact and damage |
| [WheelPart](InspectorReference/Exterior.md#wheelpart) | Body, lights, wipers and aircraft equipment |
| [WheelSetup](InspectorReference/Physics.md#wheelsetup) | Wheels, contact and damage |
| [Wiper](InspectorReference/Exterior.md#wiper) | Body, lights, wipers and aircraft equipment |
| [WiperAudioEntry](InspectorReference/Effects.md#wiperaudioentry) | Audio, particles and feedback |
| [WiperBlade](InspectorReference/Exterior.md#wiperblade) | Body, lights, wipers and aircraft equipment |
| [Wipers](InspectorReference/Exterior.md#wipers) | Body, lights, wipers and aircraft equipment |
| [WipersAudio](InspectorReference/Effects.md#wipersaudio) | Audio, particles and feedback |
| [WiperSwitchBinding](InspectorReference/Exterior.md#wiperswitchbinding) | Body, lights, wipers and aircraft equipment |
| [WorldModule](InspectorReference/World.md#worldmodule) | Cameras, passengers, water, towing and weapons |
| [YokeAnimator](InspectorReference/Interior.md#yokeanimator) | Interior controls and instruments |
| [YokeHandle](InspectorReference/World.md#yokehandle) | Cameras, passengers, water, towing and weapons |

Coverage: 223 concrete components/assets; 354 component/base/data sections; 3088 declared Inspector fields. Inherited fields are documented once at their declaring type.
