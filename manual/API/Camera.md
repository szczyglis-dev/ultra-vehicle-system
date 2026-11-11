# Camera integration API

See [Cameras](../Cameras.md) for authoring and runtime handover. Camera submodules inherit the standard [module API](Modules.md).

## Types

- [CameraModule](Camera.md#cameramodule)
- [Cameras](Camera.md#cameras)
- [Cameras.ViewMode](Camera.md#camerasviewmode)
- [InteriorCamera](Camera.md#interiorcamera)
- [OrbitCamera](Camera.md#orbitcamera)

## CameraModule

**Runtime/World/Camera/CameraModule.cs**

Base class for a Cameras submodule. Cameras renders its selected enabled submodule once per frame.

**Inherits / implements:** `WorldModule`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool active` | Active checkbox, initially false. The selected view must be explicitly activated after assignment before it can control a camera. |
| `public Transform anchor` | Position and rotation reference assigned in the Inspector. Null uses this component's transform; no object-name lookup. |
| `public virtual Transform Anchor { get; }` | Resolved anchor, falling back to this transform. |
| `public virtual bool IsActive { get; }` | This submodule's activation flag combined with its component enabled state. The owning core must also select it and hold an assigned camera to render it. |
| `public bool requirePointerLock` | Requires a locked cursor for mouse look. Scroll zoom remains available while focused. The game owns cursor locking. |
| `public float sensitivity` | Degrees of look rotation per mouse-delta unit. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public abstract void RenderCamera(Camera view, Vector2 lookDelta, float scroll, float deltaTime)` | Places the supplied camera using mouse delta, normalized scroll input and elapsed seconds. Called by Cameras; override it to implement a custom camera module. | — |
| `public abstract void ResetView()` | Resets look to its authored starting orientation. Cameras also places the attached camera immediately when controls and the selected submodule are enabled. | — |
| `public virtual void SetActive(bool value)` | Sets the activation flag and synchronizes the owning Cameras core immediately. Deactivation stops placement and restores the lens. | — |
| `public virtual void SetAnchor(Transform value)` | Assigns the explicit anchor. Use Cameras.ResetView to restart the view from its authored angles. | — |

## Cameras

**Runtime/World/Camera/Cameras.cs**

Optional vehicle camera owner. It moves an explicitly assigned camera only while the selected submodule is Active. It releases ownership when inactive, detached or disabled.

**Inherits / implements:** `WorldModule`.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<Camera> CameraChanged` | After Attach changes the assigned camera or Detach releases it; payload is the new camera or null. Inspector field edits do not raise this API event. |
| `public event System.Action<ViewMode> ModeChanged` | After SetView or Attach changes the view; payload is the new mode. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual CameraModule ActiveModule { get; }` | Submodule selected by mode; Custom uses customModule only if it belongs to this GameObject. |
| `public virtual System.Func<Vector2, bool> CanReadPointer { get; set; }` | Optional screen-position filter. Return false to suppress mouse look and zoom over UI. |
| `public CameraModule customModule` | Co-located custom submodule used when mode is Custom. Assign a subclass of CameraModule, such as the Demo free-camera examples. |
| `public bool enableControls` | Enables input processing. Use SetControlsEnabled(false) to clear pending controls immediately. |
| `public virtual InteriorCamera Interior { get; }` | Co-located interior submodule. |
| `public virtual bool IsActive { get; }` | True when the core owns its assigned camera and its selected view, component and controls are all active. |
| `public virtual bool IsAttached { get; }` | True when the core component is enabled and has an assigned camera, including inactive assignments. Use IsActive for actual control. |
| `public ViewMode mode` | Selected Orbit, Interior or Custom view. |
| `public virtual OrbitCamera Orbit { get; }` | Co-located orbit submodule. |
| `public bool readMouseInput` | Allows mouse sampling; disable it when driving look/zoom through the API. |
| `public override bool SupportsDirectControl { get; }` | Opts into direct-mode stepping; keeps camera control available. |
| `public override bool SupportsReleasedForces { get; }` | Keeps passive maintenance/observation active during release; Drive and Engine suppress force output, and TireCollision keeps native solid proxies without supplemental tread forces. |
| `public Camera viewCamera` | Explicit camera to control. Null leaves the component idle; no Camera.main lookup or camera creation. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void Attach(Camera value, CameraModule module, bool snap = true)` | Assigns a camera and selects a co-located built-in or custom submodule without changing its Active flag. snap resets its view. An unrelated or null module throws ArgumentException before attachment changes. | — |
| `public virtual void Attach(Camera value, ViewMode view = ViewMode.Orbit, bool snap = true)` | Assigns a camera and selects a view without activating it. Inactive assignments do not take camera ownership. Activating an assigned view deactivates the previous owner's selected view, preserving that owner's assignment. snap resets look; a disabled core stores the assignment. | — |
| `public virtual Camera Detach()` | Releases the camera, restores its original field of view and near clip, clears the assignment and returns the former camera. It does not destroy or disable the camera. | — |
| `public virtual void ResetView()` | Resets look to its authored starting orientation. Cameras also places the attached camera immediately when controls and the selected submodule are enabled. | — |
| `public virtual void SetActive(bool value)` | Activates/deactivates the currently selected submodule through its SetActive method. | — |
| `public virtual void SetControlsEnabled(bool value)` | Pauses or resumes camera placement and mouse input. Restores the original lens while paused. | — |
| `public override void SetEnabled(bool value)` | Enables/disables the core, releasing camera ownership and restoring its lens while disabled. Keeps the assignment for re-enabling. | — |
| `public virtual void SetModule(CameraModule module, bool snap = true)` | Selects a co-located module. Orbit/Interior map to their built-in modes; other subclasses select Custom. Invalid/null references throw ArgumentException. | — |
| `public virtual void SetView(ViewMode value, bool snap = true)` | Selects Orbit, Interior or Custom without activating a view. Optionally resets look; invalid enum values throw ArgumentOutOfRangeException. | — |

## Cameras.ViewMode

**Runtime/World/Camera/Cameras.cs**

Selects the vehicle view controlled by Cameras.

Values: `Orbit`, `Interior`, `Custom`.

## InteriorCamera

**Runtime/World/Camera/InteriorCamera.cs**

Exact cabin-anchor follow with bounded mouse look and configurable camera lens.

**Inherits / implements:** `CameraModule`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float fieldOfView` | Vertical field of view in degrees while interior is active. The core restores the previous lens on release. |
| `public float nearClipPlane` | Near clipping distance in metres while the interior view is active. Default: `0.04`. |
| `public Vector2 pitchLimits` | Minimum and maximum pitch in degrees. |
| `public Vector3 positionOffset` | Local position offset from the cabin anchor. |
| `public Vector3 rotationOffset` | Euler rotation offset in degrees relative to the cabin anchor. |
| `public Vector2 yawLimits` | Minimum and maximum cabin yaw in degrees. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderCamera(Camera view, Vector2 lookDelta, float scroll, float deltaTime)` | Places the supplied camera using mouse delta, normalized scroll input and elapsed seconds. Called by Cameras; override it to implement a custom camera module. | — |
| `public override void ResetView()` | Resets look to its authored starting orientation. Cameras also places the attached camera immediately when controls and the selected submodule are enabled. | — |
| `public virtual void SetLook(float yawDegrees, float pitchDegrees)` | Sets yaw and pitch in degrees, clamped to the configured pitch/yaw limits. Orbit yaw is a world heading; interior yaw is an anchor-relative offset. Non-finite inputs are ignored. | — |

## OrbitCamera

**Runtime/World/Camera/OrbitCamera.cs**

Mouse orbit, scroll zoom, smoothed framing and obstruction avoidance around an explicit anchor.

**Inherits / implements:** `CameraModule`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool avoidObstacles` | Master obstruction switch; off by default, with no casts while disabled. |
| `public bool ignorePassengers` | Exclude characters from ordinary-obstacle avoidance; the followed vehicle's passengers are always excluded. Initially true. |
| `public bool ignoreDynamicObstacles` | Exclude DynamicObstacle props from ordinary-obstacle avoidance. Initially true. |
| `public bool gravityAlignedFocus` | Keep the vehicle-local focus offset aligned to gravity during a rollover. |
| `public bool avoidGround` | When the master is enabled, include Terrain and OrbitCameraGround geometry. Initially true. |
| `public bool avoidOtherObstacles` | Include ordinary scenery/props; initially false. |
| `public bool avoidOtherVehicles` | Include other vehicles and their loose parts; initially false. |
| `public float distance` | Requested orbit radius in metres. |
| `public virtual Vector3 Focus { get; }` | Current world-space orbit focus. |
| `public Vector3 focusOffset` | Local offset from the anchor. Use zero when the anchor is already at the intended orbit focus. |
| `public float followResponse` | Exponential rotation/radius smoothing response per second. |
| `public float initialPitch` | Additional starting pitch in degrees relative to the anchor pitch. |
| `public float initialYaw` | Additional starting yaw in degrees relative to the anchor heading. |
| `public float maximumDistance` | Largest zoom radius in metres. |
| `public float minimumDistance` | Smallest zoom radius in metres. |
| `public LayerMask obstructionMask` | Layers checked for camera obstructions; triggers are ignored. |
| `public float obstructionRadius` | Radius in metres used for the orbit sphere cast. |
| `public Vector2 pitchLimits` | Minimum and maximum pitch in degrees. |
| `public float zoomSensitivity` | Metres of radius change per normalized scroll unit. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderCamera(Camera view, Vector2 lookDelta, float scroll, float deltaTime)` | Places the supplied camera using mouse delta, normalized scroll input and elapsed seconds. Called by Cameras; override it to implement a custom camera module. | — |
| `public override void ResetView()` | Resets look to its authored starting orientation. Cameras also places the attached camera immediately when controls and the selected submodule are enabled. | — |
| `public virtual void SetLook(float yawDegrees, float pitchDegrees)` | Sets yaw and pitch in degrees, clamped to the configured pitch/yaw limits. Orbit yaw is a world heading; interior yaw is an anchor-relative offset. Non-finite inputs are ignored. | — |
| `public virtual void Zoom(float amount)` | Changes desired radius using zoomSensitivity and distance limits; positive input zooms in. Non-finite input is ignored. | — |
| `public void SetObstacleAvoidance(bool value)` | Toggle the master obstruction switch without changing category choices. | — | — |

Orbit obstruction avoidance is off by default. When enabled, Avoid Ground selects Terrain and Orbit Camera Ground geometry; Avoid Other Obstacles and Avoid Other Vehicles opt into additional categories. The owning vehicle and its own passengers/detached parts stay excluded. Obstruction Mask restricts all selected categories.
