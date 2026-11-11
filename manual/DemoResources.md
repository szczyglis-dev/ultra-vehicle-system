# Supplied visual resources

Import Demo to use the example scene's models, materials, animations and vehicle prefabs. Reusable particle effects, materials and water styles are supplied directly with the package. Demo paths below are relative to `Assets/Szczyglis/UltraVehicleSystem/Demo`; package defaults are available without importing the sample. Resources folders are asset locations; assign the required references on the receiving component.

| Resource location | Contents / use |
| --- | --- |
| `Prefabs/Weapons` | Example shell projectile using the Demo projectile behavior and package materials |
| `Art` | Vehicle and passenger models, vehicle textures, asphalt and desert terrain textures |
| `Resources/UVSAccess` | Idle animation, standing Animator controllers and left/right passenger access profiles; see [Passenger access](PassengerAccess.md) |
| `Resources/Effects/Jet` in the package | Jet exhaust prefab, flame and shock-diamond materials/textures for `PropulsionJets` |
| `Resources/Effects/Water` in the package | Water style, surface and particle shaders, spray/foam materials and ripple texture for `WaterSurface` and boat effects |
| `Resources/Effects/Weapons` in the package | Muzzle flash/smoke and rocket exhaust prefabs, with their materials |
| `Resources/Effects` in the package | Exhaust and tire smoke prefabs, smoke/skid/sand materials |
| `Resources/Effects/Damage` in the package | Shared material impact profiles for audio and visual responses |
| `Resources/Effects/Damage` in the package | Metal sparks, glass chips, plastic dust and rubber dust prefabs using the shared smoke material |
| `Resources/Effects/Nitro` in the package | Nitro flame prefab and material |

You can replace these with compatible assets. Check material/pipeline support, particle scale/lifetime and owned cleanup before saving a prefab. New effect components receive package defaults during authoring; existing custom references are preserved. Clear or replace optional references to customize the effect.

For audio defaults and clip assignment use [Audio](Audio.md); for attribution see [Third-party credits](ThirdParty.md).
