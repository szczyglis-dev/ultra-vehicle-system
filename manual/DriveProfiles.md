# Vehicle types and drive strategies

A drive profile selects how a vehicle produces movement. The vehicle's registered modules still provide its engine, contacts, brakes and presentation. This page is the starting point for choosing and assembling a strategy; the linked guides own the detailed configuration of each subsystem.

## Choose a drive mode

Select the vehicle root and open **VehicleController > Setup > Drive mode**. Choose the movement family, then configure its settings, wheel roles and supporting modules. Selecting a different mode initializes its settings; subsequent configuration and entering Play Mode preserve your tuning unless a particular profile explicitly owns a module setting.

| Drive mode | Intended use | Continue with |
| --- | --- | --- |
| Wheeled | Cars, buses, trucks, tractors, monster trucks, quads/ATVs and other conventional wheeled vehicles | This page, then gearbox and suspension |
| Motorcycle | Motorcycles, motorbikes, bicycles and kick/electric scooters with rider lean and balance assistance | Motorcycle setup below |
| Tracked | Tanks, tracked carriers, bulldozers and other vehicles steered by their left/right tracks | [Tracked vehicles](Tracked.md) |
| Hover | Multirotor drones, quadcopters, hovercraft and flying cars with assisted hovering and sideways movement | [Combined vehicles](CombinedVehicles.md), [Aircraft](Aircraft.md) |
| Helicopter | Helicopters and other rotorcraft with collective lift, forward flight and optional altitude hold | [Aircraft](Aircraft.md) |
| Airplane | Conventional fixed-wing aircraft, such as light planes, trainers and propeller aircraft | [Aircraft](Aircraft.md) |
| Aerobatic Airplane | Aerobatic and stunt planes intended for loops, rolls and inverted flight | [Aircraft](Aircraft.md) |
| Jet | Jet aircraft, such as fighters and fast jets, with thrust-driven flight and body-rate controls | [Aircraft](Aircraft.md) |
| Boat | Motorboats, speedboats, patrol boats, ships and other powered surface vessels | [Boat](Boat.md) |
| Spaceship | Six-axis gravity-free spacecraft | Spacecraft setup below |
| Submarine | Submarines and powered underwater vehicles with depth and trim control | [Submarine](Submarine.md) |

Use Wheeled for different road models rather than looking for a separate physics mode for each body style. Their mass, wheelbase, torque, gearing and grip create the handling differences. A trailer is an independent unpowered vehicle configured through [Towing](Towing.md), not another powered drive strategy.

Keep an enabled registered `Drive` module: it runs the selected strategy. A profile cannot replace missing wheel/body geometry. In direct pose control, movement ownership instead belongs to [DirectController](Input.md); force-producing modules are skipped according to their direct-control support.

## Configure the selected mode

### Build the ground-vehicle baseline

1. Prepare a vehicle root with the correct real scale, +Z forward, Rigidbody and compound chassis colliders. Follow [Model conventions](VehicleModelConvention.md).
2. Configure **Wheel Setup** with each native WheelCollider, optional visual/caliper, radius, width and mass. Enable the intended steering, drive, service-brake and handbrake roles.
3. Set vehicle mass/centre of mass and the basic speed, steering and brake settings.
4. Register the engine, Drive, Steering, Brakes, Suspension and Friction modules needed by the setup. Use **Modules > Add module...** or a suitable quick setup, then discover/apply configuration when adding components directly.
5. Choose a transmission arrangement in [Gearbox](Gearbox.md). Add a clutch/differential/TCS only after basic propulsion works.
6. Tune loaded suspension on flat ground, then add contact helpers and special surfaces one at a time.
7. Add visual linkage, effects and cockpit readouts after the physical behavior is repeatable.

Drive Weight distributes base propulsion among driven wheels. Brake Multiplier changes an individual wheel's share of braking, while Steering Multiplier can invert or reduce a wheel's steering contribution. They are separate responsibilities; enabling Steer does not make a wheel driven. All assigned colliders must belong to this vehicle's Rigidbody, without duplicates.

The controller copies Wheel Setup into its Wheel adapters. Greyed-out fields on a bound helper/native collider indicate settings owned by the vehicle or a module. Edit the indicated source rather than attempting to retain changes to copied values.

### Follow the subsystem boundaries

| Guide | Configures |
| --- | --- |
| [Gearbox](Gearbox.md) | Ratio selection, direction safety, manual/automatic/direct transmission |
| [Clutch](Clutch.md) | Engine-to-transmission coupling and launch behavior |
| [Differential](Differential.md) | Torque sharing between paired driven wheels |
| [Traction control](TractionControl.md) | Slip-based propulsion intervention |
| [Suspension](Suspension.md) | Loaded support, force placement, damping, anti-roll and visible linkage |
| [Contact envelope](ContactEnvelope.md) | Lower rolling support over curbs/edges |
| [Solid tire contacts](TireCollision.md) | Sidewall/obstacle collision volumes |
| [Surfaces](Surfaces.md) | Physical grip versus tire-effect classification |
| [Tracked vehicles](Tracked.md) | Side slots, skid/pivot steering and visible belt construction |
| [Towing](Towing.md) | Independent trailers, coupling and brake forwarding |
| [Combined vehicles](CombinedVehicles.md) | Registered profiles, transitions and input routing |

Engine power/torque and general handling are explained in [Vehicle tuning](VehicleTuning.md); this chapter does not duplicate that configuration or the [input adapter setup](Input.md).

## Release and restore all vehicle forces

Release suspends propulsion, lift, buoyancy and driving/balance assistance, allowing the vehicle to fall or tumble. Native gravity, collider contacts and passive wheel suspension remain active.

In **Vehicle Controller > Setup > Drive mode**, enable **Release All Forces On Ignition Off** to release automatically when ignition is off. The default is **false**. Turning ignition on restores forces after an automatic release; disable the option to keep normal engine-off behavior.

- `vehicle.ReleaseAllForces()` releases manually until `vehicle.RestoreAllForces()` is called. `vehicle.ForcesReleased` reports the current state.
- Profiles expose the same operations with a `vehicle` argument and the query `AreForcesReleased(vehicle)`.
- Restore preserves pose and momentum and does not start the engine. It also overrides the current ignition-off interval; the next ignition cycle can release again.

The demo reset explicitly calls `RestoreAllForces()` before `ResetVehicle()`; reset itself does not restore forces. For custom module behavior, see [the module API](API/Modules.md#vehiclemodule).

## Motorcycle setup

Create front/rear contact wheels in Wheel Setup, with a front steering role and the intended driven/braked wheels. Confirm both tires support the bike and that wheelbase/centre of mass match the model before tuning assistance.

Add and enable `MotorcycleBalance`; it is an opt-in module and must be registered. **Maximum Lean** caps the requested bank, **Lean Rate** controls response, and balance strength/damping with a maximum angular acceleration determine upright/bank correction. The **Recovery Angle** limits the recovery behavior; assistance is not a guarantee that a fallen bike will always stand itself up.

At low speed, banking fades between **Lean Start Speed** and **Full Lean Speed**. **Steering Prediction** blends current wheel steering with anticipated driver steering; **Measured Acceleration Weight** adds measured lateral behavior. Change these after the baseline works, then compare requested/actual lean instead of increasing every gain together.

**Motorcycle Balance > Disable Balance On Driver Eject** lets the bike fall and tumble without assisted balance or Stabilization angular damping/righting after the driver is ejected. It is enabled on the demo motorcycle. Balance resumes when a driver enters again or the vehicle respawns; ejection from a passenger seat does not disable it. **Native Collision Response After Driver Eject** also removes additional body collision impulses while the riderless bike tumbles. Native collider contacts remain active.

Balance requires tire support from below; touching a wall does not activate upright assistance. Steering prediction follows the active Steering module’s resolved angle limit, including any optional speed or geometry limits you enable.

The demo motorcycle temporarily softens its springs and damping over several settling cycles after landing, without adding artificial hops. It disables launch wheelspin during nitro. Its suspension kick is smaller than the car preset. These remain configurable on **Suspension**, **Collisions**, and **Nitro**.

Bicycles can use the same Motorcycle profile and Balance Rider, with optional [Pedal Drive](Seats.md#independent-foot-policies) for moving pedal targets.

Test standstill, a slow turn, acceleration into a turn, braking and a release/fall. Rider pose and head support belong to [Seats](Seats.md#motorcycle-rider-support); they do not stabilize the motorcycle chassis.

## Spacecraft setup

**Spaceship Profile** extends Free Profile with local-axis thrust and rotation. Create it through **Tools > Ultra Vehicle System > Add Vehicle > Spaceship**. Gravity compensation allows stationary hovering; explicit Release All Forces also releases that compensation. Default drag and native damping are zero. **Align Flight Path** redirects travel toward the nose; **Stop Rotation On Release** brakes spin without leveling the craft. Disable these assists for inertial flight.

**Speed Sensitive Rotation** enables separate **Pitch/Yaw/Roll Rate By Speed** curves. X is actual travel speed in km/h; Y multiplies the corresponding **Angular Rates** value. One retains the base rate, zero disables commanded rotation on that axis, and values above one increase it. Empty curves use one. The initial curves describe a gentle reduction from 1 at rest to 0.65 at 300 km/h. This assistance remains off in new profiles and in the demo, preserving existing handling until enabled. Release braking and bank drift remain independent.

**Rotation Release Duration** controls the soft stop after releasing pitch, yaw or roll (default 1.1 seconds for approximately 95% settling); it does not automatically level the craft.

Optional **Bank Drift** sets a sideways flight-path offset from bank alone, independently of speed and throttle. **Bank Drift Enabled** switches the whole effect on or off. **Bank Drift Speed Multiplier** scales the lateral-to-forward speed ratio. **Maximum Bank Drift Angle** caps the base offset, **Bank Drift Response** smooths changes and **Bank Drift Exponent** shapes the bank response. Small banks can remain gentle while larger banks give a stronger effect. The same bank gives the same angle at low and high speeds; sideways distance travelled still scales with total travel speed. It works while coasting, without automatically yawing the craft. **Bank Drift Downwards** is off by default; enable it to add descent as the craft loses its upright orientation, including inverted flight. **Bank Drift Downward Multiplier** independently scales that downward component. Beyond 90° the drift continues toward the banked roof side rather than fading away; with downward drift disabled it stays horizontal and fades only near exact inversion, where no horizontal roof direction exists. Forward thrust follows the same direction when applied. At rest without propulsion, no bank force moves the craft. Leveling returns the assisted path to the nose. Manual strafe/lift and reverse bypass the effect. This is configurable spacecraft assistance, not aerodynamic lift.

**Keyboard Spaceship Input** retains forward thrust; Space clears thrust and brakes to a stop. Engine RPM follows thrust demand, and fresh setup uses Idle RPM = 0. See [input bindings](Input.md#keyboard-bindings) and the [profile settings](InspectorReference/Drive.md#spaceshipprofile).

## Diagnose the assembled vehicle

Use [telemetry](Scripting/Events.md#diagnostic-snapshot) to compare command, resolved braking, engine torque, gear and individual wheel state. Check enabled/registered modules and profile compatibility before treating every missing force as an engine problem.

If RPM rises without propulsion, inspect neutral/clutch, driven-wheel roles and contact. If the vehicle cannot coast, inspect brake/parking demand and wheel/chassis overlap. If it drives on flat ground but fails at curbs, investigate the contact guides rather than changing ratios. Reproduce one fault in a simple test lane before adding more assistance.

## Add a custom mode

Derive a serializable class from `DriveProfile` or a built-in family. Concrete custom profiles appear in the selector after compilation. A profile should own its movement policy and initial settings, while vehicle instances/modules own their transient state and model references.

See [independent profile example](Scripting/DriveProfiles.md#create-an-independent-profile-from-scratch) or [extend a movement family](Scripting/DriveProfiles.md#derive-from-a-movement-family). Register alternative configurations and transitions through [Combined vehicles](CombinedVehicles.md), rather than putting several active movement owners on one chassis.
