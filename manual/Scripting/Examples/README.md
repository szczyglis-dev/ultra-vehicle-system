# Scripting examples

One hundred standalone examples in ten categories. Each example solves a small application task and includes setup, behavior, comments and a complete C# component. They complement the implementation chapters with UI adapters, policies, measurements and gameplay exercises.

## Before using an example

- Save each component in the named `.cs` file under your own `Assets` scripts folder, outside the package. All examples use the `VehicleDocumentationExamples.Cookbook` namespace. If you use an assembly definition, reference `UltraVehicleSystem.Runtime` and the Unity modules your component needs.
- Assign scene references before enabling a component. Event examples assume their source reference remains fixed while enabled: disable the component before replacing a source, then enable it again.
- UI examples expose public methods for buttons, sliders or your own action system. They do not require a particular keyboard binding. Invoke Unity APIs on Unity's main thread.
- Each script owns only the request or presentation property described in its setup. Combine scripts deliberately: two input writers, beam policies or FOV writers can overwrite each other. Ordinary MonoBehaviours are not vehicle modules; the custom-module category explains installation and physics timing.
- Interior animators here are vehicle-system control components, distinct from Unity's skeletal Animator. Sources supply values; control animators move equipment; handles coordinate limbs.

## Categories

| Category | Examples | Focus |
| --- | --- | --- |
| [Commands and input](Input.md) | 10 | Adapters for UI, remote control and repeatable driving tests. |
| [Configuration and recovery](Lifecycle.md) | 10 | Runtime configuration, checkpoints and module availability. |
| [Custom vehicle modules](Modules.md) | 10 | Install these components through Add Module or your normal module registration flow. |
| [Driving challenges and gameplay](Gameplay.md) | 10 | Small challenge rules driven by authoritative telemetry. |
| [Engine, fuel and boost](Powertrain.md) | 10 | Gameplay policies around the existing engine and boost modules. |
| [Exterior equipment](Exterior.md) | 10 | Small policies for lights, wipers and moving model parts. |
| [Interior data sources](Interior.md) | 10 | Custom scalar sources plug into an interior animator’s data source field. |
| [Passengers and handle interactions](Handles.md) | 10 | Application-level gestures share HandleController ownership with normal controls. |
| [Presentation and diagnostics](Presentation.md) | 10 | Observers for camera effects, trails and development tools. |
| [Telemetry and measurements](Telemetry.md) | 10 | Read completed physics snapshots for game rules and presentation. |
