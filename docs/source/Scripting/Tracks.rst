.. _uvs-scripting-tracks--tracked-drive-and-belt-animation:

Tracked drive and belt animation
================================

Tracked movement uses wheel contacts grouped into left and right sides. The movement strategy distributes propulsion and turning demand between those sides. Belt meshes then animate from wheel motion along authored paths; they are not a chain of physical links driving the hull.

This architecture allows the mechanical wheel arrangement and rendered track model to differ in detail. The integration still needs a clear mapping: which native wheels belong to each side, which paths represent those sides and which mesh axis corresponds to forward belt travel.

.. _uvs-scripting-tracks--implementation-map:

Implementation map
------------------

+-----------------------+------------------------------------------------------------------+
| Class                 | Responsibility                                                   |
+=======================+==================================================================+
| ``TrackedProfile``    | Maps tracked propulsion/turning intent into movement behavior.   |
+-----------------------+------------------------------------------------------------------+
| ``Tracks``            | Owns explicit side membership and tracked support policy.        |
+-----------------------+------------------------------------------------------------------+
| ``TrackDrivePhysics`` | Calculates tracked torque/side-speed behavior.                   |
+-----------------------+------------------------------------------------------------------+
| ``TrackVisuals``      | Moves visible links and rollers from wheel motion.               |
+-----------------------+------------------------------------------------------------------+
| ``TrackPathBuilder``  | Prepares reusable closed paths during authoring.                 |
+-----------------------+------------------------------------------------------------------+
| ``Friction``          | Applies tire-friction behavior including tracked turning policy. |
+-----------------------+------------------------------------------------------------------+

.. _uvs-scripting-tracks--mechanical-sides:

Mechanical sides
----------------

Prefer explicit arrays for a reusable prefab. Geometric fallback is convenient for initial setup, but a model edit or unusual wheel placement can change which side a wheel appears to belong to. Reject duplicate membership during authoring rather than tuning around a wheel that receives no valid side assignment.

Track turning requires lateral slip. A model with unrestricted sideways grip can resist a pivot even when the left and right propulsion requests are correct. Diagnose side membership, engine budget and friction policy together; raising motor torque alone can hide an incorrect turn setup.

``Tracks`` stores explicit left/right ``WheelCollider`` arrays. If both are empty it uses geometric side fallback. A wheel on both sides, or outside explicit arrays, has no valid side. Configure membership in the Inspector rather than depending on object naming.

``TrackedProfile`` maps propulsion and pivot demand into the shared engine. A moving turn regulates different side speeds; a stationary pivot uses opposing targets. Steering compensation/redistribution remain bounded by the engine torque/power budget. Track visuals do not supply thrust.

``Friction`` permits lateral scrubbing during turns, with a low-speed launch policy. ``Tracks`` can add load/grip-limited lateral stability and oppose longitudinal drift during a pivot. Airborne/overturned unsupported hulls do not receive that support correction.

.. _uvs-scripting-tracks--set-explicit-wheel-sides:

Set explicit wheel sides
------------------------

The setup operation writes membership and then reapplies configuration so the relevant mechanics see a coherent wheel set. Use it after a generated vehicle has received its native wheel definitions. Do not place colliders from a trailer or nested vehicle in either array, even if they are visually near the same track.

If a damage system later changes wheel availability, use the vehicle's availability API. Side membership describes the mechanical layout; temporary availability describes which of those wheels currently participates.

Use this only during setup/spawn, after configuring the vehicle's wheel definitions. The arrays must contain operational wheels belonging to that vehicle.

**Example:** ``TrackSideSetup.cs``

.. raw:: html

   <!-- example: TrackSideSetup.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class TrackSideSetup : MonoBehaviour
       {
           public VehicleController vehicle;
           public Tracks tracks;
           public WheelCollider[] left;
           public WheelCollider[] right;

           public void ApplySides()
           {
               if (!vehicle || !tracks) return;
               tracks.leftWheels = left;
               tracks.rightWheels = right;
               if (!vehicle.TryApplyConfiguration(out var error))
                   Debug.LogWarning(error, vehicle);
           }
       }
   }

.. _uvs-scripting-tracks--belt-presentation:

Belt presentation
-----------------

``TrackVisuals`` moves existing links around prepared closed paths. Each side keeps a travel coordinate driven by native wheel rim speed, then evaluates link positions/orientations along the path. Links retain their authored offsets, so the path describes travel and the mesh supplies its own alignment.

``TrackPathBuilder`` is the authoring aid that prepares nodes from a segmented track model. It does not turn one continuous mesh into separate links or create a physical chain. Its rebuild should affect only nodes it owns. Assign its source links and destination carefully, and keep separate owned destinations for left and right sides.

``TryGetPathPoint`` can feed another application presentation, while ``AdvanceVisuals`` advances the built-in motion. A custom renderer can consume the path and speed without adding wheel forces. Keep path queries and advancement separate so sampling an effect position does not accidentally move the whole belt.

A path is expressed in the vehicle's local frame so hull translation does not change the track's authored shape. The visual system advances link travel along that shape and retains each link's model offset. It reads rim speed rather than throttle, so a belt can keep moving while the vehicle coasts or a wheel spins.

Verify path closure, ordering and travel sign with slow motion before using full vehicle speed. A reversed mesh forward axis is a presentation setup issue, not a reason to reverse mechanical propulsion on that side. Keep separate destinations/builders for each side so rebuilding one path cannot delete the other's nodes.

``TrackVisuals`` advances existing links along closed vehicle-local paths. Path/Links arrays describe corresponding nodes and links; each side reads native wheel rim speed and retains rest offsets/orientations. Travel Direction selects the animation sign. Extra Rollers use their own radii/axes.

Author/render links are independent from wheel contacts. See :doc:`tracked setup </Tracked>` for the workflow.

.. _uvs-scripting-tracks--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed tracked movement API </API/Tracks>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-tracks--driveprofile:

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

.. _uvs-scripting-tracks--ivehiclemodule:

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

.. _uvs-scripting-tracks--trackedprofile:

TrackedProfile
~~~~~~~~~~~~~~

:ref:`TrackedProfile <uvs-api-tracks--trackedprofile>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                           |
+============================================================================================+================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Ensures a Tracks component exists; explicit side membership remains vehicle-owned configuration.               |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Resolves engine output and side/pivot demand, then applies bounded tracked propulsion to the configured sides. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveDriveDemand(VehicleController vehicle, Command command)``   | Maps the command and strategy state to propulsion demand for surrounding mechanics.                            |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-tracks--tracks:

Tracks
~~~~~~

:ref:`Tracks <uvs-api-tracks--tracks>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                           |
+============================================================================================+================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Clears retained pivot state/blend before tracked movement resumes.                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies supported load/grip-limited lateral/pivot stabilization for an active tracked profile. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.           |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public virtual int SideOf(WheelCollider wheel)``                                         | Resolves a native wheel's left/right tracked-side membership.                                  |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

.. _uvs-scripting-tracks--trackvisuals:

TrackVisuals
~~~~~~~~~~~~

:ref:`TrackVisuals <uvs-api-tracks--trackvisuals>` gives the full declared contract.

+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Method                                                                              | Role                                                                                           |
+=====================================================================================+================================================================================================+
| ``public override void Configure(VehicleController owner)``                         | Caches vehicle/Tracks and prepares left/right belt paths and retained link poses.              |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                      | Checks movement-family compatibility; this is independent of the Unity enabled flag.           |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetPathPoint(Belt belt, int index, out Vector3 position)`` | Reads an interpolated point/orientation on a prepared belt path without advancing belt travel. |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public virtual void AdvanceVisuals(float deltaTime)``                             | Advances belt-link and roller presentation from the configured wheel motion.                   |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

.. _uvs-scripting-tracks--vehiclemodule:

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
