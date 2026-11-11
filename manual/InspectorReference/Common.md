# Common settings and base components

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [SceneGizmoOptions](#scenegizmooptions) | 17 |
| [Settings](#settings) | 10 |
| [VehicleModule](#vehiclemodule) | 2 |

## SceneGizmoOptions

**Source:** `Runtime/Core/SceneGizmoOptions.cs`. Serialized editor presentation settings shown by the custom Gizmos foldout. Only groups applicable to the selected component are displayed; these settings do not affect simulation. See [scene gizmo visibility](../Configuration.md#scene-gizmo-visibility).

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchors` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `axes` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `bones` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `centerOfMass` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `clearance` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `connections` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `editingHandles` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `exit` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `feet` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `geometry` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `hands` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `labels` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `pads` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `path` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `pelvis` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `ranges` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |
| `wheels` | `bool` | Show this guide group where supported by the owning component; editor presentation only. | `true` |

## Settings

Serializable shared configuration read by vehicle mechanics; apply configuration when changing persistent native setup.

**Source:** `Runtime/Core/Settings.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `brakeTorque` | `float` | Service-brake torque in N·m at full braking before each wheel's Brake Multiplier. Increase for stronger braking; handbrake strength is configured separately. | `6000`; Minimum: 0 |
| `centerOfMass` | `Vector3` | Rigidbody centre of mass in chassis-local metres. Lower Y to reduce rollover tendency; moving X or Z shifts side/front/rear loading. This is relative to the vehicle root, not the model pivot. | `new Vector3(0, 0.37941176, -0.0882353)` |
| `grip` | `float` | Multiplies the vehicle's configured tire friction strength. Increase for more road grip; decrease for easier sliding. Surface and individual driving systems can further modify the available grip. | `1.65`; Range: 0.2f to 3 |
| `mass` | `float` | Chassis Rigidbody mass in kilograms. Increase for a heavier vehicle with more inertia and greater suspension load; spring strength may need adjustment to maintain ride height. | `1350`; Minimum: 1 |
| `motorTorque` | `float` | Direct-drive motor torque budget in N·m before splitting it among driven wheels. Increase for stronger direct-drive acceleration; geared engines also have their own engine torque tuning. | `5000`; Minimum: 0 |
| `steeringAngle` | `float` | Maximum requested road-wheel steering angle in degrees before speed, grip and steering-geometry limits. Increase for tighter low-speed turns. | `32`; Range: 1 to 60 |
| `steeringSpeed` | `float` | Digital and automatic direct-mode steering actuator speed in road-wheel degrees per second, including return to centre. Explicit analog steering follows its input directly. | `100`; Minimum: 1 |
| `steeringWheelRotationAtFullLock` | `float` | Steering wheel degrees from centre to either lock (540 means 1080 degrees lock-to-lock). | `135`; Minimum: 1 |
| `suspensionTravel` | `float` | Wheel suspension travel in metres copied during configuration. More travel lets wheels extend/compress farther and changes their reachable height; align collider mounts for that travel instead of zeroing it to position meshes. | `0.1764706`; Minimum: 0.05f |
| `topSpeedKph` | `float` | Forward road-speed target/limit stored in km/h and displayed in the selected unit. The active driving system uses it to reduce propulsion near top speed; it is not a hard teleport-style velocity clamp. | `300`; Speed field; stored in km/h, displayed in the selected speed unit |

## VehicleModule

Exposes lifecycle notifications around registered module work.

**Source:** `Runtime/Core/VehicleModule.cs`. Abstract base; settings are inherited by derived components.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `localExecutionOrder` | `int` | Relative step order when Override Execution Order is on. Smaller numbers run earlier within the same category/phase; required dependencies still take priority. | `0` |
| `overrideExecutionOrder` | `bool` | Uses Local Execution Order instead of the module's normal order within its category and dependency phase. Enable only when you need a custom order between compatible modules. | `false` |
