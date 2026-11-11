# Weapons and payloads

The package supplies vehicle-mounted aiming, shot admission, recoil, rockets and payload release. The application supplies input/selection, ammunition rules, targets, scoring and replenishment. Set up one working action before adding a full effect sequence.

## Inspector quick start: one mounted barrel

1. Outside Play Mode, create the mount/yaw and elevation pivots under the vehicle. Configure their **Moving Part** helpers first, following [Moving parts](MovingParts.md).
2. Add **Weapon Barrel** on the appropriate vehicle-owned object through Add Component or **Modules > Add module...**. Drag the aiming helper into **Movement**. Create a muzzle child at the barrel tip with local +Z along the shot and assign **Muzzle**.
3. Assign **ProjectileDemo Prefab** to a prefab component implementing IWeaponProjectile, then set **Firing Enabled**, **Fire Mode**, **Shots Per Second**, speed and lifetime. A plain mesh prefab without that behavior cannot become a working projectile through the reference alone.
4. Configure the associated **Weapon Effects** and **Weapon Recoil** references/outputs only after the barrel is ready. Discover modules, apply/save, and test one shot using the demo/application firing route.
5. Follow the rocket/drop sections for mounted stores instead of using this projectile field for every payload. Input, hit behavior and ammunition rules remain application responsibilities; this Inspector setup does not create them automatically.

## Choose the operation

| Component | Use |
| --- | --- |
| MovingPart | A constrained yaw/elevation axis |
| WeaponBarrel | ProjectileDemo-prefab shot, cadence and trigger policy |
| IWeaponProjectile | Application projectile initialization contract |
| WeaponEffects / WeaponRecoil | Presentation and optional physical response to confirmed barrel fire |
| RocketLauncher + mounted Rocket stores | Sequential launch of available stores |
| ObjectDropper + DroppableObject | Release a specifically selected mounted payload |

Geometry/axis configuration belongs to [Moving parts](MovingParts.md). This page connects that movement to weapon operation and action-specific presentation; [Particles](Particles.md) and [Audio](Audio.md) cover shared effect authoring.

## Set up a barrel

### Aim and muzzle geometry

1. Create a yaw pivot under the vehicle and a separate elevation pivot beneath it.
2. Configure one MovingPart per needed axis, including independent hinge references, limits, neutral forward direction and movement speed.
3. Add/register `WeaponBarrel` and assign **Movement** to its elevation/aiming helper. Configure yaw through its own MovingPart.
4. Create **Muzzle** at the exit point, with local +Z along the shot direction, and assign it.
5. Put cosmetic barrel recoil on a suitable child so aiming and recoil do not both overwrite the same Transform.
6. Use Scene gizmos to verify limits and muzzle direction before spawning projectiles.

Use `SetMovementInput`, `SetAimAngle`, `AimAt(point/Transform)` and `StopAiming` through the supported movement path. AimAt points the allowed axis toward the supplied location; it is not an automatic ballistic lead/trajectory solver. Supply an application-compensated aim point for projectile drop or a moving target.

### ProjectileDemo prefab

Assign a prefab component implementing `IWeaponProjectile` to **ProjectileDemo Prefab**. A GameObject/Rigidbody alone is not that contract. The [complete custom projectile example](Scripting/Weapons.md#a-minimal-custom-projectile) shows initialization and an application collision/lifetime implementation.

Set **Muzzle Speed** in m/s, **Impact Impulse**, **ProjectileDemo Lifetime** and **Inherit Vehicle Velocity**. Barrel fire instantiates the component at the muzzle, supplies owner/velocity/impulse/lifetime/ignored-collider data and raises Fired. Your projectile implementation must actually use those values; the interface does not automatically create every collision/damage rule.

Inherited motion uses the carrier's velocity at the muzzle, so a turning/moving vehicle can affect launch velocity. **RefreshCollisionFilter()** updates cached owning colliders after structural changes. A custom projectile must honor the supplied filtering if it should not hit its own vehicle immediately.

## Firing admission and trigger modes

Set **Firing Enabled**, **Fire Mode** and **Shots Per Second**. For example, 0.5 shots/second is a two-second interval; this field is a rate, not seconds between shots.

`TryFire()` attempts one shot and returns false when prerequisites/cooldown prevent it. `SetTrigger(true/false)` represents held input under the selected Single/Automatic policy; send false on input release and interruption. A rejected request is not a built-in ammunition/input queue.

`CanFire`, `ReloadRemaining` and `TriggerHeld` support UI. The barrel requires an enabled owner, valid muzzle and compatible projectile prefab. Disabling/disarming clears retained trigger state so re-enabling should not resume an old press.

Use Fired for confirmed shot presentation and application ammunition accounting. Do not decrement ammunition from both input-down and Fired unless those are intentionally separate rules. There is no implicit magazine/reload inventory supplied by the barrel's interval timer.

## Shot effects and recoil

Adding WeaponBarrel also requires WeaponEffects and WeaponRecoil; configure their **Weapon** reference and the intended outputs.

### WeaponEffects

Assign **Shot Sound**/optional Audio Source, volume, pitch range, spatial blend and distances. Configure **Muzzle Flash Prefab**, **Muzzle Effect Prefab**, effect scale and lifetimes for flash/smoke. Play Audio, Emit Smoke and Spawn Muzzle Flash can be switched independently.

The component observes confirmed fire; a blocked/cooldown request should not spawn a successful-shot effect. Match effect orientation to the muzzle and check cleanup duration. A supplied audio source is a different ownership choice from the component's generated source.

### WeaponRecoil

Assign a cosmetic **Barrel** child, **Local Recoil Axis**, **Barrel Travel**, **Kick Duration** and **Return Duration**. Travel is world metres with imported scale accounted for. Keep that child separate from the aiming pivot.

**Animate Barrel** and **Apply Body Impulse** are independent. Body Impulse and muzzle-frame Angular Impulse produce a physical vehicle response; suspension movement follows physics rather than a scripted chassis pose. A heavier vehicle can respond differently to the same impulse. Test visual-only and physical-only response separately before combining them.

## Set up rockets

1. Put `Rocket` on each mounted store with its visual geometry and suitable collision shape.
2. Set **Launch Direction** (+Z), Mass, Launch Speed, motor Acceleration, Burn Seconds, Lifetime and gravity policy.
3. Configure inherited vehicle velocity and collision/detonation policy.
4. Add/register `RocketLauncher`, assign **Rockets** in the intended launch order, set **Fire Interval** in seconds and choose **Automatic** for held repeated launches (off means one launch per new trigger press).
5. Configure the rocket's exhaust anchor/prefab, engine loop, launch/explosion sound and explosion prefab.
6. Test one store before testing a complete rack and held automatic fire.

`TryFire()` selects the next available mounted store. The Rocket launch path creates an independent flying copy and deactivates the mounted source after success; do not treat the mounted source and returned flying instance as the same lifetime object. Remaining/CanFire describe available stores/admission, not a full application rearm system.

The base rocket flies without target guidance. Motor burn duration and total lifetime are separate. `StopMotor()` ends thrust/exhaust/engine loop without itself being a request to delete the projectile. Lifetime expiry follows its detonation path.

### Rocket impact and explosion

**Detonate On Collision** controls automatic contact detonation; explicit `Detonate(point)` is still available for a launched rocket. Detonation is guarded so it does not repeatedly emit an explosion for the same instance.

**Apply Explosion Force**, Explosion Radius/Impulse/Mask and Upward Modifier govern physical impulse. Effects and Exploded notification are independent of that force switch. The impulse does not automatically implement application health/armor/scoring; connect the appropriate damage rule once.

The exhaust anchor's +Z points out of the nozzle, opposite the usual forward launch direction. Check it separately from Launch Direction. The [rocket contract](Scripting/Weapons.md#rocket-and-presentation-ownership) describes copy ownership, filtering and presentation cleanup.

## Drop an object

1. Add `DroppableObject` to the root of a mounted payload, with its meshes/colliders below it.
2. Keep it as one intended rigid group and set Mass, **Inherit Velocity** and optional **Local Release Velocity** in m/s.
3. Add/register `ObjectDropper` on the vehicle, enable dropping and set **Drop Interval**.
4. Call `TryDrop(payload)` with the specific object selected by the application.
5. Observe Dropped, then handle landing/impact behavior, cleanup and replenishment in application code.

This releases the actual mounted object, unlike a barrel projectile or flying rocket copy. Its world pose is preserved and its independent Rigidbody receives the configured inherited/separation motion. The module validates that it belongs to this vehicle and has not already been dropped.

ObjectDropper does not choose an inventory slot. `CanDrop` and `CooldownRemaining` describe admission; a true request releases the selected object. A dropped payload does not automatically explode, damage something or return to its rack. See the [selected-payload example](Scripting/Weapons.md#drop-a-selected-object).

## Extend and inspect

Derive appropriate components or implement IWeaponProjectile for another behavior. Keep projectile physics/collision ownership separate from action effects and application inventory. A pooled projectile must reset all its own subscriptions, ignored contacts, timers and effects; the interface alone is not a complete pooling implementation.

Use the Scene trajectory/axis gizmos as setup aids, then test actual flight/collision at representative speeds. Inspect a fresh vehicle instance after saving changes so mounted references and muzzle hierarchy are not accidental Play Mode edits.

## Diagnose a setup

| Symptom | Check |
| --- | --- |
| TryFire always false | Owner/module state, muzzle, compatible prefab and cooldown |
| Aiming works but projectile goes sideways | Muzzle +Z versus visible barrel axis |
| Shot hits its own vehicle | ProjectileDemo honors supplied ignored colliders; refresh filter after changes |
| Recoil jitters against aim | Same Transform assigned to two motion owners |
| Rocket source disappears/duplicates unexpectedly | Mounted-source versus flying-copy lifetime policy |
| Rocket burns visually but does not guide | Base rocket has no target guidance |
| Explosion effect appears without health loss | Physical impulse/effects do not implement application health automatically |
| Payload release button does nothing | Correct selected object, ownership, enabled dropper and cooldown |

For exact actions/events and implementations, see [Weapon scripting](Scripting/Weapons.md) and [API](API/Weapons.md).
