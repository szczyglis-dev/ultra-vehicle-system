# Vehicle state and configuration API

This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [PackageVersion](Core.md#packageversion)
- [Settings](Core.md#settings)
- [VehicleController](Core.md#vehiclecontroller)

## PackageVersion

**Runtime/Core/PackageVersion.cs**

Release version shared by runtime displays and editor UI. Distribution verification keeps it aligned with package.json.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public const string Current` | Current package release string. |

## Settings

**Runtime/Core/Settings.cs**

Serializable shared configuration read by vehicle mechanics; apply configuration when changing persistent native setup.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float brakeTorque` | Full service-brake torque in newton-metres before each wheel's brake multiplier. Full service-brake torque before per-wheel multipliers, in N·m. |
| `public Vector3 centerOfMass` | Chassis-local centre of mass in metres, independent of the visual body model's pivot. |
| `public float grip` | Overall tire grip multiplier applied by the vehicle wheel-friction configuration. Initial value: `1.65f`. |
| `public float mass` | Physical mass in kilograms. Increasing it increases the inertia and the load carried by connected supports. Initial value: `1350f`. |
| `public float motorTorque` | Direct-drive wheel torque budget before per-wheel distribution, in N·m. |
| `public float steeringAngle` | Maximum road-wheel steering angle in degrees before optional speed/grip geometry limits. |
| `public float steeringSpeed` | Digital and automatic direct-mode steering actuator speed in road-wheel degrees per second, including return to centre. Explicit analog steering follows its input directly. |
| `public float steeringWheelRotationAtFullLock` | Steering wheel degrees from centre to either lock (540 means 1080 degrees lock-to-lock). |
| `public float suspensionTravel` | Available wheel suspension travel in metres. Align the collider mount for this travel rather than setting travel to zero to align a mesh. Initial value: `0.1764706f`. |
| `public float topSpeedKph` | Top speed in km/h (stored value); Speed fields display the selected speed unit. Initial value: `300f`. |
| `public float TopSpeedMph { get; set; }` | Read/write mph view of topSpeedKph; assigning converts once into canonical km/h storage. |

## VehicleController

**Runtime/Core/VehicleController.cs**

Owns one vehicle: its root body, input sampling, wheel configuration, registry and fixed-step pipeline.

**Inherits / implements:** `MonoBehaviour`.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<Telemetry> AfterPhysicsStep` | After the package module pipeline. Payload: Telemetry snapshot; this is not a separate native Physics.Simulate completion. |
| `public event Action<Collision> Collided` | During the live Unity collision callback. Payload: Collision; copy required data before deferring work. |
| `public event Action<Collision> ContactPersisted` | Live sustained native contact; copy values before retaining or deferring them. |
| `public event Action<Command> CommandSampled` | After the selected provider is sampled. Payload: the Command used for that vehicle tick. |
| `public event Action ConfigurationChanged` | After validated wheel/module configuration is applied. No payload. |
| `public event Action<DriveProfile> DriveProfileChanged` | After an immediate profile change is configured successfully. Payload: the selected `DriveProfile`. |
| `public event Action<Impact> Impacted` | After collision information has been copied. Payload: Impact snapshot safe to retain beyond the callback. |
| `public event Action<MonoBehaviour> InputSourceChanged` | After assigning input ownership. Payload: selected `MonoBehaviour`, or `null` for released input. |
| `public event Action<VehicleModule> ModuleRegistered` | After registration/configuration. Payload: the registered Module. |
| `public event Action<VehicleModule> ModuleUnregistered` | After removal from future pipeline membership. Payload: removed Module; independent callbacks may still need disabling. |
| `public event Action Repaired` | After the in-place RepairAll pass and actuator cleanup. Not emitted by Teleport alone. |
| `public event Action<Pose> Teleported` | After world pose and occupants have been synchronized. Payload: the resulting Pose. |
| `public event Action<Wheel, bool> WheelAttachmentChanged` | Forwards a child Wheel attachment change after its per-wheel notification; payload is Wheel and attached flag. |
| `public event Action<int, bool> WheelAvailabilityChanged` | After a configured wheel's availability changes. Payload: wheel index and availability bool. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual Vector3 AngularVelocity { get; }` | Current world angular velocity in rad/s, measured from pose rotation in direct mode or read from Rigidbody otherwise. |
| `public Transform body` | Visual body `Transform`; this is not the root `Rigidbody`. |
| `public virtual Rigidbody Body { get; protected set; }` | Initialized root `Rigidbody` used for vehicle force/velocity operations; lowercase body is a separate visual reference. |
| `public virtual IReadOnlyList<CategoryCore> CategoryCores { get; }` | Read-only/resolved category cores for `VehicleController`. |
| `public ModuleCategory[] categoryExecutionOrder` | Categories omitted here are appended once, so custom serialized layouts cannot drop a category. |
| `public virtual Command Command { get; protected set; }` | Command sampled for the current fixed tick; it describes intent rather than every resolved actuator output. |
| `public virtual float DirectionSelectionSpeedKph { get; }` | Ignore suspension bounce along the chassis up axis when selecting direction. Preserve both longitudinal and lateral road motion, including on a slope. |
| `public virtual float DirectionSelectionSpeedMph { get; }` | Planar direction-selection speed in mph, derived from DirectionSelectionSpeedKph. |
| `public virtual float DriveDemand { get; internal set; }` | Resolved propulsion demand after input/mechanical interpretation. |
| `public virtual float DriveDirectionSign { get; }` | Engine propulsion polarity, or +1 when no engine is configured. |
| `public DriveProfile driveProfile` | Movement strategy and its embedded configuration. Choose the profile matching the vehicle family. Initial value: `new WheeledProfile()`. |
| `public virtual bool ForcesReleased { get; }` | Effective manual or ignition-policy force release. Native physics and observation remain active. |
| `public virtual float ForwardSpeed { get; }` | Signed root velocity projected onto the configured propulsion direction, in m/s. |
| `public HandleController handles { get; }` | Per-vehicle registry, limb scheduler and request entry point. Initialized during vehicle Awake. |
| `public virtual Passengers passengers { get; }` | First registered passenger core, including disabled cores; null if absent. Resolves through TryGetModule on each access, with no component creation or stale cache. Use GetModules for deliberate multi-core setups. |
| `public virtual Body parts { get; }` | Registered body-part controller, including a disabled module; null if absent. Resolves through TryGetModule on each access without creating components or caching stale references. Use Open/Close/Toggle/GetPart for ID-based operations, parts for the configured VehicleBodyPart array and damageParts for damage boundaries. |
| `public MonoBehaviour inputSource` | Selected `MonoBehaviour` implementing IVehicleInput; use `SetInputSource` for an ownership change. |
| `public virtual bool IsDirectControl { get; }` | Whether direct-pose ownership is currently active; source flag changes are applied at the next fixed tick. |
| `public VehicleModule[] modules` | Registered mechanics components configured and stepped by the controller. Discover modules after adding or removing systems. Initial value: `Array.Empty<VehicleModule>()`. |
| `public virtual IReadOnlyList<VehicleModule> Modules { get; }` | Read-only/resolved modules for `VehicleController`. |
| `public VehicleSensors sensors { get; }` | Stable per-vehicle read-only [physics sensor readings](PhysicsSensors.md#vehiclesensors), updated with telemetry. |
| `public virtual float ServiceBrake { get; internal set; }` | Resolved service-brake demand consumed by downstream mechanics and pedal presentation. |
| `public Settings settings` | Shared vehicle mass, speed, torque, steering, grip and suspension tuning. Inspector: **Vehicle Controller > Setup > Configuration**. Initial value: `new Settings()`. |
| `public bool showGizmos` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `public virtual float SpeedKph { get; }` | Magnitude of root body velocity in km/h. |
| `public virtual float SpeedMph { get; }` | Unsigned total vehicle speed in mph, derived from SpeedKph. |
| `public virtual float SteeringAngle { get; internal set; }` | Resolved road-wheel steering angle in degrees. |
| `public virtual float SteeringNormalized { get; }` | Resolved road-wheel angle normalized against configured `steeringAngle`. |
| `public virtual float SteeringRatio { get; }` | Column-angle to road-wheel-angle conversion ratio. |
| `public virtual float SteeringWheelAngle { get; }` | Logical unwrapped steering-column degrees, before mesh-axis inversion. |
| `public virtual float SteeringWheelRotationAtFullLock { get; }` | Column travel in degrees per side at full road-wheel steering. |
| `public virtual Telemetry Telemetry { get; protected set; }` | Latest cached vehicle snapshot published after the module pipeline. |
| `public virtual Vector3 Velocity { get; }` | Current world velocity in m/s, measured from direct poses in direct mode or read from Rigidbody in physical mode. |
| `public virtual IReadOnlyList<Wheel> Wheels { get; }` | Controller-managed runtime wheel adapters in configured order. |
| `public Wheel[] wheels` | Runtime wheels data retained by `VehicleController`; it is not serialized authoring configuration. |
| `public WheelSetup[] wheelSetup` | Saved wheel definitions used as authoring input during configuration. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void AddAllAvailableModules(Func<GameObject, Type, VehicleModule> addComponent = null)` | Installs module types allowed by full-setup policy; optional creation callback supports editor-aware creation. | `addComponent` — Optional component creation callback, useful for editor Undo-aware creation. Default: `null`. |
| `public virtual T AddModule<T>() where T : VehicleModule` | Creates and registers an owned module of the requested concrete type. | **Returns:** Returned T; ownership remains as specified by the creating/lookup operation. |
| `public virtual void ApplyConfiguration()` | Runs vehicle configuration and reports invalid setup through the controller's error-reporting path; use `TryApplyConfiguration` to obtain the error directly. | No arguments; no returned value. |
| `public virtual void ConnectAvailableModules()` | Fills missing owned module/controller references while preserving existing explicit and external references. | No arguments; no returned value. |
| `public virtual void DiscoverModules()` | Rebuilds membership from owned descendants, including inactive objects, stopping at nested vehicle ownership. | No arguments; no returned value. |
| `public virtual CategoryCore GetCategoryCore(ModuleCategory category)` | Returns the controller-owned scheduling core for one module category. | `category` — Selected module category. **Returns:** Returned `CategoryCore`; ownership remains as specified by the creating/lookup operation. |
| `public virtual float GetDriveDemand(Command command)` | Resolves propulsion demand using the active movement strategy and sampled command. | `command` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual void GetModules<T>(List<T> results, bool activeOnly = false) where T : class` | Clears and fills a caller-owned list with matching registered providers in registration order. | `results` — Caller-owned list cleared and filled by lookup. `activeOnly` — `true` excludes inactive/disabled components; it does not check `SupportsProfile`. Default: `false`. |
| `public virtual Vector3 GetPointVelocity(Vector3 point)` | World velocity at a point, including chassis rotation; supports both physical and direct motion. | `point` — World-space point in metres. Returns velocity in m/s. |
| `public virtual float GetSpeed(SpeedUnit unit)` | Returns total vehicle speed in the selected unit. | — |
| `public virtual bool IsMoving(float linearSpeedThreshold = .05f, float angularSpeedThreshold = .02f)` | Reports total 3D translation or rotation above the supplied thresholds, including direct control. Does not require Rigidbody sleep. Non-finite velocity reports motion; an uninitialized vehicle with no motion provider reports stationary. | `linearSpeedThreshold` — m/s, default 0.05. `angularSpeedThreshold` — radians/s, default 0.02. Negative thresholds clamp to zero; non-finite thresholds use defaults. Equal-to-threshold motion is considered stationary. Use `!vehicle.IsMoving()` for the inverse. |
| `public virtual void PublishSteeringAngle(float degrees)` | Publishes a finite resolved road-wheel actuator angle from a custom steering mechanic. | `degrees` — Requested angle in degrees. |
| `public virtual void RefreshModuleOrder()` | Rebuilds module scheduling without reapplying vehicle/wheel configuration. | No arguments; no returned value. |
| `public virtual void RegisterModule(VehicleModule module, int index = -1)` | Registers/configures an existing owned module, optionally at a requested registration index. | `module` — Existing module component whose membership changes. `index` — Zero-based configured-entry index; use the owner's current list ordering. Default: `-1`. |
| `public virtual void ReleaseAllForces()` | Latch manual force release and clear pending control/landing/hold state without clearing momentum. | Remains released until RestoreAllForces, independently of ignition or ResetVehicle. |
| `public virtual void RepairAll()` | Repairs owned registered retained damage parts, body hinges and prepared meshes, clears wheel actuators, then emits Repaired. Does not teleport or reset chassis momentum, engine/fuel/weapon/application state. Works with future damage disabled. | — |
| `public virtual bool RepairPart(string id)` | Resolves a unique registered damage part across owned Damage components and fully repairs it. Returns false for blank/missing/ambiguous or failed restoration. | — |
| `public virtual void ResetVehicle(Vector3 position, Quaternion rotation)` | Clears Nitro/Burnout requests, engine and flight-input throttle, current command and actuators, then repairs, teleports and clears attached native wheel spin. Landing-gear reset preparations remain demo responsibilities. | — |
| `public virtual void ResolvePedals(float driveDemand, float serviceBrake)` | Publishes resolved propulsion and service-brake demand for downstream mechanics/presentation. | `driveDemand` — Resolved propulsion demand. `serviceBrake` — Resolved service-brake demand in 0–1. |
| `public virtual void RestoreAllForces()` | Clear manual release and restore mechanics, including the current automatic ignition-off interval. | Explicit restore overrides the current ignition-off interval until the next running/off cycle; does not teleport or reset velocity. |
| `public virtual float RoadWheelAngleFromSteeringWheel(float wheelAngle)` | Converts logical column degrees to road-wheel degrees using the configured steering ratio. | `wheelAngle` — Logical steering-column angle in degrees. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual void SetInputSource(MonoBehaviour source)` | Selects an IVehicleInput component; `null` releases vehicle input ownership. | `source` — Explicit provider being selected or bound. |
| `public virtual bool SetModuleEnabled<T>(bool value) where T : VehicleModule` | Finds an installed module of the requested type and changes its enabled state. | `value` — Requested bool state for this operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual void SetWheelEnabled(int index, bool available)` | Updates wheel-definition, adapter and native-contact availability together. | `index` — Zero-based configured-entry index; use the owner's current list ordering. `available` — Requested availability, distinct from mesh detachment. |
| `public virtual float SteeringInputFromWheelAngle(float wheelAngle)` | Converts logical column degrees to normalized steering input. | `wheelAngle` — Logical steering-column angle in degrees. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual float SteeringWheelAngleFromRoadWheel(float roadAngle)` | Converts road-wheel degrees to logical unwrapped column degrees. | `roadAngle` — Road-wheel steering angle in degrees. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual void Teleport(Vector3 position, Quaternion rotation)` | Resets vehicle world pose through the controller's mechanical and occupant reset contract. Preserves the supplied rotation and clears velocity on attached dynamic bodies, excluding released parts, unseated passengers and nested vehicles. | `position` — Requested point or switch detent; see its declared type and owning operation. `rotation` — Requested/output orientation in the declared frame. |
| `public virtual bool TryApplyConfiguration(out string error)` | Validates wheel ownership/geometry, builds adapters and configures modules, returning a reason on failure. | `error` — Output validation/refusal explanation; inspect when the operation returns `false`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TryGetModule<T>(out T result) where T : class` | Finds the first registered class/interface provider; `activeOnly` filters Unity active/enabled state, not profile compatibility. | `result` — Output matching provider; check the bool result before use. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TryGetModule<T>(out T result, bool activeOnly) where T : class` | Finds the first registered class/interface provider; `activeOnly` filters Unity active/enabled state, not profile compatibility. | `result` — Output matching provider; check the bool result before use. `activeOnly` — `true` excludes inactive/disabled components; it does not check `SupportsProfile`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool TrySetDriveProfile(DriveProfile profile, out string error)` | Validates/configures an immediate profile change with current settings and rejects incompatible/transitioning requests. | `profile` — Movement/surface configuration, according to its declared type. `error` — Output validation/refusal explanation; inspect when the operation returns `false`. **Returns:** `true` if admitted/applied; inspect the described completion boundary and any out values. |
| `public virtual bool UnregisterModule(VehicleModule module)` | Removes a module from future pipeline membership; independent callbacks/resources require their own disable/cleanup. | `module` — Existing module component whose membership changes. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
| `public virtual bool ValidateWheelSetup(out string error)` | Checks profile wheel requirements, native ownership, duplicates and finite minimum geometry/mass. | `error` — Output validation/refusal explanation; inspect when the operation returns `false`. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |

| Declaration | Usage |
| --- | --- |
| `public TelemetrySettings telemetry` | Optional capture groups at Setup > Telemetry, directly below Configuration. Wheel Details defaults off; other groups default on. Changes apply at the next physics publication without reconfiguration. |
