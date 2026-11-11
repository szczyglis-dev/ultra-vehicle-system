# Differential setup

`Differential` redistributes propulsion between paired driven wheels. Without it, engine output follows the ordinary per-wheel Drive Weight allocation. Add it when an axle needs open, limited-slip or finite locked coupling; it does not provide a centre differential between complete axles.

## Inspector quick start

1. Select the root and add/expand **Modules > Engine > Differential**. First verify both intended wheels drive in **Wheels > Wheel Setup**.
2. Expand **Axles**, press **+**, enable the entry and drag its two native WheelCollider components into **First** and **Second**. Use the contacts, not the tire meshes.
3. Choose a coupling mode and tune its parameters below. Add another pair for another driven axle; do not reuse a wheel in two pairs.
4. Apply/save and test a straight launch, a tight turn and one wheel on low-grip ground.

## Configure an axle

1. Add/register Differential on the vehicle.
2. Add one enabled **Axles** entry and assign its First/Second native WheelColliders, normally the two wheels of one axle.
3. Ensure both appear in this vehicle's Wheel Setup, are operational, have Drive enabled and have positive Drive Weight.
4. Choose the module's differential mode and tune its matching parameters below.
5. Add another pair for another driven axle. Each wheel should appear in only one pair.
6. Test straight driving, a wide turn, a tight turn and a split-grip launch with one side on lower-traction ground.

The mode is shared by the configured pairs. Disabled/invalid/duplicate pairs are skipped; unpaired wheels retain their base allocation. Service braking/handbrake steps do not receive fresh propulsion from differential coupling. For a tracked vehicle, start with its [side-drive policy](Tracked.md) rather than assuming an axle differential is a substitute for track steering.

## Choose the coupling policy

| Mode | What it does | Tune |
| --- | --- | --- |
| Open | Equal torque on both sides, limited by the lower estimated traction capacity | Traction Coefficient and the actual contact/load |
| Limited Slip | Redistributes the existing pair torque toward the slower or supported wheel | Torque Bias Ratio and Slip RPM Range |
| Locked | Adds finite opposing shaft-coupling torques against wheel-speed difference | Locked Coupling and Maximum Lock Torque |

### Open

A low-load/low-grip side limits both wheels' usable axle torque. The capacity estimate uses native contact force, wheel radius, forward-friction stiffness and **Traction Coefficient**. A wheel without that loaded native contact can therefore limit propulsion strongly.

Use a split-grip surface test to verify this deliberately. Increasing engine torque is not a fix for the intended open-differential limitation. If the vehicle must pull through a lifted wheel, compare a limited-slip policy instead.

### Limited slip

**Torque Bias Ratio** limits the split in favor of one side. A ratio of 3 permits up to a 3:1 split, or 75%/25%, rather than giving the preferred wheel unlimited torque. **Slip RPM Range** determines how much rotational-speed difference produces a strong bias. Smaller values respond to smaller differences.

Support state also influences the bias when only one wheel is grounded. The module redistributes the available pair torque rather than silently deleting the excess based on a traction estimate; tire forces and TCS still determine whether the result spins.

### Locked

Locked Coupling converts wheel-RPM difference into opposing transfer torque, capped by Maximum Lock Torque. It approximates finite shaft coupling rather than instantly forcing both wheels to exactly the same angular speed.

Tight turns require different path lengths on each side. Strong coupling can therefore produce scrub/understeer and make the vehicle resist turning. Test it with your tire stiffness and TCS policy; do not increase the lock cap merely to conceal a wheel that lacks contact.

## Interaction with the rest of the drivetrain

Tune base wheel roles and engine allocation first. Compare Differential enabled/disabled with the same setup, then introduce [TCS](TractionControl.md) so you can distinguish redistribution from torque reduction. A locked pair can legitimately have opposite individual coupling contributions; one wheel's torque alone is not the engine's total output.

Use [per-wheel telemetry](Scripting/Events.md#diagnostic-snapshot) for RPM, native submitted torque, support and slip. A missing axle effect often means invalid assignments, duplicate pairs, disabled wheels or braking priority rather than too-small bias.

## Troubleshoot

| Symptom | Check |
| --- | --- |
| One pair does nothing | Enabled entry, owned collider references, driven roles and positive weights |
| Pair disappears after adding another | Duplicate wheel assignment; one wheel cannot be processed twice |
| Open axle loses pull with one wheel raised | Expected low-side traction limit |
| LSD still spins a tire | Bias redistributes torque; it does not guarantee adhesion |
| Locked axle fights steering | Coupling strength/cap, tire scrub and turn radius |

For a complete axle configuration example and torque calculations, see [Drive dynamics](Scripting/DriveDynamics.md#differential) and [API](API/DriveDynamics.md).
