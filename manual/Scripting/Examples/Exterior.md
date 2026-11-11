# Exterior equipment

Small policies for lights, wipers and moving model parts. Configure the underlying components and their references before attaching these scripts.

See [MovingParts implementation](../MovingParts.md) for the underlying contracts.

## Map rain intensity to wiper speed

**Setup:** Assign Wipers. Call SetRain from your weather system; this adapter owns the running request.

**Behavior:** Starts above light rain and stops below it; Wipers performs its normal parking motion. Speed is cycles per minute.

Save as `RainWiperPolicy.cs`.

<!-- example: RainWiperPolicy.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class RainWiperPolicy : MonoBehaviour
    {
        public Wipers wipers;
        public void SetRain(float intensity)
        {
            if (!wipers) return;
            float rain = Mathf.Clamp01(intensity);
            wipers.SetSpeed(Mathf.Lerp(25, 70, rain));
            wipers.SetRunning(rain > .1f);
            // Do not stop a native animation clock or rotate the blades directly.
        }
    }
}
```

## Temporary arrival warning

**Setup:** Assign Lights and call Show when a delivery is completed.

**Behavior:** Shows hazards for four seconds, then restores the previous indicator request if nobody changed it in the meantime.

Save as `ArrivalHazards.cs`.

<!-- example: ArrivalHazards.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class ArrivalHazards : MonoBehaviour
    {
        // Read or request state through its owning component; do not bypass the vehicle pipeline.
        public Lights lights;
        IndicatorState previous;
        float remaining;
        public void Show()
        {
            if (!lights) return;
            if (remaining <= 0) previous = lights.Indicators;
            lights.SetHazards(true); remaining = 4;
        }
        void Update() { if (remaining > 0 && (remaining -= Time.deltaTime) <= 0) Restore(); }
        void Restore()
        {
            if (lights && lights.Indicators == IndicatorState.Hazard) lights.SetIndicators(previous);
            remaining = 0;
        }
        void OnDisable() { if (remaining > 0) Restore(); }
    }
}
```

## Hood button with a speed guard

**Setup:** Assign a rotational MovingPart and vehicle. Set closed/open angles to match its authored frame.

**Behavior:** Refuses new opening requests while moving. It does not force a moving hood shut or implement a physical latch.

Save as `StationaryHoodButton.cs`.

<!-- example: StationaryHoodButton.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class StationaryHoodButton : MonoBehaviour
    {
        // Read or request state through its owning component; do not bypass the vehicle pipeline.
        public VehicleController vehicle;
        public MovingPart hood;
        public float closedAngle, openAngle = 55;
        public UnityEvent blocked = new UnityEvent();
        public void Open()
        {
            if (!vehicle || !hood || vehicle.SpeedKph > .5f) { blocked.Invoke(); return; }
            hood.SetTargetAngle(openAngle);
        }
        public void Close() { if (hood) hood.SetTargetAngle(closedAngle); }
    }
}
```

## Show an opening-part warning

**Setup:** Assign one configured MovingPart and a separate lamp object.

**Behavior:** Lights while the part is more than 5% open. Polls a scalar state instead of duplicating its motion or start/completion events.

Save as `DoorOpenLamp.cs`.

<!-- example: DoorOpenLamp.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class DoorOpenLamp : MonoBehaviour
    {
        public MovingPart door;
        public GameObject lamp;
        void Update()
        {
            if (lamp) lamp.SetActive(door && door.NormalizedPosition > .05f);
            // Author closed as normalized zero; invert the condition for reversed models.
        }
    }
}
```

## Temporarily request low beams in a tunnel

**Setup:** Assign Lights. Your zone system calls EnterTunnel and LeaveTunnel for this vehicle; balance calls when zones overlap.

**Behavior:** Turns on low beams only if beams were off. Restores that prior state after the last zone is left, provided the driver has not selected a different beam mode.

Save as `TunnelBeamLease.cs`.

<!-- example: TunnelBeamLease.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class TunnelBeamLease : MonoBehaviour
    {
        public Lights lights;
        int zones;
        bool changed;
        public void EnterTunnel()
        {
            if (!lights) return;
            if (zones++ > 0) return;
            changed = lights.BeamMode == BeamMode.Off;
            if (changed) lights.SetBeamMode(BeamMode.Low);
        }
        public void LeaveTunnel()
        {
            if (zones <= 0 || --zones > 0) return;
            Restore();
        }
        void Restore()
        {
            // Preserve an explicit change to high beams made while inside.
            if (changed && lights && lights.BeamMode == BeamMode.Low) lights.SetBeamMode(BeamMode.Off);
            changed = false;
        }
        void OnDisable() { zones = 0; Restore(); }
    }
}
```

## Switch headlights from the game day/night clock

**Setup:** Assign `Lights`. Your game clock calls `SetHour` with an hour in the 0–24 range. Use this as the sole automatic beam policy; disable it when manual beam ownership takes over.

**Behavior:** Requests low beams between dusk and dawn and off during daytime. Uses the game clock rather than the computer's local time. It owns beam mode, so do not run it alongside the tunnel beam lease or another beam writer.

Save as `DayNightHeadlightPolicy.cs`.

<!-- example: DayNightHeadlightPolicy.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class DayNightHeadlightPolicy : MonoBehaviour
    {
        public Lights lights;
        [Range(0, 24)] public float dusk = 18, dawn = 6;
        public void SetHour(float hour)
        {
            if (!isActiveAndEnabled || !lights || !float.IsFinite(hour)) return;
            hour = Mathf.Repeat(hour, 24);
            bool night = dusk >= dawn ? hour >= dusk || hour < dawn : hour >= dusk && hour < dawn;
            lights.SetBeamMode(night ? BeamMode.Low : BeamMode.Off);
        }
    }
}
```

## Enable a dedicated work light while reversing

**Setup:** Assign vehicle, `Lights` and a custom light ID already authored in `Lights`. Use a separate channel from the normal reverse lamps.

**Behavior:** Enables the work light during actual rearward motion and turns it off when that motion ends or this owner is disabled. Does not override normal reverse-light or gearbox behavior.

Save as `ReverseWorkLight.cs`.

<!-- example: ReverseWorkLight.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class ReverseWorkLight : MonoBehaviour
    {
        public VehicleController vehicle;
        public Lights lights;
        public string lightId = "RearWork";
        void Update()
        {
            if (lights) lights.SetCustomLight(lightId, vehicle && vehicle.ForwardSpeed < -.2f);
        }
        void OnDisable() { if (lights) lights.SetCustomLight(lightId, false); }
    }
}
```

## Close an ordinary door after driving away

**Setup:** Assign vehicle and the `VehicleBodyPart` doors this policy may close. Exclude intentionally open equipment and detached debris.

**Behavior:** Requests close above a speed threshold through `VehicleBodyPart`, preserving its motion/hinge implementation. It does not close a door by rotating its mesh, and it does not prove the door has latched. Use a separate warning/interlock if departure must wait for closure.

Save as `DriveAwayDoorCloser.cs`.

<!-- example: DriveAwayDoorCloser.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class DriveAwayDoorCloser : MonoBehaviour
    {
        public VehicleController vehicle;
        public VehicleBodyPart[] doors;
        [Min(0)] public float closeAboveKph = 5;
        void Update()
        {
            if (!vehicle || vehicle.SpeedKph < closeAboveKph) return;
            foreach (var door in doors ?? System.Array.Empty<VehicleBodyPart>())
                if (door && !door.IsReleased && door.IsOpen) door.Close();
        }
    }
}
```

## Run a temporary windshield-wash wipe

**Setup:** Assign `Wipers` and connect `Wash` to the washer button. Connect `washerStarted` to your existing washer presentation. This component must own the running request during the wash interval.

**Behavior:** Keeps the existing wiper speed, temporarily starts wiping, then restores the previous running request. Repeated presses extend the same session. If manual/weather control should override it, call `CancelWithoutRestore` before transferring ownership.

Save as `WashWipeButton.cs`.

<!-- example: WashWipeButton.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class WashWipeButton : MonoBehaviour
    {
        public Wipers wipers;
        [Min(.1f)] public float washSeconds = 3;
        public UnityEvent washerStarted = new UnityEvent();
        bool washing, previousRunning;
        float remaining;
        public void Wash()
        {
            if (!wipers || !isActiveAndEnabled) return;
            if (!washing) previousRunning = wipers.IsRunning;
            washing = true; remaining = Mathf.Max(.1f, washSeconds);
            wipers.SetRunning(true); washerStarted.Invoke();
        }
        void Update()
        {
            if (washing && (remaining -= Time.deltaTime) <= 0) Restore();
        }
        void Restore()
        {
            if (washing && wipers) wipers.SetRunning(previousRunning);
            washing = false;
        }
        public void CancelWithoutRestore() { washing = false; remaining = 0; }
        void OnDisable() { Restore(); }
    }
}
```

## Warn on a low approach with gear not fully deployed

**Setup:** Assign an aircraft vehicle, its `LandingGear` and a separate warning object. Configure the aircraft ground sensor and suitable clearance/descent thresholds.

**Behavior:** Warns during a descending low approach when a valid ground reading exists and gear is not fully deployed. It never deploys gear automatically; gear transitions, ground lock and pilot actions retain their normal owner.

Save as `ApproachGearWarning.cs`.

<!-- example: ApproachGearWarning.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class ApproachGearWarning : MonoBehaviour
    {
        public VehicleController vehicle;
        public LandingGear gear;
        public GameObject warning;
        [Min(0)] public float warnBelowMetres = 40;
        void Update()
        {
            bool active = false;
            if (vehicle && gear)
            {
                var t = vehicle.Telemetry;
                active = t.HasGroundBelow && t.HeightAboveGround < warnBelowMetres &&
                    t.VerticalSpeed < -.5f && !gear.IsDeployed;
            }
            if (warning) warning.SetActive(active);
        }
        void OnDisable() { if (warning) warning.SetActive(false); }
    }
}
```
