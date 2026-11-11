# Module lifecycle and lookup

A module is a vehicle-owned component that contributes one responsibility to the simulation: steering, braking, fuel consumption or another mechanic. `VehicleController` gives registered modules a common configuration and fixed-step lifecycle. This lets a replacement participate in the same pipeline without adding another independent simulation loop.

There are three separate decisions when integrating a module: whether it belongs to the vehicle, whether it is enabled and compatible with the current movement profile, and when it executes. Registration answers the first question; `enabled` and `SupportsProfile` answer the second; `Phase` and execution order answer the third. Treating these independently makes optional and replaceable features easier to reason about.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `VehicleController` | Owns registration, discovery, configuration and the fixed-step schedule. |
| `VehicleModule` | Base component with enable, configuration, step and profile-support contracts. |
| `IVehicleModule` | Defines category interfaces and the cross-category `ExecutionPhase` sequence. |
| `CategoryCore` | Groups and orders registered modules within one category. |
| `ModuleConnections` | Resolves missing references between owned components. |
| `ModuleSetupAttribute` | Declares installation policy for full setup and module menus. |

## Registration and configuration

For an existing scene component, use `RegisterModule` to register that instance rather than creating a second copy. For a newly installed capability, `AddModule<T>()` combines creation and registration. `DiscoverModules` rebuilds membership from owned children, including inactive ones. It is useful after constructing a hierarchy, but stops at a nested controller so that vehicle keeps its own modules.

Put repeatable setup in `Configure(VehicleController vehicle)`. Cache the owner and resolve dependencies there; do not assume configuration happens only at startup. Runtime forces belong in `Step(VehicleController vehicle, Command command, float deltaTime)`, where `deltaTime` is the fixed timestep in seconds. Creating a new object or subscribing again on every configuration would accumulate resources each time the user applies settings.

`ConnectAvailableModules` fills missing owned module/controller/capability references. Existing explicit references and `[ExternalReference]` fields are preserved. It does not infer geometry, clips or materials.

Full setup uses `ModuleSetup` policy: `IncludeInFull = false` excludes a type; `EnabledByDefault = false` disables a newly installed optional type. A hidden `AddComponentMenu` can participate when `ModuleOnly = true` is set.

## Lookup and ordering

Use a concrete class lookup when you need that implementation's controls, and an interface lookup when several interchangeable modules expose the same capability. An explicit reference is preferable when several instances intentionally coexist, because the first registered match does not express which instance the application means.

Execution phases preserve dependencies across categories. For example, power is resolved before differential allocation, and presentation targets advance before passenger feedback. Changing a local order only changes priority inside the appropriate phase/category; it cannot move an assistance module ahead of contact sampling. Choose `Phase` for the dependency and `ExecutionOrder` for ordering among peers.

`TryGetModule<T>` returns the first registered class/interface match. Default lookup includes disabled components; `activeOnly: true` requires Unity active/enabled state. This filter does not check `SupportsProfile`. `GetModules<T>` clears and fills a caller-owned list in registration order.

Execution uses `Phase`, category priority and effective local order. Lookup order is independent of execution priority. Changes during `Step` use the tick's captured membership/order and affect the next tick. A disabled/destroyed component is skipped when reached.

After changing category/local ordering, call `RefreshModuleOrder()`. It does not configure wheels or reset simulation. `TryApplyConfiguration(out error)` validates wheel definitions, builds adapters, applies mass/center of mass and configures registered modules.

## Enable a discovered capability

Add the following adapter to an application object, assign its vehicle and call `SetTraction` from UI or gameplay. A UI toggle needs to find an installed capability even while it is disabled. Filtering the lookup to active modules would make the “on” action unable to find the very component it must enable. The following adapter therefore uses the default lookup and sends the change through the traction-control action rather than keeping a second local enabled state.

**Example: `TractionToggle.cs`**

<!-- example: TractionToggle.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class TractionToggle : MonoBehaviour
    {
        public VehicleController vehicle;

        public void SetTraction(bool enabled)
        {
            if (vehicle && vehicle.TryGetModule<TractionControl>(out var traction))
                traction.SetTractionControlEnabled(enabled);
        }
    }
}
```

If `DrivingAssists` owns the settings, use its public switch instead. For a new capability shared by several implementations, define your own interface and use `GetModules` with a reused list.

## Query several capability implementations

When several modules intentionally implement one capability, query an interface into a reused list. This example defines an application-owned inspection contract and a module implementing it. A reader does not need to know the concrete module type. The interface describes observation only; it does not expose the module's internal force calculation.

Save the two components in the marked files. Install `VehicleSpeedCapability` through module registration, assign the vehicle to `CapabilityReadout`, then call `Refresh` when your application needs the readings. `GetModules` clears the list before filling it, so repeated refreshes do not accumulate previous results.

**Example: `VehicleSpeedCapability.cs`**

<!-- example: VehicleSpeedCapability.cs -->
```csharp
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public interface IApplicationVehicleReading
    {
        string Label { get; }
        float Read();
    }

    public class VehicleSpeedCapability : PhysicsModule, IApplicationVehicleReading
    {
        private VehicleController owner;
        public string Label => "Speed (km/h)";
        public override void Configure(VehicleController vehicle) => owner = vehicle;
        public float Read() => owner ? owner.SpeedKph : 0;
    }
}
```

**Example: `CapabilityReadout.cs`**

<!-- example: CapabilityReadout.cs -->
```csharp
using System.Collections.Generic;
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class CapabilityReadout : MonoBehaviour
    {
        public VehicleController vehicle;
        private readonly List<IApplicationVehicleReading> readings = new();

        public void Refresh()
        {
            if (!vehicle) return;
            vehicle.GetModules(readings, activeOnly: true);
            foreach (var reading in readings)
                Debug.Log($"{reading.Label}: {reading.Read():0.0}", vehicle);
        }
    }
}
```

`activeOnly: true` is useful here because the reader wants currently enabled providers. It still does not mean a provider supports the active profile. Add that condition to the capability contract if an application needs it. For a high-frequency UI, publish the readings to UI properties instead of logging each refresh.

## Replace a component safely

Plan replacement as an ownership handover. First identify which object owns scheduled work, event subscriptions and generated resources. Then move consumers to the replacement before allowing both implementations to write the same actuator. Replacing steering, for example, requires considering the engine-facing steering demand and any interior presentation bindings that explicitly reference the old component.

Inheritance is suitable when the base algorithm remains useful: override the narrow operation and call `base` when its work should remain. A sibling implementation is suitable when the algorithm itself changes. In either case, preserve the public behavior consumers rely on, including admission checks, cleanup and notifications. Raising an event alone does not carry out the underlying operation.

Unregister the old module, disable it if it owns frame callbacks/subscriptions, update explicit references, then register the replacement. Remove the retired component if later discovery must not find it. Registration does not silently redirect fields pointing at the old component.

Unregistration only removes pipeline membership. `Audio` channels, handles and other nested owners have their own lifecycle; see [Architecture](../Architecture.md).

Vehicle configuration clamps root `Rigidbody` mass to at least 1 kg and applies interpolation/collision-detection settings. A custom integration requiring a different mass/physics policy must account for those configuration writes.

Registered modules are configured even when disabled. A `Configure` method can write persistent native settings; disabling its scheduled `Step` does not necessarily undo those writes. For example, native suspension continues using its configured spring settings.

## Temporarily disable a module

Use `module.SetEnabled(false)` or `vehicle.SetModuleEnabled<T>(false)` and pass `true` to resume. This changes Unity's `enabled` checkbox without removing the component or its Inspector configuration. The vehicle skips modules whose `isActiveAndEnabled` is false; that Unity property is read-only. `SetModuleEnabled<T>` also finds disabled modules, so the same call can enable them again.

Disabling invokes the module's normal `OnDisable` cleanup. For example, audio stops, engine output is cleared, and disabling `Passengers` makes seated passengers exit. This is a temporary disable with module-specific cleanup, rather than a frozen simulation state.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed module lifecycle and scheduling API](../API/Modules.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### IVehicleResetHandler

[IVehicleResetHandler](../API/Modules.md#ivehicleresethandler) gives the full declared contract.

- `void ResetVehicleState(VehicleResetReason reason)` — Clears transient state for the supplied reset reason without changing persistent configuration.

### ModuleCatalog

[ModuleCatalog](../API/Modules.md#modulecatalog) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public static Type[] GetAvailableTypes()` | Returns the catalog of eligible module implementation types. |

### VehicleModule

[VehicleModule](../API/Modules.md#vehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void Configure(VehicleController vehicle)` | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
| `public virtual void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it. |
| `public virtual void SetEnabled(bool value)` | Changes module enabled state and publishes an actual requested-flag change. |
| `public virtual bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> EnabledChanged` | After `SetEnabled` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
| `public event System.Action<VehicleController> Configured` | After controller-driven module configuration. Payload: the owning `VehicleController`. |
| `public event System.Action<VehicleController, Command, float> Stepped` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds. |
