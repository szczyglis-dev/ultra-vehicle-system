.. _uvs-api-interior--cockpit-instruments-and-bindings-api:

Cockpit instruments and bindings API
====================================

Read :doc:`the system explanation </Scripting/Interior>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _uvs-api-interior--types:

Types
-----

-  :ref:`AircraftHud <uvs-api-interior--aircrafthud>`
-  :ref:`AnchoredControlAnimator <uvs-api-interior--anchoredcontrolanimator>`
-  :ref:`AnchoredControlInput <uvs-api-interior--anchoredcontrolinput>`
-  :ref:`AnchoredRotation <uvs-api-interior--anchoredrotation>`
-  :ref:`CarHud <uvs-api-interior--carhud>`
-  :ref:`ClutchSource <uvs-api-interior--clutchsource>`
-  :ref:`CommandValueSource <uvs-api-interior--commandvaluesource>`
-  :ref:`ControlAnimator <uvs-api-interior--controlanimator>`
-  :ref:`EngineRpmSource <uvs-api-interior--enginerpmsource>`
-  :ref:`FuelTank <uvs-api-interior--fueltank>`
-  :ref:`GasSource <uvs-api-interior--gassource>`
-  :ref:`GearLeverAnimator <uvs-api-interior--gearleveranimator>`
-  :ref:`GearLeverMotionMode <uvs-api-interior--gearlevermotionmode>`
-  :ref:`GearLeverPosition <uvs-api-interior--gearleverposition>`
-  :ref:`GearPaddleAnimator <uvs-api-interior--gearpaddleanimator>`
-  :ref:`GearShiftAnimator <uvs-api-interior--gearshiftanimator>`
-  :ref:`GearShiftDirection <uvs-api-interior--gearshiftdirection>`
-  :ref:`HandbrakeSource <uvs-api-interior--handbrakesource>`
-  :ref:`HandleCommandInput <uvs-api-interior--handlecommandinput>`
-  :ref:`HandleMotion <uvs-api-interior--handlemotion>`
-  :ref:`IGearShiftAnimator <uvs-api-interior--igearshiftanimator>`
-  :ref:`IInteriorValueSource <uvs-api-interior--iinteriorvaluesource>`
-  :ref:`IndicatorSwitchBinding <uvs-api-interior--indicatorswitchbinding>`
-  :ref:`InstrumentNeedle <uvs-api-interior--instrumentneedle>`
-  :ref:`InteriorCore <uvs-api-interior--interiorcore>`
-  :ref:`InteriorDataSourceAttribute <uvs-api-interior--interiordatasourceattribute>`
-  :ref:`InteriorModule <uvs-api-interior--interiormodule>`
-  :ref:`InteriorValueSource <uvs-api-interior--interiorvaluesource>`
-  :ref:`ISteeringIntentSource <uvs-api-interior--isteeringintentsource>`
-  :ref:`PedalAnimator <uvs-api-interior--pedalanimator>`
-  :ref:`PitchSource <uvs-api-interior--pitchsource>`
-  :ref:`ProfileSwitchBinding <uvs-api-interior--profileswitchbinding>`
-  :ref:`RearMirror <uvs-api-interior--rearmirror>`
-  :ref:`RearMirrors <uvs-api-interior--rearmirrors>`
-  :ref:`RollSource <uvs-api-interior--rollsource>`
-  :ref:`RotaryAnimator <uvs-api-interior--rotaryanimator>`
-  :ref:`ServiceBrakeSource <uvs-api-interior--servicebrakesource>`
-  :ref:`SpeedValueSource <uvs-api-interior--speedvaluesource>`
-  :ref:`SteeringSource <uvs-api-interior--steeringsource>`
-  :ref:`SteeringStickAnimator <uvs-api-interior--steeringstickanimator>`
-  :ref:`SteeringWheelAnimator <uvs-api-interior--steeringwheelanimator>`
-  :ref:`SwitchAnimator <uvs-api-interior--switchanimator>`
-  :ref:`SwitchPosition <uvs-api-interior--switchposition>`
-  :ref:`ThrottleAnimator <uvs-api-interior--throttleanimator>`
-  :ref:`TwistThrottleAnimator <uvs-api-interior--twistthrottleanimator>`
-  :ref:`VehicleHandleAnimator <uvs-api-interior--vehiclehandleanimator>`
-  :ref:`VehicleValueSource <uvs-api-interior--vehiclevaluesource>`
-  :ref:`YokeAnimator <uvs-api-interior--yokeanimator>`

.. _uvs-api-interior--aircrafthud:

AircraftHud
-----------

**Runtime/Interior/Render/AircraftHud.cs**

Configuration/implementation type for aircraft hud within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorModule <uvs-api-interior--interiormodule>`.

.. _uvs-api-interior--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------+
| Member                                     | Meaning                                                                 |
+============================================+=========================================================================+
| ``public event Action<Telemetry> Changed`` | After the HUD receives an updated reading. Payload: Telemetry snapshot. |
+--------------------------------------------+-------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                                                                                      |
+====================================================================+==============================================================================================================================================================+
| ``public Renderer cockpitSurface``                                 | Assign the cockpit surface reference used by AircraftHud. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Texture customTexture``                                   | Assign the custom texture reference used by AircraftHud. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Texture DisplayTexture { get; }``                 | Read-only/resolved display texture for ``AircraftHud``.                                                                                                      |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual LandingGear LandingGear { get; protected set; }`` | Read-only/resolved landing gear for ``AircraftHud``.                                                                                                         |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float refreshRate``                                       | Maximum update/render frequency in frames per second; lower values reduce rendering work. Initial value: ``15``.                                             |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Telemetry Telemetry { get; protected set; }``     | Latest cached vehicle snapshot published after the module pipeline.                                                                                          |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string textureProperty``                                  | Shader texture property receiving the generated or assigned render texture. Initial value: ``"_BaseMap"``.                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle``                               | Assign the vehicle VehicleController component/asset used by AircraftHud.                                                                                    |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods:

Methods
~~~~~~~

+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Signature                                                   | Role and behavior                                                                         | Arguments and result                                                                       |
+=============================================================+===========================================================================================+============================================================================================+
| ``public virtual void Bind(VehicleController owner)``       | Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription. | ``owner`` — Unity/application owner whose identity controls this relationship or resource. |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController owner)`` | Binds the HUD to this vehicle's telemetry source.                                         | ``owner`` — Unity/application owner whose identity controls this relationship or resource. |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. _uvs-api-interior--anchoredcontrolanimator:

AnchoredControlAnimator
-----------------------

**Runtime/Interior/Animators/AnchoredControlAnimator.cs**

Concrete animator for service-brake, clutch and handbrake levers. Select the mechanic with Input; each lever retains its own component instance. The stationary anchor must be outside the moving-part hierarchy; its captured authored pose is retained across enable/disable.

**Inherits / implements:** ``ControlAnimator``.

.. _uvs-api-interior--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                                             |
+=============================================+=====================================================================================================================================================================+
| ``public UnityEvent<float> onValueChanged`` | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. |
+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                | Meaning                                                                                                                                                                                                                                                                                 |
+=======================================================+=========================================================================================================================================================================================================================================================================================+
| ``public MonoBehaviour dataSource``                   | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AnchoredControlInput input``                 | Hidden fallback channel when Data Source is empty: ServiceBrake (default), Clutch or Handbrake. An assigned source overrides this field.                                                                                                                                                |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Vector3 InteractionValue { get; }`` | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                                                                                                                                                                    |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AnchoredRotation motion``                    | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                                                                                                                  |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``     | Runs in the presentation phase, independently of vehicle mechanics.                                                                                                                                                                                                                     |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pressDuration``                        | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                                                                                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pressedAngle``                         | Lever angle in degrees at displayed value one.                                                                                                                                                                                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float releasedAngle``                        | Lever angle in degrees at displayed value zero.                                                                                                                                                                                                                                         |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float releaseDuration``                      | Seconds to fade after releasing the request; zero stops immediately.                                                                                                                                                                                                                    |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Value { get; private set; }``          | Current normalized displayed position.                                                                                                                                                                                                                                                  |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                  | Role and behavior                                                                                                               | Arguments and result |
+============================================================================================+=================================================================================================================================+======================+
| ``public void ResetMotion()``                                                              | Restores value zero and the released angle. Disabling also releases.                                                            | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public void SetValue(float value)``                                                      | Applies a finite normalized preview/API value, clamped to 0..1; does not command a mechanic.                                    | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle. | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--anchoredcontrolinput:

AnchoredControlInput
--------------------

**Runtime/Interior/Animators/AnchoredControlAnimator.cs**

Selects the mechanic presented by an AnchoredControlAnimator instance:

-  ``ServiceBrake`` — Resolved vehicle service braking, with Command.ServiceBrake fallback when no vehicle is supplied.
-  ``Clutch`` — Command.Clutch.
-  ``Handbrake`` — Command.Handbrake as zero or one.

.. _uvs-api-interior--anchoredrotation:

AnchoredRotation
----------------

**Runtime/Interior/Controls/AnchoredRotation.cs**

Preserves a neutral pose relative to an independent pivot frame.

.. _uvs-api-interior--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                   | Meaning                                                                                                                                                       |
+==========================================+===============================================================================================================================================================+
| ``public Transform anchor``              | Assign the anchor reference used by AnchoredRotation. Leave unassigned only when this feature is optional or the component can resolve it automatically.      |
+------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 Axis { get; }``         | Read-only/resolved axis for ``AnchoredRotation``.                                                                                                             |
+------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsValid { get; }`` | Current is valid predicate; read it instead of maintaining a second application flag.                                                                         |
+------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``             | Local axis around which the configured motion or operation takes place. Initial value: ``Vector3.right``.                                                     |
+------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform movingPart``          | Assign the moving part reference used by AnchoredRotation. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-2:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                           | Role and behavior                                                                         | Arguments and result                                                                                                                                                                                                                                                                                                               |
+=====================================================================================================+===========================================================================================+====================================================================================================================================================================================================================================================================================================================================+
| ``public virtual void CaptureRestPose()``                                                           | Captures the currently authored rest pose for this geometry mapper or blade.              | No arguments; no returned value.                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 GetPointAtAngle(Vector3 meshLocalPoint, float degrees)``                   | Returns the neutral-frame point after applying a specified rotation angle.                | ``meshLocalPoint`` — Impact point in the deformed mesh's local coordinates. ``degrees`` — Requested angle in degrees. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation.                                                                                                              |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAngle(float degrees)``                                                     | Immediately applies a moving-part/geometry rotation in degrees.                           | ``degrees`` — Requested angle in degrees.                                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetPose(float degrees, out Vector3 position, out Quaternion orientation)`` | Computes a pose from the captured anchored rest frame when geometry references are valid. | ``degrees`` — Requested angle in degrees. ``position`` — Requested point or switch detent; see its declared type and owning operation. ``orientation`` — Orientation, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------+---------------------------------------------------------------------------------+
| Declaration             | Usage                                                                           |
+=========================+=================================================================================+
| ``public bool reverse`` | Invert this control’s visual motion without changing the logical command value. |
+-------------------------+---------------------------------------------------------------------------------+

.. _uvs-api-interior--carhud:

CarHud
------

**Runtime/Interior/Render/CarHud.cs**

Configuration/implementation type for car hud within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorModule <uvs-api-interior--interiormodule>`.

.. _uvs-api-interior--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------+
| Member                                     | Meaning                                                                 |
+============================================+=========================================================================+
| ``public event Action<Telemetry> Changed`` | After the HUD receives an updated reading. Payload: Telemetry snapshot. |
+--------------------------------------------+-------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                         | Meaning                                                                                                                                                 |
+================================================================+=========================================================================================================================================================+
| ``public virtual DrivingAssists Assists { get; }``             | Read-only/resolved assists for ``CarHud``.                                                                                                              |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Renderer cockpitSurface``                             | Assign the cockpit surface reference used by CarHud. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Texture customTexture``                               | Assign the custom texture reference used by CarHud. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Texture DisplayTexture { get; }``             | Read-only/resolved display texture for ``CarHud``.                                                                                                      |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual FuelTank FuelTank { get; }``                  | Read-only/resolved fuel tank for ``CarHud``.                                                                                                            |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Lights Lights { get; }``                      | Read-only/resolved lights for ``CarHud``.                                                                                                               |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float refreshRate``                                   | Maximum update/render frequency in frames per second; lower values reduce rendering work. Initial value: ``10``.                                        |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public SpeedUnit speedUnit``                                 | Output unit; defaults to Kph. Changing this does not alter vehicle physics. For a signed SpeedValueSource, reverse motion remains negative.             |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Telemetry Telemetry { get; protected set; }`` | Latest cached vehicle snapshot published after the module pipeline.                                                                                     |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string textureProperty``                              | Shader texture property receiving the generated or assigned render texture. Initial value: ``"_BaseMap"``.                                              |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle``                           | Assign the vehicle VehicleController component/asset used by CarHud.                                                                                    |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-3:

Methods
~~~~~~~

+----------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Signature                                                | Role and behavior                                                                         | Arguments and result                                                         |
+==========================================================+===========================================================================================+==============================================================================+
| ``public virtual void Bind(VehicleController selected)`` | Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription. | ``selected`` — Selected, interpreted by this operation in the declared type. |
+----------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

.. _uvs-api-interior--clutchsource:

ClutchSource
------------

**Runtime/Interior/Controls/Source/ClutchSource.cs**

Samples Command.Clutch (0..1).

**Inherits / implements:** ``VehicleValueSource``.

.. _uvs-api-interior--methods-4:

Methods
~~~~~~~

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                             | Role and behavior                                                                                                                                                   | Arguments and result |
+=======================================+=====================================================================================================================================================================+======================+
| ``public override float ReadValue()`` | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units. | —                    |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--commandvaluesource:

CommandValueSource
------------------

**Runtime/Interior/Controls/Source/CommandValueSource.cs**

Samples a selected Command channel, without resolved actuator mapping.

**Inherits / implements:** ``VehicleValueSource``.

.. _uvs-api-interior--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------+-------------------------------------------------------+
| Member                       | Meaning                                               |
+==============================+=======================================================+
| ``public HandleInput input`` | Command channel to sample through HandleCommandInput. |
+------------------------------+-------------------------------------------------------+

.. _uvs-api-interior--methods-5:

Methods
~~~~~~~

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                             | Role and behavior                                                                                                                                                   | Arguments and result |
+=======================================+=====================================================================================================================================================================+======================+
| ``public override float ReadValue()`` | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units. | —                    |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--controlanimator:

ControlAnimator
---------------

**Runtime/Interior/Animators/ControlAnimator.cs**

Shared control presentation base. It references an optional IK handle, coordinates real limb arrival and owns Wait For Handle / Fake Sync Handle Motion. It does not act as an IK target.

**Inherits / implements:** ``VehicleHandleAnimator``.

.. _uvs-api-interior--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                                                                                                 |
+======================================================+=========================================================================================================================================================================================+
| ``public bool fakeSyncHandleMotion``                 | Default false. Outbound reach uses the contact pose captured before visual motion; after arrival it follows the live anchor.                                                            |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleHandle handle``                      | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion. |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 InteractionValue { get; }`` | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                                                                    |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                           | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics.                                  |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool waitForHandle``                        | Default true. Wait for the real palm/foot within 2.5 cm after transit, plus finger blending for hands. Mechanics remain immediate; steering is excluded.                                |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-6:

Methods
~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                     | Role and behavior                                                                                                | Arguments and result |
+===============================================================+==================================================================================================================+======================+
| ``public override void Configure(VehicleController vehicle)`` | Finds a paired ControlHandle on this object when Handle is empty, then links that contact back to this animator. | —                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--enginerpmsource:

EngineRpmSource
---------------

**Runtime/Interior/Controls/Source/EngineRpmSource.cs**

Configuration/implementation type for engine rpm source within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorValueSource <uvs-api-interior--interiorvaluesource>`.

.. _uvs-api-interior--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+-------------------------------------------------------------------+
| Member                   | Meaning                                                           |
+==========================+===================================================================+
| ``public Engine engine`` | Assign the engine Engine component/asset used by EngineRpmSource. |
+--------------------------+-------------------------------------------------------------------+

.. _uvs-api-interior--methods-7:

Methods
~~~~~~~

+---------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature                             | Role and behavior                                                                          | Arguments and result                                                   |
+=======================================+============================================================================================+========================================================================+
| ``public override float ReadValue()`` | Reads a scalar control or instrument source in its documented normalized or physical unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+---------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _uvs-api-interior--fueltank:

FuelTank
--------

**Runtime/Engine/FuelTank.cs**

Quantity change, empty transition and actual fuel increase

**Inherits / implements:** :ref:`EngineModule <uvs-api-drivedynamics--enginemodule>`.

.. _uvs-api-interior--events-and-inspector-callbacks-3:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| Member                                     | Meaning                                                                                         |
+============================================+=================================================================================================+
| ``public event Action Emptied``            | On the transition to empty fuel. No payload.                                                    |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public event Action<float> FuelChanged`` | After actual fuel quantity changes. Payload: current litres, not the requested transfer amount. |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public event Action Refuelled``          | After an actual increase in fuel, including ``SetFuel``. No payload; query quantity if needed.  |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Member                                                         | Meaning                                                                                                                        |
+================================================================+================================================================================================================================+
| ``public virtual bool BlocksIgnition { get; }``                | Whether an active/enabled tank with ``stopEngineWhenEmpty`` currently blocks engine start.                                     |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float capacityLitres``                                | Maximum fuel capacity in litres. Initial value: ``60``.                                                                        |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool consumeFuel``                                    | Consume fuel while the engine is running. Disable for an unlimited driving range while retaining the gauge and refuelling API. |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                | Default local priority within phase/category.                                                                                  |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Fraction { get; }``                     | Fuel quantity divided by capacity, suitable for a 0–1 instrument source.                                                       |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float FuelLitres { get; }``                   | Read-only/resolved fuel litres for ``FuelTank``.                                                                               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float fullLoadLitresPerHour``                         | Fuel consumption rate at full engine load, in litres per hour. Initial value: ``35``.                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HasFuel { get; }``                       | Whether the tank currently contains usable fuel.                                                                               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float idleLitresPerHour``                             | Fuel consumption rate at engine idle, in litres per hour. Initial value: ``.8f``.                                              |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float LitresPerHour { get; protected set; }`` | Read-only/resolved litres per hour for ``FuelTank``.                                                                           |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``              | Cross-category execution barrier used by the module pipeline.                                                                  |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool stopEngineWhenEmpty``                            | Stop the engine and block ignition when the tank is empty.                                                                     |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsDirectControl { get; }``        | Opts into direct-mode stepping; retains fuel/ignition policy without determining chassis motion.                               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-8:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                          | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+============================================================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual float Drain(float litres)``                                               | Removes a finite nonnegative requested number of litres, bounded by available fuel, and returns the actual litres removed. | ``litres`` — Requested fuel transfer in litres; actual transfer can be smaller. **Returns:** Actual transferred litres.                                                                                                  |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Fill()``                                                             | Sets quantity to capacity through ``SetFuel``, with normal actual-change notifications.                                    | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Refuel(float litres)``                                              | Adds up to the requested litres, limited by capacity, and returns actual transfer.                                         | ``litres`` — Requested fuel transfer in litres; actual transfer can be smaller. **Returns:** Actual transferred litres.                                                                                                  |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFuel(float litres)``                                              | Sets fuel quantity within capacity and publishes actual quantity/empty/refuel transitions.                                 | ``litres`` — Requested fuel transfer in litres; actual transfer can be smaller.                                                                                                                                          |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Stops an empty constrained engine, otherwise consumes running idle/load fuel and publishes actual quantity transitions.    | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--gassource:

GasSource
---------

**Runtime/Interior/Controls/Source/GasSource.cs**

Samples DriveDemand or raw throttle demand. Optional magnitude supports reverse propulsion and motorcycle twist grips.

**Inherits / implements:** ``VehicleValueSource``.

.. _uvs-api-interior--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+------------------------------------------------------------------------------------------------+
| Member                            | Meaning                                                                                        |
+===================================+================================================================================================+
| ``public bool absoluteValue``     | Return the magnitude, including reverse propulsion; disable to retain the signed source value. |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ``public bool useResolvedDemand`` | Read resolved signed DriveDemand when true; otherwise Command.Throttle.                        |
+-----------------------------------+------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-9:

Methods
~~~~~~~

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                             | Role and behavior                                                                                                                                                   | Arguments and result |
+=======================================+=====================================================================================================================================================================+======================+
| ``public override float ReadValue()`` | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units. | —                    |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--gearleveranimator:

GearLeverAnimator
-----------------

**Runtime/Interior/Animators/GearLeverAnimator.cs**

Follows accepted gearbox selections and coordinates a timed hand reach before moving the lever. The moving-part origin must coincide with the stationary floor anchor in its neutral pose. Preview never changes the gearbox.

**Inherits / implements:** ``ControlAnimator``.

.. _uvs-api-interior--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                | Meaning                                                                                                                                                                  |
+=======================================================+==========================================================================================================================================================================+
| ``public Transform anchor``                           | Contact transform used for IK. Parent it to the moving grip; it is separate from the animator hinge/pivot anchor.                                                        |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int DisplayedGear { get; private set; }``    | Last fully reached gear.                                                                                                                                                 |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float downshiftDelay``                       | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Engine engine``                              | Assign the engine Engine component/asset used by Propulsion.                                                                                                             |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Gearbox gearbox``                            | Assign the gearbox Gearbox component/asset used by CommercialAudio.                                                                                                      |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool HasValidRig { get; }``                  | Requires distinct anchor/moving part, with anchor outside the moving hierarchy.                                                                                          |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Vector3 InteractionValue { get; }`` | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                                                     |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsMoving { get; private set; }``        | Whether pose interpolation is active; excludes waiting for a hand.                                                                                                       |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public GearLeverMotionMode mode``                   | Rotation or Translation.                                                                                                                                                 |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform movingPart``                       | ``Transform`` whose pose this mapper owns; keep imported-mesh offsets on its child.                                                                                      |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``     | Runs in the presentation phase, independently of vehicle mechanics.                                                                                                      |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public GearLeverPosition[] positions``              | Unique signed gear numbers and their absolute poses. Defaults include R, N and gears 1–6.                                                                                |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float shiftDuration``                        | Visual lever travel duration in seconds; independent of gearbox torque transfer. Initial value: ``.18f``.                                                                |
+-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-10:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                  | Role and behavior                                                                                                               | Arguments and result |
+============================================================================================+=================================================================================================================================+======================+
| ``public bool AnimateGear(int gear)``                                                      | Queues the latest accepted visual target without changing the gearbox. Returns false on invalid rig/pose.                       | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy.                 | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public void RefreshBinding()``                                                           | Unsubscribes the old gearbox, releases any hand and silently synchronizes the new source.                                       | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public bool SetImmediate(int gear)``                                                     | Silently applies a configured pose and releases active ownership. Returns false on invalid rig/pose.                            | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle. | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public void Tick(float deltaTime)``                                                      | Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.                             | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public bool TryGetPosition(int gear, out GearLeverPosition position)``                   | Returns a unique finite pose; rejects duplicates, missing gears and values below -1.                                            | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--gearlevermotionmode:

GearLeverMotionMode
-------------------

**Runtime/Interior/Animators/GearLeverAnimator.cs**

-  ``Rotation``: Euler rotation around the floor anchor.
-  ``Translation``: position offset in anchor axes, with anchor orientation.

.. _uvs-api-interior--gearleverposition:

GearLeverPosition
-----------------

**Runtime/Interior/Animators/GearLeverAnimator.cs**

.. _uvs-api-interior--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+--------------------------------------------------------------------------+
| Member                      | Meaning                                                                  |
+=============================+==========================================================================+
| ``public int gear``         | Unique signed gear number: -1 reverse, 0 neutral, positive forward gear. |
+-----------------------------+--------------------------------------------------------------------------+
| ``public Vector3 position`` | Absolute local offset in the anchor frame, used in Translation mode.     |
+-----------------------------+--------------------------------------------------------------------------+
| ``public Vector3 rotation`` | Absolute Euler angles in the anchor frame, used in Rotation mode.        |
+-----------------------------+--------------------------------------------------------------------------+

.. _uvs-api-interior--gearpaddleanimator:

GearPaddleAnimator
------------------

**Runtime/Interior/Animators/GearPaddleAnimator.cs**

Receives accepted gear changes through IGearShiftAnimator, coalesces downshifts, then reaches, presses and releases the paddle. Link a GearPaddleHandle for the intended hand.

**Inherits / implements:** ``ControlAnimator``, ``IGearShiftAnimator``.

.. _uvs-api-interior--events-and-inspector-callbacks-4:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                          | Meaning                                                                                                                                              |
+=================================+======================================================================================================================================================+
| ``public UnityEvent onPressed`` | Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction. |
+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                   | Meaning                                                                                                                                                                  |
+==========================================================+==========================================================================================================================================================================+
| ``public GearShiftDirection direction``                  | Selects the direction policy for this configuration. Options: ``Both``, ``Up``, ``Down``.                                                                                |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float downshiftDelay``                          | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Vector3 InteractionValue { get; }``    | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                                                     |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsMoving { get; protected set; }`` | Whether paddle press/return motion is active; excludes waiting for a hand.                                                                                               |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AnchoredRotation motion``                       | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                   |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pressDuration``                           | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                                |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pressedAngle``                            | Pedal angle in degrees at displayed value one.                                                                                                                           |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float returnDuration``                          | Return travel duration in seconds, independent of outbound travel.                                                                                                       |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }``   | Current displayed pedal travel in 0–1; it can lag ``TargetValue`` while motion is smoothed.                                                                              |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-11:

Methods
~~~~~~~

+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                            | Role and behavior                                                                                   | Arguments and result |
+======================================================================+=====================================================================================================+======================+
| ``public virtual void AnimateShift(int previousGear, int nextGear)`` | Requests a presentation gesture for an accepted change from the previous gear to the next gear.     | —                    |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Press()``                                      | Requests a paddle presentation press in the selected shift direction.                               | —                    |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void ResetMotion()``                                | Clears presentation requests and restores the released/default motion state.                        | —                    |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Tick(float deltaTime)``                        | Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration. | —                    |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--gearshiftanimator:

GearShiftAnimator
-----------------

**Runtime/Interior/Animators/GearShiftAnimator.cs**

Synchronizes shift presentation with accepted mechanical gear changes.

**Inherits / implements:** :ref:`VehicleHandleAnimator <uvs-api-interior--vehiclehandleanimator>`.

.. _uvs-api-interior--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                            |
+===================================================+====================================================================================================================+
| ``public MonoBehaviour[] animators``              | Visual gear controls implementing IGearShiftAnimator. Assign the paddle animators; do not assign their IK handles. |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public Engine engine``                          | Assign the engine Engine component/asset used by Propulsion.                                                       |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public Gearbox gearbox``                        | Assign the gearbox Gearbox component/asset used by CommercialAudio.                                                |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Runs in the presentation phase, independently of vehicle mechanics.                                                |
+---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-12:

Methods
~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                     | Role and behavior                                                                                               | Arguments and result |
+===============================================================+=================================================================================================================+======================+
| ``public virtual void Bind(Engine source)``                   | Connects a gearbox to an ``IGearShiftAnimator`` and refreshes the accepted-shift subscription.                  | —                    |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Configure(VehicleController vehicle)`` | Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy. | —                    |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void RefreshBinding()``                      | Re-resolves the current gearbox/shift-handle binding and its subscription.                                      | —                    |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--gearshiftdirection:

GearShiftDirection
------------------

**Runtime/Interior/Animators/GearPaddleAnimator.cs**

Defines the allowed gear shift direction choices used by this topic.

-  ``Both``
-  ``Up``
-  ``Down``

.. _uvs-api-interior--handbrakesource:

HandbrakeSource
---------------

**Runtime/Interior/Controls/Source/HandbrakeSource.cs**

Samples Command.Handbrake as 0 or 1.

**Inherits / implements:** ``VehicleValueSource``.

.. _uvs-api-interior--methods-13:

Methods
~~~~~~~

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                             | Role and behavior                                                                                                                                                   | Arguments and result |
+=======================================+=====================================================================================================================================================================+======================+
| ``public override float ReadValue()`` | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units. | —                    |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--handlecommandinput:

HandleCommandInput
------------------

**Runtime/Interior/Controls/HandleCommandInput.cs**

Configuration/implementation type for handle command input within cockpit instruments and bindings.

.. _uvs-api-interior--methods-14:

Methods
~~~~~~~

+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                        | Role and behavior                                                                                                                                       | Arguments and result                                                                                                                                                                                                                             |
+==================================================================+=========================================================================================================================================================+==================================================================================================================================================================================================================================================+
| ``public static float Read(Command command, HandleInput input)`` | Maps one ``HandleInput`` choice to the corresponding Command channel for cockpit presentation. Handbrake returns one while held and zero when released. | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``input`` — Command handle channel or normalized rate, according to the signature. **Returns:** Computed float in the operation's documented unit/domain. |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--handlemotion:

HandleMotion
------------

**Runtime/Interior/Animators/HandleMotion.cs**

Reusable geometry mapping for animator-owned rotation or translation in an independent anchor frame. It is not an IK contact.

.. _uvs-api-interior--state-and-configuration-13:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Member                                    | Meaning                                                                                                           |
+===========================================+===================================================================================================================+
| ``public Transform anchor``               | Contact transform used for IK. Parent it to the moving grip; it is separate from the animator hinge/pivot anchor. |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``              | Local axis around which the configured motion or operation takes place. Initial value: ``Vector3.forward``.       |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public float maximum``                  | Offset at normalized value one; values may be signed/reversed to match model direction.                           |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public float minimum``                  | Offset at normalized value zero: degrees in rotation mode, local distance in translation mode.                    |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public AircraftControlMotionMode mode`` | Chooses rotation (degrees) or translation (local distance) for minimum/maximum/offset.                            |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform movingPart``           | ``Transform`` whose pose this mapper owns; keep imported-mesh offsets on its child.                               |
+-------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-15:

Methods
~~~~~~~

+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                       | Role and behavior                                                                                                                                                    | Arguments and result |
+=================================================+======================================================================================================================================================================+======================+
| ``public virtual void SetOffset(float offset)`` | Resets ``movingPart`` to the independent anchor and applies rotation in degrees or translation in local units. Invalid/nonfinite/self-descendant frames are ignored. | —                    |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetValue(float value)``   | Clamps a fraction to 0–1, maps it between minimum and maximum, then applies ``SetOffset``. Rotation uses degrees; translation uses local distance.                   | —                    |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

+-------------------------+---------------------------------------------------------------------------------+
| Declaration             | Usage                                                                           |
+=========================+=================================================================================+
| ``public bool reverse`` | Invert this control’s visual motion without changing the logical command value. |
+-------------------------+---------------------------------------------------------------------------------+

.. _uvs-api-interior--igearshiftanimator:

IGearShiftAnimator
------------------

**Runtime/Interior/Animators/IGearShiftAnimator.cs**

Presentation contract for accepted gear changes. Implement it on visual gear controls; IK handles do not consume gearbox events.

.. _uvs-api-interior--methods-16:

Methods
~~~~~~~

+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------+
| Signature                                             | Role and behavior                                                                               | Arguments and result |
+=======================================================+=================================================================================================+======================+
| ``void AnimateShift(int previousGear, int nextGear)`` | Requests a presentation gesture for an accepted change from the previous gear to the next gear. | —                    |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--iinteriorvaluesource:

IInteriorValueSource
--------------------

**Runtime/Interior/Controls/Source/InteriorValueSource.cs**

Configuration/implementation type for iinterior value source within cockpit instruments and bindings.

.. _uvs-api-interior--methods-17:

Methods
~~~~~~~

+-----------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature             | Role and behavior                                                                          | Arguments and result                                                   |
+=======================+============================================================================================+========================================================================+
| ``float ReadValue()`` | Reads a scalar control or instrument source in its documented normalized or physical unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+-----------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _uvs-api-interior--indicatorswitchbinding:

IndicatorSwitchBinding
----------------------

**Runtime/Interior/Controls/IndicatorSwitchBinding.cs**

Configuration/implementation type for indicator switch binding within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-interior--state-and-configuration-14:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                   | Meaning                                                                                                                                                |
+==========================================+========================================================================================================================================================+
| ``public SwitchPosition leftPosition``   | Selects the left position policy for this configuration. Options: ``Negative``, ``Neutral``, ``Positive``. Initial value: ``SwitchPosition.Negative``. |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Lights lights``                 | Assign the lights Lights component/asset used by IndicatorSwitchBinding.                                                                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public SwitchAnimator switchAnimator`` | Assign the switch handle SwitchHandle component/asset used by IndicatorSwitchBinding.                                                                  |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-18:

Methods
~~~~~~~

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Signature                                           | Role and behavior                                                                                                                   | Arguments and result                                                 |
+=====================================================+=====================================================================================================================================+======================================================================+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         | ``immediate`` — Whether to bypass normal presentation travel.        |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. _uvs-api-interior--instrumentneedle:

InstrumentNeedle
----------------

**Runtime/Interior/Controls/InstrumentNeedle.cs**

Specializes value-driven rotation for instruments.

**Inherits / implements:** :ref:`RotaryAnimator <uvs-api-interior--rotaryanimator>`.

.. _uvs-api-interior--interiorcore:

InteriorCore
------------

**Runtime/Interior/Core/InteriorCore.cs**

Configuration/implementation type for interior core within cockpit instruments and bindings.

**Inherits / implements:** :ref:`CategoryCore <uvs-api-modules--categorycore>`.

.. _uvs-api-interior--state-and-configuration-15:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-19:

Methods
~~~~~~~

+---------------------------+--------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                 | Role and behavior                                            | Arguments and result                                               |
+===========================+==============================================================+====================================================================+
| ``public InteriorCore()`` | Constructs ``InteriorCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+---------------------------+--------------------------------------------------------------+--------------------------------------------------------------------+

.. _uvs-api-interior--interiordatasourceattribute:

InteriorDataSourceAttribute
---------------------------

**Runtime/Interior/Controls/Source/InteriorDataSourceAttribute.cs**

Marks an Inspector component field as an IInteriorValueSource consumer. The editor picker accepts application MonoBehaviours implementing the interface.

**Inherits / implements:** ``PropertyAttribute``.

.. _uvs-api-interior--interiormodule:

InteriorModule
--------------

**Runtime/Interior/Core/InteriorModule.cs**

Configuration/implementation type for interior module within cockpit instruments and bindings.

**Inherits / implements:** :ref:`VehicleModule <uvs-api-modules--vehiclemodule>`, :ref:`IInteriorModule <uvs-api-modules--iinteriormodule>`.

.. _uvs-api-interior--state-and-configuration-16:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _uvs-api-interior--interiorvaluesource:

InteriorValueSource
-------------------

**Runtime/Interior/Controls/Source/InteriorValueSource.cs**

Base adapter for an ``IInteriorValueSource`` value producer.

**Inherits / implements:** ``MonoBehaviour``, :ref:`IInteriorValueSource <uvs-api-interior--iinteriorvaluesource>`.

.. _uvs-api-interior--methods-20:

Methods
~~~~~~~

+---------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature                             | Role and behavior                                                                          | Arguments and result                                                   |
+=======================================+============================================================================================+========================================================================+
| ``public abstract float ReadValue()`` | Reads a scalar control or instrument source in its documented normalized or physical unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+---------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _uvs-api-interior--isteeringintentsource:

ISteeringIntentSource
---------------------

**Runtime/Interior/Controls/Source/SteeringSource.cs**

Optional extension for an IInteriorValueSource that separates requested steering from the resolved visual steering value. SteeringHandRegrip uses intent to distinguish an active turn from passive return. Custom scalar-only sources retain their existing ReadValue behavior.

.. _uvs-api-interior--methods-21:

Methods
~~~~~~~

+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                      | Role and behavior                                                                                                                                                           | Arguments and result |
+================================+=============================================================================================================================================================================+======================+
| ``float ReadSteeringIntent()`` | Returns requested normalized steering (-1..1), including zero immediately when control is released. It must not return the actuator's residual angle during self-centering. | —                    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--pedalanimator:

PedalAnimator
-------------

**Runtime/Interior/Animators/PedalAnimator.cs**

Samples an interchangeable IInteriorValueSource (or built-in resolved/command fallback) and animates pedal travel. Its paired PedalHandle owns foot/ankle contact geometry.

**Inherits / implements:** ``ControlAnimator``.

.. _uvs-api-interior--events-and-inspector-callbacks-5:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                                             |
+=============================================+=====================================================================================================================================================================+
| ``public UnityEvent<float> onValueChanged`` | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. |
+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-17:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                                                                                                                                                                                 |
+==============================================================+=========================================================================================================================================================================================================================================================================================+
| ``public bool absoluteInput``                                | Use absolute input for signed propulsion/reverse commands.                                                                                                                                                                                                                              |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour dataSource``                          | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool FollowsInput { get; protected set; }`` | Whether ordinary input mapping owns this control instead of an application override.                                                                                                                                                                                                    |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public HandleInput input``                                 | Command channel selected when resolving this pedal's demand.                                                                                                                                                                                                                            |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Vector3 InteractionValue { get; }``        | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                                                                                                                                                                    |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AnchoredRotation motion``                           | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                                                                                                                  |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pressDuration``                               | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                                                                                                                                               |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pressedAngle``                                | Pedal angle in degrees at displayed value one.                                                                                                                                                                                                                                          |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float releasedAngle``                               | Pedal angle in degrees at displayed value zero.                                                                                                                                                                                                                                         |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float releaseDuration``                             | Seconds to fade after releasing the request; zero stops immediately.                                                                                                                                                                                                                    |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float TargetValue { get; protected set; }`` | Requested pedal demand in 0–1; displayed Value approaches it with press/release travel.                                                                                                                                                                                                 |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useResolvedPedals``                            | For throttle/brake, use the vehicle's resolved propulsion and service brake rather than the shared forward/reverse input.                                                                                                                                                               |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }``       | Current displayed pedal travel in 0–1; it can lag ``TargetValue`` while motion is smoothed.                                                                                                                                                                                             |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-22:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                  | Role and behavior                                                                                                                                  | Arguments and result |
+============================================================================================+====================================================================================================================================================+======================+
| ``public virtual void FollowInput()``                                                      | Releases a manual selection/value override and resumes configured input following.                                                                 | —                    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void ResetMotion()``                                                      | Clears presentation requests and restores the released/default motion state.                                                                       | —                    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetImmediate(float value)``                                          | Takes external value ownership, clamps normalized travel and applies it immediately; ``onValueChanged`` reports an actual displayed-value change.  | —                    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetValue(float value)``                                              | Clamps a fraction to 0–1, maps it between minimum and maximum, then applies ``SetOffset``. Rotation uses degrees; translation uses local distance. | —                    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle.                    | —                    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Tick(float deltaTime)``                                              | Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.                                                | —                    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--pitchsource:

PitchSource
-----------

**Runtime/Interior/Controls/Source/PitchSource.cs**

Samples normalized Command.Pitch (-1..1).

**Inherits / implements:** ``VehicleValueSource``.

.. _uvs-api-interior--methods-23:

Methods
~~~~~~~

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                             | Role and behavior                                                                                                                                                   | Arguments and result |
+=======================================+=====================================================================================================================================================================+======================+
| ``public override float ReadValue()`` | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units. | —                    |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--profileswitchbinding:

ProfileSwitchBinding
--------------------

**Runtime/Interior/Controls/ProfileSwitchBinding.cs**

Configuration/implementation type for profile switch binding within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-interior--state-and-configuration-18:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------------------------+
| Member                                     | Meaning                                                                                   |
+============================================+===========================================================================================+
| ``public string offProfileId``             | Registration ID requested by the off position; defaults to drive.                         |
+--------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public string onProfileId``              | Registration ID requested by the on position; defaults to hover.                          |
+--------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public ProfileSwitcher profileSwitcher`` | Assign the profile switcher ProfileSwitcher component/asset used by ProfileSwitchBinding. |
+--------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public SwitchAnimator switchAnimator``   | Assign the switch handle SwitchHandle component/asset used by ProfileSwitchBinding.       |
+--------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle``       | Assign the vehicle VehicleController component/asset used by ProfileSwitchBinding.        |
+--------------------------------------------+-------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-24:

Methods
~~~~~~~

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                           | Role and behavior                                                                                                                   | Arguments and result                                                                                                                                                                    |
+=====================================================+=====================================================================================================================================+=========================================================================================================================================================================================+
| ``public virtual bool SetOn(bool on)``              | Requests onProfileId when on is true, otherwise offProfileId.                                                                       | ``on`` — Select the configured on or off registration ID. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         | ``immediate`` — Whether to bypass normal presentation travel.                                                                                                                           |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                    |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--rearmirror:

RearMirror
----------

**Runtime/Interior/Render/RearMirrors.cs**

Configuration/implementation type for rear mirror within cockpit instruments and bindings.

.. _uvs-api-interior--state-and-configuration-19:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                               | Meaning                                                                                                                                             |
+======================================+=====================================================================================================================================================+
| ``public bool active``               | Enables this entry/view when it is selected by its owning system. Initial value: ``true``.                                                          |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float aspectRatio``         | Multiplier/fraction controlling aspect ratio. Increasing it increases this contribution relative to the unscaled value. Initial value: ``1.8f``.    |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Camera camera``             | Assign the camera reference used by RearMirror. Leave unassigned only when this feature is optional or the component can resolve it automatically.  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public LayerMask cullingMask``     | Layers included in this camera/render pass. Initial value: ``~0``.                                                                                  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float farClip``             | Mirror camera's far clipping distance, in metres.                                                                                                   |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float fieldOfView``         | Vertical camera field of view in degrees. Initial value: ``55``.                                                                                    |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool flipHorizontally``     | Mirrors the displayed image horizontally. Initial value: ``true``.                                                                                  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumViewDistance`` | Maximum view distance in metres in the owning system's space. Initial value: ``25``.                                                                |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float nearClip``            | Mirror camera's near clipping distance, in metres.                                                                                                  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float refreshRate``         | Maximum update/render frequency in frames per second; lower values reduce rendering work. Initial value: ``20``.                                    |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int resolution``            | Render texture resolution used by the instrument or mirror. Initial value: ``256``.                                                                 |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Renderer surface``          | Assign the surface reference used by RearMirror. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public RenderTexture texture``     | Assign the texture reference used by RearMirror. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string textureProperty``    | Shader texture property receiving the generated or assigned render texture. Initial value: ``"_BaseMap"``.                                          |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--rearmirrors:

RearMirrors
-----------

**Runtime/Interior/Render/RearMirrors.cs**

Owns mirror eligibility, camera rendering and generated textures.

**Inherits / implements:** :ref:`InteriorModule <uvs-api-interior--interiormodule>`.

.. _uvs-api-interior--events-and-inspector-callbacks-6:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+------------------------------------------------------------------------+
| Member                                                  | Meaning                                                                |
+=========================================================+========================================================================+
| ``public event Action<int, bool> MirrorEnabledChanged`` | When one mirror's eligibility changes. Payload: mirror index and bool. |
+---------------------------------------------------------+------------------------------------------------------------------------+
| ``public event Action<bool> MirrorsEnabledChanged``     | When whole-system mirror eligibility changes. Payload: bool.           |
+---------------------------------------------------------+------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-20:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                                                                                               |
+=======================================+=======================================================================================================================================================+
| ``public int maximumRendersPerFrame`` | Maximum count/resolution for maximum renders per frame. Larger values increase detail or work performed by this system. Initial value: ``2``.         |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public List<RearMirror> mirrors``   | Ordered mirrors configuration entries. Expand each item; see RearMirror for its individual settings. Initial value: ``new List<RearMirror>()``.       |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool mirrorsEnabled``        | Enables mirrors behavior for this system. Initial value: ``true``.                                                                                    |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Camera observer``            | Assign the observer reference used by RearMirrors. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-25:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                         | Role and behavior                                                                                                 | Arguments and result                                                                                                                                                                                                       |
+===================================================================================================+===================================================================================================================+============================================================================================================================================================================================================================+
| ``public virtual void SetCameraPose(int index, Vector3 localPosition, Quaternion localRotation)`` | Sets local camera position/rotation for the indexed mirror. The index must be valid; a missing camera is ignored. | ``index`` — Zero-based configured-entry index; use the owner's current list ordering. ``localPosition`` — Position in the selected parent/local frame. ``localRotation`` — Orientation in the selected parent/local frame. |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMirrorEnabled(int index, bool value)``                                   | Changes eligibility of one mirror entry.                                                                          | ``index`` — Zero-based configured-entry index; use the owner's current list ordering. ``value`` — Requested bool state for this operation.                                                                                 |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMirrorsEnabled(bool value)``                                             | Changes the whole mirror system's rendering availability.                                                         | ``value`` — Requested bool state for this operation.                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--rollsource:

RollSource
----------

**Runtime/Interior/Controls/Source/RollSource.cs**

Samples normalized roll (-1..1), optionally displaying resolved wheel steering while taxiing.

**Inherits / implements:** ``VehicleValueSource``.

.. _uvs-api-interior--state-and-configuration-21:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Member                            | Meaning                                                                                            |
+===================================+====================================================================================================+
| ``public bool useGroundSteering`` | Use resolved SteeringNormalized while an airplane is on the ground; otherwise return Command.Roll. |
+-----------------------------------+----------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-26:

Methods
~~~~~~~

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                             | Role and behavior                                                                                                                                                   | Arguments and result |
+=======================================+=====================================================================================================================================================================+======================+
| ``public override float ReadValue()`` | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units. | —                    |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--rotaryanimator:

RotaryAnimator
--------------

**Runtime/Interior/Animators/RotaryAnimator.cs**

Displays a bounded value as rotation, optionally following an IInteriorValueSource. Link a RotaryHandle when an occupant needs to touch the knob.

**Inherits / implements:** ``ControlAnimator``.

.. _uvs-api-interior--events-and-inspector-callbacks-7:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                                                                                             |
+====================================================+=====================================================================================================================================================================+
| ``public UnityEvent<float> onValueChanged``        | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<float> ValueChanged`` | When the requested instrument value changes. Payload: value in configured source units; this is not a motion-arrival notification.                                  |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-22:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                                                                                  |
+========================================================+==========================================================================================================================================================+
| ``public virtual float Angle { get; protected set; }`` | Read-only/resolved angle for ``RotaryHandle``.                                                                                                           |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour dataSource``                    | Optional component implementing ``IInteriorValueSource``; leave empty for API or ``UnityEvents`` control.                                                |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Vector3 InteractionValue { get; }``  | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                                     |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngle``                          | Upper rotation angle in degrees for the configured motion. Initial value: ``135``.                                                                       |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumValue``                          | Upper input/value endpoint mapped to the motion or instrument range. Initial value: ``1``.                                                               |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumAngle``                          | Lower rotation angle in degrees for the configured motion. Initial value: ``-135``.                                                                      |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumValue``                          | Lower input/value endpoint mapped to the motion or instrument range.                                                                                     |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AnchoredRotation motion``                     | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                   |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float NormalizedValue { get; }``      | Read-only/resolved normalized value for ``RotaryHandle``.                                                                                                |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float response``                              | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``18``. |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; }``                | Requested/current instrument-domain value exposed by this control, not a universal 0–1 axis.                                                             |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-27:

Methods
~~~~~~~

+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                    | Role and behavior                                                                                                                                  | Arguments and result |
+==============================================================+====================================================================================================================================================+======================+
| ``public virtual void Bind(MonoBehaviour valueSource)``      | Sets the ongoing instrument value source; ``null`` releases source ownership for explicit value API control.                                       | —                    |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetImmediate(float value)``            | Takes external value ownership, clamps normalized travel and applies it immediately; ``onValueChanged`` reports an actual displayed-value change.  | —                    |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetNormalizedValue(float normalized)`` | Maps a normalized fraction across an instrument's configured physical value range.                                                                 | —                    |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetValue(float value)``                | Clamps a fraction to 0–1, maps it between minimum and maximum, then applies ``SetOffset``. Rotation uses degrees; translation uses local distance. | —                    |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Tick(float deltaTime)``                | Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.                                                | —                    |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--servicebrakesource:

ServiceBrakeSource
------------------

**Runtime/Interior/Controls/Source/ServiceBrakeSource.cs**

Samples resolved service braking or raw Command.ServiceBrake (0..1).

**Inherits / implements:** ``VehicleValueSource``.

.. _uvs-api-interior--state-and-configuration-23:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+-----------------------------------------------------------------------+
| Member                           | Meaning                                                               |
+==================================+=======================================================================+
| ``public bool useResolvedBrake`` | Read resolved ServiceBrake when true; otherwise Command.ServiceBrake. |
+----------------------------------+-----------------------------------------------------------------------+

.. _uvs-api-interior--methods-28:

Methods
~~~~~~~

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                             | Role and behavior                                                                                                                                                   | Arguments and result |
+=======================================+=====================================================================================================================================================================+======================+
| ``public override float ReadValue()`` | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units. | —                    |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--speedvaluesource:

SpeedValueSource
----------------

**Runtime/Interior/Controls/Source/SpeedValueSource.cs**

Configuration/implementation type for speed value source within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorValueSource <uvs-api-interior--interiorvaluesource>`.

.. _uvs-api-interior--state-and-configuration-24:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Member                               | Meaning                                                                                                                                     |
+======================================+=============================================================================================================================================+
| ``public bool signed``               | Preserves forward/reverse sign in the speed readout instead of returning speed magnitude.                                                   |
+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``public SpeedUnit speedUnit``       | Output unit; defaults to Kph. Changing this does not alter vehicle physics. For a signed SpeedValueSource, reverse motion remains negative. |
+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle`` | Assign the vehicle VehicleController component/asset used by SpeedValueSource.                                                              |
+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-29:

Methods
~~~~~~~

+---------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature                             | Role and behavior                                                                          | Arguments and result                                                   |
+=======================================+============================================================================================+========================================================================+
| ``public override float ReadValue()`` | Reads a scalar control or instrument source in its documented normalized or physical unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+---------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _uvs-api-interior--steeringsource:

SteeringSource
--------------

**Runtime/Interior/Controls/Source/SteeringSource.cs**

Samples normalized resolved steering (-1..1), with Hover command steering support.

**Inherits / implements:** ``VehicleValueSource``, ``ISteeringIntentSource``.

.. _uvs-api-interior--state-and-configuration-25:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                                           |
+=====================================+===================================================================================================================+
| ``public bool useResolvedSteering`` | Read SteeringNormalized when true, except Hover which uses Command.Steering. False always reads Command.Steering. |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-30:

Methods
~~~~~~~

+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                     | Role and behavior                                                                                                                                                         | Arguments and result |
+===============================================+===========================================================================================================================================================================+======================+
| ``public virtual float ReadSteeringIntent()`` | Returns raw Command.Steering (-1..1), becoming zero on release while the resolved actuator may still be unwinding. Regrip consumes this intent separately from ReadValue. | —                    |
+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override float ReadValue()``         | Samples a scalar without changing vehicle state. Normalized controls use -1..1 for axes or 0..1 for pressure; RPM and speed retain their configured physical units.       | —                    |
+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--steeringstickanimator:

SteeringStickAnimator
---------------------

**Runtime/Interior/Animators/SteeringStickAnimator.cs**

Owns joystick pitch/roll model motion and taxi steering presentation. JoystickHandle supplies only the hand contacts.

**Inherits / implements:** ``SteeringWheelAnimator``.

.. _uvs-api-interior--state-and-configuration-26:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                                                                                                 |
+======================================================+=========================================================================================================================================================================================+
| ``public float controlResponse``                     | Visual pitch and airborne roll response per second. Taxi roll follows wheel steering directly.                                                                                          |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerSeat driverSeat``                  | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator.                                                                                                     |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public JoystickHandle handle``                     | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion. |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftHandRest``                    | Independent left-hand palm target, in cabin space. Reserved through the steering hand API.                                                                                              |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localPitchAxis``                    | Direction vector defining local pitch axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: ``Vector3.right``.                           |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localRollAxis``                     | Local axis used to apply roll input to the handle or stick. Initial value: ``Vector3.forward``.                                                                                         |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumPitch``                        | Pitch attitude limit in the assisted profile. Aerobatic profiles use angular rates instead.                                                                                             |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRoll``                         | Upper local roll angle in degrees. Initial value: ``6``.                                                                                                                                |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRollOffset``                   | Maximum roll offset for this control.                                                                                                                                                   |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumRoll``                         | Lower local roll angle in degrees. Initial value: ``-6``.                                                                                                                               |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public HandleMotion motion``                       | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                  |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour pitchSource``                 | Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source.                                     |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rotationPivot``                   | Floor/base pivot. Place the stick mesh and its grip targets below this transform.                                                                                                       |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsHandRegrip { get; }`` | Read-only/resolved supports hand regrip for ``SteeringStickAnimator``.                                                                                                                  |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public ThrottleAnimator throttle``                 | Assign the throttle ThrottleAnimator component/asset used by SteeringStickAnimator.                                                                                                     |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-31:

Methods
~~~~~~~

+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------+
| Signature                                    | Role and behavior                                                                    | Arguments and result |
+==============================================+======================================================================================+======================+
| ``public override void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation. | —                    |
+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------+
| ``public override void PrepareHandPose()``   | Prepares the hand pose associated with this cockpit animator.                        | —                    |
+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--steeringwheelanimator:

SteeringWheelAnimator
---------------------

**Runtime/Interior/Animators/SteeringWheelAnimator.cs**

Configuration/implementation type for steering wheel animator within cockpit instruments and bindings.

**Inherits / implements:** ``VehicleHandleAnimator``.

.. _uvs-api-interior--state-and-configuration-27:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                          | Meaning                                                                                                                                                                                                                                                                                 |
+=================================================================+=========================================================================================================================================================================================================================================================================================+
| ``public float boatSteeringResponse``                           | Boat helm rendering response per second. Zero follows the resolved rudder immediately.                                                                                                                                                                                                  |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour dataSource``                             | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float DisplayedAngle { get; protected set; }`` | Read-only/resolved displayed angle for ``SteeringWheelAnimator``.                                                                                                                                                                                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float HandSteeringInput { get; }``             | Requested steering from ISteeringIntentSource when available; scalar-only custom sources use ReadValue. Without a source, reads Command.Steering.                                                                                                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool invert``                                          | Reverses the sign of the assigned control input before applying control-surface motion.                                                                                                                                                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localRotationAxis``                            | Direction vector defining local rotation axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: ``Vector3.forward``.                                                                                                                      |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool overrideSteeringAngle``                           | Use this animator’s visual full-lock angle instead of the vehicle’s shared steering-wheel angle. Default false; does not change physical wheel steering.                                                                                                                                |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``               | Runs in the presentation phase, independently of vehicle mechanics.                                                                                                                                                                                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringAngleAtFullLock``                        | Degrees from neutral to full lock on either side when override is enabled. Default 35; nonnegative.                                                                                                                                                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform steeringWheel``                              | Assign the steering wheel reference used by SteeringWheelAnimator. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                                                                                                   |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsHandRegrip { get; }``             | Read-only/resolved supports hand regrip for ``SteeringWheelAnimator``.                                                                                                                                                                                                                  |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle``                            | Assign the vehicle VehicleController component/asset used by Audio.                                                                                                                                                                                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float VisualSteeringAngleAtFullLock { get; }`` | Resolved visual steering travel, taking the local override into account. Hand-regrip eligibility uses this value.                                                                                                                                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-32:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                  | Role and behavior                                                                                                               | Arguments and result |
+============================================================================================+=================================================================================================================================+======================+
| ``public virtual void CalibrateRestPose()``                                                | Captures the model's current neutral presentation frame for later control animation.                                            | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void PrepareHandPose()``                                                  | Prepares the hand pose associated with this cockpit animator.                                                                   | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle. | —                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--switchanimator:

SwitchAnimator
--------------

**Runtime/Interior/Animators/SwitchAnimator.cs**

Owns binary or three-position detents, requested/actual state, visual travel and switch events. It references a SwitchHandle for optional limb reach synchronization.

**Inherits / implements:** ``ControlAnimator``.

.. _uvs-api-interior--events-and-inspector-callbacks-8:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                  | Meaning                                                                                                                                                                                                  |
+=========================================================+==========================================================================================================================================================================================================+
| ``public UnityEvent<SwitchPosition> onPositionChanged`` | After a changed switch detent request. Payload: ``SwitchPosition``; silent immediate synchronization does not invoke it.                                                                                 |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<bool> onValueChanged``              | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request.                                      |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<SwitchPosition> PositionChanged`` | When requested switch detent changes. Payload: ``SwitchPosition``; distinguish all three positions with this event.                                                                                      |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<SwitchPosition> PositionReached`` | When switch travel settles at its detent. Payload: ``SwitchPosition``.                                                                                                                                   |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> Switched``                  | When switch presentation settles. Payload: bool ``IsOn``; negative and positive three-position states both count as on.                                                                                  |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> ValueChanged``              | When the requested binary ``IsOn`` state changes. Payload: bool. Moving between negative and positive detents keeps ``IsOn`` ``true`` and does not emit this event. Immediate synchronization is silent. |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-28:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                                                                |
+====================================================================+========================================================================================================================================+
| ``public bool initiallyOn``                                        | Initial binary request used by first preparation.                                                                                      |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public SwitchPosition initialPosition``                          | Initial three-position detent used by first preparation.                                                                               |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Vector3 InteractionValue { get; }``              | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                   |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsMoving { get; }``                          | Whether displayed switch travel differs from its requested detent target.                                                              |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsOn { get; }``                              | For a switch, Position is not Neutral; negative and positive both count as on.                                                         |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public HandleMotion motion``                                     | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry. |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float neutralOffset``                                     | Middle-detent geometry offset in degrees or local distance, according to motion.mode.                                                  |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual SwitchPosition Position { get; protected set; }`` | Requested switch detent, distinct from displayed travel and arrival.                                                                   |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool threePosition``                                      | Enables Negative/Neutral/Positive detents; without it Negative requests throw.                                                         |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float transitionDuration``                                | Seconds for visible detent travel; settlement events follow that travel.                                                               |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }``             | Current displayed pedal travel in 0–1; it can lag ``TargetValue`` while motion is smoothed.                                            |
+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-33:

Methods
~~~~~~~

+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                             | Role and behavior                                                                                                                                                                                     | Arguments and result |
+=======================================================================+=======================================================================================================================================================================================================+======================+
| ``public virtual void Prepare()``                                     | Initializes the contact or synchronizes its initial state without requesting a limb.                                                                                                                  | —                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetImmediate(bool value)``                      | Silently synchronizes Positive/Neutral, displayed value and motion without request or settlement callbacks.                                                                                           | —                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetPosition(SwitchPosition position)``          | Requests a detent. Invalid enum values throw ``ArgumentOutOfRangeException``; Negative in binary mode throws ``InvalidOperationException``. A changed request starts travel and emits request events. | —                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetPositionImmediate(SwitchPosition position)`` | Silently synchronizes a switch detent and displayed pose without issuing control events.                                                                                                              | —                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetValue(bool value)``                          | Requests Positive for ``true`` and Neutral for ``false``. Changed requests emit position/bool notifications and start travel.                                                                         | —                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Tick(float deltaTime)``                         | Advances visual travel and optional limb synchronization for a finite nonnegative elapsed duration.                                                                                                   | —                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void Toggle()``                                      | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                                                                                   | —                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--switchposition:

SwitchPosition
--------------

**Runtime/Interior/Animators/SwitchAnimator.cs**

Defines the allowed switch position choices used by this topic.

-  ``Negative = -1``
-  ``Neutral = 0``
-  ``Positive = 1``

.. _uvs-api-interior--throttleanimator:

ThrottleAnimator
----------------

**Runtime/Interior/Animators/ThrottleAnimator.cs**

Owns throttle grip geometry and displayed throttle, including optional external presentation. The paired ThrottleHandle contains only IK contact and grip settings.

**Inherits / implements:** ``ControlAnimator``.

.. _uvs-api-interior--events-and-inspector-callbacks-9:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                                                            |
+====================================================+====================================================================================================================================+
| ``public event System.Action<float> ValueChanged`` | When the requested instrument value changes. Payload: value in configured source units; this is not a motion-arrival notification. |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--state-and-configuration-29:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                          | Meaning                                                                                                                                                                                                                                                                                 |
+=================================================================+=========================================================================================================================================================================================================================================================================================+
| ``public MonoBehaviour dataSource``                             | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float DisplayedValue { get; protected set; }`` | Read-only/resolved displayed value for ``ThrottleAnimator``.                                                                                                                                                                                                                            |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerSeat driverSeat``                             | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator.                                                                                                                                                                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float externalValue``                                  | Externally supplied throttle/control value used when the selected input mode requests external control.                                                                                                                                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Transform HandAnchor { get; }``                | Read-only/resolved hand anchor for ``ThrottleAnimator``.                                                                                                                                                                                                                                |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Vector3 InteractionValue { get; }``           | Displayed control values exposed to the paired contact for generic value events; does not command vehicle mechanics.                                                                                                                                                                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public HandleMotion motion``                                  | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                                                                                                                  |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float response``                                       | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``5``.                                                                                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useExternalValue``                                | Uses explicit cockpit presentation instead of following vehicle throttle.                                                                                                                                                                                                               |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useLeftHand``                                     | Uses the driver's left hand rather than the right for this control.                                                                                                                                                                                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle``                            | Assign the vehicle VehicleController component/asset used by Audio.                                                                                                                                                                                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-34:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                | Role and behavior                                                                                                               | Arguments and result |
+==========================================================================================+=================================================================================================================================+======================+
| ``public override void Configure(VehicleController owner)``                              | Stores the vehicle whose hover transition geometry should be displayed.                                                         | —                    |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void FollowVehicle()``                                                  | Releases external presentation ownership and resumes vehicle-state following.                                                   | —                    |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual bool PrepareHandPose()``                                                | Prepares the hand pose associated with this cockpit animator.                                                                   | —                    |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void SetThrottle(float value)``                                         | Takes external ownership of normalized throttle-lever presentation; ``FollowVehicle`` releases that override.                   | —                    |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController owner, Command command, float deltaTime)`` | Samples vehicle/command state for this control during the module update; visual behavior is owned here, never by the IK handle. | —                    |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-interior--twistthrottleanimator:

TwistThrottleAnimator
---------------------

**Runtime/Interior/Animators/TwistThrottleAnimator.cs**

Displays resolved propulsion by rotating a throttle grip. Inherits :ref:`AnchoredControlAnimator <uvs-api-interior--anchoredcontrolanimator>`; no source selector is required.

**Inherits / implements:** :ref:`AnchoredControlAnimator <uvs-api-interior--anchoredcontrolanimator>`.

.. _uvs-api-interior--state-and-configuration-30:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+-----------------------------------------------------+
| Member                           | Meaning                                             |
+==================================+=====================================================+
| ``public bool absoluteThrottle`` | Display reverse propulsion magnitude; default true. |
+----------------------------------+-----------------------------------------------------+

.. _uvs-api-interior--vehiclehandleanimator:

VehicleHandleAnimator
---------------------

**Runtime/Interior/Animators/VehicleHandleAnimator.cs**

Shared base for instrument geometry ownership. Set Automatic Motion off when an external Animator or Timeline owns the model.

**Inherits / implements:** ``VehicleModule``, ``IInteriorModule``.

.. _uvs-api-interior--state-and-configuration-31:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                                                           |
+=============================================================+===================================================================================================================================+
| ``public bool automaticMotion``                             | Default true. Allows this animator to write model transforms; disable when an external animation system owns the visible control. |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ``public sealed override ModuleCategory Category { get; }`` | Interior scheduling category. Inspector groups this base separately from ordinary Interior modules.                               |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``           | Runs in the presentation phase, independently of vehicle mechanics.                                                               |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--vehiclevaluesource:

VehicleValueSource
------------------

**Runtime/Interior/Controls/Source/VehicleValueSource.cs**

Base for reusable vehicle presentation sources. It stores an optional vehicle and falls back to the nearest parent vehicle. Sources are read by consumers and never drive the vehicle.

**Inherits / implements:** ``InteriorValueSource``.

.. _uvs-api-interior--state-and-configuration-32:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Member                               | Meaning                                                                                                                                       |
+======================================+===============================================================================================================================================+
| ``public VehicleController vehicle`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--yokeanimator:

YokeAnimator
------------

**Runtime/Interior/Animators/YokeAnimator.cs**

Configuration/implementation type for yoke animator within cockpit instruments and bindings.

**Inherits / implements:** :ref:`SteeringWheelAnimator <uvs-api-interior--steeringwheelanimator>`.

.. _uvs-api-interior--state-and-configuration-33:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                                                                                |
+======================================================+========================================================================================================================================================================+
| ``public float controlResponse``                     | Visual pitch and airborne roll response per second. Taxi roll follows wheel steering directly.                                                                         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float HandSteeringInput { get; }`` | Read-only/resolved hand steering input for ``YokeAnimator``.                                                                                                           |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localPitchTravelAxis``              | Direction vector defining local pitch travel axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: ``Vector3.forward``. |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform pitchSlide``                      | Sliding column, with the rotating yoke below it. Leave empty to slide the yoke itself.                                                                                 |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour pitchSource``                 | Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source.                    |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pitchTravel``                         | Pitch travel in metres in the owning system's space. Initial value: ``.035f``.                                                                                         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-interior--methods-35:

Methods
~~~~~~~

+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
| Signature                                    | Role and behavior                                                                    | Arguments and result             |
+==============================================+======================================================================================+==================================+
| ``public override void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation. | No arguments; no returned value. |
+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------+

+------------------------------+--------------------------------------------------------------------+
| Declaration                  | Usage                                                              |
+==============================+====================================================================+
| ``public bool reversePitch`` | Reverse column translation independently of steering-wheel Invert. |
+------------------------------+--------------------------------------------------------------------+
