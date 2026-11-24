.. _uvs-inspectorreference-common--common-settings-and-base-components:

Common settings and base components
===================================

:doc:`Back to the complete Inspector reference </InspectorReference>`.

+-----------------------------------------------------------------------------+------------------------+
| Component or data block                                                     | Settings declared here |
+=============================================================================+========================+
| :ref:`SceneGizmoOptions <uvs-inspectorreference-common--scenegizmooptions>` | 17                     |
+-----------------------------------------------------------------------------+------------------------+
| :ref:`Settings <uvs-inspectorreference-common--settings>`                   | 10                     |
+-----------------------------------------------------------------------------+------------------------+
| :ref:`TelemetrySettings <uvs-inspectorreference-common--telemetrysettings>` | 7                      |
+-----------------------------------------------------------------------------+------------------------+
| :ref:`VehicleModule <uvs-inspectorreference-common--vehiclemodule>`         | 2                      |
+-----------------------------------------------------------------------------+------------------------+

.. _uvs-inspectorreference-common--scenegizmooptions:

SceneGizmoOptions
-----------------

Serialized presentation state only; never read by the simulation pipeline.

**Source:** ``Runtime/Core/SceneGizmoOptions.cs``. Nested configuration data; expand its owning field in the Inspector.

+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| Setting            | Type     | Description                                                            | Declared default and constraints |
+====================+==========+========================================================================+==================================+
| ``anchors``        | ``bool`` | Show configured attachment and pivot points.                           | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``axes``           | ``bool`` | Show local axes used by this component.                                | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``bones``          | ``bool`` | Show skeletal bone connections.                                        | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``centerOfMass``   | ``bool`` | Show the vehicle center-of-mass marker.                                | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``clearance``      | ``bool`` | Show the passenger/vehicle clearance envelope.                         | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``connections``    | ``bool`` | Draw lines joining the configured attachment points.                   | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``editingHandles`` | ``bool`` | Allow interactive Scene-view handles for the available setup controls. | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``exit``           | ``bool`` | Show the configured passenger exit point.                              | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``feet``           | ``bool`` | Show foot targets and contacts.                                        | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``geometry``       | ``bool`` | Show the component geometry outlines.                                  | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``hands``          | ``bool`` | Show hand targets and contacts.                                        | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``labels``         | ``bool`` | Show names and measurements beside the scene guides.                   | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``pads``           | ``bool`` | Show finger/contact pad guides.                                        | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``path``           | ``bool`` | Show the configured motion or link path.                               | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``pelvis``         | ``bool`` | Show the passenger pelvis attachment guide.                            | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``ranges``         | ``bool`` | Show configured motion/travel ranges.                                  | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+
| ``wheels``         | ``bool`` | Show registered wheel positions and contact guides.                    | ``true``                         |
+--------------------+----------+------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-common--settings:

Settings
--------

Serializable shared configuration read by vehicle mechanics; apply configuration when changing persistent native setup.

**Source:** ``Runtime/Core/Settings.cs``. Nested configuration data; expand its owning field in the Inspector.

+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Setting                             | Type        | Description                                                                                                                                                                                                                        | Declared default and constraints                                           |
+=====================================+=============+====================================================================================================================================================================================================================================+============================================================================+
| ``brakeTorque``                     | ``float``   | Service-brake torque in N·m at full braking before each wheel's Brake Multiplier. Increase for stronger braking; handbrake strength is configured separately.                                                                      | ``6000``; Minimum: 0                                                       |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``centerOfMass``                    | ``Vector3`` | Rigidbody centre of mass in chassis-local metres. Lower Y to reduce rollover tendency; moving X or Z shifts side/front/rear loading. This is relative to the vehicle root, not the model pivot.                                    | ``new Vector3(0, 0.37941176, -0.0882353)``                                 |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``grip``                            | ``float``   | Multiplies the vehicle's configured tire friction strength. Increase for more road grip; decrease for easier sliding. Surface and individual driving systems can further modify the available grip.                                | ``1.65``; Range: 0.2f to 3                                                 |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``mass``                            | ``float``   | Chassis Rigidbody mass in kilograms. Increase for a heavier vehicle with more inertia and greater suspension load; spring strength may need adjustment to maintain ride height.                                                    | ``1350``; Minimum: 1                                                       |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``motorTorque``                     | ``float``   | Direct-drive motor torque budget in N·m before splitting it among driven wheels. Increase for stronger direct-drive acceleration; geared engines also have their own engine torque tuning.                                         | ``5000``; Minimum: 0                                                       |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``steeringAngle``                   | ``float``   | Maximum requested road-wheel steering angle in degrees before speed, grip and steering-geometry limits. Increase for tighter low-speed turns.                                                                                      | ``32``; Range: 1 to 60                                                     |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``steeringSpeed``                   | ``float``   | Digital and automatic direct-mode steering actuator speed in road-wheel degrees per second, including return to centre. Explicit analog steering follows its input directly.                                                       | ``100``; Minimum: 1                                                        |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``steeringWheelRotationAtFullLock`` | ``float``   | Steering wheel degrees from centre to either lock (540 means 1080 degrees lock-to-lock).                                                                                                                                           | ``135``; Minimum: 1                                                        |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``suspensionTravel``                | ``float``   | Wheel suspension travel in metres copied during configuration. More travel lets wheels extend/compress farther and changes their reachable height; align collider mounts for that travel instead of zeroing it to position meshes. | ``0.1764706``; Minimum: 0.05f                                              |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| ``topSpeedKph``                     | ``float``   | Forward road-speed target/limit stored in km/h and displayed in the selected unit. The active driving system uses it to reduce propulsion near top speed; it is not a hard teleport-style velocity clamp.                          | ``300``; Speed field; stored in km/h, displayed in the selected speed unit |
+-------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

.. _uvs-inspectorreference-common--telemetrysettings:

TelemetrySettings
-----------------

Capture options at Vehicle Controller > Setup > Telemetry. Core world pose, velocity, speed, wheel count and step timing remain available. Null configuration uses the defaults.

**Source:** ``Runtime/Core/TelemetrySettings.cs``. Nested configuration data; expand its owning field in the Inspector.

+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting          | Type     | Description                                                                                                                                                        | Declared default and constraints |
+==================+==========+====================================================================================================================================================================+==================================+
| ``body``         | ``bool`` | Copy chassis mass and world centre of mass.                                                                                                                        | ``true``                         |
+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``controls``     | ``bool`` | Copy resolved controls and the input command. Does not disable input or mechanics.                                                                                 | ``true``                         |
+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``fuel``         | ``bool`` | Look up fuel amount, capacity and consumption for telemetry. Does not disable Fuel Tank.                                                                           | ``true``                         |
+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``ground``       | ``bool`` | Probe chassis ground clearance and count grounded wheels. Disabling skips the diagnostic height ray; wheel physics queries remain independent.                     | ``true``                         |
+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motion``       | ``bool`` | Calculate acceleration, local motion, attitude, airspeed and G-force diagnostics. Core world pose, velocity, speed and timestamps remain available.                | ``true``                         |
+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``powertrain``   | ``bool`` | Copy engine RPM/torque, gearbox state and clutch diagnostics. Does not affect drivetrain simulation.                                                               | ``true``                         |
+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``wheelDetails`` | ``bool`` | Copy detailed telemetry for every wheel, including names, poses, slip, contact and torques. Disabled by default. Does not disable Tire Feedback or Tire Collision. | ``false``                        |
+------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-common--vehiclemodule:

VehicleModule
-------------

Exposes lifecycle notifications around registered module work.

**Source:** ``Runtime/Core/VehicleModule.cs``. Abstract base; settings are inherited by derived components.

+----------------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                    | Type     | Description                                                                                                                                                                    | Declared default and constraints |
+============================+==========+================================================================================================================================================================================+==================================+
| ``localExecutionOrder``    | ``int``  | Relative step order when Override Execution Order is on. Smaller numbers run earlier within the same category/phase; required dependencies still take priority.                | ``0``                            |
+----------------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``overrideExecutionOrder`` | ``bool`` | Uses Local Execution Order instead of the module's normal order within its category and dependency phase. Enable only when you need a custom order between compatible modules. | ``false``                        |
+----------------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
