.. _uvs-inspectorreference--complete-inspector-settings-reference:

Complete Inspector settings reference
=====================================

This final reference covers every editable Inspector field declared by the package runtime components, their base classes, referenced configuration blocks, profile types and the shipped demo components. The tables include serialized private fields as well as public settings. Internal caches hidden from the Inspector, runtime-only properties, methods and development verification tools are outside this reference.

.. _uvs-inspectorreference--how-to-use-this-reference:

How to use this reference
-------------------------

-  Find a component in the alphabetical index below, or open a system chapter.
-  The Setting column gives the serialized field name. Unity normally displays a spaced label; custom inspectors may group or rename it.
-  Follow Inherited settings to see fields from base classes. Follow linked types to expand a nested configuration block or inspect a referenced package component.
-  Declared defaults are source initializers for a new component/data block, not the tuned values in a saved prefab. Constructors, selected drive profiles, setup commands and runtime binding can replace them. Range/Min entries describe Inspector constraints, not every validation rule.
-  Reference fields start unassigned unless initialized in source. Assign required model, body, animation, input and effect references before using the feature.
-  Speed fields use the selected Inspector display unit; each row states the stored unit. Other vector/angle frames depend on the component description.
-  The component enabled checkbox controls component availability. Additional per-feature switches only change that feature. Active, enabled and camera assignment can be separate states.

.. _uvs-inspectorreference--configuration-ownership:

Configuration ownership
-----------------------

Vehicle Controller → Wheels → Wheel Setup owns registered Wheel geometry, roles and visual references. Those copied fields are read-only in Wheel; its local visual smoothing remains editable. Apply Vehicle Configuration copies the authored wheel setup and module tuning to native components.

Suspension owns native WheelCollider spring, damper, travel and force application settings. Configure these in Vehicle Settings/Suspension; an overriding ShockAbsorber can supply per-wheel physical settings. A native WheelCollider edit can be replaced on the next configuration.

Use the :doc:`Inspector overview </InspectorConfiguration>` for grouped tabs, module visibility and subclass configuration, and the :doc:`configuration guide </Configuration>` for the setup workflow.

.. _uvs-inspectorreference--chapters:

Chapters
--------

+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| System                                                                                                        | Reference                                      |
+===============================================================================================================+================================================+
| :ref:`AccessAnimationEvents <uvs-inspectorreference-world--accessanimationevents>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AccessAnimationProfile <uvs-inspectorreference-world--accessanimationprofile>`                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AccessMotion <uvs-inspectorreference-world--accessmotion>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ActionInput <uvs-inspectorreference-controller--actioninput>`                                           | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AdaptiveHandGrip.Finger <uvs-inspectorreference-world--adaptivehandgripfinger>`                         | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AdaptiveHandGrip <uvs-inspectorreference-world--adaptivehandgrip>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AerobaticAirplaneProfile <uvs-inspectorreference-drive--aerobaticairplaneprofile>`                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AimingHandDemo <uvs-inspectorreference-demo--aiminghanddemo>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftControlMotion <uvs-inspectorreference-exterior--aircraftcontrolmotion>`                         | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftControlSurface <uvs-inspectorreference-exterior--aircraftcontrolsurface>`                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftControlSurfaces <uvs-inspectorreference-exterior--aircraftcontrolsurfaces>`                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftHud <uvs-inspectorreference-interior--aircrafthud>`                                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftSystemsDemo <uvs-inspectorreference-demo--aircraftsystemsdemo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AirplaneGroundContact <uvs-inspectorreference-drive--airplanegroundcontact>`                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AirplaneProfile <uvs-inspectorreference-drive--airplaneprofile>`                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AirProfile <uvs-inspectorreference-drive--airprofile>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AnchoredControlAnimator <uvs-inspectorreference-interior--anchoredcontrolanimator>`                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AnchoredRotation <uvs-inspectorreference-interior--anchoredrotation>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AnchorHandle <uvs-inspectorreference-world--anchorhandle>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AnimatorCarDemo <uvs-inspectorreference-demo--animatorcardemo>`                                         | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AntiRoll.Axle <uvs-inspectorreference-drive--antirollaxle>`                                             | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AntiRoll <uvs-inspectorreference-drive--antiroll>`                                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Audio <uvs-inspectorreference-effects--audio>`                                                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AudioEvent <uvs-inspectorreference-effects--audioevent>`                                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AudioModule <uvs-inspectorreference-effects--audiomodule>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AudioSettingsOverride <uvs-inspectorreference-effects--audiosettingsoverride>`                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AutomaticGearbox <uvs-inspectorreference-engine--automaticgearbox>`                                     | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BalanceRider <uvs-inspectorreference-world--balancerider>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BoatProfile <uvs-inspectorreference-drive--boatprofile>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BoatWaterAudio <uvs-inspectorreference-effects--boatwateraudio>`                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BoatWaterParticles <uvs-inspectorreference-effects--boatwaterparticles>`                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Body <uvs-inspectorreference-exterior--body>`                                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BrakeAudio <uvs-inspectorreference-effects--brakeaudio>`                                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Brakes <uvs-inspectorreference-drive--brakes>`                                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Burnout <uvs-inspectorreference-drive--burnout>`                                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CameraModule <uvs-inspectorreference-world--cameramodule>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CameraRigDemo <uvs-inspectorreference-demo--camerarigdemo>`                                             | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Cameras <uvs-inspectorreference-world--cameras>`                                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CarHud <uvs-inspectorreference-interior--carhud>`                                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CinematicCameraDemo <uvs-inspectorreference-demo--cinematiccamerademo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Clutch <uvs-inspectorreference-engine--clutch>`                                                         | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ClutchSource <uvs-inspectorreference-interior--clutchsource>`                                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Coasting <uvs-inspectorreference-physics--coasting>`                                                    | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Collisions <uvs-inspectorreference-physics--collisions>`                                                | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CommandValueSource <uvs-inspectorreference-interior--commandvaluesource>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CommercialAudio <uvs-inspectorreference-effects--commercialaudio>`                                      | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ContactEnvelope <uvs-inspectorreference-drive--contactenvelope>`                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`                                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlArm <uvs-inspectorreference-drive--controlarm>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlHandle <uvs-inspectorreference-world--controlhandle>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlInteraction <uvs-inspectorreference-interior--controlinteraction>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlInteractionAnimationEvents <uvs-inspectorreference-interior--controlinteractionanimationevents>` | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControllerModule <uvs-inspectorreference-controller--controllermodule>`                                 | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlsHudDemo <uvs-inspectorreference-demo--controlshuddemo>`                                         | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Coupler <uvs-inspectorreference-world--coupler>`                                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CustomLightGroup <uvs-inspectorreference-exterior--customlightgroup>`                                   | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CustomPassengerBody <uvs-inspectorreference-world--custompassengerbody>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Damage <uvs-inspectorreference-physics--damage>`                                                        | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageAudio <uvs-inspectorreference-effects--damageaudio>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageCollisionRelay <uvs-inspectorreference-physics--damagecollisionrelay>`                            | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageControlsDemo <uvs-inspectorreference-demo--damagecontrolsdemo>`                                   | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageImpactProfile <uvs-inspectorreference-effects--damageimpactprofile>`                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamagePart <uvs-inspectorreference-exterior--damagepart>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DayNightDemo <uvs-inspectorreference-demo--daynightdemo>`                                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DefaultParticlePreset <uvs-inspectorreference-effects--defaultparticlepreset>`                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Differential.Axle <uvs-inspectorreference-engine--differentialaxle>`                                    | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Differential <uvs-inspectorreference-engine--differential>`                                             | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DirectController <uvs-inspectorreference-controller--directcontroller>`                                 | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DirectWaypointAIDemo <uvs-inspectorreference-demo--directwaypointaidemo>`                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DownforceModuleDemo <uvs-inspectorreference-demo--downforcemoduledemo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Drive <uvs-inspectorreference-drive--drive>`                                                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DriveModule <uvs-inspectorreference-drive--drivemodule>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DriveProfile <uvs-inspectorreference-drive--driveprofile>`                                              | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DriveProfileSlot <uvs-inspectorreference-drive--driveprofileslot>`                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DrivingAssists <uvs-inspectorreference-drive--drivingassists>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DroppableObject <uvs-inspectorreference-world--droppableobject>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DynamicObstacle <uvs-inspectorreference-physics--dynamicobstacle>`                                      | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EffectsModule <uvs-inspectorreference-effects--effectsmodule>`                                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Engine <uvs-inspectorreference-engine--engine>`                                                         | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineAudio <uvs-inspectorreference-effects--engineaudio>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineAudioItem <uvs-inspectorreference-effects--engineaudioitem>`                                      | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineAudioModeDemo <uvs-inspectorreference-demo--engineaudiomodedemo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineModule <uvs-inspectorreference-engine--enginemodule>`                                             | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineRpmSource <uvs-inspectorreference-interior--enginerpmsource>`                                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineSoundProfile <uvs-inspectorreference-effects--enginesoundprofile>`                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EventAudio <uvs-inspectorreference-effects--eventaudio>`                                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Events <uvs-inspectorreference-effects--events>`                                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExhaustSmoke <uvs-inspectorreference-effects--exhaustsmoke>`                                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExteriorModule <uvs-inspectorreference-exterior--exteriormodule>`                                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExternalControlDemo.GizmoSettings <uvs-inspectorreference-demo--externalcontroldemogizmosettings>`      | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExternalControlDemo <uvs-inspectorreference-demo--externalcontroldemo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExternalController <uvs-inspectorreference-controller--externalcontroller>`                             | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`FreeCameraDemo <uvs-inspectorreference-demo--freecamerademo>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`FreeCameraMotionDemo <uvs-inspectorreference-demo--freecameramotiondemo>`                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`FreeParentCameraDemo <uvs-inspectorreference-demo--freeparentcamerademo>`                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`FreeProfile <uvs-inspectorreference-drive--freeprofile>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Friction <uvs-inspectorreference-physics--friction>`                                                    | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`FuelTank <uvs-inspectorreference-engine--fueltank>`                                                     | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GasSource <uvs-inspectorreference-interior--gassource>`                                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Gearbox <uvs-inspectorreference-engine--gearbox>`                                                       | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearLeverAnimator <uvs-inspectorreference-interior--gearleveranimator>`                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearLeverHandle <uvs-inspectorreference-world--gearleverhandle>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearLeverPosition <uvs-inspectorreference-interior--gearleverposition>`                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearPaddleAnimator <uvs-inspectorreference-interior--gearpaddleanimator>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearPaddleHandle <uvs-inspectorreference-world--gearpaddlehandle>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearShiftAnimator <uvs-inspectorreference-interior--gearshiftanimator>`                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearShiftDirection <uvs-inspectorreference-interior--gearshiftdirection>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HalfShaft <uvs-inspectorreference-drive--halfshaft>`                                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandbrakeSource <uvs-inspectorreference-interior--handbrakesource>`                                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandGrip.FingerPose <uvs-inspectorreference-world--handgripfingerpose>`                                 | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandGrip <uvs-inspectorreference-world--handgrip>`                                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleAnimatorBinding <uvs-inspectorreference-world--handleanimatorbinding>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleFingerPosition <uvs-inspectorreference-world--handlefingerposition>`                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleHandPose <uvs-inspectorreference-world--handlehandpose>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleHandPosition <uvs-inspectorreference-world--handlehandposition>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleHandPositionProfile <uvs-inspectorreference-world--handlehandpositionprofile>`                    | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleMotion <uvs-inspectorreference-interior--handlemotion>`                                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandlePoseSettings <uvs-inspectorreference-world--handleposesettings>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleUseSettings <uvs-inspectorreference-world--handleusesettings>`                                    | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HelicopterProfile <uvs-inspectorreference-drive--helicopterprofile>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HornAudio <uvs-inspectorreference-effects--hornaudio>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverDriveTransition <uvs-inspectorreference-drive--hoverdrivetransition>`                              | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverProfile <uvs-inspectorreference-drive--hoverprofile>`                                              | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverVisuals.TiltMount <uvs-inspectorreference-exterior--hovervisualstiltmount>`                        | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverVisuals <uvs-inspectorreference-exterior--hovervisuals>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HudDemo <uvs-inspectorreference-demo--huddemo>`                                                         | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidAccessMotion <uvs-inspectorreference-world--humanoidaccessmotion>`                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidIK <uvs-inspectorreference-world--humanoidik>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidJointDefinition <uvs-inspectorreference-world--humanoidjointdefinition>`                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidPassenger <uvs-inspectorreference-world--humanoidpassenger>`                                    | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`IGearShiftAnimator <uvs-inspectorreference-interior--igearshiftanimator>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`IndicatorAudio <uvs-inspectorreference-effects--indicatoraudio>`                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`IndicatorSwitchBinding <uvs-inspectorreference-interior--indicatorswitchbinding>`                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InputBuffer <uvs-inspectorreference-controller--inputbuffer>`                                           | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InputGate.Route <uvs-inspectorreference-controller--inputgateroute>`                                    | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InputGate <uvs-inspectorreference-controller--inputgate>`                                               | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InstrumentNeedle <uvs-inspectorreference-interior--instrumentneedle>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorCamera <uvs-inspectorreference-world--interiorcamera>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorDataSourceAttribute <uvs-inspectorreference-interior--interiordatasourceattribute>`             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorModule <uvs-inspectorreference-interior--interiormodule>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorValueSource <uvs-inspectorreference-interior--interiorvaluesource>`                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`JetBlast <uvs-inspectorreference-effects--jetblast>`                                                    | Particles, marks and other effects             |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`JetProfile <uvs-inspectorreference-drive--jetprofile>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`JoystickHandle <uvs-inspectorreference-world--joystickhandle>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardBoatInput <uvs-inspectorreference-controller--keyboardboatinput>`                               | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardDriveInput <uvs-inspectorreference-controller--keyboarddriveinput>`                             | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardFlightInput <uvs-inspectorreference-controller--keyboardflightinput>`                           | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardInput <uvs-inspectorreference-controller--keyboardinput>`                                       | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardSpaceshipInput <uvs-inspectorreference-controller--keyboardspaceshipinput>`                     | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardSubmarineInput <uvs-inspectorreference-controller--keyboardsubmarineinput>`                     | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGear <uvs-inspectorreference-exterior--landinggear>`                                             | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearPart <uvs-inspectorreference-exterior--landinggearpart>`                                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearSuspension <uvs-inspectorreference-exterior--landinggearsuspension>`                         | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearSuspensionPart <uvs-inspectorreference-exterior--landinggearsuspensionpart>`                 | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearSwitchDemo <uvs-inspectorreference-demo--landinggearswitchdemo>`                             | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LightChannel <uvs-inspectorreference-exterior--lightchannel>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Lights <uvs-inspectorreference-exterior--lights>`                                                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ManualGearbox <uvs-inspectorreference-engine--manualgearbox>`                                           | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MotorcycleBalance <uvs-inspectorreference-drive--motorcyclebalance>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MotorcycleHandle <uvs-inspectorreference-world--motorcyclehandle>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MotorcycleProfile <uvs-inspectorreference-drive--motorcycleprofile>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MovingPart <uvs-inspectorreference-exterior--movingpart>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Nitro <uvs-inspectorreference-engine--nitro>`                                                           | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ObjectDropper <uvs-inspectorreference-world--objectdropper>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`OrbitCamera <uvs-inspectorreference-world--orbitcamera>`                                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ParkingHold <uvs-inspectorreference-drive--parkinghold>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PartMotionAudio <uvs-inspectorreference-exterior--partmotionaudio>`                                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PartMotionEvents <uvs-inspectorreference-exterior--partmotionevents>`                                   | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerAccess <uvs-inspectorreference-world--passengeraccess>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerAccessDemo <uvs-inspectorreference-demo--passengeraccessdemo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerAnimatorLayers.Layer <uvs-inspectorreference-world--passengeranimatorlayerslayer>`             | World systems and passengers                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerAnimatorLayers <uvs-inspectorreference-world--passengeranimatorlayers>`                        | World systems and passengers                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerBehaviour <uvs-inspectorreference-world--passengerbehaviour>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerBody <uvs-inspectorreference-world--passengerbody>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerBodyPartConfig <uvs-inspectorreference-world--passengerbodypartconfig>`                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerFootConfig <uvs-inspectorreference-world--passengerfootconfig>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerGForceLimits <uvs-inspectorreference-world--passengergforcelimits>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerHandConfig <uvs-inspectorreference-world--passengerhandconfig>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerJointSupport <uvs-inspectorreference-world--passengerjointsupport>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerModule <uvs-inspectorreference-world--passengermodule>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerRestraints <uvs-inspectorreference-world--passengerrestraints>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Passengers <uvs-inspectorreference-world--passengers>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerSeat <uvs-inspectorreference-world--passengerseat>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerTransformSupport <uvs-inspectorreference-world--passengertransformsupport>`                    | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PedalAnimator <uvs-inspectorreference-interior--pedalanimator>`                                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PedalDrive <uvs-inspectorreference-exterior--pedaldrive>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PedalFootMode <uvs-inspectorreference-world--pedalfootmode>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PedalHandle <uvs-inspectorreference-world--pedalhandle>`                                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PhysicsModule <uvs-inspectorreference-physics--physicsmodule>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PitchSource <uvs-inspectorreference-interior--pitchsource>`                                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PowerWindowsDemo <uvs-inspectorreference-demo--powerwindowsdemo>`                                       | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ProfileSwitchBinding <uvs-inspectorreference-interior--profileswitchbinding>`                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ProfileSwitcher <uvs-inspectorreference-drive--profileswitcher>`                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ProfileTransition <uvs-inspectorreference-drive--profiletransition>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ProjectileDemo <uvs-inspectorreference-demo--projectiledemo>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Propulsion.Propeller <uvs-inspectorreference-exterior--propulsionpropeller>`                            | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Propulsion <uvs-inspectorreference-exterior--propulsion>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PropulsionJets <uvs-inspectorreference-effects--propulsionjets>`                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RagdollCollisionHelper <uvs-inspectorreference-world--ragdollcollisionhelper>`                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RagdollCollisionRelay <uvs-inspectorreference-world--ragdollcollisionrelay>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RearMirror <uvs-inspectorreference-interior--rearmirror>`                                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RearMirrors <uvs-inspectorreference-interior--rearmirrors>`                                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Rocket <uvs-inspectorreference-world--rocket>`                                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RocketLauncher <uvs-inspectorreference-world--rocketlauncher>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RollSource <uvs-inspectorreference-interior--rollsource>`                                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RotaryAnimator <uvs-inspectorreference-interior--rotaryanimator>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RotaryHandle <uvs-inspectorreference-world--rotaryhandle>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SceneGizmoOptions <uvs-inspectorreference-common--scenegizmooptions>`                                   | Common settings and base components            |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SeatAccess <uvs-inspectorreference-world--seataccess>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ServiceBrakeSource <uvs-inspectorreference-interior--servicebrakesource>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Settings <uvs-inspectorreference-common--settings>`                                                     | Common settings and base components            |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ShockAbsorber <uvs-inspectorreference-drive--shockabsorber>`                                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Skidmarks <uvs-inspectorreference-effects--skidmarks>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SpaceshipProfile <uvs-inspectorreference-drive--spaceshipprofile>`                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SpeedValueSource <uvs-inspectorreference-interior--speedvaluesource>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Stabilization <uvs-inspectorreference-physics--stabilization>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Steering <uvs-inspectorreference-drive--steering>`                                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringHandRegrip <uvs-inspectorreference-world--steeringhandregrip>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringHandRegripSettings <uvs-inspectorreference-world--steeringhandregripsettings>`                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringPart <uvs-inspectorreference-exterior--steeringpart>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringSource <uvs-inspectorreference-interior--steeringsource>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringStickAnimator <uvs-inspectorreference-interior--steeringstickanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringTieRod <uvs-inspectorreference-drive--steeringtierod>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringWheelAnimator <uvs-inspectorreference-interior--steeringwheelanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringWheelHandle.RimSample <uvs-inspectorreference-world--steeringwheelhandlerimsample>`             | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringWheelHandle <uvs-inspectorreference-world--steeringwheelhandle>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SubmarineProfile <uvs-inspectorreference-drive--submarineprofile>`                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Surface <uvs-inspectorreference-physics--surface>`                                                      | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Suspension <uvs-inspectorreference-drive--suspension>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SuspensionAxle <uvs-inspectorreference-drive--suspensionaxle>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SuspensionHub <uvs-inspectorreference-drive--suspensionhub>`                                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SuspensionRotationLimits <uvs-inspectorreference-drive--suspensionrotationlimits>`                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchAnimator <uvs-inspectorreference-interior--switchanimator>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchAudio <uvs-inspectorreference-effects--switchaudio>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchHandle <uvs-inspectorreference-world--switchhandle>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchPosition <uvs-inspectorreference-interior--switchposition>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TelemetrySettings <uvs-inspectorreference-controller--telemetrysettings>`                               | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ThrottleAnimator <uvs-inspectorreference-interior--throttleanimator>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ThrottleHandle <uvs-inspectorreference-world--throttlehandle>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireAudio <uvs-inspectorreference-effects--tireaudio>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireCollision <uvs-inspectorreference-physics--tirecollision>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireFeedback <uvs-inspectorreference-effects--tirefeedback>`                                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSmoke <uvs-inspectorreference-effects--tiresmoke>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSurface.LayerMapping <uvs-inspectorreference-effects--tiresurfacelayermapping>`                     | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSurface <uvs-inspectorreference-effects--tiresurface>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSurfaceProfile <uvs-inspectorreference-effects--tiresurfaceprofile>`                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TowingControlsDemo <uvs-inspectorreference-demo--towingcontrolsdemo>`                                   | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackedProfile <uvs-inspectorreference-drive--trackedprofile>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackPathBuilder <uvs-inspectorreference-exterior--trackpathbuilder>`                                   | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Tracks <uvs-inspectorreference-drive--tracks>`                                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackVisuals.Belt <uvs-inspectorreference-exterior--trackvisualsbelt>`                                  | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackVisuals.Roller <uvs-inspectorreference-exterior--trackvisualsroller>`                              | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackVisuals <uvs-inspectorreference-exterior--trackvisuals>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TractionControl <uvs-inspectorreference-engine--tractioncontrol>`                                       | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Trailer <uvs-inspectorreference-world--trailer>`                                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Transmission <uvs-inspectorreference-engine--transmission>`                                             | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TwistThrottleAnimator <uvs-inspectorreference-interior--twistthrottleanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`UnderwaterDemo <uvs-inspectorreference-demo--underwaterdemo>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleAudioSettings <uvs-inspectorreference-effects--vehicleaudiosettings>`                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleBodyPart <uvs-inspectorreference-exterior--vehiclebodypart>`                                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleController <uvs-inspectorreference-controller--vehiclecontroller>`                               | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleHandle <uvs-inspectorreference-world--vehiclehandle>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleHandleAnimator <uvs-inspectorreference-interior--vehiclehandleanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleMeshDeformation <uvs-inspectorreference-physics--vehiclemeshdeformation>`                        | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleModule <uvs-inspectorreference-common--vehiclemodule>`                                           | Common settings and base components            |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleSelectorDemo <uvs-inspectorreference-demo--vehicleselectordemo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleWeaponDemo <uvs-inspectorreference-demo--vehicleweapondemo>`                                     | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterEntryAudioDemo <uvs-inspectorreference-demo--waterentryaudiodemo>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterInteraction <uvs-inspectorreference-world--waterinteraction>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterProvider <uvs-inspectorreference-world--waterprovider>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterSurface <uvs-inspectorreference-world--watersurface>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterSurfaceProfile <uvs-inspectorreference-world--watersurfaceprofile>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaypointAIDemo <uvs-inspectorreference-demo--waypointaidemo>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WeaponBarrel <uvs-inspectorreference-world--weaponbarrel>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WeaponEffects <uvs-inspectorreference-effects--weaponeffects>`                                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WeaponRecoil <uvs-inspectorreference-effects--weaponrecoil>`                                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Wheel <uvs-inspectorreference-physics--wheel>`                                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelDynamics <uvs-inspectorreference-physics--wheeldynamics>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheeledProfile <uvs-inspectorreference-drive--wheeledprofile>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelLift <uvs-inspectorreference-physics--wheellift>`                                                  | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelPart <uvs-inspectorreference-exterior--wheelpart>`                                                 | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelSetup <uvs-inspectorreference-physics--wheelsetup>`                                                | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Wiper <uvs-inspectorreference-exterior--wiper>`                                                         | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WiperBlade <uvs-inspectorreference-exterior--wiperblade>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Wipers <uvs-inspectorreference-exterior--wipers>`                                                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WiperSwitchBinding <uvs-inspectorreference-exterior--wiperswitchbinding>`                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WorldModule <uvs-inspectorreference-world--worldmodule>`                                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`YokeAnimator <uvs-inspectorreference-interior--yokeanimator>`                                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`YokeHandle <uvs-inspectorreference-world--yokehandle>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+

\| :ref:`NitroAudio <uvs-inspectorreference-effects--nitroaudio>` \| Audio, particles and feedback \| \| :ref:`DamageFeedback <uvs-inspectorreference-effects--damagefeedback>` \| Audio, particles and feedback \| \| :ref:`MovingPartAudio <uvs-inspectorreference-effects--movingpartaudio>` \| Audio, particles and feedback \| \| :ref:`WipersAudio <uvs-inspectorreference-effects--wipersaudio>` \| Audio, particles and feedback \| \| :ref:`WiperAudioEntry <uvs-inspectorreference-effects--wiperaudioentry>` \| Audio, particles and feedback \| \| :ref:`ProfileTransitionAudio <uvs-inspectorreference-effects--profiletransitionaudio>` \| Audio, particles and feedback \|

\| :ref:`ProfileTransitionAudio.TransitionSound <uvs-inspectorreference-effects--profiletransitionaudiotransitionsound>` \| Audio, particles and feedback \| \| :ref:`PassengerLimbDamageFeedback <uvs-inspectorreference-world--passengerlimbdamagefeedback>` \| Cameras, passengers, water, towing and weapons \| \| :ref:`PassengerCollisionSurface <uvs-inspectorreference-world--passengercollisionsurface>` \| Cameras, passengers, water, towing and weapons \| \| :ref:`AudioClipReplacement <uvs-inspectorreference-effects--audioclipreplacement>` \| Audio, particles and feedback \| \| :ref:`AudioContextProfile <uvs-inspectorreference-effects--audiocontextprofile>` \| Audio, particles and feedback \| \| :ref:`AudioContextSettings <uvs-inspectorreference-effects--audiocontextsettings>` \| Audio, particles and feedback \| \| :ref:`DamageAudio.PartDetachmentSound <uvs-inspectorreference-effects--damageaudiopartdetachmentsound>` \| Audio, particles and feedback \| \| :ref:`TireBurnoutSmokeSettings <uvs-inspectorreference-effects--tireburnoutsmokesettings>` \| Audio, particles and feedback \| \| :ref:`RiderAnimationRule <uvs-inspectorreference-world--rideranimationrule>` \| Cameras, passengers, water, towing and weapons \| \| :ref:`RiderAnimator <uvs-inspectorreference-world--rideranimator>` \| Cameras, passengers, water, towing and weapons \| \| :ref:`RiderMotionState <uvs-inspectorreference-world--ridermotionstate>` \| Cameras, passengers, water, towing and weapons \|

Coverage: 301 component/base/data sections. Inherited settings are linked to their declaring type; preset constructors and saved prefabs can override initial values.

-  :ref:`DamageAudio <uvs-inspectorreference-effects--damageaudio>`

-  :ref:`DamageFeedback <uvs-inspectorreference-effects--damagefeedback>`

-  :ref:`DamageSoundBank <uvs-inspectorreference-effects--damagesoundbank>`

-  :ref:`DamageGroundImpactSettings <uvs-inspectorreference-effects--damagegroundimpactsettings>`

-  :ref:`DamageFeedbackProfile <uvs-inspectorreference-effects--damagefeedbackprofile>`

-  :ref:`DamageParticles <uvs-inspectorreference-effects--damageparticles>`

-  :ref:`DamageSurface <uvs-inspectorreference-effects--damagesurface>`

.. toctree::
   :maxdepth: 1
   :caption: Inspector settings by system

   InspectorReference/Common
   InspectorReference/Controller
   InspectorReference/Demo
   InspectorReference/Drive
   InspectorReference/Effects
   InspectorReference/Engine
   InspectorReference/Exterior
   InspectorReference/Interior
   InspectorReference/Physics
   InspectorReference/World
