# Module lifecycle and scheduling API

Read [the system explanation](../Scripting/Modules.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [CategoryCore](Modules.md#categorycore)
- [ExecutionPhase](Modules.md#executionphase)
- [ExteriorCore](Modules.md#exteriorcore)
- [ExteriorModule](Modules.md#exteriormodule)
- [ExternalReferenceAttribute](Modules.md#externalreferenceattribute)
- [IControllerModule](Modules.md#icontrollermodule)
- [IDriveModule](Modules.md#idrivemodule)
- [IEffectsModule](Modules.md#ieffectsmodule)
- [IEngineModule](Modules.md#ienginemodule)
- [IExteriorModule](Modules.md#iexteriormodule)
- [IInteriorModule](Modules.md#iinteriormodule)
- [IPhysicsModule](Modules.md#iphysicsmodule)
- [IVehicleModule](Modules.md#ivehiclemodule)
- [IVehicleResetHandler](Modules.md#ivehicleresethandler)
- [IWorldModule](Modules.md#iworldmodule)
- [ModuleCatalog](Modules.md#modulecatalog)
- [ModuleCategory](Modules.md#modulecategory)
- [ModuleSetupAttribute](Modules.md#modulesetupattribute)
- [PhysicsCore](Modules.md#physicscore)
- [PhysicsModule](Modules.md#physicsmodule)
- [VehicleModule](Modules.md#vehiclemodule)
- [VehicleResetReason](Modules.md#vehicleresetreason)
- [WorldCore](Modules.md#worldcore)
- [WorldModule](Modules.md#worldmodule)

## CategoryCore

**Runtime/Core/CategoryCore.cs**

Groups and orders registered modules within one category.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public abstract ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |
| `public int ExecutionOrder { get; internal set; }` | Default local priority within phase/category. |
| `public IReadOnlyList<VehicleModule> Modules { get; }` | Read-only/resolved modules for `CategoryCore`. |

## ExecutionPhase

**Runtime/Core/IVehicleModule.cs**

Defines the allowed execution phase choices used by this topic.

### Values

- `Contact`
- `Transmission`
- `Braking`
- `TrailerBraking`
- `Clutch`
- `Power`
- `Differential`
- `Steering`
- `Drive`
- `Friction`
- `Assistance`
- `Suspension`
- `Balance`
- `Presentation`
- `Coasting`
- `Parking`
- `WheelDynamics`
- `Feedback`
- `Collision`

## ExteriorCore

**Runtime/Exterior/Core/ExteriorCore.cs**

Configuration/implementation type for exterior core within module lifecycle and scheduling.

**Inherits / implements:** [CategoryCore](Modules.md#categorycore).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public ExteriorCore()` | Constructs `ExteriorCore` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## ExteriorModule

**Runtime/Exterior/Core/ExteriorModule.cs**

Base integration with the vehicle module lifecycle.

**Inherits / implements:** [VehicleModule](Modules.md#vehiclemodule), [IExteriorModule](Modules.md#iexteriormodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |

## ExternalReferenceAttribute

**Runtime/Core/ModuleSetupAttribute.cs**

Configuration/implementation type for external reference attribute within module lifecycle and scheduling.

**Inherits / implements:** `Attribute`.

## IControllerModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for icontroller module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## IDriveModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for idrive module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## IEffectsModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for ieffects module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## IEngineModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iengine module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## IExteriorModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iexterior module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## IInteriorModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iinterior module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## IPhysicsModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iphysics module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## IVehicleModule

**Runtime/Core/IVehicleModule.cs**

Defines category interfaces and the cross-category `ExecutionPhase` sequence.

### State and configuration

| Member | Meaning |
| --- | --- |
| `ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |
| `int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. | `vehicle` — Vehicle context/owner receiving the operation. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## IVehicleResetHandler

**Runtime/Core/IVehicleResetHandler.cs**

Presentation or lifecycle contract for independent vehicle components.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void ResetVehicleState(VehicleResetReason reason)` | Clears transient state for the supplied reset reason without changing persistent configuration. | — |

## IWorldModule

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iworld module within module lifecycle and scheduling.

**Inherits / implements:** [IVehicleModule](Modules.md#ivehiclemodule).

## ModuleCatalog

**Runtime/Core/ModuleCatalog.cs**

Configuration/implementation type for module catalog within module lifecycle and scheduling.

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public static Type[] GetAvailableTypes()` | Returns the catalog of eligible module implementation types. | **Returns:** Returned Type[]; ownership remains as specified by the creating/lookup operation. |

## ModuleCategory

**Runtime/Core/IVehicleModule.cs**

Defines the allowed module category choices used by this topic.

### Values

- `Controller`
- `Physics`
- `Drive`
- `Engine`
- `Interior`
- `Exterior`
- `World`
- `Effects`

## ModuleSetupAttribute

**Runtime/Core/ModuleSetupAttribute.cs**

Declares installation policy for full setup and module menus.

**Inherits / implements:** `Attribute`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool EnabledByDefault { get; set; }` | Configurable enabled by default for `ModuleSetupAttribute`. |
| `public bool IncludeInFull { get; set; }` | Configurable include in full for `ModuleSetupAttribute`. |
| `public bool ModuleOnly { get; set; }` | Configurable module only for `ModuleSetupAttribute`. |

## PhysicsCore

**Runtime/Physics/Core/PhysicsCore.cs**

Configuration/implementation type for physics core within module lifecycle and scheduling.

**Inherits / implements:** [CategoryCore](Modules.md#categorycore).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public PhysicsCore()` | Constructs `PhysicsCore` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## PhysicsModule

**Runtime/Physics/Core/PhysicsModule.cs**

Configuration/implementation type for physics module within module lifecycle and scheduling.

**Inherits / implements:** [VehicleModule](Modules.md#vehiclemodule), [IPhysicsModule](Modules.md#iphysicsmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |

## VehicleModule

**Runtime/Core/VehicleModule.cs**

Exposes lifecycle notifications around registered module work.

**Inherits / implements:** `MonoBehaviour`, [IVehicleModule](Modules.md#ivehiclemodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<VehicleController> Configured` | After controller-driven module configuration. Payload: the owning `VehicleController`. |
| `public event System.Action<bool> EnabledChanged` | After `SetEnabled` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
| `public event System.Action<VehicleController, Command, float> Stepped` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |
| `public virtual int EffectiveExecutionOrder { get; }` | Local priority after optional Inspector override. |
| `public virtual int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public int localExecutionOrder` | Order within the module category and dependency phase when Override Execution Order is enabled. Smaller values run earlier. |
| `public bool overrideExecutionOrder` | Override the default order inside this category and dependency phase. |
| `public virtual ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public virtual bool SupportsDirectControl { get; }` | Allows this module to step while the selected source owns the chassis pose. Base default: interior/exterior/effects categories; force modules require explicit opt-in. |
| `public virtual bool SupportsReleasedForces { get; }` | Opt-in for work that may continue during force release. Defaults to Interior/Exterior/Effects presentation; force-producing custom modules should keep false. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Configure(VehicleController vehicle)` | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual void SetEnabled(bool value)` | Changes module enabled state and publishes an actual requested-flag change. | `value` — Requested bool state for this operation. |
| `public virtual void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. | `profile` — Movement/surface configuration, according to its declared type. **Returns:** `true` when the described condition holds; `false` otherwise. |

## VehicleResetReason

**Runtime/Core/IVehicleResetHandler.cs**

Reason for clearing transient vehicle state.

### Values

- `Respawn`
- `ForceStateChanged`

## WorldCore

**Runtime/World/Core/WorldCore.cs**

Configuration/implementation type for world core within module lifecycle and scheduling.

**Inherits / implements:** [CategoryCore](Modules.md#categorycore).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public WorldCore()` | Constructs `WorldCore` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |

## WorldModule

**Runtime/World/Core/WorldModule.cs**

Configuration/implementation type for world module within module lifecycle and scheduling.

**Inherits / implements:** [VehicleModule](Modules.md#vehiclemodule), [IWorldModule](Modules.md#iworldmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public sealed override ModuleCategory Category { get; }` | Module responsibility category; it does not independently determine execution phase. |
