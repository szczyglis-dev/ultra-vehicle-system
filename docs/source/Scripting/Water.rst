.. _uvs-scripting-water--water-samples-and-adapters:

Water samples and adapters
==========================

A water provider adapts a water simulation to the vehicle's sampling contract. The vehicle asks for surface height, normal and water velocity at a world position. Boat and submarine movement consume those samples without depending on the rendering package that produced them.

``WaterInteraction`` is the vehicle-side connection to that provider. Water rendering, hull support and wake presentation are related through sampled state but have separate ownership, allowing an external ocean implementation to replace the sample source while preserving vehicle mechanics.

.. _uvs-scripting-water--implementation-map:

Implementation map
------------------

+------------------------+----------------------------------------------------------------------+
| Class                  | Responsibility                                                       |
+========================+======================================================================+
| ``BoatProfile``        | Consumes water support and flow for boat movement.                   |
+------------------------+----------------------------------------------------------------------+
| ``BoatWaterParticles`` | Uses hull-water contact for surface-water presentation.              |
+------------------------+----------------------------------------------------------------------+
| ``Drive``              | Retains per-vehicle hold targets and movement history.               |
+------------------------+----------------------------------------------------------------------+
| ``SubmarineProfile``   | Consumes water state for underwater movement.                        |
+------------------------+----------------------------------------------------------------------+
| ``WaterInteraction``   | Connects the active water movement family to sampling/contact state. |
+------------------------+----------------------------------------------------------------------+
| ``WaterProvider``      | Abstract sampling adapter and ``WaterSample`` data contract.         |
+------------------------+----------------------------------------------------------------------+
| ``WaterSurface``       | Built-in water-surface provider implementation.                      |
+------------------------+----------------------------------------------------------------------+

.. _uvs-scripting-water--sampling-contract:

Sampling contract
-----------------

``TrySample(Vector3 worldPosition, out WaterSample sample)`` describes one world location. Convert the external water package's values at this boundary:

+---------------------+----------------------------------------------------------------------------------+
| Value               | Contract                                                                         |
+=====================+==================================================================================+
| ``worldPosition``   | Query point in world space, in Unity metres.                                     |
+---------------------+----------------------------------------------------------------------------------+
| ``sample.height``   | Surface height in world coordinates. A height of zero can be valid water.        |
+---------------------+----------------------------------------------------------------------------------+
| ``sample.normal``   | Finite world-space unit normal of the sampled surface.                           |
+---------------------+----------------------------------------------------------------------------------+
| ``sample.velocity`` | World water-flow velocity, including relevant wave motion, in m/s.               |
+---------------------+----------------------------------------------------------------------------------+
| Return value        | ``true`` for a valid sample; ``false`` when the point has no valid water sample. |
+---------------------+----------------------------------------------------------------------------------+

Supplying local-space normals or current values in a different unit changes support and water-relative resistance. Convert once in the adapter rather than compensating in every vehicle profile.

Return ``false`` outside valid water or when the external system cannot supply a valid sample. This is a meaningful result. An assigned provider that reports dry should not be replaced by an infinite fallback plane, because doing so would make boats float beyond the actual water bounds.

``WaterProvider.TrySample`` returns height, a world-space unit normal and world water velocity, or ``false`` outside water. Supply finite values. Boat/Submarine sampling uses the vehicle's ``WaterInteraction``; assigned disabled/dry providers do not silently fall back. With no provider, ``useProfileFallback`` permits the profile plane/bounds.

``WaterInteraction`` reads only Boat/Submarine modes. Surface-boat audio/particles use its hull contact; submarine buoyancy sampling does not imply surface wake. ``WaterInteraction``'s master switch removes water physics too; disable effects on their own components when buoyancy should remain.

.. _uvs-scripting-water--bounded-flat-water-with-a-current:

Bounded flat water with a current
---------------------------------

The sample is deliberately independent of rendering: a rectangular X/Z area, one height and a constant flow vector. It is useful for checking an integration before introducing animated waves. Place several boats in the same region and give each its own ``WaterInteraction`` while sharing the provider.

For a third-party ocean, replace only the contents of ``TrySample`` with its supported query. Avoid allocating temporary objects for each query, because several sample points across several vehicles can be requested each physics tick. Cache provider-level data only when its lifetime and invalidation rules are understood.

Attach this provider to a water object, configure its world X/Z center/size and assign it to ``WaterInteraction``. Height and current are world-space values. The adapter supplies physics samples; rendering is separate.

**Example:** ``CurrentWaterProvider.cs``

.. raw:: html

   <!-- example: CurrentWaterProvider.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CurrentWaterProvider : WaterProvider
       {
           public float height;
           public Vector2 center;
           public Vector2 size = new Vector2(100, 100);
           public Vector3 current = new Vector3(1, 0, 0);

           public override bool TrySample(Vector3 position, out WaterSample sample)
           {
               sample = default;
               if (!isActiveAndEnabled || size.x <= 0 || size.y <= 0) return false;
               if (Mathf.Abs(position.x - center.x) > size.x * .5f ||
                   Mathf.Abs(position.z - center.y) > size.y * .5f) return false;
               sample = new WaterSample(height, Vector3.up, current);
               return true;
           }
       }
   }

For another ocean, query that package inside ``TrySample`` and preserve this contract. Its visible waves and sampled water should agree. Replace materials that depend on the bundled surface shader when using a different wave model.

.. _uvs-scripting-water--query-a-provider-from-an-application-tool:

Query a provider from an application tool
-----------------------------------------

A placement tool or diagnostic display can use the same provider contract as a vehicle. This example queries a configured world marker and stores the most recent result. It does not assume that a failed query means height zero, because zero can be a valid water height.

**Example:** ``WaterProbeReadout.cs``

.. raw:: html

   <!-- example: WaterProbeReadout.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class WaterProbeReadout : MonoBehaviour
       {
           public WaterProvider provider;
           public Transform probe;
           public bool HasWater { get; private set; }
           public WaterSample LastSample { get; private set; }

           public void Refresh()
           {
               HasWater = false;
               if (!provider || !probe || !provider.isActiveAndEnabled) return;
               if (!provider.TrySample(probe.position, out var sample)) return;
               LastSample = sample;
               HasWater = true;
           }
       }
   }

Read ``LastSample`` only when ``HasWater`` is ``true`` for the latest refresh. This example queries the provider directly; it does not apply ``WaterInteraction`` fallback or active-profile policy. Use the vehicle's own water integration when the desired question is whether that vehicle currently receives water support.

.. _uvs-scripting-water--height-and-depth-hold:

Height and depth hold
---------------------

The hold behavior is a feedback controller: it retains a target world height, compares that with the current vehicle height and applies available correction through the movement model. Submarine depth hold therefore does not track each passing wave or seabed distance. It therefore has different behavior from directly assigning the rigidbody's position. It can react gradually and remain affected by current, drag and limited thrust.

For a custom hold interface, feed the lift/hold-related intent through the supported input/profile path and display retained/actual state separately. A manual lift input can release or update the target, so an instrument should not assume that the target remains fixed while the pilot is actively commanding vertical motion.

A custom water provider should supply consistent samples before tuning hold response. Noisy height, inconsistent normals or an incorrect current unit can appear as a poorly tuned controller even if its response coefficients are reasonable.

A hold target is runtime state, not a shared profile setting. It represents where this particular vehicle is trying to remain. On a handover or reset, decide whether the application wants to preserve or reacquire that target; do not copy another vehicle's retained target as part of a tuning preset.

Hold authority remains bounded by powered support. It is not a positional lock on the rigidbody, so current and other physical effects can still act. A display should distinguish an enabled hold request from the vehicle having reached the requested altitude or depth.

Helicopter altitude hold and Submarine depth hold retain targets on ``Drive``, separately per vehicle. Lift input releases/updates the target. Holds require powered support and reset when leaving their applicable mode or after the relevant reset/configuration boundary. Submarine water resistance and flow remain active while hold corrects height.

.. _uvs-scripting-water--propeller-presentation:

Propeller presentation
----------------------

Choose animation demand according to the device. A main propeller may follow propulsion intent; a maneuvering thruster may follow steering, lift or pitch. RPM-driven motion expresses engine speed, while demand-gated motion expresses which actuator is active. These are separate presentation choices and can produce different results while coasting.

When debugging, verify mechanical motion using the profile and water samples first, then configure shaft direction and immersion gating. A stationary mesh does not prove missing thrust, and a spinning mesh does not prove the hull is inside valid water.

Base ``Propulsion`` applies to Helicopter, Airplane, Hover and Submarine. Its propellers can use engine RPM or a fixed base speed. See the :ref:`Boat extension <uvs-scripting-boat--animate-a-boat-propeller>` for that additional family. Only With Thrust gates/scales by selected demands; Reverse With Thrust uses propulsion intent, not hull velocity. Steering/Lift/Pitch flags add maneuver demand. Only In Water tests immersion for water vehicles. Instant Thrust Response bypasses the presentation response times.

These options animate shaft speed; they do not set physical thrust. Use drive-profile controls for movement and :doc:`water setup </Water>` for hull/effect authoring.

.. _uvs-scripting-water--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed water sampling and movement API </API/Water>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-water--driveprofile:

DriveProfile
~~~~~~~~~~~~

:ref:`DriveProfile <uvs-api-driveprofiles--driveprofile>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                              |
+============================================================================================+===================================================================================================================+
| ``public virtual Settings CreateSettings()``                                               | Returns a fresh initial shared settings object for explicit creation/profile selection.                           |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Configure(VehicleController vehicle)``                               | Empty base strategy setup hook; family implementations may ensure helpers and apply profile-owned settings.       |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Step(VehicleController vehicle, Command command, float deltaTime)`` | Abstract movement-strategy step called by Drive; apply the selected family's movement using this vehicle context. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public virtual DriveProfile Clone()``                                                    | Creates an independent serialized profile-configuration copy; configure it on its destination vehicle before use. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ResolveDriveDemand(VehicleController vehicle, Command command)``    | Maps the command and strategy state to propulsion demand for surrounding mechanics.                               |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ResolveExternalDriveIntent(VehicleController vehicle)``             | Returns signed non-wheel propulsion intent used by shared coasting/contact policy.                                |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-water--freeprofile:

FreeProfile
~~~~~~~~~~~

:ref:`FreeProfile <uvs-api-driveprofiles--freeprofile>` gives the full declared contract.

+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Method                                                                                   | Role                                                                                |
+==========================================================================================+=====================================================================================+
| ``public override float ResolveDriveDemand(VehicleController vehicle, Command command)`` | Maps the command and strategy state to propulsion demand for surrounding mechanics. |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. _uvs-scripting-water--ivehiclemodule:

IVehicleModule
~~~~~~~~~~~~~~

:ref:`IVehicleModule <uvs-api-modules--ivehiclemodule>` gives the full declared contract.

+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Method                                                                     | Role                                                                                                                        |
+============================================================================+=============================================================================================================================+
| ``void Configure(VehicleController vehicle)``                              | Repeatable setup contract supplied with the owning ``VehicleController``.                                                   |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``void Step(VehicleController vehicle, Command command, float deltaTime)`` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-water--submarineprofile:

SubmarineProfile
~~~~~~~~~~~~~~~~

:ref:`SubmarineProfile <uvs-api-water--submarineprofile>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                            |
+============================================================================================+=================================================================================================================+
| ``public override bool CanUsePropulsionBoost(VehicleController vehicle)``                  | Checks the profile propulsion switch and required water/support context before activation.                      |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveBoostDemand(VehicleController vehicle, Command command)``   | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Samples valid water, applies immersion-dependent buoyancy/resistance and powered movement/depth-hold response.  |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ContainsWater(Vector3 position)``                                    | Checks whether a position lies inside this profile's fallback water region.                                     |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-water--vehiclemodule:

VehicleModule
~~~~~~~~~~~~~

:ref:`VehicleModule <uvs-api-modules--vehiclemodule>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                                   |
+===========================================================================================+========================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                          | Role                                                                                                              |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-water--waterinteraction:

WaterInteraction
~~~~~~~~~~~~~~~~

:ref:`WaterInteraction <uvs-api-water--waterinteraction>` gives the full declared contract.

+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                       | Role                                                                                                                                                   |
+==============================================================================================================+========================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``                   | Samples the root center of mass and publishes a changed submerged/not-submerged state.                                                                 |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetInteractionEnabled(bool value)``                                                    | Changes the vehicle's water-interaction gate, affecting sampling/physics as well as its contact state.                                                 |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetWaterProvider(WaterProvider provider)``                                             | Replaces the assigned water adapter and publishes the provider change.                                                                                 |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySample(Vector3 worldPosition, out WaterSample sample)``                             | Queries valid water at a world position; ``false`` means no sample, not height zero.                                                                   |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static bool TrySampleSurface(VehicleController vehicle, Vector3 position, out WaterSample sample)`` | Queries the provider's surface sample through vehicle water policy.                                                                                    |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static WaterContact Read(VehicleController vehicle, Vector2 fallbackHalfSize)``                     | Builds surface-boat hull contact from the vehicle's water sampling and configured hull dimensions; non-Boat/dry/invalid vehicles return a dry contact. |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Event / callback                                               | Role                                                                                                             |
+================================================================+==================================================================================================================+
| ``public event System.Action<bool> InteractionEnabledChanged`` | When the master water-interaction gate changes. Payload: bool; the gate affects water physics, not just effects. |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<WaterProvider> ProviderChanged``  | When assigned water provider changes. Payload: ``WaterProvider``, possibly ``null``.                             |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> SubmergedChanged``          | When sampled body-center submergence changes. Payload: bool; this is not an arbitrary hull wetness percentage.   |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-water--waterprovider:

WaterProvider
~~~~~~~~~~~~~

:ref:`WaterProvider <uvs-api-water--waterprovider>` gives the full declared contract.

+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Method                                                                            | Role                                                                                 |
+===================================================================================+======================================================================================+
| ``public abstract bool TrySample(Vector3 worldPosition, out WaterSample sample)`` | Queries valid water at a world position; ``false`` means no sample, not height zero. |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _uvs-scripting-water--watersurfaceprofile:

WaterSurfaceProfile
~~~~~~~~~~~~~~~~~~~

:ref:`WaterSurfaceProfile <uvs-api-water--watersurfaceprofile>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Method                                                                                            | Role                                                                                                                  |
+===================================================================================================+=======================================================================================================================+
| ``public virtual WaterSample Sample(Vector3 position, float time, float baseHeight, bool waves)`` | Evaluates the configured water-wave style at a world position/time using base height and optional wave participation. |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-water--watersurface:

WaterSurface
~~~~~~~~~~~~

:ref:`WaterSurface <uvs-api-water--watersurface>` gives the full declared contract.

+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Method                                                                                        | Role                                                                                 |
+===============================================================================================+======================================================================================+
| ``public virtual void RenderSurface()``                                                       | Updates the built-in water surface's rendered representation.                        |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public override bool TrySample(Vector3 position, out WaterSample sample)``                  | Queries valid water at a world position; ``false`` means no sample, not height zero. |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual bool TrySampleAtTime(Vector3 position, float time, out WaterSample sample)`` | Queries the built-in water model at an explicit time for consistent wave evaluation. |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
