# Passengers and handle interactions

Application-level gestures share HandleController ownership with normal controls. An assigned seat, registered handle ID, allowed limbs and reachable anchors are required. A rejected request is an expected result.

See [Handles implementation](../Handles.md) for the underlying contracts.

## Trigger a one-shot dashboard gesture

**Setup:** Assign vehicle, seat and a handle ID. Connect the arrived event to presentation feedback.

**Behavior:** The controller chooses an allowed limb, transfers it, invokes arrival and returns it using the handle’s timing. Use one request per click.

Save as `DashboardGestureButton.cs`.

<!-- example: DashboardGestureButton.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class DashboardGestureButton : MonoBehaviour
    {
        public VehicleController vehicle;
        public PassengerSeat seat;
        public string handleId = "DashboardButton";
        public UnityEvent arrived = new UnityEvent(), rejected = new UnityEvent();
        public void Press()
        {
            if (!vehicle || !seat || !vehicle.handles.TryGet(handleId, out var handle) ||
                vehicle.handles.TryUse(seat, handle, () => arrived.Invoke()) == null) rejected.Invoke();
            // Arrival is visual contact; connect actual control logic through its own owner.
        }
    }
}
```

## Hold a hand at an auxiliary control

**Setup:** Assign a seat and handle that supports the chosen limb. Call BeginHold/EndHold from paired UI events.

**Behavior:** Keeps the hand at the control until released. Disabling returns an outstanding request, preventing forgotten ownership.

Save as `HeldPassengerGesture.cs`.

<!-- example: HeldPassengerGesture.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class HeldPassengerGesture : MonoBehaviour
    {
        // Read or request state through its owning component; do not bypass the vehicle pipeline.
        public VehicleController vehicle;
        public PassengerSeat seat;
        public string handleId = "radio";
        public PassengerBodyPart limb = PassengerBodyPart.RightHand;
        HandleUse use;
        public void BeginHold()
        {
            if (use != null && use.IsActive) return;
            if (vehicle && seat) use = vehicle.handles.TryReachAndHold(seat, limb, vehicle.handles.Get(handleId));
        }
        public void EndHold() { if (use != null && use.IsActive) use.Return(); use = null; }
        void OnDisable() { EndHold(); }
    }
}
```

## Show per-hand occupancy

**Setup:** Assign vehicle, seat and separate left/right status objects.

**Behavior:** Shows active transfer ownership per limb; one hand’s request does not imply that the other hand is busy.

Save as `HandBusyIndicator.cs`.

<!-- example: HandBusyIndicator.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class HandBusyIndicator : MonoBehaviour
    {
        public VehicleController vehicle;
        public PassengerSeat seat;
        public GameObject leftBusy, rightBusy;
        void Update()
        {
            if (!vehicle || !seat) return;
            if (leftBusy) leftBusy.SetActive(vehicle.handles.GetUse(seat, PassengerBodyPart.LeftHand) != null);
            if (rightBusy) rightBusy.SetActive(vehicle.handles.GetUse(seat, PassengerBodyPart.RightHand) != null);
            // A resting hand on its home handle has no temporary HandleUse.
        }
    }
}
```

## Gate an interaction by seat occupancy

**Setup:** Assign the intended seat and connect accepted/rejected callbacks.

**Behavior:** Rejects an empty seat without spawning or relocating a passenger. Useful before starting dialogue, payment or cockpit interactions.

Save as `SeatOccupancyGate.cs`.

<!-- example: SeatOccupancyGate.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class SeatOccupancyGate : MonoBehaviour
    {
        public PassengerSeat seat;
        public UnityEvent accepted = new UnityEvent(), rejected = new UnityEvent();
        public void Request()
        {
            if (!seat || !seat.Occupant) { rejected.Invoke(); return; }
            // Occupancy is authoritative; a visible character nearby is insufficient.
            accepted.Invoke();
        }
    }
}
```

## Bound an application-owned boarding request

**Setup:** Assign PassengerAccess and a configured SeatAccess. Call Board from a button; this adapter must be the sole requester while its operation is running.

**Behavior:** Starts boarding, waits for the access system to become idle and cancels after a real-time timeout. Cancellation delegates cleanup to PassengerAccess and does not force the character pose.

Save as `PassengerAccessTimeout.cs`.

<!-- example: PassengerAccessTimeout.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class PassengerAccessTimeout : MonoBehaviour
    {
        public PassengerAccess access;
        public SeatAccess target;
        [Min(1)] public float timeoutSeconds = 10;
        float deadline;
        bool watching;
        public void Board()
        {
            if (!access || access.IsBusy || !access.TryEnter(target)) return;
            watching = true; deadline = Time.unscaledTime + timeoutSeconds;
        }
        void Update()
        {
            if (!watching) return;
            if (!access || !access.IsBusy) { watching = false; return; }
            if (Time.unscaledTime < deadline) return;
            // Let the access owner unwind reservations and its own animation resources.
            watching = false; access.Cancel();
        }
        void OnDisable() { if (watching && access && access.IsBusy) access.Cancel(); watching = false; }
    }
}
```

## Refuse a passenger exit while the vehicle is moving

**Setup:** Assign vehicle and the selected occupant's `PassengerAccess`. Connect `RequestExit` to the exit button; configure `SeatAccess` outside markers and the motion implementation normally.

**Behavior:** Requests the access system's normal exit sequence only while the chassis is stationary and no access sequence is busy. Refusal reports an event. It does not teleport the occupant or bypass exit reservations.

Save as `StoppedPassengerExit.cs`.

<!-- example: StoppedPassengerExit.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class StoppedPassengerExit : MonoBehaviour
    {
        public VehicleController vehicle;
        public PassengerAccess access;
        public UnityEvent rejected = new UnityEvent();
        public void RequestExit()
        {
            if (!vehicle || !access || vehicle.IsMoving() || access.IsBusy || !access.TryExit())
                rejected.Invoke();
        }
    }
}
```

## Hold a radio handle only while push-to-talk is held

**Setup:** Assign vehicle, an occupied seat and a reachable radio handle allowing the right hand. Connect button press/release to `Press`/`Release`; connect `transmittingChanged` to your radio UI/audio integration.

**Behavior:** Starts transmission only after the hand reaches the radio. Release stops transmission immediately and returns the owned hand token. Losing the request, seat occupant or component also stops transmission; it never cancels another requester's token.

Save as `PassengerRadioPushToTalk.cs`.

<!-- example: PassengerRadioPushToTalk.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class PassengerRadioPushToTalk : MonoBehaviour
    {
        public VehicleController vehicle;
        public PassengerSeat seat;
        public string handleId = "radio";
        public UnityEvent<bool> transmittingChanged = new UnityEvent<bool>();
        HandleUse use;
        PassengerBody speaker;
        bool transmitting;
        public void Press()
        {
            if (!isActiveAndEnabled || !vehicle || !seat || !seat.Occupant ||
                (use != null && use.IsActive)) return;
            speaker = seat.Occupant;
            use = vehicle.handles.TryReachAndHold(seat, PassengerBodyPart.RightHand,
                vehicle.handles.Get(handleId));
        }
        void Update()
        {
            if (use == null || !use.IsActive || !seat || seat.Occupant != speaker)
            { Release(); return; }
            // A persistent request is holding only after arrival.
            SetTransmitting(use.Phase == HandleUsePhase.Holding);
        }
        void SetTransmitting(bool value)
        {
            if (transmitting == value) return;
            transmitting = value; transmittingChanged.Invoke(value);
        }
        public void Release()
        {
            SetTransmitting(false);
            if (use != null && use.IsActive) use.Return();
            use = null; speaker = null;
        }
        void OnDisable() { Release(); }
    }
}
```

## Release driving controls when the driver seat becomes empty

**Setup:** Assign vehicle, its driver `PassengerSeat` and the player `InputBuffer` used by this driver. The boarding flow is responsible for granting that source again after the next driver enters.

**Behavior:** On seat vacancy, clears this buffer and releases the vehicle input source only if it still owns control. It leaves an AI/replay source assigned by another system alone. It does not apply a parking brake to an unattended rolling vehicle.

Save as `VacantDriverControlRelease.cs`.

<!-- example: VacantDriverControlRelease.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class VacantDriverControlRelease : MonoBehaviour
    {
        public VehicleController vehicle;
        public PassengerSeat driver;
        public InputBuffer playerInput;
        void OnEnable()
        {
            if (driver) driver.Exited += Exited;
            if (driver && !driver.Occupant) ReleasePlayer();
        }
        void OnDisable() { if (driver) driver.Exited -= Exited; }
        void Exited(PassengerBody body, PassengerExitReason reason) { ReleasePlayer(); }
        void ReleasePlayer()
        {
            if (playerInput) playerInput.ClearControls();
            if (vehicle && playerInput && vehicle.inputSource == playerInput)
                vehicle.SetInputSource(null);
        }
    }
}
```

## Show remaining passenger capacity on a bus sign

**Setup:** Assign the passenger seats to count, excluding the driver seat, and connect `spacesChanged` to the sign or boarding UI. Include disabled/unusable seats only if your game treats them as capacity.

**Behavior:** Publishes free seat count only when it changes. Reads actual occupant state, not visible character count. A free seat may still be reserved by an entry sequence; `PassengerAccess` remains the authority for admission.

Save as `PassengerCapacitySign.cs`.

<!-- example: PassengerCapacitySign.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class PassengerCapacitySign : MonoBehaviour
    {
        public PassengerSeat[] passengerSeats;
        public UnityEvent<int> spacesChanged = new UnityEvent<int>();
        int previous = -1;
        void OnEnable() { previous = -1; Refresh(); }
        void Update() { Refresh(); }
        void Refresh()
        {
            int free = 0;
            foreach (var seat in passengerSeats ?? System.Array.Empty<PassengerSeat>())
                if (seat && !seat.Occupant) free++;
            if (free == previous) return;
            previous = free; spacesChanged.Invoke(free);
        }
    }
}
```

## Validate a bus ticket when the hand reaches the reader

**Setup:** Assign vehicle, the customer seat and a reachable ticket-reader handle. Call `ValidateTicket` after your inventory/payment policy allows the attempt. Connect `validated` to consume the ticket and update the fare UI.

**Behavior:** Commits once at visual contact, provided the same occupant is still seated and the vehicle is stopped. Refused/cancelled reaches do not consume a ticket. A per-occupant latch prevents repeat payment from repeated clicks; the ticket inventory remains application-owned.

Save as `TicketValidationGesture.cs`.

<!-- example: TicketValidationGesture.cs -->
```csharp
using UnityEngine;
using UnityEngine.Events;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples.Cookbook
{
    public sealed class TicketValidationGesture : MonoBehaviour
    {
        public VehicleController vehicle;
        public PassengerSeat seat;
        public string readerId = "TicketReader";
        public UnityEvent validated = new UnityEvent(), rejected = new UnityEvent();
        HandleUse use;
        PassengerBody paidPassenger;
        public void ValidateTicket()
        {
            if (!vehicle || !seat || !seat.Occupant || vehicle.IsMoving() ||
                seat.Occupant == paidPassenger || (use != null && use.IsActive))
            { rejected.Invoke(); return; }
            var customer = seat.Occupant;
            use = vehicle.handles.TryUse(seat, vehicle.handles.Get(readerId), () =>
            {
                if (!seat || seat.Occupant != customer || !vehicle || vehicle.IsMoving()) return;
                paidPassenger = customer; validated.Invoke();
            });
            if (use == null) rejected.Invoke();
        }
        void OnDisable() { if (use != null && use.IsActive) use.Cancel(); use = null; }
    }
}
```
