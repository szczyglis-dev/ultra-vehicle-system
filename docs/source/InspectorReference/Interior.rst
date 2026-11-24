.. _uvs-inspectorreference-interior--interior-controls-and-instruments:

Interior controls and instruments
=================================

:doc:`Back to the complete Inspector reference </InspectorReference>`.

+---------------------------------------------------------------------------------------------------------------+------------------------+
| Component or data block                                                                                       | Settings declared here |
+===============================================================================================================+========================+
| :ref:`AircraftHud <uvs-inspectorreference-interior--aircrafthud>`                                             | 5                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`AnchoredControlAnimator <uvs-inspectorreference-interior--anchoredcontrolanimator>`                     | 7                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`AnchoredRotation <uvs-inspectorreference-interior--anchoredrotation>`                                   | 7                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`CarHud <uvs-inspectorreference-interior--carhud>`                                                       | 6                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ClutchSource <uvs-inspectorreference-interior--clutchsource>`                                           | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`CommandValueSource <uvs-inspectorreference-interior--commandvaluesource>`                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`                                     | 4                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ControlInteraction <uvs-inspectorreference-interior--controlinteraction>`                               | 20                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ControlInteractionAnimationEvents <uvs-inspectorreference-interior--controlinteractionanimationevents>` | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`EngineRpmSource <uvs-inspectorreference-interior--enginerpmsource>`                                     | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GasSource <uvs-inspectorreference-interior--gassource>`                                                 | 2                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearLeverAnimator <uvs-inspectorreference-interior--gearleveranimator>`                                 | 10                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearLeverPosition <uvs-inspectorreference-interior--gearleverposition>`                                 | 4                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearPaddleAnimator <uvs-inspectorreference-interior--gearpaddleanimator>`                               | 7                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearShiftAnimator <uvs-inspectorreference-interior--gearshiftanimator>`                                 | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`HandbrakeSource <uvs-inspectorreference-interior--handbrakesource>`                                     | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`HandleMotion <uvs-inspectorreference-interior--handlemotion>`                                           | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`IndicatorSwitchBinding <uvs-inspectorreference-interior--indicatorswitchbinding>`                       | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`InstrumentNeedle <uvs-inspectorreference-interior--instrumentneedle>`                                   | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`InteriorModule <uvs-inspectorreference-interior--interiormodule>`                                       | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`InteriorValueSource <uvs-inspectorreference-interior--interiorvaluesource>`                             | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`PedalAnimator <uvs-inspectorreference-interior--pedalanimator>`                                         | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`PitchSource <uvs-inspectorreference-interior--pitchsource>`                                             | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ProfileSwitchBinding <uvs-inspectorreference-interior--profileswitchbinding>`                           | 5                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RearMirror <uvs-inspectorreference-interior--rearmirror>`                                               | 14                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RearMirrors <uvs-inspectorreference-interior--rearmirrors>`                                             | 4                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RollSource <uvs-inspectorreference-interior--rollsource>`                                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RotaryAnimator <uvs-inspectorreference-interior--rotaryanimator>`                                       | 9                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ServiceBrakeSource <uvs-inspectorreference-interior--servicebrakesource>`                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SpeedValueSource <uvs-inspectorreference-interior--speedvaluesource>`                                   | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SteeringSource <uvs-inspectorreference-interior--steeringsource>`                                       | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SteeringStickAnimator <uvs-inspectorreference-interior--steeringstickanimator>`                         | 14                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SteeringWheelAnimator <uvs-inspectorreference-interior--steeringwheelanimator>`                         | 13                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SwitchAnimator <uvs-inspectorreference-interior--switchanimator>`                                       | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ThrottleAnimator <uvs-inspectorreference-interior--throttleanimator>`                                   | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`TwistThrottleAnimator <uvs-inspectorreference-interior--twistthrottleanimator>`                         | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`VehicleHandleAnimator <uvs-inspectorreference-interior--vehiclehandleanimator>`                         | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`YokeAnimator <uvs-inspectorreference-interior--yokeanimator>`                                           | 7                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+

.. _uvs-inspectorreference-interior--aircrafthud:

AircraftHud
-----------

Configuration/implementation type for aircraft hud within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Render/AircraftHud.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorModule <uvs-inspectorreference-interior--interiormodule>`. These settings also appear on this type.

+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                                         | Description                                                                                                                                                         | Declared default and constraints |
+=====================+==============================================================================================+=====================================================================================================================================================================+==================================+
| ``cockpitSurface``  | ``Renderer``                                                                                 | Screen mesh receiving the flight-display texture through its material property block. Assign the display face rather than the whole cockpit renderer when possible. | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``customTexture``   | ``Texture``                                                                                  | Fixed texture displayed instead of drawing the generated flight HUD. Leave empty to show live vehicle readouts.                                                     | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``refreshRate``     | ``float``                                                                                    | Maximum times per second the generated flight display redraws. Lower values save work but make readout changes less smooth.                                         | ``15``; Range: 1 to 30           |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``textureProperty`` | ``string``                                                                                   | Shader texture slot on the cockpit screen that receives the HUD image. Use the exact property name exposed by the screen material's shader.                         | ``"_BaseMap"``                   |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``         | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Aircraft supplying speed, attitude and other flight readouts. If empty, the display initially binds to a VehicleController in its parent hierarchy.                 | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--anchoredcontrolanimator:

AnchoredControlAnimator
-----------------------

Concrete animator for service-brake, clutch and handbrake levers. Select the mechanic with Input; each lever retains its own component instance. The stationary anchor must be outside the moving-part hierarchy; its captured authored pose is retained across enable/disable.

**Source:** ``Runtime/Interior/Animators/AnchoredControlAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`. These settings also appear on this type.

+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                                     | Description                                                                                                                                                                                                                                                                             | Declared default and constraints |
+=====================+==========================================================================================+=========================================================================================================================================================================================================================================================================================+==================================+
| ``dataSource``      | ``MonoBehaviour``                                                                        | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). | ``None / unassigned``            |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motion``          | ``AnchoredRotation`` (:ref:`fields <uvs-inspectorreference-interior--anchoredrotation>`) | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                                                                                                                  | ``new AnchoredRotation()``       |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onValueChanged``  | ``UnityEvent<float>``                                                                    | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request.                                                                                                                     | ``No listeners``                 |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pressDuration``   | ``float``                                                                                | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                                                                                                                                               | ``.08``; Minimum: 0              |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pressedAngle``    | ``float``                                                                                | Pedal angle in degrees at displayed value one.                                                                                                                                                                                                                                          | ``25``                           |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``releasedAngle``   | ``float``                                                                                | Pedal angle in degrees at displayed value zero.                                                                                                                                                                                                                                         | ``0``                            |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``releaseDuration`` | ``float``                                                                                | Seconds to fade after releasing the request; zero stops immediately.                                                                                                                                                                                                                    | ``.12``; Minimum: 0              |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--anchoredrotation:

AnchoredRotation
----------------

Preserves a neutral pose relative to an independent pivot frame.

**Source:** ``Runtime/Interior/Controls/AnchoredRotation.cs``. Nested configuration data; expand its owning field in the Inspector.

+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting        | Type                                                                                         | Description                                                                                                                                            | Declared default and constraints |
+================+==============================================================================================+========================================================================================================================================================+==================================+
| ``anchor``     | ``Transform``                                                                                | Fixed transform defining the rotation centre and axes. It cannot be the moving mesh or its child, otherwise the hinge would move with the part.        | ``None / unassigned``            |
+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localAxis``  | ``Vector3``                                                                                  | Hinge direction in Anchor's local coordinates. The mesh rotates around this axis through the anchor position, even if its imported pivot is elsewhere. | ``Vector3.right``                |
+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mode``       | ``AircraftControlMotionMode``                                                                | Procedural rotation/translation, a sampled clip, or callback-only custom movement. Options: ``Rotation``, ``Translation``, ``Animation``, ``Custom``.  | ``Rotation``                     |
+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``movingPart`` | ``Transform``                                                                                | Mesh rotated around the independent anchor, retaining its captured offset from the hinge. Its own imported pivot does not have to lie on the hinge.    | ``None / unassigned``            |
+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``playback``   | ``PartMotionPlayback`` (:ref:`fields <uvs-inspectorreference-exterior--partmotionplayback>`) | Animation/custom binding and lifecycle callbacks.                                                                                                      | ``new PartMotionPlayback()``     |
+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``reverse``    | ``bool``                                                                                     | Mirror motion around the neutral pose without changing input or travel limits.                                                                         | ``false``                        |
+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``valueRange`` | ``Vector2``                                                                                  | Offset range used by direct SetAngle calls in non-rotation modes. Owner animators supply normalized values directly.                                   | ``new Vector2(0, 1)``            |
+----------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--carhud:

CarHud
------

Configuration/implementation type for car hud within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Render/CarHud.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorModule <uvs-inspectorreference-interior--interiormodule>`. These settings also appear on this type.

+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                                         | Description                                                                                                                                                                             | Declared default and constraints |
+=====================+==============================================================================================+=========================================================================================================================================================================================+==================================+
| ``cockpitSurface``  | ``Renderer``                                                                                 | Dashboard screen renderer receiving the display texture. The configured Texture Property must exist in its material's shader.                                                           | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``customTexture``   | ``Texture``                                                                                  | Texture replacing the generated dashboard readout. Leave empty for live speed, fuel and warning indicators.                                                                             | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``refreshRate``     | ``float``                                                                                    | Maximum dashboard image redraws per second. Reduce for cheaper small screens; increase for smoother live needles/readouts.                                                              | ``10``; Range: 1 to 30           |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``speedUnit``       | ``SpeedUnit``                                                                                | Unit used for the dashboard's speed readout. Switching between km/h, mph and m/s changes the numbers, not the vehicle's physical speed. Options: ``Kph``, ``Mph``, ``MetresPerSecond``. | ``SpeedUnit.Kph``                |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``textureProperty`` | ``string``                                                                                   | Shader texture slot receiving the generated dashboard image or Custom Texture. A wrong property name leaves the screen material unchanged.                                              | ``"_BaseMap"``                   |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``         | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Vehicle supplying speed, fuel, lights and assist indicators to the dashboard screen. If empty, the display initially finds a parent VehicleController.                                  | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--clutchsource:

ClutchSource
------------

Samples Command.Clutch (0..1).

**Source:** ``Runtime/Interior/Controls/Source/ClutchSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-interior--commandvaluesource:

CommandValueSource
------------------

Samples a selected Command channel, without resolved actuator mapping.

**Source:** ``Runtime/Interior/Controls/Source/CommandValueSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

+-----------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting   | Type            | Description                                                                                                                                                                          | Declared default and constraints |
+===========+=================+======================================================================================================================================================================================+==================================+
| ``input`` | ``HandleInput`` | Command channel to sample through HandleCommandInput. Options: ``Brake``, ``Throttle``, ``Clutch``, ``Steering``, ``Pitch``, ``Roll``, ``Yaw``, ``Lift``, ``Strafe``, ``Handbrake``. | ``HandleInput.Throttle``         |
+-----------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--controlanimator:

ControlAnimator
---------------

Shared control presentation base. It references an optional IK handle, coordinates real limb arrival and owns Wait For Handle / Fake Sync Handle Motion. It does not act as an IK target.

**Source:** ``Runtime/Interior/Animators/ControlAnimator.cs``. Abstract base; settings are inherited by derived components.

**Inherited settings:** :ref:`VehicleHandleAnimator <uvs-inspectorreference-interior--vehiclehandleanimator>`. These settings also appear on this type.

+--------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                  | Type                                                                            | Description                                                                                                                                                                                                                                                                                                                               | Declared default and constraints |
+==========================+=================================================================================+===========================================================================================================================================================================================================================================================================================================================================+==================================+
| ``fakeSyncHandleMotion`` | ``bool``                                                                        | Default false. Outbound reach uses the contact pose captured before visual motion; after arrival it follows the live anchor.                                                                                                                                                                                                              | ``false``                        |
+--------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``handle``               | ``VehicleHandle`` (:ref:`fields <uvs-inspectorreference-world--vehiclehandle>`) | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion.                                                                                                                                                   | ``None / unassigned``            |
+--------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``showGizmos``           | ``bool``                                                                        | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see :ref:`Scene gizmo visibility <uvs-configuration--scene-gizmo-visibility>` for the controls available on this component. | ``true``                         |
+--------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``waitForHandle``        | ``bool``                                                                        | Default true. Wait for the real palm/foot within 2.5 cm after transit, plus finger blending for hands. Mechanics remain immediate; steering is excluded.                                                                                                                                                                                  | ``true``                         |
+--------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--controlinteraction:

ControlInteraction
------------------

``Started``, ``Commit``, ``Completed`` and ``Cancelled``

**Source:** ``Runtime/Interior/Controls/ControlInteraction.cs``. Component / asset.

+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                            | Type                                                                            | Description                                                                                                                                                                                                                                                                           | Declared default and constraints |
+====================================+=================================================================================+=======================================================================================================================================================================================================================================================================================+==================================+
| ``animationEnterBlend``            | ``float``                                                                       | Seconds used to blend from the underlying pose into an Animator gesture. Zero applies the gesture layer immediately.                                                                                                                                                                  | ``.2``; Minimum: 0               |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animationEvents``                | ``bool``                                                                        | Use Animation Events to call Commit and Complete instead of elapsed time.                                                                                                                                                                                                             | ``false``                        |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animationLayer``                 | ``string``                                                                      | Optional Animator layer name enabled for this gesture. Empty leaves controller layer weights unchanged. Configure the trigger transition on this layer.                                                                                                                               | ``""``                           |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animationLayerWeight``           | ``float``                                                                       | Weight temporarily applied to Animation Layer during the gesture. Its previous weight is restored on completion/cancellation unless externally changed.                                                                                                                               | ``1``; Range: 0 to 1             |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animationReturnBlend``           | ``float``                                                                       | Seconds used to blend an Animator gesture back to the underlying pose after completion. Zero restores the layer immediately.                                                                                                                                                          | ``.2``; Minimum: 0               |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animator``                       | ``Animator``                                                                    | Optional override. Otherwise use the current occupant's SeatedAnimator.                                                                                                                                                                                                               | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``commitTime``                     | ``float``                                                                       | Seconds from animation start until the control action is committed when timed commit is used. Set it to the moment the hand visibly presses or moves the control.                                                                                                                     | ``.25``; Minimum: 0              |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``customDriver``                   | ``MonoBehaviour``                                                               | A MonoBehaviour implementing IControlInteractionDriver.                                                                                                                                                                                                                               | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``duration``                       | ``float``                                                                       | Total timed animation interaction length in seconds. After both this duration and Commit Time have elapsed, the sequence can complete and restore hand control.                                                                                                                       | ``.7``; Minimum: 0               |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``hand``                           | ``PassengerBodyPart``                                                           | Hand used for the interaction. Choose LeftHand or RightHand; foot selections are not accepted by this hand-interaction sequence. Options: ``LeftHand``, ``RightHand``, ``LeftFoot``, ``RightFoot``.                                                                                   | ``PassengerBodyPart.LeftHand``   |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``keepHandOnTargetWhileAnimating`` | ``bool``                                                                        | IK then Animator: keep the hand attached to its target while a finger-only animation plays. Use a gesture layer masked to fingers. The arm retains its existing IK or physical support.                                                                                               | ``false``                        |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mode``                           | ``ControlInteractionMode``                                                      | Immediate commits the control action at once. IK first transfers a hand to Target. Animator uses an animation and its timing/events. Custom delegates the sequence to the assigned interaction handler. Options: ``Immediate``, ``IK``, ``Animator``, ``Custom``, ``IKThenAnimator``. | ``ControlInteractionMode.IK``    |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onCancelled``                    | ``UnityEvent``                                                                  | Invoked if the gesture is interrupted before normal completion.                                                                                                                                                                                                                       | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onCommit``                       | ``UnityEvent``                                                                  | Invoked at the gesture commit point when the control action is applied.                                                                                                                                                                                                               | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onCompleted``                    | ``UnityEvent``                                                                  | Invoked after the gesture finishes normally.                                                                                                                                                                                                                                          | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onStarted``                      | ``UnityEvent``                                                                  | Invoked when an interaction gesture begins.                                                                                                                                                                                                                                           | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``seat``                           | ``PassengerSeat`` (:ref:`fields <uvs-inspectorreference-world--passengerseat>`) | Seat containing the character who operates this control. IK, Animator and Custom modes require an eligible occupant; Immediate can work without one.                                                                                                                                  | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``target``                         | ``VehicleHandle`` (:ref:`fields <uvs-inspectorreference-world--vehiclehandle>`) | Handle the character reaches for before the control action is committed in IK mode. Its contact pose determines where the hand goes.                                                                                                                                                  | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``timeout``                        | ``float``                                                                       | Cancels an unfinished Animator or Custom action, including missing animation events. Zero disables timeout.                                                                                                                                                                           | ``5``; Minimum: 0                |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``trigger``                        | ``string``                                                                      | Exact Animator trigger parameter name used to start an Animator-mode interaction. It must exist as a trigger in the assigned animation controller.                                                                                                                                    | ``"Interact"``                   |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--controlinteractionanimationevents:

ControlInteractionAnimationEvents
---------------------------------

Relays Animator events to the active interaction.

**Source:** ``Runtime/Interior/Controls/ControlInteractionAnimationEvents.cs``. Component / asset.

+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting         | Type                                                                                         | Description                                                                                                                                                   | Declared default and constraints |
+=================+==============================================================================================+===============================================================================================================================================================+==================================+
| ``interaction`` | ``ControlInteraction`` (:ref:`fields <uvs-inspectorreference-interior--controlinteraction>`) | Active interaction receiving commit, complete and cancel events from this animation clip. Put this relay on the object receiving the clip's Animation Events. | ``None / unassigned``            |
+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--enginerpmsource:

EngineRpmSource
---------------

Configuration/implementation type for engine rpm source within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Controls/Source/EngineRpmSource.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorValueSource <uvs-inspectorreference-interior--interiorvaluesource>`. These settings also appear on this type.

+------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting    | Type                                                               | Description                                                                                                    | Declared default and constraints |
+============+====================================================================+================================================================================================================+==================================+
| ``engine`` | ``Engine`` (:ref:`fields <uvs-inspectorreference-engine--engine>`) | Engine whose current RPM is returned to the bound gauge or control. A missing or disabled engine returns zero. | ``None / unassigned``            |
+------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--gassource:

GasSource
---------

Samples DriveDemand or raw throttle demand. Optional magnitude supports reverse propulsion and motorcycle twist grips.

**Source:** ``Runtime/Interior/Controls/Source/GasSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

+-----------------------+----------+------------------------------------------------------------------------------------------------+----------------------------------+
| Setting               | Type     | Description                                                                                    | Declared default and constraints |
+=======================+==========+================================================================================================+==================================+
| ``absoluteValue``     | ``bool`` | Return the magnitude, including reverse propulsion; disable to retain the signed source value. | ``true``                         |
+-----------------------+----------+------------------------------------------------------------------------------------------------+----------------------------------+
| ``useResolvedDemand`` | ``bool`` | Read resolved signed DriveDemand when true; otherwise Command.Throttle.                        | ``true``                         |
+-----------------------+----------+------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--gearleveranimator:

GearLeverAnimator
-----------------

Follows accepted gearbox selections and coordinates a timed hand reach before moving the lever. The moving-part origin must coincide with the stationary floor anchor in its neutral pose. Preview never changes the gearbox.

**Source:** ``Runtime/Interior/Animators/GearLeverAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`. These settings also appear on this type.

+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| Setting             | Type                                                                                         | Description                                                                                                                                                              | Declared default and constraints                |
+=====================+==============================================================================================+==========================================================================================================================================================================+=================================================+
| ``anchor``          | ``Transform``                                                                                | Contact transform used for IK. Parent it to the moving grip; it is separate from the animator hinge/pivot anchor.                                                        | ``None / unassigned``                           |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``downshiftDelay``  | ``float``                                                                                    | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. | ``.75``; Minimum: 0                             |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``engine``          | ``Engine`` (:ref:`fields <uvs-inspectorreference-engine--engine>`)                           | Assign the engine Engine component/asset used by Propulsion.                                                                                                             | ``None / unassigned``                           |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``gearbox``         | ``Gearbox`` (:ref:`fields <uvs-inspectorreference-engine--gearbox>`)                         | Assign the gearbox Gearbox component/asset used by CommercialAudio.                                                                                                      | ``None / unassigned``                           |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``mode``            | ``GearLeverMotionMode``                                                                      | Rotation or Translation. Options: ``Rotation``, ``Translation``, ``Animation``, ``Custom``.                                                                              | ``Rotation``                                    |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``movingPart``      | ``Transform``                                                                                | ``Transform`` whose pose this mapper owns; keep imported-mesh offsets on its child.                                                                                      | ``None / unassigned``                           |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``onGearRequested`` | ``UnityEngine.Events.UnityEvent<int>``                                                       | Accepted gear request, also available in Custom mode before motion starts.                                                                                               | ``new UnityEngine.Events.UnityEvent<int>()``    |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``playback``        | ``PartMotionPlayback`` (:ref:`fields <uvs-inspectorreference-exterior--partmotionplayback>`) | Clip/custom implementation and lifecycle callbacks. Custom drivers can read RequestedGear from the owner.                                                                | ``new PartMotionPlayback()``                    |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``positions``       | ``GearLeverPosition[]`` (:ref:`fields <uvs-inspectorreference-interior--gearleverposition>`) | Unique signed gear numbers and their absolute poses. Defaults include R, N and gears 1–6.                                                                                | ``Default collection/object defined in source`` |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| ``shiftDuration``   | ``float``                                                                                    | Time in seconds during which gear-changing torque transfer is interrupted/blended. Initial value: ``.14f``.                                                              | ``.18``; Minimum: 0                             |
+---------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------+

.. _uvs-inspectorreference-interior--gearleverposition:

GearLeverPosition
-----------------

**Source:** ``Runtime/Interior/Animators/GearLeverAnimator.cs``. Nested configuration data; expand its owning field in the Inspector.

+--------------+-------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting      | Type              | Description                                                                                                       | Declared default and constraints |
+==============+===================+===================================================================================================================+==================================+
| ``clip``     | ``AnimationClip`` | Optional transition clip into this gear, from its start pose to its selected pose. Falls back to the shared clip. | ``None / unassigned``            |
+--------------+-------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``gear``     | ``int``           | Signed gear number: -1 = reverse, 0 = neutral, 1 and above = forward gears. Each number must be unique.           | ``0``                            |
+--------------+-------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``position`` | ``Vector3``       | Local position in metres for this gear-lever pose.                                                                | ``Zero-initialized Vector3``     |
+--------------+-------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rotation`` | ``Vector3``       | Local Euler angles in degrees for this gear-lever pose.                                                           | ``Zero-initialized Vector3``     |
+--------------+-------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--gearpaddleanimator:

GearPaddleAnimator
------------------

Receives accepted gear changes through IGearShiftAnimator, coalesces downshifts, then reaches, presses and releases the paddle. Link a GearPaddleHandle for the intended hand.

**Source:** ``Runtime/Interior/Animators/GearPaddleAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`. These settings also appear on this type.

+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting            | Type                                                                                     | Description                                                                                                                                                              | Declared default and constraints |
+====================+==========================================================================================+==========================================================================================================================================================================+==================================+
| ``direction``      | ``GearShiftDirection``                                                                   | Selects the direction policy for this configuration. Options: ``Both``, ``Up``, ``Down``.                                                                                | ``Both``                         |
+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``downshiftDelay`` | ``float``                                                                                | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. | ``.25``; Minimum: 0              |
+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motion``         | ``AnchoredRotation`` (:ref:`fields <uvs-inspectorreference-interior--anchoredrotation>`) | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                   | ``new AnchoredRotation()``       |
+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onPressed``      | ``UnityEvent``                                                                           | Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction.                     | ``No listeners``                 |
+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pressDuration``  | ``float``                                                                                | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                                | ``.08``; Minimum: 0              |
+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pressedAngle``   | ``float``                                                                                | Pedal angle in degrees at displayed value one.                                                                                                                           | ``12``                           |
+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``returnDuration`` | ``float``                                                                                | Return travel duration in seconds, independent of outbound travel.                                                                                                       | ``.16``; Minimum: 0              |
+--------------------+------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--gearshiftanimator:

GearShiftAnimator
-----------------

Synchronizes shift presentation with accepted mechanical gear changes.

**Source:** ``Runtime/Interior/Animators/GearShiftAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleHandleAnimator <uvs-inspectorreference-interior--vehiclehandleanimator>`. These settings also appear on this type.

+---------------+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting       | Type                                                                 | Description                                                                                                        | Declared default and constraints |
+===============+======================================================================+====================================================================================================================+==================================+
| ``animators`` | ``MonoBehaviour[]``                                                  | Visual gear controls implementing IGearShiftAnimator. Assign the paddle animators; do not assign their IK handles. | ``Empty list``                   |
+---------------+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``engine``    | ``Engine`` (:ref:`fields <uvs-inspectorreference-engine--engine>`)   | Assign the engine Engine component/asset used by Propulsion.                                                       | ``None / unassigned``            |
+---------------+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``gearbox``   | ``Gearbox`` (:ref:`fields <uvs-inspectorreference-engine--gearbox>`) | Assign the gearbox Gearbox component/asset used by CommercialAudio.                                                | ``None / unassigned``            |
+---------------+----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--handbrakesource:

HandbrakeSource
---------------

Samples Command.Handbrake as 0 or 1.

**Source:** ``Runtime/Interior/Controls/Source/HandbrakeSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-interior--handlemotion:

HandleMotion
------------

Reusable geometry mapping for animator-owned rotation or translation in an independent anchor frame. It is not an IK contact.

**Source:** ``Runtime/Interior/Animators/HandleMotion.cs``. Nested configuration data; expand its owning field in the Inspector.

+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting        | Type                                                                                         | Description                                                                                                                                                          | Declared default and constraints |
+================+==============================================================================================+======================================================================================================================================================================+==================================+
| ``anchor``     | ``Transform``                                                                                | Independent hinge and local axis frame outside Moving Part. Preserves the authored neutral mesh offset; translation distances are metres regardless of anchor scale. | ``None / unassigned``            |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localAxis``  | ``Vector3``                                                                                  | Local axis around which the configured motion or operation takes place. Initial value: ``Vector3.forward``.                                                          | ``Vector3.right``                |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximum``    | ``float``                                                                                    | Offset at normalized value one; values may be signed/reversed to match model direction.                                                                              | ``20``                           |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimum``    | ``float``                                                                                    | Offset at normalized value zero: degrees in rotation mode, local distance in translation mode.                                                                       | ``-20``                          |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mode``       | ``AircraftControlMotionMode``                                                                | Chooses rotation (degrees) or translation (local distance) for minimum/maximum/offset. Options: ``Rotation``, ``Translation``, ``Animation``, ``Custom``.            | ``Rotation``                     |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``movingPart`` | ``Transform``                                                                                | ``Transform`` whose pose this mapper owns; keep imported-mesh offsets on its child.                                                                                  | ``None / unassigned``            |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``playback``   | ``PartMotionPlayback`` (:ref:`fields <uvs-inspectorreference-exterior--partmotionplayback>`) | Animation/custom implementation and lifecycle callbacks for this handle geometry.                                                                                    | ``new PartMotionPlayback()``     |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``reverse``    | ``bool``                                                                                     | Mirror motion around the neutral pose without changing input or travel limits.                                                                                       | ``false``                        |
+----------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--indicatorswitchbinding:

IndicatorSwitchBinding
----------------------

Configuration/implementation type for indicator switch binding within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Controls/IndicatorSwitchBinding.cs``. Component / asset.

+--------------------+--------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting            | Type                                                                                 | Description                                                                                                                                                                    | Declared default and constraints |
+====================+======================================================================================+================================================================================================================================================================================+==================================+
| ``leftPosition``   | ``SwitchPosition``                                                                   | Detent that selects left indicators. Choose Negative or Positive; the opposite detent selects right and Neutral remains off. Options: ``Negative``, ``Neutral``, ``Positive``. | ``SwitchPosition.Negative``      |
+--------------------+--------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``lights``         | ``Lights`` (:ref:`fields <uvs-inspectorreference-exterior--lights>`)                 | Lights module connected to the stalk. Moving the switch requests indicators, and indicator state changes move the switch back to the matching position.                        | ``None / unassigned``            |
+--------------------+--------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``switchAnimator`` | ``SwitchAnimator`` (:ref:`fields <uvs-inspectorreference-interior--switchanimator>`) | Switch animator whose requested/settled position drives this binding. Assign the matching cockpit switch component.                                                            | ``None / unassigned``            |
+--------------------+--------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--instrumentneedle:

InstrumentNeedle
----------------

Specializes value-driven rotation for instruments.

**Source:** ``Runtime/Interior/Controls/InstrumentNeedle.cs``. Component / asset.

**Inherited settings:** :ref:`RotaryAnimator <uvs-inspectorreference-interior--rotaryanimator>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-interior--interiormodule:

InteriorModule
--------------

Configuration/implementation type for interior module within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Core/InteriorModule.cs``. Abstract base; settings are inherited by derived components.

**Inherited settings:** :ref:`VehicleModule <uvs-inspectorreference-common--vehiclemodule>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-interior--interiorvaluesource:

InteriorValueSource
-------------------

Base adapter for an ``IInteriorValueSource`` value producer.

**Source:** ``Runtime/Interior/Controls/Source/InteriorValueSource.cs``. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-interior--pedalanimator:

PedalAnimator
-------------

Samples an interchangeable IInteriorValueSource (or built-in resolved/command fallback) and animates pedal travel. Its paired PedalHandle owns foot/ankle contact geometry.

**Source:** ``Runtime/Interior/Animators/PedalAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`. These settings also appear on this type.

+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                                     | Description                                                                                                                                                                                                                                                                             | Declared default and constraints |
+=====================+==========================================================================================+=========================================================================================================================================================================================================================================================================================+==================================+
| ``absoluteInput``   | ``bool``                                                                                 | Use absolute input for signed propulsion/reverse commands.                                                                                                                                                                                                                              | ``true``                         |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``dataSource``      | ``MonoBehaviour``                                                                        | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). | ``None / unassigned``            |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motion``          | ``AnchoredRotation`` (:ref:`fields <uvs-inspectorreference-interior--anchoredrotation>`) | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                                                                                                                  | ``new AnchoredRotation()``       |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onValueChanged``  | ``UnityEvent<float>``                                                                    | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request.                                                                                                                     | ``No listeners``                 |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pressDuration``   | ``float``                                                                                | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                                                                                                                                               | ``.1``; Minimum: 0               |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pressedAngle``    | ``float``                                                                                | Pedal angle in degrees at displayed value one.                                                                                                                                                                                                                                          | ``20``                           |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``releasedAngle``   | ``float``                                                                                | Pedal angle in degrees at displayed value zero.                                                                                                                                                                                                                                         | ``0``                            |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``releaseDuration`` | ``float``                                                                                | Seconds to fade after releasing the request; zero stops immediately.                                                                                                                                                                                                                    | ``.08``; Minimum: 0              |
+---------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--pitchsource:

PitchSource
-----------

Samples normalized Command.Pitch (-1..1).

**Source:** ``Runtime/Interior/Controls/Source/PitchSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-interior--profileswitchbinding:

ProfileSwitchBinding
--------------------

Configuration/implementation type for profile switch binding within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Controls/ProfileSwitchBinding.cs``. Component / asset.

+---------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                                         | Description                                                                                                                                          | Declared default and constraints |
+=====================+==============================================================================================+======================================================================================================================================================+==================================+
| ``offProfileId``    | ``string``                                                                                   | Destination profile ID requested when the switch turns off.                                                                                          | ``"Drive"``                      |
+---------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onProfileId``     | ``string``                                                                                   | Destination profile ID requested when the switch turns on.                                                                                           | ``"Hover"``                      |
+---------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``profileSwitcher`` | ``ProfileSwitcher`` (:ref:`fields <uvs-inspectorreference-drive--profileswitcher>`)          | Registered profile list used to resolve the on/off profile IDs and perform the requested change. The switch follows its active profile state.        | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``switchAnimator``  | ``SwitchAnimator`` (:ref:`fields <uvs-inspectorreference-interior--switchanimator>`)         | Switch animator whose requested/settled position drives this binding. Assign the matching cockpit switch component.                                  | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``         | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Vehicle whose movement profile is represented by the cockpit switch. It is checked alongside ProfileSwitcher to identify the currently active setup. | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--rearmirror:

RearMirror
----------

Configuration/implementation type for rear mirror within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Render/RearMirrors.cs``. Nested configuration data; expand its owning field in the Inspector.

+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                 | Type              | Description                                                                                                                                                                         | Declared default and constraints |
+=========================+===================+=====================================================================================================================================================================================+==================================+
| ``active``              | ``bool``          | Allows this individual mirror to render while the mirror system is enabled and the surface is visible. Turn off to stop updates for this mirror only.                               | ``true``                         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``aspectRatio``         | ``float``         | Width divided by height for an automatically created mirror texture. At 2, the texture is twice as wide as high. Match this to the mirror screen shape.                             | ``1.8``; Range: .5f to 3         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``camera``              | ``Camera``        | Dedicated camera looking behind the vehicle for this mirror. RearMirrors renders it manually to a texture, so do not use the main driving camera here.                              | ``None / unassigned``            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``cullingMask``         | ``LayerMask``     | Layers visible in this mirror's reflection. Exclude UI, helpers or costly geometry that should not appear behind the vehicle.                                                       | ``~0``                           |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``farClip``             | ``float``         | Mirror camera far clipping distance in metres.                                                                                                                                      | ``120``; Minimum: 1              |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``fieldOfView``         | ``float``         | Vertical view angle in degrees of this mirror camera. Increase to show a wider rear area, at the cost of making objects look smaller.                                               | ``55``; Range: 10 to 150         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``flipHorizontally``    | ``bool``          | Flips the displayed camera image left-to-right. Enable when the mirror should present a mirrored view instead of a rear-facing camera feed.                                         | ``true``                         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumViewDistance`` | ``float``         | Observer-to-mirror distance in metres beyond which this mirror stops updating. Lower values save rendering work when the camera is far from the vehicle.                            | ``25``; Minimum: 1               |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``nearClip``            | ``float``         | Mirror camera near clipping distance in metres.                                                                                                                                     | ``.1``; Minimum: .01f            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``refreshRate``         | ``float``         | Maximum mirror updates per second. Reduce to save rendering work; frame budget, visibility and distance can further lower the actual rate.                                          | ``20``; Range: 1 to 60           |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``resolution``          | ``int``           | Width in pixels of an automatically created mirror texture. Higher values sharpen the reflection but increase rendering and texture memory; an assigned Texture keeps its own size. | ``256``; Range: 64 to 2048       |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``surface``             | ``Renderer``      | Mirror-face renderer that displays this entry's camera image. Its visibility, layer and distance from the observer decide whether a render is needed.                               | ``None / unassigned``            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``texture``             | ``RenderTexture`` | Optional existing render texture receiving the mirror image. If empty, the system creates one using Resolution and Aspect Ratio.                                                    | ``None / unassigned``            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``textureProperty``     | ``string``        | Exact shader property name receiving this mirror's render texture, such as the material's main texture slot. It must match the shader used by Surface.                              | ``"_BaseMap"``                   |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--rearmirrors:

RearMirrors
-----------

Owns mirror eligibility, camera rendering and generated textures.

**Source:** ``Runtime/Interior/Render/RearMirrors.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorModule <uvs-inspectorreference-interior--interiormodule>`. These settings also appear on this type.

+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                    | Type                                                                               | Description                                                                                                                                                 | Declared default and constraints |
+============================+====================================================================================+=============================================================================================================================================================+==================================+
| ``maximumRendersPerFrame`` | ``int``                                                                            | Maximum mirror-camera renders in one frame. Lower this to spread updates across frames and reduce frame spikes; higher values update more mirrors together. | ``2``; Range: 1 to 8             |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mirrors``                | ``List<RearMirror>`` (:ref:`fields <uvs-inspectorreference-interior--rearmirror>`) | Mirror screens and their dedicated cameras. Add one entry per independently rendered mirror; each can have its own resolution and refresh limits.           | ``Empty list``                   |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mirrorsEnabled``         | ``bool``                                                                           | Master switch for updating all mirror cameras. Individual entries still need Active enabled and must pass visibility/distance checks.                       | ``true``                         |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``observer``               | ``Camera``                                                                         | Camera used to decide whether mirror surfaces are visible and close enough to update. If empty, Camera.main is used.                                        | ``None / unassigned``            |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--rollsource:

RollSource
----------

Samples normalized roll (-1..1), optionally displaying resolved wheel steering while taxiing.

**Source:** ``Runtime/Interior/Controls/Source/RollSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

+-----------------------+----------+----------------------------------------------------------------------------------------------------+----------------------------------+
| Setting               | Type     | Description                                                                                        | Declared default and constraints |
+=======================+==========+====================================================================================================+==================================+
| ``useGroundSteering`` | ``bool`` | Use resolved SteeringNormalized while an airplane is on the ground; otherwise return Command.Roll. | ``true``                         |
+-----------------------+----------+----------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--rotaryanimator:

RotaryAnimator
--------------

Displays a bounded value as rotation, optionally following an IInteriorValueSource. Link a RotaryHandle when an occupant needs to touch the knob.

**Source:** ``Runtime/Interior/Animators/RotaryAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`. These settings also appear on this type.

+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting            | Type                                                                                     | Description                                                                                                                                                                                                                                                                             | Declared default and constraints |
+====================+==========================================================================================+=========================================================================================================================================================================================================================================================================================+==================================+
| ``dataSource``     | ``MonoBehaviour``                                                                        | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). | ``None / unassigned``            |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumAngle``   | ``float``                                                                                | Upper rotation angle in degrees for the configured motion. Initial value: ``28``.                                                                                                                                                                                                       | ``135``                          |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumValue``   | ``float``                                                                                | Upper input/value endpoint mapped to the motion or instrument range. Initial value: ``1``.                                                                                                                                                                                              | ``1``                            |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimumAngle``   | ``float``                                                                                | Lower rotation angle in degrees for the configured motion. Initial value: ``-135``.                                                                                                                                                                                                     | ``-135``                         |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimumValue``   | ``float``                                                                                | Lower input/value endpoint mapped to the motion or instrument range.                                                                                                                                                                                                                    | ``0``                            |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motion``         | ``AnchoredRotation`` (:ref:`fields <uvs-inspectorreference-interior--anchoredrotation>`) | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                                                                                                                  | ``new AnchoredRotation()``       |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onValueChanged`` | ``UnityEvent<float>``                                                                    | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request.                                                                                                                     | ``No listeners``                 |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``response``       | ``float``                                                                                | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``5``.                                                                                                                                 | ``18``; Minimum: 0               |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``value``          | ``float``                                                                                | Requested value in the configured units. An assigned source replaces it each frame.                                                                                                                                                                                                     | ``0``                            |
+--------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--servicebrakesource:

ServiceBrakeSource
------------------

Samples resolved service braking or raw Command.ServiceBrake (0..1).

**Source:** ``Runtime/Interior/Controls/Source/ServiceBrakeSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

+----------------------+----------+-----------------------------------------------------------------------+----------------------------------+
| Setting              | Type     | Description                                                           | Declared default and constraints |
+======================+==========+=======================================================================+==================================+
| ``useResolvedBrake`` | ``bool`` | Read resolved ServiceBrake when true; otherwise Command.ServiceBrake. | ``true``                         |
+----------------------+----------+-----------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--speedvaluesource:

SpeedValueSource
----------------

Configuration/implementation type for speed value source within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Controls/Source/SpeedValueSource.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorValueSource <uvs-inspectorreference-interior--interiorvaluesource>`. These settings also appear on this type.

+---------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting       | Type                                                                                         | Description                                                                                                                         | Declared default and constraints |
+===============+==============================================================================================+=====================================================================================================================================+==================================+
| ``signed``    | ``bool``                                                                                     | Preserve forward/reverse sign instead of returning speed magnitude.                                                                 | ``false``                        |
+---------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``speedUnit`` | ``SpeedUnit``                                                                                | Unit used for the returned/displayed speed value. Options: ``Kph``, ``Mph``, ``MetresPerSecond``.                                   | ``SpeedUnit.Kph``                |
+---------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``   | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Vehicle whose speed is read for a gauge or display. Signed chooses forward/reverse speed; Speed Unit determines the returned units. | ``None / unassigned``            |
+---------------+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--steeringsource:

SteeringSource
--------------

Samples normalized resolved steering (-1..1), with Hover command steering support.

**Source:** ``Runtime/Interior/Controls/Source/SteeringSource.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleValueSource <uvs-inspectorreference-interior--vehiclevaluesource>`. These settings also appear on this type.

+-------------------------+----------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                 | Type     | Description                                                                                                       | Declared default and constraints |
+=========================+==========+===================================================================================================================+==================================+
| ``useResolvedSteering`` | ``bool`` | Read SteeringNormalized when true, except Hover which uses Command.Steering. False always reads Command.Steering. | ``true``                         |
+-------------------------+----------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--steeringstickanimator:

SteeringStickAnimator
---------------------

Owns joystick pitch/roll model motion and taxi steering presentation. JoystickHandle supplies only the hand contacts.

**Source:** ``Runtime/Interior/Animators/SteeringStickAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`SteeringWheelAnimator <uvs-inspectorreference-interior--steeringwheelanimator>`. These settings also appear on this type.

+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting               | Type                                                                                     | Description                                                                                                                                                                             | Declared default and constraints |
+=======================+==========================================================================================+=========================================================================================================================================================================================+==================================+
| ``controlResponse``   | ``float``                                                                                | Visual pitch and airborne roll response per second. Taxi roll follows wheel steering directly.                                                                                          | ``3``; Minimum: .1f              |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``driverSeat``        | ``PassengerSeat`` (:ref:`fields <uvs-inspectorreference-world--passengerseat>`)          | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator.                                                                                                     | ``None / unassigned``            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``handle``            | ``JoystickHandle`` (:ref:`fields <uvs-inspectorreference-world--joystickhandle>`)        | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion. | ``None / unassigned``            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``leftHandRest``      | ``Transform``                                                                            | Independent left-hand palm target, in cabin space. Reserved through the steering hand API.                                                                                              | ``None / unassigned``            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localPitchAxis``    | ``Vector3``                                                                              | Direction vector defining local pitch axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: ``Vector3.right``.                           | ``Vector3.right``                |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localRollAxis``     | ``Vector3``                                                                              | Local axis used to apply roll input to the handle or stick. Initial value: ``Vector3.forward``.                                                                                         | ``Vector3.forward``              |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumPitch``      | ``float``                                                                                | Pitch attitude limit for Simple Steering. With Simple Steering disabled, the aircraft uses angular rates instead.                                                                       | ``6``; Range: 0 to 40            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumRoll``       | ``float``                                                                                | Upper local roll angle in degrees. Initial value: ``6``.                                                                                                                                | ``6``; Range: 0 to 40            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumRollOffset`` | ``float``                                                                                | Maximum roll offset for this control.                                                                                                                                                   | ``6``                            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``minimumRoll``       | ``float``                                                                                | Lower local roll angle in degrees. Initial value: ``-6``.                                                                                                                               | ``-6``                           |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motion``            | ``HandleMotion`` (:ref:`fields <uvs-inspectorreference-interior--handlemotion>`)         | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                  | ``new HandleMotion()``           |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pitchSource``       | ``MonoBehaviour``                                                                        | Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source.                                     | ``None / unassigned``            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``rotationPivot``     | ``Transform``                                                                            | Floor/base pivot. Place the stick mesh and its grip targets below this transform.                                                                                                       | ``None / unassigned``            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``throttle``          | ``ThrottleAnimator`` (:ref:`fields <uvs-inspectorreference-interior--throttleanimator>`) | Assign the throttle ThrottleAnimator component/asset used by SteeringStickAnimator.                                                                                                     | ``None / unassigned``            |
+-----------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--steeringwheelanimator:

SteeringWheelAnimator
---------------------

Configuration/implementation type for steering wheel animator within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Animators/SteeringWheelAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`VehicleHandleAnimator <uvs-inspectorreference-interior--vehiclehandleanimator>`. These settings also appear on this type.

+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                     | Type                                                                                         | Description                                                                                                                                                                                                                                                                             | Declared default and constraints |
+=============================+==============================================================================================+=========================================================================================================================================================================================================================================================================================+==================================+
| ``anchor``                  | ``Transform``                                                                                | Optional independent steering-wheel hinge and local axis frame. Empty keeps the original rest-local rotation.                                                                                                                                                                           | ``None / unassigned``            |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``boatSteeringResponse``    | ``float``                                                                                    | Boat helm rendering response per second. Zero follows the resolved rudder immediately.                                                                                                                                                                                                  | ``20``; Minimum: 0               |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``dataSource``              | ``MonoBehaviour``                                                                            | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). | ``None / unassigned``            |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``invert``                  | ``bool``                                                                                     | Reverses the sign of the assigned control input before applying control-surface motion.                                                                                                                                                                                                 | ``false``                        |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localRotationAxis``       | ``Vector3``                                                                                  | Direction vector defining local rotation axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: ``Vector3.forward``.                                                                                                                      | ``Vector3.forward``              |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motionMode``              | ``AircraftControlMotionMode``                                                                | Procedural rotation/translation, clip animation, or callback-only custom steering motion. Options: ``Rotation``, ``Translation``, ``Animation``, ``Custom``.                                                                                                                            | ``Rotation``                     |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``overrideSteeringAngle``   | ``bool``                                                                                     | Use this animator’s visual full-lock angle instead of the vehicle’s shared steering-wheel angle. Default false; does not change physical wheel steering.                                                                                                                                | ``false``                        |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``playback``                | ``PartMotionPlayback`` (:ref:`fields <uvs-inspectorreference-exterior--partmotionplayback>`) | Animation/custom steering motion and lifecycle callbacks.                                                                                                                                                                                                                               | ``new PartMotionPlayback()``     |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``showGizmos``              | ``bool``                                                                                     | Show mode-specific steering motion guides in the Scene view. Expand **Gizmos** for independent visibility controls; see :ref:`Scene gizmo visibility <uvs-configuration--scene-gizmo-visibility>` for the controls available on this component.                                         | ``true``                         |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``steeringAngleAtFullLock`` | ``float``                                                                                    | Degrees from neutral to full lock on either side when override is enabled. Default 35; nonnegative.                                                                                                                                                                                     | ``35``; Minimum: 0               |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``steeringWheel``           | ``Transform``                                                                                | Assign the steering wheel reference used by SteeringWheelAnimator. Leave unassigned only when this feature is optional or the component can resolve it automatically.                                                                                                                   | ``None / unassigned``            |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``translationTravel``       | ``float``                                                                                    | Metres of translation from neutral at full steering, in either direction.                                                                                                                                                                                                               | ``.05``                          |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``                 | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Assign the vehicle VehicleController component/asset used by Audio.                                                                                                                                                                                                                     | ``None / unassigned``            |
+-----------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--switchanimator:

SwitchAnimator
--------------

Owns binary or three-position detents, requested/actual state, visual travel and switch events. It references a SwitchHandle for optional limb reach synchronization.

**Source:** ``Runtime/Interior/Animators/SwitchAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`. These settings also appear on this type.

+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| Setting                | Type                                                                             | Description                                                                                                                                                         | Declared default and constraints                  |
+========================+==================================================================================+=====================================================================================================================================================================+===================================================+
| ``initiallyOn``        | ``bool``                                                                         | Initial binary request used by first preparation.                                                                                                                   | ``false``                                         |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ``initialPosition``    | ``SwitchPosition``                                                               | Initial three-position detent used by first preparation. Options: ``Negative``, ``Neutral``, ``Positive``.                                                          | ``Negative``                                      |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ``motion``             | ``HandleMotion`` (:ref:`fields <uvs-inspectorreference-interior--handlemotion>`) | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                              | ``new HandleMotion{minimum = 25, maximum = -25}`` |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ``neutralOffset``      | ``float``                                                                        | Middle-detent geometry offset in degrees or local distance, according to motion.mode.                                                                               | ``0``                                             |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ``onPositionChanged``  | ``UnityEvent<SwitchPosition>``                                                   | After a changed switch detent request. Payload: ``SwitchPosition``; silent immediate synchronization does not invoke it.                                            | ``No listeners``                                  |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ``onValueChanged``     | ``UnityEvent<bool>``                                                             | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. | ``No listeners``                                  |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ``threePosition``      | ``bool``                                                                         | Enables Negative/Neutral/Positive detents; without it Negative requests throw.                                                                                      | ``false``                                         |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+
| ``transitionDuration`` | ``float``                                                                        | Seconds for visible detent travel; settlement events follow that travel.                                                                                            | ``.16``; Minimum: .01f                            |
+------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------+

.. _uvs-inspectorreference-interior--throttleanimator:

ThrottleAnimator
----------------

Owns throttle grip geometry and displayed throttle, including optional external presentation. The paired ThrottleHandle contains only IK contact and grip settings.

**Source:** ``Runtime/Interior/Animators/ThrottleAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`ControlAnimator <uvs-inspectorreference-interior--controlanimator>`. These settings also appear on this type.

+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting              | Type                                                                                         | Description                                                                                                                                                                                                                                                                             | Declared default and constraints |
+======================+==============================================================================================+=========================================================================================================================================================================================================================================================================================+==================================+
| ``dataSource``       | ``MonoBehaviour``                                                                            | Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven). | ``None / unassigned``            |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``driverSeat``       | ``PassengerSeat`` (:ref:`fields <uvs-inspectorreference-world--passengerseat>`)              | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator.                                                                                                                                                                                                     | ``None / unassigned``            |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``externalValue``    | ``float``                                                                                    | Externally supplied throttle/control value used when the selected input mode requests external control.                                                                                                                                                                                 | ``0``; Range: 0 to 1             |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``motion``           | ``HandleMotion`` (:ref:`fields <uvs-inspectorreference-interior--handlemotion>`)             | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                                                                                                                  | ``new HandleMotion()``           |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``response``         | ``float``                                                                                    | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``5``.                                                                                                                                 | ``5``; Minimum: 0                |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``useExternalValue`` | ``bool``                                                                                     | Uses explicit cockpit presentation instead of following vehicle throttle.                                                                                                                                                                                                               | ``false``                        |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``useLeftHand``      | ``bool``                                                                                     | Uses the driver's left hand rather than the right for this control.                                                                                                                                                                                                                     | ``true``                         |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``          | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Assign the vehicle VehicleController component/asset used by Audio.                                                                                                                                                                                                                     | ``None / unassigned``            |
+----------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--twistthrottleanimator:

TwistThrottleAnimator
---------------------

Displays resolved propulsion by rotating a throttle grip. Inherits :ref:`AnchoredControlAnimator <uvs-api-interior--anchoredcontrolanimator>`; no source selector is required.

**Source:** ``Runtime/Interior/Animators/TwistThrottleAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`AnchoredControlAnimator <uvs-inspectorreference-interior--anchoredcontrolanimator>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _uvs-inspectorreference-interior--vehiclehandleanimator:

VehicleHandleAnimator
---------------------

Shared base for instrument geometry ownership. Set Automatic Motion off when an external Animator or Timeline owns the model.

**Source:** ``Runtime/Interior/Animators/VehicleHandleAnimator.cs``. Abstract base; settings are inherited by derived components.

**Inherited settings:** :ref:`VehicleModule <uvs-inspectorreference-common--vehiclemodule>`. These settings also appear on this type.

+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type     | Description                                                                                                                       | Declared default and constraints |
+=====================+==========+===================================================================================================================================+==================================+
| ``automaticMotion`` | ``bool`` | Default true. Allows this animator to write model transforms; disable when an external animation system owns the visible control. | ``true``                         |
+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--vehiclevaluesource:

VehicleValueSource
------------------

Base for reusable vehicle presentation sources. It stores an optional vehicle and falls back to the nearest parent vehicle. Sources are read by consumers and never drive the vehicle.

**Source:** ``Runtime/Interior/Controls/Source/VehicleValueSource.cs``. Abstract base; settings are inherited by derived components.

**Inherited settings:** :ref:`InteriorValueSource <uvs-inspectorreference-interior--interiorvaluesource>`. These settings also appear on this type.

+-------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting     | Type                                                                                         | Description                                                                                                                                   | Declared default and constraints |
+=============+==============================================================================================+===============================================================================================================================================+==================================+
| ``vehicle`` | ``VehicleController`` (:ref:`fields <uvs-inspectorreference-controller--vehiclecontroller>`) | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. | ``None / unassigned``            |
+-------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _uvs-inspectorreference-interior--yokeanimator:

YokeAnimator
------------

Configuration/implementation type for yoke animator within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Animators/YokeAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`SteeringWheelAnimator <uvs-inspectorreference-interior--steeringwheelanimator>`. These settings also appear on this type.

+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                  | Type              | Description                                                                                                                                         | Declared default and constraints |
+==========================+===================+=====================================================================================================================================================+==================================+
| ``controlResponse``      | ``float``         | Visual pitch and airborne roll response per second. Taxi roll follows wheel steering directly.                                                      | ``1.5``; Minimum: .1f            |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localPitchTravelAxis`` | ``Vector3``       | Direction the yoke slides for pitch commands, in the slider parent's local coordinates. Usually forward/back along the steering column.             | ``Vector3.forward``              |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pitchAnchor``          | ``Transform``     | Optional independent column translation direction frame outside the slider. Local Pitch Travel Axis uses its local axes; Pitch Travel is in metres. | ``None / unassigned``            |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pitchSlide``           | ``Transform``     | Sliding column, with the rotating yoke below it. Leave empty to slide the yoke itself.                                                              | ``None / unassigned``            |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pitchSource``          | ``MonoBehaviour`` | Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source. | ``None / unassigned``            |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pitchTravel``          | ``float``         | Maximum yoke slide in metres from neutral for full pitch input in either direction. Increase for a longer push/pull stroke.                         | ``.035``; Minimum: 0             |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``reversePitch``         | ``bool``          | Reverse column translation independently of steering-wheel Invert.                                                                                  | ``false``                        |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
