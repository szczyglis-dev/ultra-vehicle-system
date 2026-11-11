# Introduction and quick start

Build a vehicle from reusable mechanics, model controls and presentation components. Start with a drive mode, configure the model and wheels, then add the systems your game needs.

## First vehicle

1. [Install and create a working car](GettingStarted.md).
2. [Check the model hierarchy and pivots](VehicleModelConvention.md).
3. [Connect your controls](Input.md).
4. [Tune mass, suspension and handling](VehicleTuning.md).
5. [Choose optional systems](ChoosingSystems.md).

For a working example, open the supplied [Demo scene](Demo.md). If something does not work, use [Troubleshooting](Troubleshooting.md).

## Setup guides

| Task | Guides |
| --- | --- |
| Configure the Inspector and prefab | [Vehicle configuration](Configuration.md), [Inspector options](InspectorConfiguration.md) |
| Understand the controller and module categories | [Modules and architecture](ModulesAndArchitecture.md) |
| Choose speed authoring and display units | [Speed units](SpeedUnits.md) |
| Choose movement and change modes | [Drive profiles](DriveProfiles.md), [Combined vehicles](CombinedVehicles.md) |
| Configure a drivetrain | [Gearbox](Gearbox.md), [Clutch](Clutch.md), [Differential](Differential.md), [Traction control](TractionControl.md) |
| Configure wheels and ground contact | [Suspension](Suspension.md), [Contact envelope](ContactEnvelope.md), [Solid tire contacts](TireCollision.md), [Ground surfaces](Surfaces.md), [Tracked vehicles](Tracked.md) |
| Build aircraft or water vehicles | [Aircraft](Aircraft.md), [Boat](Boat.md), [Submarine](Submarine.md), [Water](Water.md) |
| Add orbit and cabin views | [Cameras and anchors](Cameras.md) |
| Add characters | [Passengers](Passengers.md), [Seats](Seats.md), [Handles](Handles.md), [Hand grips](SteeringHandGrip.md), [Reusable hand positions](HandPositions.md), [Anatomical setup](HumanAnatomy.md), [Entry and exit](PassengerAccess.md) |
| Add controls and displays | [Interior overview](Interior.md), [Control animators and instruments](InteriorControls.md), [Interaction gestures](ControlInteractions.md), [Custom animation and IK](HandleAnimation.md), [Mirrors, fuel and assists](InteriorSystems.md), [Exterior wipers](Wipers.md) |
| Collisions and stabilization | [Collisions and stabilization](CollisionsAndStabilization.md) |
| Add body systems | [Moving parts](MovingParts.md), [Lights](Lights.md), [Damage](Damage.md), [Towing](Towing.md) |
| Add effects and weapons | [Audio](Audio.md), [Particles](Particles.md), [Tire marks](Decals.md), [Weapons](Weapons.md) |
| Plan deployment and performance | [Installation layouts](Distribution.md), [Performance](Performance.md), [Physics scope](Physics.md) |

## Programming

Use the [Scripting Reference](Scripting/README.md) for implementation contracts and complete C# examples. [Architecture](Architecture.md) explains ownership and the execution pipeline; [Scripting](Scripting.md) explains extension choices; [API](API.md) is the public API map.

## Supplied content

Vehicle names such as Car, Boat and Jet refer to example configurations in **Demo**. See [Demo resources](DemoResources.md) for asset references and [Third-party credits](ThirdParty.md) for attribution.

## Reference and support

[Modules list](ModulesAndArchitecture.md#modules-list) groups all runtime components by responsibility, with brief purposes and collaborators. Continue with [Performance](Performance.md), [Troubleshooting](Troubleshooting.md) and the [Inspector reference](InspectorReference.md) for tuning and individual settings.
