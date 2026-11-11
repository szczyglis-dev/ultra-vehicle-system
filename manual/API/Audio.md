# Audio cores and channels API

Read [the system explanation](../Scripting/Audio.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [Audio](Audio.md#audio)
- [AudioClipReplacement](Audio.md#audioclipreplacement)
- [AudioContextMedium](Audio.md#audiocontextmedium)
- [AudioContextPoint](Audio.md#audiocontextpoint)
- [AudioContextProfile](Audio.md#audiocontextprofile)
- [AudioContextSettings](Audio.md#audiocontextsettings)
- [AudioContextView](Audio.md#audiocontextview)
- [AudioEvent](Audio.md#audioevent)
- [AudioModule](Audio.md#audiomodule)
- [AudioSettingsOverride](Audio.md#audiosettingsoverride)
- [BoatWaterAudio](Audio.md#boatwateraudio)
- [BrakeAudio](Audio.md#brakeaudio)
- [CommercialAudio](Audio.md#commercialaudio)
- [EngineAudio](Audio.md#engineaudio)
- [EngineAudioItem](Audio.md#engineaudioitem)
- [EngineAudioItemState](Audio.md#engineaudioitemstate)
- [EnginePitchMode](Audio.md#enginepitchmode)
- [EngineSoundProfile](Audio.md#enginesoundprofile)
- [EventAudio](Audio.md#eventaudio)
- [HornAudio](Audio.md#hornaudio)
- [IAudioModule](Audio.md#iaudiomodule)
- [IndicatorAudio](Audio.md#indicatoraudio)
- [MovingPartAudio](Audio.md#movingpartaudio)
- [NitroAudio](Audio.md#nitroaudio)
- [ProfileTransitionAudio](Audio.md#profiletransitionaudio)
- [ProfileTransitionAudio.TransitionSound](Audio.md#profiletransitionaudiotransitionsound)
- [SwitchAudio](Audio.md#switchaudio)
- [TireAudio](Audio.md#tireaudio)
- [VehicleAudioSettings](Audio.md#vehicleaudiosettings)
- [WiperAudioEntry](Audio.md#wiperaudioentry)
- [WipersAudio](Audio.md#wipersaudio)

## Audio

**Runtime/Effects/Audio/Audio.cs**

Owns channel discovery, common audio settings and render-frame dispatch.

**Inherits / implements:** [EffectsModule](Presentation.md#effectsmodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual AudioModule[] AudioModules { get; }` | Audio channels owned by this core, including child parts and excluding nested vehicles or nested audio cores. |
| `public AudioContextSettings context` | Central [camera, area and medium configuration](../Audio.md#camera-area-and-medium-profiles). |
| `public Camera ListeningCamera { get; }` | Resolved active listening camera, or null. |
| `public CameraModule ListeningView { get; }` | Resolved vehicle view module, or null for external views. |
| `public string AudioMedium { get; }` | Resolved listener medium: air, water or an explicit custom ID. |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public virtual float CornerSquealWait { get; }` | Remaining wait before a sustained corner becomes audible, in seconds. |
| `public virtual bool EngineLoopPlaying { get; }` | Read-only/resolved engine loop playing for Audio. |
| `public virtual float EngineLoopVolume { get; }` | Read-only/resolved engine loop volume for Audio. |
| `public virtual float EnginePitch { get; }` | Read-only/resolved engine pitch for Audio. |
| `public virtual float EngineToneCutoff { get; }` | Current engine low-pass filter cutoff, in Hz. |
| `public virtual int PlayedEventCount { get; }` | Read-only/resolved played event count for Audio. |
| `public VehicleController vehicle` | Assign the vehicle VehicleController component/asset used by Audio. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void RefreshPlaybackConfiguration()` | Rebuilds audio profile definitions and invalidates registered sources' static spatial/routing settings; source settings reapply at their next use. | — |
| `public override void Configure(VehicleController owner)` | Stores the owner, ensures standard channels, refreshes channel order and resolves missing channel references. | `owner` — Unity/application owner whose identity controls this relationship or resource. |
| `public virtual AudioSource CreateSource(string name, bool loop)` | Resolves a source using the core Audio Settings and initializes its gain to zero. For explicit ownership reporting, use VehicleAudioSettings.ResolveSource. | `name` — Generated source label. `loop` — Looping playback. Returns the resolved AudioSource. |
| `public virtual void EnsureModules(System.Func<System.Type, AudioModule> addChannel = null)` | Ensures the audio core has its required standard channel components. | `addChannel` — Optional audio-channel creation callback. Default: `null`. |
| `public virtual float FilterCornerSqueal(float skid, bool corner, float deltaTime)` | Filters or evaluates corner squeal using the tire-audio policy without changing tire physics. | `skid` — Resolved skid activity. `corner` — Corner, interpreted by this operation in the declared type. `deltaTime` — Elapsed time in seconds supplied by the owning loop. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual void PlayEvent(EffectEvent effect)` | Plays the configured presentation sound for a vehicle effect event. | `effect` — Resolved vehicle `EffectEvent` to present. |
| `public virtual void RefreshAudioModules()` | Rebuilds the audio core's channel snapshot in effective execution order. | No arguments; no returned value. |
| `public virtual void UpdateLoop(AudioSource source, AudioClip clip, float volume, float pitch, float blend, VehicleAudioSettings settings = null)` | Smooths loop gain and pitch, updates the recording, and starts/stops playback at the audible threshold. Optional settings select per-sound routing; null uses the core settings. Core Volume, Pitch and Enabled control the channel mix. | — |
| `public void SetListeningCamera(Camera camera, CameraModule module = null)` | Uses externally supplied listening context. | Optional module identifies a vehicle view. |
| `public void UseAutomaticListeningCamera()` | Restores active vehicle-view / Camera.main detection. | No arguments. |
| `public void SetAudioMedium(string medium)` | Overrides automatic medium detection. | Case-sensitive ID; null/empty restores automatic detection. |
| `public void RefreshAudioContext()` | Refreshes matching camera, area and medium conditions against prepared profile definitions. | Called automatically by rendering/playback. |
| `public void RefreshAudioProfiles()` | Rebuilds profile definitions and replacement-clip lists after code edits, additions or replacements. | Existing profile `enabled` switches need no rebuild. |
| `public void RegisterAudioSource(AudioModule channel, AudioSource source)` | Associates a source with this context and channel scope. | Does not transfer source ownership. |
| `public void UnregisterAudioChannel(AudioModule channel)` | Restores and releases context state for a channel. | Called by the AudioModule lifecycle. |
| `public AudioClip GetOriginalLoopClip(AudioSource source)` | Reads the logical recording before context replacement. | Returns the original clip or current source clip. |
| `public AudioClip ResolveLoopClip(AudioModule channel, AudioSource source, AudioClip original)` | Selects a stable loop replacement from matching rules. | Returns null for an enabled empty replacement list. |
| `public void ApplyAudioContext(AudioModule channel, AudioSource source)` | Applies matched gain, pitch, filtering and routing. | Use ordinary settings first; repeated context application does not compound gain. |
| `public AudioClip PlayOneShot(AudioModule channel, AudioSource source, AudioClip original, float volume = 1)` | Plays a context-selected one-shot using configured source settings. | Returns the selected clip or null when unavailable/silenced. |
| `public AudioClip PlayClip(AudioModule channel, AudioSource source, AudioClip original)` | Plays a context-selected recording through source.clip. | Returns the selected clip or null when unavailable/silenced. |

## AudioContextSettings

**Runtime/Effects/Audio/Context/AudioContextProfile.cs**

Serialized context configuration on Audio. `enabled` gates the layer; `cameras` and `listenerCamera` override automatic view lookup; `waterProvider` supplies surface samples; `underwaterDepth` sets the Water threshold; `transitionSeconds` blends gain/pitch/filtering; `profiles` contains ordered AudioContextProfile entries.


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool enabled` | Enables this entry/layer. |
| `public Cameras cameras` | Optional vehicle camera core. Empty uses Cameras on this vehicle. |
| `public Camera listenerCamera` | Optional external listening camera. Empty follows this vehicle's active view, then Camera.main. Code may also call SetListeningCamera. |
| `public WaterProvider waterProvider` | Water sampled at the listener/vehicle point, including waves. Empty uses this vehicle's Water Interaction/profile when available. |
| `public float underwaterDepth` | Depth below the sampled surface required to select Water. |
| `public float transitionSeconds` | Seconds to blend volume, pitch and filtering after a context change. Clip changes retain normalized loop position. |
| `public AudioContextProfile[] profiles` | Matching profiles combine in list order: gain/pitch multiply, lowest filter cutoff wins, last mixer/spatial/clip override wins. Disabled entries have no effect. |

## AudioContextProfile

**Runtime/Effects/Audio/Context/AudioContextProfile.cs**

An enabled entry combines optional `channel`, `view`, `camera`, `cameraModule`, `area` and `medium` conditions. `samplePoint` selects listener or vehicle position; `customMedium` supplies the ID for Custom. `name` labels the entry. Playback modifiers are `mute`, `volumeMultiplier`, `pitchMultiplier`, `lowPass`/`lowPassCutoff`, `output` and `overrideSpatialBlend`/`spatialBlend`. `clipReplacements` contains original-to-variant mappings. Matching entries stack as described in [profile authoring](../Audio.md#camera-area-and-medium-profiles).


### State and configuration

| Member | Meaning |
| --- | --- |
| `public string name` | Inspector label. |
| `public bool enabled` | Enables this entry/layer. |
| `public AudioModule channel` | Optional channel to affect, such as Engine Audio. Empty affects every audio channel of this vehicle. |
| `public AudioContextView view` | Required view, or Any. |
| `public Camera camera` | Optional actual rendering camera. Supports external camera systems too. |
| `public CameraModule cameraModule` | Optional exact vehicle camera module, including custom views. |
| `public AudioContextPoint samplePoint` | Position tested against Area and Medium. Listener follows the selected camera; Vehicle follows this vehicle. |
| `public Collider area` | Optional volume containing the sample point. Use a Box, Sphere, Capsule or convex Mesh collider; it may be a trigger. |
| `public AudioContextMedium medium` | Required medium, or Any. |
| `public string customMedium` | Case-sensitive medium ID supplied through Audio.SetAudioMedium. Used with Medium = Custom. |
| `public bool mute` | Silences matching audio. |
| `public float volumeMultiplier` | Multiplies ordinary gain. |
| `public float pitchMultiplier` | Multiplies ordinary pitch. |
| `public bool lowPass` | Enables the context low-pass ceiling. |
| `public float lowPassCutoff` | Low-pass ceiling in Hz. |
| `public AudioMixerGroup output` | Optional mixer route for reverb, EQ, distortion or other effects. Last matching nonempty route wins; shared mixer assets are never modified. |
| `public bool overrideSpatialBlend` | Overrides ordinary source spatial blend. |
| `public float spatialBlend` | Override from 0 (2D) to 1 (3D). |
| `public AudioClipReplacement[] clipReplacements` | Serialized context setting. |

## AudioClipReplacement

**Runtime/Effects/Audio/Context/AudioContextProfile.cs**

`enabled` gates the mapping; `original` identifies a recording; `clips` supplies random variants. An enabled empty/null list is silent. Null slots are skipped, and continuous loops retain their selected variant until the rule or available variants change.


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool enabled` | Enables this entry/layer. |
| `public AudioClip original` | Original recording matched by this replacement. |
| `public AudioClip[] clips` | Random replacements for the original recording. An empty list deliberately silences it. Loops keep one variant until the matching rule changes. |

## AudioContextView

**Runtime/Effects/Audio/Context/AudioContextProfile.cs**

Values: `Any`, `Orbit`, `Interior`, `Custom`, `External`. External means a listening camera without a vehicle CameraModule.

## AudioContextMedium

**Runtime/Effects/Audio/Context/AudioContextProfile.cs**

Values: `Any`, `Air`, `Water`, `Custom`. Custom uses AudioContextProfile.customMedium and Audio.SetAudioMedium.

## AudioContextPoint

**Runtime/Effects/Audio/Context/AudioContextProfile.cs**

Values: `Listener`, `Vehicle`. Selects the world position tested for area containment and automatic medium detection.

## AudioEvent

**Runtime/Effects/Audio/AudioEvent.cs**

Configuration/implementation type for audio event within audio cores and channels.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip[] clips` | Audio recordings available for selection for clips. No assigned clip means this recording is unavailable. |
| `public string eventId` | Text identifier/name for event id. Keep it consistent with the referenced animation, profile or application setting. Initial value: `""`. |
| `public float minimumIntensity` | Lowest event intensity that is eligible to play this sound entry. Initial value: `.05f`. |

## AudioModule

**Runtime/Effects/Audio/Core/AudioModule.cs**

Base channel with source creation, loop update and cleanup helpers.

**Inherits / implements:** [EffectsModule](Presentation.md#effectsmodule), [IAudioModule](Audio.md#iaudiomodule).

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public abstract void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |

## AudioSettingsOverride

**Runtime/Effects/Audio/VehicleAudioSettings.cs**

Optional per-cue override inheriting [VehicleAudioSettings](Audio.md#vehicleaudiosettings).

**Inherits / implements:** [VehicleAudioSettings](Audio.md#vehicleaudiosettings).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool overrideSettings` | Selects this cue’s independent VehicleAudioSettings instead of the shared settings. |

## BoatWaterAudio

**Runtime/Effects/Audio/Modules/BoatWaterAudio.cs**

Configuration/implementation type for boat water audio within audio cores and channels.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float fullLappingMotion` | Hull-motion amount at which lapping audio reaches full configured contribution. Initial value: `.12f`. |
| `public float fullWakeSpeed` | Hull speed in m/s at which wake audio reaches its full configured contribution. Initial value: `20`. |
| `public Vector2 hullHalfSize` | Hull half-width and half-length, metres; converts real roll/pitch rates to water-contact motion. |
| `public virtual float HullMotion { get; protected set; }` | Read-only/resolved hull motion for `BoatWaterAudio`. |
| `public VehicleAudioSettings lappingAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip lappingLoop` | Audio recording for lapping loop. No assigned clip means this recording is unavailable. |
| `public virtual float LappingVolume { get; }` | Read-only/resolved lapping volume for `BoatWaterAudio`. |
| `public virtual AudioClip LastSplashClip { get; protected set; }` | Read-only/resolved last splash clip for `BoatWaterAudio`. |
| `public virtual int PlayedSplashCount { get; protected set; }` | Read-only/resolved played splash count for `BoatWaterAudio`. |
| `public VehicleAudioSettings splashAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip[] splashClips` | Audio recordings available for selection for splash clips. No assigned clip means this recording is unavailable. |
| `public float splashThreshold` | Threshold/tolerance for splash threshold. The corresponding action or transition is admitted only when its comparison condition is satisfied. Initial value: `.2f`. |
| `public VehicleAudioSettings wakeAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip wakeLoop` | Audio recording for wake loop. No assigned clip means this recording is unavailable. |
| `public virtual float WakeVolume { get; }` | Read-only/resolved wake volume for `BoatWaterAudio`. |
| `public virtual bool WaterContact { get; protected set; }` | Read-only/resolved water contact for `BoatWaterAudio`. |
| `public bool waterSoundsEnabled` | Enables water sounds behavior for this system. Initial value: `true`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |

## BrakeAudio

**Runtime/Effects/Audio/Modules/BrakeAudio.cs**

Configuration/implementation type for brake audio within audio cores and channels.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public Vector2 brakeSpeedRangeKph` | Speed range in km/h from silent to full brake-loop volume. |
| `public AudioClip brakingLoop` | Default brake recording. A grounded wheel uses its surface brakingLoop when supplied; the surface empty-clip checkbox selects this recording or silence otherwise. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |


| Declaration | Usage |
| --- | --- |
| `public TireFeedback tireFeedback` | Channel-owned source. Explicit assignment wins; empty resolves from the vehicle. Engine item overrides take priority over the channel engine. |
| `public override void Configure(VehicleController owner)` | Resolves a missing source from the configured vehicle without replacing an explicit assignment. |
## CommercialAudio

**Runtime/Effects/Audio/Modules/CommercialAudio.cs**

Configuration/implementation type for commercial audio within audio cores and channels.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool airBrakesEnabled` | Enables air brakes behavior for this system. Initial value: `true`. |
| `public virtual int AirSoundCount { get; protected set; }` | Read-only/resolved air sound count for `CommercialAudio`. |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public VehicleAudioSettings brakeApplyAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip brakeApplyClip` | Audio recording for brake apply clip. No assigned clip means this recording is unavailable. |
| `public VehicleAudioSettings brakeReleaseAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip brakeReleaseClip` | Audio recording for brake release clip. No assigned clip means this recording is unavailable. |
| `public float brakeThreshold` | Threshold/tolerance for brake threshold. The corresponding action or transition is admitted only when its comparison condition is satisfied. Initial value: `.12f`. |
| `public Gearbox gearbox` | Assign the gearbox Gearbox component/asset used by CommercialAudio. |
| `public virtual AudioClip LastAirClip { get; protected set; }` | Read-only/resolved last air clip for `CommercialAudio`. |
| `public virtual AudioClip LastReverseClip { get; protected set; }` | Read-only/resolved last reverse clip for `CommercialAudio`. |
| `public float movingSpeedKph` | Moving speed in km/h (stored value); Speed fields display the selected speed unit. Initial value: `1.5f`. |
| `public AudioClip parkingApplyClip` | Audio recording for parking apply clip. No assigned clip means this recording is unavailable. |
| `public bool parkingApplySound` | When checked, parking apply sound is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |
| `public VehicleAudioSettings parkingAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip parkingReleaseClip` | Audio recording for parking release clip. No assigned clip means this recording is unavailable. |
| `public bool parkingReleaseSound` | Play a pneumatic parking-brake release sound when the parking brake is released. |
| `public virtual bool ReverseAlarmActive { get; protected set; }` | Read-only/resolved reverse alarm active for `CommercialAudio`. |
| `public bool reverseAlarmEnabled` | Enables reverse alarm behavior for this system. Initial value: `true`. |
| `public VehicleAudioSettings reverseAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip reverseBeepClip` | One beep; cadence is controlled separately below. |
| `public virtual int ReverseBeepCount { get; protected set; }` | Read-only/resolved reverse beep count for `CommercialAudio`. |
| `public float reverseInterval` | Time in seconds used for reverse interval. Larger values make this phase/wait last longer. Initial value: `.85f`. |
| `public float stoppedSpeedKph` | Stopped speed in km/h (stored value); Speed fields display the selected speed unit. Initial value: `.5f`. |
| `public bool stopStartOnly` | Service-brake hiss only on stopping and setting off; disable for pedal-edge sounds. |
| `public VehicleController vehicle` | Assign the vehicle VehicleController component/asset used by CommercialAudio. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderAudio(Audio core, float deltaTime)` | Updates brake responses and the reversing alarm through the owning Audio core. | — |
| `public override void SuspendAudio()` | Stops all commercial audio and resets playback state. | — |

## EngineAudio

**Runtime/Effects/Audio/Modules/EngineAudio.cs**

Owns and renders independent engine/rotor sound items. Each item has its own sources and state; profile assets remain shared immutable configuration.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public virtual float EngineLoopDelayRemaining { get; }` | Largest remaining ordinary start delay among prepared items, in seconds. |
| `public virtual bool EngineLoopPlaying { get; }` | True if any item loop is playing. |
| `public virtual float EngineLoopVolume { get; }` | Sum of current loop-source volumes across items. Spatial attenuation and mixer output are applied separately. |
| `public virtual float EnginePitch { get; }` | Arithmetic mean pitch of currently playing item loops; zero if none play. Use TryGetState for per-item pitch. |
| `public virtual float EngineToneCutoff { get; }` | Lowest enabled item low-pass cutoff in Hz, or 22000 if no tone filter is enabled. |
| `public float gizmoSize` | Scene marker radius in metres; default 0.08. |
| `public List<EngineAudioItem> items` | Independent engine/rotor sounds. Each item owns its ID, profile, anchor, response and ignition settings. |
| `public virtual AudioClip LastIgnitionClip { get; protected set; }` | Most recent start/stop recording played by any item. |
| `public bool showGizmos` | Shows audio-origin scene guides. Sub-options independently control markers, ID labels and connections. |
| `public virtual int StartSoundCount { get; protected set; }` | Total start one-shots played by this channel across all items, including subsequently removed items. |
| `public virtual int StopSoundCount { get; protected set; }` | Total stop one-shots played by this channel across all items, including subsequently removed items. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual bool AddItem(EngineAudioItem item)` | Adds a non-null item with a unique non-empty ID and prepares its engine subscription. Returns false for invalid or duplicate IDs/references. | — |
| `public virtual AudioSource GetIgnitionSource(string id)` | Returns the generated start/stop source for the unique ID, or null before the first audible ignition transition. | — |
| `public virtual EngineAudioItem GetItem(string id)` | Returns the unique item matching ID, or null for a missing or ambiguous ID. Edits take effect on the next audio render. | — |
| `public virtual AudioSource GetLoopSource(string id)` | Returns the generated loop source for the unique ID, or null if unresolved/not created. Playback settings are reapplied by the audio renderer. | — |
| `public virtual void RefreshItems()` | Synchronizes directly edited/replaced lists with runtime voices and engine subscriptions. RenderAudio also synchronizes automatically; removed voices are released. | — |
| `public virtual bool RemoveItem(string id)` | Removes the unique ID, unsubscribes its engine and releases only its generated sources. Returns false if ID is missing or ambiguous. | — |
| `public override void RenderAudio(Audio core, float deltaTime)` | Synchronizes items and renders each active sound once using its own engine, spool, profile and modulation state. | — |
| `public virtual bool SelectItem(string id)` | Exclusively activates the unique matching item and immediately stops all other items. Missing or ambiguous IDs return false without changing selection. | — |
| `public virtual bool SetItemActive(string id, bool active)` | Sets one item active/inactive by ID. Inactive immediately stops its loop and ignition. Reactivation does not synthesize ignition. Returns whether ID resolved. | — |
| `public virtual bool SetItemAnchor(string id, Transform anchor)` | Changes one item's origin and reparents existing sources without restart. Null restores Audio core origin. Returns whether ID resolved. | — |
| `public virtual bool SetItemProfile(string id, EngineSoundProfile profile)` | Replaces one item's reusable preset. Null selects override-only settings. Other items and shared assets are unchanged. Returns whether ID resolved. | — |
| `public override void SuspendAudio()` | Stops every owned source and releases engine subscriptions. Re-enabling restores loops for already-running engines without replaying ignition. | — |
| `public virtual bool TryGetItem(string id, out EngineAudioItem item)` | Returns true and the unique matching mutable item. Empty, missing or duplicate IDs return false with a null item. | — |
| `public virtual bool TryGetState(string id, out EngineAudioItemState state)` | Returns a snapshot of playing state, volume, pitch, selected loop, delay and ignition history for the ID. False means unresolved or not prepared. | — |


| Declaration | Usage |
| --- | --- |
| `public Engine engine` | Channel-owned source. Explicit assignment wins; empty resolves from the vehicle. Engine item overrides take priority over the channel engine. |
| `public override void Configure(VehicleController owner)` | Resolves a missing source from the configured vehicle without replacing an explicit assignment. |
## EngineAudioItem

**Runtime/Effects/Audio/EngineAudioItem.cs**

Serializable per-source configuration. Assign several items for multiple engines/rotors, and switch them through ID-based activation.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool active` | Enables this sound only. Disabling stops its loop and ignition without affecting other items. |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public Engine engine` | Optional mechanical engine to follow. Empty uses Engine Audio > Engine, which resolves from the vehicle when unassigned. |
| `public float engineLoopReferenceRpm` | RPM at which the loop plays at its original pitch. Zero uses normalized RPM and the exponent instead. |
| `public float engineLoopStartDelay` | Delay after an actual engine-start transition before an ordinary loop can play. Already-running engines and propulsion spool are not delayed. |
| `public float engineRpmPitchExponent` | Shapes normalized RPM-to-pitch response when Reference RPM is zero. |
| `public AudioClip engineStartClip` | Local start clip, used without a profile start clip or when Override Ignition Clips is enabled. |
| `public AudioClip engineStopClip` | Local stop clip, used without a profile stop clip or when Override Ignition Clips is enabled. |
| `public Vector2 engineToneCutoff` | Idle-to-loaded low-pass cutoff in Hz for this item's detailed engine response. |
| `public bool followPropulsionSpool` | Scales the sound with propulsion spin-up/down. Off follows ignition state directly. |
| `public float forwardSpeedReference` | Full forward-speed activity for an override-only Motion loop. |
| `public string id` | Unique, case-sensitive ID used by EngineAudio's runtime API. |
| `public VehicleAudioSettings ignitionAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public bool loadSensitiveTone` | Applies a low-pass filter to detailed RPM sounds according to engine load. |
| `public AudioClip LoopClip { get; }` | Effective loop recording: item override first, otherwise the profile loop; null if neither is assigned. |
| `public AudioClip loopOverride` | Replaces the profile loop, or supplies the loop when no profile is assigned. |
| `public VehicleAudioSettings mixAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public bool overrideIgnitionClips` | Use this item's ignition clips instead of profile clips. Otherwise assigned profile clips and their volumes take priority. |
| `public EnginePitchMode pitchMode` | Pitch mapping for override-only loops. Profile sounds use their own Pitch Mode. |
| `public bool playIgnitionSounds` | Plays start/stop sounds on actual running-state transitions, not on item activation or mode changes. |
| `public VehicleAudioSettings profileAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public Propulsion propulsion` | Optional propulsion spool to follow. Empty uses the vehicle's Propulsion. |
| `public bool reactToEngineActivity` | Allows engine RPM/throttle or profile activity to change volume and load-sensitive tone. |
| `public bool reactToPitch` | Allows RPM/motion/spool to change pitch. Off holds Fixed Pitch exactly. |
| `public EngineSoundProfile soundProfile` | Reusable loop, pitch and ignition settings. Empty allows an override-only sound. |
| `public VehicleAudioSettings startAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public VehicleAudioSettings stopAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public bool useEngineResponse` | Allows detailed RPM reference, exponent, load tone and shift response. Profile sounds also require Use Engine Response on their profile. |
| `public float verticalSpeedReference` | Full vertical-speed activity for an override-only Motion loop. |

## EngineAudioItemState

**Runtime/Effects/Audio/EngineAudioItem.cs**

Read-only per-item playback snapshot returned by EngineAudio.TryGetState.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public float DelayRemaining { get; }` | Seconds remaining before the ordinary loop may start. Spool-driven loops follow propulsion instead. |
| `public AudioClip LastIgnitionClip { get; }` | Most recent ignition clip played by this item. |
| `public AudioClip LoopClip { get; }` | Recording currently assigned to the generated loop source. |
| `public float Pitch { get; }` | Current playback pitch multiplier; zero if no loop source exists. |
| `public bool Playing { get; }` | Whether this item's loop source is playing. |
| `public int StartSoundCount { get; }` | Start one-shots played by this item. |
| `public int StopSoundCount { get; }` | Stop one-shots played by this item. |
| `public float Volume { get; }` | Current loop-source gain, before spatial attenuation and mixer processing. |

## EnginePitchMode

**Runtime/Effects/Audio/EngineSoundProfile.cs**

Defines the allowed engine pitch mode choices used by this topic.

### Values

- `Rpm`
- `Constant`
- `Motion`

## EngineSoundProfile

**Runtime/Effects/Audio/EngineSoundProfile.cs**

Stores engine sound behavior and asset configuration.

**Inherits / implements:** `ScriptableObject`.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public float forwardSpeedReference` | Forward speed in m/s used to normalize a forward-speed-driven sound profile. Initial value: `25`. |
| `public AudioClip loop` | Audio recording for loop. No assigned clip means this recording is unavailable. |
| `public EnginePitchMode pitchMode` | Selects the pitch mode policy for this configuration. Options: `Rpm`, `Constant`, `Motion`. |
| `public VehicleAudioSettings startAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip startClip` | Start sound used by items referencing this profile, unless explicitly overridden on the item. |
| `public VehicleAudioSettings stopAudioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip stopClip` | Stop sound used by items referencing this profile, unless explicitly overridden on the item. |
| `public bool useEngineResponse` | For RPM profiles, retain `EngineAudio`'s RPM exponent/reference, throttle level, tone filter and shift response. |
| `public float verticalSpeedReference` | Vertical speed in m/s used to normalize a vertical-speed-driven sound profile. Initial value: `6`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual float EvaluateActivity(VehicleController vehicle, Engine engine)` | Evaluates sound activity from the configured sound profile and mechanical input. | `vehicle` — Vehicle context/owner receiving the operation. `engine` — Engine whose running/RPM/gearbox state supplies the operation. **Returns:** Computed float in the operation's documented unit/domain. |
| `public virtual float EvaluatePitch(float activity)` | Evaluates audio pitch from the configured engine sound response. | `activity` — Normalized presentation activity. **Returns:** Computed float in the operation's documented unit/domain. |

## EventAudio

**Runtime/Effects/Audio/Modules/EventAudio.cs**

Configuration/implementation type for event audio within audio cores and channels.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<EffectEvent, AudioClip> Played` | When `EventAudio` plays a resolved event clip. Payload: `EffectEvent` and `AudioClip`. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Events events` | Custom Events source used by EventAudio; empty resolves on the owning vehicle. |
| `public AudioEvent[] eventSounds` | Application-defined sound mappings. New lists are empty; configure an exact custom ID, clips and Audio Settings. Event intensity scales gain. |
| `public virtual int PlayedEventCount { get; protected set; }` | Read-only/resolved played event count for `EventAudio`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void PlayEvent(EffectEvent effect)` | Plays the configured presentation sound for a vehicle effect event. | `effect` — Resolved vehicle `EffectEvent` to present. |
| `public override void RenderAudio(Audio owner, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `owner` — Unity/application owner whose identity controls this relationship or resource. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |

## HornAudio

**Runtime/Effects/Audio/Modules/HornAudio.cs**

Held audible warning using a replaceable clip or packaged default. Inherits [AudioModule](Audio.md#audiomodule); add beside the Audio core.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Channel volume, pitch, spatial anchor, distance and output mixer. |
| `public AudioClip clip` | Optional replacement recording. |
| `public bool IsSounding { get; }` | True while the source is playing at nonzero volume. |
| `public float releaseDuration` | Seconds to fade after releasing the request; zero stops immediately. |
| `public bool useDefaultClip` | Use the serialized default horn when Clip is empty and Use Default Clip is enabled. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderAudio(Audio core, float deltaTime)` | Follows the owning vehicle's held Command.Horn, including master/channel mute. The Audio core calls this once per render frame. | — |
| `public override void SuspendAudio()` | Immediately stops playback and clears its release envelope. | — |

## IAudioModule

**Runtime/Effects/Audio/Core/AudioModule.cs**

Configuration/implementation type for iaudio module within audio cores and channels.

**Inherits / implements:** [IEffectsModule](Modules.md#ieffectsmodule).

### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## IndicatorAudio

**Runtime/Effects/Audio/Modules/IndicatorAudio.cs**

Follows actual indicator output phase.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public virtual AudioClip LastPlayedClip { get; protected set; }` | Read-only/resolved last played clip for `IndicatorAudio`. |
| `public Lights lights` | Assign the lights Lights component/asset used by IndicatorAudio. |
| `public virtual int PlayedClickCount { get; protected set; }` | Read-only/resolved played click count for `IndicatorAudio`. |
| `public AudioClip tickOff` | Optional replacement for the relay click when the lamps turn off. |
| `public AudioClip tickOn` | Optional replacement for the relay click when the lamps turn on. |
| `public bool useDefaultClicks` | When checked, use default clicks is active; when unchecked the owning system skips that optional policy. Initial value: `true`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void SetClips(AudioClip on, AudioClip off)` | Replaces indicator tick clips, retaining generated defaults for independently unassigned clips. | `on` — On, interpreted by this operation in the declared type. `off` — Off, interpreted by this operation in the declared type. |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |

## MovingPartAudio

**Runtime/Effects/Audio/Modules/MovingPartAudio.cs**

Optional audio receiver for moving mechanisms.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public MonoBehaviour motionSource` | MovingPart or VehicleBodyPart publishing motion notifications. |
| `public PartMotionAudio movementAudio` | Optional [opening/closing sound settings](MovingParts.md#partmotionaudio). Start cues play once per changed request, including explicit closing of an impact-unlatched panel; completion cues follow actual hinge arrival. Collision swinging alone is silent. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController owner)` | Stores the vehicle whose hover transition geometry should be displayed. | `owner` — Unity/application owner whose identity controls this relationship or resource. |
| `public virtual AudioSource GetMotionAudioSource(PartMotionEvent phase)` | Returns the configured or owned audio source for the requested movement phase. | — |
| `public virtual bool PlayMotionAudio(PartMotionEvent phase)` | Plays the configured audio for the requested movement phase. | — |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public virtual void StopMotionAudio()` | Stops every source created by this part. Explicitly assigned or anchor-attached sources remain user-owned. | — |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |

## NitroAudio

**Runtime/Effects/Audio/Modules/NitroAudio.cs**

Optional audio driven by Nitro output notifications.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Nitro nitro` | Nitro source supplying output state and strength. |
| `public VehicleAudioSettings nitroLoopAudioSettings` | Loop mix/spatial settings. Default volume .7, pitch range .8–1.25, distance 3–55 m; pitch and gain follow RPM. |
| `public AudioClip nitroLoopClip` | Sustained jet-engine loop during boost. Bundled default assigned on component creation; clear to mute. |
| `public AudioSource NitroLoopSource { get; }` | Current loop source, created on demand and stopped when boost ends. |
| `public VehicleAudioSettings nitroOffAudioSettings` | Independent VehicleAudioSettings for the Off cue. Default volume 0.45, distance 3–45 m. Supplied AudioSources/anchors are preserved during component cleanup. |
| `public AudioClip nitroOffClip` | Release cue; bundled jet shutdown default assigned on creation. Internal shifts do not end the audio session. |
| `public AudioSource NitroOffSource { get; }` | Resolved Off AudioSource, created on demand. Null before the first audible Off cue. |
| `public VehicleAudioSettings nitroOnAudioSettings` | Independent VehicleAudioSettings for the On cue: enabled, volume, pitch, source/anchor, mixer, spatial range and routing. Default volume 0.65, distance 3–45 m. |
| `public AudioClip nitroOnClip` | Activation cue; bundled jet-engine default assigned on creation. Replace or clear as needed. |
| `public AudioSource NitroOnSource { get; }` | Resolved On AudioSource, created on demand. Null before the first audible On cue. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController vehicle)` | Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |

## ProfileTransitionAudio

**Runtime/Effects/Audio/Modules/ProfileTransitionAudio.cs**

Optional audio receiver for admitted profile transitions.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public TransitionSound[] sounds` | Audio routes matched to a transition component. Each route owns both direction clips and its playback settings. |
| `public ProfileSwitcher switcher` | Profile switcher supplying admitted transitions. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController owner)` | Stores the vehicle whose hover transition geometry should be displayed. | `owner` — Unity/application owner whose identity controls this relationship or resource. |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |

## ProfileTransitionAudio.TransitionSound

**Runtime/Effects/Audio/Modules/ProfileTransitionAudio.cs**

Presentation or lifecycle contract for independent vehicle components.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip forwardClip` | Optional sound for fromProfileId → toProfileId. |
| `public AudioClip reverseClip` | Optional sound for the reverse direction of a bidirectional route. |
| `public ProfileTransition transition` | Transition route whose direction selects a recording. |

## SwitchAudio

**Runtime/Effects/Audio/Modules/SwitchAudio.cs**

Configuration/implementation type for switch audio within audio cores and channels.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public AudioClip click` | Audio recording for click. No assigned clip means this recording is unavailable. |
| `public virtual int PlayedClickCount { get; protected set; }` | Read-only/resolved played click count for `SwitchAudio`. |
| `public SwitchAnimator switchAnimator` | Assign the switch handle SwitchHandle component/asset used by SwitchAudio. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |

## TireAudio

**Runtime/Effects/Audio/Modules/TireAudio.cs**

Consumes per-wheel contact/effect-surface state.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public Vector2 cornerSquealDelay` | Minimum and maximum sustained-turn delay before squeal starts, in seconds. |
| `public float cornerSquealMinimumSpeed` | Minimum vehicle speed in km/h for the sustained-corner squeal contribution. Initial value: `50`. |
| `public virtual float CornerSquealWait { get; protected set; }` | Remaining wait before a sustained corner becomes audible, in seconds. |
| `public float cornerSteeringThreshold` | Threshold/tolerance for corner steering threshold. The corresponding action or transition is admitted only when its comparison condition is satisfied. Initial value: `.75f`. |
| `public bool delayCornerSqueal` | Delay squeal during sustained high-speed corners. Disable for immediate slip feedback. |
| `public AudioClip tireSquealLoop` | Audio recording for tire squeal loop. No assigned clip means this recording is unavailable. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual float FilterCornerSqueal(float skid, bool highSpeedCorner, float deltaTime)` | Filters or evaluates corner squeal using the tire-audio policy without changing tire physics. | `skid` — Resolved skid activity. `highSpeedCorner` — Corner-squeal input used by tire-audio filtering. `deltaTime` — Elapsed time in seconds supplied by the owning loop. **Returns:** Computed float in the operation's documented unit/domain. |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |


| Declaration | Usage |
| --- | --- |
| `public TireFeedback tireFeedback` | Channel-owned source. Explicit assignment wins; empty resolves from the vehicle. Engine item overrides take priority over the channel engine. |
| `public override void Configure(VehicleController owner)` | Resolves a missing source from the configured vehicle without replacing an explicit assignment. |
## VehicleAudioSettings

**Runtime/Effects/Audio/VehicleAudioSettings.cs**

Universal serialized playback, source/anchor and spatial configuration. Clips and triggering rules belong to the owning mechanism.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public Transform audioAnchor` | Emitter transform for generated sources; empty uses the owning mechanism. Pooled audio creates independent voices under this anchor. |
| `public float cooldown` | Minimum interval between matching one-shots, in seconds. |
| `public float dopplerLevel` | Doppler multiplier. |
| `public bool enabled` | Enables this playback configuration. |
| `public float maxDistance` | Outer attenuation distance in metres, not below Min Distance. |
| `public float minDistance` | Full-volume distance in metres. |
| `public AudioMixerGroup output` | Mixer output group. |
| `public float pitch` | Fixed pitch or one-shot pitch multiplier; 1 uses the recording’s original pitch. |
| `public float pitchJitter` | Symmetric pitch jitter for impact-driven audio. |
| `public Vector2 pitchRange` | Pitch endpoints for dynamic response, or bounds for random one-shots. |
| `public int priority` | Unity voice priority, 0..256. |
| `public float response` | Response speed for smoothed playback. |
| `public AudioRolloffMode rolloffMode` | Distance attenuation policy. |
| `public AudioSource source` | Optional dedicated AudioSource. Supplied sources remain user-owned. |
| `public float spatialBlend` | 0 = nonpositional, 1 = fully positional audio. |
| `public float spread` | Stereo spread in degrees. |
| `public float volume` | Playback gain. Loop sources use Unity’s source-volume range; one-shots apply this gain as their volume scale. |
| `public Vector2 volumeRange` | Low/high gain endpoints for intensity-driven sounds. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void RefreshConfiguration()` | Invalidates this settings block so registered sources reapply static spatial/routing edits at their next use. | — |
| `public void ApplyTo(AudioSource target)` | Applies mixer/spatial configuration once per registered source until refreshed; unregistered sources apply on each call. Does not start playback or replace dynamic gain/pitch. | — |
| `public float PitchAt(float activity)` | Maps normalized activity through Pitch Range and clamps to the supported pitch domain. | — |
| `public float RandomPitch()` | Returns a clamped random pitch using Pitch and Pitch Range. | — |
| `public AudioSource ResolveSource(Transform defaultParent, string name, bool loop, out bool created)` | Returns an assigned source, a source on Audio Anchor, or a generated child source. The created result identifies ownership: destroy only generated sources. | — |

## WiperAudioEntry

**Runtime/Effects/Audio/Modules/WipersAudio.cs**

Presentation or lifecycle contract for independent vehicle components.

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public string id` | Unique, case-sensitive ID used by EngineAudio's runtime API. |
| `public AudioClip LastStrokeClip { get; internal set; }` | Last assigned stroke clip for this entry; null until a configured clip is used. |
| `public AudioClip outwardClip` | Audio for the outward stroke; entry value is used when overrideAudio is true. |
| `public bool overrideAudio` | Uses this entry's clips, volume and pitch-synchronization policy instead of the module defaults. |
| `public AudioClip returnClip` | Audio for the return stroke; entry value is used when overrideAudio is true. |
| `public bool synchronizeAudioSpeed` | Fits clip duration to the entry's effective mechanical rate; otherwise uses pitch 1. Entry value is used when overrideAudio is true. |

## WipersAudio

**Runtime/Effects/Audio/Modules/WipersAudio.cs**

Optional shared and per-entry audio for wiper mechanisms.

**Inherits / implements:** [AudioModule](Audio.md#audiomodule).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public VehicleAudioSettings audioSettings` | Reusable [VehicleAudioSettings](Audio.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `public List<WiperAudioEntry> entries` | Per-wiper audio overrides addressed by the mechanism entry ID. |
| `public virtual AudioClip LastStrokeClip { get; protected set; }` | Read-only/resolved last stroke clip for Wipers. |
| `public AudioClip outwardClip` | Audio for the outward stroke; entry value is used when overrideAudio is true. |
| `public AudioClip returnClip` | Audio for the return stroke; entry value is used when overrideAudio is true. |
| `public bool synchronizeAudioSpeed` | Fits clip duration to the entry's effective mechanical rate; otherwise uses pitch 1. Entry value is used when overrideAudio is true. |
| `public Wipers wipers` | Assign the wipers Wipers component/asset used by WiperSwitchBinding. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public override void Configure(VehicleController owner)` | Stores the vehicle whose hover transition geometry should be displayed. | `owner` — Unity/application owner whose identity controls this relationship or resource. |
| `public virtual AudioSource GetAudioSource(string id = null)` | Returns the resolved shared voice when id is null, or the last resolved voice for a unique wiper ID. Returns null before playback or for an unknown ID. Generated voices are runtime state and are not stored in Audio Settings. | — |
| `public override void RenderAudio(Audio core, float deltaTime)` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | `core` — Owning audio or passenger core supplying shared context. `deltaTime` — Elapsed time in seconds supplied by the owning loop. |
| `public override void SuspendAudio()` | Suspends the channel's playback and active subscriptions/resources as implemented by that channel. | No arguments; no returned value. |
