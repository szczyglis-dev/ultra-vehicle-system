# Gearbox setup

A gearbox connects engine RPM/torque to driven-wheel speed through selectable ratios. Configure it after basic wheel roles and engine operation work. This page owns gear selection and ratios; [Clutch](Clutch.md), [Differential](Differential.md) and [Traction control](TractionControl.md) describe the subsequent coupling/sharing/intervention layers.

## Inspector quick start

1. Select the root and open **Modules > Engine**. Confirm Engine is enabled. Add **Automatic Gearbox**, **Manual Gearbox**, or both with **Transmission** through **Add module...**.
2. For one gearbox, drag its component into **Engine > Gearbox**. With Transmission installed, assign its Engine and gearbox references and choose its mode there instead of setting two competing owners of the engine connection.
3. Expand the gearbox. Add **Forward Ratios** in gear order and set **Reverse Ratio** and **Final Drive**, or use speed-at-redline authoring below. Check the driven wheel roles/radii in **Wheels > Wheel Setup**.
4. Set shift timing/direction guards, apply vehicle configuration and save. In Play Mode, test launch, a shift, neutral and reverse. Use **Live** to distinguish selected gear from actual speed/RPM.

## Choose the transmission arrangement

| Arrangement | Configure | Behavior |
| --- | --- | --- |
| Automatic | Connect `AutomaticGearbox` to Engine | Chooses forward gears from loaded road-speed/RPM evidence and handles signed direction requests |
| Manual | Connect `ManualGearbox` to Engine | Explicit gear/shift requests; selected gear determines direction |
| Selectable | Add `Transmission`, assign Engine and both gearbox plugins | Runtime Automatic/Manual/Direct selection |
| Direct transmission | No active gearbox connected | Propulsion without selectable ratios/gears |

Transmission **Direct** still uses vehicle physics and ordinary throttle/brake input. It is different from `DirectController`, whose [direct movement mode](Input.md) owns the chassis pose and adapts presentation to that motion.

## Configure

1. Add/register the chosen gearbox and assign **Engine > Gearbox**, or let `Transmission` own that connection.
2. Choose direct ratio authoring or speed-at-redline authoring below; do not expect both to remain independent.
3. Set **Final Drive**, **Efficiency**, **Shift Duration** and **Direction Change Speed**.
4. For an automatic, set shift thresholds and minimum gear time with a useful RPM gap.
5. Apply configuration, then test every forward gear, neutral and reverse using a repeatable road.

When Transmission is installed, edit its selected mode/references rather than repeatedly replacing Engine.gearbox from another script. It preserves a compatible safe gear on handover or falls back to neutral when needed. Disabling the selector disconnects its engine gearbox connection; disabling a gearbox also removes it from `Engine.ActiveGearbox`.

### Author ratios directly

Leave **Gear Speed Limits Kph** empty. Enter positive **Forward Ratios** in gear order, first gear at array index 0. Ordinarily the reduction decreases as gear number increases. **Reverse Ratio** is also positive; the gearbox applies the reverse sign internally. Final Drive multiplies either reduction.

For example, first gear 4 and final drive 3 give an overall reduction of 12:1. Ignoring slip, 3000 engine RPM corresponds to 250 wheel RPM. With a 0.3 m rolling radius that is about 28.3 km/h. Actual acceleration/top speed still depends on available torque/power, losses, wheel slip and load.

Higher reduction gives greater wheel torque and less road speed at the same engine RPM. Lower reduction gives more road speed but can make launch/climbing difficult. Efficiency scales transmitted output; it is not a speed limit.

### Author speed at redline

A nonempty **Gear Speed Limits Kph** array derives forward ratios during engine/gearbox configuration from engine maximum RPM, driven-wheel radius and final drive. One entry corresponds to each forward gear. Use increasing positive road-speed targets. These are redline gearing targets, not independent hard per-gear road-speed clamps.

**Reverse Speed Limit Kph** participates when custom speed-range authoring is active; zero retains the existing reverse ratio. Changing wheel radius or engine maximum RPM requires reapplying configuration to derive the intended ratios again. Clear the speed array before returning to direct ratio authoring.

Speed fields retain their declared stored units while the Inspector can display your selected unit. Follow [Speed units](SpeedUnits.md) when copying numeric tuning from code or external data.

## Automatic shift decisions

**Upshift RPM** and **Downshift RPM** are separated thresholds. **Minimum Gear Time** spaces automatic upshifts and direction changes. Low-RPM downshifts bypass that dwell and can skip intermediate ratios during rapid braking, while respecting loaded road-speed evidence, safe RPM, clutch guards and an in-progress shift. At standstill, first gear can be selected as soon as the current shift finishes. **Shift Duration** is the mechanical shift interruption itself. A narrow threshold gap can hunt between gears even when the shift animation looks correct.

Automatic forward selection uses road-speed estimates from loaded native driven-wheel contacts. Free-spinning airborne tires are not evidence that the vehicle has accelerated along the road. A jump or supplemental tire touch therefore need not cause an automatic upshift.

An open/driver-controlled slipping clutch suppresses automatic forward shifts while the driver owns coupling. Tune the engine's useful RPM range first, then choose shift points that leave the next gear in a usable range. Do not solve missing native support or constant brake demand by lowering the shift threshold.

## Manual selection and direction safety

Gear numbers are −1 reverse, 0 neutral and positive forward indices. With a manual gearbox, positive throttle drives the selected gear and braking is separate. Input adapter mappings and signed forward/reverse behavior are described in [Input](Input.md).

For the supplied signed automatic/direct driving behavior, holding the reverse/brake direction while stopping is not an unconditional immediate reversal. Stop, release and press again as required by the direction-request logic. **Reverse Engage Speed** allows a small standstill tolerance; Direction Change Speed guards selecting a gear against significant opposite motion. Slope release tolerances are coordinated with Brakes.

Use command requests or `TrySelectGear`/`TryShiftUp`/`TryShiftDown` for custom controls. Requests can fail for an invalid/same gear, an in-progress shift, unsafe reversal or a target ratio that would exceed engine redline. The vehicle-context overload also requires this to be the engine's active gearbox. A false result is not an automatic retry queue.

`GearChanged` reports accepted gear state; `ShiftStarted` and `ShiftCompleted` describe the interval. Connect a cockpit indicator/paddle to the accepted state through [Interior controls](InteriorControls.md#animate-a-gear-paddle), instead of assuming every input press selected a gear.

## Verify and troubleshoot

| Symptom | Check |
| --- | --- |
| Engine revs but car does not drive | Neutral, clutch engagement, engine running and driven wheels |
| Ratios change after Apply | Nonempty speed-at-redline authoring owns derived ratios |
| No automatic shift while airborne | Expected loaded-native-contact requirement |
| Automatic hunts between gears | Threshold gap, minimum gear time and useful next-gear RPM |
| Reverse request is ignored | Release/repress state, direction speed and current shift |
| Manual downshift is rejected | Predicted engine RPM in the lower gear |
| Selector changes to neutral | Safe handover could not preserve a gear with the new ratios/direction |

For the algorithm, code examples and API, see [Drive dynamics](Scripting/DriveDynamics.md#engine-and-gearbox) and [API](API/DriveDynamics.md).
