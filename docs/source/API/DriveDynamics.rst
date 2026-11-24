.. _uvs-api-drivedynamics--engine-and-drivetrain-api:

Engine and drivetrain API
=========================

Read :doc:`the system explanation </Scripting/DriveDynamics>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _uvs-api-drivedynamics--types:

Types
-----

-  :ref:`AntiLockBrakes <uvs-api-drivedynamics--antilockbrakes>`
-  :ref:`AutomaticGearbox <uvs-api-drivedynamics--automaticgearbox>`
-  :ref:`BoostSuspensionSettings <uvs-api-drivedynamics--boostsuspensionsettings>`
-  :ref:`Brakes <uvs-api-drivedynamics--brakes>`
-  :ref:`Burnout <uvs-api-drivedynamics--burnout>`
-  :ref:`BurnoutSuspensionSettings <uvs-api-drivedynamics--burnoutsuspensionsettings>`
-  :ref:`Clutch <uvs-api-drivedynamics--clutch>`
-  :ref:`Differential <uvs-api-drivedynamics--differential>`
-  :ref:`Differential.Axle <uvs-api-drivedynamics--differentialaxle>`
-  :ref:`DifferentialMode <uvs-api-drivedynamics--differentialmode>`
-  :ref:`DrivingAssists <uvs-api-drivedynamics--drivingassists>`
-  :ref:`Engine <uvs-api-drivedynamics--engine>`
-  :ref:`EngineCore <uvs-api-drivedynamics--enginecore>`
-  :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`
-  :ref:`Gearbox <uvs-api-drivedynamics--gearbox>`
-  :ref:`ManualGearbox <uvs-api-drivedynamics--manualgearbox>`
-  :ref:`MotorcycleBalance <uvs-api-drivedynamics--motorcyclebalance>`
-  :ref:`MotorcycleGroundAssist <uvs-api-drivedynamics--motorcyclegroundassist>`
-  :ref:`MotorcycleWheelieControl <uvs-api-drivedynamics--motorcyclewheeliecontrol>`
-  :ref:`Nitro <uvs-api-drivedynamics--nitro>`
-  :ref:`ParkingHold <uvs-api-drivedynamics--parkinghold>`
-  :ref:`Steering <uvs-api-drivedynamics--steering>`
-  :ref:`TractionControl <uvs-api-drivedynamics--tractioncontrol>`
-  :ref:`Transmission <uvs-api-drivedynamics--transmission>`
-  :ref:`TransmissionMode <uvs-api-drivedynamics--transmissionmode>`

.. _uvs-api-drivedynamics--antilockbrakes:

AntiLockBrakes
--------------

**Runtime/Drive/Brakes/AntiLockBrakes.cs**

Optional per-wheel service-brake pressure modulation after Brakes. Detects impending lock-up from contact-relative tire speed; parking brakes, low-speed holding and airborne wheels remain independent.

**Inherits / implements:** ``DriveModule``, ``IVehicleResetHandler``.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                         |
+====================================================+=================================================================================================+
| ``public event System.Action<bool> ActiveChanged`` | Raised when any wheel enters or leaves ABS pressure reduction; payload is the new active state. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                | Meaning                                                                                                                                    |
+=======================================================================+============================================================================================================================================+
| ``public virtual bool Active { get; protected set; }``                | Whether ABS is currently reducing service-brake pressure on at least one wheel.                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                       | Default local priority within phase/category.                                                                                              |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MaximumSlip { get; protected set; }``          | Highest measured braking-slip ratio in the latest ABS step.                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumPressure``                                      | Lowest retained fraction of requested service-brake torque. Zero allows complete pressure release.                                         |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MinimumPressureScale { get; protected set; }`` | Lowest retained service-brake fraction in the latest step; one means no intervention.                                                      |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumReleaseDuration``                               | Minimum duration of a pressure-release pulse, giving the tire time to recover rotation. Initial value: ``.04f``.                           |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumSpeedKph``                                      | Minimum contact speed in km/h for pressure modulation. Below this speed normal brakes can stop and hold the vehicle. Initial value: ``5``. |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                     | Execution phase; ABS runs during Braking after service-brake demand is applied.                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float recoverySlip``                                         | Braking-slip ratio below which pressure builds again. Kept below Target Slip to avoid rapid switching. Initial value: ``.1f``.             |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float recoveryTime``                                         | Seconds to rebuild full pressure once the tire rolls again. Initial value: ``.12f``.                                                       |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float releaseTime``                                          | Seconds to release full service-brake pressure after detecting a locking tire. Initial value: ``.035f``.                                   |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float targetSlip``                                           | Longitudinal braking-slip ratio that starts pressure release. A locked tire has a ratio near one. Initial value: ``.2f``.                  |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                  | Role and behavior                                                                                     | Arguments and result |
+============================================================================================+=======================================================================================================+======================+
| ``public override void Configure(VehicleController vehicle)``                              | Clears transient intervention state when the module is configured.                                    | —                    |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual float GetPressureScale(Wheel wheel)``                                     | Returns the retained service-brake fraction for this wheel, or one when no modulation history exists. | —                    |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void ResetVehicleState(VehicleResetReason reason)``                       | Clears transient state when the vehicle is reset.                                                     | —                    |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetAbsEnabled(bool value)``                                          | Enables or disables ABS through the module enabled state; disabling clears pressure history.          | —                    |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Updates the mechanism for this vehicle, command and fixed-step duration.                              | —                    |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Returns whether the profile requires wheel-based mechanics.                                           | —                    |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-drivedynamics--automaticgearbox:

AutomaticGearbox
----------------

**Runtime/Engine/Gearbox/AutomaticGearbox.cs**

Makes automatic shift decisions from operating conditions.

**Inherits / implements:** :ref:`Gearbox <uvs-api-drivedynamics--gearbox>`.

.. _uvs-api-drivedynamics--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                                                                                                                                     |
+======================================================+=============================================================================================================================================================================================================================+
| ``public override bool AutomaticDirection { get; }`` | Read-only/resolved automatic direction for ``AutomaticGearbox``.                                                                                                                                                            |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float downshiftRpm``                        | Downshift in revolutions per minute. Initial value: ``2500``.                                                                                                                                                               |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumGearTime``                     | Minimum dwell before automatic upshifts and direction changes (.7 seconds). Low-RPM downshifts bypass this dwell and may skip ratios; shift duration, loaded-road-speed evidence, clutch guards and RPM limits still apply. |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reverseEngageSpeedKph``               | Maximum speed treated as standstill for automatic reverse selection (km/h); allows small suspension/creep motion on slopes.                                                                                                 |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float upshiftRpm``                          | Upshift in revolutions per minute. Initial value: ``7000``.                                                                                                                                                                 |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-1:

Methods
~~~~~~~

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| Signature                                                             | Role and behavior                                                                                                                                                    | Arguments and result                              |
+=======================================================================+======================================================================================================================================================================+===================================================+
| ``public override void ResetVehicleState(VehicleResetReason reason)`` | Respawn clears reverse-input admission, cancels pending shifting and restores forward launch through the base reset. Other reset reasons leave this state unchanged. | ``reason`` — Reset stage supplied by the vehicle. |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+

.. _uvs-api-drivedynamics--boostsuspensionsettings:

BoostSuspensionSettings
-----------------------

**Runtime/Drive/Suspension/BoostSuspensionSettings.cs**

Shared physical suspension kick configuration. See :ref:`setup and behavior <uvs-drivingactions--suspension-kick-and-departure-wheelspin>`.

.. _uvs-api-drivedynamics--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Member                           | Meaning                                                                                                                                      |
+==================================+==============================================================================================================================================+
| ``public bool enabled``          | Enable effect; default true.                                                                                                                 |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float frontLift``       | Front extension in metres; default 0.035.                                                                                                    |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumTilt``     | Gravity-relative pitch/roll cancellation angle; default 20 degrees. A fresh boost press is required after automatic suspension cancellation. |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rearCompression`` | Rear compression in metres; default 0.02.                                                                                                    |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float returnTime``      | Smooth recovery in seconds; default 0.3.                                                                                                     |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float riseTime``        | Smooth rise in seconds; default 0.15.                                                                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--brakes:

Brakes
------

**Runtime/Drive/Brakes/Brakes.cs**

Configuration/implementation type for brakes within engine and drivetrain.

**Inherits / implements:** :ref:`DriveModule <uvs-api-driveprofiles--drivemodule>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Member                                                    | Meaning                                                                                                          |
+===========================================================+==================================================================================================================+
| ``public event System.Action<bool> BrakingChanged``       | Moving service-brake activity changes; payload is active/inactive. Owned by Brakes, independent of TireFeedback. |
+-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> HandbrakeChanged``     | When resolved handbrake state changes. Payload: bool.                                                            |
+-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<float> ServiceBrakeChanged`` | When resolved service braking changes. Payload: normalized resolved brake demand.                                |
+-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                        | Meaning                                                                                                                                                                                             |
+===============================================================+=====================================================================================================================================================================================================+
| ``public float brakeEventMinimumSpeedKph``                    | Brake event minimum speed in km/h (stored value); Speed fields display the selected speed unit. Initial value: ``3``.                                                                               |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakeEventThreshold``                          | Threshold/tolerance for brake event threshold. The corresponding action or transition is admitted only when its comparison condition is satisfied. Initial value: ``.1f``.                          |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakeRiseTime``                                | Seconds for a held digital brake to reach full service-brake strength. Zero is immediate.                                                                                                           |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float DigitalBrakeStrength { get; }``        | Read-only/resolved digital brake strength for Brakes.                                                                                                                                               |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Engine engine``                                      | Optional explicit link when engine and brakes live on different objects.                                                                                                                            |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``               | Default local priority within phase/category.                                                                                                                                                       |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Handbrake { get; protected set; }``     | Read-only/resolved handbrake for Brakes.                                                                                                                                                            |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float handbrakeTorque``                              | Force/torque budget for handbrake torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``6000``. |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``             | Cross-category execution barrier used by the module pipeline.                                                                                                                                       |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool progressiveDigitalBraking``                     | Ramp button/keyboard service braking. Analog pedals always use their exact input strength.                                                                                                          |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rollingBrakeTorque``                           | Optional constant brake torque while coasting. Zero allows natural downhill rolling.                                                                                                                |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ServiceBrake { get; protected set; }`` | Resolved service-brake demand consumed by downstream mechanics and pedal presentation.                                                                                                              |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float slopeReverseReleaseGrace``                     | Seconds to recognize a fresh reverse press after releasing a stopped brake on a slope. Does not engage reverse from a continuously held brake.                                                      |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-2:

Methods
~~~~~~~

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                | Arguments and result                                                                                                                                            |
+=========================================================================+==================================================================================================================+=================================================================================================================================================================+
| ``public override void Configure(VehicleController v)``                 | Resolves an Engine reference only when no explicit engine is assigned.                                           | ``v`` — V, interpreted by this operation in the declared type.                                                                                                  |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Resolves signed-pedal direction/braking policy, publishes actuator demand and applies service/handbrake torques. | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.                             | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.    |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--burnout:

Burnout
-------

**Runtime/Drive/Grounded/Burnout.cs**

**Inherits / implements:** :ref:`DriveModule <uvs-api-driveprofiles--drivemodule>`, :ref:`IVehicleResetHandler <uvs-api-modules--ivehicleresethandler>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+--------------------------------------------------------+
| Member                                            | Meaning                                                |
+===================================================+========================================================+
| ``public event System.Action BurnoutStarted``     | Assistance begins.                                     |
+---------------------------------------------------+--------------------------------------------------------+
| ``public event System.Action BurnoutStopped``     | Assistance ends, including reset/disable.              |
+---------------------------------------------------+--------------------------------------------------------+
| ``public event System.Action<bool> StateChanged`` | Reports transitions into and out of active assistance. |
+---------------------------------------------------+--------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                  | Meaning                                                                                                                                                                                          |
+=========================================================+==================================================================================================================================================================================================+
| ``public bool automaticThrottle``                       | Supply a throttle request in the selected drive direction before brakes/gearbox/clutch while the held launch request is eligible. Default true.                                                  |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float boatBowLiftDegrees``                     | Extra boat powered-pitch target degrees while Burnout is active; default 2, range 0–5; existing tilt/pitch guards remain.                                                                        |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool bypassStabilityControl``                  | Temporarily skip Steering arcade yaw/lateral stabilization and slide speed hold during burnout. Default true; authored assist settings are preserved.                                            |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool bypassTractionControl``                   | Let intentional wheelspin pass through the optional TCS while assistance is nonzero. Default true; normal TCS resumes after recovery.                                                            |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float cooldown``                               | Seconds before starting another cycle after release/abort. Default 0.4.                                                                                                                          |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float CooldownRemaining { get; }``             | Seconds before another launch can begin.                                                                                                                                                         |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``         | 240; resolves wheelspin before engine torque.                                                                                                                                                    |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool forceForwardDirection``                   | Request forward drive during boost; disable to retain the selected direction. Default true.                                                                                                      |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float forwardGrip``                            | Driven tire longitudinal grip scale during wheelspin. Default 0.55, allowing forward motion while spinning.                                                                                      |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float gripRecoveryTime``                       | Recovery interval after spin or release. Default 0.4 seconds.                                                                                                                                    |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float holdBrakeTorque``                        | Maximum per-wheel holding torque in N m before wheel brake multipliers. Default 8000.                                                                                                            |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float holdDuration``                           | Seconds at full non-driven-wheel hold. Default 0.6.                                                                                                                                              |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool holdNonDrivenWheels``                     | Optional non-driven-wheel brake hold; disabled by default so the vehicle moves during wheelspin.                                                                                                 |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float holdReleaseTime``                        | Seconds to smoothly release that hold. Default 0.4.                                                                                                                                              |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsActive { get; }``                       | Whether the installed module currently assists wheelspin.                                                                                                                                        |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumSpinSpeed``                       | Safety speed cutoff for wheelspin assistance, independent of sustained steering. Default 60 m/s (216 km/h).                                                                                      |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumStartSpeed``                      | Highest speed at which a new burnout may start. Default 40 m/s (144 km/h), including starts while already driving.                                                                               |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumEndSpeed``                        | Minimum road speed in m/s required for timed recovery while held. Default 12 (43.2 km/h); zero uses duration alone. Clamped to maximumSpinSpeed. Key release always begins recovery immediately. |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``       | Power in the Drive category; native profiles consume the resolved boost during Drive.                                                                                                            |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Progress { get; }``                      | Elapsed spin and recovery fraction.                                                                                                                                                              |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool Requested { get; }``                      | Explicit held API request.                                                                                                                                                                       |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float sidewaysGrip``                           | Driven tire lateral grip scale during wheelspin. Default 0.4 for drifting and donuts; normal grip returns during recovery.                                                                       |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spinDuration``                           | Minimum held wheelspin duration before recovery. Default 3 seconds; recovery also requires minimumEndSpeed and no sustained steering.                                                            |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Strength { get; }``                      | Current wheelspin assistance fraction.                                                                                                                                                           |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsDirectControl { get; }`` | Processes direct mode to clear assistance.                                                                                                                                                       |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public BurnoutSuspensionSettings suspensionKick``     | Supported front/rear spring shift; enabled by default, with a 0.9-second return.                                                                                                                 |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float sustainSteeringThreshold``               | Steering magnitude required to retain a held powered slide. Default 0.15.                                                                                                                        |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool sustainWhileSteering``                    | Hold wheelspin while steering beyond sustainSteeringThreshold, even after the duration and minimum end speed. Default true; releasing Ctrl or the safety cutoff still ends assistance.           |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float throttle``                               | Automatic forward pedal strength. Default 1; range 0.1 to 1.                                                                                                                                     |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float torqueMultiplier``                       | Maximum temporary combustion/direct torque and finite power/acceleration-cap multiplier. Default 2.5; minimum 1.                                                                                 |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float wheelSpeedMultiplier``                   | Bounded native wheel overspeed allowance during wheelspin. Default 1.5; range 1–2; prevents runaway wheel energy.                                                                                |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-3:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Signature                                                                           | Role and behavior                                                                                                   | Arguments and result                                                                          |
+=====================================================================================+=====================================================================================================================+===============================================================================================+
| ``public override void Configure(VehicleController vehicle)``                       | Caches the owning vehicle and resolves missing engine references during repeatable setup.                           | Uses the supplied vehicle and command context; returns the profile-specific admission result. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public void ResetState()``                                                        | Clear launch request, wheelspin, hold and cooldown.                                                                 | See signature for arguments.                                                                  |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual void ResetVehicleState(VehicleResetReason reason)``                | Clears transient state for the supplied reset reason without changing persistent configuration.                     | —                                                                                             |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public void SetBurnout(bool held)``                                               | Set a held launch request; false starts recovery immediately.                                                       | See signature for arguments.                                                                  |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float dt)`` | Advance rolling or standing wheelspin, sustained powered turns and release recovery; apply optional holding brakes. | See signature for arguments.                                                                  |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--burnoutsuspensionsettings:

BurnoutSuspensionSettings
-------------------------

**Runtime/Drive/Suspension/BoostSuspensionSettings.cs**

**Inherits / implements:** :ref:`BoostSuspensionSettings <uvs-api-drivedynamics--boostsuspensionsettings>`.

.. _uvs-api-drivedynamics--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                         | Meaning                                                                                                                                                                                                                                                    |
+================================================+============================================================================================================================================================================================================================================================+
| ``public float maximumForwardActivationSpeed`` | Maximum forward speed for starting suspension kick, default 5 m/s (18 km/h). Reverse movement has no lower bound. An accepted kick remains active above this threshold; a rejected start requires a fresh press. Independent of burnout propulsion limits. |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--clutch:

Clutch
------

**Runtime/Engine/Gearbox/Clutch.cs**

Models coupling and finite rotational energy transfer.

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-3:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Member                                                  | Meaning                                                                                            |
+=========================================================+====================================================================================================+
| ``public event System.Action<bool> AutomaticChanged``   | When automatic clutch assistance selection changes. Payload: bool.                                 |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public event System.Action<float> EngagementChanged`` | When resolved clutch coupling changes. Payload: normalized engagement, distinct from pedal travel. |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                                                                                                                                |
+=============================================================+========================================================================================================================================================================================================+
| ``public bool allowLaunchWheelspin``                        | Let stored flywheel energy briefly exceed traction control's propulsion budget on a clutch launch.                                                                                                     |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool automatic``                                   | Assist normal launches/coasting. Touching the clutch pedal always gives the driver direct control.                                                                                                     |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool DriverControlled { get; }``           | Whether manual mode or a pedal override currently controls clutch engagement.                                                                                                                          |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Engagement { get; protected set; }`` | Resolved clutch coupling fraction: zero disconnected, one connected.                                                                                                                                   |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engagementRate``                             | Automatic assistance only. Driver pedal/button input is applied immediately.                                                                                                                           |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Engine engine``                                    | Assign the engine Engine component/asset used by Clutch.                                                                                                                                               |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineBrakingTorque``                        | Force/torque budget for engine braking torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``35``. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``             | Default local priority within phase/category.                                                                                                                                                          |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float manualEngagement``                           | Manual clutch engagement fraction: 0 disconnects the drivetrain and 1 requests full engagement. Initial value: ``1``.                                                                                  |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Pedal { get; protected set; }``      | Clutch pedal travel: zero released, one fully pressed; opposite direction to engagement.                                                                                                               |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``           | Cross-category execution barrier used by the module pipeline.                                                                                                                                          |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float SlipRpm { get; }``                   | Engine RPM minus gearbox-reflected wheel RPM; measures coupling slip.                                                                                                                                  |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float torqueCapacity``                             | Maximum crankshaft torque transmitted by a fully engaged clutch, in Nm.                                                                                                                                |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-4:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                        | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+==========================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Resolves the engine only when no explicit reference is assigned.                                         | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAutomatic(bool value)``                                           | Chooses automatic clutch assistance rather than manual engagement ownership.                             | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetManualEngagement(float value)``                                   | Requests normalized manual clutch coupling, distinct from clutch pedal travel.                           | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                                                                             |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Advances manual/automatic coupling and publishes ``EngagementChanged`` after a resolved coupling change. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--differential:

Differential
------------

**Runtime/Engine/Drivetrain/Differential.cs**

Distributes driven axle torque.

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`.

.. _uvs-api-drivedynamics--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                                                                                                                |
+===================================================+========================================================================================================================================================================================================+
| ``public Axle[] axles``                           | Ordered axles configuration entries. Expand each item; see Differential.Axle for its individual settings. Initial value: ``Array.Empty<Axle>()``.                                                      |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                                                                                                                                          |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lockedCoupling``                   | Strength of the RPM-equalizing coupling in locked differential mode. Initial value: ``4``.                                                                                                             |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLockTorque``                | Force/torque budget for maximum lock torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``1000``. |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public DifferentialMode mode``                  | Selects the operating policy; see the listed options and the owning component guide. Options: ``Open``, ``LimitedSlip``, ``Locked``. Initial value: ``DifferentialMode.LimitedSlip``.                  |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                                                                                                          |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float slipRpmRange``                     | Wheel RPM difference that produces the full speed-based limited-slip bias. Initial value: ``150``.                                                                                                     |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float torqueBiasRatio``                  | Multiplier/fraction controlling torque bias ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: ``3``.                                                     |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tractionCoefficient``              | Scales the traction estimate used to distribute differential torque. Initial value: ``1``.                                                                                                             |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-5:

Methods
~~~~~~~

+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                      | Arguments and result                                                                                                                                            |
+=========================================================================+========================================================================================================+=================================================================================================================================================================+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Distributes axle torque and bounded shaft coupling; skips adding propulsion while service/handbraking. | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.                   | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.    |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--differentialaxle:

Differential.Axle
-----------------

**Runtime/Engine/Drivetrain/Differential.cs**

Configuration/implementation type for axle within engine and drivetrain.

.. _uvs-api-drivedynamics--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                          | Meaning                                                                                                                                                   |
+=================================+===========================================================================================================================================================+
| ``public bool enabled``         | Includes this entry in its owning system's configured behavior. Initial value: ``true``.                                                                  |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider first``  | Assign the first reference used by Differential.Axle. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string label``         | Readable name identifying this entry in configuration lists. Initial value: ``"Axle"``.                                                                   |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider second`` | Assign the second reference used by Differential.Axle. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--differentialmode:

DifferentialMode
----------------

**Runtime/Engine/Drivetrain/Differential.cs**

Defines the allowed differential mode choices used by this topic.

.. _uvs-api-drivedynamics--values:

Values
~~~~~~

-  ``Open``
-  ``LimitedSlip``
-  ``Locked``

.. _uvs-api-drivedynamics--drivingassists:

DrivingAssists
--------------

**Runtime/Drive/Core/DrivingAssists.cs**

Configuration/implementation type for driving assists within engine and drivetrain.

**Inherits / implements:** :ref:`DriveModule <uvs-api-driveprofiles--drivemodule>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-4:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                 |
+==============================================================+=========================================================================================+
| ``public event System.Action<bool> StabilityControlChanged`` | When ``DrivingAssists`` changes its stability-assistance choice. Payload: bool.         |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public event System.Action<bool> TractionControlChanged``  | When ``DrivingAssists`` changes its coordinated traction-control choice. Payload: bool. |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                                                                 |
+===================================================+=========================================================================================================================================================+
| ``public float corneringFreedom``                 | Amount of cornering freedom retained while allocating traction between propulsion and turning. Initial value: ``.65f``.                                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lateralResponse``                  | Strength of sideways-motion correction relative to the vehicle. Initial value: ``5``.                                                                   |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchReferenceSpeed``             | Low-speed reference in m/s used to stabilize slip/traction calculations during launch. Initial value: ``3``.                                            |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumYawRate``                   | Upper requested yaw rate used by turning assistance, in rad/s.                                                                                          |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumTorqueScale``               | Multiplier/fraction controlling minimum torque scale. Increasing it increases this contribution relative to the unscaled value. Initial value: ``.2f``. |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                                                           |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float recoveryRate``                     | Rate at which allowed drive torque recovers after excess slip subsides. Initial value: ``4``.                                                           |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reductionRate``                    | Rate at which allowed drive torque decreases when wheel slip exceeds the target. Initial value: ``8``.                                                  |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reserveGripForCornering``           | When checked, reserve grip for cornering is active; when unchecked the owning system skips that optional policy.                                        |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool stabilityControlEnabled``           | Enables stability control behavior for this system. Initial value: ``true``.                                                                            |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float stabilityStrength``                | Overall blend/strength of the stability corrections; zero removes this assistance contribution. Initial value: ``.72f``.                                |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool stabilizePoweredSlides``            | Allows stability assistance to correct powered sliding instead of leaving it entirely to driver input. Initial value: ``true``.                         |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float targetSlip``                       | Desired longitudinal slip magnitude while applying propulsion torque. Initial value: ``.24f``.                                                          |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool tractionControlEnabled``            | Enables traction control behavior for this system. Initial value: ``true``.                                                                             |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tractionReserve``                  | Fraction of estimated traction kept available when limiting drive torque. Initial value: ``.98f``.                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawResponse``                      | Strength/speed of the yaw response toward the requested heading/turn behavior. Initial value: ``7.5f``.                                                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-6:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                              | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+================================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual void Apply()``                                                            | Writes coordinated traction/stability assist choices to the connected mechanics. Disabling the coordinator does not restore previous settings. | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Caches the vehicle and applies its coordinated assist choices.                                                                                 | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAssistsEnabled(bool value)``                                      | Applies the application's combined assist enable choice through ``DrivingAssists``.                                                            | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetStabilityControl(bool value)``                                    | Changes the coordinated stability-assistance choice.                                                                                           | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTractionControl(bool value)``                                     | Changes the coordinated traction-control choice through ``DrivingAssists``.                                                                    | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies the coordinator's current traction/stability choices to its connected mechanics.                                                       | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--engine:

Engine
------

**Runtime/Engine/Engine.cs**

Resolves running state, RPM and propulsion torque/power.

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`, :ref:`IVehicleResetHandler <uvs-api-modules--ivehicleresethandler>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-5:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                  |
+==============================================================+==========================================================================================================================+
| ``public event System.Action<Gearbox> ActiveGearboxChanged`` | Reports a change of effective gearbox identity, including removal or disable. Read ActiveGearbox when first subscribing. |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> EngineStateChanged``      | After engine running state changes. Payload: running bool; a rejected start does not report success.                     |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<int> GearChanged``              | After accepted gear selection. Payload: signed gear index, with reverse -1, neutral 0 and forward gears positive.        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                   | Meaning                                                                                                                                                                                                                                                    |
+==========================================================================+============================================================================================================================================================================================================================================================+
| ``public virtual Gearbox ActiveGearbox { get; }``                        | Currently enabled connected gearbox, or ``null`` when no enabled gearbox participates.                                                                                                                                                                     |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float airborneTorqueWeight``                                    | Relative torque weight of airborne wheels when other driven wheels have contact. One disables contact-based redistribution.                                                                                                                                |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float AverageWheelRpm { get; protected set; }``         | Read-only/resolved average wheel rpm for Engine.                                                                                                                                                                                                           |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Clutch clutch``                                                 | Assign the clutch Clutch component/asset used by Engine.                                                                                                                                                                                                   |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool compensateDriveResistance``                                | Allow available torque to overcome measured opposing load and gravity without spending the acceleration budget; default true. Does not create torque or bypass tire traction.                                                                              |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float directSpeedLimiterRangeKph``                              | Additional speed fade range in km/h used by direct drive.                                                                                                                                                                                                  |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float DriveDirectionSign { get; }``                     | +1 normally, -1 when longitudinal propulsion is inverted.                                                                                                                                                                                                  |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float EffectiveMaxRpm { get; }``                        | Current engine redline including an active Nitro percentage increase. Base maxRpm is preserved; stop/release/depletion/disable restore the normal limit. Used by engine RPM targets, rev limiting, torque curve normalization and gearbox over-rev guards. |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool EngineRunning { get; }``                           | Read-only/resolved engine running for Engine.                                                                                                                                                                                                              |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                          | Default local priority within phase/category.                                                                                                                                                                                                              |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float FlywheelEnergyJoules { get; }``                   | Read-only/resolved flywheel energy joules for Engine.                                                                                                                                                                                                      |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Gearbox gearbox``                                               | Optional plugin. Missing or disabled gearbox uses the original direct drive.                                                                                                                                                                               |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual string GearLabel { get; }``                             | Read-only/resolved gear label for Engine.                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float idleRpm``                                                 | Engine idle speed in revolutions per minute. Initial value: ``900``.                                                                                                                                                                                       |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float InertialDriveTorque { get; protected set; }``     | Read-only/resolved inertial drive torque for Engine.                                                                                                                                                                                                       |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float internalFriction``                                        | Fraction of peak torque lost to internal friction at maximum RPM with a driver-controlled clutch.                                                                                                                                                          |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool invertDriveDirection``                                     | Reverses longitudinal propulsion while retaining logical throttle and gear direction.                                                                                                                                                                      |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsRunning { get; }``                               | Current is running predicate; read it instead of maintaining a second application flag.                                                                                                                                                                    |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchBlendSpeed``                                        | Forward speed in m/s at which launch RPM support fully fades to idle RPM.                                                                                                                                                                                  |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchRpm``                                               | Engine speed target used for initial launch/clutch engagement. Initial value: ``3200``.                                                                                                                                                                    |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDriveAcceleration``                                | Propulsion acceleration budget in m/s²; zero disables the limit. Compensate Drive Resistance additionally admits opposing load within available torque/power.                                                                                              |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumPowerKw``                                          | Maximum output power in ``kW``; zero disables the power cap.                                                                                                                                                                                               |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maxRpm``                                                  | Engine upper speed limit in revolutions per minute. Initial value: ``8000``.                                                                                                                                                                               |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float NormalizedRpm { get; }``                          | Engine RPM normalized between idle and the current EffectiveMaxRpm.                                                                                                                                                                                        |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float OutputTorque { get; protected set; }``            | Resolved propulsion torque after direction inversion; downstream allocation/intervention may limit wheel output.                                                                                                                                           |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float peakTorque``                                              | Peak crankshaft combustion torque before ratio multiplication, in N·m.                                                                                                                                                                                     |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                        | Cross-category execution barrier used by the module pipeline.                                                                                                                                                                                              |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float response``                                                | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``3``.                                                                                                    |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reverseSpeedRatio``                                       | Multiplier/fraction controlling reverse speed ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: ``0.3f``.                                                                                                    |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float revLimiterRange``                                         | RPM range over which the coupled shaft rev limiter fades propulsion torque.                                                                                                                                                                                |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rotationalInertia``                                       | Engine/flywheel rotational inertia in kg m², used when the driver operates the clutch.                                                                                                                                                                     |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Rpm { get; protected set; }``                     | Resolved engine rotational speed in revolutions per minute.                                                                                                                                                                                                |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rpmResponse``                                             | Response toward rpm response. Higher values follow the requested state faster. Initial value: ``10``.                                                                                                                                                      |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float shiftRpmResponse``                                        | RPM response per second while shifting. Lower values give a slower RPM drop, independently of vehicle type.                                                                                                                                                |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float speedLimiterRangeKph``                                    | Road-speed range in km/h over which propulsion fades near the top speed.                                                                                                                                                                                   |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsDirectControl { get; }``                  | Opts into direct-mode stepping; updates RPM and gearbox presentation without propulsion forces.                                                                                                                                                            |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsReleasedForces { get; }``                 | Keeps passive maintenance/observation active during release; Drive and Engine suppress force output, and TireCollision keeps native solid proxies without supplemental tread forces.                                                                       |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Throttle { get; }``                               | Read-only/resolved throttle for Engine.                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationCurve torqueCurve``                                    | Engine torque shape over normalized engine speed. Tune together with the engine torque and RPM limits.                                                                                                                                                     |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float TransmittedClutchTorque { get; protected set; }`` | Read-only/resolved transmitted clutch torque for Engine.                                                                                                                                                                                                   |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-7:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                         | Arguments and result                                                                                                                                            |
+=========================================================================+===========================================================================================================================+=================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``           | Caches the owner, synchronizes running state, configures registered gearboxes and resolves missing drivetrain references. | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                    |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetState()``                                    | Clears the declaring mechanic's retained simulation history at an explicit reset boundary.                                | No arguments; no returned value.                                                                                                                                |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetVehicleState(VehicleResetReason reason)``    | Clears transient state for the supplied reset reason without changing persistent configuration.                           | —                                                                                                                                                               |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEngineRunning(bool running)``                  | Requests the engine running state through ignition/fuel policy and transition notifications.                              | ``running`` — Requested running state.                                                                                                                          |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StartEngine()``                                   | Requests ignition, respecting the active fuel/engine policy.                                                              | No arguments; no returned value.                                                                                                                                |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Resolves running state, demand, RPM and torque output; stopped engines clear their propulsion state.                      | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StopEngine()``                                    | Requests engine shutdown and running-state notifications.                                                                 | No arguments; no returned value.                                                                                                                                |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleEngine()``                                  | Requests the opposite engine-running state through ignition/shutdown policy.                                              | No arguments; no returned value.                                                                                                                                |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--enginecore:

EngineCore
----------

**Runtime/Engine/Core/EngineCore.cs**

Configuration/implementation type for engine core within engine and drivetrain.

**Inherits / implements:** :ref:`CategoryCore <uvs-api-modules--categorycore>`.

.. _uvs-api-drivedynamics--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-8:

Methods
~~~~~~~

+-------------------------+------------------------------------------------------------+--------------------------------------------------------------------+
| Signature               | Role and behavior                                          | Arguments and result                                               |
+=========================+============================================================+====================================================================+
| ``public EngineCore()`` | Constructs ``EngineCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+-------------------------+------------------------------------------------------------+--------------------------------------------------------------------+

.. _uvs-api-drivedynamics--enginemodule:

EngineModule
------------

**Runtime/Engine/Core/EngineModule.cs**

Configuration/implementation type for engine module within engine and drivetrain.

**Inherits / implements:** :ref:`VehicleModule <uvs-api-modules--vehiclemodule>`, :ref:`IEngineModule <uvs-api-modules--ienginemodule>`.

.. _uvs-api-drivedynamics--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--gearbox:

Gearbox
-------

**Runtime/Engine/Gearbox/Gearbox.cs**

Shared validated selection, ratios and shift state.

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-6:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                                           |
+====================================================+===================================================================================================================+
| ``public event System.Action<int> GearChanged``    | After accepted gear selection. Payload: signed gear index, with reverse -1, neutral 0 and forward gears positive. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<int> ShiftCompleted`` | When that shift interval completes; a zero-duration shift can complete immediately. Payload: gear index.          |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<int> ShiftStarted``   | When an accepted selection starts its shift interval. Payload: selected gear index.                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-13:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                              | Meaning                                                                                                                                                                            |
+=====================================================+====================================================================================================================================================================================+
| ``public virtual bool AutomaticDirection { get; }`` | Read-only/resolved automatic direction for Gearbox.                                                                                                                                |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int CurrentGear { get; }``         | Selected signed gear index: -1 reverse, 0 neutral, positive forward.                                                                                                               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float directionChangeSpeed``               | Maximum movement speed at which a requested forward/reverse change is admitted. Initial value: ``0.6f``.                                                                           |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float efficiency``                         | Fraction of drivetrain output retained after transmission losses. Initial value: ``0.9f``.                                                                                         |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float finalDrive``                         | Final-drive ratio multiplying the selected gear ratio. Initial value: ``3.4f``.                                                                                                    |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float[] forwardRatios``                    | Forward gear ratios, first gear at index 0. Used directly with no custom speed ranges.                                                                                             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int GearCount { get; }``           | Number of configured forward gears.                                                                                                                                                |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual string GearLabel { get; }``        | Read-only/resolved gear label for Gearbox.                                                                                                                                         |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float[] gearSpeedLimitsKph``               | Optional road speed at engine redline per forward gear, in km/h. Empty uses the authored Forward Ratios directly. Non-empty values derive ratios from wheel radius and engine RPM. |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsShifting { get; }``         | Whether the gearbox's configured shift interval is still active.                                                                                                                   |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Ratio { get; }``             | Current signed transmission ratio including the declaring gearbox's ratio policy.                                                                                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reverseRatio``                       | Positive reverse gear reduction before final drive.                                                                                                                                |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reverseSpeedLimitKph``               | Optional reverse road speed at redline; zero preserves the authored Reverse Ratio.                                                                                                 |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float shiftDuration``                      | Time in seconds during which gear-changing torque transfer is interrupted/blended. Initial value: ``.14f``.                                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-9:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                            | Role and behavior                                                                                                                                                                                                                                                                          | Arguments and result                                                                                                                                                                                                                                                                                                                                        |
+======================================================================================================================+============================================================================================================================================================================================================================================================================================+=============================================================================================================================================================================================================================================================================================================================================================+
| ``public virtual void ConfigureFor(VehicleController vehicle, Engine engine)``                                       | Connects and prepares the gearbox for its vehicle and engine context.                                                                                                                                                                                                                      | ``vehicle`` — Vehicle context/owner receiving the operation. ``engine`` — Engine whose running/RPM/gearbox state supplies the operation.                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetVehicleState(VehicleResetReason reason)``                                                 | Respawn cancels an unfinished shift; automatic direction returns to first gear. AutomaticGearbox also clears reverse-input admission. Other reset reasons leave this state unchanged.                                                                                                      | —                                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Simulate(VehicleController vehicle, Command command, float wheelRpm, float maxRpm, float dt)`` | Advances gearbox shift/selection state for one mechanical timestep.                                                                                                                                                                                                                        | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``wheelRpm`` — Wheel rotational speed in revolutions per minute. ``maxRpm`` — Engine redline used for selection validation. ``dt`` — Elapsed time in seconds.                                           |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Synchronize(int gear)``                                                                        | Synchronizes the gear selector as an explicit helper. It does not replace ``TrySelectGear`` safety validation for driving input.                                                                                                                                                           | ``gear`` — Signed gear index: -1 reverse, 0 neutral, positive forward.                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySelectGear(int gear, float forwardSpeed, float wheelRpm, float maxRpm)``                    | Selects a signed gear (-1 reverse, 0 neutral, positive forward). Rejects invalid/unchanged gears, an active shift, unsafe direction changes or unsafe over-rev. The vehicle overload verifies this is the engine's active gearbox; the numeric overload takes explicit speed/RPM evidence. | ``gear`` — Signed gear index: -1 reverse, 0 neutral, positive forward. ``forwardSpeed`` — Signed forward speed in m/s. ``wheelRpm`` — Wheel rotational speed in revolutions per minute. ``maxRpm`` — Engine redline used for selection validation. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySelectGear(int gear, VehicleController vehicle)``                                           | Selects a signed gear (-1 reverse, 0 neutral, positive forward). Rejects invalid/unchanged gears, an active shift, unsafe direction changes or unsafe over-rev. The vehicle overload verifies this is the engine's active gearbox; the numeric overload takes explicit speed/RPM evidence. | ``gear`` — Signed gear index: -1 reverse, 0 neutral, positive forward. ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryShiftDown(VehicleController vehicle)``                                                      | Requests the next lower gear through the gearbox's validated selection path.                                                                                                                                                                                                               | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryShiftUp(VehicleController vehicle)``                                                        | Requests the next higher gear through the gearbox's validated selection path.                                                                                                                                                                                                              | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--manualgearbox:

ManualGearbox
-------------

**Runtime/Engine/Gearbox/ManualGearbox.cs**

Provides the manually selected gearbox implementation.

**Inherits / implements:** :ref:`Gearbox <uvs-api-drivedynamics--gearbox>`.

.. _uvs-api-drivedynamics--motorcyclebalance:

MotorcycleBalance
-----------------

**Runtime/Drive/Grounded/MotorcycleBalance.cs**

Configuration/implementation type for motorcycle balance within engine and drivetrain.

**Inherits / implements:** :ref:`DriveModule <uvs-api-driveprofiles--drivemodule>`.

.. _uvs-api-drivedynamics--state-and-configuration-14:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                                                                                                                                                                 |
+==============================================================+=========================================================================================================================================================================================================================================================================+
| ``public float accelerationSmoothTime``                      | Smoothing time for measured path acceleration, in seconds. Initial value: ``.2``.                                                                                                                                                                                       |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ActualLean { get; protected set; }``  | Resolved gravity-relative bank around the pitched longitudinal axis, in degrees. Climbing pitch is excluded.                                                                                                                                                            |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool assistBrakingTurns``                           | Keep supported braking turns aligned with steering through bounded physical torque; yields during wheel lift. Default ``true``.                                                                                                                                         |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool assistBurnoutTurns``                           | Enable bounded low-speed heading torque during powered circles with both tires supported. Does not overwrite position or velocity. Default ``true``.                                                                                                                    |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float balanceDamping``                              | Damping applied to roll while maintaining motorcycle balance. Initial value: ``65``.                                                                                                                                                                                    |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float balanceStrength``                             | Strength of the restoring torque toward the requested motorcycle lean. Initial value: ``1200``.                                                                                                                                                                         |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool BalanceSuppressed { get; }``                   | Whether temporary impact suppression or configured driver-ejection policy currently suppresses balance.                                                                                                                                                                 |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakingYawDamping``                           | Fallback braking-slide heading damping when ground assistance is disabled; assisted turns use the shared yaw controller. Default ``6``.                                                                                                                                 |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float burnoutTurnAcceleration``                     | Heading acceleration cap in radians per second squared. Default ``3``.                                                                                                                                                                                                  |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float burnoutTurnLean``                             | Maximum inside bank during assisted powered circles, in degrees; existing clearance and balance limits still apply. Default ``14``.                                                                                                                                     |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float burnoutTurnMaximumSpeed``                     | Maximum assisted circle speed in m/s; fades through the upper quarter of the range. Default ``8``.                                                                                                                                                                      |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float burnoutTurnRate``                             | Maximum assisted heading rate in radians per second. Default ``1.1``.                                                                                                                                                                                                   |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool coordinateSteering``                           | Optional wheel-angle limit based on the supported bank at speed. Initial value: ``false``.                                                                                                                                                                              |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CorneringAccelerationLimit { get; }`` | Supported lateral path acceleration in m/s², derived from gravity, Maximum Lean and Steering Balance Margin.                                                                                                                                                            |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentLean { get; protected set; }`` | Read-only/resolved current lean for ``MotorcycleBalance``.                                                                                                                                                                                                              |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool disableBalanceOnDriverEject``                  | Stop assisted riding balance and Stabilization angular damping/righting when the driver is ejected, allowing native falling and tumbling. A new driver or vehicle respawn restores balance. Ordinary passenger ejection does not affect it.                             |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``              | Default local priority within phase/category.                                                                                                                                                                                                                           |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float fullLeanSpeed``                               | Ground speed in m/s at which full banking is available.                                                                                                                                                                                                                 |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public MotorcycleGroundAssist groundAssist``               | Optional ground-contact assistance for hard turns and boost. Does not act in flight or during requested wheelies. Initial value: ``new MotorcycleGroundAssist()``.                                                                                                      |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundLeanBrakingAcceleration``               | Maximum acceleration opposing excessive outward bank in radians per second squared; physical contact can cause a small transient overshoot. Default ``30``.                                                                                                             |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundLeanLimit``                             | Base side-bank boundary relative to gravity in degrees; slope bank reduction scales this bound on inclined terrain. Default ``55``.                                                                                                                                     |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundLeanLimitMargin``                       | Minimum anticipation margin in degrees before the boundary. Fast outward roll brakes earlier when its stopping distance requires it. Default ``10``.                                                                                                                    |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leanObstacleClearance``                       | Safety margin before a blocked rider bank. Initial value: ``.08`` metres.                                                                                                                                                                                               |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public LayerMask leanObstacleLayers``                      | Solid obstacle layers used by the rider bank-clearance check. Initial value: all layers.                                                                                                                                                                                |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leanRate``                                    | Maximum rate at which requested motorcycle lean changes, in degrees per second. Initial value: ``170``.                                                                                                                                                                 |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leanRateDamping``                             | Feed-forward damping of the requested lean rate.                                                                                                                                                                                                                        |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leanStartSpeed``                              | Ground speed in m/s below which banking fades to zero.                                                                                                                                                                                                                  |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool limitGroundLean``                              | Enable gravity-relative and support-plane bank boundaries on tire support. The latter uses Maximum Lean to retain slope clearance. Brakes outward roll and yields to inward recovery; uses no new ground probes. Default ``true``.                                      |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngularAcceleration``                  | Upper bound on the profile's applied angular acceleration. Initial value: ``150``.                                                                                                                                                                                      |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBrakingYawAcceleration``               | Maximum fallback braking-slide heading deceleration without ground assistance, in radians per second squared. Default ``12``.                                                                                                                                           |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLean``                                 | Largest requested motorcycle lean angle in degrees. Initial value: ``45``.                                                                                                                                                                                              |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float measuredAccelerationWeight``                  | Blend steering anticipation with actual path acceleration; chassis yaw spin does not count as cornering.                                                                                                                                                                |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool nativeCollisionResponseAfterDriverEject``      | After driver ejection, use native collider friction and restitution instead of additional Collisions body-friction, rebound and crash-transfer impulses. Requires Disable Balance On Driver Eject. Driver re-entry or respawn restores configured collision assistance. |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``            | Cross-category execution barrier used by the module pipeline.                                                                                                                                                                                                           |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool preventObstacleLean``                          | Limit assisted bank near solid obstacles using one approximate torso capsule per occupant. Initial value: ``true``.                                                                                                                                                     |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float recoveryAngle``                               | Maximum gravity-relative bank eligible for normal motorcycle balance, in degrees. Pitch is excluded. Initial value: ``65``.                                                                                                                                             |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reversalLeanRate``                            | Opposite-bank target rate in degrees/s, at least Lean Rate. Initial value: ``335``.                                                                                                                                                                                     |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringBalanceMargin``                       | Cornering capacity fraction shared by path assistance and optional wheel-angle limiting. Initial value: ``.95``.                                                                                                                                                        |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringPrediction``                          | Blend from current wheel steering to anticipated driver steering.                                                                                                                                                                                                       |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float TargetLean { get; protected set; }``  | Requested motorcycle lean after steering and speed resolution, in degrees.                                                                                                                                                                                              |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool UseNativeCollisionResponse { get; }``          | Whether driver ejection currently requests native collision response.                                                                                                                                                                                                   |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public MotorcycleWheelieControl wheelieControl``           | Separate bank and turn response while Wheel Lift owns the maneuver, including controlled lowering. Initial value: ``new MotorcycleWheelieControl()``.                                                                                                                   |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-10:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                   | Role and behavior                                                                                                                               | Arguments and result |
+=============================================================================================+=================================================================================================================================================+======================+
| ``public override void Configure(VehicleController vehicle)``                               | Measures wheelbase and prepares wheel/contact geometry for balance response.                                                                    | —                    |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual float ConstrainSteering(VehicleController vehicle, float requestedAngle)`` | Resolve a steering demand inside the configured cornering envelope without changing Rigidbody inertia. Low-speed full lock remains available.   | —                    |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void ResetVehicleState(VehicleResetReason reason)``                        | Clears transient state for the supplied vehicle reset reason.                                                                                   | —                    |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``  | Uses gravity, contact and steering evidence to apply bounded motorcycle lean/balance support.                                                   | —                    |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                              | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                            | —                    |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SuspendBalance(float duration)``                                      | Temporarily release assisted roll control for the given seconds without changing authored settings. Respawn or driver entry clears suppression. | —                    |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-drivedynamics--motorcyclegroundassist:

MotorcycleGroundAssist
----------------------

**Runtime/Drive/Grounded/Assistance/MotorcycleGroundAssist.cs**

Bounded ground-contact, cornering and braking assistance for MotorcycleBalance.

.. _uvs-api-drivedynamics--state-and-configuration-15:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                         | Meaning                                                                                                                                                                                                 |
+================================================+=========================================================================================================================================================================================================+
| ``public float angularDamping``                | Damping of unwanted pitch and roll rate relative to the requested bank. Does not damp yaw. Initial value: ``12``.                                                                                       |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float bankResponseTime``              | Seconds for a critically damped bank-target response. Smooths both pickup and reversal without reducing wheel steering. Initial value: ``.17f``.                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float bankTurnInfluence``             | Contribution of actual bank to the supported turn, including coasting with neutral steering. Initial value: ``.35f``.                                                                                   |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakeRecoveryTime``             | Seconds to restore full service-brake pressure after a load/slip intervention. Initial value: ``.15f``.                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakeReleaseTime``              | Seconds to release service-brake pressure after detecting excessive tire slip. Initial value: ``.04f``.                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakeSlipLimit``                | Tread/road speed slip ratio above which service-brake pressure is eased. Reduced while banked to retain lateral grip. Initial value: ``.25f``.                                                          |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakingLeanScale``              | Fraction of normal maximum bank retained under full braking. One preserves the steering envelope; smaller values deliberately widen braking turns. Initial value: ``1``.                                |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakingResponseMultiplier``     | Response-time multiplier when reversing a turn while braking. Lower values admit the opposite turn sooner. Initial value: ``.65f``.                                                                     |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool brakingSupport``                 | Reserve service-brake grip for steering and ease front pressure when the rear tire unloads. Does not change handbrake or standstill holding. Initial value: ``true``.                                   |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakingYawStrength``            | Correction of persistent unwanted yaw while braking into a requested turn. Zero uses proportional steering response only. Initial value: ``40``.                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float contactAcceleration``           | Maximum contact rebound damping acceleration in m/s² with at least two supported tires. No steady downforce or single-contact hold-down is applied. Initial value: ``15``.                              |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float corneringStrength``             | Multiplier for the supported cornering envelope. Higher values allow tighter assisted turns without raising the rider's maximum bank. Initial value: ``1.85f``.                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enabled``                        | Controls enabled for this mechanism.                                                                                                                                                                    |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float fullSpeed``                     | Ground speed in m/s where full assistance is available. Initial value: ``12``.                                                                                                                          |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float handbrakeSlideDeceleration``    | Extra road-plane deceleration in m/s² at tight handbrake steering; dissipates slide speed without adding yaw. Initial value: ``5``. Zero disables it.                                                   |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngularAcceleration``    | Maximum added pitch/roll angular acceleration in rad/s². Initial value: ``60``.                                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBankRate``               | Maximum bank-target speed in degrees per second. Bank Response Time smooths acceleration and reversal around this limit. Initial value: ``140``.                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBrakingYawAcceleration`` | Maximum requested yaw correction under full service or handbrake braking, in rad/s². Applied through the current chassis inertia. Initial value: ``25``.                                                |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumContactAuthority``       | Minimum turn-assist contact authority with at least two supported tires. Incidental single-tire contact keeps its actual support share; manual wheelie uses separate settings. Initial value: ``.65f``. |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pitchSupport``                  | Restoring pitch acceleration toward the supporting surface, in rad/s² per radian. Inactive without tire contact or during wheelie. Initial value: ``40``.                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rearLoadReserve``               | Rear share of total contact load below which front brake pressure is eased to discourage stoppies. Initial value: ``.12f``.                                                                             |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reduceLeanOnSlopes``             | Reduce the bank request and physical world-bank boundary as terrain gets steeper, retaining ordinary handlebar steering instead. Initial value: ``true``.                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float responseTime``                  | Seconds for the assistance strength to approach a changed steering/boost demand. Initial value: ``.12f``.                                                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float slopeLeanFullAngle``            | Terrain inclination in degrees where the minimum bank scale is reached. Initial value: ``45``.                                                                                                          |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float slopeLeanMinimumScale``         | Fraction of the normal bank request and world-bank boundary retained on steep terrain; handlebar steering stays available. Initial value: ``.2f``.                                                      |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float slopeLeanResponseTime``         | Response time in seconds for following sustained terrain inclination; filters short bumps and smooths the physical bank boundary. Zero is immediate. Initial value: ``.35f``.                           |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float slopeLeanStartAngle``           | Supporting terrain inclination in degrees where bank reduction starts. Initial value: ``5``.                                                                                                            |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float startSpeed``                    | Ground speed in m/s where assistance begins fading in. Initial value: ``3``.                                                                                                                            |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringResponseTime``          | Seconds to ease steering into a new turn while the bank target anticipates the input. Zero disables this easing. Initial value: ``.12f``.                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float stoppiePitchAngle``             | Nose-down pitch relative to the supporting surface, in degrees, at which rear unloading receives full front-pressure relief. Initial value: ``6``.                                                      |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float supportDamping``                | Damping of separating support-point velocity, in 1/s. Does not compress resting suspension. Initial value: ``10``.                                                                                      |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float turnEntrySupport``              | Cornering authority before the chassis banks into a new turn. The rest arrives smoothly with actual lean; parking steering stays unchanged. Initial value: ``.45f``.                                    |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--motorcyclewheeliecontrol:

MotorcycleWheelieControl
------------------------

**Runtime/Drive/Grounded/Assistance/MotorcycleWheelieControl.cs**

Lean and yaw limits while a motorcycle is supported by its rear wheel, with smooth recovery after landing.

.. _uvs-api-drivedynamics--state-and-configuration-16:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                                                          |
+=============================================+==================================================================================================================================================================================+
| ``public float accelerationMultiplier``     | Powered acceleration scale on one driven support with the steering tire raised. Defaults to 1.08; does not increase top speed.                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float balanceDamping``             | Roll damping for rear-wheel balance. Initial value: ``200``.                                                                                                                     |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float balanceStrength``            | Roll spring for rear-wheel balance; separate from the stiffer two-wheel cornering response. Initial value: ``1200``.                                                             |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enabled``                     | Controls enabled for this mechanism.                                                                                                                                             |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float highSpeedLeanScale``         | Fraction of wheelie lean retained at high speed. Reduces single-tire camber wobble. Initial value: ``.65f``.                                                                     |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leanFadeEndSpeed``           | Speed at which High Speed Lean Scale is fully applied. Initial value: ``25``.                                                                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leanFadeStartSpeed``         | Speed above which the small wheelie bank is reduced further. Initial value: ``12``.                                                                                              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leanResponseTime``           | Seconds to ease wheelie bank changes. Does not set the body's rotation. Initial value: ``.2f``.                                                                                  |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLateralAcceleration`` | Arcade sideways acceleration budget in m/s² during wheelie. Allows a useful turn without requiring a large body bank. Initial value: ``3``.                                      |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLean``                | Maximum sideways lean in degrees during wheel lift and controlled lowering. Initial value: ``12``.                                                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRollAcceleration``    | Maximum wheelie roll correction in radians per second squared. Initial value: ``300``.                                                                                           |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumSteeringAngle``       | Maximum wheel angle during wheelie, capped by the vehicle steering lock independently of speed. Recovery blends back to ordinary steering after lowering. Initial value: ``90``. |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumYawAcceleration``     | Maximum wheelie yaw correction in radians per second squared. Initial value: ``8``.                                                                                              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumYawRate``             | Requested wheelie heading rate in radians per second at full steering. Separate from body lean; also limited by Maximum Lateral Acceleration. Initial value: ``.22f``.           |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumContactAuthority``    | Minimum steering-assist authority on the supporting tire. One rear tire is the expected wheelie support, not half of normal support. Initial value: ``1``.                       |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float releaseRecoveryTime``        | Seconds to hand stance, steering and damping back to normal riding after the front wheel settles. Initial value: ``.9f``.                                                        |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float turnResponse``               | Response toward the requested wheelie turn rate. Initial value: ``8``.                                                                                                           |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--nitro:

Nitro
-----

**Runtime/Engine/Boost/Nitro.cs**

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`, :ref:`IVehicleResetHandler <uvs-api-modules--ivehicleresethandler>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-7:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Member                                           | Meaning                                                                                             |
+==================================================+=====================================================================================================+
| ``public event Action<float> AmountChanged``     | Reports actual remaining charge after a change; payload is charge units.                            |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public event Action<bool> BoostStateChanged``  | Reports transitions into/out of resolved boost; payload is the active flag.                         |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public event Action Depleted``                 | Raised once when positive charge reaches zero.                                                      |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public event Action NitroStarted``             | Effective boost begins.                                                                             |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public event Action NitroStopped``             | Effective boost ends, including reset/disable.                                                      |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public event Action<bool> OutputStateChanged`` | Reports a change of the propulsion-output session. Receivers can be absent without affecting boost. |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-17:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                                                                                                                                                                                                           |
+====================================================================+===================================================================================================================================================================================================================================================================================+
| ``public float accelerationMultiplier``                            | Multiplier for the finite wheel-drive acceleration cap. Default 3.                                                                                                                                                                                                                |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float additionalAcceleration``                            | Additional grounded chassis acceleration in m/s², independent of tire torque limits. Default 10; zero uses engine torque only. Stops immediately on release, braking or loss of eligibility; fades near boosted top speed.                                                        |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float additionalMaxRpmPercent``                           | Extra engine redline as a percentage during boost. Default 25 raises 8000 RPM to 10000; zero preserves the normal limit. Scales with final partial boost strength and stays available through an internal shift.                                                                  |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float additionalPowerKw``                                 | Extra engine power allowance in kW. Default 350; an uncapped engine remains uncapped.                                                                                                                                                                                             |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool allowPitchAboveMaxRpm``                              | Default true. Controls RPM-driven Engine Audio pitch above its ordinary maximum when actual RPM exceeds this engine base redline. Applies per Nitro component to sounds following its engine; constant/motion/fixed-pitch sounds remain unchanged. Unity pitch ceiling remains 3. |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool allowReverse``                                       | Permit boost in reverse. Default true.                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool automaticRefill``                                    | Refill automatically after release and refillDelay. Default false; demo Car enables it.                                                                                                                                                                                           |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float buildUpTime``                                       | Seconds for boost power to build from zero to full. Default 0.2; zero gives immediate full power. Release/braking removes assistance immediately. Consumption follows the resolved power fraction. Internal shifts preserve the existing build-up level.                          |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float capacity``                                          | Maximum charge in arbitrary consistent units. Default 100; minimum 0.01.                                                                                                                                                                                                          |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool consumesNitro``                                      | Consume supply while boosting. Default true; false permits unlimited boost even with zero charge.                                                                                                                                                                                 |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float cooldown``                                          | Seconds before a new activation after boost stops. Default 0.25.                                                                                                                                                                                                                  |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CooldownRemaining { get; protected set; }`` | Seconds until a new activation may begin.                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Engine engine``                                           | Registered engine receiving the boost; leave unassigned to resolve it from the owning vehicle.                                                                                                                                                                                    |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                    | 250, so supply and boost resolve before Engine output.                                                                                                                                                                                                                            |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool forceForwardDirection``                              | Request forward drive during boost; disable to retain the selected direction. Default true.                                                                                                                                                                                       |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float fullTankDuration``                                  | Seconds of full boost supplied by a full tank. Default 15; consumption is capacity / duration per second.                                                                                                                                                                         |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HasOutput { get; private set; }``            | Current propulsion-output session, including retained output during internal shifts. Read on subscription to initialize presentation.                                                                                                                                             |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsBoosting { get; }``                        | Whether an enabled Nitro component currently contributes boost.                                                                                                                                                                                                                   |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchForwardGrip``                                 | Departure longitudinal grip fraction; default 0.35.                                                                                                                                                                                                                               |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchGripDuration``                                | Smooth recovery duration in seconds; default 0.65.                                                                                                                                                                                                                                |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchSidewaysGrip``                                | Departure lateral grip fraction; default 0.65.                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchSpeed``                                       | Departure threshold in m/s; default 1.                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool launchWheelspin``                                    | Enable one departure grip pulse per nitro activation; default true.                                                                                                                                                                                                               |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool lockAutomaticGearChanges``                           | Default true. Suppresses automatic gear selection while boost is actually active, including an internal shift interruption. Explicit manual gear requests still use normal safety guards. Disabling this restores the usual automatic shift behavior.                             |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumActivationAmount``                           | Minimum charge needed to begin a new activation. Default 1; an active use may consume its remaining partial charge.                                                                                                                                                               |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumThrottle``                                   | Minimum requested throttle magnitude required for boost. Default 0.1; nonzero propulsion demand is always required.                                                                                                                                                               |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float NormalizedAmount { get; }``                 | Remaining / capacity, from zero to one.                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float OutputStrength { get; }``                   | Current boost presentation strength, including retained RPM assistance during internal shifts.                                                                                                                                                                                    |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                  | Power phase, before Engine.                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float refillDelay``                                       | Seconds since last boost before automatic refill; a held request also blocks refill. Default 1.                                                                                                                                                                                   |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float refillPerSecond``                                   | Automatic refill rate in charge units per second. Default 25.                                                                                                                                                                                                                     |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Remaining { get; }``                        | Charge clamped to the configured capacity.                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Requested { get; }``                         | Explicit component API/Inspector request; Command.Nitro independently contributes to the held request.                                                                                                                                                                            |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool requireGroundContact``                               | Require at least one supported driven tire. Default false.                                                                                                                                                                                                                        |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float shiftSpeedMultiplier``                              | Gear-change and automatic gear dwell speed multiplier during boost. Default 4; preserves authored gearbox settings.                                                                                                                                                               |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Strength { get; protected set; }``          | Resolved boost fraction for this tick; the final partial charge may supply less than one.                                                                                                                                                                                         |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsDirectControl { get; }``            | True so direct-pose mode can clear the active boost state without consuming supply or producing forces.                                                                                                                                                                           |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public BoostSuspensionSettings suspensionKick``                  | Configurable supported spring displacement, enabled by default.                                                                                                                                                                                                                   |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float topSpeedMultiplier``                                | Multiplier for the engine road-speed envelope. Default 1.35.                                                                                                                                                                                                                      |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float torqueMultiplier``                                  | Engine combustion/direct-drive torque multiplier. Default 3.                                                                                                                                                                                                                      |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-11:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                                           | Arguments and result         |
+============================================================================================+=============================================================================================================================================================+==============================+
| ``public virtual float AddNitro(float value)``                                             | Adds a positive finite amount, clamps at capacity, and returns the charge actually accepted.                                                                | See signature for arguments. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Resolves an unassigned engine and clamps the starting charge; does not refill automatically.                                                                | See signature for arguments. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ``public virtual void Refill()``                                                           | Fills the current capacity through SetAmount.                                                                                                               | See signature for arguments. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ``public virtual void ResetState(bool refill = false)``                                    | Clears API request, boost, cooldown and refill timer. Supply is retained unless refill is true.                                                             | See signature for arguments. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ``public virtual void ResetVehicleState(VehicleResetReason reason)``                       | Clears transient state for the supplied reset reason without changing persistent configuration.                                                             | —                            |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ``public virtual void SetAmount(float value)``                                             | Sets charge clamped to [0, capacity], notifying amount/depletion transitions. Non-finite values are ignored.                                                | See signature for arguments. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ``public virtual void SetBoost(bool held)``                                                | Sets the explicit held boost request; pass false on release. Engine throttle and eligibility checks still apply.                                            | See signature for arguments. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Resolve boost eligibility and supply, increase engine output and apply configured extra grounded acceleration. Shifts suspend boost without a new cooldown. | See signature for arguments. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+

.. _uvs-api-drivedynamics--parkinghold:

ParkingHold
-----------

**Runtime/Drive/Brakes/ParkingHold.cs**

Configuration/implementation type for parking hold within engine and drivetrain.

**Inherits / implements:** :ref:`DriveModule <uvs-api-driveprofiles--drivemodule>`.

.. _uvs-api-drivedynamics--state-and-configuration-18:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                                                              |
+===================================================+======================================================================================================================================================+
| ``public bool assistParkingBrake``                | Counter gravity-driven slope creep while the handbrake or detached-trailer parking brake is active; native tires handle braking and external pushes. |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool assistServiceBrake``                | Counter gravity-driven slope creep while the service brake is active; no added planar braking resistance on level ground.                            |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float captureSpeed``                     | Maximum vehicle speed in m/s at which the stationary parking/service hold can capture the body. Initial value: ``.5f``.                              |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                                                                                        |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                                                        |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-12:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                    | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+======================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Resolves the local Trailer used by detached-parking policy.                                                          | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Adds bounded low-speed support while applicable parking/service braking is active; does nothing for a sleeping body. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                 | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--steering:

Steering
--------

**Runtime/Drive/Steering/Steering.cs**

Configuration/implementation type for steering within engine and drivetrain.

**Inherits / implements:** :ref:`DriveModule <uvs-api-driveprofiles--drivemodule>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-8:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                         |
+====================================================+=================================================================================================+
| ``public event System.Action<float> AngleChanged`` | When resolved road-wheel steering angle changes. Payload: angle in degrees, not column degrees. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-19:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                                                                                                                                      |
+====================================================================+==============================================================================================================================================================================================================+
| ``public float ackermann``                                         | Blend toward Ackermann inner/outer wheel steering geometry; zero uses parallel steering. Initial value: ``1``.                                                                                               |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool advancedSteeringGeometry``                           | Optional radius/grip limits and Ackermann geometry. Off uses the configured steering angle directly.                                                                                                         |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Angle { get; }``                            | Read-only/resolved angle for Steering.                                                                                                                                                                       |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool arcadeHandling``                                     | Game-oriented yaw and lateral grip assistance while tires touch the ground.                                                                                                                                  |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float arcadeLateralAcceleration``                         | Force/torque budget for arcade lateral acceleration; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: ``35``. |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float assistanceStrength``                                | Overall strength of the optional yaw/lateral steering assistance. Initial value: ``.72f``.                                                                                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentAngleLimit { get; protected set; }`` | Read-only/resolved current angle limit for Steering.                                                                                                                                                         |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                    | Default local priority within phase/category.                                                                                                                                                                |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float highSpeedAngleRatio``                               | Multiplier/fraction controlling high speed angle ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: ``0.3f``.                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lateralResponse``                                   | Strength of sideways-motion correction relative to the vehicle. Initial value: ``4``.                                                                                                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLateralAcceleration``                        | Steering authority at speed is limited to this requested lateral acceleration (m/s²).                                                                                                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumYawRate``                                    | Upper requested yaw rate used by turning assistance, in rad/s.                                                                                                                                               |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumTurnRadius``                                 | Minimum rear-axle centre turning radius in metres; zero disables the low-speed radius cap.                                                                                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                  | Cross-category execution barrier used by the module pipeline.                                                                                                                                                |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool speedSensitiveSteering``                             | Optional reduction of steering angle with speed. Off preserves full steering authority.                                                                                                                      |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool stabilizePoweredSlides``                             | Keep a powered full-lock slide near its entry speed instead of accelerating into an expanding circle.                                                                                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool StabilizingPoweredSlide { get; }``           | Read-only/resolved stabilizing powered slide for Steering.                                                                                                                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useGroundGripLimit``                                 | When checked, use ground grip limit is active; when unchecked the owning system skips that optional policy. Initial value: ``true``.                                                                         |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Wheelbase { get; protected set; }``         | Measured axle span used by steering geometry, in metres.                                                                                                                                                     |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawResponse``                                       | Strength/speed of the yaw response toward the requested heading/turn behavior. Initial value: ``7.5f``.                                                                                                      |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-13:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                                           | Arguments and result                                                                                                                                            |
+=========================================================================+=============================================================================================================================================+=================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``           | Discovers owned steering tie rods and measures axle/wheel geometry for its steering model.                                                  | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                    |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshWheelBindings(VehicleController vehicle)`` | Rebuilds prepared steering membership, multipliers and tie-rod links while preserving actuator angle; removed steering outputs are cleared. | —                                                                                                                                                               |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Advances steering response/native wheel angles, publishes the resolved actuator and emits ``AngleChanged`` on a change.                     | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                        | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.    |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--tractioncontrol:

TractionControl
---------------

**Runtime/Engine/Drivetrain/TractionControl.cs**

Limits propulsion according to contact capacity and slip.

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-9:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                                                                |
+====================================================+========================================================================================================================================+
| ``public event System.Action<bool> ActiveChanged`` | When resolved traction-control intervention changes between active/inactive. Payload: bool; enabled configuration is a separate state. |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-20:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                              | Meaning                                                                                                                                                 |
+=====================================================================+=========================================================================================================================================================+
| ``public virtual bool Active { get; }``                             | Read-only/resolved active for ``TractionControl``.                                                                                                      |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float corneringFreedom``                                   | Allow power-dependent wheelspin during tight powered turns, while retaining straight-line launch control.                                               |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                     | Default local priority within phase/category.                                                                                                           |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float launchReferenceSpeed``                               | Low-speed reference in m/s used to stabilize slip/traction calculations during launch. Initial value: ``3``.                                            |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MaximumSlip { get; protected set; }``        | Read-only/resolved maximum slip for ``TractionControl``.                                                                                                |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumTorqueScale``                                 | Multiplier/fraction controlling minimum torque scale. Increasing it increases this contribution relative to the unscaled value. Initial value: ``.2f``. |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MinimumTorqueScale { get; protected set; }`` | Read-only/resolved minimum torque scale for ``TractionControl``.                                                                                        |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                   | Cross-category execution barrier used by the module pipeline.                                                                                           |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float recoveryRate``                                       | Rate at which allowed drive torque recovers after excess slip subsides. Initial value: ``4``.                                                           |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reductionRate``                                      | Rate at which allowed drive torque decreases when wheel slip exceeds the target. Initial value: ``8``.                                                  |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reserveGripForCornering``                             | When checked, reserve grip for cornering is active; when unchecked the owning system skips that optional policy.                                        |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float targetSlip``                                         | Desired longitudinal slip magnitude while applying propulsion torque. Initial value: ``.24f``.                                                          |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tractionReserve``                                    | Fraction of estimated traction kept available when limiting drive torque. Initial value: ``.98f``.                                                      |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-14:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                               | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Resets retained intervention feedback before later propulsion steps.                                            | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTractionControlEnabled(bool value)``                              | Enables/disables this traction-control module through its module action.                                        | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Limits wheel propulsion from contact/slip evidence and emits ``ActiveChanged`` when intervention state changes. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                            | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--transmission:

Transmission
------------

**Runtime/Engine/Gearbox/Transmission.cs**

Selects Direct, Manual or Automatic transmission operation.

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`.

.. _uvs-api-drivedynamics--events-and-inspector-callbacks-10:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+--------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                        |
+==============================================================+================================================================================+
| ``public event System.Action<TransmissionMode> ModeChanged`` | After the declaring component's selected mode changes. Payload: its mode enum. |
+--------------------------------------------------------------+--------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--state-and-configuration-21:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                                                                                             |
+===================================================+=====================================================================================================================================================================================+
| ``public AutomaticGearbox automatic``             | Assign the automatic AutomaticGearbox component/asset used by Transmission.                                                                                                         |
+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Engine engine``                          | Assign the engine Engine component/asset used by Transmission.                                                                                                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                                                                                                                       |
+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public ManualGearbox manual``                   | Assign the manual ManualGearbox component/asset used by Transmission.                                                                                                               |
+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public TransmissionMode mode``                  | Selects the operating policy; see the listed options and the owning component guide. Options: ``Automatic``, ``Manual``, ``Direct``. Initial value: ``TransmissionMode.Automatic``. |
+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                                                                                       |
+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--methods-15:

Methods
~~~~~~~

+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                     | Arguments and result                                                                                                                                            |
+=========================================================================+=======================================================================================================================+=================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``           | Resolves missing engine/manual/automatic references and applies the selected transmission mode.                       | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                    |
+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMode(TransmissionMode value)``                 | Changes transmission or camera mode through the declaring component's transition rules.                               | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                    |
+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Consumes a transmission toggle or changed mode field and applies the selected Direct/Manual/Automatic implementation. | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-drivedynamics--transmissionmode:

TransmissionMode
----------------

**Runtime/Engine/Gearbox/Transmission.cs**

Defines the allowed transmission mode choices used by this topic.

.. _uvs-api-drivedynamics--values-1:

Values
~~~~~~

-  ``Automatic``
-  ``Manual``
-  ``Direct``
