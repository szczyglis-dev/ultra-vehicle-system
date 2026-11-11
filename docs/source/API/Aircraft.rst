.. _uvs-api-aircraft--flight-and-landing-gear-api:

Flight and landing gear API
===========================

Read :doc:`the system explanation </Scripting/Aircraft>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _uvs-api-aircraft--types:

Types
-----

-  :ref:`AerobaticAirplaneProfile <uvs-api-aircraft--aerobaticairplaneprofile>`
-  :ref:`AircraftAerodynamics <uvs-api-aircraft--aircraftaerodynamics>`
-  :ref:`AircraftControlMode <uvs-api-aircraft--aircraftcontrolmode>`
-  :ref:`AircraftControlMotion <uvs-api-aircraft--aircraftcontrolmotion>`
-  :ref:`AircraftControlMotionMode <uvs-api-aircraft--aircraftcontrolmotionmode>`
-  :ref:`AircraftControlSurface <uvs-api-aircraft--aircraftcontrolsurface>`
-  :ref:`AircraftControlSurfaces <uvs-api-aircraft--aircraftcontrolsurfaces>`
-  :ref:`AircraftSurfaceType <uvs-api-aircraft--aircraftsurfacetype>`
-  :ref:`AirplaneGroundContact <uvs-api-aircraft--airplanegroundcontact>`
-  :ref:`AirplaneProfile <uvs-api-aircraft--airplaneprofile>`
-  :ref:`HelicopterProfile <uvs-api-aircraft--helicopterprofile>`
-  :ref:`HoverVisuals <uvs-api-aircraft--hovervisuals>`
-  :ref:`HoverVisuals.TiltMount <uvs-api-aircraft--hovervisualstiltmount>`
-  :ref:`JetProfile <uvs-api-aircraft--jetprofile>`
-  :ref:`LandingGear <uvs-api-aircraft--landinggear>`
-  :ref:`LandingGearPart <uvs-api-aircraft--landinggearpart>`
-  :ref:`LandingGearPartType <uvs-api-aircraft--landinggearparttype>`
-  :ref:`LandingGearState <uvs-api-aircraft--landinggearstate>`
-  :ref:`LandingGearSuspension <uvs-api-aircraft--landinggearsuspension>`
-  :ref:`LandingGearSuspensionPart <uvs-api-aircraft--landinggearsuspensionpart>`
-  :ref:`Propulsion <uvs-api-aircraft--propulsion>`
-  :ref:`Propulsion.Propeller <uvs-api-aircraft--propulsionpropeller>`

.. _uvs-api-aircraft--aerobaticairplaneprofile:

AerobaticAirplaneProfile
------------------------

**Runtime/Drive/Profiles/AerobaticAirplaneProfile.cs**

Initial parameter preset for unrestricted body-rate controls.

**Inherits / implements:** :ref:`AirplaneProfile <uvs-api-aircraft--airplaneprofile>`.

.. _uvs-api-aircraft--methods:

Methods
~~~~~~~

All runtime behavior and editable fields are inherited from :ref:`AirplaneProfile <uvs-api-aircraft--airplaneprofile>`. This class only supplies initial parameter values.

.. _uvs-api-aircraft--methods-1:

Methods
~~~~~~~

+---------------------------------------+--------------------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                             | Role and behavior                                                        | Arguments and result                                               |
+=======================================+==========================================================================+====================================================================+
| ``public AerobaticAirplaneProfile()`` | Constructs ``AerobaticAirplaneProfile`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+---------------------------------------+--------------------------------------------------------------------------+--------------------------------------------------------------------+

.. _uvs-api-aircraft--aircraftaerodynamics:

AircraftAerodynamics
--------------------

**Runtime/Drive/Profiles/AirplaneProfile.cs**

.. _uvs-api-aircraft--values:

Values
~~~~~~

-  ``Simplified = 0``: Simplified lift, drag and flight-path alignment.
-  ``RelativeAirflow = 1``: Relative-airflow normal forces and parasite, induced and pressure drag.

.. _uvs-api-aircraft--aircraftcontrolmode:

AircraftControlMode
-------------------

**Runtime/Drive/Profiles/AirplaneProfile.cs**

.. _uvs-api-aircraft--values-1:

Values
~~~~~~

-  ``AssistedAttitude = 0``: Pitch/bank target control.
-  ``BodyRates = 1``: Unrestricted body angular-rate control.

.. _uvs-api-aircraft--aircraftcontrolmotion:

AircraftControlMotion
---------------------

**Runtime/Exterior/Aircraft/AircraftControlMotion.cs**

Configuration/implementation type for aircraft control motion within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-aircraft--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                                                                                            |
+========================================================+====================================================================================================================================================================+
| ``public Transform anchor``                            | Assign the anchor reference used by AircraftControlMotion. Leave unassigned only when this feature is optional or the component can resolve it automatically.      |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``                           | Local axis around which the configured motion or operation takes place. Initial value: ``Vector3.right``.                                                          |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximum``                               | Upper deflection angle in degrees mapped to the selected aircraft control channel. Initial value: ``20``.                                                          |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimum``                               | Lower deflection angle in degrees mapped to the selected aircraft control channel. Initial value: ``-20``.                                                         |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AircraftControlMotionMode mode``              | Selects the operating policy; see the listed options and the owning component guide. Options: ``Rotation``, ``Translation``.                                       |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform movingPart``                        | Assign the moving part reference used by AircraftControlMotion. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                             | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics.             |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }`` | Current value in this control's domain; use the declaring control's detailed value contract.                                                                       |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-2:

Methods
~~~~~~~

+----------------------------------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Signature                                          | Role and behavior                                                                        | Arguments and result                                                          |
+====================================================+==========================================================================================+===============================================================================+
| ``public virtual void SetValue(float normalized)`` | Applies normalized aircraft-control travel to its authored rotation/translation mapping. | ``normalized`` — Normalized value; the owner maps it to its configured range. |
+----------------------------------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

+-------------------------+--------------------------------------------------------------------------------+
| Declaration             | Usage                                                                          |
+=========================+================================================================================+
| ``public bool reverse`` | Mirror motion around the neutral pose without changing input or travel limits. |
+-------------------------+--------------------------------------------------------------------------------+

.. _uvs-api-aircraft--aircraftcontrolmotionmode:

AircraftControlMotionMode
-------------------------

**Runtime/Exterior/Aircraft/AircraftControlMotion.cs**

Defines the allowed aircraft control motion mode choices used by this topic.

.. _uvs-api-aircraft--values-2:

Values
~~~~~~

-  ``Rotation``
-  ``Translation``

.. _uvs-api-aircraft--aircraftcontrolsurface:

AircraftControlSurface
----------------------

**Runtime/Exterior/Aircraft/AircraftControlSurface.cs**

Configuration/implementation type for aircraft control surface within flight and landing gear.

**Inherits / implements:** :ref:`AircraftControlMotion <uvs-api-aircraft--aircraftcontrolmotion>`.

.. _uvs-api-aircraft--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                                                                                                                                         |
+=====================================+=================================================================================================================================================================================================================+
| ``public Vector3 customMix``        | Pitch, roll and yaw mix for Custom; enables new airframe layouts without new controller code.                                                                                                                   |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool invert``              | Reverses the sign of the assigned control input before applying control-surface motion.                                                                                                                         |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AircraftSurfaceType type`` | Selects the mechanism/visual variant used by this configuration. Options: ``Rudder``, ``LeftAileron``, ``RightAileron``, ``Elevator``, ``LeftElevator``, ``RightElevator``, ``Flap``, ``Airbrake``, ``Custom``. |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-3:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                           | Role and behavior                                                                                           | Arguments and result                                                                                                                                                                                                                                                                                     |
+=====================================================================================================+=============================================================================================================+==========================================================================================================================================================================================================================================================================================================+
| ``public virtual void SetControls(float pitch, float roll, float yaw, float flap, float airbrake)`` | Applies pitch/roll/yaw/flap/airbrake contributions through this surface's authored axis and motion mapping. | ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``roll`` — Normalized roll input. ``yaw`` — Normalized yaw input. ``flap`` — Flap, interpreted by this operation in the declared type. ``airbrake`` — Airbrake, interpreted by this operation in the declared type. |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--aircraftcontrolsurfaces:

AircraftControlSurfaces
-----------------------

**Runtime/Exterior/Aircraft/AircraftControlSurfaces.cs**

Presents the configured control-surface motion.

**Inherits / implements:** :ref:`ExteriorModule <uvs-api-modules--exteriormodule>`.

.. _uvs-api-aircraft--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                             |
+======================================================+=====================================================================================================================+
| ``public event Action<float> AirbrakeChanged``       | When airbrake presentation request changes. Payload: normalized airbrake value.                                     |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public event Action<Vector3> ControlsChanged``     | When aircraft surface-control presentation changes. Payload: the component's pitch/roll/yaw Vector3 representation. |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> ExternalControlChanged`` | When aircraft surface presentation changes external/follow-vehicle ownership. Payload: external-control bool.       |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public event Action<float> FlapsChanged``          | When flap presentation request changes. Payload: normalized flap value.                                             |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                                                                                     |
+===================================================+=============================================================================================================================================================================+
| ``public float airbrake``                         | Requested aerodynamic brake deployment from zero to one.                                                                                                                    |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 Controls { get; }``      | Read-only/resolved controls for ``AircraftControlSurfaces``.                                                                                                                |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool externalControl``                   | Uses explicit surface controls instead of the vehicle's current flight command.                                                                                             |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float flaps``                            | Requested flap deployment from zero retracted to one fully extended.                                                                                                        |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                                                                               |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float response``                         | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``5``.                     |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AircraftControlSurface[] surfaces``      | Ordered surfaces configuration entries. Expand each item; see AircraftControlSurface for its individual settings. Initial value: ``Array.Empty<AircraftControlSurface>()``. |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-4:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                           | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=============================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual void FollowVehicle()``                                                    | Releases external presentation ownership and resumes vehicle-state following.                                                               | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAirbrake(float value)``                                           | Updates the normalized aircraft airbrake presentation request.                                                                              | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetControls(float pitch, float roll, float yaw)``                    | Takes external pitch/roll/yaw presentation ownership for configured control-surface entries; ``FollowVehicle`` restores mechanic-following. | ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``roll`` — Normalized roll input. ``yaw`` — Normalized yaw input.                                                                   |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFlaps(float value)``                                              | Updates normalized flap presentation for the configured aircraft control surfaces.                                                          | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Smooths external or command-following pitch/roll/yaw, applies surface geometry and publishes changed presentation.                          | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--aircraftsurfacetype:

AircraftSurfaceType
-------------------

**Runtime/Exterior/Aircraft/AircraftControlSurface.cs**

Defines the allowed aircraft surface type choices used by this topic.

.. _uvs-api-aircraft--values-3:

Values
~~~~~~

-  ``Rudder``
-  ``LeftAileron``
-  ``RightAileron``
-  ``Elevator``
-  ``LeftElevator``
-  ``RightElevator``
-  ``Flap``
-  ``Airbrake``
-  ``Custom``

.. _uvs-api-aircraft--airplanegroundcontact:

AirplaneGroundContact
---------------------

**Runtime/Drive/Air/AirplaneGroundContact.cs**

``Tracks`` ground support and ground/air authority blending.

**Inherits / implements:** :ref:`PhysicsModule <uvs-api-modules--physicsmodule>`.

.. _uvs-api-aircraft--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                                  |
+===================================================================+==========================================================================================+
| ``public override int ExecutionOrder { get; }``                   | Default local priority within phase/category.                                            |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual float FlightBlend { get; protected set; }``      | Smoothed blend from ground behavior at zero to flight behavior at one.                   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual int GroundedWheelCount { get; protected set; }`` | Read-only/resolved grounded wheel count for ``AirplaneGroundContact``.                   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual bool IsAirborne { get; protected set; }``        | Current is airborne predicate; read it instead of maintaining a second application flag. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                 | Cross-category execution barrier used by the module pipeline.                            |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-5:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                  | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+====================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy.                    | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Counts operational gear contacts, including tire-tread support, updates airborne/takeoff grace and blends ground/flight authority. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                               | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--airplaneprofile:

AirplaneProfile
---------------

**Runtime/Drive/Profiles/AirplaneProfile.cs**

Owns the configurable fixed-wing flight pipeline, including assisted attitude, body rates and relative-airflow aerodynamics.

**Inherits / implements:** :ref:`AirProfile <uvs-api-driveprofiles--airprofile>`.

.. _uvs-api-aircraft--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                                                                                                                                                   |
+========================================================+===========================================================================================================================================================================================================================+
| ``public AircraftAerodynamics aerodynamics``           | Simplified lift/alignment or relative-airflow forces.                                                                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool airspeedControlAuthorityEnabled``        | Scale control torque with airspeed/attached flow. Disable to retain full commanded control authority at low speed. Default: enabled.                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool allowGroundReverse``                     | Permit reverse propulsion on supported landing gear with positive ground reverse limits. Default: ``false``; never authorizes airborne reverse.                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool angularDampingEnabled``                  | Apply angular velocity damping inside profile attitude/rate control; disabling retains commanded control torque. Default: enabled.                                                                                        |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool attitudeControlEnabled``                 | Master switch for profile pitch/roll/yaw control torque; leaves aerodynamic forces active. Default: enabled.                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeDamping``                       | Attitude damping. Initial value: ``6f``.                                                                                                                                                                                  |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool attitudeSpringEnabled``                  | AssistedAttitude mode: angle-to-target restoring torque, including pitch/roll input response. BodyRates uses rate control instead. Default: enabled.                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeStrength``                      | Attitude strength. Initial value: ``14f``.                                                                                                                                                                                |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool bankCompensationEnabled``                | Simplified aerodynamics: increase lift to compensate for bank. Disabled by the Aerobatic/Jet preset constructors. Default: enabled.                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AircraftControlMode controlMode``             | Assisted attitude targets or unrestricted body-rate control.                                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float coordinatedTurn``                       | Coordinated turn. Initial value: ``1.8f``.                                                                                                                                                                                |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float coordinatedTurnAssist``                 | Coordinated turn assist. Initial value: ``0.8f``.                                                                                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool coordinatedTurnEnabled``                 | Add bank-derived automatic turn demand. BodyRates also requires Rate Coordinated Turn Enabled. Default: enabled.                                                                                                          |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool dragEnabled``                            | Apply profile air resistance. In RelativeAirflow mode this also gates parasite, induced and pressure drag. Default: enabled.                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineIdleRpm``                         | Engine idle rpm. Initial value: ``700f``.                                                                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineMaximumRpm``                      | Engine maximum rpm. Initial value: ``2700f``.                                                                                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float enginePowerKw``                         | Engine power kw. Initial value: ``180f``.                                                                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumThrustNewtons``                  | Static thrust at full spool in N. Positive values replace ground/flight acceleration-based thrust; zero preserves it. Throttle, spool, speed envelope and optional power limit still apply. Default 0; Jet default 90000. |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enginePowerLimitEnabled``                | Limit thrust acceleration by engine power, speed and mass. Disabling retains throttle and spool response. Default: enabled.                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool flightAlignmentEnabled``                 | Apply flight-path alignment toward the airframe. In RelativeAirflow mode gates pitch/yaw crossflow correction, independently of lift trim. Default: enabled.                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float flightPathResponse``                    | Flight path response. Initial value: ``2f``.                                                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float flightTransitionTime``                  | Flight transition time. Initial value: ``0.35f``.                                                                                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool gLimiterEnabled``                        | Apply G-derived pitch-rate and aerodynamic normal-force limits. Disabled in the base preset; enabled by Jet.                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundAcceleration``                    | Ground acceleration. Initial value: ``6f``.                                                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundFriction``                        | Hull-contact friction for wheel-free aircraft only. Gear tires use the shared Friction module.                                                                                                                            |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundHandlingAssistance``              | Shared steering yaw and lateral grip assistance, only while tires touch the ground.                                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundLateralResponse``                 | Ground lateral response. Initial value: ``5f``.                                                                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundReverseAcceleration``             | Ground reverse acceleration. Initial value: ``2f``.                                                                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundReverseSpeed``                    | Ground-only reverse speed in m/s. Zero disables reverse thrust.                                                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundRotationAuthority``               | Ground rotation authority. Initial value: ``0.7f``.                                                                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool groundRotationEnabled``                  | Allow pitch control for rotation while still grounded. Airborne pitch control remains independent. Default: enabled.                                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundSteeringAngle``                   | Ground steering angle. Initial value: ``35f``.                                                                                                                                                                            |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundSteeringRate``                    | Ground steering rate. Initial value: ``75f``.                                                                                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundYawResponse``                     | Ground yaw response. Initial value: ``4f``.                                                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float inducedDrag``                           | Induced drag acceleration at one G; grows with aerodynamic load squared.                                                                                                                                                  |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool inducedDragEnabled``                     | Allow aerodynamic-load induced drag when the inherited Drag Enabled master is on. Default: enabled.                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingTransitionTime``                 | Landing transition time. Initial value: ``0.08f``.                                                                                                                                                                        |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool liftEnabled``                            | Apply aerodynamic lift. Disabling does not remove gravity, drag or attitude control. Default: enabled.                                                                                                                    |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float liftMultiplier``                        | Lift multiplier. Initial value: ``1.12f``.                                                                                                                                                                                |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float liftSpeed``                             | Minimum forward airspeed for ground rotation/takeoff, in m/s.                                                                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAlignmentAcceleration``          | Maximum alignment acceleration. Initial value: ``18f``.                                                                                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBank``                           | Maximum bank. Initial value: ``45f``.                                                                                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumControlAcceleration``            | Maximum control acceleration. Initial value: ``20f``.                                                                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumG``                              | Maximum g. Initial value: ``4.5f``.                                                                                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumGroundLateralAcceleration``      | Maximum ground lateral acceleration. Initial value: ``5f``.                                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLiftAcceleration``               | Maximum lift acceleration. Initial value: ``35f``.                                                                                                                                                                        |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumPitch``                          | Pitch attitude limit in AssistedAttitude mode. BodyRates uses angular rates instead.                                                                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumSpeed``                          | Forward airspeed limit in m/s. Thrust fades out near this speed.                                                                                                                                                          |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumTurnRate``                       | Maximum turn rate. Initial value: ``70f``.                                                                                                                                                                                |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumAirControlAuthority``            | Low-speed control assistance. Base default: zero; Aerobatic: 0.2; Jet: 0.05.                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumGroundTurnRadius``               | Minimum ground turn radius. Initial value: ``6f``.                                                                                                                                                                        |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float parasiteDrag``                          | Forward parasite drag acceleration / speed squared, in 1/metres.                                                                                                                                                          |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool parasiteDragEnabled``                    | Allow forward-speed parasite drag when the inherited Drag Enabled master is on. Default: enabled.                                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float parkingBrakeTorque``                    | Parking brake torque. Initial value: ``5000f``.                                                                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool pitchControlEnabled``                    | Allow profile control torque around the local pitch axis. Does not suppress aerodynamic torque from other systems. Default: enabled.                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pitchPathResponse``                     | Pitch path response. Initial value: ``5f``.                                                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pitchRate``                             | Pitch rate. Initial value: ``110f``.                                                                                                                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool pressureDragEnabled``                    | Allow crossflow pressure drag when the inherited Drag Enabled master is on. Default: enabled.                                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool progressiveThrustEnvelope``              | Progressive fourth-power thrust fade instead of linear fade.                                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool propulsionEnabled``                      | Apply engine/propeller thrust, including supported ground reverse. Engine and propeller presentation remain independent. Default: enabled.                                                                                |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool rateCoordinatedTurnEnabled``             | Enable bank-derived turn assistance for body-rate control when coordinatedTurnEnabled is on.                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rateResponse``                          | Rate response. Initial value: ``6f``.                                                                                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float referenceAirspeed``                     | Reference airspeed. Initial value: ``100f``.                                                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool RequiresWheels { get; }``       | Whether this profile requires valid wheel definitions during configuration.                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool rollControlEnabled``                     | Allow profile control torque around the local roll axis. Default: enabled.                                                                                                                                                |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rollRate``                              | Roll rate. Initial value: ``200f``.                                                                                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool rudderEnabled``                          | Allow commanded yaw/rudder input in profile attitude control. Default: enabled.                                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rudderRate``                            | Rudder rate. Initial value: ``35f``.                                                                                                                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float serviceBrakeTorque``                    | Service brake torque. Initial value: ``3000f``.                                                                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool sideForceEnabled``                       | Allow sideways aerodynamic normal force; inherited Lift Enabled controls the lift-axis force. Default: enabled.                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float sidePressureDrag``                      | Side pressure drag. Initial value: ``0.008f``.                                                                                                                                                                            |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool speedLimiterEnabled``                    | Fade thrust near configured forward/reverse speed limits; does not directly clamp Rigidbody velocity. Default: enabled.                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float stallAngle``                            | Stall angle. Initial value: ``35f``.                                                                                                                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool stallEnabled``                           | Reduce lift/support near low airspeed; RelativeAirflow mode also reduces attached flow at excessive angle of attack. Disable for full aerodynamic support. Default: enabled.                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float stallSpeedRatio``                       | Stall speed ratio. Initial value: ``0.55f``.                                                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float suspensionDamper``                      | Suspension damper. Initial value: ``1785f``.                                                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float suspensionSpring``                      | Suspension spring. Initial value: ``24000f``.                                                                                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float suspensionTravel``                      | Suspension travel. Initial value: ``0.18f``.                                                                                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float takeoffContactGrace``                   | Seconds without tire contact before entering flight. Touchdown is detected on the first tire contact.                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tireGrip``                              | Tire grip. Initial value: ``1.3f``.                                                                                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useLandingGear``                         | Keep native tires active in flight to detect touchdown without rebuilding wheel actors. Disable only for a wheel-free aircraft.                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool UsesWheelPropulsion { get; }``  | True for wheel/track drive; false for native thrust profiles, including aircraft with support wheels.                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float wingPressureDrag``                      | Additional quadratic pressure drag for airflow across the wings / across the fuselage.                                                                                                                                    |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool yawControlEnabled``                      | Allow profile control torque around the local yaw axis. Default: enabled.                                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool yawLimiterEnabled``                      | Limit body-rate yaw demand by airspeed and gravity.                                                                                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawPathResponse``                       | Yaw path response. Initial value: ``4f``.                                                                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawRate``                               | Yaw rate. Initial value: ``45f``.                                                                                                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 ResolveAngularRates(float speedKph)`` | Returns speed-scaled pitch/yaw/roll rates in degrees/s.                                                                                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-6:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                   | Arguments and result                                                                                                                                                                                                       |
+============================================================================================+=====================================================================================================================================+============================================================================================================================================================================================================================+
| ``public AirplaneProfile()``                                                               | Constructs ``AirplaneProfile`` with the supplied initial state.                                                                     | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanUsePropulsionBoost(VehicleController vehicle)``                  | Checks the profile propulsion switch and required water/support context before activation.                                          | Uses the supplied vehicle and command context; returns the profile-specific admission result.                                                                                                                              |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Ensures propulsion/ground-contact helpers and writes aircraft-owned engine, steering, braking, grip/travel and suspension settings. | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                               |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 PressureDragAcceleration(Transform frame, Vector3 velocity)``     | Evaluates jet pressure-drag acceleration from the supplied speed/state.                                                             | ``frame`` — Frame, interpreted by this operation in the declared type. ``velocity`` — World velocity in m/s. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation.               |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveBoostDemand(VehicleController vehicle, Command command)``   | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes.                     | Uses the supplied vehicle and command context; returns the profile-specific admission result.                                                                                                                              |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveDriveDemand(VehicleController vehicle, Command command)``   | Maps the command and strategy state to propulsion demand for surrounding mechanics.                                                 | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveExternalDriveIntent(VehicleController vehicle)``            | Returns signed non-wheel propulsion intent used by shared coasting/contact policy.                                                  | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** Computed float in the operation's documented unit/domain.                                                                                        |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Runs the shared fixed-wing physics pipeline using the selected control/aerodynamic parameters and ground-contact authority.         | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.   |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--helicopterprofile:

HelicopterProfile
-----------------

**Runtime/Drive/Profiles/HelicopterProfile.cs**

Configuration/implementation type for helicopter profile within flight and landing gear.

**Inherits / implements:** :ref:`AirProfile <uvs-api-driveprofiles--airprofile>`.

.. _uvs-api-aircraft--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                                                                                                                 |
+=============================================+=========================================================================================================================================================================================================================================+
| ``public float attitudeInputScale``         | Pitch/roll input contribution to the target up vector.                                                                                                                                                                                  |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeStrength``           | Attitude strength. Initial value: ``18``.                                                                                                                                                                                               |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool automaticLeveling``           | Automatic leveling. Initial value: ``true``.                                                                                                                                                                                            |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool compensateGravity``           | Compensate gravity. Initial value: ``true``.                                                                                                                                                                                            |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool holdAltitude``                | Hold height after releasing ascend/descend and brake horizontal drift after releasing movement, without returning to a position. Requires a running engine and fully spooled rotor. Disable for the original vertical damping behavior. |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool horizontalDriveEnabled``      | Allow horizontal thrust from rotor tilt and automatic drift braking. Default: enabled.                                                                                                                                                  |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool hoverDriftBrakingEnabled``    | Brake horizontal drift in neutral powered hover when altitude hold and automatic leveling are active. Default: enabled.                                                                                                                 |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool linearDragEnabled``           | Apply inherited velocity-proportional air resistance. Default: enabled.                                                                                                                                                                 |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tiltAccelerationMultiplier`` | Multiplier for horizontal acceleration from rotor tilt.                                                                                                                                                                                 |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float verticalDamping``            | Vertical damping. Initial value: ``1.5f``.                                                                                                                                                                                              |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool verticalLiftEnabled``         | Allow the vertical rotor-support/collective channel, including altitude hold and gravity compensation. Default: enabled.                                                                                                                |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawAcceleration``            | Yaw acceleration. Initial value: ``5``.                                                                                                                                                                                                 |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool yawControlEnabled``           | Apply commanded yaw torque independently of horizontal thrust. Default: enabled.                                                                                                                                                        |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-7:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                               | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override bool CanUsePropulsionBoost(VehicleController vehicle)``                  | Checks the profile propulsion switch and required water/support context before activation.                      | Uses the supplied vehicle and command context; returns the profile-specific admission result.                                                                                                                            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Ensures a Propulsion helper exists for helicopter presentation/spool integration.                               | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public HelicopterProfile()``                                                             | Constructs ``HelicopterProfile`` with the supplied initial state.                                               | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveBoostDemand(VehicleController vehicle, Command command)``   | Returns finite normalized propulsion/collective intent for boost admission; each profile selects relevant axes. | Uses the supplied vehicle and command context; returns the profile-specific admission result.                                                                                                                            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies resistance, spool-dependent powered support, lift/height hold and commanded helicopter motion.          | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--hovervisuals:

HoverVisuals
------------

**Runtime/Exterior/Aircraft/HoverVisuals.cs**

Configuration/implementation type for hover visuals within flight and landing gear.

**Inherits / implements:** :ref:`ExteriorModule <uvs-api-modules--exteriormodule>`.

.. _uvs-api-aircraft--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
| Member                            | Meaning                                                                                                       |
+===================================+===============================================================================================================+
| ``public TiltMount[] tiltMounts`` | Optional hover engine mounts. Uses folded-wheel thrust, turn and strafe tilt without the wheel-fold rotation. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-8:

Methods
~~~~~~~

+------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                          | Role and behavior                                                       | Arguments and result                                                                                                                                                                                                                                 |
+====================================================================================+=========================================================================+======================================================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController owner)``                        | Stores the vehicle whose hover transition geometry should be displayed. | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                                                                                                           |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Quaternion GetWheelTilt(WheelSetup wheel, HoverProfile profile)`` | Returns the wheel's hover-transition presentation tilt.                 | ``wheel`` — Native wheel or wheel adapter being configured/queried. ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation. |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--hovervisualstiltmount:

HoverVisuals.TiltMount
----------------------

**Runtime/Exterior/Aircraft/HoverVisuals.cs**

Configuration/implementation type for tilt mount within flight and landing gear.

.. _uvs-api-aircraft--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                             | Meaning                                                                                                                                                           |
+====================================+===================================================================================================================================================================+
| ``public Quaternion restRotation`` | Reference/orientation rotation for rest rotation. Identity adds no rotation. Initial value: ``Quaternion.identity``.                                              |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform transform``     | Assign the transform reference used by HoverVisuals.TiltMount. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--jetprofile:

JetProfile
----------

**Runtime/Drive/Profiles/JetProfile.cs**

Initial parameter preset for relative-airflow fighter response and limits.

**Inherits / implements:** :ref:`AerobaticAirplaneProfile <uvs-api-aircraft--aerobaticairplaneprofile>`.

.. _uvs-api-aircraft--methods-9:

Methods
~~~~~~~

All runtime behavior and editable fields are inherited from :ref:`AirplaneProfile <uvs-api-aircraft--airplaneprofile>`. This class only supplies initial parameter values.

.. _uvs-api-aircraft--methods-10:

Methods
~~~~~~~

+-------------------------+------------------------------------------------------------+--------------------------------------------------------------------+
| Signature               | Role and behavior                                          | Arguments and result                                               |
+=========================+============================================================+====================================================================+
| ``public JetProfile()`` | Constructs ``JetProfile`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+-------------------------+------------------------------------------------------------+--------------------------------------------------------------------+

.. _uvs-api-aircraft--landinggear:

LandingGear
-----------

**Runtime/Exterior/Aircraft/LandingGear.cs**

Owns deployment sequencing and physical gear-contact availability.

**Inherits / implements:** :ref:`ExteriorModule <uvs-api-modules--exteriormodule>`.

.. _uvs-api-aircraft--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                                                                               |
+========================================================+=======================================================================================================================================================+
| ``public event Action<LandingGearState> StateChanged`` | When deployment sequencing changes ``LandingGearState``. Payload: actual sequence state; use this rather than treating request acceptance as arrival. |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                                                                                                    |
+===================================================================+============================================================================================================================================================+
| ``public override int ExecutionOrder { get; }``                   | Default local priority within phase/category.                                                                                                              |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundClearanceLock``                              | Ground-probe distance in metres used by the ground retraction interlock. Initial value: ``.6f``.                                                           |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public LayerMask groundMask``                                   | Layers considered supporting ground by this system. Initial value: ``~0``.                                                                                 |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool initiallyDeployed``                                 | Starts the landing gear deployed when checked, or retracted when unchecked. Initial value: ``true``.                                                       |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsDeployed { get; }``                       | Current is deployed predicate; read it instead of maintaining a second application flag.                                                                   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsGroundLocked { get; }``                   | Current is ground locked predicate; read it instead of maintaining a second application flag.                                                              |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public LandingGearPart[] parts``                                | Ordered parts configuration entries. Expand each item; see LandingGearPart for its individual settings. Initial value: ``Array.Empty<LandingGearPart>()``. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                 | Cross-category execution barrier used by the module pipeline.                                                                                              |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool preventGroundRetraction``                           | Prevent retraction while tires touch the ground or the hull is within Ground Clearance Lock.                                                               |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RequestedDeployed { get; protected set; }`` | Read-only/resolved requested deployed for ``LandingGear``.                                                                                                 |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual LandingGearState State { get; protected set; }`` | Read-only/resolved state for ``LandingGear``.                                                                                                              |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider[] wheels``                                 | Assign the wheels references used by LandingGear. Entries are processed in list order. Initial value: ``Array.Empty<WheelCollider>()``.                    |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-11:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                 | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Connects suspension, initializes authored deployment once and synchronizes gear-part/contact policy.              | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetGear(bool deployed)``                                           | Synchronizes gear state immediately for spawn/reset, bypassing ordinary request interlocks.                       | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction.                                                                                                                                              |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetDeployed(bool deployed)``                                         | Requests landing-gear deployment/retraction subject to clearance, ground and alignment interlocks.                | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Advances part delays/travel and gear state; retraction waits for unloaded suspension alignment before continuing. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Toggle()``                                                           | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.               | **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                            |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--landinggearpart:

LandingGearPart
---------------

**Runtime/Exterior/Aircraft/LandingGearPart.cs**

Maps deployment progress to a door/strut pose.

**Inherits / implements:** :ref:`AircraftControlMotion <uvs-api-aircraft--aircraftcontrolmotion>`.

.. _uvs-api-aircraft--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                                                              |
+===================================================================+======================================================================================================================+
| ``public virtual float DeployedFraction { get; protected set; }`` | Current deployed fraction: one deployed, zero retracted.                                                             |
+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float duration``                                         | Time in seconds over which this transition/action runs. Initial value: ``2``.                                        |
+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float extendDelay``                                      | Delay before this gear part starts extension, in seconds.                                                            |
+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float retractDelay``                                     | Delay before this gear part starts retraction, in seconds.                                                           |
+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public virtual float RetractionFraction { get; }``              | Gear-part travel from fully extended at zero to retracted at one.                                                    |
+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public LandingGearPartType type``                               | Selects the mechanism/visual variant used by this configuration. Options: ``Strut``, ``Door``, ``Link``, ``Custom``. |
+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-12:

Methods
~~~~~~~

+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                      | Role and behavior                                                                                                                            | Arguments and result                                                                                                                                                                              |
+================================================================================+==============================================================================================================================================+===================================================================================================================================================================================================+
| ``public virtual void Animate(bool deployed, float elapsed, float deltaTime)`` | Applies gear-part deployment animation using its authored motion mapping.                                                                    | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction. ``elapsed`` — Elapsed operation time in seconds. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CaptureDeployedPose()``                                  | Captures the current gear-part pose as the fully deployed baseline.                                                                          | No arguments; no returned value.                                                                                                                                                                  |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(bool deployed)``                            | Synchronizes this part immediately to the requested deployed/retracted pose through its gear-part mapping.                                   | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction.                                                                                                                       |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetRetraction(float amount)``                            | Applies landing-gear travel with zero deployed and one retracted.                                                                            | ``amount`` — Requested damage/repair amount in the mechanic's damage units.                                                                                                                       |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetValue(float normalized)``                            | Applies deployed fraction: 1 fully deployed, 0 fully retracted, retaining the captured deployed mesh offset and current suspension rotation. | ``normalized`` — Normalized value; the owner maps it to its configured range.                                                                                                                     |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--landinggearparttype:

LandingGearPartType
-------------------

**Runtime/Exterior/Aircraft/LandingGearPart.cs**

Defines the allowed landing gear part type choices used by this topic.

.. _uvs-api-aircraft--values-4:

Values
~~~~~~

-  ``Strut``
-  ``Door``
-  ``Link``
-  ``Custom``

.. _uvs-api-aircraft--landinggearstate:

LandingGearState
----------------

**Runtime/Exterior/Aircraft/LandingGear.cs**

Defines the allowed landing gear state choices used by this topic.

.. _uvs-api-aircraft--values-5:

Values
~~~~~~

-  ``Deployed``
-  ``Retracting``
-  ``Retracted``
-  ``Extending``

.. _uvs-api-aircraft--landinggearsuspension:

LandingGearSuspension
---------------------

**Runtime/Exterior/Aircraft/LandingGearSuspension.cs**

Configuration/implementation type for landing gear suspension within flight and landing gear.

**Inherits / implements:** :ref:`ExteriorModule <uvs-api-modules--exteriormodule>`.

.. _uvs-api-aircraft--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                                                                                        |
+===================================================+================================================================================================================================================================================+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                                                                                                                  |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsStraight { get; }``       | Current is straight predicate; read it instead of maintaining a second application flag.                                                                                       |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public LandingGearSuspensionPart[] parts``      | Ordered parts configuration entries. Expand each item; see LandingGearSuspensionPart for its individual settings. Initial value: ``Array.Empty<LandingGearSuspensionPart>()``. |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                                                                                  |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-13:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                         | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===========================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Connects ``LandingGear`` and prepares changed runtime leg state while preserving authored deployed geometry in Edit Mode. | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetSuspension()``                                                  | Clears load-driven landing-gear hinge displacement and velocity.                                                          | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Uses native wheel load to advance each leg's bounded angular spring/damper/inertia model.                                 | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--landinggearsuspensionpart:

LandingGearSuspensionPart
-------------------------

**Runtime/Exterior/Aircraft/LandingGearSuspensionPart.cs**

Describes load-driven hinge response for a gear part.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-aircraft--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                                                                                                                           |
+=====================================+===================================================================================================================================================================================================+
| ``public float angularInertia``     | Effective angular inertia used when converting the suspension response into hinge motion. Initial value: ``500``.                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float authoredAngle``      | Angle already present in the authored deployed mesh, in degrees.                                                                                                                                  |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float dampingTorque``      | Force/torque budget for damping torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``3500``. |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public LandingGearPart gearPart`` | Assign the gear part LandingGearPart component/asset used by LandingGearSuspensionPart.                                                                                                           |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``        | Local axis around which the configured motion or operation takes place. Initial value: ``Vector3.forward``.                                                                                       |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngle``       | Upper rotation angle in degrees for the configured motion. Initial value: ``28``.                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``          | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics.                                            |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float springTorque``       | Rotational spring response is integrated by ``LandingGearSuspension``; ``authoredAngle`` describes the existing deployed geometry and must not be captured from a compressed animated pose.       |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider wheel``      | Assign the wheel reference used by LandingGearSuspensionPart. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                  |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------+--------------------------------------------------------------------------------+
| Declaration             | Usage                                                                          |
+=========================+================================================================================+
| ``public bool reverse`` | Mirror motion around the neutral pose without changing input or travel limits. |
+-------------------------+--------------------------------------------------------------------------------+

.. _uvs-api-aircraft--propulsion:

Propulsion
----------

**Runtime/Exterior/Aircraft/Propulsion.cs**

Animates propellers and rotors for aircraft, boats and submarines.

**Inherits / implements:** :ref:`ExteriorModule <uvs-api-modules--exteriormodule>`.

.. _uvs-api-aircraft--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                          |
+=============================================+==================================================================================================================================+
| ``public event Action<float> SpeedChanged`` | When resolved propulsion presentation speed changes. Payload: the component's current speed value; it does not set engine power. |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                           | Meaning                                                                                                                                                        |
+==================================================================+================================================================================================================================================================+
| ``public Engine engine``                                         | Assign the engine Engine component/asset used by Propulsion.                                                                                                   |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Propeller[] propellers``                                | Ordered propellers configuration entries. Expand each item; see Propulsion.Propeller for its individual settings. Initial value: ``Array.Empty<Propeller>()``. |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rotor``                                       | Rotor.                                                                                                                                                         |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float SpeedNormalized { get; protected set; }`` | Resolved normalized propeller/rotor presentation speed, separate from mechanical thrust.                                                                       |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spinDownSeconds``                                 | Time in seconds used for spin down seconds. Larger values make this phase/wait last longer. Initial value: ``2.4f``.                                           |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spinUpSeconds``                                   | Time in seconds used for spin up seconds. Larger values make this phase/wait last longer. Initial value: ``1.8f``.                                             |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--methods-14:

Methods
~~~~~~~

+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                      | Role and behavior                                                                                  | Arguments and result                                                                                                                                         |
+================================================================+====================================================================================================+==============================================================================================================================================================+
| ``public override void Configure(VehicleController owner)``    | Stores the owner and resolves missing hull/engine references used by spool/propeller presentation. | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                   |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)`` | Checks movement-family compatibility; this is independent of the Unity enabled flag.               | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-aircraft--propulsionpropeller:

Propulsion.Propeller
--------------------

**Runtime/Exterior/Aircraft/Propulsion.cs**

Configuration/implementation type for propeller within flight and landing gear.

.. _uvs-api-aircraft--state-and-configuration-13:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                                                                                                         |
+=======================================+=================================================================================================================================================================+
| ``public float degreesPerSecond``     | Visible propeller/rotor spin speed at full requested output, in degrees per second. Initial value: ``900``.                                                     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool instantThrustResponse`` | Bypass smoothing of control-driven shaft demand to match immediate thrust forces. Engine-only rotation keeps its engine spool.                                  |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``          | Local axis around which the configured motion or operation takes place. Initial value: ``Vector3.up``.                                                          |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maneuverSpeed``        | Shaft speed at full steering, lift or pitch demand; throttle can request a higher speed.                                                                        |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool onlyInWater``           | Require an enabled water provider/fallback and at least partial hull immersion. A dry hull stops shaft rotation.                                                |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool onlyWithThrust``        | Scale rotation by throttle and enabled maneuver demands. No demand stops the shaft. Works with fixed speed or engine RPM.                                       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reverseWithThrust``     | Reverse rotation for negative throttle. Independent of Only With Thrust and Use Engine Rpm.                                                                     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rpmRatio``             | Rotor RPM / engine RPM. Negative values reverse rotation.                                                                                                       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spinWithLift``          | Include vertical Lift demand in shaft rotation.                                                                                                                 |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spinWithPitch``         | Include Pitch demand in shaft rotation.                                                                                                                         |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spinWithSteering``      | Include combined Steering/Yaw demand, including turning at rest. Forward/reverse throttle determines shaft direction.                                           |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform transform``        | Assign the transform reference used by Propulsion.Propeller. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool physicsRotation``       | Advance collidable blades on the physics clock.                                                                                                                 |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useEngineRpm``          | Derive rotor speed from engine RPM instead of fixed degrees per second.                                                                                         |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

======================= ===================================
Declaration             Usage
======================= ===================================
``public bool reverse`` Reverse the visible shaft rotation.
======================= ===================================
