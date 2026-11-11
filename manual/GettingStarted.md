# Getting started

For existing vehicles, [Basic Inspector workflow](InspectorConfiguration.md#basic-inspector-workflow) explains how to add components, fill lists, assign scene objects versus profile assets, apply settings and save prefab changes. Its subsystem table leads to practical setups for lights, suspension, audio, particles, damage and cockpit equipment.

## Install the package

1. Open a Unity **6000.0.84f1** or newer project and sign in with the Unity account used to acquire Ultra Vehicle System from the Asset Store.
2. Open **Window → Package Management → Package Manager** and select **My Assets**.
3. Select **Ultra Vehicle System**, click **Download** if needed, then **Import**.
4. In the **Import Unity Package** window, keep the package files selected. Keep **Documentation** for the manual and **Demo** for the example scene and vehicles, then click **Import**.
5. Find the imported content under `Assets/Szczyglis/UltraVehicleSystem`. The manual is in `Documentation`; the example scene is `Demo/Demo.unity`.

The package requires Unity **6000.0.84f1** or newer and Unity Input System **1.19.0**. Install Input System through Package Manager if it is not already present. The supplied demo uses URP materials. Use a compatible URP project for its intended appearance; when using another render pipeline, supply suitable materials for the sample models and effects. The vehicle mechanics do not require URP.

## Run the supplied scene

1. Keep **Demo** selected when importing the package from My Assets.
2. Open `Assets/Szczyglis/UltraVehicleSystem/Demo/Demo.unity`.
3. Enter Play Mode. Use the on-screen vehicle list to identify selection keys and the selected vehicle's control hints.
4. Use Page Up / Page Down to cycle vehicles, Tab or C to change camera mode and R to reset the selected vehicle's pose.

See [Demo](Demo.md) for the controls.

## Create your first wheel vehicle

This walkthrough builds a four-wheel car from your own model.

**Video tutorial:** [Create your first vehicle](https://www.youtube.com/watch?v=vm_SU-W8ODY)

### 1. Prepare the root and model

1. Create a root GameObject named **Car**. Use scale **(1, 1, 1)**, local **+Z forward** and **+Y up**.
2. Place the body model beneath it. Keep imported mesh scale/orientation corrections on model children.
3. Add a **Rigidbody** to the root and a suitable chassis collider. Keep the chassis collider clear of the wheel volumes. Wheels share the root Rigidbody; do not add a Rigidbody to each tire.
4. Select the root and choose **Tools → UltraVehicleSystem → Add Vehicle → Wheeled**. This adds VehicleController and the supporting modules.

### 2. Add a Wheel component for each tire

1. Create a **Wheels** child beneath the root.
2. Under Wheels, create an empty object for the first wheel, for example **WheelFL**. Place its pivot at the visible tire center. Keep its scale at **(1, 1, 1)** and its axes aligned with the vehicle.
3. On that object choose **Add Component → UltraVehicleSystem → Physics → Wheels → Wheel**. Adding **Wheel** also adds the required Unity **WheelCollider** on the same object.
4. Assign the visible tire's transform to **Wheel → Visual**. Use a centered visual pivot with the imported mesh beneath it if the source mesh has an offset origin. The visual pivot must be separate from the WheelCollider object: Wheel moves the visual to match suspension, steering and tire spin.
5. Set **Radius**, **Width** and **Mass** to match this tire. Radius is half the outside tire diameter, in metres. Review the WheelCollider gizmo against the model.
6. Set the wheel roles: enable **Steering** on front wheels, **Driven** on the driven axle, **Brake** for service braking and **Handbrake** on the intended parking-brake wheels.
7. Repeat for the remaining tires, for example **WheelFR**, **WheelRL** and **WheelRR**. Check each Visual assignment and pivot position individually.

For a first rear-wheel-drive car, use this role setup:

| Wheels | Steering | Driven | Brake | Handbrake |
| --- | --- | --- | --- | --- |
| Front pair | On | Off | On | Off |
| Rear pair | Off | On | On | On |

Enable Driven on both pairs for all-wheel drive. Wheel count and roles can be changed for other axle layouts.

### 3. Register and configure the wheels

1. Select the vehicle root and open **VehicleController → Wheels**.
2. Click **Discover child Wheel Colliders** to populate **Wheel Setup** from the child wheels.
3. Expand every entry. Check its WheelCollider, wheel visual, radius and Steer/Drive/Brake/Handbrake roles. Add an optional caliper visual if needed.
4. Use **Advanced wheel configuration** for width, mass, steering multiplier, drive weight and visual rotation offsets. After discovery, **Wheel Setup** is the authoring source used when the controller configures the Wheel components; make further tuning changes here.
5. Click **Apply vehicle configuration**. Resolve validation messages before checking.

### 4. Connect input and check

1. In **Setup**, check the input source installed by the preset. Use the keyboard sample, `ActionInput` or your own `IVehicleInput` provider.
2. Set the vehicle mass, center of mass and drivetrain values for your model. Adjust suspension travel, spring and damping for its weight.
3. Place the vehicle above a ground collider and enter Play Mode. Check tire contact, steering direction, acceleration and braking.
4. If a mesh rotates incorrectly, adjust its child orientation or Wheel Setup rotation offset. Check steering multipliers if an axle steers the wrong way.
5. Exit Play Mode, save tuning and references, then save the vehicle as a prefab.

The configured vehicle should have supported wheels, correct steering, forward acceleration and a stop under braking. If it does not, use [Troubleshooting](Troubleshooting.md) before adding more systems.

Choose the next feature in [Choose systems](ChoosingSystems.md). Assign its model geometry and assets explicitly. Non-wheel modes can use an empty wheel list; aircraft can use authored landing gear. Setup cannot infer model-specific hinges, seats or effect outlets.

Continue with [Configuration](Configuration.md), [Drive profiles](DriveProfiles.md) and [Vehicle tuning](VehicleTuning.md). For custom mechanics and replacements, see [Scripting](Scripting.md).
