# Damage feedback API

See [setup, surfaces and examples](../DamageFeedback.md). Physics damage remains in [Damage](Damage.md).

## Types

- [DamageFeedback](#damagefeedback)
- [DamageAudio](#damageaudio)
- [DamageContact](#damagecontact)
- [DamageCue](#damagecue)
- [DamageSurface](#damagesurface)
- [DamageSurfaceQuery](#damagesurfacequery)
- [DamageSurfaceType](#damagesurfacetype)
- [IDamageSurfaceProvider](#idamagesurfaceprovider)
- [IDamageSurfaceResponseProvider](#idamagesurfaceresponseprovider)
- [DamageFeedbackProfile](#damagefeedbackprofile)
- [DamageSoundBank](#damagesoundbank)
- [DamageContactAudio](#damagecontactaudio)
- [DamageParticles](#damageparticles)
- [DamageAudio.PartDetachmentSound](#damageaudiopartdetachmentsound)
- [DamageContactRelay](#damagecontactrelay)
- [DamageContactEvent](#damagecontactevent)
- [DamageSoundEvent](#damagesoundevent)
- [DamageEffectEvent](#damageeffectevent)
- [DamageLandingAudioResponse](#damagelandingaudioresponse)
- [IDamageContactFilter](#idamagecontactfilter)
- [DamageContactLimiter](#damagecontactlimiter)
- [DamageSurfaceResponse](#damagesurfaceresponse)
- [DamageClipLayout](#damagecliplayout)
- [DamageSoundGroup](#damagesoundgroup)
- [DamageAudioResponseEvaluator](#damageaudioresponseevaluator)
- [DamageVolumeScale](#damagevolumescale)
- [DamageHitSoundEvent](#damagehitsoundevent)
- [DamagePartSoundEvent](#damagepartsoundevent)
- [DamageGroundImpactSettings](#damagegroundimpactsettings)

## DamageFeedback

**Runtime/Effects/Damage/DamageFeedback.cs**

Vehicle contact presentation API, configured separately from physical damage.

| Declaration | Meaning |
| --- | --- |
| `public event Action<DamageContact> Impacted` | An accepted impact, landing, compression or detachment response. |
| `public event Action<DamageContact> Scraped` | An active sliding-contact sample. |
| `public event Action Cleared` | Current contacts and presentation have been cleared. |
| `public event Action<DamageContact> Contacted` | Every accepted contact, including impacts and scraping. |
| `public event Action<DamageContact> TireImpacted` | Accepted wheel-strike contact; distinct from touchdown. |
| `public event Action<DamageContact> TireLanded` | Accepted wheel touchdown, including intensity and fall height. |
| `public event Action<DamageContact> SuspensionMoved` | Accepted spring/compression presentation cue. |
| `public event Action<DamageContact> PartBroken` | Accepted breakage presentation cue; use DamagePart.Detached for physical detachment. |
| `public event Action EffectsCleared` | Custom visual effect leases were cleared. |
| `public event Action<DamageContact> FallLanded` | Public event; see the setup guide for usage. |
| `public event Action<DamageContact> RolloverImpacted` | Public event; see the setup guide for usage. |
| `public event Action<DamageHit, DamageImpactProfile> EffectPlayed` | A pooled custom effect started. |
| `public DamageContactEvent onContact` | Configuration or state for this response; see the setup guide. |
| `public DamageContactEvent onImpact` | Configuration or state for this response; see the setup guide. |
| `public DamageContactEvent onScrape` | Configuration or state for this response; see the setup guide. |
| `public DamageContactEvent onTireImpact` | Inspector callback equivalent to TireImpacted. |
| `public DamageContactEvent onTireLanding` | Inspector callback equivalent to TireLanded. |
| `public DamageContactEvent onSuspension` | Inspector callback equivalent to SuspensionMoved. |
| `public DamageContactEvent onBreakage` | Inspector callback equivalent to PartBroken. |
| `public DamageContactEvent onFallLanding` | Public field; see the setup guide for usage. |
| `public DamageContactEvent onRolloverImpact` | Public field; see the setup guide for usage. |
| `public DamageEffectEvent onEffectPlayed` | Configuration or state for this response; see the setup guide. |
| `public UnityEngine.Events.UnityEvent onCleared` | Configuration or state for this response; see the setup guide. |
| `public UnityEngine.Events.UnityEvent onEffectsCleared` | Inspector callback equivalent to EffectsCleared. |
| `public DamageFeedbackProfile profile` | Configuration or state for this response; see the setup guide. |
| `public DamageFeedbackProfile[] surfaceResponses` | Additional response profiles used by code providers or future spawned targets. Scene Damage Surface profiles are discovered during configuration; sound-only overrides need no registration. |
| `public DamageParticles particles` | Configuration or state for this response; see the setup guide. |
| `public Damage damage` | Configuration or state for this response; see the setup guide. |
| `public DamageImpactProfile[] impactProfiles` | Configuration or state for this response; see the setup guide. |
| `public DamageImpactProfile fallbackImpactProfile` | Configuration or state for this response; see the setup guide. |
| `public bool impactEffectsEnabled` | Enable pooled particles/custom prefabs on accepted damage hits. Does not change damage, dents or sound. |
| `public int maximumEffectInstances` | Total prewarmed visual effect instances per vehicle. Profiles allocate their requested share in list order. |
| `public DamagePoolOverflow effectOverflow` | Skip a hit when its pool is busy, or replace that profile's oldest active effect. |
| `public bool contactsEnabled` | Configuration or state for this response; see the setup guide. |
| `public bool wheelContactsEnabled` | Configuration or state for this response; see the setup guide. |
| `public bool partContactsEnabled` | Configuration or state for this response; see the setup guide. |
| `public bool breakageEnabled` | Configuration or state for this response; see the setup guide. |
| `public int maximumContactPairs` | Fixed contact-cache capacity. Excess pairs replace the least recent; no collection grows on collisions. |
| `public override ExecutionPhase Phase { get; }` | Configuration or state for this response; see the setup guide. |
| `public override int ExecutionOrder { get; }` | Configuration or state for this response; see the setup guide. |
| `public int ActiveEffectCount { get; }` | Configuration or state for this response; see the setup guide. |
| `public int PlayedEffectCount { get; }` | Public property; see the setup guide for usage. |
| `public int DroppedEffectCount { get; }` | Public property; see the setup guide for usage. |
| `public int ImpactCount { get; private set; }` | Configuration or state for this response; see the setup guide. |
| `public int ScrapeCount { get; private set; }` | Configuration or state for this response; see the setup guide. |
| `public uint ContactRevision { get; }` | Public property; see the setup guide for usage. |
| `public void WarmUpEffects()` | Rebuild custom visual-effect pools outside the contact loop. |
| `public bool TryPlayEffect(DamageHit hit)` | Request a material-profile custom visual effect. |
| `public void SetImpactEffectsEnabled(bool value)` |  ------- Public API ------- |
| `public DamageImpactProfile ResolveImpactProfile(DamagePart part)` | Configuration or state for this response; see the setup guide. |
| `public DamageImpactProfile ResolveImpactProfile(DamageHit hit)` | Configuration or state for this response; see the setup guide. |
| `public void RegisterContactFilter(IDamageContactFilter filter)` | Register an external presentation rule; duplicate instances are ignored. |
| `public void UnregisterContactFilter(IDamageContactFilter filter)` | Stop applying a registered rule. |
| `public DamageSurfaceType ClassifyContact(DamageSurfaceQuery query)` | Resolve the inherited target surface or layer fallback. |
| `public DamageFeedbackProfile ResolveContactResponse(DamageSurfaceQuery query)` | Resolve an explicit copied-contact response, then a surface mapping, then the default profile. |
| `public void ClearState()` | Clear current contact state, active effects and sound tails. |
| `public void ClearEffects()` | Return custom visual effects to their prepared pool. |
| `public void SetContactsEnabled(bool value)` | Toggle native contact observation; disabling clears presentation history. External SubmitContact stays available. |
| `public void SetParticlesEnabled(bool value)` | Toggle built-in particle emission; disabling also clears existing particles. |
| `public DamageFeedbackProfile ResolveContactResponse(DamageContact contact)` | Resolve an explicit copied-contact response, then a surface mapping, then the default profile. |
| `public static DamageContact FromDamageHit(DamageHit hit)` | Configuration or state for this response; see the setup guide. |
| `public bool SubmitContact(DamageContact sample)` | Validate and dispatch copied contact data without changing vehicle physics; returns admission success. |
| `public override void Configure(VehicleController owner)` | Configuration or state for this response; see the setup guide. |
| `public void ResetVehicleState(VehicleResetReason reason)` | Configuration or state for this response; see the setup guide. |
| `public override void Step(VehicleController owner, Command command, float dt)` | Configuration or state for this response; see the setup guide. |

## DamageAudio

**Runtime/Effects/Damage/DamageAudio.cs**

Vehicle damage audio module. Native contacts, scripted damage and named-part cues share sound-bank configuration and pooled playback.

| Declaration | Meaning |
| --- | --- |
| `public event Action<DamageContact, AudioClip> Played` | The contact and actual selected audio clip. |
| `public event Action<DamageContact, AudioClip> ScrapeStarted` | A scrape lane became audible; carries the contact and original loop clip. |
| `public event Action<DamageContact, AudioClip> ScrapeStopped` | A scrape lane ended, changed material/group or was cleared; not each loop iteration. |
| `public event Action<DamageHit, DamageImpactProfile, AudioClip> DamagePlayed` | Scripted material-profile audio was accepted. |
| `public event Action<DamagePart, AudioClip> DetachmentPlayed` | A configured part-detachment cue played. |
| `public DamageFeedback feedback` | Configuration or state for this response; see the setup guide. |
| `public VehicleAudioSettings audioSettings` | Configuration or state for this response; see the setup guide. |
| `public DamageContactAudio contactAudio` | Configuration or state for this response; see the setup guide. |
| `public bool muteBodyPartOnDetach` | Let accepted one-shots and the current scrape iteration finish; ignore subsequent part impacts/scrapes after detachment. The detachment cue itself may still play. |
| `public DamageImpactProfile[] impactProfiles` | Optional material profiles for scripted damage. Empty reuses Damage Feedback's scripted profiles. Physical contacts use the feedback profile. |
| `public DamageImpactProfile fallbackProfile` | Configuration or state for this response; see the setup guide. |
| `public PartDetachmentSound[] detachmentSounds` | Configuration or state for this response; see the setup guide. |
| `public DamageSoundEvent onPlayed` | Configuration or state for this response; see the setup guide. |
| `public DamageHitSoundEvent onDamagePlayed` | Typed Inspector callback for scripted hit, selected profile and clip. |
| `public DamagePartSoundEvent onDetachmentPlayed` | Typed Inspector callback for the named part and its detachment clip. |
| `public DamageSoundEvent onScrapeStarted` | Typed Inspector callback equivalent to ScrapeStarted. |
| `public DamageSoundEvent onScrapeStopped` | Typed Inspector callback equivalent to ScrapeStopped. |
| `public AudioClip LastPlayedClip { get; private set; }` | Latest successful one-shot clip, retained after clearing sounds. |
| `public DamageContact LastPlayedContact { get; private set; }` | Copied contact belonging to LastPlayedClip. |
| `public bool HasPlayedContact { get; private set; }` | Whether a successful one-shot snapshot has been recorded. |
| `public virtual int ActiveVoiceCount { get; }` | Configuration or state for this response; see the setup guide. |
| `public int PlayedCount { get; }` | Configuration or state for this response; see the setup guide. |
| `public int DroppedCount { get; }` | Configuration or state for this response; see the setup guide. |
| `public int AllocatedVoiceCount { get; }` | Configuration or state for this response; see the setup guide. |
| `public void SetMuteBodyPartOnDetach(bool value)` | Set detached-part mute; accepted one-shots finish, subsequent contacts are rejected. |
| `public void SetContactAudioEnabled(bool value)` | Enable damage playback or immediately stop its one-shots and scrape loops. |
| `public bool PlayResponse(DamageSoundBank response, DamageContact contact, float volumeScale = 1)` | Play an explicit response through the shared selector, modulation and pooled voices. |
| `public virtual bool TryPlay(DamageHit hit)` | Request a scripted damage sound using the shared audio voice pool. |
| `public virtual void RefreshPartSounds()` | Configuration or state for this response; see the setup guide. |
| `public virtual DamageImpactProfile ResolveProfile(DamageHit hit)` | Configuration or state for this response; see the setup guide. |
| `public virtual DamageImpactProfile ResolveProfile(DamagePart part)` | Configuration or state for this response; see the setup guide. |
| `public virtual void WarmUp()` | Rebuild audio capacity and prewarm scripted-profile state outside the contact loop. |
| `public override void SuspendAudio()` | Configuration or state for this response; see the setup guide. |
| `public virtual void ClearSounds()` | Stop the audio channel and reset sound cooldowns. |
| `public override void Configure(VehicleController vehicle)` | Configuration or state for this response; see the setup guide. |
| `public override void RenderAudio(Audio core, float deltaTime)` | Configuration or state for this response; see the setup guide. |

## DamageContact

**Runtime/Effects/Damage/Contacts/DamageContact.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public readonly DamageCue Cue` | Configuration or state for this response; see the setup guide. |
| `public readonly DamagePart Part` | Originating damage part, if known; required for part-specific scrape muting. |
| `public readonly DamageFeedbackProfile ResponseProfile` | Optional target-specific sound and custom-effect response. |
| `public readonly bool HasDamageHit` | True for scripted damage routed through a copied DamageHit. |
| `public readonly DamageHit Hit` | Original scripted damage details when HasDamageHit is true. |
| `public readonly Vector3 Point` | World-space values in metres and seconds. |
| `public readonly Vector3 Normal` | World-space values in metres and seconds. |
| `public readonly Vector3 Tangent` | World-space values in metres and seconds. |
| `public readonly float Speed` | Configuration or state for this response; see the setup guide. |
| `public readonly float Load` | Configuration or state for this response; see the setup guide. |
| `public readonly float Mass` | Configuration or state for this response; see the setup guide. |
| `public readonly float Intensity` | Configuration or state for this response; see the setup guide. |
| `public readonly float FallHeight` | Descent height in metres for a wheel touchdown; zero when unavailable. |
| `public readonly PartMaterial Material` | Configuration or state for this response; see the setup guide. |
| `public readonly Transform Anchor` | Configuration or state for this response; see the setup guide. |
| `public readonly Transform Target` | Shared target identity supplied to external contact policies. |
| `public readonly IDamageContactFilter Filter` | Optional target-side admission rule for this contact. |
| `public readonly bool SparksAllowed` | Configuration or state for this response; see the setup guide. |
| `public readonly DamageSurfaceType SurfaceType` | Configuration or state for this response; see the setup guide. |
| `public DamageContact(DamageCue cue, Vector3 point, Vector3 normal, Vector3 tangent, float speed, float load, float mass, PartMaterial material, Transform anchor, float intensity, bool sparksAllowed = true, DamageSurfaceType surfaceType = DamageSurfaceType.Hard, DamagePart part = null, DamageFeedbackProfile responseProfile = null, DamageHit? damageHit = null, float fallHeight = 0, Transform target = null, IDamageContactFilter filter = null)` | Configuration or state for this response; see the setup guide. |

## DamageCue

**Runtime/Effects/Damage/Contacts/DamageContact.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

Values: `Body`, `TireImpact`, `LoosePart`, `Suspension`, `Breakage`, `Scrape`, `TireLanding`, `FallLanding`, `RolloverImpact`.

## DamageSurface

**Runtime/Effects/Damage/Surfaces/DamageSurface.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public DamageSurfaceType surfaceType` | Default surface, or attached surface when Separate Detached Surface is enabled. |
| `public bool allowSparks` | Disable for sand, grass, water-edge props or other surfaces that should never produce metallic sparks. |
| `public DamageFeedbackProfile responseProfile` | Optional sound banks and pooled custom impact effect for this target. Empty uses the vehicle defaults. Classification still controls Soft suppression. |
| `public float scrapeGain` | Scale sustained body-scrape audio/particle activity on this collider or its children. |
| `public bool useDetachedSurface` | Select a separate surface from the nearest parent Damage Part's detachment state. |
| `public DamageSurfaceType detachedSurfaceType` | Surface used while that part is detached. |
| `public DamageSurfaceType CurrentSurfaceType { get; }` | Effective attached/detached surface now. |
| `public void RefreshPart()` | Rediscover the owning Damage Part after reparenting the marker. Initial discovery is automatic. |
| `public DamageSurfaceType GetDamageSurfaceType(DamageSurfaceQuery contact)` | Configuration or state for this response; see the setup guide. |
| `public DamageFeedbackProfile GetDamageResponse(DamageSurfaceQuery contact)` | Configuration or state for this response; see the setup guide. |

## DamageSurfaceQuery

**Runtime/Effects/Damage/Surfaces/DamageSurface.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public readonly Collider VehicleCollider` | Configuration or state for this response; see the setup guide. |
| `public readonly Collider OtherCollider` | Configuration or state for this response; see the setup guide. |
| `public readonly Vector3 Point` | World-space values in metres and seconds. |
| `public readonly Vector3 Normal` | World-space values in metres and seconds. |
| `public readonly Vector3 RelativeVelocity` | Configuration or state for this response; see the setup guide. |
| `public readonly float NormalSpeed` | Configuration or state for this response; see the setup guide. |
| `public DamageSurfaceQuery(Collider vehicleCollider, Collider otherCollider, Vector3 point, Vector3 normal, Vector3 relativeVelocity, float normalSpeed)` | Configuration or state for this response; see the setup guide. |

## DamageSurfaceType

**Runtime/Effects/Damage/Surfaces/DamageSurface.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

Values: `Hard`, `Soft`, `Humanoid`, `Plastic`, `Glass`.

## IDamageSurfaceProvider

**Runtime/Effects/Damage/Surfaces/DamageSurface.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `DamageSurfaceType GetDamageSurfaceType(DamageSurfaceQuery contact)` | Configuration or state for this response; see the setup guide. |

## IDamageSurfaceResponseProvider

**Runtime/Effects/Damage/Surfaces/DamageSurface.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `DamageFeedbackProfile GetDamageResponse(DamageSurfaceQuery contact)` | Configuration or state for this response; see the setup guide. |

## DamageFeedbackProfile

**Runtime/Effects/Damage/Profiles/DamageFeedbackProfile.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public float minimumImpactSpeed` | Configuration or state for this response; see the setup guide. |
| `public float mediumImpactSpeed` | Configuration or state for this response; see the setup guide. |
| `public float heavyImpactSpeed` | Configuration or state for this response; see the setup guide. |
| `public float fullImpactSpeed` | Configuration or state for this response; see the setup guide. |
| `public float contactRetriggerTime` | Minimum separation from the previous hit on the same collider pair. New contact normals can retrigger a tumble impact. |
| `public LayerMask softLayers` | Fallback soft-object layers. An explicit Damage Surface or custom provider takes priority. |
| `public DamageSurfaceResponse[] surfaceResponses` | Default material-to-profile mappings; object response profiles take priority. |
| `public DamageImpactProfile impactEffect` | Optional pooled effect for this response. Register surface response profiles on DamageFeedback before play, or call WarmUpEffects after changing them. |
| `public DamageImpactProfile scrapeEffect` | Pooled prefab for ongoing sliding; its cooldown/lifetime control emissions. |
| `public DamageSoundBank bodyThud` | Low body-impact layer mixed under the material impact. Disable to use material sounds alone. |
| `public float impactPitchByStrength` | Pitch reduction as impact intensity rises, in addition to bank pitch variation. |
| `public float impactPitchByGlancing` | Pitch lift for grazing strikes compared with head-on impacts. |
| `public float glancingImpactGain` | Relative body-impact gain for a glancing strike. Head-on gain is one. |
| `public DamageSoundBank body` | Body-impact response, shared clips or Light/Medium/Heavy groups. |
| `public DamageSoundBank metalCrunch` | Configuration or state for this response; see the setup guide. |
| `public DamageSoundBank humanoid` | Body-impact recordings for Humanoid targets. |
| `public DamageSoundBank soft` | Configuration or state for this response; see the setup guide. |
| `public DamageSoundBank tireLanding` | Wheel touchdown recordings. |
| `public DamageSoundBank tireImpact` | Wheel strike recordings. |
| `public DamageLandingAudioResponse tireLandingResponse` | Dynamic touchdown gain and pitch/rate response. |
| `public DamageSoundBank suspension` | Configuration or state for this response; see the setup guide. |
| `public DamageLandingAudioResponse suspensionResponse` | Spring/compression gain and pitch response to normal approach speed, descent height and supported load. |
| `public DamageSoundBank glass` | Configuration or state for this response; see the setup guide. |
| `public DamageSoundBank plastic` | Configuration or state for this response; see the setup guide. |
| `public DamageSoundBank scrape` | Configuration or state for this response; see the setup guide. |
| `public float scrapeMinimumSpeed` | Configuration or state for this response; see the setup guide. |
| `public float scrapeFullSpeed` | Configuration or state for this response; see the setup guide. |
| `public float contactTimeout` | Time without a contact sample before its scraping loop fades. Includes sleeping bodies. |
| `public float scrapeAttack` | Configuration or state for this response; see the setup guide. |
| `public float scrapeRelease` | Configuration or state for this response; see the setup guide. |
| `public float suspensionMinimumStrokeSpeed` | Configuration or state for this response; see the setup guide. |
| `public float suspensionLoadRise` | Configuration or state for this response; see the setup guide. |
| `public Material sparkMaterial` | Configuration or state for this response; see the setup guide. |
| `public Material debrisMaterial` | Configuration or state for this response; see the setup guide. |
| `public Material glassMaterial` | Configuration or state for this response; see the setup guide. |
| `public float sparkMinimumSpeed` | Configuration or state for this response; see the setup guide. |
| `public float sparksPerSecond` | Configuration or state for this response; see the setup guide. |
| `public int impactDebrisCount` | Configuration or state for this response; see the setup guide. |
| `public DamageSoundBank fallLanding` | Public field; see the setup guide for usage. |
| `public DamageSoundBank rolloverImpact` | Public field; see the setup guide for usage. |
| `public DamageGroundImpactSettings groundImpacts` | Public field; see the setup guide for usage. |
| `public DamageFeedbackProfile ResponseFor(DamageSurfaceType surface)` | Return the configured material response, or null when no override exists. |

## DamageSoundBank

**Runtime/Effects/Damage/Profiles/DamageSoundBank.cs**

Single shared clip list or three strength groups, with independent volume and pitch modulation.

| Declaration | Meaning |
| --- | --- |
| `public bool enabled` | Enable this response. |
| `public bool avoidRepeat` | Avoid the previous recording when a valid alternative exists. |
| `public DamageClipLayout layout` | Shared clips or separate strength groups. |
| `public AudioClip[] clips` | Single-layout variations. |
| `public DamageSoundGroup light` | Weak-contact clip group. |
| `public DamageSoundGroup medium` | Medium-contact clip group. |
| `public DamageSoundGroup heavy` | Strong-contact clip group. |
| `public float mediumStrength` | Normalized boundary of Medium. |
| `public float heavyStrength` | Normalized boundary of Heavy. |
| `public float volume` | Common gain multiplied by the group gain. |
| `public float cooldown` | Minimum replay spacing in Single layout. |
| `public bool usePhysicalResponse` | Apply additional mass, angle and landing/suspension modifiers. |
| `public bool randomizePitch` | Use Pitch range rather than Fixed Pitch. |
| `public float fixedPitch` | Common pitch when randomization is disabled. |
| `public Vector2 pitch` | Common random pitch range. |
| `public float pitchJitter` | Optional additive random variation after the pitch curve. |
| `public bool modulateVolume` | Enable strength-driven volume. |
| `public DamageVolumeScale volumeScale` | Linear or perceived-energy volume interpolation. |
| `public float minimumGain` | Quietest relative impact gain. |
| `public AnimationCurve volumeByStrength` | Normalized strength to normalized volume response. |
| `public bool modulatePitch` | Enable strength-driven pitch/playback rate. |
| `public AnimationCurve pitchByStrength` | Pitch multiplier against normalized strength. |

## DamageContactAudio

**Runtime/Effects/Damage/Audio/DamageContactAudio.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public bool enabled` | Configuration or state for this response; see the setup guide. |
| `public bool impactSounds` | Enable body and Humanoid impacts, including wheel contact with a character. |
| `public bool tireImpactSounds` | Enable wheel strike audio independently. |
| `public bool tireLandingSounds` | Enable wheel touchdown audio independently. |
| `public bool fallLandingSounds` | Public field; see the setup guide for usage. |
| `public bool rolloverImpactSounds` | Public field; see the setup guide for usage. |
| `public bool scrapeSounds` | Configuration or state for this response; see the setup guide. |
| `public bool suspensionSounds` | Configuration or state for this response; see the setup guide. |
| `public bool breakageSounds` | Configuration or state for this response; see the setup guide. |
| `public int maximumVoices` | Configuration or state for this response; see the setup guide. |
| `public int PlayedCount { get; }` | Public property; see the setup guide for usage. |
| `public int DroppedCount { get; }` | Public property; see the setup guide for usage. |
| `public int AllocatedVoiceCount { get; }` | Configuration or state for this response; see the setup guide. |
| `public int ActiveVoiceCount { get; }` | Configuration or state for this response; see the setup guide. |
| `public void WarmUp()` | Rebuild audio capacity and prewarm scripted-profile state outside the contact loop. |
| `public void SuspendAudio()` | Configuration or state for this response; see the setup guide. |
| `public bool PlayResponse(DamageSoundBank response, DamageContact hit, float volumeScale = 1)` | Play a response using normalized contact strength and shared voice allocation. |

## DamageParticles

**Runtime/Effects/Damage/Visuals/DamageParticles.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public bool enabled` | Configuration or state for this response; see the setup guide. |
| `public bool sparksEnabled` | Configuration or state for this response; see the setup guide. |
| `public bool debrisEnabled` | Configuration or state for this response; see the setup guide. |
| `public bool glassEnabled` | Configuration or state for this response; see the setup guide. |
| `public int maximumParticlesPerSystem` | Configuration or state for this response; see the setup guide. |
| `public int maximumEmissionsPerStep` | Configuration or state for this response; see the setup guide. |
| `public int EmittedCount { get; private set; }` | Configuration or state for this response; see the setup guide. |
| `public void WarmUp()` | Rebuild audio capacity and prewarm scripted-profile state outside the contact loop. |
| `public void Clear()` | Public method; see the setup guide for usage. |

## DamageAudio.PartDetachmentSound

**Runtime/Effects/Damage/DamageAudio.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public bool enabled` | Configuration or state for this response; see the setup guide. |
| `public DamagePart part` | Configuration or state for this response; see the setup guide. |
| `public DamageSoundBank response` | Shared bank for the named part-detachment cue, played at full strength. |

## DamageContactRelay

**Runtime/Effects/Damage/Contacts/DamageContactRelay.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

## DamageContactEvent

**Runtime/Effects/Damage/Contacts/DamageSignals.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

## DamageSoundEvent

**Runtime/Effects/Damage/Contacts/DamageSignals.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

## DamageEffectEvent

**Runtime/Effects/Damage/Contacts/DamageSignals.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

## DamageLandingAudioResponse

**Runtime/Effects/Damage/Audio/DamageLandingAudioResponse.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public float fullImpactSpeed` | Normal approach speed in m/s for the strongest response. |
| `public float fullFallHeight` | Descent height in metres for the full height contribution. |
| `public float fullLoad` | Contact load in multiples of supported weight for the full load contribution. |
| `public float fullTravelSpeed` | Tangential speed relative to the surface, in m/s, for the full travel contribution. |
| `public Vector2 gain` | Gain multipliers from gentle to hard touchdown. |
| `public Vector2 pitch` | Pitch and playback-rate multipliers from gentle to hard touchdown. |
| `public float travelInfluence` | Bounded contribution from tangential travel; impact speed remains primary. |

## IDamageContactFilter

**Runtime/Effects/Damage/Contacts/IDamageContactFilter.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `bool AllowContact(DamageFeedback source, DamageContact contact)` | Return false to suppress contact presentation without changing physical collisions or damage. |

## DamageContactLimiter

**Runtime/World/Damage/DamageContactLimiter.cs**

A target-side implementation of IDamageContactFilter, shared by all of the target’s colliders. It has no dependency on character type.

| Declaration | Meaning |
| --- | --- |
| `public float contactSeparation` | Quiet gap allowing a new impact (default .35 seconds). |
| `public float repeatTime` | Minimum spacing during sustained impacts from one vehicle (default .8 seconds). |
| `public bool AllowContact(DamageFeedback source, DamageContact contact)` | Track a bounded, allocation-free history per vehicle. Suspension and scrape samples pass through. |
| `public void ClearState()` | Clear this target’s contact history. |

## DamageSurfaceResponse

**Runtime/Effects/Damage/Profiles/DamageFeedbackProfile.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public DamageSurfaceType surface` | Material to match. |
| `public DamageFeedbackProfile profile` | Sound banks, friction loop and particle/effect settings for that material. |

## DamageClipLayout

**Runtime/Effects/Damage/Profiles/DamageSoundBank.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

Values: `Single`, `StrengthGroups`.

## DamageSoundGroup

**Runtime/Effects/Damage/Profiles/DamageSoundBank.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public bool enabled` | Enable this strength group. |
| `public AudioClip[] clips` | Variations for this group. |
| `public float volume` | Multiplier on the bank Volume. |
| `public Vector2 pitch` | Multiplier range on the bank pitch. |
| `public float cooldown` | Minimum repeat spacing, independent of other groups. |

## DamageAudioResponseEvaluator

**Runtime/Effects/Damage/Audio/DamageAudioResponseEvaluator.cs**

Stateless volume and pitch evaluation shared by automatic and explicit playback.

| Declaration | Meaning |
| --- | --- |
| `public static bool Evaluate(DamageSoundBank bank, float strength, float variation, out float volume, out float pitch, bool loop = false)` | Calculate volume/pitch multipliers without selecting or playing a clip. Strength and random variation are normalized; loop volume fades to zero rather than using the impact gain floor. Returns false for disabled/invalid responses. |

## DamageVolumeScale

**Runtime/Effects/Damage/Profiles/DamageSoundBank.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

Values: `PerceivedEnergy`, `Linear`.

## DamageHitSoundEvent

**Runtime/Effects/Damage/Contacts/DamageSignals.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

## DamagePartSoundEvent

**Runtime/Effects/Damage/Contacts/DamageSignals.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.


## DamageGroundImpactSettings

**Runtime/Effects/Damage/Profiles/DamageGroundImpactSettings.cs**

See the [damage response setup](../DamageFeedback.md) for configuration and examples.

| Declaration | Meaning |
| --- | --- |
| `public LayerMask groundLayers` | Public field; see the setup guide for usage. |
| `public float minimumGroundNormal` | Public field; see the setup guide for usage. |
| `public bool includeDynamicGround` | Public field; see the setup guide for usage. |
| `public float minimumAirTime` | Public field; see the setup guide for usage. |
| `public float minimumFallHeight` | Public field; see the setup guide for usage. |
| `public float minimumLandingSpeed` | Public field; see the setup guide for usage. |
| `public float minimumRolloverSpeed` | Public field; see the setup guide for usage. |
| `public float minimumTilt` | Public field; see the setup guide for usage. |
| `public float minimumSpinSpeed` | Public field; see the setup guide for usage. |
| `public float fullImpactSpeed` | Public field; see the setup guide for usage. |
| `public float fullSpinSpeed` | Public field; see the setup guide for usage. |
| `public float spinInfluence` | Public field; see the setup guide for usage. |
| `public float impactInterval` | Public field; see the setup guide for usage. |
| `public float separationTime` | Public field; see the setup guide for usage. |
| `public float newFaceAngle` | Public field; see the setup guide for usage. |
| `public float settleTime` | Public field; see the setup guide for usage. |
