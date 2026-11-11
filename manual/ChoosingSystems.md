# Choose the systems you need

Get the vehicle moving before adding passengers, damage or effects. A working prefab is easier to extend when each new system can be tested on its own.

## Start with movement

Choose a [drive mode](DriveProfiles.md). The Add Vehicle preset installs a starting combination of modules. You still need the model's colliders, wheel references and input; the preset cannot place those for you.

For a wheel vehicle, verify ground contact, steering, propulsion and braking. For aircraft, verify taxiing and takeoff. For water vehicles, verify buoyancy and the water bounds before adding presentation.

## Add the result you want

| Desired result | Add or configure | Prepare first |
| --- | --- | --- |
| Different input, AI or replay | Input source | Working movement and command ownership |
| Optional boost | [Nitro](DrivingActions.md#nitro-boost) module | Running wheel-powered Engine, throttle and nitro supply |
| Wheelspin launch | [Burnout](DrivingActions.md#burnout-launch) | Optional Drive module, driven tires, Brakes and Friction |
| Manual/automatic gears | Engine, gearboxes and Transmission | Driven wheels and ratios |
| Driver or passenger | Passengers and seats | Character rig, pelvis position and reachable targets |
| Moving steering wheel/pedals | Interior animators or handles | Independent pivots and neutral anchors |
| Opening door/window | VehicleBodyPart or MovingPart | Hinge/slide frame and collision clearance |
| Collision damage | Damage, DamagePart and optional VehicleMeshDeformation | Part boundaries, collider ownership and readable visual meshes |
| Water support | Boat/Submarine and WaterInteraction | Water provider or profile bounds |
| Engine/tire sound | Audio and channels | Assigned clips and mechanical state |
| Dust, marks or splash | TireFeedback and the relevant effect | Contact detection and assigned materials/prefabs |
| Trailer | Trailer and Coupler | Independent vehicle bodies and nearby hitch anchors |

A handle gives a limb a contact target; an animator moves the model; a gameplay binding requests an action. Install the pieces your interaction requires. For example, a door can open without a character, and a character can rest a hand without operating a switch.

## Save and validate

Edit persistent settings outside Play Mode and save the prefab. Check a fresh instance after adding a system: spawning, disabling/enabling and resetting exercise different lifecycles. Your game owns input possession, save data, respawn, repair and the lifetime of detached characters or debris.

See [Troubleshooting](Troubleshooting.md) for failed setup and [Scripting](Scripting.md) for replacing a built-in responsibility.
