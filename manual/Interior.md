# Plan the cockpit

Use this page to plan passenger and cockpit integration and find the guide that owns each setup. The package separates seat occupancy, character pose, control movement and gameplay actions so you can use a cockpit with or without a visible driver.

## Pick a starting point

| Goal | Start here | Then add |
| --- | --- | --- |
| Driver mannequin in an existing vehicle | [Passengers](Passengers.md) | Anatomy, seated fitting and grips |
| Prepare a reusable physical character | [Human anatomy](HumanAnatomy.md) | A vehicle seat and contact targets |
| Player walks into/out of vehicles | [Passenger access](PassengerAccess.md) | Application locomotion/input/camera handover |
| Working gauges and cockpit controls | [Interior controls](InteriorControls.md) | Optional passenger contacts and gestures |
| Hand reaches to operate an existing control | [Timed interactions](ControlInteractions.md) | Input/UI selection and action feedback |
| Mirrors or digital screens | [Interior systems](InteriorSystems.md) | The relevant cockpit control bindings |

You do not have to implement the entire stack. A racing camera can use gauges without a driver body. An externally animated passenger can use seat occupancy without a physical ragdoll. A physical driver can hold a stationary handle even when the application has no clickable cockpit.

## Documentation boundaries

Each guide has one primary responsibility. Follow its linked prerequisites instead of repeating setup in several components.

| Guide | Owns this setup | Follow its links for |
| --- | --- | --- |
| [Passengers](Passengers.md) | Core/seats, body sources, controller modes, occupancy and character lifetime | Seat support, anatomy and boarding |
| [Passenger access](PassengerAccess.md) | Outside endpoints, admission/clearance, door and boarding clips, reservation/completion | Immediate occupancy and ordinary seated gestures |
| [Human anatomy](HumanAnatomy.md) | Avatar/bone mapping, physical skeleton, saved anatomical joints and prefab validation | Vehicle-specific support and finger fitting |
| [Seats](Seats.md) | Body fitting, pelvis/chest support, rider support and release policy | Limb targets and finger fitting |
| [Handles](Handles.md) | Hand/foot targets, limb ownership, control transfers, compliant rests and foot pins | Moving control geometry and finger fitting |
| [Hand grips](SteeringHandGrip.md) | Palm/finger calibration, control surface dimensions, motorcycle preparation and regrip | Limb mode assignment and physical seat fitting |
| [Interior controls](InteriorControls.md) | Moving geometry, needles, pedals, switches, aircraft controls and mechanic bindings | Passenger fitting, gestures and display systems |
| [Timed interactions](ControlInteractions.md) | One action's admission, contact commit, gesture timing, completion and cancellation | Control geometry and changes in seat occupancy |
| [Interior systems](InteriorSystems.md) | Mirror rendering, digital panels, fuel/assist actions | Cockpit switches and telemetry extensions |

Detailed signatures and implementation contracts remain in [Scripting](Scripting.md) and [API](API.md). Exact Inspector field meanings remain in the [Inspector reference](InspectorReference.md). These setup guides explain how to combine the parts.

## A reliable construction order

1. **Verify the vehicle.** Drive it with a known input source and confirm steering, engine and gearbox state before building cockpit visuals.
2. **Prepare the character independently.** Validate its Avatar, physical bones and saved anatomy if using a ragdoll. Save it as a reusable character prefab.
3. **Establish occupancy.** Add a seat and attach/spawn the intended character with the chosen controller mode. Confirm one seat has one occupant.
4. **Fit body support and contacts.** Position the seat origin, hand/foot destinations and grip surfaces. Test static support, then vehicle movement.
5. **Build instrument movement.** Add controls one at a time and check their value sources, units, ranges and update owners.
6. **Connect player actions.** Use a binding/API request first, then an optional timed gesture. Verify that the mechanic changes once and the control reflects its result.
7. **Add boarding and application handover.** Integrate walking/input/camera ownership only after direct entry and the seated setup work.
8. **Test interruption and reuse.** Exit, eject, disable, reset and reuse the vehicle/character. Check that old callbacks and contacts do not retain ownership.

Keep a small test scene with one representative character and vehicle. It is easier to isolate a bad joint or marker there than in a full gameplay scene containing several animation/input systems.

## Decide who owns each state

One system should write each pose or gameplay value at a time. An input source owns the vehicle command; an engine/gearbox owns accepted mechanical state; a control animator owns its visual Transform; a passenger controller/limb policy owns the body; an access/interaction request temporarily owns its transition.

A visual switch changing position is not proof its requested mechanic change was accepted. An empty seat is not proof an animated exit has finished. A correct preview pose is not proof physical constraints remain stable while driving. Observe the appropriate result for each layer.

Prefer separate Transforms for stationary cabin geometry, neutral motion anchors, moving carriers and moving hand contacts. The actual hierarchy conventions are centralized in [moving geometry](InteriorControls.md#prepare-moving-geometry) and [seat contacts](Handles.md#bind-a-limb-to-a-control).

## Save and reuse deliberately

Save anatomical/finger calibration on the character prefab, vehicle geometry/bindings on the vehicle prefab, and access clip/timing settings in profile assets. Keep application player identity, input/camera authority and detached-character lifetime in your gameplay integration.

Review preview-generated changes and prefab overrides before applying them. Refit a replacement character instead of assuming equal height means equal limb lengths, palm frames and fingers. At runtime, refresh discovery/register new modules using the relevant public API; changing the hierarchy alone is not every system's reconfiguration signal.
