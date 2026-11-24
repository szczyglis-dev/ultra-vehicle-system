# Body, lights, wipers and aircraft equipment

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [AircraftControlMotion](#aircraftcontrolmotion) | 9 |
| [AircraftControlSurface](#aircraftcontrolsurface) | 3 |
| [AircraftControlSurfaces](#aircraftcontrolsurfaces) | 5 |
| [Body](#body) | 2 |
| [CustomLightGroup](#customlightgroup) | 4 |
| [DamagePart](#damagepart) | 27 |
| [ExteriorModule](#exteriormodule) | 0 |
| [HoverVisuals](#hovervisuals) | 1 |
| [HoverVisuals.TiltMount](#hovervisualstiltmount) | 2 |
| [LandingGear](#landinggear) | 6 |
| [LandingGearPart](#landinggearpart) | 4 |
| [LandingGearSuspension](#landinggearsuspension) | 1 |
| [LandingGearSuspensionPart](#landinggearsuspensionpart) | 11 |
| [LightChannel](#lightchannel) | 8 |
| [LightLensBinding](#lightlensbinding) | 4 |
| [Lights](#lights) | 17 |
| [MovingPart](#movingpart) | 21 |
| [PartClipAnimation](#partclipanimation) | 4 |
| [PartMotionAudio](#partmotionaudio) | 9 |
| [PartMotionEvents](#partmotionevents) | 4 |
| [PartMotionPlayback](#partmotionplayback) | 3 |
| [PartMotionSignals](#partmotionsignals) | 9 |
| [PedalDrive](#pedaldrive) | 11 |
| [Propulsion](#propulsion) | 4 |
| [Propulsion.Propeller](#propulsionpropeller) | 16 |
| [SteeringPart](#steeringpart) | 13 |
| [TrackPathBuilder](#trackpathbuilder) | 10 |
| [TrackVisuals](#trackvisuals) | 3 |
| [TrackVisuals.Belt](#trackvisualsbelt) | 4 |
| [TrackVisuals.Roller](#trackvisualsroller) | 5 |
| [VehicleBodyPart](#vehiclebodypart) | 30 |
| [VehicleLampGlow](#vehiclelampglow) | 4 |
| [WheelPart](#wheelpart) | 4 |
| [Wiper](#wiper) | 13 |
| [WiperBlade](#wiperblade) | 5 |
| [Wipers](#wipers) | 3 |
| [WiperSwitchBinding](#wiperswitchbinding) | 3 |

## AircraftControlMotion

Configuration/implementation type for aircraft control motion within cockpit instruments and bindings.

**Source:** `Runtime/Exterior/Aircraft/AircraftControlMotion.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Independent hinge and local axis frame outside Moving Part. Preserves the authored neutral offset; translation follows its normalized local axis in metres. | `None / unassigned` |
| `localAxis` | `Vector3` | Rotation or slide axis in Anchor's coordinates. For Rotation it is the hinge direction; for Translation it is the line the control moves along. | `Vector3.right` |
| `maximum` | `float` | Upper deflection angle in degrees mapped to the selected aircraft control channel. | `20` |
| `minimum` | `float` | Lower deflection angle in degrees mapped to the selected aircraft control channel. | `-20` |
| `mode` | `AircraftControlMotionMode` | Rotation turns the part around the configured axis; Translation slides it along that axis. Motion endpoints are degrees for rotation and metres for translation. Options: `Rotation`, `Translation`, `Animation`, `Custom`. | `Rotation` |
| `movingPart` | `Transform` | Control mesh moved relative to Anchor. Its pose is set by the current mapped control value; the anchor must remain independent of it. | `None / unassigned` |
| `playback` | `PartMotionPlayback` ([fields](Exterior.md#partmotionplayback)) | Animation/custom binding and lifecycle callbacks for this moving part. | `new PartMotionPlayback()` |
| `reverse` | `bool` | Mirror motion around the neutral pose without changing input or travel limits. | `false` |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |

## AircraftControlSurface

Configuration/implementation type for aircraft control surface within flight and landing gear.

**Source:** `Runtime/Exterior/Aircraft/AircraftControlSurface.cs`. Component / asset.

**Inherited settings:** [AircraftControlMotion](Exterior.md#aircraftcontrolmotion). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `customMix` | `Vector3` | Pitch, roll and yaw mix for Custom; enables new airframe layouts without new controller code. | `Zero-initialized Vector3` |
| `invert` | `bool` | Reverses the sign of the assigned control input before applying control-surface motion. | `false` |
| `type` | `AircraftSurfaceType` | Chooses which flight command moves this surface. Rudder follows yaw, ailerons follow opposite roll directions, elevators follow pitch, and flap/airbrake follow their deployment commands. Custom uses the configured input mapping. Options: `Rudder`, `LeftAileron`, `RightAileron`, `Elevator`, `LeftElevator`, `RightElevator`, `Flap`, `Airbrake`, `Custom`. | `Rudder` |

## AircraftControlSurfaces

Presents the configured control-surface motion.

**Source:** `Runtime/Exterior/Aircraft/AircraftControlSurfaces.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `airbrake` | `float` | Requested airbrake deployment amount. | `0`; Range: 0 to 1 |
| `externalControl` | `bool` | Take flap/airbrake requests from your integration rather than the component default input path. | `false` |
| `flaps` | `float` | Requested flap deployment amount, independent of pitch/roll/yaw input. | `0`; Range: 0 to 1 |
| `response` | `float` | How quickly the visible control surfaces follow flight commands. Increase for immediate-looking aileron/rudder movement; decrease for slower actuator motion. | `5`; Minimum: 0 |
| `surfaces` | `AircraftControlSurface[]` ([fields](Exterior.md#aircraftcontrolsurface)) | Visible rudders, ailerons, elevators, flaps and airbrakes updated from flight commands. Add a separate entry for each independently moving mesh. | `Empty list` |

## Body

Finds and operates authored `VehicleBodyPart` entries.

**Source:** `Runtime/Exterior/Parts/Body.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `damageParts` | `DamagePart[]` ([fields](Exterior.md#damagepart)) | Additional damage boundaries, including WheelPart. Damage merges these with its own Parts registry. | `Empty list` |
| `parts` | `VehicleBodyPart[]` ([fields](Exterior.md#vehiclebodypart)) | Doors, hood, trunk and other BodyPart components managed by this body module. Register parts here so body commands can find and operate them. | `Empty list` |

## CustomLightGroup

An independently requested/blinking custom lighting group. Inherits all physical light and emission parameters and `LitChanged` from [LightChannel](../API/Lights.md#lightchannel).

**Source:** `Runtime/Exterior/Lights/CustomLightGroup.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [LightChannel](Exterior.md#lightchannel). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `blinking` | `bool` | Blink this group while it is requested on. | `false` |
| `blinkInterval` | `float` | Seconds between blink state changes for this group. | `.45`; Minimum: .05f |
| `id` | `string` | Unique, case-sensitive ID within this Lights component. | `None / unassigned` |
| `on` | `bool` | Requested enabled state of this custom lighting group. | `false` |

## DamagePart

### State and configuration

**Source:** `Runtime/Exterior/Parts/DamagePart.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `damageEnabled` | `bool` | Allow routed and direct damage accumulation. Explicit Detach/RepairFully remain available. | `true` |
| `debrisAngularDamping` | `float` | Angular drag per second after release. Reduces prolonged spinning of loose panels without changing their inherited release velocity. | `.5`; Minimum: 0 |
| `debrisColliderMinimumThickness` | `float` | Minimum world-space thickness in metres for an automatically generated debris collider. | `.03`; Minimum: .005f |
| `debrisContactAngularChange` | `float` | Additional angular speed allowance in degrees/s for moving-object contact impulses and the combined post-solver spin budget. | `180`; Minimum: 1 |
| `debrisContactSpeedChange` | `float` | Additional linear speed allowance in m/s for moving-object contacts and the combined post-solver contact budget. Stationary ground retains full support and stopping forces. | `4`; Minimum: .1f |
| `debrisDepenetrationSpeed` | `float` | Maximum speed in m/s used to separate released debris from overlapping colliders. Lower values soften recovery when a car traps a thin panel; this does not clamp ordinary impact velocity. | `2`; Minimum: 0 |
| `debrisGroundPenetrationTolerance` | `float` | Ground overlap in metres tolerated before correcting a crushed part. | `.01`; Minimum: 0 |
| `debrisGroundProjection` | `bool` | Correct deep solver penetration into stationary ground after a heavy vehicle crushes a thin part. Operates only at real ground contacts; free flight remains physical. | `true` |
| `debrisGroundProjectionLimit` | `float` | Maximum ground penetration correction in metres per contact callback. | `.3`; Minimum: .01f |
| `debrisMaximumAngularSpeed` | `float` | Native released-part angular speed limit in degrees/s with contact stabilization enabled. Detached Wheel Parts can raise this to preserve inherited tire RPM. | `720`; Minimum: 1 |
| `debrisSolverIterations` | `int` | Native position solver iterations on released debris. More iterations improve thin-panel support under a heavy vehicle. | `12`; Range: 1 to 64 |
| `debrisSurfaceSpeedMultiplier` | `float` | Multiplier of the impacting surface world speed used by the debris contact speed budget. Faster pre-solver debris motion is preserved; the contact speed-change allowance is added. | `1.25`; Minimum: 1 |
| `debrisVelocitySolverIterations` | `int` | Native velocity solver iterations on released debris. | `4`; Range: 1 to 32 |
| `deformableMeshes` | `MeshFilter[]` | Readable MeshFilter meshes deformed by impacts on this damage part; assign only meshes that should visibly dent. | `Empty list` |
| `deformationMultiplier` | `float` | Zero disables mesh dents. Does not affect detachment. | `1`; Minimum: 0 |
| `detachedVehicleColliders` | `Collider[]` | Chassis-owned solid colliders enabled when this part detaches. Author them disabled, outside every detachable group, and assign each to only one part. Full repair restores their captured enabled states. Empty disables this feature. | `Empty list` |
| `detachmentMultiplier` | `float` | Zero prevents collision detachment. | `1`; Minimum: 0 |
| `detachThreshold` | `float` | Accumulated damage required to detach this group. | `30`; Minimum: 1 |
| `excludeDebrisFromWheelSupport` | `bool` | Keep detached panels out of native wheel suspension support. Solid tire and chassis colliders still push the debris, without firing full wheel spring forces into a light panel. | `true` |
| `generateMissingDebrisCollider` | `bool` | Generate a simple box from this part's mesh bounds on release if its damage boundary has no solid collider. Prevents detached lamps/glass from falling through the world. Colliders are retained. | `true` |
| `mass` | `float` | Rigidbody mass in kilograms assigned to the part when released. Higher mass gives the detached piece more inertia; it does not directly set its damage threshold. | `15`; Minimum: .01f |
| `material` | `PartMaterial` | Material category reported with this part's damage. Damage effects and sounds can use it to distinguish metal, glass, plastic, rubber and mechanical hits. Options: `Metal`, `Glass`, `Plastic`, `Rubber`, `Mechanical`, `Custom`. | `PartMaterial.Metal` |
| `materialId` | `string` | Optional case-sensitive impact material key, e.g. carbon or wood. Matching custom profiles take priority over the enum response. | `None / unassigned` |
| `partId` | `string` | Stable identifier for scripts and damage reactions. | `None / unassigned` |
| `prewarmDebrisPhysics` | `bool` | Prepare the disabled debris contact helper and shared contact code during startup, reducing first-detachment allocation/JIT work. Does not create a Rigidbody or change attached collision geometry. | `true` |
| `releasedCollisionDelay` | `float` | Minimum seconds to ignore former vehicle collisions after release. Overlapping pairs wait until separated. | `.5`; Minimum: 0 |
| `stabilizeDebrisContacts` | `bool` | Limit solver contact impulses on released parts, preventing thin panels trapped under heavy vehicles from being explosively ejected. Does not clamp inherited release velocity. | `true` |

## ExteriorModule

Base integration with the vehicle module lifecycle.

**Source:** `Runtime/Exterior/Core/ExteriorModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [VehicleModule](Common.md#vehiclemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## HoverVisuals

Configuration/implementation type for hover visuals within flight and landing gear.

**Source:** `Runtime/Exterior/Aircraft/HoverVisuals.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `tiltMounts` | `TiltMount[]` ([fields](Exterior.md#hovervisualstiltmount)) | Optional hover engine mounts. Uses folded-wheel thrust, turn and strafe tilt without the wheel-fold rotation. | `Empty list` |

## HoverVisuals.TiltMount

Configuration/implementation type for tilt mount within flight and landing gear.

**Source:** `Runtime/Exterior/Aircraft/HoverVisuals.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `restRotation` | `Quaternion` | Original local rotation of this mount before hover tilt is added. It preserves the model's alignment as the mount transitions between movement poses. | `Quaternion.identity` |
| `transform` | `Transform` | Part rotated when changing between wheel-driving and hover poses. Assign the independent wheel/engine mount that should tilt with this transition. | `None / unassigned` |

## LandingGear

Owns deployment sequencing and physical gear-contact availability.

**Source:** `Runtime/Exterior/Aircraft/LandingGear.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `groundClearanceLock` | `float` | Downward probe length in metres from the vehicle centre of mass used to block unsafe retraction near the ground. A larger value keeps the gear locked down farther above the surface. | `.6`; Minimum: 0 |
| `groundMask` | `LayerMask` | Layers checked by the ground-clearance retraction lock. Include runways/terrain that should prevent folding the gear while too close to the ground. | `~0` |
| `initiallyDeployed` | `bool` | Starts the landing gear deployed when checked, or retracted when unchecked. | `true` |
| `parts` | `LandingGearPart[]` ([fields](Exterior.md#landinggearpart)) | Moving struts, doors and links involved in deploying or retracting the landing gear. Each part supplies its own motion and timing. | `Empty list` |
| `preventGroundRetraction` | `bool` | Prevent retraction while tires touch the ground or the hull is within Ground Clearance Lock. | `true` |
| `wheels` | `WheelCollider[]` | Native wheel colliders belonging to the retractable landing gear. Their availability follows gear deployment so retracted wheels do not keep supporting the aircraft. | `Empty list` |

## LandingGearPart

Maps deployment progress to a door/strut pose.

**Source:** `Runtime/Exterior/Aircraft/LandingGearPart.cs`. Component / asset.

**Inherited settings:** [AircraftControlMotion](Exterior.md#aircraftcontrolmotion). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `duration` | `float` | Seconds this part takes to move between extended and retracted poses, after its direction-specific delay. Different values let doors and struts move at different speeds. | `2`; Minimum: .01f |
| `extendDelay` | `float` | Delay in seconds before this part begins its deployment motion. | `0`; Minimum: 0 |
| `retractDelay` | `float` | Delay in seconds before this part begins its retraction motion. | `0`; Minimum: 0 |
| `type` | `LandingGearPartType` | Identifies this piece as a strut, door, link or custom part for landing-gear setup. Its actual movement still comes from this part's configured poses and timing. Options: `Strut`, `Door`, `Link`, `Custom`. | `Strut` |

## LandingGearSuspension

Configuration/implementation type for landing gear suspension within flight and landing gear.

**Source:** `Runtime/Exterior/Aircraft/LandingGearSuspension.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `parts` | `LandingGearSuspensionPart[]` ([fields](Exterior.md#landinggearsuspensionpart)) | Gear legs that receive additional loaded suspension motion. Each entry connects a landing-gear part with the wheel and its load response. | `Empty list` |

## LandingGearSuspensionPart

Describes load-driven hinge response for a gear part.

**Source:** `Runtime/Exterior/Aircraft/LandingGearSuspensionPart.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Optional independent suspension spring hinge and local axis frame. Empty uses Gear Part > Anchor. Drives visible motion, wheel mount and spring-load torque. | `None / unassigned` |
| `angularInertia` | `float` | Effective angular inertia used when converting the suspension response into hinge motion. | `500`; Minimum: 1 |
| `authoredAngle` | `float` | Angle already present in the authored deployed mesh, in degrees. | `28` |
| `dampingTorque` | `float` | Strength of the torque opposing the leg's suspension rotation. Increase to settle the gear faster after a load change; reduce to allow more oscillation. | `3500`; Minimum: 0 |
| `gearPart` | `LandingGearPart` ([fields](Exterior.md#landinggearpart)) | Deployable gear part whose pose receives the suspension compression offset. Assign the leg rather than a fixed chassis object. | `None / unassigned` |
| `localAxis` | `Vector3` | Local axis around which this gear part rotates under suspension load. Match it to the leg's compression hinge direction. | `Vector3.forward` |
| `maximumAngle` | `float` | Maximum additional suspension rotation in degrees for this gear leg. Increase for more visible compression travel under load. | `28`; Range: -80 to 80 |
| `reverse` | `bool` | Mirror motion around the neutral pose without changing input or travel limits. | `false` |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `springTorque` | `float` | Strength of the rotational spring returning the loaded gear leg toward its uncompressed pose. Increase for a firmer leg; Damping Torque controls how much it oscillates. | `18000`; Minimum: 1 |
| `wheel` | `WheelCollider` | Wheel collider providing ground contact and load information for this leg. The additional suspension response follows this wheel's state. | `None / unassigned` |

## LightChannel

One lamp/emission output channel, including lit output state and its output notification.

**Source:** `Runtime/Exterior/Lights/LightChannel.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `color` | `Color` | Colour assigned to this channel's Unity lights and lens-emission tint. It changes both the cast light and the visible illuminated lamp colour. | `Color.white` |
| `emission` | `float` | Emission multiplier applied to the channel lens materials when active. | `2`; Minimum: 0 |
| `enabled` | `bool` | Allows this lamp group to light when requested. Turn off to make the group unavailable without clearing its Light and lens assignments. | `true` |
| `glows` | `VehicleLampGlow[]` ([fields](Exterior.md#vehiclelampglow)) | Visible lens halos, separate from lights illuminating the road. Use Add lamp glows in this component's context menu to create and connect them in Edit Mode. | `Empty list` |
| `intensity` | `float` | Light intensity applied to the channel light sources when active. | `4`; Minimum: 0 |
| `lenses` | `Renderer[]` | Renderers whose emission is changed to show illuminated lamp glass. This makes the lamp look lit even when it uses no Unity Light. | `Empty list` |
| `lensMaterials` | `LightLensBinding[]` ([fields](Exterior.md#lightlensbinding)) | Existing on/off materials for individual lens slots. Emission and textures are authored on those assets; no materials are created at runtime. | `Empty list` |
| `lights` | `Light[]` | Unity Light components switched together by this channel. Use these for the light cast onto the world; lens glow is configured separately. | `Empty list` |

## LightLensBinding

One lens material slot switched between existing material assets. No runtime materials are created or modified.

**Source:** `Runtime/Exterior/Lights/LightLensBinding.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `materialIndex` | `int` | Zero-based material slot. Other slots on the Renderer stay unchanged. | `0`; Minimum: 0 |
| `offMaterial` | `Material` | Your material for the unlit lens. Empty uses the original slot material. | `None / unassigned` |
| `onMaterial` | `Material` | Your material for the lit lens. Configure emission, color and texture on this asset. Empty uses the original slot material. | `None / unassigned` |
| `renderer` | `Renderer` | Renderer containing the visible lamp surface, including skinned meshes. | `None / unassigned` |

## Lights

Owns beam/indicator requests, automatic outputs and timing.

**Source:** `Runtime/Exterior/Lights/Lights.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `automaticBrakeLights` | `bool` | Derives brake-light activation from the vehicle brake request unless overridden through the light API. | `true` |
| `automaticReverseLights` | `bool` | Derives reverse-light activation from the vehicle drivetrain direction unless overridden through the light API. | `true` |
| `blinkInterval` | `float` | Seconds between the lit and unlit phases of an indicator. A full on/off cycle takes twice this time; increase for slower blinking. | `.45`; Minimum: .05f |
| `brakeLights` | `LightChannel` ([fields](Exterior.md#lightchannel)) | Optional Light sources and emissive renderers for the service brake. | `new LightChannel{color = Color.red, intensity = .12}` |
| `brakeLightThreshold` | `float` | Minimum applied service brake that turns on stop lamps. Includes progressive and analog braking. | `.01`; Range: 0 to 1 |
| `customLights` | `List<CustomLightGroup>` ([fields](Exterior.md#customlightgroup)) | Additional named/custom lighting groups independent of the standard vehicle channels. | `Empty list` |
| `engine` | `Engine` ([fields](Engine.md#engine)) | Engine used to determine reverse gear for reverse lamps. Setup finds the vehicle's Engine when empty; movement/drive demand provides a fallback when no gearbox is active. | `None / unassigned` |
| `handbrakeActivatesBrakeLights` | `bool` | Includes an applied handbrake in the automatic brake-light request. | `false` |
| `headlights` | `LightChannel` ([fields](Exterior.md#lightchannel)) | Low-beam lamp group: its Unity lights, glowing lens renderers and emission settings. Updated by the headlight request. | `new LightChannel()` |
| `headlightsOn` | `bool` | Initial/requested low-beam headlight state. | `false` |
| `highBeams` | `LightChannel` ([fields](Exterior.md#lightchannel)) | High-beam lamp group, configured separately from the normal headlights. Assign only the lights/lenses that should respond to the high-beam request. | `new LightChannel()` |
| `highBeamsOn` | `bool` | Initial/requested high-beam state. | `false` |
| `indicators` | `IndicatorState` | Starts with indicators off, blinking on the left, blinking on the right, or blinking on both sides as hazards. Control commands can change this state during play. Options: `Off`, `Left`, `Right`, `Hazard`. | `Off` |
| `leftIndicators` | `LightChannel` ([fields](Exterior.md#lightchannel)) | Lamps and lens renderers blinking for a left turn or hazards. The blink interval is shared with the right side. | `new LightChannel{color = new Color(1, .4, 0), intensity = .1}` |
| `reverseLights` | `LightChannel` ([fields](Exterior.md#lightchannel)) | Optional Light sources and emissive renderers for selected reverse gear / direct reverse drive. | `new LightChannel{intensity = .25}` |
| `rightIndicators` | `LightChannel` ([fields](Exterior.md#lightchannel)) | Lamps and lens renderers blinking for a right turn or hazards. Keep the left lamps in Left Indicators so single-side requests work correctly. | `new LightChannel{color = new Color(1, .4, 0), intensity = .1}` |
| `tailLights` | `LightChannel` ([fields](Exterior.md#lightchannel)) | Rear/tail light channel. | `new LightChannel{color = Color.red, intensity = .04}` |

## MovingPart

Owns rotation/translation requests, constraints and scheduled motion.

**Source:** `Runtime/Exterior/Parts/MovingPart.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Optional independent hinge and local axis frame. Rotation uses its pivot and axes; Part-space translation uses its axes while preserving the neutral mesh pose. | `None / unassigned` |
| `angleLimits` | `Vector2` | Minimum and maximum rotation in degrees relative to the captured neutral pose. Used when Limit Rotation is on and to map normalized position commands to angles. | `new Vector2(-45, 45)` |
| `decreasingMotionCurve` | `AnimationCurve` | Normalized elapsed time to travel progress toward a lower angle/position. Independent of the increasing curve. Speed sets average travel speed; target changes restart from the current pose. | `AnimationCurve.Linear(0, 0, 1, 1)` |
| `increasingIsOpening` | `bool` | Increasing angle/position represents opening events and sounds when enabled; disable to reverse opening/closing directions. | `true` |
| `increasingMotionCurve` | `AnimationCurve` | Normalized elapsed time to travel progress toward a higher angle/position. Linear preserves constant speed; flatten near the end to slow down. Applies to fixed targets, not rate input or aiming. | `AnimationCurve.Linear(0, 0, 1, 1)` |
| `limitRotation` | `bool` | Restricts rotation to Angle Limits. Turn off for continuous rotation, such as a turret that can turn through a full circle. | `true` |
| `localAxis` | `Vector3` | Local rotation axis for rotational movement, or base travel direction for translation. Use a nonzero vector aligned with the model's intended hinge/slide direction. | `Vector3.up` |
| `localForward` | `Vector3` | Direction treated as the part's forward/aiming direction when calculating a target angle. Change it for a mesh whose visible forward direction is not local Z. | `Vector3.forward` |
| `motion` | `MovingPartMotion` | Rotation turns around Local Axis; Translation slides along the chosen translation frame. Selecting the mode changes whether Angle Limits or Translation Limits define the travel. Options: `Rotation`, `Translation`, `Animation`, `Custom`. | `Rotation` |
| `motionEnabled` | `bool` | Allows rotation and translation commands to move this part. Turn off to freeze the motion without deleting its references or limits. | `true` |
| `motionEvents` | `PartMotionEvents` ([fields](Exterior.md#partmotionevents)) | Inspector callbacks for operation starts and actual arrivals. Interrupted operations do not publish completion. | `new PartMotionEvents()` |
| `part` | `Transform` | Transform moved by rotation/translation commands. If empty, the component's own transform is used. Assign the moving mesh, keeping any fixed anchor outside its hierarchy. | `None / unassigned` |
| `playback` | `PartMotionPlayback` ([fields](Exterior.md#partmotionplayback)) | Clip or custom motion implementation, plus lifecycle callbacks. Rotation/Translation still use the existing procedural path. | `new PartMotionPlayback()` |
| `reverse` | `bool` | Mirror motion around the neutral pose without changing input or travel limits. | `false` |
| `showGizmos` | `bool` | Show motion guides and the active pose owner in the Scene view. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `speed` | `float` | Angular rate in degrees per second for input/aiming, or average travel speed for a fixed target shaped by the direction curve. | `35`; Minimum: 0 |
| `translationAnchor` | `Transform` | Optional direction override in Anchor translation space. Empty uses Anchor; invalid references fall back to the neutral part frame. | `None / unassigned` |
| `translationDirectionAngles` | `Vector3` | Additional Euler rotation of the travel axis in the selected coordinate space, in degrees. | `Zero-initialized Vector3` |
| `translationLimits` | `Vector2` | Translation travel in metres, measured from the authored neutral pose. | `new Vector2(0, .35)` |
| `translationSpace` | `MovingPartSpace` | Frame used for translation: Part follows the part's neutral axes, Parent follows its parent, World uses world axes, and Anchor uses the assigned fixed reference. Choose the frame in which the slide should remain aligned. Options: `Part`, `Parent`, `World`, `Anchor`. | `Part` |
| `translationSpeed` | `float` | Translation rate in metres per second for input, or average travel speed for a fixed target shaped by the direction curve. | `.2`; Minimum: 0 |

## PartClipAnimation

Samples a non-Legacy animation clip on an assigned Animator, with an optional separate closing clip.

**Source:** `Runtime/Exterior/Parts/Motion/PartClipAnimation.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `animator` | `Animator` | Dedicated Animator at the root used by the clip's transform/bone paths. No controller asset is required. | `None / unassigned` |
| `clip` | `AnimationClip` | Clip sampled from its closed/start pose (0) to its open/end pose (1). Supports transform and skeletal animation. | `None / unassigned` |
| `closingClip` | `AnimationClip` | Optional separate closing clip, sampled forward as progress decreases. Empty plays the main clip backwards. | `None / unassigned` |
| `duration` | `float` | Seconds for a full 0..1 trip. Zero uses the selected clip's duration. | `0`; Minimum: 0 |

## PartMotionAudio

Four cue clip lists and optional independent settings overrides. The Audio Settings group configures shared playback; individual cues can override it.

**Source:** `Runtime/Exterior/Parts/PartMotionAudio.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `audioSettings` | `VehicleAudioSettings` ([fields](Effects.md#vehicleaudiosettings)) | Shared playback settings for this moving part, used unless an individual phase overrides them. | `new VehicleAudioSettings{minDistance = 1, maxDistance = 25, pitchRange = new Vector2(.95, 1.05), cooldown = .1}` |
| `closingClips` | `AudioClip[]` | Random one-shot clips before closing begins. | `Empty list` |
| `closingCompleted` | `AudioSettingsOverride` ([fields](Effects.md#audiosettingsoverride)) | Optional playback override for the fully-closed cue. | `new AudioSettingsOverride()` |
| `closingCompletedClips` | `AudioClip[]` | Random one-shot clips when the actual pose reaches its closing target. | `Empty list` |
| `closingStarted` | `AudioSettingsOverride` ([fields](Effects.md#audiosettingsoverride)) | Optional playback override for the closing-start cue. | `new AudioSettingsOverride()` |
| `openingClips` | `AudioClip[]` | Random one-shot clips before opening begins. Empty lists stay silent. | `Empty list` |
| `openingCompleted` | `AudioSettingsOverride` ([fields](Effects.md#audiosettingsoverride)) | Optional playback override for the fully-open cue. | `new AudioSettingsOverride()` |
| `openingCompletedClips` | `AudioClip[]` | Random one-shot clips when the actual pose reaches its opening target. | `Empty list` |
| `openingStarted` | `AudioSettingsOverride` ([fields](Effects.md#audiosettingsoverride)) | Optional playback override for the opening-start cue. | `new AudioSettingsOverride()` |

## PartMotionEvents

Inspector callbacks shared by VehicleBodyPart and MovingPart. C# events on the component publish the same operation notifications.

**Source:** `Runtime/Exterior/Parts/PartMotionEvents.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `onClosingCompleted` | `UnityEvent` | Invoked when this part reaches its fully closed target. | `No listeners` |
| `onClosingStarted` | `UnityEvent` | Invoked once when this part begins closing; connect Inspector listeners to the closing transition. | `No listeners` |
| `onOpeningCompleted` | `UnityEvent` | Invoked when this part reaches its fully open target. | `No listeners` |
| `onOpeningStarted` | `UnityEvent` | Invoked once when this part begins opening; connect Inspector listeners to the opening transition. | `No listeners` |

## PartMotionPlayback

Shared normalized motion state used by procedural parts, animation clips and custom movement drivers.

**Source:** `Runtime/Exterior/Parts/PartMotionPlayback.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `animation` | `PartClipAnimation` ([fields](Exterior.md#partclipanimation)) | Animation clip, binding root and optional closing animation. | `new PartClipAnimation()` |
| `customDriver` | `MonoBehaviour` | Optional component implementing ICustomPartMotion. Inspector callbacks can be used instead, or alongside it. | `None / unassigned` |
| `signals` | `PartMotionSignals` ([fields](Exterior.md#partmotionsignals)) | Movement lifecycle and external movement requests, available in code and the Inspector. | `new PartMotionSignals()` |

## PartMotionSignals

C# and Inspector notifications for accepted requests, progress and operation termination.

**Source:** `Runtime/Exterior/Parts/Motion/PartMotionSignals.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `onBegin` | `UnityEvent<float>` | Accepted operation target in normalized units. May cancel or replace the request. | `No listeners` |
| `onCancel` | `UnityEvent` | Operation interrupted, replaced, disabled or explicitly cancelled. | `No listeners` |
| `onEnd` | `UnityEvent` | Operation completed successfully. Stopping or cancelling does not fire this event. | `No listeners` |
| `onInputChanged` | `UnityEvent<float>` | Signed rate demand, including zero when rate input is released. | `No listeners` |
| `onMove` | `UnityEvent<float>` | Reported normalized progress after the pose update. Custom mode never writes a pose itself. | `No listeners` |
| `onMoveRequested` | `UnityEvent<float>` | Accepted target request; connect your own movement implementation here in Custom mode. | `No listeners` |
| `onStop` | `UnityEvent` | Operation stopped, after successful completion, a manual stop or cancellation. | `No listeners` |
| `onStopRequested` | `UnityEvent` | Explicit stop/cancel request; stop your external tween, animation or task here. | `No listeners` |
| `onTick` | `UnityEvent<float>` | Elapsed seconds for an active motion update in any mode. Custom motion can use this instead of a separate Update. | `No listeners` |

## PedalDrive

### Methods

**Source:** `Runtime/Exterior/Bicycle/PedalDrive.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `boostCadenceMultiplier` | `float` | Maximum cadence multiplier at full nitro strength. Road speed still determines the requested cadence. | `1.5`; Minimum: 1 |
| `cadenceResponse` | `float` | Cadence acceleration/deceleration in RPM per second. | `180`; Minimum: .01f |
| `crank` | `Transform` | Crank pivot; its local axis follows the wheel axle. | `None / unassigned` |
| `driveRatio` | `float` | Driven-wheel revolutions per crank revolution. | `2.8`; Minimum: .01f |
| `leftPedal` | `Transform` | Independent pedal pivot counter-rotated to keep the left foot platform level. | `None / unassigned` |
| `localAxis` | `Vector3` | Crank rotation axis in the pivot's initial local frame. | `Vector3.right` |
| `maximumCadence` | `float` | Maximum cadence in revolutions/minute. | `110`; Minimum: 0 |
| `minimumCadence` | `float` | Minimum cadence while actively pedalling, in revolutions/minute. | `20`; Minimum: 0 |
| `pedalWhileCoasting` | `bool` | Keep rotating while coasting forward. Otherwise requires forward throttle. | `false` |
| `rider` | `BalanceRider` ([fields](World.md#balancerider)) | Rider whose occupied seat and riding blend enable pedalling. | `None / unassigned` |
| `rightPedal` | `Transform` | Independent pedal pivot counter-rotated to keep the right foot platform level. | `None / unassigned` |

## Propulsion

Animates propellers and rotors for aircraft, boats and submarines.

**Source:** `Runtime/Exterior/Aircraft/Propulsion.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `engine` | `Engine` ([fields](Engine.md#engine)) | Engine supplying running state and, when selected, RPM for visible propeller/rotor rotation. The component finds the vehicle's Engine during setup when empty. | `None / unassigned` |
| `propellers` | `Propeller[]` ([fields](Exterior.md#propulsionpropeller)) | Independently rotating propellers or rotors. Each entry chooses its mesh, rotation axis and whether spin follows engine RPM or control demand. | `Empty list` |
| `spinDownSeconds` | `float` | Seconds for spool or a smoothed shaft demand to fall toward zero. Longer values let the propeller coast visibly after power is removed. | `2.4`; Minimum: .01f |
| `spinUpSeconds` | `float` | Seconds for engine spool or a smoothed shaft demand to rise toward full speed. Longer values make the rotor take longer to get going after startup or increased demand. | `1.8`; Minimum: .01f |

## Propulsion.Propeller

Configuration/implementation type for propeller within flight and landing gear.

**Source:** `Runtime/Exterior/Aircraft/Propulsion.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Optional independent shaft pivot and local axis frame outside the rotating mesh. Empty keeps mesh-local rotation. | `None / unassigned` |
| `degreesPerSecond` | `float` | Visible propeller/rotor spin speed at full requested output, in degrees per second. | `900` |
| `instantThrustResponse` | `bool` | Bypass smoothing of control-driven shaft demand to match immediate thrust forces. Engine-only rotation keeps its engine spool. | `false` |
| `localAxis` | `Vector3` | Axis in the propeller mesh's local coordinates around which it spins. Set it along the shaft, with the mesh pivot at the rotation centre. | `Vector3.up` |
| `maneuverSpeed` | `float` | Shaft speed at full steering, lift or pitch demand; throttle can request a higher speed. | `.5`; Range: 0 to 1 |
| `onlyInWater` | `bool` | Require an enabled water provider/fallback and at least partial hull immersion. A dry hull stops shaft rotation. | `false` |
| `onlyWithThrust` | `bool` | Scale rotation by throttle and enabled maneuver demands. No demand stops the shaft. Works with fixed speed or engine RPM. | `false` |
| `physicsRotation` | `bool` | Advance collidable blades before each physics simulation. Leave disabled for visual-only shafts. | `false` |
| `reverse` | `bool` | Reverse the visible shaft rotation. | `false` |
| `reverseWithThrust` | `bool` | Reverse rotation for negative throttle. Independent of Only With Thrust and Use Engine Rpm. | `false` |
| `rpmRatio` | `float` | Rotor RPM / engine RPM. Negative values reverse rotation. | `1` |
| `spinWithLift` | `bool` | Include vertical Lift demand in shaft rotation. | `false` |
| `spinWithPitch` | `bool` | Include Pitch demand in shaft rotation. | `false` |
| `spinWithSteering` | `bool` | Include combined Steering/Yaw demand, including turning at rest. Forward/reverse throttle determines shaft direction. | `false` |
| `transform` | `Transform` | Mesh rotated for this propeller or rotor. Assign a transform whose pivot is at the shaft centre so it spins in place. | `None / unassigned` |
| `useEngineRpm` | `bool` | Derive rotor speed from engine RPM instead of fixed degrees per second. | `false` |

## SteeringPart

Rotates a rudder, outboard motor or another visible steering pivot from a scalar source, independently of vehicle forces.

**Source:** `Runtime/Exterior/Parts/SteeringPart.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Optional independent steering pivot and local axis frame. Empty retains the original rest-local mesh rotation. | `None / unassigned` |
| `inputSource` | `MonoBehaviour` | Optional Steering Source or another IInteriorValueSource. Empty uses the vehicle steering command; disabled or invalid sources produce zero. | `None / unassigned` |
| `localAxis` | `Vector3` | Rotation axis in the part neutral local frame. | `Vector3.up` |
| `motionMode` | `AircraftControlMotionMode` | Procedural rotation/translation, clip animation or callback-only custom movement. Options: `Rotation`, `Translation`, `Animation`, `Custom`. | `Rotation` |
| `multiplier` | `float` | Scales steering travel; zero stops rotation. | `1` |
| `part` | `Transform` | Rudder, outboard motor or other steering pivot. Initial local rotation is neutral. | `None / unassigned` |
| `playback` | `PartMotionPlayback` ([fields](Exterior.md#partmotionplayback)) | Animation/custom implementation and lifecycle callbacks. | `new PartMotionPlayback()` |
| `response` | `float` | Steering response per second; zero follows the source immediately. | `8`; Minimum: 0 |
| `reverse` | `bool` | Reverses visible steering rotation. | `false` |
| `showGizmos` | `bool` | Show mode-specific steering motion guides in the Scene view. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `steeringAngle` | `float` | Angle in degrees at full steering before Multiplier and Reverse. | `30`; Minimum: 0 |
| `translationTravel` | `float` | Metres of translation at full steering in either direction. | `.05` |
| `vehicle` | `VehicleController` ([fields](Controller.md#vehiclecontroller)) | Optional fallback vehicle; finds the parent vehicle when empty. | `None / unassigned` |

## TrackPathBuilder

Prepares reusable closed paths during authoring.

**Source:** `Runtime/Exterior/TrackPathBuilder.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `explicitLinks` | `Transform[]` | Additional links, or the complete list when Links Parent is empty. Duplicates are removed. | `Empty list` |
| `leftBelt` | `bool` | Marks this path as the left track belt; unchecked configures the right belt. | `true` |
| `linksParent` | `Transform` | Collect mesh objects recursively from this parent. Leave empty to use only Explicit Links. | `None / unassigned` |
| `order` | `LinkOrder` | AroundBelt sorts the selected track links around the belt; InputOrder keeps the supplied order. Use InputOrder when the model already has a correctly sequenced chain. Options: `AroundBelt`, `InputOrder`. | `LinkOrder.AroundBelt` |
| `pathParent` | `Transform` | Optional destination. If empty, a dedicated Path object is created beside this builder. | `None / unassigned` |
| `position` | `LinkPosition` | Chooses whether generated path points use each link's mesh-bounds centre or transform pivot. Use mesh centres when imported pivots are displaced from the visible links. Options: `MeshBoundsCenter`, `TransformPivot`. | `LinkPosition.MeshBoundsCenter` |
| `reverseOrder` | `bool` | Reverse the node order and matching links together. | `false` |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `travelDirection` | `float` | Direction relative to positive wheel rim speed; default matches clockwise ordering in vehicle Y/Z. | `-1` |
| `visuals` | `TrackVisuals` ([fields](Exterior.md#trackvisuals)) | Assign the vehicle's TrackVisuals. Automatically found in parents when available. | `None / unassigned` |

## TrackVisuals

Moves visible links and rollers from wheel motion.

**Source:** `Runtime/Exterior/TrackVisuals.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `leftBelt` | `Belt` ([fields](Exterior.md#trackvisualsbelt)) | Path and moving link meshes for the left track. Its links advance at the measured left-side track speed. | `new Belt()` |
| `rightBelt` | `Belt` ([fields](Exterior.md#trackvisualsbelt)) | Path and moving link meshes for the right track. Keeping it separate lets opposite track speeds show turning on the spot. | `new Belt()` |
| `rollers` | `Roller[]` ([fields](Exterior.md#trackvisualsroller)) | Road wheels, return rollers or sprockets to spin with a track. Each entry chooses a side, mesh axis and radius used to convert belt speed to rotation. | `Empty list` |

## TrackVisuals.Belt

Configuration/implementation type for belt within tracked movement.

**Source:** `Runtime/Exterior/TrackVisuals.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `links` | `Transform[]` | Visible track links, one per path point in matching order. Their initial offsets/orientations are retained while they move around the captured loop. | `Empty list` |
| `path` | `Transform[]` | Ordered points forming the closed belt loop, with at least three entries. Their initial positions are captured as the fixed path the links travel along. | `Empty list` |
| `reverse` | `bool` | Reverse belt travel along its authored path. | `false` |
| `travelDirection` | `float` | Path travel direction relative to positive wheel rim speed. | `-1` |

## TrackVisuals.Roller

Configuration/implementation type for roller within tracked movement.

**Source:** `Runtime/Exterior/TrackVisuals.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `left` | `bool` | Drive this roller from the left track speed rather than the right. | `false` |
| `localAxis` | `Vector3` | Roller mesh's local axle direction. The mesh rotates around this axis at a speed calculated from belt speed and Radius. | `Vector3.right` |
| `radius` | `float` | Roller radius in metres used to turn belt speed into angular speed. A smaller roller must spin faster to match the same moving track. | `.5`; Minimum: .01f |
| `reverse` | `bool` | Reverse the visible roller spin. | `false` |
| `transform` | `Transform` | Roller or sprocket mesh rotated by the selected track's speed. Put its pivot on the axle so the mesh spins without orbiting. | `None / unassigned` |

## VehicleBodyPart

Defines a named opening/moving body element.

**Source:** `Runtime/Exterior/Parts/VehicleBodyPart.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Optional independent hinge. Its position replaces Hinge Anchor and its local axes define Hinge Axis for animation and physical joints. | `None / unassigned` |
| `closingMotionCurve` | `AnimationCurve` | Normalized elapsed time to closing progress, independently of opening. Speed determines average commanded degrees per second. | `AnimationCurve.Linear(0, 0, 1, 1)` |
| `completionTolerance` | `float` | Actual hinge angle tolerance in degrees for completion events, including physical hinges. | `1`; Minimum: .001f |
| `damper` | `float` | Damping of hinge angular movement, reducing overshoot and repeated oscillation. | `50`; Minimum: 0 |
| `hingeAnchor` | `Vector3` | Hinge position in this transform's local mesh coordinates. Zero uses its origin. | `Zero-initialized Vector3` |
| `hingeAxis` | `Vector3` | Local hinge axis used for this part opening motion. | `Vector3.up` |
| `localTranslationAxis` | `Vector3` | Translation axis in Anchor axes when assigned, otherwise in the captured part frame. | `Vector3.up` |
| `mass` | `float` | Rigidbody mass in kilograms used when this part is physically simulated. | `15`; Minimum: .01f |
| `minimumUnlatchForce` | `float` | Minimum average contact force in newtons: collision impulse divided by the fixed timestep. | `4000`; Minimum: 0 |
| `minimumUnlatchSpeed` | `float` | Minimum impact speed into the contact normal in m/s. Rejects ordinary sliding along a panel. | `1`; Minimum: 0 |
| `motion` | `MovingPartMotion` | How accepted open/close requests move this part. Custom only dispatches callbacks and driver requests. Options: `Rotation`, `Translation`, `Animation`, `Custom`. | `Rotation` |
| `motionEvents` | `PartMotionEvents` ([fields](Exterior.md#partmotionevents)) | Inspector callbacks for operation starts and actual arrivals. Interrupted operations do not publish completion. | `new PartMotionEvents()` |
| `openAngle` | `float` | Requested fully open hinge angle in degrees. | `70`; Range: -170 to 170 |
| `openingMotionCurve` | `AnimationCurve` | Normalized elapsed time to opening progress. Linear gives constant commanded speed; flatten the end to slow before fully open. Physical hinges follow this spring target under load. | `AnimationCurve.Linear(0, 0, 1, 1)` |
| `partId` | `string` | Stable identifier used by body-part lookup and control APIs. | `None / unassigned` |
| `partType` | `PartType` | Body-part role used by controls, damage and presentation. Options: `Door`, `Hood`, `Trunk`, `Tailgate`, `Other`. | `Door` |
| `permanentImpactUnlatch` | `bool` | Keep the damaged latch open until Close/SetOpen(false) is explicitly called. Otherwise it can latch again after returning to its closed pose. | `false` |
| `playback` | `PartMotionPlayback` ([fields](Exterior.md#partmotionplayback)) | Clip binding, optional external driver and lifecycle callbacks. | `new PartMotionPlayback()` |
| `releasedCollisionDelay` | `float` | Minimum seconds to ignore former vehicle collisions after release. Overlapping pairs wait until separated. | `.5`; Minimum: 0 |
| `reverse` | `bool` | Mirror motion around the neutral pose without changing input or travel limits. | `false` |
| `showGizmos` | `bool` | Show this part's motion guides and range in the Scene view. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `speed` | `float` | Average commanded angular speed in degrees/second. Direction curves redistribute this speed over the trip; physical hinges follow the resulting spring target under load. | `100`; Minimum: 1 |
| `spring` | `float` | Restoring strength of this part hinge motion toward its requested pose. | `300`; Minimum: 0 |
| `temporaryUnlatchDelay` | `float` | Minimum seconds before a temporary released latch may engage again near the closed pose. | `.25`; Minimum: 0 |
| `translationDistance` | `float` | Metres of translation at the fully open position. | `.35` |
| `translationDuration` | `float` | Seconds for a full translational opening or closing trip. | `1`; Minimum: .001f |
| `unlatchedDamperMultiplier` | `float` | Hinge damping multiplier while collision-unlatched. Lower values allow longer swinging. | `1`; Range: 0 to 1 |
| `unlatchedSpringMultiplier` | `float` | Closing spring multiplier while collision-unlatched. Zero lets the panel swing freely; one keeps its normal spring. | `1`; Range: 0 to 1 |
| `unlatchOnImpact` | `bool` | Allow a physical collision or damage impact to release the closed latch. Both impact thresholds must be met. | `true` |
| `usePhysics` | `bool` | Use native Rigidbody/joint motion for this part rather than only transforming the visible model. | `false` |

## VehicleLampGlow

A depth-tested lens halo, controlled by a LightChannel and rendered with the bundled Lamp Glow material. Use the Lights component menu's **Add lamp glows** command to create saved sources at assigned lamps.

**Source:** `Runtime/Exterior/Lights/VehicleLampGlow.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `brightness` | `float` | Visible lens brightness; independent of the Unity Light intensity and does not illuminate other objects. | `2`; Minimum: 0 |
| `directional` | `bool` | Fade when viewed from behind the lamp. The glow object's local Z axis points out of the lens. | `true` |
| `glowRenderer` | `Renderer` | Renderer using the bundled Lamp Glow material. Save the quad as a child of the lamp, facing outward along its local Z axis. | `None / unassigned` |
| `radius` | `float` | Halo radius in world metres, independent of the vehicle model scale. | `.12`; Range: .005f to .5f |

## WheelPart

Inherits [DamagePart](../API/Damage.md#damagepart). Add to the visual wheel root. See [setup and repair tutorials](../Damage.md#detachable-wheels).

**Source:** `Runtime/Exterior/Parts/WheelPart.cs`. Component / asset.

**Inherited settings:** [DamagePart](Exterior.md#damagepart). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `colliderSegments` | `int` | Number of sides used by the detached solid wheel collision shape. More segments make rolling smoother at extra collision cost. | `20`; Range: 8 to 32 |
| `debrisMaterial` | `PhysicsMaterial` | Physics material applied to detached wheel/debris contacts. | `None / unassigned` |
| `generateRollingCollider` | `bool` | Build a convex cylindrical tire collider on release so the detached wheel can roll. Disable to use your own colliders. | `true` |
| `wheel` | `Wheel` ([fields](Physics.md#wheel)) | Wheel adapter on the vehicle's WheelCollider mount. Visual must be this transform or a child of it. | `None / unassigned` |

## Wiper

Configuration/implementation type for wiper within exterior wipers.

**Source:** `Runtime/Exterior/Wipers/Wipers.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Optional reference positioning the fallback blade at Anchor Local Position. Use it when the blade should follow an attachment separate from its own pivot. | `None / unassigned` |
| `anchorLocalPosition` | `Vector3` | Local pivot-position adjustment in metres. | `Zero-initialized Vector3` |
| `blade` | `Transform` | Blade transform rotated by the fallback sweep animation when no Helper is assigned. Its resting local rotation is captured before motion starts. | `None / unassigned` |
| `cyclesPerMinute` | `float` | Full wipe cycles per minute for this wiper. | `45`; Minimum: 0 |
| `helper` | `WiperBlade` ([fields](Exterior.md#wiperblade)) | Optional WiperBlade component owning this blade's anchored motion. When assigned, it receives the sweep value instead of the raw Blade/Anchor fallback. | `None / unassigned` |
| `id` | `string` | Unique, case-sensitive ID within this Wipers component. | `None / unassigned` |
| `independentSettings` | `bool` | Use this entry's running state and speed instead of the shared defaults. | `false` |
| `localAxis` | `Vector3` | Axis in the fallback blade's local frame around which the wipe rotates. Set it along the wiper spindle so the blade sweeps across the glass. | `Vector3.forward` |
| `parkedAngle` | `float` | Resting blade angle in degrees added to its captured local rotation. Adjust it to place the blade at the bottom of the glass when stopped. | `0` |
| `reverse` | `bool` | Reverses the authored sweep direction for this wiper. | `false` |
| `running` | `bool` | Requests this individual wiper to run. | `false` |
| `sweepAngle` | `float` | Total angular travel in degrees from the parked pose to the far end of a wipe. Increase to cover a larger part of the glass; Reverse flips the sweep direction. | `75` |
| `type` | `WiperType` | Category used to select this wiper for front, rear or custom commands. It does not change the sweep geometry by itself. Options: `Front`, `Rear`, `Custom`. | `Front` |

## WiperBlade

Maps normalized stroke to authored blade geometry.

**Source:** `Runtime/Exterior/Wipers/WiperBlade.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `maximumAngle` | `float` | Blade rotation in degrees at sweep value one. The difference from Minimum Angle sets the width and direction of the wipe. | `65` |
| `minimumAngle` | `float` | Blade rotation in degrees at sweep value zero. Usually the parked end of the wipe; use Maximum Angle for the far end. | `0` |
| `motion` | `AnchoredRotation` ([fields](Interior.md#anchoredrotation)) | Anchored rotation setup for this blade. Put its anchor on the wiper spindle and keep imported mesh alignment on the moving child. | `new AnchoredRotation{localAxis = Vector3.forward}` |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `type` | `WiperType` | Category identifying the blade as front, rear or custom. Use matching categories when selecting which wipers a command should operate. Options: `Front`, `Rear`, `Custom`. | `Front` |

## Wipers

Owns wiper cycle timing, running state and blade dispatch.

**Source:** `Runtime/Exterior/Wipers/Wipers.cs`. Component / asset.

**Inherited settings:** [ExteriorModule](Exterior.md#exteriormodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `cyclesPerMinute` | `float` | Default complete outward-and-return wiper cycles per minute. | `45`; Minimum: 0 |
| `running` | `bool` | Initial/requested running state for the wiper system. | `false` |
| `wipers` | `List<Wiper>` ([fields](Exterior.md#wiper)) | Individual blades controlled by this module. Each can share the main speed/audio settings or use its own overrides and commands. | `Empty list` |

## WiperSwitchBinding

Configuration/implementation type for wiper switch binding within exterior wipers.

**Source:** `Runtime/Exterior/Wipers/WiperSwitchBinding.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `onMeansRunning` | `bool` | Maps the switch On position to running wipers; unchecked reverses that mapping. | `true` |
| `switchAnimator` | `SwitchAnimator` ([fields](Interior.md#switchanimator)) | Switch animator whose requested/settled position drives this binding. Assign the matching cockpit switch component. | `None / unassigned` |
| `wipers` | `Wipers` ([fields](Exterior.md#wipers)) | Wiper module started or stopped by the switch. Changes made by other controls are also reflected back onto the handle. | `None / unassigned` |
