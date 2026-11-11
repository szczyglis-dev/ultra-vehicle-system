# Scripting reference

[Modules list](../ModulesAndArchitecture.md#modules-list) — browse components by category, with purposes and requirements.

[Events reference](EventsReference.md) — event and Inspector-callback tables grouped by class, with arguments and firing conditions.

[Custom modules](CustomModules.md) — create, install and schedule your own component, including Add Component and Tools menus.

[Profiling and debugging](ProfilingAndDebugging.md) — capture vehicle work and add custom markers.

Use the setup guide to build and check a system first. These chapters explain implementation contracts and provide complete C# components. Examples use the `VehicleDocumentationExamples` namespace; save a component in the named file, reference the runtime assembly and assign the listed scene references before use.

## Start with Inspector setup

Configuring the built-in components does not require writing the implementations described in this reference. Use [Basic Inspector workflow](../InspectorConfiguration.md#basic-inspector-workflow) for adding modules, assigning references, applying configuration and saving. Start with the relevant practical guide below; return to these technical chapters for custom behavior and application integration.

| System | Inspector-first guides |
| --- | --- |
| Chassis, wheels, brakes and steering | [Physics](../Physics.md), [Suspension](../Suspension.md), [Tire collision](../TireCollision.md), [Contact envelope](../ContactEnvelope.md) |
| Power and transmission | [Gearbox](../Gearbox.md), [Clutch](../Clutch.md), [Differential](../Differential.md), [TCS](../TractionControl.md), [Boost actions](../DrivingActions.md) |
| Movement families and switching | [Drive profiles](../DriveProfiles.md), [Aircraft](../Aircraft.md), [Boat](../Boat.md), [Submarine](../Submarine.md), [Tracks](../Tracked.md), [Combined vehicles](../CombinedVehicles.md) |
| Environment and physical responses | [Water](../Water.md), [Ground surfaces](../Surfaces.md), [Crash/landing response](../CollisionsAndStabilization.md), [Towing](../Towing.md) |
| Panels, wheels and damage | [Moving parts](../MovingParts.md), [Damage registries and setup](../Damage.md#inspector-workflow-and-part-registries), [Wipers](../Wipers.md) |
| Lighting, sound and particles | [Lights](../Lights.md), [Audio](../Audio.md), [Particles](../Particles.md), [Tire marks](../Decals.md) |
| Cockpit and views | [Controls/instruments](../InteriorControls.md), [Screens/mirrors/fuel](../InteriorSystems.md), [Cameras](../Cameras.md), [Input](../Input.md) |
| Occupants and boarding | [Passengers](../Passengers.md), [Seats](../Seats.md), [Passenger access](../PassengerAccess.md), [Humanoid preparation](../HumanAnatomy.md) |
| Hands, feet and authored animation | [Handles](../Handles.md), [Saved hand positions](../HandPositions.md), [Grip fitting](../SteeringHandGrip.md), [Animation/IK](../HandleAnimation.md), [Timed interactions](../ControlInteractions.md) |
| Mounted weapons and payloads | [Weapons](../Weapons.md) |

Use the [Inspector field reference](../InspectorReference.md) for exact fields/defaults after completing a setup. Keep the API contracts and examples below for cases that need code; they are not additional components to install for every vehicle.

## Code examples

[Scripting examples](Examples/README.md) contains 100 standalone components in 10 categories, with setup instructions, comments and expected behavior.

## Reading a technical chapter

Each topic starts with the system's purpose and the relationship between its parts. **Implementation map** names the classes responsible for each role. Individual component sections explain purpose and cooperation first, then configuration, technical behavior and integration points. They cover data flow, configuration authority and public operations together. Examples appear beside the behavior they illustrate, with setup, expected results and lifetime considerations. API identifiers use `code formatting`; values include units or normalized conventions where those affect integration.

For a new extension, read [Architecture](../Architecture.md), then [Scripting](../Scripting.md) and the relevant topic. For an existing integration, use the [API map](../API.md) to reach the owner of the operation. Each topic ends with a complete public method/event index, including package base contracts. The [API reference](../API.md) adds exact arguments, results, event payloads and declared state/configuration.

## Integrate with the vehicle

[What is available directly on vehicle](../Scripting.md#what-is-available-directly-on-vehicle) — shortcuts, seats, body parts, handles, telemetry data/settings, chassis state, module queries and events.

| Task | Read |
| --- | --- |
| Understand category/phase ownership | [Architecture](../Architecture.md) |
| Choose an extension point | [Scripting](../Scripting.md) |
| Install a custom module on the root or a child | [Step-by-step installation](../Scripting.md#install-your-component-on-a-vehicle-step-by-step) |
| Find public operations | [API map](../API.md) |
| Open/close a body part and read requested versus actual state | [Body-part scripting](Damage.md#open-a-named-part) |
| Operate a generic moving part and observe arrival | [Moving-part operations](MovingParts.md#operate-a-movingpart-and-read-its-state) |
| Read collision impacts, accepted damage or supply a custom response | [Impact notification guide](Damage.md#choose-the-impact-notification) |
| Register, find or replace modules | [Module lifecycle](Modules.md) |
| Supply commands and switch providers | [Input](Input.md) |
| Find events by name and owner | [Events reference](EventsReference.md) |
| Observe without polling physics | [Events and telemetry](Events.md) |
| Add or switch movement modes | [Drive profiles](DriveProfiles.md) |
| Write an independent movement profile and select it in the Inspector | [Profile from scratch](DriveProfiles.md#create-an-independent-profile-from-scratch) |

## Events and subscriptions

Use events to connect UI, audio and application rules to accepted vehicle state changes. Subscribe to the owning component with `+=`, remove the same handler with `-=`, and read current state once when binding. For continuous readings, use telemetry snapshots.

[Events and telemetry](Events.md#subscribe-to-a-components-events) explains handler arguments, initial state, safe source changes and cleanup with a complete engine/seat example. It also covers [Inspector callbacks](Events.md#inspector-callbacks-and-c-events), which use `UnityEvent.AddListener` / `RemoveListener` instead of C# event syntax. Exact payloads and firing conditions are listed in the corresponding [API topic](../API.md).

## Mechanics and environment

| Topic | Reference |
| --- | --- |
| Wheel authoring, native/envelope/solid contact | [Wheel contact](WheelContact.md) |
| Springs, shock overrides and linkage | [Suspension](Suspension.md) |
| Engine, gears, clutch, differential and TCS | [Drivetrain](DriveDynamics.md) |
| Boat resistance and rocking | [Boat](Boat.md) |
| Track sides and belt paths | [Tracks](Tracks.md) |
| Flight, gear and instruments | [Aircraft](Aircraft.md) |
| Providers, depth hold and propeller presentation | [Water](Water.md) |
| Physical grip versus effect surfaces | [Surface feedback](SurfaceFeedback.md) |
| Physical hitch lifecycle | [Towing](Towing.md) |
| Hits, detachment and restoration | [Damage](Damage.md) |
| Aiming, projectiles, rockets and payloads | [Weapons](Weapons.md) |

## Characters and presentation

| Topic | Reference |
| --- | --- |
| Occupancy, custom characters and controller factory | [Passenger controllers](PassengerControllers.md) |
| Dynamic supports, release and collision policy | [Passenger physics](PassengerPhysics.md) |
| Skeletal frames | [Anatomy](Anatomy.md) |
| Contact targets and transfer actions | [Handles](Handles.md) |
| Finger fit, steering mapping and reservations | [Grip solving](GripSolving.md) |
| Animated boarding and reservations | [Passenger access](PassengerAccess.md) |
| Committed IK/Animator/custom gestures | [Interactions](Interactions.md) |
| Instruments, mirrors and fuel | [Interior](Interior.md) |
| Exterior part motion, blade timing, parking and cockpit binding | [Exterior motion and moving parts](MovingParts.md) |
| Channel output and indicator timing | [Lights](Lights.md) |
| Audio sources and custom channels | [Audio](Audio.md) |
| Particle/mark resource ownership | [Presentation](Presentation.md) |

## Profiling and debugging

[Profiling and debugging](ProfilingAndDebugging.md) covers repeatable captures, built-in UVS samples, custom ProfilerMarker scopes and integration diagnostics.

## Crash presentation

[Crash Feedback](../DamageFeedback.md#shared-events-and-api) provides copied contact events, configurable audio and particles, and custom contact submission. Use damage events for authoritative damage logic.
