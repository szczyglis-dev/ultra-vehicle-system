# Cameras

`Cameras` is an optional World component for quickly viewing a vehicle. It supplies two built-in camera submodules: `OrbitCamera` for exterior orbit and `InteriorCamera` for the cabin. Vehicles created through Tools or Add Component receive this group automatically. It remains idle until you explicitly assign a `Camera` and activate the selected submodule; leave that field empty to use your own camera system.

## Set up an orbit view

1. Select the vehicle and open **Modules → World → Cameras** in its Inspector. You can also add **UltraVehicleSystem → World → Cameras → Cameras** through Tools or Add Component.
2. Create a child Transform where you want the orbit focus. Set its rotation to the desired starting view orientation.
3. Assign it to the Orbit Camera submodule's `anchor`. Set `focusOffset` to zero if the anchor is already at the focus. Without an anchor, the vehicle root and the local offset are used.
4. Assign a scene camera to the core's `viewCamera` and select **Orbit**, then check **Active** on the Orbit Camera submodule. Active starts unchecked. In Play Mode, mouse movement rotates the view and the wheel zooms.
5. Adjust `distance`, `minimumDistance`, `maximumDistance`, `sensitivity`, `zoomSensitivity`, `followResponse`, `initialYaw`, `initialPitch` and `pitchLimits`. Obstruction settings control how the camera retracts at scenery.

Each camera submodule has **Enable Look**, enabled by default. Turn it off to ignore pointer/look-delta rotation while retaining the current look angles. Following, scroll zoom and free-camera movement continue. Explicit `SetLook` calls remain available for scripted orientation. The camera core also suppresses pointer deltas passed to custom modules; custom input adapters should respect `enableLook` when reading their own controls.

`requirePointerLock` optionally limits mouse look to a locked cursor. Your game decides when to lock/unlock it. Scroll zoom works while focused. `readMouseInput` lets you disable automatic mouse sampling and drive the view through code. `CanReadPointer` can reserve pointer input for a UI overlay.

**Gravity Aligned Focus** keeps the orbit anchor height upright relative to gravity when the vehicle rolls or pitches. Enable it for vehicles that can tumble: the focus will not swing below the ground with the chassis. This changes the focus frame; obstruction casts still require **Avoid Obstacles**. The demo motorcycle uses this option.

## Set up the interior view

1. Create a Transform at the driver's eye position, usually below the animated body or cabin. Point its local Z axis in the viewing direction.
2. Assign it to the Interior Camera submodule's `anchor`. The module follows that Transform's position and rotation directly; object names are irrelevant.
3. Select **Interior** on `Cameras` and check **Active** on its Interior Camera submodule. Tune `positionOffset`, `rotationOffset`, `sensitivity`, `yawLimits` and `pitchLimits`.
4. Set the interior `fieldOfView` and `nearClipPlane` to suit the cabin. The default interior near clip is **0.04 m**. The previous camera lens is restored when switching to Orbit, disabling camera controls or releasing the camera.

### Keep the interior horizon level

Enable **Limit Roll** to compensate camera bank while retaining vehicle heading, pitch and mouse look. **Maximum Roll** defaults to 0.3°; zero requests a level horizon. **Roll Response Time** smooths compensation, so the limit describes the stabilized target rather than a hard instantaneous bound during abrupt motion. The compensation eases out near a vertical viewing direction where horizon roll becomes ambiguous.

**Stabilize Roll Position** also reduces the cabin eye point's sideways orbit around the chassis; **Position Roll Influence** selects how much authored mount roll remains (zero stays above the chassis, one follows the mount). Head-pinned views retain their actual head position. **Release Roll On Rollover**, enabled by default, fades stabilization between 75° and 105° of vehicle tilt and while following an ejected driver; ordinary collisions do not disable it. Motorcycle authoring enables roll and position stabilization automatically. Existing components retain their serialized settings.

### Pin the interior view to the driver's head

Enable **Pin To Head** on Interior Camera to parent the borrowed camera to the current humanoid driver's `headCameraAnchor`. Assign this field on **Humanoid Passenger** to an empty Transform below the head bone, slightly in front of the eyes, with local **+Z forward** and **+Y up**. The demo mannequin prefabs include **Head Camera Anchor**. The authored point replaces the cabin position/rotation offsets; mouse look and lens settings still apply.

**Follow Head Position** starts enabled; **Follow Head Rotation** starts disabled. Each channel can be switched independently. With position following disabled, the camera holds the world position captured at pinning. With rotation following disabled, it retains the point's initial +Z/+Y orientation relative to the cabin anchor: turning, pitching or rolling the vehicle still turns the view, while head-bone motion does not. Mouse look remains available. Rebinding a different camera or head point captures a new starting pose.

**Detach On Eject** is off by default: the camera remains attached to the ejected driver's head. Enable it to restore the camera's previous parent and return to the cabin view on ejection. Ordinary exits return to the cabin view. A replacement driver or FPP/TPP body supplies its own head point. Missing drivers or head points fall back to the normal cabin anchor.

Switching views, detaching the camera or disabling camera control restores the camera's previous parent as well as its lens. Pinning starts disabled, so existing cabin setups retain their behavior.

Both anchors are explicit Inspector references. Renaming an anchor does not affect the camera. Disabling the selected submodule pauses placement; it does not switch to another view automatically.

## Attach, switch and release in code

Call `Attach(camera, Cameras.ViewMode.Orbit)` or `Attach(camera, Cameras.ViewMode.Interior)` to assign a camera. `SetView(...)` switches an attached camera. `Detach()` releases and returns the camera without destroying or disabling it. Attachment alone does not start a view or take control from another vehicle. Call the selected module's `SetActive(true)`, or the core's `SetActive(true)`, to activate it. `SetActive(false)` stops placement and restores the original lens while retaining the camera assignment. An active flag is useful only when that submodule is selected by its core.

Activating a view assigned to a camera already controlled by another vehicle deactivates that previous view first. Both cores retain their assignments, so they can be activated again later. `IsAttached` reports the assignment; `Cameras.IsActive` reports actual control. Component enabled state and `enableControls` remain additional gates.

`SetControlsEnabled(false)` pauses camera placement and mouse controls; `SetControlsEnabled(true)` resumes them if the selected view is still Active. `SetEnabled(false)` disables the core and releases its active ownership while keeping the authored assignment for re-enabling. `ResetView()` resets look and immediately places an active attached camera. Submodules expose `SetAnchor`, `SetLook`, and `OrbitCamera.Zoom`; call `ResetView` after replacing an anchor if you want its starting rotation applied.

Assigning `viewCamera` directly in the Inspector is also supported and takes effect on the next camera update, provided the selected submodule is Active. API events `CameraChanged` and `ModeChanged` report calls through the attachment/view methods. No camera is found by tag, created or enabled automatically.

## Custom camera submodules

Derive from `CameraModule`, implement `ResetView()` and `RenderCamera(...)`, and add the component alongside `Cameras` on the vehicle. The core renders only its selected Active submodule. Your render implementation should also check `IsActive` so direct calls respect the checkbox. Use `anchor`/`Anchor` for your authored mount; do not look up objects by name. Your component can live in your own assembly or optional sample, without adding a new built-in package mode.

Select the component in the core's `customModule` field and choose **Custom**, or call `SetModule(customModule)`. To assign and select it together, call `Attach(camera, customModule)`, then `customModule.SetActive(true)`. Null modules and modules from a different GameObject are rejected. All co-located custom camera modules appear beneath Cameras in the vehicle Inspector.

**Example: `CustomFollowCamera.cs`**

<!-- example: CustomFollowCamera.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class CustomFollowCamera : CameraModule
    {
        public Vector3 offset = new Vector3(0, 2, -6);
        public override void ResetView() { }
        public override void RenderCamera(Camera view, Vector2 lookDelta, float scroll, float deltaTime)
        {
            if (!view || !IsActive) return;
            view.transform.SetPositionAndRotation(Anchor.TransformPoint(offset), Anchor.rotation);
        }
    }
}
```

**Example: `CustomCameraBinding.cs`**

<!-- example: CustomCameraBinding.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class CustomCameraBinding : MonoBehaviour
    {
        public Cameras cameras;
        public Camera view;
        public CameraModule customView;

        public void Show()
        {
            if (!cameras || !view || !customView || customView.gameObject != cameras.gameObject) return;
            cameras.Attach(view, customView);
            customView.SetActive(true);
        }

        public void Hide()
        {
            if (!cameras || cameras.viewCamera != view || cameras.ActiveModule != customView) return;
            cameras.SetActive(false);
            cameras.Detach();
        }
    }
}
```

## Demo integration

The Demo scene and vehicle prefabs have `Cameras` with explicitly assigned exterior and cabin anchors. `CameraRigDemo` assigns and explicitly activates the chosen Orbit, Interior, Cinematic, Free Look or Free Parent submodule. It deactivates and detaches the previous view when switching. Cinematic is also a Demo-only custom submodule, so every demo view uses the same Active gate. The rig handles selection and cursor capture without camera movement calculations.

`Scripts/Cameras/FreeCameraDemo.cs`, `FreeParentCameraDemo.cs`, their shared `FreeCameraMotionDemo.cs` and `CinematicCameraDemo.cs` show custom submodules supplied only by the Demo. They are not runtime package components. Free Look moves in world space; Free Parent stores its position and rotation relative to its anchor and follows the vehicle. Each vehicle's Free Parent component remembers its own local pose. Cinematic follows its anchor heading with smoothed framing, obstruction avoidance and wheel zoom. `Move(...)` also allows scripted navigation, and respects both Active and the core's control gates.

To reproduce the example, add the custom component on a vehicle with `Cameras`, assign its `anchor`, attach/select it with `Cameras.Attach(camera, customModule)` and call `customModule.SetActive(true)`. Tune `movementSpeed`, `movementResponse`, `boostMultiplier`, `sensitivity` and `requirePointerLock`. The example uses numpad navigation and Numpad + boost.

See [Camera API](API/Camera.md) for all configuration fields and methods.

## Optional orbit obstruction avoidance

**Orbit Camera > Obstacle Avoidance > Avoid Obstacles** is off by default, including in the demo vehicles. No obstruction casts run while it is off. Enable it to shorten the camera distance at the selected categories:

- **Avoid Ground** includes Terrain and colliders below an enabled **Orbit Camera Ground** marker. This category is selected initially, but only runs when Avoid Obstacles is enabled.
- **Avoid Other Obstacles** also includes ordinary scenery and unmarked props; off by default.
- **Avoid Other Vehicles** includes other vehicles and their detached parts; off by default.
- **Ignore Passengers** and **Ignore Dynamic Obstacles** keep characters and marked props excluded from the ordinary-obstacle category. Both exclusions are on by default.

The followed vehicle, its passengers and its own detached parts are always excluded. **Obstruction Mask** restricts all enabled categories by layer; triggers are ignored. `orbit.SetObstacleAvoidance(true)` toggles the master switch from code; category fields can also be changed at runtime.
