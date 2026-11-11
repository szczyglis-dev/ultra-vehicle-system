.. _uvs-inspectorreference-demo--demo-components-and-examples:

Demo components and examples
============================

:doc:`Back to the complete Inspector reference </InspectorReference>`.

+----------------------------------------------------------------------------------------------------------+------------------------+
| Component or data block                                                                                  | Settings declared here |
+==========================================================================================================+========================+
| :ref:`AimingHandDemo <uvs-inspectorreference-demo--aiminghanddemo>`                                      | 17                     |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`AircraftSystemsDemo <uvs-inspectorreference-demo--aircraftsystemsdemo>`                            | 7                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`AnimatorCarDemo <uvs-inspectorreference-demo--animatorcardemo>`                                    | 13                     |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`CameraRigDemo <uvs-inspectorreference-demo--camerarigdemo>`                                        | 2                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`CinematicCameraDemo <uvs-inspectorreference-demo--cinematiccamerademo>`                            | 11                     |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ControlsHudDemo <uvs-inspectorreference-demo--controlshuddemo>`                                    | 0                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`DamageControlsDemo <uvs-inspectorreference-demo--damagecontrolsdemo>`                              | 1                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`DayNightDemo <uvs-inspectorreference-demo--daynightdemo>`                                          | 3                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`DirectWaypointAIDemo <uvs-inspectorreference-demo--directwaypointaidemo>`                          | 8                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`DownforceModuleDemo <uvs-inspectorreference-demo--downforcemoduledemo>`                            | 1                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`EngineAudioModeDemo <uvs-inspectorreference-demo--engineaudiomodedemo>`                            | 0                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ExternalControlDemo <uvs-inspectorreference-demo--externalcontroldemo>`                            | 3                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ExternalControlDemo.GizmoSettings <uvs-inspectorreference-demo--externalcontroldemogizmosettings>` | 5                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`FreeCameraDemo <uvs-inspectorreference-demo--freecamerademo>`                                      | 0                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`FreeCameraMotionDemo <uvs-inspectorreference-demo--freecameramotiondemo>`                          | 3                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`FreeParentCameraDemo <uvs-inspectorreference-demo--freeparentcamerademo>`                          | 0                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`HudDemo <uvs-inspectorreference-demo--huddemo>`                                                    | 4                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`PassengerAccessDemo <uvs-inspectorreference-demo--passengeraccessdemo>`                            | 3                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`PowerWindowsDemo <uvs-inspectorreference-demo--powerwindowsdemo>`                                  | 6                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`TowingControlsDemo <uvs-inspectorreference-demo--towingcontrolsdemo>`                              | 1                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`UnderwaterDemo <uvs-inspectorreference-demo--underwaterdemo>`                                      | 8                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`VehicleSelectorDemo <uvs-inspectorreference-demo--vehicleselectordemo>`                            | 6                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`VehicleWeaponDemo <uvs-inspectorreference-demo--vehicleweapondemo>`                                | 8                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`WaterEntryAudioDemo <uvs-inspectorreference-demo--waterentryaudiodemo>`                            | 15                     |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`WaypointAIDemo <uvs-inspectorreference-demo--waypointaidemo>`                                      | 10                     |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`LandingGearSwitchDemo <uvs-inspectorreference-demo--landinggearswitchdemo>`                        | 4                      |
+----------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ProjectileDemo <uvs-inspectorreference-demo--projectiledemo>`                                      | 1                      |
+----------------------------------------------------------------------------------------------------------+------------------------+

.. _uvs-inspectorreference-demo--aiminghanddemo:

AimingHandDemo
--------------

Tutorial: acquire a seated hand through ``vehicle.handles.TryAcquire``, move a stable palm target, then cancel the token after the visible return. The controller owns admission and restores the home binding. Place the custom handle under the vehicle; call ``vehicle.handles.Refresh()`` when adding it at runtime. The optional weapon and cursor handling belong to the application. Vehicle Handles supplies SetInput before passenger work.

**Source:** ``Demo/Scripts/Controls/AimingHandDemo.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleHandle <uvs-inspectorreference-world--vehiclehandle>`. These settings also appear on this type.

+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                | Type                                                                            | Description                                                                                                | Declared default and constraints |
+========================+=================================================================================+============================================================================================================+==================================+
| ``aimDistance``        | ``float``                                                                       | Distance along the camera ray used as the aiming point, in metres. This does not change arm length.        | ``50``; Minimum: 1               |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``impactImpulse``      | ``float``                                                                       | Additional impulse applied by the demo ProjectileDemo when it hits a dynamic object.                       | ``12``; Minimum: 0               |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``muzzleSpeed``        | ``float``                                                                       | ProjectileDemo speed relative to the vehicle, in metres per second.                                        | ``90``; Minimum: 1               |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pistolPrefab``       | ``GameObject``                                                                  | Optional visual prefab. Its +Z axis points along the barrel; a child named Muzzle marks the bullet origin. | ``None / unassigned``            |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``posePistolThumb``    | ``bool``                                                                        | Temporarily point the active thumb along the pistol; restore its previous pose on return.                  | ``true``                         |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``projectileLifetime`` | ``float``                                                                       | ProjectileDemo lifetime in seconds; prevents missed bullets from accumulating.                             | ``5``; Minimum: .1f              |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``reach``              | ``float``                                                                       | Shoulder-to-wrist distance as a fraction of arm length. A small bend avoids a fully locked elbow.          | ``.98``; Range: .5f to .98f      |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``readInput``          | ``bool``                                                                        | Disable to drive SetMode, SetPointer and TryFire from your own input code instead.                         | ``true``                         |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``response``           | ``float``                                                                       | How quickly the raised hand follows a changing aim direction. Higher is faster.                            | ``12``; Minimum: 1               |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``seat``               | ``PassengerSeat`` (:ref:`fields <uvs-inspectorreference-world--passengerseat>`) | The occupied seat whose left or right hand we temporarily control.                                         | ``None / unassigned``            |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``shotInterval``       | ``float``                                                                       | Minimum time between accepted shots, in seconds.                                                           | ``.2``; Minimum: .02f            |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``shotSound``          | ``AudioClip``                                                                   | Optional single-shot sound. Played in 3D at the muzzle.                                                    | ``None / unassigned``            |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``thumbAimOffset``     | ``Vector3``                                                                     | Extra thumb direction adjustment in pistol-local Euler degrees. Zero points along the barrel.              | ``Zero-initialized Vector3``     |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``toggleKey``          | ``Key``                                                                         | Cycle Off -> Right -> Left -> Off.                                                                         | ``Key.Y``                        |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``transitionDuration`` | ``float``                                                                       | Seconds to raise the hand or return it to the original handle.                                             | ``.3``; Minimum: .05f            |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``viewCamera``         | ``Camera``                                                                      | Camera used to turn a screen position into a world-space aiming ray. Falls back to Camera.main.            | ``None / unassigned``            |
+------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--audio-settings:

Audio Settings
~~~~~~~~~~~~~~

+-------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Field             | Type                     | Behavior                                                                                                                                |
+===================+==========================+=========================================================================================================================================+
| ``audioSettings`` | ``VehicleAudioSettings`` | Shared playback, pitch, emitter and spatial settings. See :ref:`Audio Settings <uvs-inspectorreference-effects--vehicleaudiosettings>`. |
+-------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-inspectorreference-demo--aircraftsystemsdemo:

AircraftSystemsDemo
-------------------

**Source:** ``Demo/Scripts/Vehicles/AircraftSystemsDemo.cs``. Component / asset.

+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| Setting         | Type                                                                                  | Description                                                                                                                              | Declared default and constraints          |
+=================+=======================================================================================+==========================================================================================================================================+===========================================+
| ``dropKey``     | ``Key``                                                                               | Press to release the next eligible payload in Drop Objects through Dropper.                                                              | ``Key.M``                                 |
+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| ``dropObjects`` | ``DroppableObject[]`` (:ref:`fields <uvs-inspectorreference-world--droppableobject>`) | Payload objects checked in order when the drop key is pressed. Already released or unavailable entries are skipped.                      | ``System.Array.Empty<DroppableObject>()`` |
+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| ``dropper``     | ``ObjectDropper`` (:ref:`fields <uvs-inspectorreference-world--objectdropper>`)       | Payload release system used by the demo drop key. It releases the next eligible object from Drop Objects.                                | ``None / unassigned``                     |
+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| ``fireKey``     | ``Key``                                                                               | Hold to request rocket firing through Launcher. The launcher's own interval and remaining rockets control the actual shots.              | ``Key.Enter``                             |
+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| ``gear``        | ``LandingGear`` (:ref:`fields <uvs-inspectorreference-exterior--landinggear>`)        | Landing-gear system operated by the demo gear key and shown in its controls panel. Leave empty if this aircraft has no retractable gear. | ``None / unassigned``                     |
+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| ``gearKey``     | ``Key``                                                                               | Press to toggle landing-gear deployment. Retraction can still be refused by the gear's ground-safety lock.                               | ``Key.G``                                 |
+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| ``launcher``    | ``RocketLauncher`` (:ref:`fields <uvs-inspectorreference-world--rocketlauncher>`)     | Rocket launcher operated by the demo fire key. The controls panel also reads its remaining rocket count.                                 | ``None / unassigned``                     |
+-----------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+

.. _uvs-inspectorreference-demo--animatorcardemo:

AnimatorCarDemo
---------------

Select the F11 Car example and use its left-side panel in Play Mode to compare animated, IK and physical passenger ownership. Configure the driver seat with Parent attachment; wire the dedicated controller, wheel visual and three interactions below.

**Source:** ``Demo/Scripts/Vehicles/AnimatorCarDemo.cs``. Demo component.

+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting         | Type                          | Description                                                                                                                         | Declared default and constraints |
+=================+===============================+=====================================================================================================================================+==================================+
| ``controller``  | ``RuntimeAnimatorController`` | Humanoid graph with steering poses and masked gesture layers.                                                                       | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``leftLever``   | ``SwitchAnimator``            | Left switch mechanism toggled once on commit.                                                                                       | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``leftSwitch``  | ``ControlInteraction``        | Left-hand press, committed at its animation marker.                                                                                 | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rightLever``  | ``SwitchAnimator``            | Right switch mechanism toggled once on commit.                                                                                      | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rightSwitch`` | ``ControlInteraction``        | Right-hand press, committed at its animation marker.                                                                                | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``seat``        | ``PassengerSeat``             | Driver seat whose controller is changed from the example panel. Parent attachment keeps the animated driver aligned during driving. | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``steering``    | ``SteeringWheelAnimator``     | Visible steering angle used by the baked steering blend tree.                                                                       | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``     | ``VehicleController``         | Example car selected through the shared F11 fleet shortcut.                                                                         | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``wave``        | ``ControlInteraction``        | Left-hand wave and its masked animation layer.                                                                                      | ``None / unassigned``            |
+-----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

+------------------------+--------------------------------------------------------------------------------------+------------------------------------------+
| Additional setting     | Meaning                                                                              | Inspector path                           |
+========================+======================================================================================+==========================================+
| ``handles``            | Explicit handles switched independently of the passenger controller.                 | Animator Car Demo > Handles              |
+------------------------+--------------------------------------------------------------------------------------+------------------------------------------+
| ``waveHandle``         | Handle owning the authored wave gesture in built-in modes.                           | Animator Car Demo > Wave Handle          |
+------------------------+--------------------------------------------------------------------------------------+------------------------------------------+
| ``selectedSeatMode``   | Initial passenger strategy; Animator by default.                                     | Animator Car Demo > Selected Seat Mode   |
+------------------------+--------------------------------------------------------------------------------------+------------------------------------------+
| ``selectedHandleMode`` | Initial IK, Animator + IK, Animator or Custom handle selection; Animator by default. | Animator Car Demo > Selected Handle Mode |
+------------------------+--------------------------------------------------------------------------------------+------------------------------------------+

.. _uvs-inspectorreference-demo--camerarigdemo:

CameraRigDemo
-------------

Demo view routing and cursor capture. All camera placement is handled by Cameras submodules.

**Source:** ``Demo/Scripts/Cameras/CameraRigDemo.cs``. Component / asset.

+------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting    | Type          | Description                                                                                                                                                                                                                                 | Declared default and constraints |
+============+===============+=============================================================================================================================================================================================================================================+==================================+
| ``mode``   | ``ViewMode``  | Selects orbit, cockpit, cinematic, world free-look or vehicle-relative free-camera view. The matching camera module on Target controls the view's behaviour. Options: ``Orbit``, ``Interior``, ``Cinematic``, ``FreeLook``, ``FreeParent``. | ``ViewMode.Orbit``               |
+------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``target`` | ``Transform`` | Vehicle/root transform currently followed by the demo camera. The rig reads camera modules on this target when changing view modes.                                                                                                         | ``None / unassigned``            |
+------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--cinematiccamerademo:

CinematicCameraDemo
-------------------

A custom camera can also ignore mouse look and follow the vehicle's heading instead.

**Source:** ``Demo/Scripts/Cameras/CinematicCameraDemo.cs``. Component / asset.

**Inherited settings:** :ref:`CameraModule <uvs-inspectorreference-world--cameramodule>`. These settings also appear on this type.

+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                    | Type          | Description                                                                                                                                             | Declared default and constraints |
+============================+===============+=========================================================================================================================================================+==================================+
| ``distance``               | ``float``     | Requested exterior cinematic camera radius in metres.                                                                                                   | ``7``; Minimum: .1f              |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``focusOffset``            | ``Vector3``   | Point the cinematic camera looks toward, relative to its anchor in metres. Move it upward to frame the cabin or rider rather than the vehicle origin.   | ``Zero-initialized Vector3``     |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``followVehicleRotation``  | ``bool``      | Follow complete vehicle attitude for unrestricted flight, avoiding horizon-heading flips. Enabled for the demo spaceship, whose follow response is 8.   | ``false``                        |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``ignorePassengers``       | ``bool``      | Exclude passenger bodies from view obstruction.                                                                                                         | ``true``                         |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``ignoreDynamicObstacles`` | ``bool``      | Exclude marked dynamic obstacles from view obstruction.                                                                                                 | ``true``                         |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``followResponse``         | ``float``     | How quickly the cinematic camera catches up with its desired pose. Higher values follow more tightly; lower values give a slower, floating camera move. | ``4``; Minimum: .01f             |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``height``                 | ``float``     | Vertical offset in metres used by the cinematic camera framing. Increase to view the target from higher above.                                          | ``2.2``                          |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumDistance``        | ``float``     | Farthest zoom distance in metres allowed by this cinematic camera. Increase to allow wider views of the surrounding scene.                              | ``65``; Minimum: .1f             |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimumDistance``        | ``float``     | Closest zoom distance in metres allowed by this cinematic camera. Increase to prevent the camera from zooming too close to the model.                   | ``1.5``; Minimum: .1f            |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``obstructionMask``        | ``LayerMask`` | Scene layers that can block the cinematic camera. Exclude decorative/nonblocking layers if they should not pull the camera closer.                      | ``~0``                           |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``zoomSensitivity``        | ``float``     | Camera-radius change in metres per normalized scroll unit.                                                                                              | ``.6``; Minimum: .01f            |
+----------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--controlshuddemo:

ControlsHudDemo
---------------

**Source:** ``Demo/Scripts/UI/ControlsHudDemo.cs``. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-demo--damagecontrolsdemo:

DamageControlsDemo
------------------

**Source:** ``Demo/Scripts/Controls/DamageControlsDemo.cs``. Component / asset.

+--------------+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting      | Type                                                                                       | Description                                                                                                                                | Declared default and constraints |
+==============+============================================================================================+============================================================================================================================================+==================================+
| ``selector`` | ``VehicleSelectorDemo`` (:ref:`fields <uvs-inspectorreference-demo--vehicleselectordemo>`) | Demo vehicle selector determining which vehicle receives body-part/damage keyboard actions. Actions follow the currently selected vehicle. | ``None / unassigned``            |
+--------------+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--daynightdemo:

DayNightDemo
------------

Sample lighting switch. It changes the environment without modifying a vehicle's requested light state.

**Source:** ``Demo/Scripts/Environment/DayNightDemo.cs``. Component / asset.

+-------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting     | Type      | Description                                                                                                                             | Declared default and constraints |
+=============+===========+=========================================================================================================================================+==================================+
| ``night``   | ``bool``  | Initial/requested night-lighting mode for the demo.                                                                                     | ``false``                        |
+-------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``skyFill`` | ``Light`` | Extra fill light enabled during the day and disabled at night. Assign the secondary light used to soften daytime shadows.               | ``None / unassigned``            |
+-------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``sun``     | ``Light`` | Main directional light adjusted for the demo's day/night state. Night lowers its intensity, changes its colour and moves its direction. | ``None / unassigned``            |
+-------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--directwaypointaidemo:

DirectWaypointAIDemo
--------------------

Pose-driven companion to WaypointAIDemo. No wheel forces or Rigidbody pose writes.

**Source:** ``Demo/Scripts/Vehicles/DirectWaypointAIDemo.cs``. Component / asset.

+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| Setting              | Type                                                                                         | Description                                                                                                                                                             | Declared default and constraints                                          |
+======================+==============================================================================================+=========================================================================================================================================================================+===========================================================================+
| ``acceleration``     | ``float``                                                                                    | Rate of speed change in metres per second squared.                                                                                                                      | ``3``; Minimum: .1f                                                       |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``arrivalDistance``  | ``float``                                                                                    | Distance in metres at which the next checkpoint becomes active.                                                                                                         | ``3``; Minimum: .1f                                                       |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``checkpoints``      | ``Transform[]``                                                                              | The same world-space driving loop used by the physical AI example.                                                                                                      | ``None / unassigned``                                                     |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``controller``       | ``DirectController`` (:ref:`fields <uvs-inspectorreference-controller--directcontroller>`)   | Dedicated pose-driven Input Source selected while this direct AI owns the vehicle.                                                                                      | ``None / unassigned``                                                     |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``entryCheckpoints`` | ``Transform[]``                                                                              | Optional approach points used before joining the shared driving loop.                                                                                                   | ``None / unassigned``                                                     |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``speedKph``         | ``float``                                                                                    | Requested direct cruising speed along the route. This example ignores collision response and follows checkpoint height differences relative to its initial ride height. | ``20``; Speed field; stored in km/h, displayed in the selected speed unit |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``turnSpeed``        | ``float``                                                                                    | Maximum heading change in degrees per second. The chassis pose is supplied through DirectController.                                                                    | ``80``; Minimum: 1                                                        |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``vehicle``          | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Vehicle whose world pose this example supplies. The demo switch assigns this automatically.                                                                             | ``None / unassigned``                                                     |
+----------------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. _uvs-inspectorreference-demo--downforcemoduledemo:

DownforceModuleDemo
-------------------

Optional extension example: add this module through the controller dashboard to apply speed-based downforce.

**Source:** ``Demo/Scripts/Vehicles/DownforceModuleDemo.cs``. Component / asset.

**Inherited settings:** :ref:`PhysicsModule <uvs-inspectorreference-physics--physicsmodule>`. These settings also appear on this type.

+--------------------------+-----------+----------------------------------------------------------+----------------------------------+
| Setting                  | Type      | Description                                              | Declared default and constraints |
+==========================+===========+==========================================================+==================================+
| ``forcePerSpeedSquared`` | ``float`` | Downforce coefficient multiplying squared vehicle speed. | ``.5``; Minimum: 0               |
+--------------------------+-----------+----------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--engineaudiomodedemo:

EngineAudioModeDemo
-------------------

The demo maps the selected movement slot to the sound item's matching ID.

**Source:** ``Demo/Scripts/Vehicles/EngineAudioModeDemo.cs``. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-demo--externalcontroldemo:

ExternalControlDemo
-------------------

Demo ownership policy; the runtime controller itself has no concept of a player or AI.

**Source:** ``Demo/Scripts/Controls/ExternalControlDemo.cs``. Component / asset.

+----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting              | Type                                                                                              | Description                                                                                                                               | Declared default and constraints |
+======================+===================================================================================================+===========================================================================================================================================+==================================+
| ``checkpoints``      | ``Transform[]``                                                                                   | Ordered points forming the demo AI driving loop. If empty, the example creates a loop automatically; these are passed to WaypointAIDemo.  | ``None / unassigned``            |
+----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``entryCheckpoints`` | ``Transform[]``                                                                                   | Optional approach points followed before joining the main driving loop. Use them to guide the vehicle out of its starting position first. | ``None / unassigned``            |
+----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``gizmos``           | ``GizmoSettings`` (:ref:`fields <uvs-inspectorreference-demo--externalcontroldemogizmosettings>`) | Scene-only route visibility; does not change AI driving.                                                                                  | ``new GizmoSettings()``          |
+----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--externalcontroldemogizmosettings:

ExternalControlDemo.GizmoSettings
---------------------------------

**Source:** ``Demo/Scripts/Controls/ExternalControlDemo.cs``. Nested configuration data; expand its owning field in the Inspector.

+----------------------+----------+--------------------------------------------------------------------+----------------------------------+
| Setting              | Type     | Description                                                        | Declared default and constraints |
+======================+==========+====================================================================+==================================+
| ``showConnections``  | ``bool`` | Show connecting lines between checkpoints.                         | ``true``                         |
+----------------------+----------+--------------------------------------------------------------------+----------------------------------+
| ``showDrivingRoute`` | ``bool`` | Show the main driving loop.                                        | ``true``                         |
+----------------------+----------+--------------------------------------------------------------------+----------------------------------+
| ``showEntryRoute``   | ``bool`` | Show the approach route before the vehicle joins its driving loop. | ``true``                         |
+----------------------+----------+--------------------------------------------------------------------+----------------------------------+
| ``showGizmos``       | ``bool`` | Draw the AI route points and connecting lines in the Scene view.   | ``true``                         |
+----------------------+----------+--------------------------------------------------------------------+----------------------------------+
| ``showPointMarkers`` | ``bool`` | Show checkpoint spheres independently of route connecting lines.   | ``true``                         |
+----------------------+----------+--------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--freecamerademo:

FreeCameraDemo
--------------

**Source:** ``Demo/Scripts/Cameras/FreeCameraDemo.cs``. Component / asset.

**Inherited settings:** :ref:`FreeCameraMotionDemo <uvs-inspectorreference-demo--freecameramotiondemo>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-demo--freecameramotiondemo:

FreeCameraMotionDemo
--------------------

Custom camera example: add beside Cameras, assign it with SetModule/Attach, then SetActive(true). This component belongs to the optional Demo, not the runtime package.

**Source:** ``Demo/Scripts/Cameras/FreeCameraMotionDemo.cs``. Abstract base; settings are inherited by derived components.

**Inherited settings:** :ref:`CameraModule <uvs-inspectorreference-world--cameramodule>`. These settings also appear on this type.

+----------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting              | Type      | Description                                                                                                                                            | Declared default and constraints |
+======================+===========+========================================================================================================================================================+==================================+
| ``boostMultiplier``  | ``float`` | Multiplies free-camera movement speed while boost is held. At 4, boosted movement is four times the normal speed.                                      | ``4``; Minimum: 1                |
+----------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``movementResponse`` | ``float`` | How quickly free-camera velocity approaches the requested movement or comes to rest. Increase for sharper starts/stops; decrease for a smoother glide. | ``12``; Minimum: .1f             |
+----------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``movementSpeed``    | ``float`` | Base free-camera movement speed in metres per second.                                                                                                  | ``2``; Minimum: .1f              |
+----------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--freeparentcamerademo:

FreeParentCameraDemo
--------------------

A second custom view reuses navigation but keeps its pose in the vehicle anchor's frame. Each vehicle owns its own module and therefore remembers its own local camera pose.

**Source:** ``Demo/Scripts/Cameras/FreeParentCameraDemo.cs``. Component / asset.

**Inherited settings:** :ref:`FreeCameraMotionDemo <uvs-inspectorreference-demo--freecameramotiondemo>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-demo--huddemo:

HudDemo
-------

Example HUD consuming the public immutable telemetry API, with no dependency on physics internals.

**Source:** ``Demo/Scripts/UI/HudDemo.cs``. Component / asset.

+------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                | Type                                                                                         | Description                                                                                                                                                               | Declared default and constraints |
+========================+==============================================================================================+===========================================================================================================================================================================+==================================+
| ``showFlightAttitude`` | ``bool``                                                                                     | Shows the extra attitude readout for vehicles using an air movement profile. Turning it off hides those flight instruments while retaining the normal telemetry.          | ``true``                         |
+------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``speedUnit``          | ``SpeedUnit``                                                                                | Unit used for the demo's speed readout. Changing km/h, mph or m/s only changes the display, not vehicle speed or physics. Options: ``Kph``, ``Mph``, ``MetresPerSecond``. | ``SpeedUnit.Kph``                |
+------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``            | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Vehicle whose telemetry is displayed and whose reset position the demo tracks. VehicleSelectorDemo changes this reference when another vehicle is selected.               | ``None / unassigned``            |
+------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``wipersKey``          | ``Key``                                                                                      | Press to toggle the selected vehicle's wipers. Choose None to leave this demo shortcut unbound.                                                                           | ``Key.X``                        |
+------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--passengeraccessdemo:

PassengerAccessDemo
-------------------

Explicit demo selection; runtime access never searches for a player or reads a keyboard.

**Source:** ``Demo/Scripts/Controls/PassengerAccessDemo.cs``. Component / asset.

+------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                | Type                                                                                              | Description                                                                                                                                             | Declared default and constraints |
+========================+===================================================================================================+=========================================================================================================================================================+==================================+
| ``defaultProfile``     | ``AccessAnimationProfile`` (:ref:`fields <uvs-inspectorreference-world--accessanimationprofile>`) | Boarding profile used when the selected SeatAccess has no seat-specific animation profile. Supply compatible humanoid clips and Animator bindings here. | ``None / unassigned``            |
+------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``selector``           | ``VehicleSelectorDemo`` (:ref:`fields <uvs-inspectorreference-demo--vehicleselectordemo>`)        | Selector used to find the active vehicle and seat for demo entry/exit. It also updates whether a driver is present after the operation finishes.        | ``None / unassigned``            |
+------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``standingController`` | ``RuntimeAnimatorController``                                                                     | Animator controller assigned to the standing demo character before it enters a vehicle. Seat access can then select the appropriate boarding profile.   | ``None / unassigned``            |
+------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--powerwindowsdemo:

PowerWindowsDemo
----------------

Example consumer: all mechanics live in MovingPart; this script only supplies held input.

**Source:** ``Demo/Scripts/Controls/PowerWindowsDemo.cs``. Component / asset.

+-----------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting         | Type                                                                         | Description                                                                                                                           | Declared default and constraints |
+=================+==============================================================================+=======================================================================================================================================+==================================+
| ``leftDown``    | ``Key``                                                                      | Hold to lower the assigned left window. Release to stop it at its current position.                                                   | ``Key.LeftBracket``              |
+-----------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``leftUp``      | ``Key``                                                                      | Hold to raise the assigned left window. Release to stop it before it reaches the upper travel limit.                                  | ``Key.RightBracket``             |
+-----------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``leftWindow``  | ``MovingPart`` (:ref:`fields <uvs-inspectorreference-exterior--movingpart>`) | MovingPart that slides the left window while its up/down keys are held. Configure that part's travel range to match the door opening. | ``None / unassigned``            |
+-----------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rightDown``   | ``Key``                                                                      | Hold to lower the assigned right window. It operates independently of the left window.                                                | ``Key.Semicolon``                |
+-----------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rightUp``     | ``Key``                                                                      | Hold to raise the assigned right window. Release to stop movement at its current position.                                            | ``Key.Quote``                    |
+-----------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rightWindow`` | ``MovingPart`` (:ref:`fields <uvs-inspectorreference-exterior--movingpart>`) | MovingPart that slides the right window. It has independent up/down keys so either window can be moved without the other.             | ``None / unassigned``            |
+-----------------+------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--towingcontrolsdemo:

TowingControlsDemo
------------------

Player key binding stays in the sample; gameplay and AI call Coupler directly.

**Source:** ``Demo/Scripts/Controls/TowingControlsDemo.cs``. Component / asset.

+--------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------------------+
| Setting      | Type                                                                                       | Description                                                                                         | Declared default and constraints |
+==============+============================================================================================+=====================================================================================================+==================================+
| ``selector`` | ``VehicleSelectorDemo`` (:ref:`fields <uvs-inspectorreference-demo--vehicleselectordemo>`) | Demo selector used to route attach/detach keyboard commands to the currently active towing vehicle. | ``None / unassigned``            |
+--------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--underwaterdemo:

UnderwaterDemo
--------------

Camera-local underwater atmosphere. Restore the current day/night settings after rendering.

**Source:** ``Demo/Scripts/Environment/UnderwaterDemo.cs``. Component / asset.

+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting               | Type                                                                            | Description                                                                                                                                                                 | Declared default and constraints |
+=======================+=================================================================================+=============================================================================================================================================================================+==================================+
| ``ambience``          | ``AudioClip``                                                                   | Continuous sound played while the camera is underwater. Assign a loopable recording; leaving it empty omits this ambience.                                                  | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``ambiencePitch``     | ``float``                                                                       | Playback pitch multiplier for underwater ambience. 1 plays the original recording; lower values make it deeper and slower. This is a sound setting, not a viewing angle.    | ``.78``; Range: .25f to 1.5f     |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``ambienceVolume``    | ``float``                                                                       | Underwater ambience's target volume while submerged. Increase to make it louder; Fade Duration controls the transition into and out of that level.                          | ``.65``; Range: 0 to 1           |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``audioOutput``       | ``UnityEngine.Audio.AudioMixerGroup``                                           | Mixer group for the generated underwater ambience source. Use it to control or process underwater sound separately from other demo audio.                                   | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``fadeDuration``      | ``float``                                                                       | Time scale in seconds for fading the ambience volume toward its wet/dry target. Zero changes volume immediately; larger values soften the transition.                       | ``.7``; Minimum: 0               |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``submersionDepth``   | ``float``                                                                       | Depth in metres below the sampled surface that the camera must reach before underwater effects turn on. Increase to avoid switching effects during small surface crossings. | ``.15``; Minimum: 0              |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``surfaceHysteresis`` | ``float``                                                                       | Depth margin in metres between entering and leaving underwater state; prevents rapid toggling near the surface.                                                             | ``.05``; Minimum: 0              |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``water``             | ``WaterProvider`` (:ref:`fields <uvs-inspectorreference-world--waterprovider>`) | Water provider sampled at the camera position to decide whether the view is submerged. Its height controls the underwater visual/audio transition.                          | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--vehicleselectordemo:

VehicleSelectorDemo
-------------------

Demo-only player selection. Inactive demo cars receive parking input; the runtime package makes no player-count assumptions.

**Source:** ``Demo/Scripts/Vehicles/VehicleSelectorDemo.cs``. Component / asset.

+-----------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting         | Type                                                                                           | Description                                                                                                                                                                    | Declared default and constraints |
+=================+================================================================================================+================================================================================================================================================================================+==================================+
| ``activeIndex`` | ``int``                                                                                        | Initially selected index in the demo vehicle list.                                                                                                                             | ``0``                            |
+-----------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``hud``         | ``HudDemo`` (:ref:`fields <uvs-inspectorreference-demo--huddemo>`)                             | Telemetry display rebound to the selected vehicle. Leave empty if this demo should switch vehicles without a shared HUD.                                                       | ``None / unassigned``            |
+-----------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``orbitCamera`` | ``CameraRigDemo`` (:ref:`fields <uvs-inspectorreference-demo--camerarigdemo>`)                 | Demo camera rig retargeted when the selected vehicle changes. Its free-camera state reserves numeric keypad navigation for the camera; vehicle driving controls remain active. | ``None / unassigned``            |
+-----------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicles``    | ``VehicleController[]`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Vehicles available through the demo selection keys and previous/next controls, in display order. Selection transfers player input, camera target and HUD to that entry.        | ``None / unassigned``            |
+-----------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

+-------------------------------+----------+------------------------------------------------------------------------------------------------------------+------------------+
| Setting                       | Type     | Description                                                                                                | Declared default |
+===============================+==========+============================================================================================================+==================+
| ``automaticParkingHandbrake`` | ``bool`` | Apply the handbrake to inactive or unoccupied demo vehicles. Does not change player or AI handbrake input. | ``true``         |
+-------------------------------+----------+------------------------------------------------------------------------------------------------------------+------------------+

.. _uvs-inspectorreference-demo--vehicleweapondemo:

VehicleWeaponDemo
-----------------

Example of adding vehicle-specific controls/HUD without extending Command or the controller.

**Source:** ``Demo/Scripts/Vehicles/VehicleWeaponDemo.cs``. Component / asset.

+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting         | Type                                                                          | Description                                                                                                                                   | Declared default and constraints |
+=================+===============================================================================+===============================================================================================================================================+==================================+
| ``depress``     | ``Key``                                                                       | Hold to request downward barrel movement, within the weapon movement limits.                                                                  | ``Key.Delete``                   |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``elevate``     | ``Key``                                                                       | Hold to request upward barrel movement through the assigned Weapon's MovingPart.                                                              | ``Key.Insert``                   |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``fire``        | ``Key``                                                                       | Hold to send the weapon trigger request. Single/automatic fire behaviour and reload timing remain controlled by WeaponBarrel.                 | ``Key.Enter``                    |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rotateLeft``  | ``Key``                                                                       | Hold to turn the assigned Turret left. It does not change barrel elevation.                                                                   | ``Key.LeftBracket``              |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rotateRight`` | ``Key``                                                                       | Hold to turn the assigned Turret right, within that MovingPart's angle limits.                                                                | ``Key.RightBracket``             |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``showHud``     | ``bool``                                                                      | Shows this example's weapon-key hints and ready/reload information in the demo controls display.                                              | ``true``                         |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``turret``      | ``MovingPart`` (:ref:`fields <uvs-inspectorreference-exterior--movingpart>`)  | Optional MovingPart receiving left/right turret rotation commands. Keep elevation on Weapon and horizontal rotation on this part.             | ``None / unassigned``            |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``weapon``      | ``WeaponBarrel`` (:ref:`fields <uvs-inspectorreference-world--weaponbarrel>`) | Barrel receiving elevation and trigger commands from the demo weapon keys. If empty, the component searches child objects for a WeaponBarrel. | ``None / unassigned``            |
+-----------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--waterentryaudiodemo:

WaterEntryAudioDemo
-------------------

Demo-only water entry/exit for any vehicle, independently of its drive profile.

**Source:** ``Demo/Scripts/Environment/WaterEntryAudioDemo.cs``. Component / asset.

+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting               | Type                                                                            | Description                                                                                                                                                                           | Declared default and constraints |
+=======================+=================================================================================+=======================================================================================================================================================================================+==================================+
| ``exitSplashes``      | ``bool``                                                                        | Enables splash sound/particles when a tracked vehicle leaves the water.                                                                                                               | ``true``                         |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``foamMaterial``      | ``Material``                                                                    | Material used by the generated foam patch at the water-entry point. Leave empty to omit the default foam layer.                                                                       | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``fullEntrySpeed``    | ``float``                                                                       | Water-entry speed in m/s mapped to full splash intensity.                                                                                                                             | ``8``; Minimum: .1f              |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumParticles``  | ``int``                                                                         | Particle count cap for a full-intensity splash.                                                                                                                                       | ``180``; Minimum: 1              |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimumEntrySpeed`` | ``float``                                                                       | Minimum entry speed in m/s required for an entry splash.                                                                                                                              | ``1``; Minimum: 0                |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimumExitSpeed``  | ``float``                                                                       | Minimum exit speed in m/s required for an exit splash.                                                                                                                                | ``1``; Minimum: 0                |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimumParticles``  | ``int``                                                                         | Particle count used for the smallest admitted splash.                                                                                                                                 | ``50``; Minimum: 1               |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rearmHeight``       | ``float``                                                                       | Height in metres a previously wet vehicle must clear above the surface before another entry splash can be triggered. Increase to avoid repeated splashes from bobbing at the surface. | ``.2``; Minimum: 0               |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``splashClips``       | ``AudioClip[]``                                                                 | One-shot recordings available for water-entry/exit splashes. The example chooses a clip for an accepted crossing; assign several for variation.                                       | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``splashParticles``   | ``bool``                                                                        | Also emits spray/foam when a water-entry sound is accepted. Turn off for audio-only surface crossings.                                                                                | ``true``                         |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``splashPrefab``      | ``ParticleSystem``                                                              | Optional custom spray particle effect for a vehicle hitting the water. Without one, Spray Material can be used to build the default effect.                                           | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``splashRadius``      | ``float``                                                                       | Maximum spread in metres of the entry splash. Actual spread is scaled by impact strength, so light entries produce smaller bursts.                                                    | ``1.4``; Minimum: .1f            |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``sprayMaterial``     | ``Material``                                                                    | Material used by the automatically generated airborne entry spray when no Splash Prefab is assigned.                                                                                  | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``water``             | ``WaterProvider`` (:ref:`fields <uvs-inspectorreference-world--waterprovider>`) | Water provider sampled to detect vehicles crossing the surface. The effect works independently of whether the vehicle uses a boat driving profile.                                    | ``None / unassigned``            |
+-----------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--audio-settings-1:

Audio Settings
~~~~~~~~~~~~~~

+-------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Field             | Type                     | Behavior                                                                                                                                |
+===================+==========================+=========================================================================================================================================+
| ``audioSettings`` | ``VehicleAudioSettings`` | Shared playback, pitch, emitter and spatial settings. See :ref:`Audio Settings <uvs-inspectorreference-effects--vehicleaudiosettings>`. |
+-------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-inspectorreference-demo--waypointaidemo:

WaypointAIDemo
--------------

Small public-API example: steering and speed control only; no navigation or obstacle avoidance.

**Source:** ``Demo/Scripts/Vehicles/WaypointAIDemo.cs``. Component / asset.

+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| Setting                      | Type                                                                                           | Description                                                                                                                                                    | Declared default and constraints                                          |
+==============================+================================================================================================+================================================================================================================================================================+===========================================================================+
| ``arrivalDistance``          | ``float``                                                                                      | Distance in metres from a target at which the AI advances to the next waypoint. Increase to cut corners earlier; decrease to follow each point more closely.   | ``6``; Minimum: 1                                                         |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``brakeEngageOverspeedKph``  | ``float``                                                                                      | Amount above the AI's target speed, in km/h, at which service braking begins. Increase to tolerate a larger overshoot before braking.                          | ``3``; Speed field; stored in km/h, displayed in the selected speed unit  |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``brakeReleaseOverspeedKph`` | ``float``                                                                                      | Remaining excess speed in km/h at which AI braking stops. Keep below Brake Engage Overspeed to avoid rapidly switching brakes on and off.                      | ``1``; Speed field; stored in km/h, displayed in the selected speed unit  |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``checkpoints``              | ``Transform[]``                                                                                | Ordered main-route targets, wrapping back to the first point. At least two are needed; startup selects a suitable nearby part of the route.                    | ``None / unassigned``                                                     |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``controller``               | ``ExternalController`` (:ref:`fields <uvs-inspectorreference-controller--externalcontroller>`) | ExternalController receiving the AI's analog steering, throttle and brake commands. It must also be the vehicle's selected Input Source for AI driving to run. | ``None / unassigned``                                                     |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``entryCheckpoints``         | ``Transform[]``                                                                                | Optional initial approach route followed before joining the main loop. Use it to avoid cutting straight across obstacles from the spawn position.              | ``None / unassigned``                                                     |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``speedKph``                 | ``float``                                                                                      | Cruising speed. The simple tracked driver is capped at 12 km/h.                                                                                                | ``20``; Speed field; stored in km/h, displayed in the selected speed unit |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``steeringChangePerSecond``  | ``float``                                                                                      | Maximum change of normalized steering input per second.                                                                                                        | ``1.5``; Minimum: .1f                                                     |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``steeringSmoothTime``       | ``float``                                                                                      | Approximate seconds over which the AI smooths toward a new steering command. Increase for gentler steering; decrease to react sooner to a sharp bend.          | ``.25``; Minimum: .02f                                                    |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``vehicle``                  | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`)   | Vehicle driven around the waypoint route. The example supports wheeled, motorcycle and tracked profiles rather than aircraft or boats.                         | ``None / unassigned``                                                     |
+------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. _uvs-inspectorreference-demo--landinggearswitchdemo:

LandingGearSwitchDemo
---------------------

Application binding example: connect SwitchAnimator to LandingGear. Assign the gear, animator and seat. The binding samples deployment requests in LateUpdate; SwitchAnimator owns switch motion and its SwitchHandle owns the left-hand contact. Actual limb arrival gates switch motion through ControlAnimator.

**Source:** ``Demo/Scripts/Controls/LandingGearSwitchDemo.cs``. Component / asset.

+---------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                            | Description                                                                                                                                                       | Declared default and constraints |
+=====================+=================================================================================+===================================================================================================================================================================+==================================+
| ``landingGear``     | ``LandingGear`` (:ref:`fields <uvs-inspectorreference-exterior--landinggear>`)  | Landing gear connected to this cockpit switch. Requests are checked by the gear system, so a ground interlock can reject retraction and restore the switch state. | ``None / unassigned``            |
+---------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onMeansDeployed`` | ``bool``                                                                        | Maps the switch's on endpoint to extended gear rather than retracted gear.                                                                                        | ``true``                         |
+---------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``seat``            | ``PassengerSeat`` (:ref:`fields <uvs-inspectorreference-world--passengerseat>`) | Occupied seat whose left hand operates the gear switch through vehicle.handles.                                                                                   | ``None / unassigned``            |
+---------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``switchAnimator``  | ``SwitchAnimator``                                                              | Binary gear switch animator. Its paired handle supplies the left-hand contact; On Means Deployed selects the gear-down endpoint.                                  | ``None / unassigned``            |
+---------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-demo--projectiledemo:

ProjectileDemo
--------------

**Source:** ``Demo/Scripts/Vehicles/ProjectileDemo.cs``. Component / asset.

+----------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                          | Type     | Description                                                                                                                       | Declared default and constraints |
+==================================+==========+===================================================================================================================================+==================================+
| ``transferImpulseToVehicleRoot`` | ``bool`` | Transfer the game impulse to the vehicle hull when a door or other attached Rigidbody is hit. Native part collisions still occur. | ``true``                         |
+----------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
