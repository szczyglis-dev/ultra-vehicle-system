# Troubleshooting

Start with one vehicle on a simple ground collider. Resolve configuration warnings before tuning handling or visual effects.

## Vehicle and wheels

| Symptom | Check |
| --- | --- |
| Wheel setup is rejected | Every entry needs a unique WheelCollider owned by the root Rigidbody. Radius, width and mass must be finite and above the accepted minimums. |
| Vehicle falls through the ground | Chassis/ground colliders, active WheelColliders, collision layers, wheel radius and suspension placement. |
| Wheels spin but the car barely moves | Driven-wheel flags, brake/handbrake input, gear selection, tire contact and traction-control intervention. |
| Vehicle will not accelerate | Input source enabled/assigned, engine ignition, fuel policy, selected gear and enabled Drive/Engine modules. |
| Wheels move away from the car | Separate the visible wheel pivot from the WheelCollider object; put mesh import offsets below the visual pivot. |
| Steering or tire rotation is reversed | Axis orientation, visual rotation offset and wheel steering multiplier. |
| Tuning resets on Play | Save outside Play Mode; edit physical wheel data in Wheel Setup after discovery. |

Use the controller's **Live** tab to distinguish missing input from missing mechanical response. Temporarily disable optional assists/effects to isolate the system involved.

## Characters and controls

| Symptom | Check |
| --- | --- |
| Seat stays empty | Assigned body/prefab, seat/core enabled state and both spawn-on-start flags. Custom mode requires application-owned spawning/entry. |
| Character bends or stretches | Bone mapping, authored joints, character scale and reachable pelvis/limb targets. Stronger drives do not fix an unreachable target. |
| Hand or foot does not follow | Limb mode, handle/anchor assignment, enabled handle, Hold and the chosen passenger controller. |
| Control rotates around the wrong point | Independent neutral anchor at the actual hinge, outside the moving hierarchy. |
| Entry animation is rejected | Seat reservation, vehicle speed, outside clearance, motion adapter and complete animation-profile bindings. |

Use the seated preview before checking dynamic restraints. See [Passengers](Passengers.md), [Handles](Seats.md) and [Access](PassengerAccess.md).

## Water, effects and rendering

| Symptom | Check |
| --- | --- |
| Boat sinks or loses thrust | Water provider enabled state, finite bounds, immersion, hull size and WaterInteraction master switch. |
| Vehicle floats but there is no splash | BoatWaterParticles channel switches and assigned materials/prefabs. Submarine support does not generate surface-boat effects. |
| Ground grip changes but effects do not | `Surface` configures grip; `TireSurface` and its profile configure effects. |
| Sound or particles are missing | Core/channel enabled state, assigned assets and the triggering mechanical state. |
| Mirror is blank | Observer, dedicated mirror camera, surface, material texture property, culling layers and pipeline support. |
| Damage does not deform a mesh | MeshFilter mesh readability, vertex density, damage switches and part multipliers. |

For technical timing and ownership questions, use the corresponding [reference topic](Scripting/README.md).
