# Supplied visual resources

The Asset Store import includes the Demo scene and reusable effect assets. All paths below are relative to the UltraVehicleSystem directory. Assign assets to the appropriate components; a Resources folder does not automatically bind its contents to every vehicle.

## Reusable effects

| Resource location | Contents / use |
| --- | --- |
| `Resources/Effects/Damage` | Default Damage, Glass and Plastic Feedback profiles; Metal, Glass, Plastic, Rubber and Mechanical Impact profiles; Metal Sparks, Glass Chips, Plastic Dust and Rubber Dust particle prefabs; dedicated sparks, glass and debris materials. See [damage feedback](DamageFeedback.md). |
| `Resources/Effects/Exhaust` | `Exhaust Smoke.prefab` for exhaust outlets driven by ExhaustSmoke. |
| `Resources/Effects/Jet` | `UVS Jet Exhaust.prefab`, JetFlame and ShockDiamond materials and textures for PropulsionJets. |
| `Resources/Effects/Lights` | `Lamp Glow.mat` for VehicleLampGlow. |
| `Resources/Effects/Nitro` | `NitroFlame.prefab` and `Nitro Flame.mat` for nitro exhaust effects. |
| `Resources/Effects/Shared` | `Smoke.mat`, the shared fallback material for generated smoke and dust. |
| `Resources/Effects/Tires` | `Tire Smoke.prefab`, `Tire Skid.mat` and `Tire Sand.mat`. TireSmoke uses the active TireSurfaceProfile's Particle Material for smoke and grains; Default Material is the fallback. The sand material is assigned to the demo sand/gravel profiles. Skidmarks keeps its own mark material. See [surface responses](Surfaces.md). |
| `Resources/Effects/Water` | `DefaultWaterSurfaceProfile.asset`, WaterSurface, WaterSpray and WaterFoam materials, and WaterRipples texture for WaterSurface and water particles. |
| `Resources/Effects/Weapons` | MuzzleFlash, MuzzleSmoke and Rocket Exhaust prefabs; Shell, Smoke, Rocket Smoke and Rocket Flame materials; SmokeTexture asset and rocket credit notice. |

## Demo assets

| Resource location | Contents / use |
| --- | --- |
| `Demo/Art` | Vehicle, mannequin and pistol models, model textures, asphalt and desert terrain textures, source animations and credit notices. |
| `Demo/Demo.unity` | Configured vehicle fleet, terrain, obstacles, water and demonstration controls. |
| `Demo/HandPositions` | Aircraft stick, throttle and wheel hand presets; MotorcycleGripProfile; WheelPalmPressure, WheelPinch and WheelWrappedGrip profiles. See [hand positions](HandPositions.md). |
| `Demo/Materials` | Vehicle and passenger materials; ground/checker materials and texture; cockpit instruments, mirrors, lights, pistol and underwater scenery materials. Reusable effect materials are in Resources/Effects. |
| `Demo/PhysicsMaterials` | Airplane rolling contact, Boat slipway and Loose obstacle contact physics materials; these affect collider response rather than rendered appearance. |
| `Demo/Prefabs` | Configured vehicle and trailer prefabs, including CarAnimator. |
| `Demo/Prefabs/CarAnimator` | Animator mannequin variants, PassengerAnimator controller, steering and switch animations, Wave animation and Steering Arms mask. |
| `Demo/Prefabs/Passengers` | UVS Mannequin Man, UVS Motorcycle Rider and UVS Standing Mannequin prefabs. |
| `Demo/Prefabs/Weapons` | `DefaultShell.prefab`, an example projectile using demo behavior and reusable weapon materials. |
| `Demo/Resources/UVSAccess` | Idle animation, Standing/StandingRight and left/right access controllers, plus left/right access profiles with open-door variants. See [passenger access](PassengerAccess.md). |
| `Demo/Surfaces` | AsphaltProfile, Dry gravel Profile and SandProfile: tire audio, particle and mark responses assigned through TireSurface. Sand and gravel explicitly reference Tire Sand. |

New effect components receive reusable defaults during authoring; repeated setup preserves existing custom references. Replace the appropriate prefab, material or surface profile to customize the effect. Check render-pipeline compatibility, particle scale/lifetime and resource cleanup before saving a prefab. Custom particle systems and custom prefabs retain their authored appearance.

For recordings and sound profiles in `Resources/Audio` and `Demo/Audio`, use [Audio](Audio.md). For authors, licenses and source links, see [Third-party credits](ThirdParty.md).
