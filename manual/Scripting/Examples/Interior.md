# Interior data sources

Custom scalar sources plug into an interior animator’s data source field. They publish values only; the receiving animator owns mesh motion, limits and handle synchronization.

See [Interior implementation](../Interior.md) for the underlying contracts.

## Altitude relative to a captured origin

**Setup:** Assign vehicle and a needle configured in metres. Call CaptureOrigin at the start of an exercise.

**Behavior:** Reports signed height along gravity-up from the captured chassis position; climbing is positive. This is displacement, not ground clearance or absolute sea-level altitude.

Save as `RelativeAltitudeSource.cs`.

<!-- example: RelativeAltitudeSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class RelativeAltitudeSource : InteriorValueSource
    {
        public VehicleController vehicle;
        Vector3 origin;
        bool ready;
        void OnEnable() { CaptureOrigin(); }
        public void CaptureOrigin()
        {
            if (!vehicle) return;
            origin = vehicle.Telemetry.Position; ready = true;
        }
        public override float ReadValue()
        {
            if (!vehicle || !ready) return 0;
            // Keep the reference independent of a rotated cockpit or banked aircraft.
            Vector3 up = Physics.gravity.sqrMagnitude > .0001f ? -Physics.gravity.normalized : Vector3.up;
            return Vector3.Dot(vehicle.Telemetry.Position - origin, up);
        }
    }
}
```

## Steering-column degrees for a custom dial

**Setup:** Assign vehicle, then assign this source to a rotary instrument.

**Behavior:** Outputs signed logical steering-wheel degrees. Configure the receiving range for the full authored steering lock.

Save as `SignedSteeringDegreesSource.cs`.

<!-- example: SignedSteeringDegreesSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class SignedSteeringDegreesSource : InteriorValueSource
    {
        public VehicleController vehicle;
        public bool invert;
        public override float ReadValue()
        {
            // Logical wheel angle is independent of a model's visual axis convention.
            float degrees = vehicle ? vehicle.SteeringWheelAngle : 0;
            return invert ? -degrees : degrees;
        }
    }
}
```

## Peak-speed memory needle

**Setup:** Assign vehicle. Call ResetPeak from a UI action. Configure a needle for km/h.

**Behavior:** Tracks peak speed in Update, so the needle can read the stored value without mutating source state.

Save as `PeakSpeedMemorySource.cs`.

<!-- example: PeakSpeedMemorySource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class PeakSpeedMemorySource : InteriorValueSource
    {
        // ReadValue stays side-effect free; accumulation happens once per render frame.
        public VehicleController vehicle;
        float peakKph;
        void Update()
        {
            if (vehicle) peakKph = Mathf.Max(peakKph, vehicle.SpeedKph);
        }
        public void ResetPeak() { peakKph = 0; }
        public override float ReadValue() => peakKph;
    }
}
```

## Filtered brake-pressure display

**Setup:** Assign vehicle and use a 0–1 input range on the instrument.

**Behavior:** Filters resolved service-brake demand for presentation only. It does not delay actual brakes or other control animators.

Save as `BrakePressureFilterSource.cs`.

<!-- example: BrakePressureFilterSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class BrakePressureFilterSource : InteriorValueSource
    {
        public VehicleController vehicle;
        [Min(0)] public float response = 12;
        float displayed;
        void OnEnable() { displayed = vehicle ? vehicle.ServiceBrake : 0; }
        void Update()
        {
            float target = vehicle ? vehicle.ServiceBrake : 0;
            // Exponential response behaves consistently across render frame rates.
            displayed = Mathf.Lerp(displayed, target, 1 - Mathf.Exp(-response * Time.deltaTime));
        }
        public override float ReadValue() => displayed;
    }
}
```

## Nitro reserve gauge

**Setup:** Assign Nitro and use a 0–1 instrument range.

**Behavior:** Shows available charge, not current boost strength. Depletion/refilling is reflected on the next read.

Save as `NitroReserveSource.cs`.

<!-- example: NitroReserveSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class NitroReserveSource : InteriorValueSource
    {
        public Nitro nitro;
        public bool showUsedInstead;
        public override float ReadValue()
        {
            if (!nitro) return 0;
            float available = nitro.NormalizedAmount;
            // Inversion permits a gauge whose empty/full artwork is reversed.
            return showUsedInstead ? 1 - available : available;
        }
    }
}
```

## Drive a fuel gauge with the real tank fraction

**Setup:** Assign `FuelTank`, then assign this source to the instrument's data-source field. Configure the instrument input range as 0–100.

**Behavior:** Publishes remaining fuel percent with an optional usable-reserve offset. The reserve can map a practical empty mark above literal tank empty; it does not remove or reserve actual fuel.

Save as `FuelPercentGaugeSource.cs`.

<!-- example: FuelPercentGaugeSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class FuelPercentGaugeSource : InteriorValueSource
    {
        public FuelTank tank;
        [Min(0)] public float unusableReserveLitres;
        public override float ReadValue()
        {
            if (!tank) return 0;
            float reserve = Mathf.Clamp(unusableReserveLitres, 0, tank.capacityLitres);
            float usableCapacity = tank.capacityLitres - reserve;
            return usableCapacity > .001f
                ? Mathf.Clamp01((tank.FuelLitres - reserve) / usableCapacity) * 100 : 0;
        }
    }
}
```

## Build a signed turn-rate instrument

**Setup:** Assign vehicle and a signed instrument input range in degrees per second, for example −30 to +30. Invert the source only if the artwork needs it.

**Behavior:** Projects snapshot angular velocity onto gravity-up and converts radians to degrees. Reads actual chassis rotation rather than steering demand, so a stopped turned wheel does not show a turn rate.

Save as `TurnRateGaugeSource.cs`.

<!-- example: TurnRateGaugeSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class TurnRateGaugeSource : InteriorValueSource
    {
        public VehicleController vehicle;
        public bool invert;
        public override float ReadValue()
        {
            if (!vehicle) return 0;
            Vector3 up = Physics.gravity.sqrMagnitude > .001f ? -Physics.gravity.normalized : Vector3.up;
            float rate = Vector3.Dot(vehicle.Telemetry.AngularVelocity, up) * Mathf.Rad2Deg;
            return invert ? -rate : rate;
        }
    }
}
```

## Show climb rate in feet per minute

**Setup:** Assign an aircraft vehicle and a signed needle range in ft/min. Use negative values for descent.

**Behavior:** Converts gravity-relative vertical velocity from the telemetry snapshot. Applies an optional render-frame low-pass filter; reading the source does not advance the filter or change flight physics.

Save as `ClimbRateFeetSource.cs`.

<!-- example: ClimbRateFeetSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class ClimbRateFeetSource : InteriorValueSource
    {
        public VehicleController vehicle;
        [Min(0)] public float response = 4;
        float displayed;
        void OnEnable() { displayed = Target(); }
        float Target() => vehicle ? vehicle.Telemetry.VerticalSpeed * 196.8504f : 0;
        void Update()
        {
            displayed = Mathf.Lerp(displayed, Target(),
                1 - Mathf.Exp(-Mathf.Max(0, response) * Time.deltaTime));
        }
        public override float ReadValue() => displayed;
    }
}
```

## Move a gear-position pointer from accepted gearbox state

**Setup:** Assign `Engine` and a rotary instrument with authored positions for input −1 (reverse), 0 (neutral) and positive forward gear numbers. Use the actual forward gear range for your gearbox.

**Behavior:** Reads the selected gearbox's accepted gear, not a queued button request. If there is no gearbox the value is neutral; the separate GearLabel remains more suitable for text in direct-drive modes.

Save as `GearPositionGaugeSource.cs`.

<!-- example: GearPositionGaugeSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class GearPositionGaugeSource : InteriorValueSource
    {
        public Engine engine;
        public override float ReadValue()
        {
            var gearbox = engine ? engine.ActiveGearbox : null;
            return gearbox ? gearbox.CurrentGear : 0;
        }
    }
}
```

## Feed a ground-clearance gauge with a validity flag

**Setup:** Assign vehicle and a needle range in metres. Your UI can use `HasReading` to display an unavailable flag when the ground sensor has no hit.

**Behavior:** Clamps a valid measured clearance to the instrument scale. Returns zero when unavailable but exposes validity separately, so a missing reading need not be presented as actual zero clearance.

Save as `GroundClearanceGaugeSource.cs`.

<!-- example: GroundClearanceGaugeSource.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class GroundClearanceGaugeSource : InteriorValueSource
    {
        public VehicleController vehicle;
        [Min(.1f)] public float maximumMetres = 100;
        public bool HasReading => vehicle && vehicle.Telemetry.HasGroundBelow;
        public override float ReadValue()
        {
            if (!HasReading) return 0;
            return Mathf.Clamp(vehicle.Telemetry.HeightAboveGround, 0, Mathf.Max(.1f, maximumMetres));
        }
    }
}
```
