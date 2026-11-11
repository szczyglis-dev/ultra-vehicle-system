.. _uvs-scripting-audio--audio-ownership-and-extension:

Audio ownership and extension
=============================

Vehicle audio is organized as a core plus replaceable channels. The core dispatches channels and supplies default VehicleAudioSettings for custom channels; each built-in sound uses its own VehicleAudioSettings for playback and emitter routing. A channel reads vehicle state or events and manages its particular voices. Engine, tire, indicator and switch audio can therefore be configured or replaced independently.

An audio channel is a presentation consumer. It should use mechanical RPM, contact or accepted actions as inputs, rather than changing the engine or replaying input requests to infer what happened. This makes the same mechanic usable with a different sound implementation.

.. _uvs-scripting-audio--configure-in-the-inspector-first:

Configure in the Inspector first
--------------------------------

Start with :ref:`one engine loop <uvs-audio--inspector-quick-start-one-working-engine-loop>` or :ref:`collision/landing sound mappings <uvs-audio--inspector-quick-start-collision-and-landing-sounds>`. Add the Audio core and channel, assign clips/profiles and emitter anchors, then test the mechanic in Play Mode. Ordinary sound authoring does not require the extension classes below.

.. _uvs-scripting-audio--changing-spatial-audio-settings:

Changing spatial audio settings
-------------------------------

For sources registered with a vehicle Audio core, mixer routing, spatial blend, min/max distance, rolloff, Doppler, spread and priority are applied once. After changing those fields from code or the Play Mode Inspector, call ``settings.RefreshConfiguration()`` for that settings block, or ``audio.RefreshPlaybackConfiguration()`` to invalidate spatial settings across the core's sources. They are reapplied at the next loop update or sound playback; no restart is required. An unregistered AudioSource still receives settings on every explicit ``ApplyTo(source)`` call.

Volume/pitch modulation, mute/playback requests, source/anchor selection and camera/area/underwater context remain live. Context profiles continue to blend and restore their configured spatial baseline. Do not call configuration refresh every frame.

**Example:** ``SpatialAudioControl.cs``

.. raw:: html

   <!-- example: SpatialAudioControl.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public sealed class SpatialAudioControl : MonoBehaviour
       {
           public VehicleAudioSettings settings = new VehicleAudioSettings();
           public void SetAudibleDistance(float metres)
           {
               settings.maxDistance = Mathf.Max(settings.minDistance, metres);
               settings.RefreshConfiguration();
           }
       }
   }

.. _uvs-scripting-audio--implementation-map:

Implementation map
------------------

+------------------------+--------------------------------------------------------------------------+
| Class                  | Responsibility                                                           |
+========================+==========================================================================+
| ``Audio``              | Owns channel discovery, common audio settings and render-frame dispatch. |
+------------------------+--------------------------------------------------------------------------+
| ``AudioModule``        | Base channel with source creation, loop update and cleanup helpers.      |
+------------------------+--------------------------------------------------------------------------+
| ``DamageAudio``        | Separate Effects module for damage sound presentation.                   |
+------------------------+--------------------------------------------------------------------------+
| ``EngineAudio``        | Selects and modulates the engine loop and ignition transitions.          |
+------------------------+--------------------------------------------------------------------------+
| ``EngineSoundProfile`` | Stores engine sound behavior and asset configuration.                    |
+------------------------+--------------------------------------------------------------------------+
| ``IndicatorAudio``     | Follows actual indicator output phase.                                   |
+------------------------+--------------------------------------------------------------------------+
| ``TireAudio``          | Consumes per-wheel contact/effect-surface state.                         |
+------------------------+--------------------------------------------------------------------------+

.. _uvs-scripting-audio--core-and-channels:

Core and channels
-----------------

Use ``AudioModule`` for a channel that belongs to the audio core's lifecycle. Its ``RenderAudio`` callback runs in the render-frame flow, which is appropriate for smooth volume and pitch changes. Do not schedule the same channel from ``Update`` as well, or its smoothing and playback logic will advance twice.

Use an event subscription when the signal is a discrete transition such as a settled switch click. Use a continuously read state for a loop such as engine RPM. In either case, release subscriptions and owned sources when the channel stops participating; an invisible or disabled vehicle should not leave orphaned voices behind.

``Audio`` supplies default settings for custom sources and advances its local ``AudioModule`` channels once per render frame. Each built-in sound stores its playback configuration in Audio Settings. A channel creates sources through its core and owns cleanup. Core/channel disable suspends playback. ``DamageAudio`` is a separate Effects module; not every sound-producing component is an ``AudioModule`` channel.

.. _uvs-scripting-audio--independent-engine-sounds:

Independent engine sounds
-------------------------

``EngineAudio.items`` contains independent ``EngineAudioItem`` configurations. Each item has a unique ID, active switch, profile or override clip, source anchor, engine/spool references, pitch/load response, ignition settings. Several items may play simultaneously, including several references to the same shared profile. Runtime voices and filter state belong to the channel, not the profile asset.

Use ``TryGetItem``/``GetItem`` to edit one item. Playback/item changes are read on the next render; spatial/routing edits follow the explicit refresh rules below. ``SetItemActive(id, false)`` stops that item's voices immediately. ``SetItemAnchor`` moves generated sources using the item origin without restarting playback; independently configured cue anchors take precedence. ``AddItem`` rejects null items, empty IDs and duplicates. ``RemoveItem`` unsubscribes and destroys only that item's generated sources. Direct list edits are synchronized automatically during rendering; ``RefreshItems`` can apply structural edits immediately. IDs are case-sensitive; missing or ambiguous IDs return failure/null rather than selecting an arbitrary item.

An item's ``loopOverride`` takes precedence over its profile loop. Without a profile, that same override provides an independent recording using the item's fallback volume and pitch settings. ``reactToPitch = false`` holds ``audioSettings.pitch``; RPM, motion and spool cannot change it. ``reactToEngineActivity = false`` removes activity-dependent gain/tone changes, while propulsion spool can still scale volume. Turn off ``followPropulsionSpool`` to follow engine running state and ordinary start delay instead.

Assigned profile start/stop clips and volumes take priority over the item's local ignition fallback. ``overrideIgnitionClips`` explicitly selects the local pair instead. Item activation, mode changes and restoring presentation do not invent ignition events. ``engineLoopStartDelay`` applies to real running-state transitions for ordinary loops; supported propulsion loops follow spin-up/down.

``SelectItem(id)`` selects one item exclusively; ``SetItemActive(id, active)`` changes one independently so multiple rotors/layers may remain enabled. Missing or duplicate IDs do not change selection. Engine Audio does not read ProfileSwitcher. The Porsche demo helper listens to its profile-change event and calls SelectItem with the current slot ID (``Drive`` or ``Hover``).

Use ``GetLoopSource``/``GetIgnitionSource`` for a generated source and ``TryGetState`` for per-ID pitch, volume, playing state, selected recording, delay and ignition history. Channel-wide properties provide summaries: loop volume is summed, playing means any loop, pitch averages playing loops, and tone cutoff reports the lowest enabled filter. An absent/not-yet-created source returns null.

**Example:** ``RotorAudioControl.cs``

.. raw:: html

   <!-- example: RotorAudioControl.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public sealed class RotorAudioControl : MonoBehaviour
       {
           [SerializeField] private EngineAudio engineAudio;

           public void SetRotorEnabled(bool enabled)
           {
               if (engineAudio) engineAudio.SetItemActive("Rotor1", enabled);
           }

           public void SetRotorGain(float gain)
           {
               if (engineAudio && engineAudio.TryGetItem("Rotor1", out var item))
                   item.profileAudioSettings.volume = Mathf.Max(0, gain);
           }

           public bool AddAuxiliaryLoop(AudioClip clip, Transform anchor)
           {
               return engineAudio && engineAudio.AddItem(new EngineAudioItem {
                   id = "auxiliary", loopOverride = clip, audioSettings = new UltraVehicleSystem.VehicleAudioSettings { audioAnchor = anchor, pitch = 1 },
                   reactToPitch = false,
                   reactToEngineActivity = false, playIgnitionSounds = false
               });
           }
       }
   }

.. _uvs-scripting-audio--listening-context:

Listening context
-----------------

Keep reusable configuration on ``Audio.context.profiles``; see :ref:`profile authoring <uvs-audio--camera-area-and-medium-profiles>`. Built-in loops and one-shots, including child-part receivers, share this layer. An empty profile list changes no recordings. Profiles filter by channel identity without editing channel settings or shared sound assets.

An external camera controller calls ``audio.SetListeningCamera(camera, module)`` when its listening view changes. The optional module identifies Interior/Orbit/custom vehicle views; omit it for an external view. ``UseAutomaticListeningCamera()`` restores vehicle-camera detection. ``SetAudioMedium("vacuum")`` selects a case-sensitive custom medium; null/empty restores water-provider detection. ``ListeningCamera``, ``ListeningView`` and ``AudioMedium`` expose the resolved context. ``RefreshAudioContext()`` reevaluates matching conditions; playback/rendering also does this automatically. It does not rebuild profile definitions.

Define **Audio > Context > Profiles** before startup. Existing profiles can be enabled or disabled during play without rebuilding them. To change a definition (levels, filters, channel, conditions or replacement clips), replace an entry, or add profiles from code, explicitly refresh the definitions:

Assign Audio Core and configure at least one profile before using this example.

.. raw:: html

   <!-- example: audio-profile-switch.cs -->

.. code-block:: csharp

   using UnityEngine;

   public sealed class AudioProfileSwitchExample : MonoBehaviour
   {
       public UltraVehicleSystem.Audio audioCore;

       public void SetProfileEnabled(bool enabled)
       {
           audioCore.context.profiles[0].enabled = enabled;
       }

       public void SetProfileGain(float gain)
       {
           audioCore.context.profiles[0].volumeMultiplier = gain;
           audioCore.RefreshAudioProfiles();
       }
   }

After assigning a new ``audio.context.profiles`` array from code, call the same refresh method. ``RefreshPlaybackConfiguration()`` refreshes profile definitions as well as static source routing/spatial settings. Master volume/pitch, listening-camera selection, context enable and existing profile enable switches remain live.

Custom ``AudioModule`` implementations use the inherited ``UpdateLoop``, ``PlayOneShot`` and ``PlayClip`` helpers. Apply ordinary ``VehicleAudioSettings`` and dynamic source gain/pitch before a one-shot; the helper selects replacements and applies context. For an external source, ``Audio.RegisterAudioSource(channel, source)`` associates channel scope, and ``ApplyAudioContext(channel, source)`` applies current modifiers. Source playback and destruction still belong to its owner. The context restores source/filter baselines before channel writes, so repeated updates do not compound gain or override engine-load filtering.

.. _uvs-scripting-audio--add-a-custom-loop-channel:

Add a custom loop channel
-------------------------

The example lazily creates one voice through ``CreateSource``, then reuses it. ``UpdateLoop`` receives the desired clip, volume, pitch and response factor. The exponential response factor uses ``dt`` so smoothing tracks elapsed time instead of depending on a fixed number of render frames.

The voice is channel-owned; the clip is an assigned asset. Deriving from ``AudioModule`` keeps the base cleanup behavior. If a subclass overrides lifecycle cleanup, retain the base work or provide equivalent release of every source it created.

Attach this beside ``Audio``, assign a loop clip, and refresh the core's audio modules. It creates one owned source and lets the core apply routing. Base lifecycle cleanup remains intact.

**Example:** ``AuxiliaryAudioLoop.cs``

.. raw:: html

   <!-- example: AuxiliaryAudioLoop.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class AuxiliaryAudioLoop : AudioModule
       {
           public AudioClip loop;
           [Range(0, 1)] public float volume = .2f;
           private AudioSource voice;

           public override void RenderAudio(UltraVehicleSystem.Audio core, float dt)
           {
               if (!voice) voice = CreateSource(core, "Auxiliary loop", true);
               UpdateLoop(core, voice, loop, loop ? volume : 0, 1,
                   1 - Mathf.Exp(-core.audioSettings.response * dt));
           }
       }
   }

Do not destroy externally assigned clips/mixers. See :doc:`event subscriptions </Scripting/Events>` for custom event-driven audio and :doc:`presentation </Scripting/Presentation>` for generated visual resources.

.. _uvs-scripting-audio--damage-impact-playback:

Damage impact playback
----------------------

DamageAudio.ResolveProfile(hit) selects an eligible response using its optional override list, the linked Damage Feedback configuration and fallback. ResolveProfile(part) only matches materials. TryPlay(hit) performs threshold, cooldown and voice-budget checks and returns whether a sound started. Played reports the copied DamageContact and selected AudioClip. DamagePlayed additionally reports the scripted DamageHit and material profile. Audio pitch and cooldown state belong to each DamageAudio instance, never the shared ScriptableObject.

WarmUp rebuilds voices and cached profile state after structural configuration changes. ClearSounds stops voices and resets cooldowns. Disabling the channel clears playback; enabling it again reuses its prepared sources. For the physical metadata contract and custom pooled effects, see :ref:`Damage scripting <uvs-scripting-damage--custom-impact-effect>`.

.. _uvs-scripting-audio--horn:

Horn
----

Add ``HornAudio`` beside the vehicle's Audio core. It follows the held ``Command.Horn`` flag independently of ignition, uses a spatial looping source and fades out on release. Channel mute, master audio suspension, disabling and vehicle deactivation stop the sound. Override Clip or leave Use Default Clip enabled for the bundled recording. The editor assigns the default recording as a serialized reference; runtime-created channels need an explicit Clip. The recording is in ``Resources/Audio``.

The road demo vehicles use **H** (hold) through KeyboardDriveInput.Horn Key, or **gamepad east face button (B/Circle)** through ActionInput. ActionInput.Horn can reference a custom action or PlayerInput action named Horn. AI/UI integrations can hold it with ``InputBuffer.SetHorn(true)`` and release with false. This is a continuous request, so release and loss of keyboard focus clear it. Keyboard/gamepad merged input preserves it.

.. _uvs-scripting-audio--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed audio cores and channels API </API/Audio>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-audio--audio:

Audio
~~~~~

:ref:`Audio <uvs-api-audio--audio>` gives the full declared contract.

-  ``public override void Configure(VehicleController owner)`` — Binds the component to its configured owner and selected source.

-  ``public virtual AudioSource CreateSource(string name, bool loop)`` — Current create source.

-  ``public virtual void EnsureModules(System.Func<System.Type, AudioModule> addChannel = null)`` — Current ensure modules.

-  ``public virtual float FilterCornerSqueal(float skid, bool corner, float deltaTime)`` — // Smooths cornering squeal separately from short slip spikes so tire audio does not chatter.

-  ``public virtual void PlayEvent(EffectEvent effect)`` — Current play event.

-  ``public virtual void RefreshAudioModules()`` — Current refresh audio modules.

-  ``public virtual void UpdateLoop(AudioSource source, AudioClip clip, float volume, float pitch, float blend, VehicleAudioSettings settings = null)`` — Current update loop.

-  ``public void SetListeningCamera(Camera camera, CameraModule module = null)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public void UseAutomaticListeningCamera()`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public void SetAudioMedium(string medium)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public void RefreshAudioContext()`` — Reevaluates camera, area and medium conditions against the prepared profile definitions.

-  ``public void RefreshAudioProfiles()`` — Applies edited/replaced profile definitions and replacement-clip lists; see :ref:`listening context <uvs-scripting-audio--listening-context>`.

-  ``public void RegisterAudioSource(AudioModule channel, AudioSource source)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public void UnregisterAudioChannel(AudioModule channel)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public AudioClip GetOriginalLoopClip(AudioSource source)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public AudioClip ResolveLoopClip(AudioModule channel, AudioSource source, AudioClip original)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public void ApplyAudioContext(AudioModule channel, AudioSource source)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public void RefreshPlaybackConfiguration()`` — Rebuilds audio profile definitions and reapplies static spatial/routing settings at the next use of each registered source.

-  ``public AudioClip PlayOneShot(AudioModule channel, AudioSource source, AudioClip original, float volume = 1)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

-  ``public AudioClip PlayClip(AudioModule channel, AudioSource source, AudioClip original)`` — See :ref:`listening context <uvs-scripting-audio--listening-context>` for selection and playback rules.

.. _uvs-scripting-audio--audiomodule:

AudioModule
~~~~~~~~~~~

-  **AudioModule** — ``public abstract void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.
-  **AudioModule** — ``public virtual void SuspendAudio()`` — Suspends the channel's playback and active subscriptions/resources as implemented by that channel.

.. _uvs-scripting-audio--audiosettingsoverride:

AudioSettingsOverride
~~~~~~~~~~~~~~~~~~~~~

:ref:`AudioSettingsOverride <uvs-api-audio--audiosettingsoverride>` gives the full declared contract.

.. _uvs-scripting-audio--boatwateraudio:

BoatWaterAudio
~~~~~~~~~~~~~~

-  **BoatWaterAudio** — ``public override void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.
-  **BoatWaterAudio** — ``public override void SuspendAudio()`` — Suspends the channel's playback and active subscriptions/resources as implemented by that channel.

.. _uvs-scripting-audio--brakeaudio:

BrakeAudio
~~~~~~~~~~

-  **BrakeAudio** — ``public override void Configure(VehicleController owner)`` — Resolves a missing channel source without replacing explicit assignments.

-  **BrakeAudio** — ``public override void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.

.. _uvs-scripting-audio--commercialaudio:

CommercialAudio
~~~~~~~~~~~~~~~

:ref:`CommercialAudio <uvs-api-audio--commercialaudio>` gives the full declared contract.

-  ``public override void RenderAudio(Audio core, float deltaTime)`` — Updates brake responses and the reversing alarm through the owning Audio core.
-  ``public override void SuspendAudio()`` — Stops commercial sounds and resets playback state.

.. _uvs-scripting-audio--damageaudio:

DamageAudio
~~~~~~~~~~~

See :doc:`setup and examples </DamageFeedback>` and the :ref:`full API <uvs-api-damagefeedback--damageaudio>`.

-  ``public event Action<DamageContact, AudioClip> Played``
-  ``public event Action<DamageHit, DamageImpactProfile, AudioClip> DamagePlayed``
-  ``public event Action<DamagePart, AudioClip> DetachmentPlayed``
-  ``public void SetMuteBodyPartOnDetach(bool value)``
-  ``public virtual DamageImpactProfile ResolveProfile(DamageHit hit)``
-  ``public virtual DamageImpactProfile ResolveProfile(DamagePart part)``
-  ``public virtual bool TryPlay(DamageHit hit)``
-  ``public override void Configure(VehicleController vehicle)``
-  ``public virtual void WarmUp()``
-  ``public virtual void RefreshPartSounds()``
-  ``protected override void OnEnable()``
-  ``protected override void OnDisable()``
-  ``public override void RenderAudio(Audio core, float deltaTime)``
-  ``public override void SuspendAudio()``
-  ``public virtual void ClearSounds()``

.. _uvs-scripting-audio--engineaudio:

EngineAudio
~~~~~~~~~~~

-  **EngineAudio** — ``public override void Configure(VehicleController owner)`` — Resolves a missing channel source without replacing explicit assignments.

-  **EngineAudio** — ``public virtual bool AddItem(EngineAudioItem item)`` — Adds a non-null item with a unique non-empty ID and prepares its engine subscription. Returns false for invalid or duplicate IDs/references.

-  **EngineAudio** — ``public virtual AudioSource GetIgnitionSource(string id)`` — Returns the generated start/stop source for the unique ID, or null before the first audible ignition transition.

-  **EngineAudio** — ``public virtual EngineAudioItem GetItem(string id)`` — Returns the unique item matching ID, or null for a missing or ambiguous ID. Edits take effect on the next audio render.

-  **EngineAudio** — ``public virtual AudioSource GetLoopSource(string id)`` — Returns the generated loop source for the unique ID, or null if unresolved/not created. Playback settings are reapplied by the audio renderer.

-  **EngineAudio** — ``public virtual void RefreshItems()`` — Synchronizes directly edited/replaced lists with runtime voices and engine subscriptions. RenderAudio also synchronizes automatically; removed voices are released.

-  **EngineAudio** — ``public virtual bool RemoveItem(string id)`` — Removes the unique ID, unsubscribes its engine and releases only its generated sources. Returns false if ID is missing or ambiguous.

-  **EngineAudio** — ``public override void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.

-  **EngineAudio** — ``public virtual bool SelectItem(string id)`` — Exclusively activates the unique matching item and immediately stops all other items. Missing or ambiguous IDs return false without changing selection.

-  **EngineAudio** — ``public virtual bool SetItemActive(string id, bool active)`` — Sets one item active/inactive by ID. Inactive immediately stops its loop and ignition. Reactivation does not synthesize ignition. Returns whether ID resolved.

-  **EngineAudio** — ``public virtual bool SetItemAnchor(string id, Transform anchor)`` — Changes one item's origin and reparents existing sources without restart. Null restores Audio core origin. Returns whether ID resolved.

-  **EngineAudio** — ``public virtual bool SetItemProfile(string id, EngineSoundProfile profile)`` — Replaces one item's reusable preset. Null selects override-only settings. Other items and shared assets are unchanged. Returns whether ID resolved.

-  **EngineAudio** — ``public override void SuspendAudio()`` — Suspends the channel's playback and active subscriptions/resources as implemented by that channel.

-  **EngineAudio** — ``public virtual bool TryGetItem(string id, out EngineAudioItem item)`` — Returns true and the unique matching mutable item. Empty, missing or duplicate IDs return false with a null item.

-  **EngineAudio** — ``public virtual bool TryGetState(string id, out EngineAudioItemState state)`` — Returns a snapshot of playing state, volume, pitch, selected loop, delay and ignition history for the ID. False means unresolved or not prepared.

.. _uvs-scripting-audio--enginesoundprofile:

EngineSoundProfile
~~~~~~~~~~~~~~~~~~

-  **EngineSoundProfile** — ``public virtual float EvaluateActivity(VehicleController vehicle, Engine engine)`` — Evaluates sound activity from the configured sound profile and mechanical input.
-  **EngineSoundProfile** — ``public virtual float EvaluatePitch(float activity)`` — Evaluates audio pitch from the configured engine sound response.

.. _uvs-scripting-audio--eventaudio:

EventAudio
~~~~~~~~~~

:ref:`EventAudio <uvs-api-audio--eventaudio>` gives the full declared contract.

-  ``public event System.Action<EffectEvent, AudioClip> Played`` — // Reports the accepted effect event and recording after playback starts.
-  ``public virtual void PlayEvent(EffectEvent effect)`` — Current play event.
-  ``public override void RenderAudio(Audio owner, float deltaTime)`` — Current render audio.
-  ``public override void SuspendAudio()`` — Current suspend audio.

.. _uvs-scripting-audio--hornaudio:

HornAudio
~~~~~~~~~

:ref:`HornAudio <uvs-api-audio--hornaudio>` gives the full declared contract.

-  ``public override void RenderAudio(Audio core, float deltaTime)`` — Current render audio.
-  ``public override void SuspendAudio()`` — Current suspend audio.

.. _uvs-scripting-audio--iaudiomodule:

IAudioModule
~~~~~~~~~~~~

-  ``void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.

.. _uvs-scripting-audio--indicatoraudio:

IndicatorAudio
~~~~~~~~~~~~~~

-  **IndicatorAudio** — ``public override void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.
-  **IndicatorAudio** — ``public virtual void SetClips(AudioClip on, AudioClip off)`` — Replaces indicator tick clips, retaining generated defaults for independently unassigned clips.
-  **IndicatorAudio** — ``public override void SuspendAudio()`` — Suspends the channel's playback and active subscriptions/resources as implemented by that channel.

.. _uvs-scripting-audio--movingpartaudio:

MovingPartAudio
~~~~~~~~~~~~~~~

:ref:`MovingPartAudio <uvs-api-audio--movingpartaudio>` gives the full declared contract.

-  ``public override void Configure(VehicleController owner)`` — Binds the component to its configured owner and selected source.
-  ``public virtual AudioSource GetMotionAudioSource(PartMotionEvent phase)`` — Returns the configured or owned audio source for the requested movement phase.
-  ``public virtual bool PlayMotionAudio(PartMotionEvent phase)`` — Plays the configured audio for the requested movement phase.
-  ``public override void RenderAudio(Audio core, float deltaTime)`` — Current render audio.
-  ``public virtual void StopMotionAudio()`` — Stops audio owned by this receiver.
-  ``public override void SuspendAudio()`` — Current suspend audio.

.. _uvs-scripting-audio--nitroaudio:

NitroAudio
~~~~~~~~~~

:ref:`NitroAudio <uvs-api-audio--nitroaudio>` gives the full declared contract.

-  ``public override void Configure(VehicleController vehicle)`` — Binds the component to its configured owner and selected source.
-  ``public override void RenderAudio(Audio core, float deltaTime)`` — Current render audio.
-  ``public override void SuspendAudio()`` — Current suspend audio.

.. _uvs-scripting-audio--profiletransitionaudio:

ProfileTransitionAudio
~~~~~~~~~~~~~~~~~~~~~~

:ref:`ProfileTransitionAudio <uvs-api-audio--profiletransitionaudio>` gives the full declared contract.

-  ``public override void Configure(VehicleController owner)`` — Binds the component to its configured owner and selected source.
-  ``public override void RenderAudio(Audio core, float deltaTime)`` — Current render audio.
-  ``public override void SuspendAudio()`` — Current suspend audio.

.. _uvs-scripting-audio--profiletransitionaudiotransitionsound:

ProfileTransitionAudio.TransitionSound
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`ProfileTransitionAudio.TransitionSound <uvs-api-audio--profiletransitionaudiotransitionsound>` gives the full declared contract.

.. _uvs-scripting-audio--switchaudio:

SwitchAudio
~~~~~~~~~~~

-  **SwitchAudio** — ``public override void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.

.. _uvs-scripting-audio--tireaudio:

TireAudio
~~~~~~~~~

-  **TireAudio** — ``public override void Configure(VehicleController owner)`` — Resolves a missing channel source without replacing explicit assignments.

-  **TireAudio** — ``public virtual float FilterCornerSqueal(float skid, bool highSpeedCorner, float deltaTime)`` — Filters or evaluates corner squeal using the tire-audio policy without changing tire physics.

-  **TireAudio** — ``public override void RenderAudio(Audio core, float deltaTime)`` — Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it.

-  **TireAudio** — ``public override void SuspendAudio()`` — Suspends the channel's playback and active subscriptions/resources as implemented by that channel.

.. _uvs-scripting-audio--vehicleaudiosettings:

VehicleAudioSettings
~~~~~~~~~~~~~~~~~~~~

-  **VehicleAudioSettings** — ``public void ApplyTo(AudioSource target)`` — Applies mixer/spatial configuration once per registered source until refreshed; unregistered sources apply on each call. Does not start playback or replace dynamic gain/pitch.
-  **VehicleAudioSettings** — ``public void RefreshConfiguration()`` — Invalidates this settings block for registered sources so static spatial/routing edits apply at their next use.
-  **VehicleAudioSettings** — ``public float PitchAt(float activity)`` — Maps normalized activity through Pitch Range and clamps to the supported pitch domain.
-  **VehicleAudioSettings** — ``public float RandomPitch()`` — Returns a clamped random pitch using Pitch and Pitch Range.
-  **VehicleAudioSettings** — ``public AudioSource ResolveSource(Transform defaultParent, string name, bool loop, out bool created)`` — Returns an assigned source, a source on Audio Anchor, or a generated child source. The created result identifies ownership: destroy only generated sources.

.. _uvs-scripting-audio--wiperaudioentry:

WiperAudioEntry
~~~~~~~~~~~~~~~

:ref:`WiperAudioEntry <uvs-api-audio--wiperaudioentry>` gives the full declared contract.

.. _uvs-scripting-audio--wipersaudio:

WipersAudio
~~~~~~~~~~~

:ref:`WipersAudio <uvs-api-audio--wipersaudio>` gives the full declared contract.

-  ``public override void Configure(VehicleController owner)`` — Binds the component to its configured owner and selected source.
-  ``public virtual AudioSource GetAudioSource(string id = null)`` — Current get audio source.
-  ``public override void RenderAudio(Audio core, float deltaTime)`` — Current render audio.
-  ``public override void SuspendAudio()`` — Current suspend audio.
