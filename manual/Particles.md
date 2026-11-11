# Vehicle particles

Particle modules turn resolved vehicle state/contact feedback into presentation. They do not supply tire grip, exhaust thrust or projectile damage. Establish the mechanic first, then tune its effect at representative speeds and camera distances.

Vehicle creation fills missing bundled presets/materials from `Resources/Effects`; importing the Demo sample is not required for those resources. Custom assets are supplied by your project. Shared surface classification belongs to [Surfaces](Surfaces.md), while this page owns emitter/output configuration.

## Inspector quick start: add an exhaust outlet

1. Select the vehicle root outside Play Mode and open **Vehicle Controller > Effects**. Expand **Exhaust Smoke**, or add it through **Modules > Add module...**. Assign **Vehicle** and **Engine** if they are not resolved by configuration.
2. In the Hierarchy, create an empty child at the exhaust tip and orient its local +Z outward. Add one child per outlet. Under **Exhaust Points**, press **+** for each and drag these Transforms into the list; the package does not locate exhaust pipes by mesh name.
3. Choose one output path: assign a **Particle Prefab** from the Project window, allow **Create Default Particles** to use the bundled path, or fill **Particles** with existing ParticleSystem components matching the outlets. Start with one outlet/output before duplicating it.
4. Set **Idle Rate**, **Loaded Rate** and **Response**. For supplied custom systems, decide whether **Animate Custom Particles** may alter their appearance. Check material compatibility and ParticleSystem lifetime/size in the effect asset as well as the vehicle's emission rate.
5. Apply vehicle configuration, save, and enter Play Mode. Start/stop the engine and apply throttle. Check direction and emission first, then tune density. A stopped engine or unsupported drive-profile presentation can deliberately suppress exhaust.

### Inspector quick start: tire smoke and jets

1. For tires, install **Tire Feedback** and **Tire Smoke** on the vehicle, open them in **Effects**, and assign the Tire Feedback reference. Use working Wheel Setup/contact before testing smoke.
2. Assign the tire particle prefab/default materials. If supplying **Wheel Particles** explicitly, add one output in each configured wheel slot; otherwise use the generated-output path. Perform a supported skid and then a rolling pass on a configured loose surface.
3. For nozzles/rotors, add **Propulsion Jets** and assign Vehicle/Engine plus **Hover Points** or **Aircraft Points**. Create/drag the outlet Transforms as for exhaust and configure the generated design or Particle Prefab. The active profile selects the relevant points.
4. For wakes/splashes use **Boat Water Particles** and the [water setup](Water.md#add-audio-and-particles). Ordinary ParticleSystem playback alone is not a connection to engine, tire or water activity.

## Choose the effect and its data

| Module | Reads | Configure here |
| --- | --- | --- |
| TireSmoke | TireFeedback wheel contact/slip and selected surface | Per-wheel output, rate/smoothing, smoke/loose-ground presentation |
| ExhaustSmoke | Running engine, load/RPM activity and profile | Outlet geometry, idle/load emission and custom appearance ownership |
| PropulsionJets | Selected movement family and engine/spool activity | Hover/aircraft outlets and visual jet settings |
| BoatWaterParticles | Water/motion state | Water emitter locations and wake/spray response; see boat setup |
| WeaponEffects / Rocket | Confirmed shot or projectile flight | Weapon-specific effect lifecycle in [Weapons](Weapons.md) |

Add/register the intended module and assign references explicitly when a manually added/child component cannot resolve the expected local vehicle/core. A particle module with no activity source should not be diagnosed first as a bad material.

## Tire smoke and loose ground

1. Add `TireFeedback` and `TireSmoke` to the vehicle and assign **TireFeedback**.
2. Use the supplied Tire Smoke prefab/Smoke and Tire Sand materials or choose your own compatible assets.
3. For explicit scene systems, fill **Wheel Particles** in configured wheel order. Otherwise allow the module to create outputs from its prefab/default path.
4. Set **Maximum Rate**, **Minimum Intensity** and **Emission Response**.
5. Test a supported skid, a rolling pass, wheel lift and a transition between surfaces.

Maximum Rate is particles/second at the upper activity range. Minimum Intensity is the activity gate; it is not a wheel-speed threshold. Emission Response smooths density changes, with zero following the resolved activity immediately. `CurrentIntensity` and `GetWheelParticles(index)` help identify the current selected output.

Use [TireSurfaceProfile](Surfaces.md#rolling-activity-versus-skid-activity) for rolling dust, granular particles, color/material/lifetime and enabled flags. That classification can select loose-ground presentation without changing physical grip. Custom systems/prefabs retain their authored design according to the module's custom path; do not expect every built-in smoke/sand parameter to redesign an arbitrary prefab.

When feedback/contact becomes unavailable, emission is stopped rather than preserving an old skid forever. Existing particles may still finish their lifetime. Disabling emission is different from immediately clearing every particle in a supplied system.

### Standing burnout

Under **Tire Smoke > Standing Burnout**, leave **Smoke Mode** on Automatic to detect strong wheelspin at low road-relative speed. **Burnout Smoke** sets thresholds, buildup, rate, lifetime and size. A separate world-space emitter builds a cloud around the tire circumference, gradually replacing contact-patch emission; existing particles fade naturally. Locked/airborne wheels, granular surfaces and disabled surface particles do not qualify.

Choose Contact Patch for ordinary smoke or Tire Ring to request the cloud while the grounded tire has particle activity. Custom skid systems keep their appearance. Runtime switching and notifications are covered in [Particle ownership](Scripting/Presentation.md#particle-ownership).

## Exhaust

1. Add `ExhaustSmoke` and assign **Vehicle** and **Engine**.
2. Create **Exhaust Points** under the model's outlets and fill that array. Local +Z points out along the emission direction.
3. Use the supplied Exhaust Smoke prefab/material, provide a custom prefab, or assign matching **Particles** systems for the outlets.
4. Configure **Idle Rate**, **Loaded Rate**, **Intensity Multiplier** and **Response**.
5. For Nitro, assign **Nitro Particle Prefab** (the Demo flame is assigned by default when imported) and tune **Nitro Intensity**, **Nitro Rpm Influence** and **Nitro Response**. Flames use the same Exhaust Points and modulate emission, speed and size with RPM. Clear the prefab to disable them.
6. Test ignition, load changes, Nitro activation/release and engine stop from driver and external views.

The package cannot infer pipe positions from a mesh. Use independent outlet Transforms rather than rotating the entire exhaust mesh to fix a ParticleSystem direction. The module follows outlet pose while computing activity from engine behavior.

Ordinary exhaust is suppressed for hover/airplane-family profile presentation. Use the appropriate propulsion outlets for those modes instead of increasing ExhaustSmoke rate to fight the profile condition.

### Custom-system ownership

**Animate Custom Particles** permits the module to change custom output appearance such as speed, size and tint. With it off, a supplied design retains its appearance while the module controls its emission/outlet pose. Check this flag when a custom prefab changes unexpectedly during acceleration.

Repeated vehicle setup fills missing defaults without replacing your supplied custom material/prefab references. **Create Default Particles** controls automatic creation from the available default path; it does not remove application-owned systems already assigned.

## Propulsion jets

Add `PropulsionJets` and assign **Vehicle**, **Engine**, **Hover Points** and **Aircraft Points** as appropriate. The active profile selects the matching outlet set. Position/orient each point on the actual nozzle; keep those points with the moving nozzle geometry where applicable.

Set **Idle Rate**, **Loaded Rate**, **Jet Speed**, **Color** and **Default Material** for generated output, or supply a **Particle Prefab** for another design. **Jets Enabled**/`SetJetsEnabled` is a runtime visual switch; it does not turn engine thrust on/off.

**Follow Propulsion Spool** scales presentation by the associated Propulsion state. Check that module/reference and its spool when emission remains low after ignition. A missing spool source should not be compensated with an extreme loaded rate. Custom-prefab appearance follows its supported path rather than being assumed identical to the generated preset.

Visible propeller/rotor meshes belong to `Propulsion.propellers`, not to jet particles. Their setup is in [Aircraft](Aircraft.md); changing a particle speed is not a flight-performance adjustment.

## Water and one-shot effects

Configure hull/water activity through [Boat](Boat.md), [Water](Water.md) and the relevant water-particle component. Do not generate road-tire dust to represent a hull wake. Surface-ground classification and water-provider queries have different owners.

For muzzle/explosion effects, use [Weapons](Weapons.md), which describes the confirmed action and cleanup boundary. Connect any additional gameplay effect once at that boundary rather than separately from both input and action completion.

For material-specific impact prefabs, use [Damage impact effects](Damage.md#pooled-particles-and-custom-effects).

## Budgets, pooling and reuse

Estimate cost from active emitter count, emission rate and particle lifetime. A maximum of 100 particles/second with a two-second lifetime can maintain roughly 200 particles per continuously active emitter before other limits apply; multiplying that across every wheel/vehicle matters more than one close-up test.

Use sensible prefab maximum-particle limits, lifetime and material/render settings. Test several vehicles and loose-ground activity, not only a single skid. Generated outputs are owned/cleaned by their module; assigned external assets/systems have different ownership. Avoid creating another output on every sample in application code.

On reuse/rebinding, check that emission follows the new activity source and that old generated hosts are not duplicated. A visible lingering particle is not necessarily a stale emission request: inspect rate versus existing particle lifetime.

## Troubleshoot

| Symptom | Check |
| --- | --- |
| Tire effect never starts | TireFeedback, supported contact/slip, minimum intensity and enabled output |
| Dust appears while simply rolling | Intentional surface rolling activity |
| Effect is on the wrong wheel | Explicit array order versus configured Wheels |
| Exhaust points the wrong way | Outlet +Z and custom prefab orientation |
| Supplied prefab changes appearance | Animate Custom Particles and selected built-in/custom path |
| Jets show in the wrong movement mode | Profile and correct outlet array |
| Particles remain after stop | Existing lifetime versus a nonzero stale emission rate |
| Many vehicles become expensive | Emitter count, rate/lifetime, capacity and transparent overdraw |

For allocation, generated-system ownership and update contracts, see [Presentation scripting](Scripting/Presentation.md) and [API](API/Presentation.md). Bundled asset locations are listed in [Demo resources](DemoResources.md).

## Jet Blast

**Jet Blast** is an optional physical effect, separate from exhaust particles. Add it to the vehicle root through **Add Component > Ultra Vehicle System > Effects > Jet Blast** or the matching **Tools > Ultra Vehicle System > Add Component** menu, then apply vehicle configuration.

Assign **Outlets** at the exhaust tips with local **+Z pointing out of the engine**. **Maximum Range**, **Start Radius** and **End Radius** define the plume. **Maximum Force** sets newtons per outlet at full power; **Idle Strength** sets the running-idle fraction: the default **0.12** emits 12% of Maximum Force even at zero throttle. Set it to zero to disable idle blast. Both values can be adjusted in the component Inspector. **Force Multiplier** scales both idle and full-power exhaust. Throttle and engine spool scale the force. A stopped engine produces no blast. Heavy bodies accelerate less, and force decreases towards the edge and end of the plume.

**Activation** selects **Engine Running** (including idle, regardless of which vehicle is selected) or **Throttle Only**. In Throttle Only mode, **Minimum Throttle** sets the activation threshold. The demo uses Engine Running. Its wider plume reaches low vehicles underneath the elevated exhaust outlet; use the selected range gizmos to check the actual occupied volume.

**Affected Layers** selects targets; triggers, the emitting vehicle and its attached children are ignored. Compound targets receive one force per outlet. **Contact Capacity** reserves the query buffer at startup; increase it for crowded scenes. Disable the component to disable the effect. **Show Gizmos** previews the range when selected. This effect samples the plume volume; solid obstacles do not occlude it.

From code, read `JetBlast.Strength` and subscribe to `BodyPushed(Rigidbody, Vector3)` to observe the body and force in newtons. Use the inherited `SetEnabled(bool)` to switch the effect. The demo Jet supplies a configured example; automatic Jet setup leaves it optional.
