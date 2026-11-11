# Add vehicle sound

See [Crash, contact and landing effects](DamageFeedback.md) for configurable impact layers, scraping, glass breakage, suspension cues and pooled particles.

`Audio` supplies common mixer/spatial settings. `Engine Audio` contains a list of independent sound items: use one for a car engine, four for a quadcopter's rotors, or several layers/engines on the same vehicle. Each item can use a shared Engine Sound Profile or just its own clip override.

Registered sources reuse static spatial/routing settings. After editing mixer, distances, rolloff, spatial blend, Doppler, spread or priority in Play Mode, call `VehicleAudioSettings.RefreshConfiguration()` for that block or `Audio.RefreshPlaybackConfiguration()` for the core. Dynamic volume/pitch and contexts remain live. See [runtime spatial settings](Scripting/Audio.md#changing-spatial-audio-settings).

## Mechanism audio receivers

**Nitro Audio**, **Moving Part Audio**, **Wipers Audio** and **Profile Transition Audio** receive notifications from their assigned mechanism. They inherit `AudioModule` and appear under **Effects → Audio**, including channels on child parts. The owning Audio core controls their mute, master volume, pitch and mixer fallback. They can be disabled or removed without stopping vehicle mechanics. Configure boost clips on Nitro Audio, motion cues on Moving Part Audio, and shared/per-wiper recordings on Wipers Audio. Create Vehicle and the package authoring menus add the appropriate receivers. Configure transition recordings under Profile Transition Audio → Sounds; each entry references its transition component.

## Inspector quick start: one working engine loop

1. Select the vehicle root outside Play Mode and open **Vehicle Controller > Effects**. Expand **Audio**, then its nested **Engine Audio** module. Existing vehicle presets normally supply these; if missing, open **Modules > Add module...** and add Audio/Engine Audio. Audio submodules can be on the core object or its child parts; nested vehicles and nested audio cores keep separate ownership.
2. Assign the core's **Vehicle** and **Engine** where needed. Ensure there is one active AudioListener in the viewing setup. In the Project window import/select a seamless looping AudioClip; test the recording itself before adjusting vehicle response.
3. In Engine Audio, expand **Items**, press **+**, give the item a unique **Id** such as `engine`, and enable **Active**. For the smallest setup, assign the clip to **Loop Override**. For a reusable setup, create **Assets > Create > UltraVehicleSystem > Audio > Engine Sound Profile**, assign its loop and drag the asset into **Sound Profile**.
4. Create an empty child at the engine position and assign it to the item's **Audio Settings > Audio Anchor**. Set volume, pitch response, spatial blend and distances in the appropriate settings groups. Start with audible conservative gains and an observer inside the maximum distance.
5. Press **Apply vehicle configuration**, save, then enter Play Mode. Start the engine and change RPM. Confirm the loop stops/starts correctly before layering start/stop clips, several engines or rotor items.
6. For a horn or indicator relay, add **Horn Audio** or **Indicator Audio** through the module menu. Expand it under Audio, assign its mechanic/clip settings, and test the actual horn request or indicator phase. Adding an AudioSource alone does not connect it to vehicle mechanics.

### Inspector quick start: collision and landing sounds

1. Expand **Audio > Damage Audio**. Default vehicle setups include this channel. Physical crash response remains on Collisions; wheel touchdown detection remains on Suspension.
2. Configure **Collision Sound** for contacts without a matching material profile, and **Landing Sound** for wheel touchdowns. Assign Clips and each sound's Audio Settings: gain, pitch, cooldown, emitter and distance.
3. Set **Minimum Collision Speed** and **Full Collision Speed** on Damage Audio independently of damage thresholds. Material impact profiles select and scale collision recordings when they match.
4. Apply/save and test a gentle collision and a wheel landing. Damage Audio subscribes directly to VehicleController.Impacted and Suspension.Landed; neither Events nor Event Audio is required.


## Shared Audio Settings

Sound-producing components, event mappings and reusable sound profiles expose **Audio Settings** using the same serialized `UltraVehicleSystem.VehicleAudioSettings` class. The clip or clip list belongs to its sound entry; the settings group contains playback enable, source, **Audio Anchor**, mixer output, volume, fixed/random/dynamic pitch parameters, cooldown, smoothing and spatial attenuation. Multiple sounds with independent roles have separate groups, such as opening/completion cues, engine start/stop, water lapping/wake/splash or commercial brake/reverse sounds.

A dedicated **Source** is used by single-emitter systems. Otherwise **Audio Anchor** selects an emitter, reusing a source on that transform or creating an owned child source. An empty anchor uses the mechanism's transform. Generated sources are runtime state owned by each emitter; Audio Settings is not mutated to store them. Multiple owners can reuse one settings instance and create independent voices. Generated sources are cleaned up by their owning component; supplied sources are retained. Pooled tire, braking, water-entry and damage responses create independent voices under their configured emitter instead of sharing a single source between simultaneous sounds. Dynamic position consumers place unanchored voices at contact/impact points.

Engine items and profiles have separate loop, start and stop settings. Mix, profile-gain and ignition-gain groups multiply the selected recording's gain. React To Pitch selects engine response or the item's fixed Audio Settings Pitch. Engine item IDs and trigger semantics belong to `EngineAudio`; clips and reusable profiles are configured on the item.

The `Audio` core’s **Volume**, **Pitch** and **Enabled** control the channel mix. Individual loop groups control their own smoothing response. Recording profiles supply the relevant clip gain and pitch mapping; pooled channels use their component settings for voice ownership and routing.

For custom code, `ApplyTo` configures mixer/spatial properties without changing playback state or the consumer's dynamic gain/pitch. `RandomPitch` and `PitchAt` evaluate pitch. `ResolveSource` reports whether it created a source; release only sources you own. Use fully qualified `UltraVehicleSystem.VehicleAudioSettings` when importing `UnityEngine`, which also defines a type named `VehicleAudioSettings`. See the [API](API/Audio.md#vehicleaudiosettings) and [Inspector fields](InspectorReference/Effects.md#vehicleaudiosettings).

## Camera, area and medium profiles

Configure **Audio > Context > Profiles** to vary any channel without duplicating its base setup. **Add interior engine** and **Add underwater** create editable starting points; each profile has its own **Enabled** switch. Empty profiles preserve ordinary audio.

1. Choose **Channel**, or leave it empty for the whole vehicle. Match **View**, an exact **Camera**/**Camera Module**, **Area**, **Medium**, or a combination. Every assigned condition must match. Area accepts a Box, Sphere, Capsule or convex Mesh collider, including triggers.
2. Choose **Sample Point**: Listener tests the camera position; Vehicle tests the vehicle position. Assign **Context > Water Provider** for sampled water, including waves; otherwise the vehicle's Water Interaction/profile supplies water when available. **Underwater Depth** sets the water threshold.
3. Set volume/pitch multipliers, mute, low-pass filtering or spatial blend. Assign **Output** to a mixer group for additional EQ, reverb or other effects. In **Clip Replacements**, map an original recording to variants; an enabled empty replacement list silences it. Loops keep a stable variant and retain normalized playback position when recordings change.

Profile definitions are prepared when the vehicle audio is configured. During play, toggle an existing profile's **Enabled** switch; camera, area and medium conditions keep selecting profiles automatically. After changing profile parameters, replacing the list or adding profiles from code, call `audio.RefreshAudioProfiles()`. `audio.RefreshPlaybackConfiguration()` also refreshes these definitions. See the [runtime example](Scripting/Audio.md#listening-context).

Matching profiles combine in list order: volume/pitch multiply, the lowest cutoff wins, and the last matching mixer, spatial or clip override wins. For example, an interior-engine profile and a Water profile can apply together. **Transition Seconds** blends levels/filtering; shared sound settings and mixer assets stay unchanged. Camera detection follows the active vehicle view, then Camera.main; external controllers and custom media use the [context API](Scripting/Audio.md#listening-context).

Context gain, pitch and routing are applied from separate channel baselines. Active low-pass filters stay connected between frames; engine tone and context filtering compose without repeatedly bypassing the filter. Leaving a profile restores the authored settings through the configured transition.

Demo vehicles include editable interior and underwater audio profiles where applicable. Adjust attenuation and low-pass filtering under **Vehicle Controller > Effects > Audio > Context > Profiles**. The **Add interior engine** and **Add underwater** shortcuts create starting profiles; compare them from an interior camera and below the water surface.

## 1. Prepare the audio components

1. Add **Audio** and **Engine Audio** on the vehicle root through **Effects → Audio** or the package's Add Component menu.
2. Connect **Engine Audio > Engine** to the engine mechanic and register the audio modules with `VehicleController`. Add Vehicle presets do this for you.
3. Set the common mixer **Output**, **Spatial Blend** and distance range on `Audio`. The scene needs an `AudioListener`.
4. Open **Vehicle Controller → Effects → Audio → Engine Audio → Items**. Each list entry is a separate source configuration.

## 2. Create an Engine Sound Profile

Create **Assets → Create → UltraVehicleSystem → Audio → Engine Sound Profile**. Assign a seamless Loop and configure Volume/Pitch Range under Audio Settings. Optional Start Clip/Stop Clip have separate Start Audio Settings and Stop Audio Settings groups.

| Pitch Mode | Behavior |
| --- | --- |
| Rpm | Maps normalized engine RPM to pitch. Use Engine Response enables the item's detailed RPM reference/exponent, shifting and load-tone behavior when that item's switch is also enabled. |
| Constant | Uses the first Pitch Range value. Spool can still vary pitch during spin-up/down unless the item disables pitch response. |
| Motion | Uses forward/vertical vehicle speed relative to the profile's reference speeds. |

Shared profiles contain asset references and sound behavior, not scene anchors. Duplicate an asset to tune its recording/settings independently. Changing a shared profile affects every item that references it.

## 3. Configure independent items

1. Set **ID** at the top of each entry. Use unique, non-empty names such as `Engine`, `Rotor1` or `RearEngine`; these are the IDs used by the API.
2. **Active** enables only this item. Disabling stops its loop and ignition; other items continue playing.
3. Assign **Sound Profile**, or assign **Loop Override** alone. Loop Override replaces a profile's recording while retaining its response settings; without a profile it uses this item's loop settings.
4. Assign **Audio Settings → Audio Anchor** to a `Transform`/empty `GameObject` at the engine or rotor. Unanchored ignition cues inherit the item origin; Start/Stop Audio Settings can select independent emitters. Empty uses the `Audio` core origin. `SetItemAnchor` moves generated sources using the item origin without restarting playback.
5. Leave the item's **Engine** and **Propulsion** overrides empty to follow the Engine Audio channel's engine and the vehicle spool, or assign independent references for a particular engine/rotor.
6. Balance **Profile Audio Settings → Volume** for profile loop gain, **Ignition Audio Settings → Volume** for start/stop gain and **Mix Audio Settings → Volume** for the whole item. No global engine-item tuning is required.

For four rotors, add four entries referencing the desired profile(s), assign four anchors and reduce their individual gains to balance the combined level. The demo drone has `Rotor1` through `Rotor4`, each at its corresponding rotor, sharing the total loop gain equally. Sources/filter state remain independent even when profiles are shared.

### Response switches

- **React To Pitch:** enable RPM/motion/spool pitch response. Disable to hold **Fixed Pitch** exactly.
- **React To Engine Activity:** enable activity-based volume and load tone. Disable for constant activity gain; spool may still scale the volume.
- **Follow Propulsion Spool:** follow rotor/propeller spin-up/down. Disable to gate the item directly by its engine running state and ordinary start delay.
- **Use Engine Response:** allow detailed RPM mapping, reference RPM, exponent, load tone and shift response. A profile must also enable its corresponding switch.

Without a profile, the item supplies Audio Settings Volume, Pitch Mode, Audio Settings Pitch Range and the detailed RPM or motion reference settings. With a profile, its loop volume/pitch mapping is used instead. Other audio channels, such as tire and water sounds, remain independent.

## 4. Switch sounds by ID

Use `engineAudio.SelectItem("Hover")` to enable only that item and stop the others. `engineAudio.SelectItem("Drive")` selects the drive sound again. A missing or duplicate ID returns false without changing the current selection.

Use `SetItemActive(id, true/false)` when several sounds should remain independently enabled, such as four rotors. Engine Audio has no drive-mode filters or dependency on `ProfileSwitcher`.

The demo Porsche's items are named `Drive` and `Hover`. Its Demo Engine Audio Mode helper listens to `ProfileSwitcher.ProfileChanged` and selects the sound using the current slot ID. This connection belongs to the demo; other projects can call the same API from their own vehicle/controller code. Selection does not replay ignition.

### Audio source gizmos

Audio guides appear only while the vehicle or its audio component is selected.

Expand **Gizmos** on Engine Audio to toggle markers, ID labels and anchor connections separately. Sources use yellow spheres at their anchor/origin, visible before entering Play Mode; inactive items use muted wire spheres. During playback the markers follow actual generated sources. **Gizmo Size** sets the marker radius in metres.

## 5. Configure ignition

Assign Start Clip, Stop Clip and their volumes in the shared sound profile. An item uses those when present, falling back to its local Engine Start Clip/Engine Stop Clip otherwise. **Override Ignition Clips** explicitly selects the local pair, including silence for an empty clip. **Play Ignition Sounds** can disable transitions for one item.

Each item's Engine Loop Start Delay applies to actual engine-start transitions for ordinary loops. Already-running vehicles do not synthesize a start; spool-driven sources follow propulsion instead. Item activation and sound selection also do not synthesize start sounds.

## Runtime control

Use `EngineAudio.GetItem(id)`/`TryGetItem` to edit settings, `SelectItem`, `SetItemActive`, `SetItemProfile` and `SetItemAnchor` for targeted changes, and `AddItem`/`RemoveItem` for structural changes. `GetLoopSource`, `GetIgnitionSource` and `TryGetState` expose each item's playback. See [Audio scripting](Scripting/Audio.md#independent-engine-sounds) for a complete example and [the API](API/Audio.md#engineaudio) for return values and lookup rules.

## Tire and contact sound profiles

Engine Sound Profiles do not configure tire noise. For road, gravel or other ground sounds, create a **Tire Surface Profile**, assign its tire loop and rolling activity settings, then assign it through a **Tire Surface** on the ground collider or a parent. Set `TireFeedback`'s Default Surface for ground without an explicit mapping. See [Surface setup](Surfaces.md) for the complete assignment process.

`TireAudio` uses rolling/slip feedback; Brake Audio uses the surface's **Braking Loop**. **Use Default Tire Loop When Empty** and **Use Default Brake Loop When Empty** independently choose fallback clips or silence. **Brake Audio Multiplier** scales braking sound. Multiple contacted surfaces are mixed, with identical recordings sharing one voice. Other sound types keep their own channels; see [Audio scripting](Scripting/Audio.md) for custom playback.

## Add the remaining channels

The `Audio` core dispatches playback channels and provides defaults for custom sources; built-in sounds expose their own Audio Settings groups. Keep core-managed channels on the same `GameObject` as the core. Verify the referenced mechanic/event source before tuning volume.

| Channel/system | Configure and test |
| --- | --- |
| `TireAudio` | `TireFeedback` source and surface loop behavior; test rolling and a skid |
| `BrakeAudio` | Resolved braking feedback and its clips; test threshold crossings and release |
| `IndicatorAudio` | Lights phase and relay clips/default-click policy |
| `SwitchAudio` | Assigned `SwitchAnimator` and settled-position click feedback |
| `EventAudio` | User-defined event-to-sound mappings; test each exact application ID |
| `BoatWaterAudio` | Water/motion activity for the configured boat |
| `DamageAudio` | Accepted damage/part response through the dedicated components |
| Weapon audio | Confirmed shot/rocket presentation; see Weapons |

Assign compatible clips and output routing per channel. A surface-selected tire loop is independent of Engine Sound Profile selection. A control switch's click is also independent of its mechanic action: it should not request another action merely because sound played.

### Event and switch sounds

Use `Events` and `EventAudio` for application-defined sound triggers. Assign the hub on Event Audio, add an Event Sounds entry such as `ApplicationAlert`, and publish that exact string through `Events.Publish`. New custom mapping lists are empty; vehicle mechanics do not publish string IDs.

`SwitchAudio` follows the handle's settled switch event. A requested detent and arrival can occur at different times; choose the notification that matches the sound rather than attaching every click to initial input. The [control guide](InteriorControls.md#choose-the-correct-event) explains those boundaries.

For an application sound not represented by a channel, implement `AudioModule` or another appropriate owner. The [custom-channel example](Scripting/Audio.md#add-a-custom-loop-channel) shows lifecycle-safe registration/playback rather than allocating a new looping source every frame.

### Damage audio

Use **Damage Audio** for impact, scrape, landing, breakage and scripted-damage sounds. It shares one prepared voice pool and receives physical contacts from **Damage Feedback**. Configure **Damage Feedback** under **Vehicle Controller > Effects** and **Damage Audio** under **Effects > Audio**; the [damage response guide](DamageFeedback.md) covers banks, surfaces and custom effects.

**Damage Feedback > Profile** supplies physical contact sound banks. **Damage Audio > Contact Audio** controls voice capacity and enabled sound groups. **Audio Settings** controls playback and routing for the shared pool. Heavy impacts may replace an older busy voice; quieter contacts can be skipped when capacity is exhausted. **Mute Body Part On Detach** is enabled by default and silences subsequent detached-part contacts while accepted one-shots finish naturally.

For scripted damage, leave Damage Audio's **Impact Profiles** empty to reuse **Damage Feedback > Scripted Material Responses > Impact Profiles**. An explicit audio list can override a matching material response. Use the Impact Profile's recordings, intensity curves, pitch mode and cooldown for that scripted reaction. All sound types share the same prepared voices.

`DamageAudio.Played(contact, clip)` reports the copied contact and actual selected recording. `DamageFeedback.Contacted` reports accepted response events, while `Damage.Hit` remains the gameplay-damage notification. `TryPlay(hit)` requests a scripted presentation-only sound. `PlayedCount`, `DroppedCount` and `ActiveVoiceCount` report voice use.

Call `WarmUp()` after changing audio capacity or scripted profile lists. `ClearSounds()` stops voices and resets cooldowns. Numeric volume settings and enable switches may be changed directly at runtime. The Audio core still supplies master gain and interior/underwater context.

### Part detachment sounds

In **Damage Audio > Detachment Sounds**, add an entry with **Part**, **Clips**, **Enabled** and its **Audio Settings**. The channel plays a valid clip at the release position on `DamagePart.Detached`, including parts released with a parent group. Empty lists are silent; master Audio settings still apply.

Bindings survive repair/release cycles. After changing the list or Part references in code, call `RefreshPartSounds()`; applying vehicle configuration also refreshes them. Subscribe to `DetachmentPlayed(part, clip)` for accepted playback.

### Body-part and moving-part cues

`VehicleBodyPart` and `MovingPart` provide independent start and completion clip lists for opening and closing. Their **Movement Audio** settings support common or per-event source/anchor, volume, pitch, cooldown, mixer and spatial configuration. Generated emitters are allocated only for audible clips; existing source ownership is retained. See [the full event/audio setup](MovingParts.md#motion-events-and-four-audio-cues).

### Held horn

Assign **Clip** for a replacement recording. With **Clip** empty and **Use Default Clip** enabled, the channel uses its serialized default from `Resources/Audio/Interior/Horn.wav`. Disabling that option with no clip leaves it silent. Holding the command starts looping; release fades over **Release Duration** (default 0.05 s). Channel and core Audio Settings control volume, pitch, spatial attenuation and availability; disabling the channel suspends playback.

## Mixer and spatial tuning

Choose one intended `AudioListener` and test at the actual driver/external camera positions. **Spatial Blend** mixes 2D and 3D presentation; Min/Max Distance and rolloff determine distance response. Mixer attenuation, source volume, channel gain and profile volume can all contribute, so check the gain chain before repeatedly raising one number.

Reserve an overall loudness budget for engine, tires, transient sounds and several nearby vehicles. A louder engine can hide a working brake/relay sound without that channel being broken. Use the mixer for categories and the component/profile for a particular vehicle's balance.

A sound profile's speed/RPM references control modulation, not physics. For example, making a rotor loop reach full pitch earlier does not make the aircraft lift earlier. `Propulsion` spool is a separately observed physical/presentation state.

## Disable, reuse and clean up

The core/channel lifecycle suspends owned playback when disabled and releases generated resources according to their owner. Turning a channel back on is not a command to re-emit every previous one-shot. Rebinding should remove old event subscriptions so a pooled vehicle does not play several copies of one response.

The application still owns external `AudioSource` components and assets it supplies. Keep a supplied source's intended scope clear; do not assign one source to several independent loops expecting each channel to retain separate playback position.

## Verify the complete soundscape

| Symptom | Check |
| --- | --- |
| Replacement engine clip is ignored | Engine Audio Sound Profile, Loop Override and no-preset Engine Loop fallback |
| Profile is assigned but silent | Empty Loop, missing override, ignition/spool and core/channel availability |
| Works near the vehicle only | Listener position, spatial blend and distance/rolloff |
| One sound cuts another off | Shared `AudioSource` or a conflicting playback owner |
| Tire loop changes on one patch | Surface profile selection, including intentionally empty loops |
| Sound doubles after reuse | Duplicate channels/subscriptions or a second application listener |
| Rotor picture and loop do not match | `Propulsion` reference/spool and selected sound mode |

Test start/stop, idle/load, a shift, a skid, a channel disable/re-enable and a mode change. Save permanent profile/reference changes outside Play Mode. Exact channel operations and ownership are listed in [Audio API](API/Audio.md).

### Typed events and the effect adapter

Mechanics publish typed notifications with their context. Damage Audio receives Impact, LandingEvent and part-detachment notifications directly; engine, horn, indicator and mechanism audio use their own sources. Configure collision audio thresholds under Damage Audio. Events and Event Audio are optional custom application channels. See [event ownership](Scripting/Events.md#effect-event-ownership).

## Channel-owned sources

**Effects > Audio** owns master routing, volume, listening context and channel scheduling. Set the mechanical source on the channel: **Effects > Audio > Engine Audio > Engine**, **Tire Audio > Tire Feedback**, or **Brake Audio > Tire Feedback**. Engine sound items may override the channel engine through **Engine Audio > Items > Element > Engine**. Brake Audio resolves its feedback independently and does not require Tire Audio.

Creating a default car assigns these references on the channels. Configuration and runtime playback resolve an empty source from the vehicle without replacing a manual assignment. This also supports feedback modules added later. To switch an established source at runtime, assign the channel field explicitly; engine item assignments retain priority.

## Included clip names

Included recordings use PascalCase names arranged by sound family, action and optional variant: `EngineStart`, `EngineStop`, `EngineLoopCar`, `EngineLoopJet`, `TireLoopSqueal`, `TireLoopGravel`, `WaterSplashHull`, `WeaponShotPistol` and `NitroStart` / `NitroLoop` / `NitroStop`. Shared clips are in `Resources/Audio`; demo-specific clips are in `Demo/Audio`. Assign the clip in the relevant audio channel or sound profile. See [Credits](Credits.md) and [Third-party assets](ThirdParty.md) for each recording's attribution.
