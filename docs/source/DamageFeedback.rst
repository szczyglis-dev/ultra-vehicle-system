.. _uvs-damagefeedback--damage-sounds-and-visual-effects:

Damage sounds and visual effects
================================

Use **Damage Feedback** and **Damage Audio** for impact sounds, scraping, breakage, sparks, fragments and landing sounds. Configure **Damage Feedback** alongside the other effects in **Vehicle Controller > Effects**, and **Damage Audio** in **Effects > Audio**. **Damage**, under the physics modules, continues to control damage amounts, deformation and detached parts. Turning presentation off does not change the vehicle's collision physics.

.. _uvs-damagefeedback--body-sounds-for-falls-and-rollovers:

Body sounds for falls and rollovers
-----------------------------------

In **Damage Feedback > Profile > Audio Responses**, **Fall Landing** is an additional body thud on the first qualifying ground contact after a height fall. **Rollover Impact** supplies subsequent qualifying tilted/spinning ground strikes. Both default to ``CrashMedium01`` and use the common bank volume/pitch curves. The first height landing takes priority over rollover audio for that same strike.

Configure **Ground Impacts** in the profile's landing-response settings:

+-----------------+-----------------------------------------------------------------------------------------------+
| Response        | Default minimums                                                                              |
+=================+===============================================================================================+
| Fall Landing    | 0.15 s airborne, 0.5 m descent and 3 m/s normal approach speed.                               |
+-----------------+-----------------------------------------------------------------------------------------------+
| Rollover Impact | 2.5 m/s normal approach speed, plus at least 35 degrees of tilt or 1.5 rad/s pitch/roll spin. |
+-----------------+-----------------------------------------------------------------------------------------------+

Contact speed includes rotational motion at the impact point, so a fast tumble can sound strong even with little forward speed. Full Impact Speed, Full Spin Speed and Spin Influence shape strength; the bank controls gain, pitch and random variation. Upright yaw-only donuts do not qualify as a tumble. Ground Layers, Minimum Ground Normal and Include Dynamic Ground select eligible ground; movable props/ragdolls are excluded by default.

Body colliders, attached panels (including hinged parts) and wheels share one contact history: several contacts from one impact do not multiply these sounds. Immediate rebounds do not replay Fall Landing; Rollover Impact can play once for each new qualifying strike. Replay/settling settings control separation, impact interval and when a fresh independent fall is armed. Detached debris does not count as the vehicle landing. The same recording selected by Body and a dedicated ground bank is not started twice on the same contact.

**Damage Audio > Contact Audio > Fall Landing Sounds / Rollover Impact Sounds** independently disable these layers. ``DamageFeedback.FallLanded`` / ``RolloverImpacted`` and Inspector ``onFallLanding`` / ``onRolloverImpact`` report the accepted cues, with contact position, intensity, part and fall height. Tire Landing and Suspension remain separate responses.

.. _uvs-damagefeedback--vehicle-setup:

Vehicle setup
-------------

1. Add **Damage Feedback** and **Damage Audio** to the vehicle root. Keep its **Audio** core enabled. The demo vehicles already include this setup.
2. Assign **Default Damage Feedback**, or create your own asset with **Assets > Create > UltraVehicleSystem > Damage > Feedback Profile**. The same profile supplies contact sound banks, thresholds and the default particle appearance.
3. In **Damage Feedback**, the profile and contact-source controls appear directly at the top. Expand **Particles** immediately below them to independently enable sparks, debris and glass. Particle and custom-effect capacities are limited by the Inspector settings.
4. In **Damage Audio**, the always-visible **Contact Audio** controls let you enable impact, scrape, suspension and breakage sounds independently and set voice capacity. **Mute Body Part On Detach** follows these controls; **Audio Settings** below it controls playback and routing for the shared pool. The Audio core supplies master volume, mixer routing and interior/underwater context.
5. **Mute body part on detach** is enabled by default. Once a part detaches, already accepted one-shots finish naturally, while later impacts or scraping are silent. An active scrape finishes its current clip iteration without looping again. The sound of detachment itself may still play. Disable this option to hear detached debris.

Body strikes on the roof, sides or underside use the impact banks; sustained sliding separately uses Scrape. Wheel strikes use **Tire Impact** and supported touchdowns use **Tire Landing**, with Suspension as a separate spring/compression cue. Disabling the Tire Feedback effect does not disable touchdown sounds supplied by the Suspension module.

Body impacts mix **Body Thud** underneath the Light, Medium or Heavy material bank. The body transient has priority over crunch and lamp breakage in a busy voice pool. Bank pitch provides random variation; **Impact Pitch By Strength**, **Impact Pitch By Glancing** and **Glancing Impact Gain** adjust the response to impact strength and incidence angle. Disable Body Thud to use the material sounds alone. **Minimum Gain** in each contact sound bank controls how much quieter weak accepted impacts can be; full intensity still uses the bank volume. The Tire Impact and Humanoid defaults retain a stronger minimum so they remain audible among engine sounds. Landing and suspension use their separate response curves. Body impacts use the Body response, with either a shared clip list or Light/Medium/Heavy groups. Metal impacts may add a crunch layer. Wheel strikes use **Tire Impact** and touchdowns use **Tire Landing**, while touchdown and loaded suspension movement use Suspension. Glass and plastic breakage follow the part's material. Scraping depends on sliding speed and contact load, and fades when contact ends. Quiet support contacts are ignored.

The contact thresholds use normal approach speed in metres per second, so a glancing hit need not sound like a head-on crash at the same road speed. Audio variations avoid immediately repeating the same clip where alternatives exist. Sound and particle pools are prepared during configuration; accepted contacts do not create new emitters or effect objects.

**Damage Audio > Contact Audio > Tire Impact Sounds** and **Tire Landing Sounds** independently enable wheel strikes and touchdowns. Both are enabled by default; **Impact Sounds** controls body and Humanoid hits, and **Suspension Sounds** controls spring/compression cues. Configure separate **Tire Impact** and **Tire Landing** banks in the Feedback Profile. From code, set ``damageAudio.contactAudio.tireImpactSounds`` or ``tireLandingSounds``; contact callbacks distinguish ``DamageCue.TireImpact`` and ``DamageCue.TireLanding``.

In the Feedback Profile, **Tire Landing Response** adjusts touchdown volume and pitch/playback rate from normal approach speed, fall height, contact load relative to supported weight, and speed along the landing surface. Impact speed is the main input; height and load refine it, and travel speed adds only a small contribution. **Gain** and **Pitch** specify gentle-to-hard multipliers; the Tire Landing bank still supplies its base volume and random pitch. A lower pitch also plays the clip more slowly. Native-contact fallbacks estimate descent height from normal approach speed when the suspension landing event is unavailable.

**Suspension Response** independently controls spring/compression volume and pitch from approach speed, fall height and supported load. Hard landings use a stronger, lower sound; gentle bumps remain quiet. A much stronger touchdown can replace the short suppression window of a preceding weak stroke. Suspension audio remains independent of the target material.

.. _uvs-damagefeedback--choose-clips-and-strength-response:

Choose clips and strength response
----------------------------------

Open **Damage Feedback > Profile > Audio Responses** and expand the response to edit. Every bank uses the same settings, including Plastic, Glass, wheels, suspension and scraping.

-  **Layout > Single** uses one shared clip list. It can contain one recording or several variations.
-  **Layout > Strength Groups** uses separate **Light**, **Medium** and **Heavy** lists. **Medium Strength** and **Heavy Strength** choose their boundaries on the normalized 0–1 contact-strength scale. Each group has its own enabled switch, volume multiplier, pitch multiplier range and cooldown.
-  **Volume** is the common gain. **Randomize Pitch** chooses a range; turn it off to set **Fixed Pitch**.
-  **Modulate Volume** enables **Minimum Gain** and **Volume By Strength**. The curve runs from the minimum gain at zero response to full gain at one response, using the selected **Volume Scale** (perceived energy or linear). **Modulate Pitch** enables the independent pitch/playback-rate curve; **Pitch Jitter** adds optional small variation. Both options work in either layout. Groups select the recordings; curves shape their playback.
-  **Use Physical Response** additionally applies vehicle mass, impact angle and the configured landing/suspension response. Turn it off for playback driven only by the bank settings and curves. Landing banks have their volume modulation disabled by default because their physical response already supplies the touchdown dynamics.

Body uses the three strength groups by default. Other bundled responses retain their existing recordings and playback levels. Body's shared clip list is also populated so switching it to Single works immediately. Group pitch and volume multiply the bank settings; a disabled or empty group is silent.

.. _uvs-damagefeedback--play-the-same-response-from-code:

Play the same response from code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: csharp

   DamageAudio audio = vehicle.GetComponent<DamageAudio>();
   DamageSoundBank response = audio.feedback.profile.plastic;
   var contact = new DamageContact(
       DamageCue.Body, hitPoint, hitNormal, Vector3.zero,
       impactSpeed, contactForce, vehicle.Body.mass,
       PartMaterial.Plastic, vehicle.transform, strength,
       surfaceType: DamageSurfaceType.Plastic);
   audio.PlayResponse(response, contact);

``strength`` is normalized from 0 to 1. This method uses the same clip layout, no-repeat selection, cooldowns, voice pool, positioning and Played notifications as automatic contacts. ``DamageAudioResponseEvaluator.Evaluate`` is also available for code that needs the bank's volume and pitch multipliers without playing audio. Keep the bank instance for reuse rather than constructing settings for each collision.

The same bank editor is used by **Damage Impact Profile > Sound** for scripted DamageHit responses and by **Damage Audio > Detachment Cues > Response**. Scripted profiles normalize their chosen metric between Minimum Impact and Maximum Impact before selecting a group. An explicit part-detachment cue uses full strength. Sound cooldown lives in the bank; the Impact Profile cooldown controls its custom visual effect.

.. _uvs-damagefeedback--set-the-target-surface:

Set the target surface
----------------------

**Damage Surface** is a component. Add it through **Add Component > Ultra Vehicle System > Effects > Damage > Damage Surface**, or the equivalent **Tools > Ultra Vehicle System > Add Component** submenu. Put it on the hit collider or a parent shared by its colliders.

-  **Hard** allows the usual impact banks and metallic scraping.
-  **Glass** uses the Glass bank and glass fragments on strong impacts/breakage, without metal crunch or sparks. The bundled Glass response silences its Light group so a tiny touch does not play a full shatter. Its scrape bank is disabled by default; assign a glass friction loop or Scrape Effect in its response profile to enable sliding feedback. Select it explicitly for glass props or panels; a Damage Part whose material is Glass also supplies this classification against ordinary hard surfaces.
-  **Plastic** uses the Plastic impact bank and its own scrape loop, without metallic crunch or built-in metal sparks. Both Car bumpers use Hard/metal while attached and Plastic after detachment. A part marked Plastic also uses this response against ordinary hard ground. Soft and Humanoid targets keep their own response.
-  **Soft** uses the Soft bank and suppresses the built-in metal/glass fragments, sparks and metallic scraping. Demo crates use Soft.
-  **Humanoid** uses its own dull body-impact bank without metallic scraping, sparks or glass. Put one Damage Surface on the character root shared by all its bone colliders. Demo mannequins already use this setup. **Damage Contact Limiter** on the character root groups its bone impacts. Its **Contact Separation** allows a new hit after a quiet gap, and **Repeat Time** limits repeated responses during sustained contact. Different vehicles are tracked independently. Humanoid impacts use **Impact Sounds** even when a wheel hits the character; disabling Tire Impact Sounds or Tire Landing Sounds does not silence that bank. Humanoid transients have primary-impact priority when the audio pool is busy.
-  **Allow Sparks** and **Scrape Gain** refine a Hard surface's response.
-  **Response Profile** optionally replaces its audio banks and custom impact effect. Leave it empty to use the vehicle's profile. Contact admission thresholds remain on the vehicle's profile.

For a new target material, create a Feedback Profile, choose its recordings and assign it to the target's Damage Surface. You do not need to modify package code. Shared recordings are in ``Resources/Audio/Damage``; their credits and licenses are in ``Resources/Audio/Credits.md``.

For a vehicle part, enable **Damage Surface > Separate Detached Surface** and choose **Attached Surface** and **Detached Surface** independently. The nearest parent Damage Part supplies its state automatically. Detachment switches the surface immediately; repair returns to the attached surface. Other objects keep their single Surface Type unless this option is enabled. Audio, particles and surface response selection use the current type; damage and deformation material settings are unchanged. **Response Profile**, **Allow Sparks** and **Scrape Gain** are shared between the two states. To use different banks/effects, map each type in the vehicle Feedback Profile and leave the object's Response Profile empty. If code reparents the marker to another part, call ``RefreshPart()`` once afterward.

In the default Feedback Profile, **Surface Responses** maps a material to a response profile. The bundled **Default Plastic Feedback** supplies Plastic impacts and friction audio. For another material response, create a Feedback Profile and choose its sound banks, **Scrape** loop and particle materials, then assign it in that list. An object's **Damage Surface > Response Profile** takes priority. This lets two objects of the same surface type have different sounds and effects.

**Impact Effect** selects a pooled prefab for impacts; **Scrape Effect** selects a pooled prefab for sustained sliding. Set the scrape effect's cooldown and lifetime so repeated emissions overlap naturally. Prefabs can contain particles, including material-specific sparks, or implement the effect interface. Plastic suppresses automatic metal sparks; explicitly assigned custom effects can still emit the particles you choose. Register profiles before play, or call ``WarmUpEffects()`` after adding new effects. Distinct particle materials are prepared in separate pools; contacts do not create particle systems.

Contact strength uses incoming velocity at the hit point, including rotation around the centre of mass and the contacted object's motion. A tumbling vehicle can therefore make a strong impact at low forward speed and after a small fall. Tire and suspension audio use this normal approach speed as well; height is an additional input, not a requirement for a hard impact.

The profile's **Impact Effect** can reference an Impact Profile containing a custom effect prefab. Scene Damage Surface profiles are prepared automatically when configuring the vehicle. For a code provider or a target spawned later, add the profile to **Damage Feedback > Surface Responses** before configuration, or call ``WarmUpEffects()`` after the target is created. This prewarms its custom effects within **Maximum Effect Instances**. The source prefab may use particles or implement ``IDamageImpactEffect``; ``PlayImpact`` starts the response and ``StopImpact`` returns it to rest. Soft and Humanoid surfaces can use such explicitly assigned custom effects, for example dust or cloth movement, while retaining suppression of built-in metallic effects.

For contacts submitted from code, pass the target’s ``DamageContactLimiter`` as the optional ``filter`` argument to ``DamageContact``, and its root as ``target``. For native contacts, the filter on the collider or nearest ancestor is discovered automatically. Grouping affects contact presentation callbacks and effects; physical collisions and damage remain unchanged.

Providers on parent objects are inherited. The nearest ``IDamageSurfaceProvider`` supplies Hard/Soft/Humanoid/Plastic/Glass classification; a provider may also implement ``IDamageSurfaceResponseProvider`` to choose a response profile from code. Provider identities are cached while a collider pair remains in contact. Call ``ClearState()`` after replacing providers or changing collider ancestry during contact. Already registered response profiles may be switched live; adding new custom effect prefabs requires ``WarmUpEffects()`` or ``vehicle.ApplyConfiguration()``.

.. _uvs-damagefeedback--custom-contact-rules:

Custom contact rules
--------------------

Damage Feedback accepts general external rules through ``IDamageContactFilter``. It contains no character-specific repeat limiter. Add **Damage Contact Limiter** through **Add Component > Ultra Vehicle System > World > Damage > Damage Contact Limiter** to any object with several colliders whose impacts should be grouped. The demo mannequins already have it.

To define your own rule, attach an implementation to the target collider or an ancestor:

.. code-block:: csharp

   using UltraVehicleSystem;
   using UnityEngine;

   public sealed class MyContactRule : MonoBehaviour, IDamageContactFilter
   {
       public bool AllowContact(DamageFeedback source, DamageContact contact)
       {
           // Example: omit presentation for contacts slower than 2 m/s.
           return contact.Speed >= 2f;
       }
   }

Alternatively, call ``feedback.RegisterContactFilter(rule)`` to apply a rule to the vehicle’s contacts, and ``feedback.UnregisterContactFilter(rule)`` when it should stop applying. Registering the same instance twice is harmless. Returning ``false`` suppresses contact effects, audio and presentation callbacks; it does not suppress physics or physical damage. A disabled/destroyed Behaviour filter is skipped. ``SubmitContact`` returns ``false`` for a filtered-out contact. Custom stateful filters can use ``source.ContactRevision`` to detect ``ClearState()`` and invalidate their history.

.. _uvs-damagefeedback--shared-events-and-api:

Shared events and API
---------------------

The **Signals and callbacks** foldouts also let you connect Inspector callbacks for contacts, impacts, scrapes, custom effects, clearing and selected audio clips. These mirror the C# events described below.

Subscribe to ``DamageFeedback.Contacted`` for every accepted presentation contact, or use ``Impacted`` and ``Scraped`` separately. Each receives a copied ``DamageContact`` describing position, normal, speed, intensity, part, surface type and optional surface response. ``DamageAudio.Played`` supplies that contact and the actual selected clip. ``DamageFeedback.EffectPlayed`` reports a pooled custom effect.

Use ``TireImpacted``, ``TireLanded``, ``SuspensionMoved`` and ``PartBroken`` when you only need one cue category; matching Inspector callbacks are ``onTireImpact``, ``onTireLanding``, ``onSuspension`` and ``onBreakage``. They run only after the contact passes filters. These are presentation notifications: ``PartBroken`` is not a replacement for the physical ``DamagePart.Detached`` event.

``DamageAudio.DamagePlayed`` and ``DetachmentPlayed`` also have typed Inspector callbacks (``onDamagePlayed``, ``onDetachmentPlayed``). ``ScrapeStarted`` / ``ScrapeStopped`` and their Inspector equivalents report the audible scrape loop lifecycle, rather than every solver sample or loop iteration. A stop can mean fading out, clearing, disabling or switching the loop's material/strength group. Up to two scrape lanes can be active. ``Played`` remains the one-shot notification; ``LastPlayedClip``, ``LastPlayedContact`` and ``HasPlayedContact`` retain its latest successful playback for diagnostics, including after clearing sounds.

Use ``SetContactsEnabled(false)`` to stop native observation and clear its history; explicit ``SubmitContact`` requests remain available. ``SetParticlesEnabled(false)`` also removes built-in particles already in flight. ``SetContactAudioEnabled(false)`` stops damage voices and scrape loops immediately, without changing the physical damage module. ``ResolveContactResponse(contact)`` resolves the explicit response, surface mapping and default profile for copied contact data. ``ClearEffects()`` clears custom visual leases and raises ``EffectsCleared`` / ``onEffectsCleared``; ``ClearState()`` additionally resets contact history and raises ``Cleared`` / ``onCleared``.

.. code-block:: csharp

   void OnEnable()
   {
       feedback.TireLanded += OnTireLanding;
       audio.ScrapeStarted += OnScrapeStarted;
   }

   void OnDisable()
   {
       feedback.TireLanded -= OnTireLanding;
       audio.ScrapeStarted -= OnScrapeStarted;
   }

   void OnTireLanding(DamageContact contact)
   {
       // Drive your own landing response from contact.Intensity and contact.FallHeight.
   }

   void OnScrapeStarted(DamageContact contact, AudioClip clip)
   {
       // Start your own surface-dependent feedback once this scrape becomes audible.
   }

Use ``Damage.Hit`` for gameplay damage and health logic. A physical collision can damage multiple parts; it does not need to play the same vehicle sound once for every damage notification. Scripted ``Damage.ApplyImpact`` calls also reach Feedback and Audio through the common response path.

.. raw:: html

   <!-- example: ObserveDamageResponse.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   public sealed class ObserveDamageResponse : MonoBehaviour
   {
       public DamageFeedback feedback;
       public DamageAudio damageAudio;

       private void OnEnable()
       {
           if (feedback) feedback.Contacted += OnContact;
           if (damageAudio) damageAudio.Played += OnSound;
       }
       private void OnDisable()
       {
           if (feedback) feedback.Contacted -= OnContact;
           if (damageAudio) damageAudio.Played -= OnSound;
       }
       private void OnContact(DamageContact contact)
       {
           // Use copied contact data for your own UI or already-prepared effects.
           if (contact.SurfaceType == DamageSurfaceType.Soft) { }
       }
       private void OnSound(DamageContact contact, AudioClip clip)
       {
           // clip is the recording actually selected by Damage Audio.
       }
   }

For your own collision source, call ``DamageFeedback.SubmitContact(contact)``. It validates the data and applies the same event, sound and effect routing without changing vehicle physics. Include **Part** when submitting a part contact so detached-part muting can identify it; use **LoosePart** for a detached impact. ``ClearState()`` clears current contacts and sound tails. ``DamageAudio.ClearSounds()`` stops audio only. ``WarmUp()`` rebuilds audio capacity; ``WarmUpEffects()`` rebuilds custom effect capacity. Do not rebuild pools for each hit.

.. raw:: html

   <!-- example: CustomDamageSurface.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   public sealed class CustomDamageSurface : MonoBehaviour,
       IDamageSurfaceProvider, IDamageSurfaceResponseProvider
   {
       public bool soft = true;
       public DamageFeedbackProfile response;

       public DamageSurfaceType GetDamageSurfaceType(DamageSurfaceQuery contact)
           => soft ? DamageSurfaceType.Soft : DamageSurfaceType.Hard;

       public DamageFeedbackProfile GetDamageResponse(DamageSurfaceQuery contact)
           => response;
   }

.. _uvs-damagefeedback--scripted-damage-and-part-cues:

Scripted damage and part cues
-----------------------------

**Damage Feedback > Scripted material responses** holds material Impact Profiles and a fallback. Each profile can select a built-in part material or a custom **Material Id**, set intensity thresholds and supply a pooled visual prefab. Damage Audio normally reuses these profiles for scripted damage, with optional sound overrides under **Scripted damage sounds**. A profile can carry both the visual effect and recordings for that scripted reaction.

**Damage Audio > Detachment cues** optionally assigns a sound to a specific part's actual Detached event. These are event cues; later contact sounds are governed by Mute Body Part On Detach. If using a custom feedback profile's own breakage bank, leave extra per-part cues empty unless a second layer is intentional.

.. _uvs-damagefeedback--included-assets:

Included assets
---------------

``Resources/Audio/Damage`` contains default audio for body impacts, soft-object impacts, scraping, glass, tires and suspension. ``Resources/Effects/Damage`` contains the default feedback profile, material Impact Profiles, particle prefabs and materials. Replace the profile's recordings or effects to suit your vehicle.

The shared damage particle materials have Built-in, URP and HDRP shader variants. They use the same material assets across these pipelines.

See the :doc:`Damage feedback API </API/DamageFeedback>` and :doc:`physics damage guide </Damage>`.

Material impact profiles and their fallback are configured in **Scripted material responses** at the bottom of Damage Feedback. Use ``DamageFeedback.impactProfiles``, ``DamageFeedback.fallbackImpactProfile`` and ``DamageFeedback.ResolveImpactProfile(...)`` from code.
