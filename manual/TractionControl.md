# Traction control setup

`TractionControl` limits propulsion when driven-wheel contact indicates excess slip or demand exceeds the contact budget. It acts after differential/surface processing; braking and airborne wheel dynamics remain separate. Add it after ordinary engine, gearing, wheel roles and grip work.

## Inspector quick start

1. Select the root and add/expand **Modules > Engine > Traction Control**. Establish working Engine, driven-wheel contact and Friction settings first.
2. Check **Modules > Drive > Driving Assists** too: an enabled facade can own the traction-control switch. Configure it consistently with the desired TCS state.
3. Start with the slip and reduction/recovery parameters below. Apply vehicle configuration and save.
4. Compare the same launch with TCS on/off in Play Mode. Inspect wheel slip/torque in Live before increasing intervention; burnout has a separate intentional-slip policy.

## Tune intervention

1. Register/enable TractionControl and use a simple consistent road surface.
2. Check engine and per-wheel torque, native support and slip with TCS disabled first.
3. Enable TCS with its starting **Target Slip** and **Launch Reference Speed**.
4. Tune **Reduction Rate** for how rapidly it removes power and **Recovery Rate** for how quickly it returns it.
5. Tune the cornering options only after a straight launch is predictable.
6. Repeat the same launch/turn with TCS off to verify that the change is intervention rather than a different surface or input.

Use your intended tire dimensions, vehicle load and engine power. A physically broken contact setup cannot be corrected by a slip controller.

## Understand the tuning groups

| Setting | Influence |
| --- | --- |
| Target Slip | Slip amount the controller permits before stronger intervention |
| Launch Reference Speed | Low-speed reference for launch/slip calculations, in m/s |
| Traction Reserve | Fraction of estimated contact traction budget available for propulsion |
| Minimum Torque Scale | Lower bound for retained propulsion scale |
| Reduction / Recovery Rate | Speed of removing/restoring torque scale |
| Reserve Grip For Cornering | Leaves longitudinal capacity for lateral demand |
| Cornering Freedom | Allows more power-dependent slip during tight powered turns |

A lower target or smaller reserve is more restrictive. Faster reduction catches slip sooner; slow recovery can keep the car feeling weak after traction returns. Minimum Torque Scale is a torque fraction, not an engine RPM limit.

Do not compare low-speed ratios without considering Launch Reference Speed. Near standstill, tiny changes in contact speed can otherwise dominate a naive slip interpretation. Native tire contact, actual supported load and requested torque matter together.

## Cornering and clutch launches

With grip reserved for cornering, the controller reduces the longitudinal budget as lateral demand rises. Cornering Freedom relaxes powered-turn intervention, useful when a setup should retain some controlled wheelspin. It does not add lateral tire grip or change the vehicle's steering geometry.

A [locked differential](Differential.md) can create coupling torque within a pair; TCS must coexist with that transfer rather than treating every wheel torque as an independent engine. A [clutch launch](Clutch.md) can transfer stored flywheel energy: Allow Launch Wheelspin on Clutch determines whether that inertial share bypasses the normal propulsion budget briefly.

## Read state and switch it at runtime

| Reading | Meaning |
| --- | --- |
| `Active` | Currently intervening; it does not mean the component's enabled flag |
| `MinimumTorqueScale` | Lowest current driven-wheel propulsion scale; 1 means no reduction |
| `MaximumSlip` | Largest slip reported by the current intervention sampling |
| `ActiveChanged` | Intervention state changed |

Use `SetTractionControlEnabled`, inherited `SetEnabled`, or `VehicleController.SetModuleEnabled<TractionControl>` for a runtime enable/disable. Disabling resets its retained intervention state. Do not assign Active as a pause flag; it is a read-only result.

If `DrivingAssists` is enabled, configure the shared values and requested enabled state on that facade. Its next Apply/step can replace direct TCS/steering edits. The [interior systems guide](InteriorSystems.md#drivingassists) owns facade and cockpit-control integration.

## Diagnose unwanted intervention

| Symptom | Inspect first |
| --- | --- |
| Vehicle feels underpowered | Torque scale, recovery rate, contact/load and brake demand |
| Tires spin before intervention | Reduction rate, target slip and clutch inertial bypass |
| Steering under power loses too much drive | Cornering reserve/freedom and lateral grip |
| Intervention never occurs | Enabled/registered module, driven operational wheels and usable native contact |
| Turning the component off does not persist | Enabled DrivingAssists owns the state |

Use wheel diagnostics and the same road test before increasing engine power. Detailed contact-capacity calculations and a runtime control example are in [Drive dynamics](Scripting/DriveDynamics.md) and [API](API/DriveDynamics.md).
