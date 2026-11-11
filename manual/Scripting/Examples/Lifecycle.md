# Configuration and recovery

Runtime configuration, checkpoints and module availability. Apply configuration only when settings change; these examples do not rebuild the vehicle every frame.

See [Modules implementation](../Modules.md) for the underlying contracts.

## Recover to a recorded checkpoint

**Setup:** Assign vehicle and a safe checkpoint Transform outside obstacles. Call Save, then Recover when needed.

**Behavior:** Uses ResetVehicle for repair and occupant reset; it does not restore a dynamic in-air physics snapshot.

Save as `CheckpointRecovery.cs`.

<!-- example: CheckpointRecovery.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class CheckpointRecovery : MonoBehaviour
    {
        // Read or request state through its owning component; do not bypass the vehicle pipeline.
        public VehicleController vehicle;
        public Transform checkpoint;
        Pose saved;
        bool ready;
        public void Save()
        {
            if (!checkpoint) return;
            saved = new Pose(checkpoint.position, checkpoint.rotation); ready = true;
        }
        public void Recover()
        {
            if (ready && vehicle) vehicle.ResetVehicle(saved.position, saved.rotation);
        }
    }
}
```

## Apply a workshop top-speed setting

**Setup:** Assign vehicle and call ApplyMph from a confirmed menu action.

**Behavior:** Changes the shared top-speed setting using its mph convenience property, validates configuration, and rolls back a failed request. Gear speed ranges remain separately authored.

Save as `TopSpeedWorkshop.cs`.

<!-- example: TopSpeedWorkshop.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class TopSpeedWorkshop : MonoBehaviour
    {
        public VehicleController vehicle;
        public void ApplyMph(float mph)
        {
            if (!vehicle || !float.IsFinite(mph) || mph <= 0) return;
            float previous = vehicle.settings.TopSpeedMph;
            vehicle.settings.TopSpeedMph = mph;
            if (vehicle.TryApplyConfiguration(out var error)) return;
            vehicle.settings.TopSpeedMph = previous;
            vehicle.ApplyConfiguration(); // Restore the previously valid setting.
            Debug.LogWarning(error, vehicle);
        }
    }
}
```

## React to dynamically registered Nitro

**Setup:** Assign vehicle and a separate badge object.

**Behavior:** Refreshes on module registration/removal and on enable. It indicates registered availability, not whether boost is currently active or enabled.

Save as `OptionalModuleBadge.cs`.

<!-- example: OptionalModuleBadge.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class OptionalModuleBadge : MonoBehaviour
    {
        // Read or request state through its owning component; do not bypass the vehicle pipeline.
        public VehicleController vehicle;
        public GameObject badge;
        void OnEnable()
        {
            if (!vehicle) return;
            vehicle.ModuleRegistered += Changed; vehicle.ModuleUnregistered += Changed;
            Refresh();
        }
        void OnDisable()
        {
            if (!vehicle) return;
            vehicle.ModuleRegistered -= Changed; vehicle.ModuleUnregistered -= Changed;
        }
        void Changed(UltraVehicleSystem.VehicleModule module) { Refresh(); }
        void Refresh() { if (badge) badge.SetActive(vehicle && vehicle.TryGetModule<Nitro>(out _)); }
    }
}
```

## Display wheel availability changes

**Setup:** Assign vehicle. Connect refreshRequested to a UI rebuild action.

**Behavior:** Notifies UI after wheel availability changes; it avoids assuming that wheel index means left/right across every model.

Save as `WheelAvailabilityPanel.cs`.

<!-- example: WheelAvailabilityPanel.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class WheelAvailabilityPanel : MonoBehaviour
    {
        public VehicleController vehicle;
        public UnityEvent refreshRequested = new UnityEvent();
        void OnEnable() { if (vehicle) vehicle.WheelAvailabilityChanged += Changed; refreshRequested.Invoke(); }
        void OnDisable() { if (vehicle) vehicle.WheelAvailabilityChanged -= Changed; }
        void Changed(int index, bool available)
        {
            Debug.Log($"Wheel {index}: available={available}", this);
            refreshRequested.Invoke(); // Re-read this vehicle's wheel configuration.
        }
    }
}
```

## Service repair with a speed guard

**Setup:** Assign vehicle and wire RequestRepair to a garage button.

**Behavior:** Repairs the vehicle through the shared API while nearly stationary. This is an application rule, not a change to collision damage policy.

Save as `RepairAtRest.cs`.

<!-- example: RepairAtRest.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class RepairAtRest : MonoBehaviour
    {
        public VehicleController vehicle;
        public UnityEvent rejected = new UnityEvent(), completed = new UnityEvent();
        public void RequestRepair()
        {
            if (!vehicle || vehicle.SpeedKph > .5f) { rejected.Invoke(); return; }
            vehicle.RepairAll();
            completed.Invoke();
            // Currency or inventory checks belong before RepairAll in your game.
        }
    }
}
```

## Recover after falling outside the playable area

**Setup:** Assign vehicle, a clear recovery marker and a world-space `Bounds` enclosing the playable region. Allow legitimate jumps/aircraft routes inside those bounds.

**Behavior:** Resets and repairs an out-of-bounds vehicle at the marker, with a cooldown to prevent a reset loop. The marker is assumed authored clear of obstacles; the script does not search for a safe pose.

Save as `WorldBoundsRecovery.cs`.

<!-- example: WorldBoundsRecovery.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class WorldBoundsRecovery : MonoBehaviour
    {
        public VehicleController vehicle;
        public Transform recovery;
        public Bounds allowed = new Bounds(Vector3.zero, new Vector3(2000, 500, 2000));
        [Min(.1f)] public float cooldownSeconds = 3;
        float nextRecovery;
        void Update()
        {
            if (!vehicle || !recovery || Time.time < nextRecovery ||
                allowed.Contains(vehicle.transform.position)) return;
            nextRecovery = Time.time + Mathf.Max(.1f, cooldownSeconds);
            vehicle.ResetVehicle(recovery.position, recovery.rotation);
        }
    }
}
```

## Offer a rescue after a car stays overturned

**Setup:** Assign a wheeled vehicle, a clear rescue marker and a separate rescue-button object. Wire that button to `Recover`.

**Behavior:** Shows the rescue option only after the car stays slow and inverted for several seconds. Rechecks the condition on click and repairs/resets at the authored marker; it does not automatically interrupt a rolling crash.

Save as `OverturnedRescueOffer.cs`.

<!-- example: OverturnedRescueOffer.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class OverturnedRescueOffer : MonoBehaviour
    {
        public VehicleController vehicle;
        public Transform rescue;
        public GameObject button;
        [Min(.1f)] public float dwellSeconds = 4;
        float elapsed;
        bool Eligible => vehicle && vehicle.SpeedKph < 2 &&
            Vector3.Dot(vehicle.transform.up, Vector3.up) < -.3f;
        void Update()
        {
            elapsed = Eligible ? elapsed + Time.deltaTime : 0;
            if (button) button.SetActive(elapsed >= dwellSeconds);
        }
        public void Recover()
        {
            if (!rescue || !Eligible || elapsed < dwellSeconds) return;
            vehicle.ResetVehicle(rescue.position, rescue.rotation); elapsed = 0;
        }
        void OnDisable() { elapsed = 0; if (button) button.SetActive(false); }
    }
}
```

## Apply a saved driving-assist preference in the garage

**Setup:** Assign the vehicle, its `TractionControl`, and optionally its `DrivingAssists` facade. Call `Apply` while parked; call `RestoreSaved` after references and configuration are ready.

**Behavior:** Persists a local player preference. If `DrivingAssists` is installed it uses the facade so its next tick does not undo the request. The default saved preference enables assistance; no vehicle configuration rebuild is needed.

Save as `GarageTractionPreference.cs`.

<!-- example: GarageTractionPreference.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class GarageTractionPreference : MonoBehaviour
    {
        public VehicleController vehicle;
        public TractionControl traction;
        public DrivingAssists assists;
        public string preferenceKey = "vehicle.traction.enabled";
        public UnityEvent rejected = new UnityEvent();
        public void RestoreSaved() { Apply(PlayerPrefs.GetInt(preferenceKey, 1) != 0); }
        public void Apply(bool enabled)
        {
            if (!vehicle || vehicle.IsMoving() || (!assists && !traction))
            { rejected.Invoke(); return; }
            if (assists) assists.SetTractionControl(enabled);
            else traction.SetTractionControlEnabled(enabled);
            PlayerPrefs.SetInt(preferenceKey, enabled ? 1 : 0);
            PlayerPrefs.Save(); // Persist on a menu action, never every frame.
        }
    }
}
```

## Prepare a retained vehicle for its next rental

**Setup:** Assign a vehicle, its dedicated `InputBuffer` and an authored clear depot marker. The rental flow calls `ReturnToDepot` after the game has removed occupants through its own passenger access policy.

**Behavior:** Checks seats are empty, clears buffered requests, releases the selected input source, stops the engine and resets/repairs the vehicle. It deliberately does not refuel, refill weapons or erase application inventory.

Save as `RentalVehicleReturn.cs`.

<!-- example: RentalVehicleReturn.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class RentalVehicleReturn : MonoBehaviour
    {
        public VehicleController vehicle;
        public InputBuffer controls;
        public Transform depot;
        public UnityEvent returned = new UnityEvent(), rejected = new UnityEvent();
        public void ReturnToDepot()
        {
            if (!vehicle || !depot) { rejected.Invoke(); return; }
            foreach (var seat in vehicle.GetComponentsInChildren<PassengerSeat>(true))
                if (seat.GetComponentInParent<VehicleController>(true) == vehicle && seat.Occupant)
                { rejected.Invoke(); return; }
            if (controls) controls.ClearControls();
            vehicle.SetInputSource(null);
            if (vehicle.TryGetModule<Engine>(out var engine)) engine.StopEngine();
            vehicle.ResetVehicle(depot.position, depot.rotation);
            returned.Invoke();
        }
    }
}
```

## Spend one repair kit on a named wheel

**Setup:** Assign vehicle, its retained `WheelPart`, and a kit count. Give the wheel a unique registered part ID. Call `UseKit` from inventory UI while stationary.

**Behavior:** Consumes a kit only when a detached wheel is successfully repaired by ID. It cannot recreate destroyed debris, and a mounted wheel does not consume a kit. Full body repair remains a different action.

Save as `RoadsideWheelRepairKit.cs`.

<!-- example: RoadsideWheelRepairKit.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class RoadsideWheelRepairKit : MonoBehaviour
    {
        public VehicleController vehicle;
        public WheelPart wheelPart;
        [Min(0)] public int kits = 1;
        public UnityEvent repaired = new UnityEvent(), rejected = new UnityEvent();
        public void UseKit()
        {
            if (!vehicle || !wheelPart || kits <= 0 || vehicle.IsMoving() ||
                !wheelPart.IsDetached || !vehicle.RepairPart(wheelPart.partId))
            { rejected.Invoke(); return; }
            kits--; repaired.Invoke();
        }
    }
}
```
