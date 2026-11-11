.. _uvs-water--water-providers-and-effects:

Water providers and effects
===========================

Water sampling, visible rendering and hull presentation are separate layers. Configure them here, then tune surface-hull movement in :doc:`Boat </Boat>` or underwater movement in :doc:`Submarine </Submarine>`. A water mesh alone does not make the physics recognize an ocean.

.. _uvs-water--inspector-quick-start-connect-a-boat-to-water:

Inspector quick start: connect a boat to water
----------------------------------------------

1. Configure a Boat/Submarine vehicle under **Vehicle Controller > Setup > Drive mode**. Select a separate scene water object and add **Water Surface** through Add Component.
2. Set its position/Size and assign a Water Surface Profile asset created with **Create > UltraVehicleSystem > Water > Surface Profile**. Configure its optional renderer/material using the surface steps below; remove solid water-plane support when buoyancy should support the hull.
3. Select the vehicle root and add/expand **Modules > World > Water Interaction**. Drag the scene WaterSurface into **Water Provider** and fit the hull dimensions/settings. Do not assign the visible water material as a provider.
4. Apply/save and test flotation/immersion with small or zero waves. The same provider can serve several vehicles.
5. Add **Boat Water Audio** under Audio and **Boat Water Particles** under Effects only after the water state works. Assign their water/vehicle references and output anchors using :ref:`Add audio and particles <uvs-water--add-audio-and-particles>`.

.. _uvs-water--choose-the-water-arrangement:

Choose the water arrangement
----------------------------

+------------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| Arrangement                        | Provides                                                      | Use                                                    |
+====================================+===============================================================+========================================================+
| Profile fallback plane             | One flat height and optional X/Z bounds, no current           | First physics tests or deliberately flat water         |
+------------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| WaterSurface + WaterSurfaceProfile | Shared analytical wave samples and optional bundled rendering | A coherent finite water area without an external ocean |
+------------------------------------+---------------------------------------------------------------+--------------------------------------------------------+
| Custom WaterProvider               | Samples from your own ocean/river simulation                  | Integration with another renderer or water framework   |
+------------------------------------+---------------------------------------------------------------+--------------------------------------------------------+

Several vehicles can share one provider while retaining their own WaterInteraction, hull settings and effects. There is no requirement to duplicate the ocean component for every boat.

.. _uvs-water--set-up-a-water-surface:

Set up a water surface
----------------------

.. _uvs-water--bundled-provider-and-renderer:

Bundled provider and renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a water object at the intended mean world height and add ``WaterSurface``.
2. Set **Size** to the desired sampling extent, then inspect its placement/orientation relative to the playable area. Keep a horizontal, sensibly scaled surface for the height-based water model.
3. Assign a **Surface Renderer** with MeshFilter/MeshRenderer when it should render. Sampling can also be used independently of visible geometry.
4. Create a **Water Surface Profile** asset through **Create > UltraVehicleSystem > Water > Surface Profile** and assign it.
5. Assign a compatible **Material Override**, or retain the material already on the renderer.
6. Enable **Generate Grid** for the bundled finite grid, or disable it to keep your own mesh. Choose **Grid Cell Size** for wave detail versus geometry cost.
7. Keep solid collision off the visible water plane when buoyancy should provide support. Real seabed, docks and shore colliders remain separate.
8. On the vehicle root, add/register ``WaterInteraction``, assign **Water Provider** to this surface and configure the relevant drive profile.

The provider's finite Size is not the same as a fallback profile's unlimited-plane convention. A WaterSurface does not become infinite merely because a size component is zero. Keep actual sample bounds, visible extent and gameplay boundaries consistent.

.. _uvs-water--watersurfaceprofile-and-wave-behavior:

WaterSurfaceProfile and wave behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Wave A** and **Wave B** contain X/Z direction, wavelength in metres and amplitude in metres. **Wave Speed** affects their shared phase. CPU samples and the compatible shader use the same parameters so the hull and visible surface agree.

Begin with small/zero amplitudes, then add waves after hull behavior is stable. Ripple scale/strength, colors, roughness, reflection, depth absorption and shoreline foam primarily describe rendering. They are not additional independent physical displacement fields or terrain grip settings.

Without a style the surface samples flat water. With **Animate Waves** off, sampling/rendered wave amplitude is flat rather than a paused nonzero crest. A material that ignores the supplied shader properties can still display something different, so verify it against sampled height.

.. _uvs-water--flat-fallback-plane:

Flat fallback plane
~~~~~~~~~~~~~~~~~~~

With no explicit provider, Boat/Submarine profile fields **Water Level**, **Water Center** and **Water Size** define a flat world-height plane and X/Z rectangle. Centre is world X/Z; positive size values are full extent. A nonpositive size component permits an unlimited fallback area.

Keep **Use Profile Fallback** enabled on WaterInteraction if this is intended. Without a WaterInteraction component, compatible profiles can use their own fallback, but adding the explicit root component makes ownership/switches/effect hull dimensions easier to manage.

Use fallback for debugging before integrating an ocean. It does not read the position of an unrelated rendered plane automatically and carries no current/wave velocity.

.. _uvs-water--enable-or-disable-interaction:

Enable or disable interaction
-----------------------------

+---------------------------------------------+---------------------------------------------------------------+
| Control                                     | Effect                                                        |
+=============================================+===============================================================+
| WaterSurface.waterEnabled                   | Sampling and surface eligibility as a whole                   |
+---------------------------------------------+---------------------------------------------------------------+
| WaterSurface.renderSurface                  | Visibility without disabling sampling                         |
+---------------------------------------------+---------------------------------------------------------------+
| Animate Waves                               | Physical/visual analytical wave excitation                    |
+---------------------------------------------+---------------------------------------------------------------+
| Reflections Enabled / Depth Effects Enabled | Optional rendering features                                   |
+---------------------------------------------+---------------------------------------------------------------+
| WaterInteraction.waterInteractionEnabled    | Vehicle master water interaction, including buoyancy          |
+---------------------------------------------+---------------------------------------------------------------+
| Use Profile Fallback                        | Allows profile plane/bounds only when no provider is assigned |
+---------------------------------------------+---------------------------------------------------------------+
| Component enabled state                     | Normal Unity lifecycle of that provider/interaction/effect    |
+---------------------------------------------+---------------------------------------------------------------+

An explicitly assigned provider that is disabled, rejects a query or reports dry space does not silently fall back to another invisible ocean. Likewise, disabling an installed WaterInteraction stops sampling for that vehicle; it does not remove the component and reveal the fallback underneath.

Use ``SetInteractionEnabled`` and ``SetWaterProvider`` for public state changes/events. ``IsSubmerged``/``SubmergedChanged`` report the root centre-of-mass comparison with sampled surface height; they are not a full percentage of submerged hull volume or a per-propeller wet/dry test.

.. _uvs-water--hull-contact-dimensions-and-diagnostics:

Hull contact dimensions and diagnostics
---------------------------------------

**WaterInteraction > Hull Half Size** is half-width and half-length in metres for shared contact/effect geometry. A 2 m by 6 m footprint uses approximately ``(1, 3)``. It takes precedence over audio/particle components' fallback dimensions.

These dimensions locate bow/stern/side activity for audio/particles. They do not convert Boat into a multi-point displacement solver. Boat's Buoyancy Depth and Submarine's Hull Half Height remain the physics settings described in their own guides.

The shared contact readout includes water-relative velocity, horizontal/forward speed, roll/pitch activity and local entry speed at the hull sides. Hull rotation can therefore create a splash at one side even when centre-of-mass vertical speed is small.

Use ``WaterInteraction.TrySample`` or the provider's ``TrySample`` in diagnostic tools. A false result means no valid water; height zero can be valid water and must not be used as a failure flag. The :ref:`sample probe example <uvs-scripting-water--query-a-provider-from-an-application-tool>` reads those values without changing vehicle movement.

.. _uvs-water--add-audio-and-particles:

Add audio and particles
-----------------------

Shared Boat water effects consume Boat contact. They do not automatically render underwater Submarine wakes or flight spray. Keep the enabled Boat profile and valid water contact in the first presentation test.

.. _uvs-water--water-audio:

Water audio
~~~~~~~~~~~

1. Install the ``Audio`` core and ``BoatWaterAudio`` channel on the same vehicle GameObject.
2. Assign **Lapping Loop**, **Wake Loop** and optional **Splash Clips**.
3. Tune their volumes with mixer/spatial settings through the :doc:`audio workflow </Audio>`.
4. Set **Full Wake Speed** in m/s, **Full Lapping Motion**, **Splash Threshold** and **Splash Cooldown**.
5. Compare idle rocking, coasting and a stronger water entry.

Lapping follows physical hull/contact motion; wake follows relative speed. Splash threshold/cooldown avoid replaying a clip continuously for one sustained entry. Empty sound clips do not change buoyancy. **Water Sounds Enabled** suppresses this presentation channel independently.

.. _uvs-water--particle-channels:

Particle channels
~~~~~~~~~~~~~~~~~

Add ``BoatWaterParticles`` and assign **Vehicle**, **Engine**, **Spray Material** and **Foam Material**, or replace channel designs with **Propeller Prefab**, **Wake Prefab** and **Splash Prefab**.

+---------------------+---------------------------------------------------+----------------------------------------------+
| Channel             | Main trigger                                      | Important setup                              |
+=====================+===================================================+==============================================+
| Propeller spray     | Powered running engine and throttle activity      | Motor Outlet or vehicle-local Stern Offset   |
+---------------------+---------------------------------------------------+----------------------------------------------+
| Wake                | Water-relative hull speed, including coasting     | Full Effect Speed, Wake Rate and foam output |
+---------------------+---------------------------------------------------+----------------------------------------------+
| Hull entry splashes | Local inward water-entry speed at bow/stern/sides | Splash Entry Threshold / Full Entry Speed    |
+---------------------+---------------------------------------------------+----------------------------------------------+
| Hull ripples        | Low-speed surrounding activity                    | Hull Ripples Enabled / Hull Ripple Rate      |
+---------------------+---------------------------------------------------+----------------------------------------------+
| Running spray       | Speed-dependent bow-side droplets                 | Running Spray Factor                         |
+---------------------+---------------------------------------------------+----------------------------------------------+

Place **Motor Outlet** on the actual propulsion outlet; otherwise **Stern Offset** is the hull-relative fallback. Check the shared hull half-size before changing splash thresholds, since it affects the sampled side/bow/stern motion.

**Water Particles Enabled** is the whole visual switch. Propeller Enabled, Wake Enabled and Splashes Enabled select channels; disabling Wake also suppresses its surrounding ripples. Engine-off coasting can leave a wake, while powered propeller spray stops. These switches do not disable flotation.

Use CurrentPropellerRate, CurrentWakeRate and the corresponding diagnostics to distinguish a missing activity source from an invisible material. A tiny sustained rate may accumulate fractional emission instead of producing a burst every frame.

.. _uvs-water--budgets-and-distance:

Budgets and distance
~~~~~~~~~~~~~~~~~~~~

Propeller/Wake/Splash Budgets bound built-in output. **Cull Distance** suppresses distant presentation; zero disables this distance culling. Test the actual active camera and several boats, not just one close-up emitter.

Custom child systems/sub-emitters need their own sensible maximum particles/lifetimes; an application prefab can create more work than the parent channel's basic budget implies. General emitter ownership/render cost is covered in :doc:`Particles </Particles>`.

.. _uvs-water--use-another-ocean-or-river:

Use another ocean or river
--------------------------

Implement ``WaterProvider.TrySample(worldPosition, out sample)`` as an adapter. Return finite world height, a sensible world-space unit normal and water velocity in m/s, or false outside that water. Assign the adapter explicitly to the vehicle root's WaterInteraction.

The :ref:`complete bounded-current provider example <uvs-scripting-water--bounded-flat-water-with-a-current>` is a useful baseline: verify a known flat height/current before calling an external simulation. Replace the sample calculation, not the vehicle's whole input/movement pipeline.

Keep physics and visible water on the same coordinate/time convention. A shifted origin, milliseconds mistaken for seconds, local height returned as world height or a current in the wrong units can look like unstable buoyancy or depth hold. Reuse query data where its validity is known and avoid allocating an object per sample.

The bundled style supplies analytical wave motion, not an arbitrary river current. A custom provider is appropriate when horizontal flow or another ocean system must drive physical samples.

.. _uvs-water--rendering-and-performance:

Rendering and performance
-------------------------

The bundled renderer uses a finite grid, analytical wave displacement, ripple normals, environment reflection and optional depth tint/foam. Compatible shaders/materials are required for your render pipeline; the sampling API itself does not depend on that renderer.

**Depth Effects Enabled** consumes existing camera depth when available. WaterSurface does not force camera depth/opaque passes to exist. Configure the pipeline/camera appropriately; a missing depth input is not repaired by increasing shoreline foam. Reflection uses the environment/probe setup rather than creating an independent planar reflection camera.

**Grid Vertex Count** helps inspect geometry cost. Grid area and cell size together determine density; halving cell size across the same area can roughly quadruple cell count. An authored mesh with too few vertices cannot show detailed vertex waves merely because the shader samples a smaller wavelength.

Test multiple active hulls, entry/exit, distant effect culling and provider boundaries. Reduce unnecessary grid density, effect lifetime/rate and budgets before adding more emitters. See :doc:`Performance </Performance>` and :doc:`Demo resources </DemoResources>`.

.. _uvs-water--troubleshoot-shared-water:

Troubleshoot shared water
-------------------------

+------------------------------------------------------+----------------------------------------------------------------------+
| Symptom                                              | Inspect                                                              |
+======================================================+======================================================================+
| Visible ocean but hull falls                         | Assigned provider/sample result, interaction state and sample bounds |
+------------------------------------------------------+----------------------------------------------------------------------+
| Hull floats with water rendering off                 | Expected: renderSurface is independent of sampling                   |
+------------------------------------------------------+----------------------------------------------------------------------+
| Explicit dry provider still expected to use fallback | No fallback occurs through an assigned dry/disabled provider         |
+------------------------------------------------------+----------------------------------------------------------------------+
| Splash location wrong on a long hull                 | Hull Half Size and outlet geometry                                   |
+------------------------------------------------------+----------------------------------------------------------------------+
| Wave and hull phase disagree                         | Style/shader parameters, time and world-space sampling convention    |
+------------------------------------------------------+----------------------------------------------------------------------+
| No Submarine wake                                    | Shared boat contact effects are Boat-only                            |
+------------------------------------------------------+----------------------------------------------------------------------+
| Shoreline/depth appearance missing                   | Existing camera depth and compatible shader                          |
+------------------------------------------------------+----------------------------------------------------------------------+
| Custom ocean drifts wildly                           | Sample current units and surface velocity consistency                |
+------------------------------------------------------+----------------------------------------------------------------------+

For detailed runtime contracts and APIs, see :doc:`Water scripting </Scripting/Water>` and :doc:`API </API/Water>`.
