.. _uvs-scripting-boat--boat-dynamics:

Boat dynamics
=============

Boat motion combines support from displaced water, resistance relative to water flow and powered propulsion. The profile applies these to the vehicle's root rigidbody; the visible hull, propeller animation, wake and audio are consumers of that motion rather than its source.

Tune the system in that order: establish an appropriate floating waterline, tune unpowered settling/coasting, then add thrust and turning. This makes it possible to distinguish a buoyancy problem from excess drag or a purely visual trim effect.

.. _uvs-scripting-boat--implementation-map:

Implementation map
------------------

+----------------------+--------------------------------------------------------------------+
| Class                | Responsibility                                                     |
+======================+====================================================================+
| ``BoatProfile``      | Owns authored boat movement parameters and the profile behavior.   |
+----------------------+--------------------------------------------------------------------+
| ``Drive``            | Retains the vehicle's boat motion and sampling history.            |
+----------------------+--------------------------------------------------------------------+
| ``DrivePhysics``     | Contains shared movement calculations used by profiles.            |
+----------------------+--------------------------------------------------------------------+
| ``BoatRocking``      | Calculates the boat's trim/rocking response.                       |
+----------------------+--------------------------------------------------------------------+
| ``WaterInteraction`` | Connects vehicle water sampling and hull contact state.            |
+----------------------+--------------------------------------------------------------------+
| ``Propulsion``       | Animates propellers and rotors for aircraft, boats and submarines. |
+----------------------+--------------------------------------------------------------------+

``BoatProfile`` applies buoyancy, water-relative resistance, powered thrust and rudder torque. It reads shared provider samples where configured; fallback bounds supply a flat plane otherwise.

.. _uvs-scripting-boat--displacement-and-momentum:

Displacement and momentum
-------------------------

Water-relative velocity matters when a provider supplies a current. A hull drifting with the current should not experience the same resistance as one moving equally fast against it. Keep provider velocity in world metres per second and use the same sampling model for the visible water and physical boat.

The fallback plane is useful for a bounded flat-water scene. When an explicit provider is assigned, a failed sample means dry or unavailable water, not a request to silently use the fallback plane. Check shoreline behavior using the provider bounds as well as the rendered shoreline.

``waterLevel`` is the fallback unloaded waterline; ``buoyancyDepth`` controls displacement response and reserve support. ``verticalDamping`` controls heave. Engine-off boats retain buoyancy and passive resistance. Outside water there is no powered water motion or buoyancy.

Forward drag and quadratic speed resistance dissipate propulsion momentum. Lateral resistance separately reduces sideways drift. Yaw damping controls passive turn decay; powered rudder response approaches a bounded rate according to speed and stationary authority.

.. _uvs-scripting-boat--rocking-and-powered-trim:

Rocking and powered trim
------------------------

Trim is an orientation response layered around supported motion. Separate recovery from excitation: the spring/damper restores a pose, while acceleration, powered load and waves disturb it. Excessive excitation with weak recovery can look like unstable buoyancy even when the vertical support itself is well tuned.

For a diagnostic run, reduce ``rockingStrength`` and evaluate floating height, coasting and turning first. Restore trim gradually after the basic motion is understandable. Do not tune a wake particle effect as evidence of water contact; read the shared water state.

``rockingStrength`` scales maneuver trim and synthetic waves. A spring/damper supplies pitch/roll restoration. Acceleration tilt excites it from vehicle motion; sustained powered pitch builds/releases with load. Ambient waves and occasional impulses are separate layers. Zero ``rockingStrength`` disables these excitations while retaining buoyancy and propulsion.

``Drive`` retains acceleration, load, random and water-history state per vehicle. Configuration, discontinuities and loss of water reset the relevant history. Profile configuration is not shared transient simulation state.

.. _uvs-scripting-boat--input-and-helm:

Input and helm
--------------

The helm is presentation of the resolved steering actuator. The hull receives turning response from the profile; the cockpit wheel or handle displays the corresponding demand. This distinction lets an analog controller steer at partial magnitude without the visual helm inventing a separate full-left/full-right rule.

For a new input adapter, preserve analog/digital channel metadata in the command. For a new helm model, configure its animator/handle axis and range. For a different hull steering model, extend the boat profile instead. These are three distinct changes even when the visible symptom is “the boat turns wrong.”

Braking a boat supplies opposing powered intent rather than a road-wheel brake force. Check forward coasting, reverse thrust while still moving forward, and turning at low water-relative speed. These expose whether a custom input/presentation adapter is following actual propulsion intent or only hull velocity.

Explicit analog steering retains magnitude; digital/unspecified input uses rise/return times. The resolved steering actuator drives both hull turning and helm animation. Brake supplies opposing thrust; negative propulsion demand supplies reverse.

.. _uvs-scripting-boat--adjust-coasting-without-changing-effects:

Adjust coasting without changing effects
----------------------------------------

The sample changes the vehicle-local ``BoatProfile.forwardDragScale``, so the adjustment belongs to this boat's movement configuration. It does not edit an effect asset or a shared water provider. Reapplying configuration also makes the operation an explicit tuning boundary rather than a hidden continuous modifier.

Call ``Apply`` from a tuning UI after assigning a Boat vehicle. It edits the local mode and reapplies configuration. Other profile types are ignored.

**Example:** ``BoatCoastingControl.cs``

.. raw:: html

   <!-- example: BoatCoastingControl.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class BoatCoastingControl : MonoBehaviour
       {
           public VehicleController vehicle;
           [Min(0)] public float resistance = .5f;

           public void Apply()
           {
               if (!vehicle || !(vehicle.driveProfile is BoatProfile boat)) return;
               boat.forwardDragScale = resistance;
               if (!vehicle.TryApplyConfiguration(out var error))
                   Debug.LogWarning(error, vehicle);
           }
       }
   }

A lower value permits longer forward coast but does not remove other resistance. Check it with a consistent hull load and :doc:`water provider </Scripting/Water>`.

.. _uvs-scripting-boat--animate-a-boat-propeller:

Animate a boat propeller
------------------------

A presentation subclass is enough when the desired change is only “let this existing animation support another movement family.” The override keeps the base families and adds the boat case. Removing ``base.SupportsProfile(profile)`` would intentionally restrict the subclass to boats, which may be appropriate for an application-specific component.

After installing the component, configure the propeller's axis and demand flags from the model's intended motion. Hull reverse velocity and reverse propulsion intent are different states: a boat can still coast forward while reverse thrust is applied.

The base ``Propulsion`` component supports Helicopter, Airplane, Hover and Submarine, not Boat. Use a presentation subclass when a boat needs its mesh animation. Add this in place of ``Propulsion``, assign engine and propeller pivots, and configure the per-propeller demand flags. It changes supported presentation, not the Boat profile's thrust.

**Example:** ``BoatPropellerPresentation.cs``

.. raw:: html

   <!-- example: BoatPropellerPresentation.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class BoatPropellerPresentation : Propulsion
       {
           public override bool SupportsProfile(DriveProfile profile)
               => base.SupportsProfile(profile) || profile is BoatProfile;
       }
   }

.. _uvs-scripting-boat--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed boat movement API </API/Boat>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-boat--boatprofile:

BoatProfile
~~~~~~~~~~~

:ref:`BoatProfile <uvs-api-boat--boatprofile>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                               |
+============================================================================================+====================================================================================================================+
| ``public event System.Action<bool> SinkingChanged``                                        | Reports explicit sinking state changes once per transition.                                                        |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetBuoyancyEnabled(bool enabled)``                                   | Toggles gravity-derived flotation independently of water damping.                                                  |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetSinking(bool enabled)``                                           | Suspends or resumes configured upward flotation and damping; preserves the authored switches and current momentum. |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StartSinking()``                                                     | Starts sinking under native Rigidbody gravity without altering hull mass or teleporting.                           |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StopSinking()``                                                      | Resumes configured flotation at the current depth; does not force a separately disabled buoyancy switch on.        |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanUsePropulsionBoost(VehicleController vehicle)``                  | Checks the profile propulsion switch and required water/support context before activation.                         |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Resolves steering, samples water and applies buoyancy, water-relative resistance, thrust and trim/rocking.         |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ContainsWater(Vector3 position)``                                    | Checks whether a position lies inside this profile's fallback water region.                                        |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-boat--driveprofile:

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

.. _uvs-scripting-boat--freeprofile:

FreeProfile
~~~~~~~~~~~

:ref:`FreeProfile <uvs-api-driveprofiles--freeprofile>` gives the full declared contract.

+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Method                                                                                   | Role                                                                                |
+==========================================================================================+=====================================================================================+
| ``public override float ResolveDriveDemand(VehicleController vehicle, Command command)`` | Maps the command and strategy state to propulsion demand for surrounding mechanics. |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
