# Exterior wipers

`Wipers` is an `ExteriorModule`. Add the module from **VehicleController > Modules > Add module... > Exterior**, or use **Add Component > UltraVehicleSystem > Exterior > Wipers** and **Tools > UltraVehicleSystem > Add Component > Exterior > Wipers**. The same menu group contains `WiperBlade` and `WiperSwitchBinding`. Register/discover directly added modules through the vehicle controller. Cockpit stalks remain interior controls and connect to the exterior wiper system through `WiperSwitchBinding`.

## Wipers

### Geometry and registration

1. Add `Wipers` to the vehicle.
2. Add `WiperBlade` to each blade assembly and assign its **Motion** moving part, independent spindle anchor and local axis. Set the blade's minimum/maximum angles for park and full sweep.
3. Add one entry to the module's **Wipers** list for each helper. Set a stable unique **Id** and assign **Helper**. A helper by itself does not animate autonomously; it must be in this list.
4. Choose the entry's wiper type as appropriate for the assembly. Prefer the helper path for model-mounted geometry; direct pivot fields are available when no helper is assigned.
5. Test the module's running state and sweep at a low speed. Confirm both park and maximum travel before enabling audio.

IDs are case-sensitive. Use meaningful IDs such as `FrontLeft`, `FrontRight` and `Rear`; they identify entries for runtime operations, not hierarchy searches. The supplied demo uses `Wiper1`, `Wiper2` and so on. Missing/duplicate IDs should be corrected before connecting individual controls.

### Shared and individual settings

With **Independent Settings** off, an entry inherits the module's shared running/speed defaults. Enable it for that blade's own initial **Running** state and **Cycles Per Minute**. This is useful for a rear wiper that should not automatically start with the front pair.

**Cycles Per Minute** is a full outward-and-return sweep rate, not degrees per second. Each entry can follow its own phase/rate. A speed of zero pauses travel; a stop request allows the current cycle to finish and park. Use the explicit Park operation when immediate parking is required.

| API action | Scope |
| --- | --- |
| `SetRunning(bool)` / `Toggle()` | Request collective running/off state |
| `SetSpeed(float)` | Apply a collective speed in cycles/minute |
| ID overloads | Change the selected blade's request/rate |
| `RestoreWiperControl(id)` | Return the entry to its configured individual/shared policy |
| `Park(id)` / `ParkAll()` | Move immediately to park |
| `RegisterWiper` / `UnregisterWiper` | Change runtime membership using valid IDs |

Collective running changes replace running requests while preserving individual speeds. A collective speed change replaces those rates. `IsRunning` reports that at least one blade has a running request; it is different from `IsParked`, which reports that all blades are at rest. Read `GetWiper`, `IsWiperRunning` and `GetSpeed` for a specific entry.

### Blade audio

New Wipers components added in the editor receive WiperSweepOutward.wav and WiperSweepReturn.wav from the package’s Resources/Audio/Interior folder as shared audio defaults. Replace or clear these clips for a different sound or silence; per-blade Override Audio remains independent. Runtime-created components need explicit clip assignments.

Assign an entry **Audio Source** if a particular scene source should be used. With **Override Audio** off, it inherits the module's shared audio choices. Enable that override for different outward/return clips, volume or pitch synchronization. Independently moving blades need independently timed audio; the module can generate voices when no source is assigned.

Check sound at both slow and fast wipe rates. Synchronization should follow the sweep rather than replaying one unrelated loop on every frame. Missing clips should not be diagnosed as a geometry problem; verify silent blade motion first.

### Individual runtime control

Attach this helper to a UI/gameplay object and assign Wipers. Its IDs match the demo naming; replace them with your configured IDs for another vehicle. Connect a Button to the appropriate void method.

**Example: `IndividualWiperControl.cs`**

<!-- example: IndividualWiperControl.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class IndividualWiperControl : MonoBehaviour
    {
        public Wipers wipers;
        public void StartFirst()
        {
            if (!wipers) return;
            wipers.SetSpeed("Wiper1", 60);
            wipers.SetRunning("Wiper1", true);
        }
        public void StopFirst() { if (wipers) wipers.SetRunning("Wiper1", false); }
        public void StartAll() { if (wipers) wipers.SetRunning(true); }
        public void ParkAllNow() { if (wipers) wipers.ParkAll(); }
    }
}
```

Disabling Wipers parks its blades and releases its active presentation. A cockpit on/off switch belongs to [the wiper-switch recipe](InteriorControls.md#wiper-switch); multi-speed or independent blade controls call the API above. The [wiper reference](Scripting/MovingParts.md#wipers) covers phases, callbacks and runtime ownership.
