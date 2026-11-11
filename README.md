# Ultra Vehicle System

Ultra Vehicle System is a modular vehicle package for Unity. It provides ready-to-use movement, physics and control systems for ground, air and water vehicles, with configurable passengers, interactive controls, damage and effects. Use it to build vehicles for your game with your own models, input and gameplay rules, or start from the supplied examples.

**Full documentation:** https://uvs.readthedocs.io/

**YouTube:** [Tutorials and videos](https://www.youtube.com/watch?v=vm_SU-W8ODY&list=PLVuGjQDh104Q&index=1)

<img width="1672" height="941" alt="cover" src="https://github.com/user-attachments/assets/414f828b-1caf-4d24-bf4a-8db6a525833b" />

## Version and compatibility

| Item | Support |
| --- | --- |
| Version | **1.0.2** |
| Unity | **Unity 6.0 LTS — 6000.0.84f1 or newer** |
| Render pipelines | **Built-in Render Pipeline, Universal Render Pipeline (URP) and High Definition Render Pipeline (HDRP)** |
| Input | Unity Input System **1.19.0** |

Vehicle mechanics are independent of the render pipeline. The supplied demo uses URP materials; for Built-in or HDRP, assign materials and shaders suitable for that pipeline to vehicles, water and effects. Installation keeps your project's render pipeline settings.

## Key features

- **Ready-to-use vehicle physics and controllers.** Configure cars, buses, trucks, motorcycles, tracked vehicles and tanks, airplanes, aerobatic aircraft, jets, helicopters, drones, hover vehicles, boats and submarines. Built-in drive profiles provide movement and handling for each family, while your models define the vehicle's appearance.
- **Modular design with custom extension points.** Combine only the mechanics and presentation systems your vehicle needs. Extend or replace built-in components, add your own modules, and create independent drive profiles that appear in the Inspector without modifying package code.
- **A dedicated vehicle Inspector.** Configure the vehicle through grouped Setup, Wheels, Seats, Modules, Effects and Live views. Discover wheel colliders, assign wheel roles, inspect live state, preview supported poses, and copy or paste module configurations; custom subclasses retain their additional Inspector fields.
- **Engine, transmission and driving assists.** Build a drivetrain with engine torque/RPM configuration, ignition and fuel, manual or automatic gearboxes, clutch, differential, traction control and stability assistance. Tune gearing, shift behavior and speed limits to suit the vehicle.
- **Suspension, brakes and ground contact.** Configure spring and damper response, suspension travel, anti-roll support, steering geometry, service brakes and handbrakes. Add motorcycle balance, tracked steering, configurable surface grip, contact-envelope support and solid-tire helpers for the terrain your game uses.
- **Flexible input and multiple movement modes.** Use keyboard controls, Input Actions, gamepads or external commands from AI, replay and application code. Register any number of drive profiles and cycle through them, select by ID, route input per mode and assign animated transitions to specific profile pairs. Configure and display speeds in km/h, mph or m/s.
- **Drivers, passengers and interactive character controls.** Configure seats, boarding and exit points, animated or physical occupants, humanoid IK, hand grips and foot contacts. Add steering wheels, yokes, sticks and other handles, with configurable restraints, limb release and passenger ejection.
- **Interactive interiors, body systems and aircraft equipment.** Add instrument readouts, HUDs, mirrors, lights, doors, moving body parts, windows, wipers, levers and pedals. Configure aircraft control surfaces, visible propellers/rotors, retractable landing gear and hinged gear suspension; connect trailers with towing and brake support.
- **Damage, weapons and audiovisual effects.** Configure impacts, deformation of supported readable meshes, detachable parts and repair actions. Add aiming, projectiles, recoil, rockets and payload release, then combine engine and mechanical audio, tire smoke, skid marks, water effects and propulsion particles.
- **Public APIs, events and ready-made examples.** Drive systems from your own scripts, read telemetry and react to typed events. Integrate custom input, components, characters and water providers using the API reference and complete C# examples. The Demo sample includes a selectable vehicle fleet and examples of the package's main systems.

## Start building

Read [Introduction and quick start](manual/Introduction.md) for the setup sequence and full guide index, or go directly to [Getting started](manual/GettingStarted.md).

Explore the [demo vehicles](manual/Demo.md), browse the [scripting reference](manual/Scripting/README.md) and [public API](manual/API.md), or consult [Troubleshooting](manual/Troubleshooting.md). See [Installation and included content](manual/Distribution.md) for import instructions and included folders.

## Links

- GitHub, docs, issues, changelog: [Ultra Vehicle System on GitHub](https://github.com/szczyglis-dev/ultra-vehicle-system)
- Documentation: [Online manual](https://uvs.readthedocs.io/)
- License: [LICENSE.md](LICENSE.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Author

Marcin Szczygliński (szczyglis83@gmail.com)

## Complete Inspector reference

[All component settings](manual/InspectorReference.md) — descriptions, declared defaults, Inspector limits, inherited settings and nested configuration for every package system and the demo components.

## Demo credits

Authors, licenses and available source URLs for the models and audio used in the demo are listed in [Credits](manual/Credits.md) and the documentation’s [Third-party credits](manual/ThirdParty.md).
