# Clutch setup

`Clutch` controls how much engine torque reaches the active transmission. It supports automatic launch/coasting assistance and a driver-controlled pedal, including stored flywheel energy during a launch. Configure the [gearbox](Gearbox.md) first so neutral, ratio and shift behavior can be distinguished from clutch slip.

## Inspector quick start

1. Select the root and add/expand **Modules > Engine > Clutch**, with a working Engine and gearbox present.
2. Assign **Engine > Clutch** and the clutch's Engine reference where needed. Begin with automatic assistance to test launching without custom pedal input.
3. Set capacity and engagement behavior below. For pedal control, bind the continuous clutch channel on the input source; moving a pedal mesh alone does not operate the clutch.
4. Apply/save, then test launch, disengagement/coasting and shifting before tuning flywheel launches or effects.

## Configure

1. Add/register Clutch and assign **Engine > Clutch**, or let engine configuration resolve its registered module. Check the clutch's Engine reference too.
2. Choose automatic assistance or continuous driver ownership below.
3. Set **Torque Capacity** against engine crankshaft torque and **Engine > Rotational Inertia** for the intended flywheel response.
4. Bind the clutch channel in your input source: **0 means pedal released/coupled; 1 means pedal depressed/disconnected**.
5. Test free revving, gradual launch, abrupt release, a shift and throttle-off coasting before tuning traction intervention.

Do not connect a visual `PedalAnimator` as the engine input source. It displays demand; the actual command comes through `InputBuffer.SetClutch(float)`, an ActionInput axis or another `IVehicleInput` implementation. See [Input](Input.md) and [pedal presentation](InteriorControls.md#pedals-and-foot-movement).

## Automatic assistance and pedal override

With **Automatic** enabled, the module assists ordinary launch/coasting coupling. Touching the driver clutch pedal gives the driver direct control even with automatic assistance configured. The override is retained while the physical launch synchronizes; releasing the button does not necessarily mean the assistance resumes on that exact same frame.

**Engagement Rate** smooths automatic engagement. Driver pedal/button changes apply without a hidden return ramp. If the engine is stopped, effective coupling is zero. Neutral and an active gear shift also force disengagement.

With Automatic off, **Manual Engagement** is a multiplier for the driver's coupling: target engagement is that multiplier times `(1 − pedal)`, subject to neutral/shift behavior. `SetManualEngagement` also selects manual control. Do not confuse this engagement value with the pedal amount, whose convention is reversed.

| Reading | Meaning |
| --- | --- |
| Pedal | Driver command, 0 released to 1 depressed |
| Engagement | Effective coupling, 0 open to 1 engaged |
| DriverControlled | Driver/manual coupling owns the current response |
| SlipRpm | Engine speed minus coupled shaft speed |

## Capacity and flywheel response

Torque Capacity is the maximum crankshaft torque transmitted by a fully engaged clutch, in N·m. Set it in the engine domain, before gearbox/final-drive multiplication. Too little capacity causes prolonged slipping; very high capacity makes an abrupt release transfer energy more forcefully.

Rotational Inertia determines how much energy is stored at a given RPM and how quickly engine speed responds. More inertia does not add engine power, but a revved engine can briefly transfer stored energy on release. Compare engine RPM, clutch slip and wheel speed during a launch rather than judging only engine sound.

**Allow Launch Wheelspin** permits the stored flywheel-energy share to exceed the normal traction-control propulsion budget briefly. Disable it when TCS should contain that share too. This is distinct from raising the engine's continuous power or the tire's grip.

## Coasting and braking

**Engine Braking Torque** supplies speed-dependent shaft drag during appropriate automatic coasting. It is not a static parking brake and should not hold a stopped vehicle on a slope. Configure service brakes, handbrake/parking and [coasting behavior](Suspension.md#wheel-spin-and-coasting) separately.

The engine includes idle support. This model does not simulate engine stalls or clutch heat/wear, so a stalled real-world launch should not be expected to reproduce every consequence here.

## Test and diagnose

Run the same flat-road launch with no driver pedal, partial pedal and a full depress/release. Then test on a slope with explicit braking. Change capacity and inertia separately so their effects remain identifiable.

| Symptom | Inspect |
| --- | --- |
| Pedal works backwards | Command convention: 1 disconnects |
| Car never moves although RPM rises | Neutral, stopped engine, low capacity or zero Manual Engagement |
| Automatic stops shifting after clutch use | Driver-controlled/slipping state is still active |
| Launch wheelspin remains with TCS | Allow Launch Wheelspin and the inertial torque share |
| Vehicle rolls after throttle release | Engine drag is not a parking brake |

For energy transfer, clutch/gearbox coordination and exact methods, see [Drive dynamics](Scripting/DriveDynamics.md#clutch) and its [API](API/DriveDynamics.md).
