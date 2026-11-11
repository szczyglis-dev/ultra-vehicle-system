# Mirrors, displays and fuel

This page configures the interior systems that perform rendering or resource/assist actions. Build their cockpit switches and needles in [Interior controls](InteriorControls.md), then bind those controls to the working systems here. Passenger support and gestures have their own [seat](Seats.md) and [interaction](ControlInteractions.md) guides.

Add vehicle modules through **VehicleController > Modules > Add module...**, or discover/register modules added directly to the hierarchy. Configure a system and test its public action before adding the switch that operates it. For shared hinge/carrier conventions, use [moving geometry](InteriorControls.md#prepare-moving-geometry).

## Inspector quick start

| Equipment | Where to edit it on the vehicle root | Model objects/references to prepare |
| --- | --- | --- |
| Rear mirror | Modules > Interior > Rear Mirrors | A dedicated rear-view Camera and separate mirror Renderer for each Mirrors entry; an observer camera |
| Dashboard screen | Modules > Interior > Car Hud or Aircraft Hud | A separate screen Renderer with suitable UVs/material; Vehicle reference |
| Fuel supply | Modules > Engine > Fuel Tank | Engine context and capacity/initial fuel; a gauge is configured separately |
| Combined TCS/stability switch | Modules > Drive > Driving Assists | Working Traction Control and Steering modules |

For a first display, select the screen child, add **Car Hud** through Add Component, and assign the root's **Vehicle Controller** to **Vehicle**. Drag the screen's Renderer into **Cockpit Surface**, set **Texture Property** for its shader, and leave **Custom Texture** empty for generated output. Discover the child module from the vehicle's Modules tab, apply configuration and save. Enter Play Mode and change speed/RPM. If the whole dashboard changes texture, separate the screen Renderer before adjusting the HUD.

For a mirror, follow the camera/surface registration steps below rather than reusing the player's view camera. For Fuel Tank, set capacity, initial fuel and consumption on the Engine-category module, then test its gauge/empty behavior independently of cockpit animation.

## RearMirrors

### Camera, screen and observer

1. Add `RearMirrors` to the vehicle.
2. Create a separate visible mirror surface with an appropriate material and UVs.
3. Create a dedicated Camera for that mirror, parent it to the vehicle and aim it at the intended rear view. Do not reuse the player's active view camera.
4. Add an entry to **Mirrors** and assign its **Surface** Renderer and **Camera**.
5. Assign **Observer** to the camera representing the viewer, or leave it empty to use Camera.main.
6. Set the entry's field of view, near/far clip distances, culling mask, texture resolution/aspect and refresh rate.
7. Exclude mirror surfaces from the mirror camera's rendered layers to prevent recursive mirror views, and test from the actual driving camera.

The mirror module owns its dedicated camera's automatic enabled state and target while bound. It submits explicit renders rather than letting every mirror join the normal camera stack. If a camera setting is repeatedly replaced, edit the mirror entry that owns it rather than editing that live camera value.

### Texture and material binding

Leave **Texture** empty to let the module allocate its own render texture using **Resolution** and **Aspect Ratio**. Assign a RenderTexture when the application owns its format/lifetime. The module must not be used as the owner that destroys a supplied shared texture.

**Texture Property** must be the property read by the mirror material's shader, commonly `_BaseMap` in URP or the appropriate property for your shader. **Flip Horizontally** changes the texture mapping for a mirror view; check text and left/right landmarks instead of assuming the Camera's orientation alone provides the desired reflection.

The module uses per-renderer property overrides. Keep each mirror surface independently addressable when different views need different textures. A custom shader must read the assigned property. After changing generated texture dimensions, disable/re-enable the module so its owned resources can be recreated; do not expect changing the numbers to resize an already allocated texture immediately.

### Eligibility and render cost

**Maximum View Distance** is measured from the observer to the surface. Frustum/layer checks skip mirrors outside the observer's eligible view, and **Maximum Renders Per Frame** bounds work across entries. **Refresh Rate** is each entry's requested cadence, subject to that shared budget. It is not the main camera frame rate.

Use a smaller texture and lower cadence for a small dashboard mirror. Raise the budget only after checking how many mirrors are visible simultaneously. Frustum eligibility is not occlusion testing; use an application visibility/quality policy to disable a mirror that is behind other geometry or unnecessary in a particular camera.

Use `SetMirrorsEnabled(bool)` for the collection and `SetMirrorEnabled(index, bool)` for an entry. Rebinding/removing entries and disabling the module restore owned camera/surface state. The built-in render pipeline uses explicit Camera rendering; SRP rendering depends on support for the module's render request. See [rendering/ownership contracts](Scripting/Interior.md#rearmirrors) for custom pipelines and quality-policy code.

## CarHud

### Put a display on the dashboard

1. Create a separate screen surface with UVs covering the intended panel.
2. Add `CarHud`, assign **Vehicle** and the screen's **Cockpit Surface** Renderer.
3. Set **Texture Property** to the texture property actually read by that surface's shader.
4. Leave **Custom Texture** empty to use the generated panel, and set **Speed Unit** for its displayed speed.
5. Choose **Refresh Rate** based on the screen's size and required smoothness, then test with changing speed, RPM and gear.

The generated panel presents speed, RPM, gear and fuel, with supported status indication. It does not require a UI canvas. Give the screen a separate Renderer/material arrangement so the texture override affects that screen rather than an entire dashboard atlas.

### Custom output and telemetry

Assign **Custom Texture** to show an application-provided texture; the component binds that texture but does not draw your custom content into it. A RenderTexture from a UI/camera or another application renderer can therefore supply the panel image.

`DisplayTexture` exposes the selected/generated texture. `Changed` reports cached telemetry updates, while Refresh Rate controls surface redraw/presentation. Reducing panel refresh does not slow physics. On disable/rebind, the component releases its subscription and restores the surface override it owned.

For a custom canvas/UI, subscribe to the HUD's Changed event or the vehicle's `AfterPhysicsStep`. Use the [telemetry snapshot](Scripting/Events.md#diagnostic-snapshot) for world motion, speed, RPM, fuel and wheel diagnostics; use a [needle/value source](InteriorControls.md#add-an-rpm-or-speed-needle) for a physical dial. Neither path needs a separate polling physics loop per label.

## AircraftHud

Configure Vehicle, Cockpit Surface, Texture Property and Refresh Rate using the same screen workflow above. `AircraftHud` provides its aircraft-oriented generated panel and telemetry/landing-gear observation rather than the CarHud road dashboard. It also accepts an application-provided Custom Texture.

Use separate screen objects when a vehicle has several independently rendered panels. Decide whether they should share one custom texture or render different information; adding multiple writers to the same Renderer/property does not compose the images automatically.

## FuelTank

### Resource configuration

Add `FuelTank` to the vehicle. Set **Capacity Litres**, initial fuel, **Idle Litres Per Hour** and **Full Load Litres Per Hour**. Consumption is resolved from running engine load/RPM; the rates are fuel volume per hour, not per frame or per kilometre.

**Consume Fuel** controls depletion. Disable it for unlimited range while retaining the gauge/refuelling API. **Stop Engine When Empty** independently controls the ignition rule: with it enabled, an empty tank stops the engine and blocks ignition even if consumption is disabled. Refuelling does not restart the engine automatically.

### Gameplay and gauges

Use `SetFuel`, `Refuel`, `Fill` or `Drain` through the resource API. Refuel/Drain return the amount actually added/removed after capacity/empty limits, so application inventory can charge the real transferred amount. Persist resource state in your own save system and restore it through the public action.

`FuelLitres`, `Fraction` and `LitresPerHour` support displays and gameplay. Fraction is 0–1; do not feed it into a litres-range gauge without converting the range. The complete [fuel needle example](Scripting/Interior.md#add-a-fuel-needle-source) and [instrument workflow](InteriorControls.md#fuel-temperature-pressure-and-other-values) own that visual setup. The [service-action example](Scripting/Interior.md#refuel-through-a-service-action) demonstrates application refuelling.

## DrivingAssists

Use `DrivingAssists` when one cabin/gameplay policy should switch traction control and steering stability together. Ensure the corresponding TractionControl and Steering modules are registered, then configure desired traction/stability behavior on the facade. It resolves these through the vehicle module lookup. While enabled, it owns the corresponding underlying settings; directly editing those values can be replaced by its next Apply/step.

Use `SetTractionControl`, `SetStabilityControl` or `SetAssistsEnabled` for runtime switches. Stability means the configured yaw/lateral steering assistance; it is not an automatic guarantee against every rollover or collision. Its API state is suitable for status lamps and UI. Configure a visual switch/indicator using the [control binding guidance](InteriorControls.md#other-binary-actions), with application binding where bidirectional synchronization is needed.

If your application wants full direct control of the underlying modules, omit/disable the facade and configure them through [Traction control](TractionControl.md) and vehicle steering tuning. Do not leave two active policies continuously writing opposite values.

## Diagnose an interior system

| Symptom | Inspect first |
| --- | --- |
| Mirror shows black/old image | Eligible observer view, camera/mask, render support and refresh budget |
| Mirror camera edits do not persist | Settings belong to its mirror entry |
| Mirror recursively shows itself | Mirror surfaces included in the mirror camera's culling mask |
| Wiper helper never moves | Entry registered in Wipers, enabled module/helper and nonzero speed |
| Stop does not freeze the blade immediately | Stop finishes its cycle; zero speed pauses and Park parks immediately |
| Rear blade starts with collective control | Collective action intentionally replaced that running request |
| Digital panel changes the whole dashboard | Renderer/material/texture-property scope and screen UVs |
| Custom panel is static | Custom Texture binding does not render application content |
| Full tank UI disagrees with the engine | Correct tank/vehicle binding, initial state and empty-tank policy |
| Assist setting reverts | Enabled DrivingAssists facade owns that underlying setting |

For component fields and API operations, continue with [Interior API](API/Interior.md) and the [Inspector reference](InspectorReference.md).

For exterior blade setup, speed and audio, see [Wipers](Wipers.md).
