# Engine, fuel and boost

Gameplay policies around the existing engine and boost modules. These scripts use public requests and retain the drivetrain’s normal eligibility and safety checks.

See [DriveDynamics implementation](../DriveDynamics.md) for the underlying contracts.

## Buy a bounded amount of fuel

**Setup:** Assign FuelTank and call BuyLitres from a service UI. Credit values are illustrative local game state.

**Behavior:** Charges only for litres the tank actually accepted; a nearly full tank cannot consume the full requested budget.

Save as `RefuelBudget.cs`.

<!-- example: RefuelBudget.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class RefuelBudget : MonoBehaviour
    {
        public FuelTank tank;
        [Min(0)] public float credits = 100, pricePerLitre = 2;
        public void BuyLitres(float requested)
        {
            if (!tank || requested <= 0 || pricePerLitre <= 0) return;
            float affordable = Mathf.Min(requested, credits / pricePerLitre);
            float accepted = tank.Refuel(affordable);
            // Refuel returns the actual addition, including capacity clamping.
            credits = Mathf.Max(0, credits - accepted * pricePerLitre);
        }
    }
}
```

## Fuel reserve warning with recovery threshold

**Setup:** Assign FuelTank and a dedicated lamp object.

**Behavior:** Reads initial state on enable, lights below 15%, and turns off only after refuelling above 20%.

Save as `FuelReserveLamp.cs`.

<!-- example: FuelReserveLamp.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class FuelReserveLamp : MonoBehaviour
    {
        public FuelTank tank;
        public GameObject lamp;
        bool low;
        void OnEnable() { if (tank) { tank.FuelChanged += Changed; Changed(tank.FuelLitres); } }
        void OnDisable() { if (tank) tank.FuelChanged -= Changed; }
        void Changed(float litres)
        {
            if (!tank) return;
            low = low ? tank.Fraction < .2f : tank.Fraction < .15f;
            if (lamp) lamp.SetActive(low); // Use a separate lamp, not this component's object.
        }
    }
}
```

## Request a timed Nitro burst

**Setup:** Assign Nitro. Call Burst from a power-up action; the component must remain enabled for the timer.

**Behavior:** A burst holds the Nitro API request for a duration. Fuel, throttle, braking, cooldown and supply can still prevent activation. This component must be the sole API request owner.

Save as `NitroBurstRequest.cs`.

<!-- example: NitroBurstRequest.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class NitroBurstRequest : MonoBehaviour
    {
        // Read or request state through its owning component; do not bypass the vehicle pipeline.
        public Nitro nitro;
        [Min(0)] public float seconds = 1;
        float remaining;
        public void Burst() { if (nitro) { remaining = seconds; nitro.SetBoost(remaining > 0); } }
        void Update()
        {
            if (remaining <= 0) return;
            remaining = Mathf.Max(0, remaining - Time.deltaTime);
            if (remaining == 0 && nitro) nitro.SetBoost(false);
        }
        void OnDisable() { remaining = 0; if (nitro) nitro.SetBoost(false); }
    }
}
```

## Stop an unattended idling engine

**Setup:** Assign vehicle, Engine and the driver PassengerSeat.

**Behavior:** Stops ignition after 30 seconds of near-stationary idle without a driver. It never automatically starts the engine again.

Save as `IdleEngineShutdown.cs`.

<!-- example: IdleEngineShutdown.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class IdleEngineShutdown : MonoBehaviour
    {
        // Only an empty driver seat qualifies as unattended.
        public VehicleController vehicle;
        public Engine engine;
        public PassengerSeat driver;
        [Min(0)] public float idleSeconds = 30;
        float elapsed;
        void Update()
        {
            bool waiting = vehicle && engine && driver && engine.IsRunning &&
                !driver.Occupant && vehicle.SpeedKph < .5f && engine.Throttle < .01f;
            elapsed = waiting ? elapsed + Time.deltaTime : 0;
            if (!waiting || elapsed < idleSeconds) return;
            engine.StopEngine();
            elapsed = 0;
        }
        void OnDisable() { elapsed = 0; }
    }
}
```

## Select a movement mode from a menu

**Setup:** Assign vehicle, ProfileSwitcher and a registered target ID, such as hover. Call Select from a button.

**Behavior:** Applies an application-level speed policy before requesting the switch; exposes rejection to UI instead of assuming it succeeded.

Save as `GuardedModeButton.cs`.

<!-- example: GuardedModeButton.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class GuardedModeButton : MonoBehaviour
    {
        public VehicleController vehicle;
        public ProfileSwitcher switcher;
        public string targetId = "Hover";
        public float maximumSpeedKph = 10;
        public UnityEvent rejected = new UnityEvent();
        public void Select()
        {
            if (!vehicle || !switcher || vehicle.SpeedKph > maximumSpeedKph ||
                !switcher.SwitchTo(targetId)) rejected.Invoke();
            // Register profiles in the switcher first; this script does not create them.
        }
    }
}
```

## Refuel continuously while parked at a pump

**Setup:** Assign vehicle, `Engine`, `FuelTank` and the pump location. Connect press/release UI events to `BeginFueling`/`EndFueling`; this session must be the only fuel writer while active.

**Behavior:** Adds litres only while the engine is off, the vehicle is stopped and the pump remains in range. `Tracks` the amount actually accepted; at capacity or after an invalid condition it ends. Payment authorization belongs before `BeginFueling`.

Save as `FuelPumpSession.cs`.

<!-- example: FuelPumpSession.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class FuelPumpSession : MonoBehaviour
    {
        public VehicleController vehicle;
        public Engine engine;
        public FuelTank tank;
        public Transform pump;
        [Min(0)] public float litresPerSecond = 1, reachMetres = 4;
        public float DeliveredLitres { get; private set; }
        bool fueling;
        public void BeginFueling() { DeliveredLitres = 0; fueling = true; }
        public void EndFueling() { fueling = false; }
        void Update()
        {
            if (!fueling) return;
            if (!vehicle || !engine || !tank || !pump || engine.IsRunning || vehicle.IsMoving() ||
                Vector3.Distance(vehicle.transform.position, pump.position) > reachMetres)
            { EndFueling(); return; }
            if (Time.deltaTime <= 0) return;
            float requested = Mathf.Max(0, litresPerSecond) * Time.deltaTime;
            float accepted = tank.Refuel(requested);
            DeliveredLitres += accepted;
            if (accepted < requested) EndFueling();
        }
        void OnDisable() { EndFueling(); }
    }
}
```

## Estimate range from a measured fuel burn rate

**Setup:** Assign vehicle. `Drive` with its `FuelTank` enabled and normal fuel consumption. Read `EstimatedKilometres` only when `HasEstimate` is true; call `ResetEstimate` for a new route.

**Behavior:** Integrates supported distance and the tank reported consumption rate over a minimum sample distance before estimating remaining range. The estimate reflects the recent accumulated driving mix, not a guaranteed reachable distance; instant refuel quantity is not mistaken for negative consumption.

Save as `EstimatedFuelRange.cs`.

<!-- example: EstimatedFuelRange.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class EstimatedFuelRange : MonoBehaviour
    {
        public VehicleController vehicle;
        [Min(1)] public float minimumMetres = 250;
        public bool HasEstimate { get; private set; }
        public float EstimatedKilometres { get; private set; }
        float metres, litres;
        public void ResetEstimate() { metres = litres = EstimatedKilometres = 0; HasEstimate = false; }
        void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
        void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; }
        void Sample(Telemetry t)
        {
            if (!t.HasFuelTank) { HasEstimate = false; return; }
            if (t.GroundedWheels > 0) metres += t.Velocity.magnitude * t.DeltaTime;
            litres += Mathf.Max(0, t.FuelLitresPerHour) * t.DeltaTime / 3600;
            HasEstimate = metres >= minimumMetres && litres > .001f;
            EstimatedKilometres = HasEstimate ? t.FuelLitres * metres / litres / 1000 : 0;
        }
    }
}
```

## Require a seated driver and brake before starting

**Setup:** Assign `Engine`, vehicle and the driver seat. Connect `StartPressed` to a UI/button action and `rejected` to feedback. Configure the normal fuel/ignition system first.

**Behavior:** Allows a start request only for an occupied driver seat with the sampled service-brake input held and the chassis stationary. Reports success only if the engine actually runs; an empty `FuelTank` can still reject ignition. This is a UI policy, so other ignition callers need the same game-level authorization.

Save as `BrakeToStartButton.cs`.

<!-- example: BrakeToStartButton.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class BrakeToStartButton : MonoBehaviour
    {
        public VehicleController vehicle;
        public Engine engine;
        public PassengerSeat driver;
        public UnityEvent started = new UnityEvent(), rejected = new UnityEvent();
        public void StartPressed()
        {
            if (!vehicle || !engine || !driver || !driver.Occupant || vehicle.IsMoving() ||
                vehicle.Command.ServiceBrake < .5f || engine.IsRunning)
            { rejected.Invoke(); return; }
            engine.StartEngine();
            if (engine.IsRunning) started.Invoke(); else rejected.Invoke();
        }
    }
}
```

## Consume a boost pickup only if charge was accepted

**Setup:** Assign a separate pickup visual and charge amount. Your collection trigger resolves the entering vehicle and calls `Collect(vehicle)`. Keep this component enabled until collection succeeds.

**Behavior:** Looks up the entrant's installed `Nitro` and consumes the pickup only when `AddNitro` returns a positive amount. A full reservoir or a vehicle without `Nitro` leaves the pickup available. No repeated collider callback can collect it twice.

Save as `NitroChargePickup.cs`.

<!-- example: NitroChargePickup.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class NitroChargePickup : MonoBehaviour
    {
        [Min(0)] public float charge = 10;
        public GameObject visual;
        public UnityEvent collected = new UnityEvent();
        bool spent;
        public void Collect(VehicleController entrant)
        {
            if (spent || !entrant || !entrant.TryGetModule<Nitro>(out var nitro)) return;
            if (nitro.AddNitro(charge) <= 0) return;
            spent = true;
            if (visual) visual.SetActive(false);
            collected.Invoke();
        }
    }
}
```

## Track a trip's fuel expense without charging refills twice

**Setup:** Assign vehicle and currency per litre. Call `BeginTrip` at dispatch and `EndTrip` after arrival. Read `LitresConsumed` and `Expense` in the trip report.

**Behavior:** Integrates `FuelTank`'s reported consumption rate in snapshot time, including idling. Refilling changes the reserve but does not directly increase this expense. Telemetry must come from an enabled `FuelTank` with consumption configured.

Save as `TripFuelExpense.cs`.

<!-- example: TripFuelExpense.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class TripFuelExpense : MonoBehaviour
    {
        public VehicleController vehicle;
        [Min(0)] public float currencyPerLitre = 2;
        public float LitresConsumed { get; private set; }
        public float Expense { get; private set; }
        bool recording;
        public void BeginTrip() { LitresConsumed = Expense = 0; recording = true; }
        public void EndTrip() { recording = false; }
        void OnEnable() { if (vehicle) vehicle.AfterPhysicsStep += Sample; }
        void OnDisable() { if (vehicle) vehicle.AfterPhysicsStep -= Sample; recording = false; }
        void Sample(Telemetry t)
        {
            if (!recording || !t.HasFuelTank) return;
            float consumed = Mathf.Max(0, t.FuelLitresPerHour) * t.DeltaTime / 3600;
            LitresConsumed += consumed;
            Expense += consumed * Mathf.Max(0, currencyPerLitre);
        }
    }
}
```
