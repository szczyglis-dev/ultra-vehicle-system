.. _uvs-scripting-eventsreference--events-reference:

Events reference
================

Public notifications grouped by the class that declares them. Each class has its own table with the event/callback, argument types and the point at which it fires. Events follow declaration order within each class; the class sections are ordered by name.

``C#`` means subscribe with ``+=`` / ``-=``. ``Inspector`` means a UnityEvent field, connected in the Inspector or with ``AddListener`` / ``RemoveListener``. Arguments are shown in delegate order; ``—`` means no arguments. Read current state when first subscribing rather than expecting an initial notification.

Inherited events are listed once on their declaring base class: Module lifecycle events also apply to derived modules. Profiles and helper classes are included where they expose events. Inspector callbacks nested in settings identify their invoking component below.

.. _uvs-scripting-eventsreference--runtime-classes:

Runtime classes
---------------

.. _uvs-scripting-eventsreference--aircraftcontrolsurfaces:

AircraftControlSurfaces
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| Event / callback           | Kind | Arguments   | When it fires / meaning                                                                            |
+============================+======+=============+====================================================================================================+
| ``AirbrakeChanged``        | C#   | ``float``   | When the normalized airbrake presentation request changes.                                         |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| ``ControlsChanged``        | C#   | ``Vector3`` | When displayed pitch/roll/yaw controls change; Vector3 components carry those presentation values. |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| ``ExternalControlChanged`` | C#   | ``bool``    | When aircraft surface presentation changes external/follow-vehicle ownership.                      |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| ``FlapsChanged``           | C#   | ``float``   | When the normalized flap presentation request changes.                                             |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+

Details: :ref:`AircraftControlSurfaces API <uvs-api-aircraft--aircraftcontrolsurfaces>`.

.. _uvs-scripting-eventsreference--aircrafthud:

AircraftHud
~~~~~~~~~~~

+------------------+------+---------------+--------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                    |
+==================+======+===============+============================================+
| ``Changed``      | C#   | ``Telemetry`` | After the HUD receives an updated reading. |
+------------------+------+---------------+--------------------------------------------+

Details: :ref:`AircraftHud API <uvs-api-interior--aircrafthud>`.

.. _uvs-scripting-eventsreference--anchoredcontrolanimator:

AnchoredControlAnimator
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+
| Event / callback   | Kind      | Arguments | When it fires / meaning                                                                |
+====================+===========+===========+========================================================================================+
| ``onValueChanged`` | Inspector | ``float`` | After the animated control value changes (0–1), including reset to the released value. |
+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+

Details: :ref:`AnchoredControlAnimator API <uvs-api-interior--anchoredcontrolanimator>`.

.. _uvs-scripting-eventsreference--antilockbrakes:

AntiLockBrakes
~~~~~~~~~~~~~~

+-------------------+------+-----------+----------------------------------------------------------------------------------+
| Event / callback  | Kind | Arguments | When it fires / meaning                                                          |
+===================+======+===========+==================================================================================+
| ``ActiveChanged`` | C#   | ``bool``  | Raised when one or more wheels enter/leave ABS service-brake pressure reduction. |
+-------------------+------+-----------+----------------------------------------------------------------------------------+

Details: :ref:`AntiLockBrakes API <uvs-api-drivedynamics--antilockbrakes>`.

.. _uvs-scripting-eventsreference--balancerider:

BalanceRider
~~~~~~~~~~~~

+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind      | Arguments             | When it fires / meaning                                                                                                                  |
+==========================+===========+=======================+==========================================================================================================================================+
| ``BodyLeanChanged``      | C#        | ``Vector2``           | Requested torso lean changes; X forward and Y sideways in degrees.                                                                       |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``FootLifted``           | C#        | ``PassengerBodyPart`` | A foot leaves its target support phase, including return to riding, flight, release or disable.                                          |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``FootPlanted``          | C#        | ``PassengerBodyPart`` | When a foot becomes planted; payload identifies the left or right foot.                                                                  |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``FootPushingChanged``   | C#        | ``bool``              | When foot-pushing starts or stops; payload is the new active state.                                                                      |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``MotionUpdated``        | C#        | ``RiderMotionState``  | After the rider motion state is sampled, including speed, foot-pushing and planted-foot state.                                           |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``RidingBlendChanged``   | C#        | ``float``             | The effective ground-to-riding target blend changes.                                                                                     |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``onBodyLeanChanged``    | Inspector | ``Vector2``           | Inspector counterpart of BodyLeanChanged.                                                                                                |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``onFootLifted``         | Inspector | ``PassengerBodyPart`` | Inspector counterpart of FootLifted.                                                                                                     |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``onFootPlanted``        | Inspector | ``PassengerBodyPart`` | A foot reaches its target support phase at rest, while stepping, or during inside/fallen support; this is not a measured sole collision. |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``onFootPushingChanged`` | Inspector | ``bool``              | Foot propulsion begins or stops; false is also published on disable or loss of occupancy.                                                |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``onMotionUpdated``      | Inspector | ``RiderMotionState``  | Current motion state after rider targets update. Suitable for custom animation integrations.                                             |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``onRidingBlendChanged`` | Inspector | ``float``             | Inspector counterpart of RidingBlendChanged.                                                                                             |
+--------------------------+-----------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`BalanceRider API <uvs-api-passengercontrollers--balancerider>`.

.. _uvs-scripting-eventsreference--boatprofile:

BoatProfile
~~~~~~~~~~~

+--------------------+------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback   | Kind | Arguments | When it fires / meaning                                                                                                                                 |
+====================+======+===========+=========================================================================================================================================================+
| ``SinkingChanged`` | C#   | ``bool``  | Raised once when sinking is started or stopped. The argument is the new sinking state; repeated requests for the same state do not raise another event. |
+--------------------+------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`BoatProfile API <uvs-api-boat--boatprofile>`.

.. _uvs-scripting-eventsreference--brakes:

Brakes
~~~~~~

+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+
| Event / callback        | Kind | Arguments | When it fires / meaning                                                                                          |
+=========================+======+===========+==================================================================================================================+
| ``BrakingChanged``      | C#   | ``bool``  | Moving service-brake activity changes; payload is active/inactive. Owned by Brakes, independent of TireFeedback. |
+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+
| ``HandbrakeChanged``    | C#   | ``bool``  | When the resolved handbrake state changes; bool reports the new state.                                           |
+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+
| ``ServiceBrakeChanged`` | C#   | ``float`` | When resolved service-brake demand changes (0–1).                                                                |
+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Brakes API <uvs-api-drivedynamics--brakes>`.

.. _uvs-scripting-eventsreference--burnout:

Burnout
~~~~~~~

+--------------------+------+-----------+--------------------------------------------------------+
| Event / callback   | Kind | Arguments | When it fires / meaning                                |
+====================+======+===========+========================================================+
| ``BurnoutStarted`` | C#   | —         | Assistance begins.                                     |
+--------------------+------+-----------+--------------------------------------------------------+
| ``BurnoutStopped`` | C#   | —         | Assistance ends, including reset/disable.              |
+--------------------+------+-----------+--------------------------------------------------------+
| ``StateChanged``   | C#   | ``bool``  | Reports transitions into and out of active assistance. |
+--------------------+------+-----------+--------------------------------------------------------+

Details: :ref:`Burnout API <uvs-api-drivedynamics--burnout>`.

.. _uvs-scripting-eventsreference--cameras:

Cameras
~~~~~~~

+-------------------+------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback  | Kind | Arguments    | When it fires / meaning                                                                                                                               |
+===================+======+==============+=======================================================================================================================================================+
| ``CameraChanged`` | C#   | ``Camera``   | After Attach changes the assigned camera or Detach releases it; payload is the new camera or null. Inspector field edits do not raise this API event. |
+-------------------+------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ModeChanged``   | C#   | ``ViewMode`` | After SetView or Attach changes the view; payload is the new mode.                                                                                    |
+-------------------+------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Cameras API <uvs-api-camera--cameras>`.

.. _uvs-scripting-eventsreference--carhud:

CarHud
~~~~~~

+------------------+------+---------------+--------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                    |
+==================+======+===============+============================================+
| ``Changed``      | C#   | ``Telemetry`` | After the HUD receives an updated reading. |
+------------------+------+---------------+--------------------------------------------+

Details: :ref:`CarHud API <uvs-api-interior--carhud>`.

.. _uvs-scripting-eventsreference--clutch:

Clutch
~~~~~~

+-----------------------+------+-----------+----------------------------------------------------------------------------+
| Event / callback      | Kind | Arguments | When it fires / meaning                                                    |
+=======================+======+===========+============================================================================+
| ``AutomaticChanged``  | C#   | ``bool``  | When automatic clutch assistance selection changes.                        |
+-----------------------+------+-----------+----------------------------------------------------------------------------+
| ``EngagementChanged`` | C#   | ``float`` | When resolved clutch engagement changes (0–1); distinct from pedal travel. |
+-----------------------+------+-----------+----------------------------------------------------------------------------+

Details: :ref:`Clutch API <uvs-api-drivedynamics--clutch>`.

.. _uvs-scripting-eventsreference--controlinteraction:

ControlInteraction
~~~~~~~~~~~~~~~~~~

+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                                                                                                                 |
+==================+===========+===========+=========================================================================================================================================+
| ``onCancelled``  | Inspector | —         | After an active interaction is cancelled. No payload; committed gameplay is not rolled back.                                            |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``onCommit``     | Inspector | —         | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks. |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``onCompleted``  | Inspector | —         | After the interaction completes. No payload; completion commits first if still needed.                                                  |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``onStarted``    | Inspector | —         | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately.                          |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`ControlInteraction API <uvs-api-interactions--controlinteraction>`.

.. _uvs-scripting-eventsreference--coupler:

Coupler
~~~~~~~

+------------------+------+-------------+---------------------------------------------------------------+
| Event / callback | Kind | Arguments   | When it fires / meaning                                       |
+==================+======+=============+===============================================================+
| ``Attached``     | C#   | ``Trailer`` | After coupler admission creates the relationship.             |
+------------------+------+-------------+---------------------------------------------------------------+
| ``Detached``     | C#   | ``Trailer`` | After explicit detachment/cleanup of this hitch relationship. |
+------------------+------+-------------+---------------------------------------------------------------+

Details: :ref:`Coupler API <uvs-api-towing--coupler>`.

.. _uvs-scripting-eventsreference--damage:

Damage
~~~~~~

+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments            | When it fires / meaning                                                                                  |
+==========================+======+======================+==========================================================================================================+
| ``DeformationRequested`` | C#   | ``DamageHit, float`` | Accepted hit and radius before part detachment; optional deformation receivers process it synchronously. |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``EffectsCleared``       | C#   | —                    | Requests clearing optional impact presentation.                                                          |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``FullyRepaired``        | C#   | —                    | After a full repair pass and effect cleanup; it does not guarantee destroyed objects were recreated.     |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``Hit``                  | C#   | ``DamageHit``        | When a damage hit is accepted.                                                                           |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``PartsChanged``         | C#   | —                    | Reports that the damage boundary list has been refreshed.                                                |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+

Details: :ref:`Damage API <uvs-api-damage--damage>`.

.. _uvs-scripting-eventsreference--damageaudio:

DamageAudio
~~~~~~~~~~~

+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback       | Kind      | Arguments                                     | When it fires / meaning                                                                                                                           |
+========================+===========+===============================================+===================================================================================================================================================+
| ``DamagePlayed``       | C#        | ``DamageHit, DamageImpactProfile, AudioClip`` | A scripted hit sound started; includes the selected material profile.                                                                             |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``DetachmentPlayed``   | C#        | ``DamagePart, AudioClip``                     | A named part detachment sound started.                                                                                                            |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Played``             | C#        | ``DamageContact, AudioClip``                  | A one-shot started; includes the contact and actual clip.                                                                                         |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ScrapeStarted``      | C#        | ``DamageContact, AudioClip``                  | A scrape lane became audible; contact and original loop clip.                                                                                     |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ScrapeStopped``      | C#        | ``DamageContact, AudioClip``                  | A scrape lane faded/stopped, switched material/group or was cleared.                                                                              |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onDamagePlayed``     | Inspector | ``DamageHit, DamageImpactProfile, AudioClip`` | A scripted DamageHit sound successfully started, with its selected material profile and clip.                                                     |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onDetachmentPlayed`` | Inspector | ``DamagePart, AudioClip``                     | A named part's detachment sound successfully started.                                                                                             |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onPlayed``           | Inspector | ``DamageContact, AudioClip``                  | A one-shot successfully started. Reports the contact and actual clip, including audio-context processing; does not report scrape loop iterations. |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onScrapeStarted``    | Inspector | ``DamageContact, AudioClip``                  | A sustained scrape loop started. Reports its contact and original clip before audio-context processing.                                           |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onScrapeStopped``    | Inspector | ``DamageContact, AudioClip``                  | A scrape loop stopped, faded out, changed material/group or was cleared. Does not report each loop iteration.                                     |
+------------------------+-----------+-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`DamageAudio API <uvs-api-damagefeedback--damageaudio>`.

.. _uvs-scripting-eventsreference--damagefeedback:

DamageFeedback
~~~~~~~~~~~~~~

+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback     | Kind      | Arguments                          | When it fires / meaning                                                                                                                           |
+======================+===========+====================================+===================================================================================================================================================+
| ``Cleared``          | C#        | —                                  | Contact history and presentation were cleared.                                                                                                    |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Contacted``        | C#        | ``DamageContact``                  | Any accepted presentation contact.                                                                                                                |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``EffectPlayed``     | C#        | ``DamageHit, DamageImpactProfile`` | Custom pooled impact effect successfully started.                                                                                                 |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``EffectsCleared``   | C#        | —                                  | Custom effect leases were cleared.                                                                                                                |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``FallLanded``       | C#        | ``DamageContact``                  | First qualifying height-fall ground contact, shared across body, attached panels and wheels.                                                      |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Impacted``         | C#        | ``DamageContact``                  | Accepted non-scrape cue.                                                                                                                          |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PartBroken``       | C#        | ``DamageContact``                  | Accepted breakage presentation cue; not physical detachment itself.                                                                               |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``RolloverImpacted`` | C#        | ``DamageContact``                  | One qualifying tilted/spinning ground strike.                                                                                                     |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Scraped``          | C#        | ``DamageContact``                  | Accepted sustained-contact sample; can run every physics step.                                                                                    |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``SuspensionMoved``  | C#        | ``DamageContact``                  | Accepted suspension compression/landing cue.                                                                                                      |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``TireImpacted``     | C#        | ``DamageContact``                  | Accepted wheel strike, distinct from touchdown.                                                                                                   |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``TireLanded``       | C#        | ``DamageContact``                  | Accepted wheel touchdown with landing strength/height.                                                                                            |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onBreakage``       | Inspector | ``DamageContact``                  | Accepted part breakage cue. Use DamagePart.Detached for the physical detachment itself.                                                           |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onCleared``        | Inspector | —                                  | Contact history and presentation were cleared.                                                                                                    |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onContact``        | Inspector | ``DamageContact``                  | Every accepted impact or scrape sample. This is presentation data and does not apply physical damage.                                             |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onEffectPlayed``   | Inspector | ``DamageHit, DamageImpactProfile`` | Custom pooled impact prefab successfully started.                                                                                                 |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onEffectsCleared`` | Inspector | —                                  | Custom effect leases were cleared.                                                                                                                |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onFallLanding``    | Inspector | ``DamageContact``                  | First qualifying ground contact after a height fall; shared by body, attached parts and wheels.                                                   |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onImpact``         | Inspector | ``DamageContact``                  | Every accepted non-scrape cue, including body, wheel, landing, suspension and breakage.                                                           |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onRolloverImpact`` | Inspector | ``DamageContact``                  | A qualifying tilted/spinning ground impact, deduplicated across the whole vehicle.                                                                |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onScrape``         | Inspector | ``DamageContact``                  | Accepted sustained-contact samples; may run every physics step while sliding. Use Damage Audio scrape lifecycle callbacks for audible start/stop. |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onSuspension``     | Inspector | ``DamageContact``                  | Accepted suspension compression or landing response.                                                                                              |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onTireImpact``     | Inspector | ``DamageContact``                  | Accepted wheel strike, independently of a touchdown.                                                                                              |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onTireLanding``    | Inspector | ``DamageContact``                  | Accepted wheel touchdown, with landing strength and fall-height data.                                                                             |
+----------------------+-----------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`DamageFeedback API <uvs-api-damagefeedback--damagefeedback>`.

.. _uvs-scripting-eventsreference--damagepart:

DamagePart
~~~~~~~~~~

+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments             | When it fires / meaning                                                                    |
+==================+======+=======================+============================================================================================+
| ``Damaged``      | C#   | ``DamagePart, float`` | After the part accepts damage.                                                             |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| ``Detached``     | C#   | ``DamagePart``        | After a damage part detaches.                                                              |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| ``Repaired``     | C#   | ``DamagePart, float`` | After damage is actually removed.                                                          |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| ``Restored``     | C#   | ``DamagePart``        | After full remount/state/mesh repair; incremental Repair(amount) does not emit this event. |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+

Details: :ref:`DamagePart API <uvs-api-damage--damagepart>`.

.. _uvs-scripting-eventsreference--drivingassists:

DrivingAssists
~~~~~~~~~~~~~~

+-----------------------------+------+-----------+--------------------------------------------------------------------------+
| Event / callback            | Kind | Arguments | When it fires / meaning                                                  |
+=============================+======+===========+==========================================================================+
| ``StabilityControlChanged`` | C#   | ``bool``  | When ``DrivingAssists`` changes its stability-assistance choice.         |
+-----------------------------+------+-----------+--------------------------------------------------------------------------+
| ``TractionControlChanged``  | C#   | ``bool``  | When ``DrivingAssists`` changes its coordinated traction-control choice. |
+-----------------------------+------+-----------+--------------------------------------------------------------------------+

Details: :ref:`DrivingAssists API <uvs-api-drivedynamics--drivingassists>`.

.. _uvs-scripting-eventsreference--droppableobject:

DroppableObject
~~~~~~~~~~~~~~~

+------------------+------+---------------------+--------------------------------------------------+
| Event / callback | Kind | Arguments           | When it fires / meaning                          |
+==================+======+=====================+==================================================+
| ``Dropped``      | C#   | ``DroppableObject`` | After this payload detaches and inherits motion. |
+------------------+------+---------------------+--------------------------------------------------+

Details: :ref:`DroppableObject API <uvs-api-weapons--droppableobject>`.

.. _uvs-scripting-eventsreference--engine:

Engine
~~~~~~

+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments   | When it fires / meaning                                                                                                  |
+==========================+======+=============+==========================================================================================================================+
| ``ActiveGearboxChanged`` | C#   | ``Gearbox`` | Reports a change of effective gearbox identity, including removal or disable. Read ActiveGearbox when first subscribing. |
+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+
| ``EngineStateChanged``   | C#   | ``bool``    | After engine running state changes.                                                                                      |
+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+
| ``GearChanged``          | C#   | ``int``     | When Engine observes a changed gearbox gear during Step; the initial gear sample is silent.                              |
+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Engine API <uvs-api-drivedynamics--engine>`.

.. _uvs-scripting-eventsreference--eventaudio:

EventAudio
~~~~~~~~~~

+------------------+------+----------------------------+--------------------------------------------------+
| Event / callback | Kind | Arguments                  | When it fires / meaning                          |
+==================+======+============================+==================================================+
| ``Played``       | C#   | ``EffectEvent, AudioClip`` | When ``EventAudio`` plays a resolved event clip. |
+------------------+------+----------------------------+--------------------------------------------------+

Details: :ref:`EventAudio API <uvs-api-audio--eventaudio>`.

.. _uvs-scripting-eventsreference--events:

Events
~~~~~~

+------------------+------+-----------------+------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments       | When it fires / meaning                                                                              |
+==================+======+=================+======================================================================================================+
| ``Raised``       | C#   | ``EffectEvent`` | When the adapter translates a typed source notification or an integration publishes a custom effect. |
+------------------+------+-----------------+------------------------------------------------------------------------------------------------------+

Details: :ref:`Events API <uvs-api-events--events>`.

.. _uvs-scripting-eventsreference--fueltank:

FuelTank
~~~~~~~~

+------------------+------+-----------+------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                        |
+==================+======+===========+================================================================================================+
| ``Emptied``      | C#   | —         | On the transition to empty fuel.                                                               |
+------------------+------+-----------+------------------------------------------------------------------------------------------------+
| ``FuelChanged``  | C#   | ``float`` | After fuel quantity changes; the value is current litres, not the transfer amount.             |
+------------------+------+-----------+------------------------------------------------------------------------------------------------+
| ``Refuelled``    | C#   | —         | After an actual increase in fuel, including ``SetFuel``. No payload; query quantity if needed. |
+------------------+------+-----------+------------------------------------------------------------------------------------------------+

Details: :ref:`FuelTank API <uvs-api-interior--fueltank>`.

.. _uvs-scripting-eventsreference--gearbox:

Gearbox
~~~~~~~

+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+
| Event / callback   | Kind | Arguments | When it fires / meaning                                                                                |
+====================+======+===========+========================================================================================================+
| ``GearChanged``    | C#   | ``int``   | After gear selection/synchronization changes the signed gear: reverse -1, neutral 0, forward positive. |
+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+
| ``ShiftCompleted`` | C#   | ``int``   | When that shift interval completes; a zero-duration shift can complete immediately.                    |
+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+
| ``ShiftStarted``   | C#   | ``int``   | When an accepted selection starts its shift interval.                                                  |
+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+

Details: :ref:`Gearbox API <uvs-api-drivedynamics--gearbox>`.

.. _uvs-scripting-eventsreference--gearleveranimator:

GearLeverAnimator
~~~~~~~~~~~~~~~~~

+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| Event / callback    | Kind      | Arguments | When it fires / meaning                                                    |
+=====================+===========+===========+============================================================================+
| ``onGearRequested`` | Inspector | ``int``   | Accepted gear request, also available in Custom mode before motion starts. |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+

Details: :ref:`GearLeverAnimator API <uvs-api-interior--gearleveranimator>`.

.. _uvs-scripting-eventsreference--gearpaddleanimator:

GearPaddleAnimator
~~~~~~~~~~~~~~~~~~

+------------------+-----------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                                                                                                                              |
+==================+===========+===========+======================================================================================================================================================+
| ``onPressed``    | Inspector | —         | Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction. |
+------------------+-----------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`GearPaddleAnimator API <uvs-api-interior--gearpaddleanimator>`.

.. _uvs-scripting-eventsreference--handleanimatorcontroller:

HandleAnimatorController
~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+-----------+-----------+----------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                            |
+==================+===========+===========+====================================================+
| ``Cancelled``    | C#        | —         | After interruption or cancellation.                |
+------------------+-----------+-----------+----------------------------------------------------+
| ``Completed``    | C#        | —         | After successful gesture completion.               |
+------------------+-----------+-----------+----------------------------------------------------+
| ``InMove``       | C#        | —         | When the gesture reports movement.                 |
+------------------+-----------+-----------+----------------------------------------------------+
| ``Reached``      | C#        | —         | When the action commits, at most once per gesture. |
+------------------+-----------+-----------+----------------------------------------------------+
| ``Started``      | C#        | —         | After the gesture is accepted.                     |
+------------------+-----------+-----------+----------------------------------------------------+
| ``onCancelled``  | Inspector | —         | After interruption or cancellation.                |
+------------------+-----------+-----------+----------------------------------------------------+
| ``onCompleted``  | Inspector | —         | After successful gesture completion.               |
+------------------+-----------+-----------+----------------------------------------------------+
| ``onInMove``     | Inspector | —         | When the gesture reports movement.                 |
+------------------+-----------+-----------+----------------------------------------------------+
| ``onReached``    | Inspector | —         | When the action commits, at most once per gesture. |
+------------------+-----------+-----------+----------------------------------------------------+
| ``onStarted``    | Inspector | —         | After the gesture is accepted.                     |
+------------------+-----------+-----------+----------------------------------------------------+

Details: :ref:`HandleAnimatorController API <uvs-api-handles--handleanimatorcontroller>`.

.. _uvs-scripting-eventsreference--handlecontroller:

HandleController
~~~~~~~~~~~~~~~~

+------------------+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                                                                                             |
+==================+======+===============+=====================================================================================================================+
| ``Finished``     | C#   | ``HandleUse`` | After completion or cancellation has released ownership and restored any owned binding. Payload is the ended token. |
+------------------+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| ``Started``      | C#   | ``HandleUse`` | After a token owns its limb. Payload is the new token.                                                              |
+------------------+------+---------------+---------------------------------------------------------------------------------------------------------------------+

Details: :ref:`HandleController API <uvs-api-handles--handlecontroller>`.

.. _uvs-scripting-eventsreference--handleuse:

HandleUse
~~~~~~~~~

+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                                         |
+==================+======+===========+=================================================================================================================+
| ``Arrived``      | C#   | —         | After binding the destination and running the arrival callback. Persistent acquisitions do not emit this event. |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+
| ``Cancelled``    | C#   | —         | After cancellation has released ownership. An already committed action is not undone.                           |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+
| ``Completed``    | C#   | —         | After the return completes and the home binding is restored.                                                    |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+

Details: :ref:`HandleUse API <uvs-api-handles--handleuse>`.

.. _uvs-scripting-eventsreference--humanoidpassenger:

HumanoidPassenger
~~~~~~~~~~~~~~~~~

+--------------------+------+-----------------------+------------------------------------+
| Event / callback   | Kind | Arguments             | When it fires / meaning            |
+====================+======+=======================+====================================+
| ``AfterSeatedIK``  | C#   | ``HumanoidPassenger`` | Immediately after seated IK work.  |
+--------------------+------+-----------------------+------------------------------------+
| ``BeforeSeatedIK`` | C#   | ``HumanoidPassenger`` | Immediately before seated IK work. |
+--------------------+------+-----------------------+------------------------------------+

Details: :ref:`HumanoidPassenger API <uvs-api-passengercontrollers--humanoidpassenger>`.

.. _uvs-scripting-eventsreference--inputgateroute:

InputGate.Route
~~~~~~~~~~~~~~~

+------------------+-----------+-----------+--------------------------------------------------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                                                                    |
+==================+===========+===========+============================================================================================+
| ``onSelected``   | Inspector | —         | InputGate selects the route matching the active profile, after assigning its input source. |
+------------------+-----------+-----------+--------------------------------------------------------------------------------------------+

Details: :ref:`InputGate.Route API <uvs-api-input--inputgateroute>`.

.. _uvs-scripting-eventsreference--ipartmotionsource:

IPartMotionSource
~~~~~~~~~~~~~~~~~

+------------------------+------+---------------------+------------------------------------------------+
| Event / callback       | Kind | Arguments           | When it fires / meaning                        |
+========================+======+=====================+================================================+
| ``MotionAudioStopped`` | C#   | —                   | Reports the corresponding source state change. |
+------------------------+------+---------------------+------------------------------------------------+
| ``MotionOccurred``     | C#   | ``PartMotionEvent`` | Reports the corresponding source state change. |
+------------------------+------+---------------------+------------------------------------------------+

Details: :ref:`IPartMotionSource API <uvs-api-movingparts--ipartmotionsource>`.

.. _uvs-scripting-eventsreference--jetblast:

JetBlast
~~~~~~~~

+------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments              | When it fires / meaning                                                                                                 |
+==================+======+========================+=========================================================================================================================+
| ``BodyPushed``   | C#   | ``Rigidbody, Vector3`` | After force is applied to an affected body, once per outlet and physics step; payload is the body and force in newtons. |
+------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`JetBlast API <uvs-api-presentation--jetblast>`.

.. _uvs-scripting-eventsreference--landinggear:

LandingGear
~~~~~~~~~~~

+------------------+------+----------------------+----------------------------------------------------------+
| Event / callback | Kind | Arguments            | When it fires / meaning                                  |
+==================+======+======================+==========================================================+
| ``StateChanged`` | C#   | ``LandingGearState`` | When deployment sequencing changes ``LandingGearState``. |
+------------------+------+----------------------+----------------------------------------------------------+

Details: :ref:`LandingGear API <uvs-api-aircraft--landinggear>`.

.. _uvs-scripting-eventsreference--lightchannel:

LightChannel
~~~~~~~~~~~~

+------------------+------+-----------+------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                              |
+==================+======+===========+======================================================+
| ``LitChanged``   | C#   | ``bool``  | When a ``LightChannel``'s actual lit output changes. |
+------------------+------+-----------+------------------------------------------------------+

Details: :ref:`LightChannel API <uvs-api-lights--lightchannel>`.

.. _uvs-scripting-eventsreference--lights:

Lights
~~~~~~

+---------------------------+------+--------------------+------------------------------------------------+
| Event / callback          | Kind | Arguments          | When it fires / meaning                        |
+===========================+======+====================+================================================+
| ``BeamModeChanged``       | C#   | ``BeamMode``       | When requested beam mode changes.              |
+---------------------------+------+--------------------+------------------------------------------------+
| ``IndicatorPhaseChanged`` | C#   | ``bool``           | When the shared flashing output phase changes. |
+---------------------------+------+--------------------+------------------------------------------------+
| ``IndicatorsChanged``     | C#   | ``IndicatorState`` | When requested direction/hazard state changes. |
+---------------------------+------+--------------------+------------------------------------------------+

Details: :ref:`Lights API <uvs-api-lights--lights>`.

.. _uvs-scripting-eventsreference--movingpart:

MovingPart
~~~~~~~~~~

+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments           | When it fires / meaning                                                                                                |
+==========================+======+=====================+========================================================================================================================+
| ``ClosingCompleted``     | C#   | —                   | Once after the actual pose reaches the requested closing target.                                                       |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``ClosingStarted``       | C#   | —                   | Once before a closing operation moves the pose.                                                                        |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionAudioStopped``   | C#   | —                   | Requests stopping movement audio after interruption or disable.                                                        |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionEnabledChanged`` | C#   | ``bool``            | When moving-part motion availability changes.                                                                          |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionOccurred``       | C#   | ``PartMotionEvent`` | Reports an admitted movement phase to optional presentation receivers.                                                 |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``Moved``                | C#   | ``MovingPart``      | After moving-part pose changes.                                                                                        |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpeningCompleted``     | C#   | —                   | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpeningStarted``       | C#   | —                   | Once before an opening operation moves the pose. No payload; interruptions never imply completion.                     |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`MovingPart API <uvs-api-movingparts--movingpart>`.

.. _uvs-scripting-eventsreference--nitro:

Nitro
~~~~~

+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| Event / callback       | Kind | Arguments | When it fires / meaning                                                                             |
+========================+======+===========+=====================================================================================================+
| ``AmountChanged``      | C#   | ``float`` | Reports actual remaining charge after a change; payload is charge units.                            |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``BoostStateChanged``  | C#   | ``bool``  | Reports transitions into/out of resolved boost; payload is the active flag.                         |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``Depleted``           | C#   | —         | Raised once when positive charge reaches zero.                                                      |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``NitroStarted``       | C#   | —         | Effective boost begins.                                                                             |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``NitroStopped``       | C#   | —         | Effective boost ends, including reset/disable.                                                      |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``OutputStateChanged`` | C#   | ``bool``  | Reports a change of the propulsion-output session. Receivers can be absent without affecting boost. |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+

Details: :ref:`Nitro API <uvs-api-drivedynamics--nitro>`.

.. _uvs-scripting-eventsreference--objectdropper:

ObjectDropper
~~~~~~~~~~~~~

+----------------------------+------+------------------------------------+---------------------------------------------------------------------------------+
| Event / callback           | Kind | Arguments                          | When it fires / meaning                                                         |
+============================+======+====================================+=================================================================================+
| ``Dropped``                | C#   | ``ObjectDropper, DroppableObject`` | After the dropper releases a payload; includes the dropper and released object. |
+----------------------------+------+------------------------------------+---------------------------------------------------------------------------------+
| ``DroppingEnabledChanged`` | C#   | ``bool``                           | When dropper availability changes.                                              |
+----------------------------+------+------------------------------------+---------------------------------------------------------------------------------+

Details: :ref:`ObjectDropper API <uvs-api-weapons--objectdropper>`.

.. _uvs-scripting-eventsreference--partmotionevents:

PartMotionEvents
~~~~~~~~~~~~~~~~

+------------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| Event / callback       | Kind      | Arguments | When it fires / meaning                                                                                        |
+========================+===========+===========+================================================================================================================+
| ``onClosingCompleted`` | Inspector | —         | VehicleBodyPart or MovingPart reaches its closed target; follows ClosingCompleted.                             |
+------------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| ``onClosingStarted``   | Inspector | —         | VehicleBodyPart or MovingPart starts closing; follows its ClosingStarted C# event.                             |
+------------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| ``onOpeningCompleted`` | Inspector | —         | VehicleBodyPart or MovingPart reaches its open target; follows OpeningCompleted, not an interrupted operation. |
+------------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| ``onOpeningStarted``   | Inspector | —         | VehicleBodyPart or MovingPart starts opening; follows its OpeningStarted C# event.                             |
+------------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+

Details: :ref:`PartMotionEvents API <uvs-api-movingparts--partmotionevents>`.

.. _uvs-scripting-eventsreference--partmotionsignals:

PartMotionSignals
~~~~~~~~~~~~~~~~~

+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| Event / callback    | Kind      | Arguments | When it fires / meaning                                                    |
+=====================+===========+===========+============================================================================+
| ``Began``           | C#        | ``float`` | Accepted normalized operation target; a listener may cancel or replace it. |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``Cancelled``       | C#        | —         | After an operation is interrupted, replaced or cancelled.                  |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``Ended``           | C#        | —         | After successful completion; manual stop and cancellation do not raise it. |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``InputChanged``    | C#        | ``float`` | Changed signed rate demand, including zero on release.                     |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``Moved``           | C#        | ``float`` | Actual normalized progress after a pose update.                            |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``MoveRequested``   | C#        | ``float`` | Accepted normalized target request for an external movement owner.         |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``Stopped``         | C#        | —         | After successful completion, manual stop or cancellation.                  |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``StopRequested``   | C#        | —         | Explicit stop/cancel request for an external movement owner.               |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``TickRequested``   | C#        | ``float`` | Elapsed seconds during an active motion update.                            |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onBegin``         | Inspector | ``float`` | Accepted normalized operation target; a listener may cancel or replace it. |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onCancel``        | Inspector | —         | After an operation is interrupted, replaced or cancelled.                  |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onEnd``           | Inspector | —         | After successful completion; manual stop and cancellation do not raise it. |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onInputChanged``  | Inspector | ``float`` | Changed signed rate demand, including zero on release.                     |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onMove``          | Inspector | ``float`` | Actual normalized progress after a pose update.                            |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onMoveRequested`` | Inspector | ``float`` | Accepted normalized target request for an external movement owner.         |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onStop``          | Inspector | —         | After successful completion, manual stop or cancellation.                  |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onStopRequested`` | Inspector | —         | Explicit stop/cancel request for an external movement owner.               |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+
| ``onTick``          | Inspector | ``float`` | Elapsed seconds during an active motion update.                            |
+---------------------+-----------+-----------+----------------------------------------------------------------------------+

Details: :ref:`PartMotionSignals API <uvs-api-movingparts--partmotionsignals>`.

.. _uvs-scripting-eventsreference--passengeraccess:

PassengerAccess
~~~~~~~~~~~~~~~

+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Event / callback      | Kind      | Arguments                        | When it fires / meaning                                                                                             |
+=======================+===========+==================================+=====================================================================================================================+
| ``AfterEnter``        | C#        | ``PassengerSeatContext``         | After the entire entry sequence succeeds and its reservation/Target are cleared.                                    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``AfterExit``         | C#        | ``PassengerSeatContext``         | After the entire exit sequence succeeds and its reservation/Target are cleared.                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``BeforeEnter``       | C#        | ``PassengerSeatContext``         | After reservation succeeds, before collision preparation, door requests and entry motion.                           |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``BeforeExit``        | C#        | ``PassengerSeatContext``         | Before collision preparation, door requests and exit motion; occupancy is still retained.                           |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``Cancelled``         | C#        | ``PassengerSeatContext``         | After a prepared/started sequence is cancelled and reservation/Target cleared; context retains original identities. |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterBegin``        | C#        | ``PassengerSeatContext``         | Once an admitted entry starts in Opening, after Before checks; seat reservation is held.                            |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterCancelled``    | C#        | ``PassengerSeatContext``         | After a reserved entry is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing.   |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterFinished``     | C#        | ``PassengerSeatContext``         | Only after the entire entry succeeds, including the required door state and reservation/Target cleanup.             |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterInProgress``   | C#        | ``PassengerAccessProgress``      | After each entry motion sample in Moving, starting at zero; progress one is not whole-sequence completion.          |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitBegin``         | C#        | ``PassengerSeatContext``         | Once an admitted exit starts in Opening, after Before checks; seat reservation is held.                             |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitCancelled``     | C#        | ``PassengerSeatContext``         | After a reserved exit is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing.    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitFinished``      | C#        | ``PassengerSeatContext``         | Only after the entire exit succeeds, including the required door state and reservation/Target cleanup.              |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitInProgress``    | C#        | ``PassengerAccessProgress``      | After each exit motion sample in Moving, starting at zero; progress one is not whole-sequence completion.           |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``Finished``          | C#        | ``PassengerAccess, bool``        | When an access attempt ends; the bool reports success. Check occupancy after cancellation/handover.                 |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``StateChanged``      | C#        | ``PassengerAccess, AccessState`` | When access sequencing changes.                                                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onCancelled``       | Inspector | —                                | Inspector callback when access is cancelled; no payload.                                                            |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onCompleted``       | Inspector | —                                | Inspector callback when access succeeds; no payload.                                                                |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterBegin``      | Inspector | —                                | Counterpart of ``EnterBegin``; no arguments.                                                                        |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterCancelled``  | Inspector | —                                | Counterpart of ``EnterCancelled``; no arguments.                                                                    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterFinish``     | Inspector | —                                | Counterpart of ``EnterFinished``; no arguments.                                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterInProgress`` | Inspector | ``float``                        | Counterpart of ``EnterInProgress``; normalized motion time 0..1.                                                    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitBegin``       | Inspector | —                                | Counterpart of ``ExitBegin``; no arguments.                                                                         |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitCancelled``   | Inspector | —                                | Counterpart of ``ExitCancelled``; no arguments.                                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitFinish``      | Inspector | —                                | Counterpart of ``ExitFinished``; no arguments.                                                                      |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitInProgress``  | Inspector | ``float``                        | Counterpart of ``ExitInProgress``; normalized motion time 0..1.                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onStarted``         | Inspector | —                                | Inspector callback when access sequencing starts; no payload.                                                       |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+

Details: :ref:`PassengerAccess API <uvs-api-passengeraccess--passengeraccess>`.

.. _uvs-scripting-eventsreference--passengers:

Passengers
~~~~~~~~~~

+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Event / callback     | Kind      | Arguments                                             | When it fires / meaning                                                                       |
+======================+===========+=======================================================+===============================================================================================+
| ``AfterEject``       | C#        | ``PassengerSeatContext``                              | After seat ejection and its built-in velocity change.                                         |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``AfterEnter``       | C#        | ``PassengerSeatContext``                              | After successful attachment and entry notifications; carries the seat/passenger context.      |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``AfterExit``        | C#        | ``PassengerSeatContext``                              | After detachment and exit notifications; before an ejection adds its velocity change.         |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``BeforeEject``      | C#        | ``PassengerSeatContext``                              | Before a seat starts ejection detachment; occupancy is still retained.                        |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``BeforeEnter``      | C#        | ``PassengerSeatContext``                              | Forwards the validated seat entry boundary before occupancy/controller assignment.            |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``BeforeExit``       | C#        | ``PassengerSeatContext``                              | Before an occupied seat detaches its passenger, including ejection and lifecycle cleanup.     |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``Entered``          | C#        | ``PassengerSeat, PassengerBody``                      | After a body acquires a seat; includes both the seat and occupant.                            |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``Exited``           | C#        | ``PassengerSeat, PassengerBody, PassengerExitReason`` | After occupancy is released; includes seat, former occupant and exit reason.                  |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``OccupantReplaced`` | C#        | ``PassengerSeat, PassengerBody, PassengerBody``       | After presentation replacement; previous and replacement bodies, with seat on the core event. |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``onBeforeEject``    | Inspector | ``PassengerSeatContext``                              | Before any seat ejects its occupant.                                                          |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``onBeforeEnter``    | Inspector | ``PassengerSeatContext``                              | Before an occupant acquires any seat on this vehicle.                                         |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``onBeforeExit``     | Inspector | ``PassengerSeatContext``                              | Before occupancy ends on any seat, including ejection or disable.                             |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``onEjected``        | Inspector | ``PassengerSeatContext``                              | After a successful ejection, including its optional impulse.                                  |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``onEntered``        | Inspector | ``PassengerSeat, PassengerBody``                      | After an occupant acquires a seat; includes both seat and passenger.                          |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``onExited``         | Inspector | ``PassengerSeat, PassengerBody, PassengerExitReason`` | After occupancy ends; includes seat, passenger and reason.                                    |
+----------------------+-----------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------+

Details: :ref:`Passengers API <uvs-api-passengercontrollers--passengers>`.

.. _uvs-scripting-eventsreference--passengerseat:

PassengerSeat
~~~~~~~~~~~~~

+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Event / callback        | Kind      | Arguments                                                           | When it fires / meaning                                                                                    |
+=========================+===========+=====================================================================+============================================================================================================+
| ``AfterEject``          | C#        | ``PassengerSeatContext``                                            | After ejection detachment and built-in velocity change; custom controllers own their physics.              |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``AfterEnter``          | C#        | ``PassengerSeatContext``                                            | After successful attachment and Entered notifications.                                                     |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``AfterExit``           | C#        | ``PassengerSeatContext``                                            | After detachment and Exited notifications; an ejection velocity change happens afterward.                  |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``BeforeEject``         | C#        | ``PassengerSeatContext``                                            | Before ejection detaches the still-seated occupant.                                                        |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``BeforeEnter``         | C#        | ``PassengerSeatContext``                                            | After admission checks, before occupancy/controller assignment; the seat is still empty.                   |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``BeforeExit``          | C#        | ``PassengerSeatContext``                                            | Before detachment while still occupied; includes exit, ejection, disable and destruction.                  |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``BodyPartChanged``     | C#        | ``PassengerBodyPart``                                               | After a supported limb edit or individual damage-release recovery. Payload: affected hand/foot.            |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``ControllerChanged``   | C#        | ``PassengerSeat, PassengerControllerType, PassengerControllerType`` | After a successful controller handover; does not synthesize another entry or exit.                         |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``Entered``             | C#        | ``PassengerBody``                                                   | After this seat acquires its occupant.                                                                     |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``Exited``              | C#        | ``PassengerBody, PassengerExitReason``                              | After this seat releases occupancy; includes former occupant and exit reason.                              |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``OccupantReplaced``    | C#        | ``PassengerBody, PassengerBody``                                    | After presentation replacement; previous and replacement bodies, with seat on the core event.              |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``ResetRequested``      | C#        | ``PassengerBody``                                                   | When a custom occupant receives a vehicle-reset request; the application performs its reset.               |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``SpinePoseChanged``    | C#        | ``Pose``                                                            | After SetSpinePose commits the new anchor-local pose. Payload: position in metres and normalized rotation. |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onBeforeEject``       | Inspector | ``PassengerBody``                                                   | Before ejection releases occupancy or applies its impulse.                                                 |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onBeforeEnter``       | Inspector | ``PassengerBody``                                                   | Before seat occupancy is acquired. The request is validated again after observers return.                  |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onBeforeExit``        | Inspector | ``PassengerBody``                                                   | Before seat occupancy is released, including ejection and disable paths.                                   |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onControllerChanged`` | Inspector | ``PassengerControllerType``                                         | After the seat switches to a different passenger controller.                                               |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onEjected``           | Inspector | ``PassengerBody``                                                   | After successful ejection and its optional impulse.                                                        |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onEntered``           | Inspector | ``PassengerBody``                                                   | After the passenger acquires this seat.                                                                    |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onExited``            | Inspector | ``PassengerBody, PassengerExitReason``                              | After occupancy ends. Includes the released passenger and the exit reason.                                 |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onFeetReleased``      | Inspector | ``PassengerBody``                                                   | Once when both feet have entered the damage-released state.                                                |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onHandsReleased``     | Inspector | ``PassengerBody``                                                   | Once when both hands have entered the damage-released state.                                               |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onLimbReleased``      | Inspector | ``PassengerBodyPart``                                               | Invoked once when an individual hand or foot enters damage-released state.                                 |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``onResetRequested``    | Inspector | ``PassengerBody``                                                   | When a custom occupant is asked to reset its seated pose.                                                  |
+-------------------------+-----------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Details: :ref:`PassengerSeat API <uvs-api-passengercontrollers--passengerseat>`.

.. _uvs-scripting-eventsreference--passengervariants:

PassengerVariants
~~~~~~~~~~~~~~~~~

+--------------------+------+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event              | Kind | Arguments                              | Meaning                                                                                                                                                                                                           |
+====================+======+========================================+===================================================================================================================================================================================================================+
| ``VariantChanged`` | C#   | ``PassengerVariant, PassengerVariant`` | After a successful presentation commit. Payload: previous and current variant; null denotes the original. A variant-owned exit also reports returning to the original policy, without respawning its parked body. |
+--------------------+------+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-eventsreference--pedalanimator:

PedalAnimator
~~~~~~~~~~~~~

+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+
| Event / callback   | Kind      | Arguments | When it fires / meaning                                                                |
+====================+===========+===========+========================================================================================+
| ``onValueChanged`` | Inspector | ``float`` | After displayed pedal travel changes (0–1), including immediate positioning and reset. |
+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+

Details: :ref:`PedalAnimator API <uvs-api-interior--pedalanimator>`.

.. _uvs-scripting-eventsreference--profileswitcher:

ProfileSwitcher
~~~~~~~~~~~~~~~

+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| Event / callback           | Kind      | Arguments                             | When it fires / meaning                                                                          |
+============================+===========+=======================================+==================================================================================================+
| ``ProfileChanged``         | C#        | ``DriveProfile``                      | After configuring an accepted target profile; an animated transition may still be in progress.   |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``ProfilesChanged``        | C#        | —                                     | After successful registration, removal or list replacement. Does not imply a strategy change.    |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionAudioStopped`` | C#        | —                                     | Requests stopping transition presentation.                                                       |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionBegan``        | C#        | ``ProfileTransition, string, string`` | Admitted transition component, source profile ID and destination profile ID.                     |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionCompleted``    | C#        | —                                     | After animated transition completion, contact restoration and final presentation.                |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionInterrupted``  | C#        | —                                     | On disable during a transition, after finalizing the selected target and presentation.           |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionProgressed``   | C#        | ``float``                             | During animation, with normalized progress.                                                      |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionStarted``      | C#        | —                                     | After target configuration and animated-route initialization; immediate switches do not emit it. |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``onCompleted``            | Inspector | —                                     | Inspector callback after animated route completion.                                              |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``onProgressed``           | Inspector | ``float``                             | Inspector callback with normalized animation progress.                                           |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``onStarted``              | Inspector | —                                     | Inspector callback when an animated route starts.                                                |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+

Details: :ref:`ProfileSwitcher API <uvs-api-driveprofiles--profileswitcher>`.

.. _uvs-scripting-eventsreference--propulsion:

Propulsion
~~~~~~~~~~

+------------------+------+-----------+-------------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                                                 |
+==================+======+===========+=========================================================================================================================+
| ``SpeedChanged`` | C#   | ``float`` | When visual propulsion spool changes (0 stopped to 1 full speed); not RPM, mechanical thrust or individual shaft speed. |
+------------------+------+-----------+-------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Propulsion API <uvs-api-aircraft--propulsion>`.

.. _uvs-scripting-eventsreference--propulsionjets:

PropulsionJets
~~~~~~~~~~~~~~

+------------------------+------+-----------+---------------------------------------------+
| Event / callback       | Kind | Arguments | When it fires / meaning                     |
+========================+======+===========+=============================================+
| ``JetsEnabledChanged`` | C#   | ``bool``  | When jet presentation availability changes. |
+------------------------+------+-----------+---------------------------------------------+

Details: :ref:`PropulsionJets API <uvs-api-presentation--propulsionjets>`.

.. _uvs-scripting-eventsreference--rearmirrors:

RearMirrors
~~~~~~~~~~~

+---------------------------+------+---------------+-----------------------------------------------+
| Event / callback          | Kind | Arguments     | When it fires / meaning                       |
+===========================+======+===============+===============================================+
| ``MirrorEnabledChanged``  | C#   | ``int, bool`` | When one mirror's eligibility changes.        |
+---------------------------+------+---------------+-----------------------------------------------+
| ``MirrorsEnabledChanged`` | C#   | ``bool``      | When whole-system mirror eligibility changes. |
+---------------------------+------+---------------+-----------------------------------------------+

Details: :ref:`RearMirrors API <uvs-api-interior--rearmirrors>`.

.. _uvs-scripting-eventsreference--rideranimationrule:

RiderAnimationRule
~~~~~~~~~~~~~~~~~~

+------------------+-----------+-----------+-------------------------------------------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                                                             |
+==================+===========+===========+=====================================================================================+
| ``onEntered``    | Inspector | —         | Condition began, including angle-range transitions. Can call custom animation code. |
+------------------+-----------+-----------+-------------------------------------------------------------------------------------+
| ``onExited``     | Inspector | —         | Condition ended or the occupant/binding was released.                               |
+------------------+-----------+-----------+-------------------------------------------------------------------------------------+

Details: :ref:`RiderAnimationRule API <uvs-api-passengercontrollers--rideranimationrule>`.

.. _uvs-scripting-eventsreference--rocket:

Rocket
~~~~~~

+------------------+------+---------------------+-------------------------------------+
| Event / callback | Kind | Arguments           | When it fires / meaning             |
+==================+======+=====================+=====================================+
| ``Exploded``     | C#   | ``Rocket, Vector3`` | At the rocket's explosion boundary. |
+------------------+------+---------------------+-------------------------------------+

Details: :ref:`Rocket API <uvs-api-weapons--rocket>`.

.. _uvs-scripting-eventsreference--rocketlauncher:

RocketLauncher
~~~~~~~~~~~~~~

+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments                  | When it fires / meaning                                                            |
+==========================+======+============================+====================================================================================+
| ``Fired``                | C#   | ``RocketLauncher, Rocket`` | After an admitted shot launches a rocket; holding the trigger alone is not a shot. |
+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+
| ``FiringEnabledChanged`` | C#   | ``bool``                   | When weapon firing availability changes.                                           |
+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+
| ``TriggerChanged``       | C#   | ``bool``                   | When held trigger intent changes.                                                  |
+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+

Details: :ref:`RocketLauncher API <uvs-api-weapons--rocketlauncher>`.

.. _uvs-scripting-eventsreference--rotaryanimator:

RotaryAnimator
~~~~~~~~~~~~~~

+--------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------------------+
| Event / callback   | Kind      | Arguments | When it fires / meaning                                                                                             |
+====================+===========+===========+=====================================================================================================================+
| ``ValueChanged``   | C#        | ``float`` | When SetValue changes the requested value in configured units; does not wait for visible rotation to settle.        |
+--------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged`` | Inspector | ``float`` | After the requested rotary value changes, in configured units; follows ValueChanged and does not wait for settling. |
+--------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------------------+

Details: :ref:`RotaryAnimator API <uvs-api-interior--rotaryanimator>`.

.. _uvs-scripting-eventsreference--seataccess:

SeatAccess
~~~~~~~~~~

+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| Event / callback      | Kind      | Arguments | When it fires / meaning                                                                            |
+=======================+===========+===========+====================================================================================================+
| ``onEnterBegin``      | Inspector | —         | Invoked when an admitted enter operation begins for this access path.                              |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| ``onEnterCancelled``  | Inspector | —         | Invoked when a reserved enter operation is cancelled or fails. Rejected requests do not invoke it. |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| ``onEnterFinish``     | Inspector | —         | Invoked after the entire enter operation succeeds, including door cleanup.                         |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| ``onEnterInProgress`` | Inspector | ``float`` | Normalized enter motion progress (0..1). One does not imply door cleanup has finished.             |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| ``onExitBegin``       | Inspector | —         | Invoked when an admitted exit operation begins for this access path.                               |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| ``onExitCancelled``   | Inspector | —         | Invoked when a reserved exit operation is cancelled or fails. Rejected requests do not invoke it.  |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| ``onExitFinish``      | Inspector | —         | Invoked after the entire exit operation succeeds, including door cleanup.                          |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+
| ``onExitInProgress``  | Inspector | ``float`` | Normalized exit motion progress (0..1). One does not imply door cleanup has finished.              |
+-----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------+

Details: :ref:`SeatAccess API <uvs-api-passengeraccess--seataccess>`.

.. _uvs-scripting-eventsreference--skidmarks:

Skidmarks
~~~~~~~~~

================ ==== ========= ==================================
Event / callback Kind Arguments When it fires / meaning
================ ==== ========= ==================================
``Cleared``      C#   —         After skidmark history is cleared.
================ ==== ========= ==================================

Details: :ref:`Skidmarks API <uvs-api-presentation--skidmarks>`.

.. _uvs-scripting-eventsreference--stabilization:

Stabilization
~~~~~~~~~~~~~

+------------------+------+---------------+--------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                                                                                      |
+==================+======+===============+==============================================================================================================+
| ``Overturned``   | C#   | ``Telemetry`` | Raised once when sustained tilt qualifies; carries the telemetry snapshot at that transition.                |
+------------------+------+---------------+--------------------------------------------------------------------------------------------------------------+
| ``Recovered``    | C#   | ``Telemetry`` | Raised once when tilt falls below the recovery threshold; carries the telemetry snapshot at that transition. |
+------------------+------+---------------+--------------------------------------------------------------------------------------------------------------+

Details: :ref:`Stabilization API <uvs-api-collisionsandstabilization--stabilization>`.

.. _uvs-scripting-eventsreference--steering:

Steering
~~~~~~~~

+------------------+------+-----------+---------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                               |
+==================+======+===========+=======================================================================================+
| ``AngleChanged`` | C#   | ``float`` | When the resolved road-wheel angle changes, in degrees (not steering-column degrees). |
+------------------+------+-----------+---------------------------------------------------------------------------------------+

Details: :ref:`Steering API <uvs-api-drivedynamics--steering>`.

.. _uvs-scripting-eventsreference--suspension:

Suspension
~~~~~~~~~~

+----------------------+------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback     | Kind | Arguments        | When it fires / meaning                                                                                                                                                         |
+======================+======+==================+=================================================================================================================================================================================+
| ``Landed``           | C#   | ``LandingEvent`` | First upright wheel support after qualifying flight. Context includes height, air time, speed and impact data; assisted rebounds are marked. Independent of landing assistance. |
+----------------------+------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``LandingCompleted`` | C#   | ``LandingEvent`` | First support from all operational wheel rays after Landed; may be the same step. This does not mean suspension motion has settled.                                             |
+----------------------+------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Suspension API <uvs-api-suspension--suspension>`.

.. _uvs-scripting-eventsreference--switchanimator:

SwitchAnimator
~~~~~~~~~~~~~~

+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback      | Kind      | Arguments          | When it fires / meaning                                                                                                                         |
+=======================+===========+====================+=================================================================================================================================================+
| ``PositionChanged``   | C#        | ``SwitchPosition`` | When the requested detent changes; distinguishes all three positions.                                                                           |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PositionReached``   | C#        | ``SwitchPosition`` | When motion settles at the requested detent.                                                                                                    |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Switched``          | C#        | ``bool``           | When motion settles; both negative and positive detents report true.                                                                            |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ValueChanged``      | C#        | ``bool``           | When requested IsOn changes; negative and positive detents both count as on. Immediate synchronization is silent.                               |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onPositionChanged`` | Inspector | ``SwitchPosition`` | After a changed detent request, following PositionChanged; immediate synchronization is silent.                                                 |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged``    | Inspector | ``bool``           | After the binary IsOn request changes, following ValueChanged. Negative/positive detents both count as on; immediate synchronization is silent. |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`SwitchAnimator API <uvs-api-interior--switchanimator>`.

.. _uvs-scripting-eventsreference--throttleanimator:

ThrottleAnimator
~~~~~~~~~~~~~~~~

+------------------+------+-----------+-----------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                       |
+==================+======+===========+===============================================================================================+
| ``ValueChanged`` | C#   | ``float`` | When the displayed throttle value changes during Step, including smoothing toward its target. |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------+

Details: :ref:`ThrottleAnimator API <uvs-api-interior--throttleanimator>`.

.. _uvs-scripting-eventsreference--tirefeedback:

TireFeedback
~~~~~~~~~~~~

+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments                   | When it fires / meaning                                                                                                |
+==========================+======+=============================+========================================================================================================================+
| ``Sampled``              | C#   | —                           | After TireFeedback updates its wheel/contact classification. No payload; read the component's current cached feedback. |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``SkiddingChanged``      | C#   | ``bool``                    | When aggregate feedback skid state changes.                                                                            |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``WheelGroundedChanged`` | C#   | ``int, bool``               | When feedback grounded state changes; arguments are wheel index and the new state.                                     |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``WheelSurfaceChanged``  | C#   | ``int, TireSurfaceProfile`` | When a wheel selects a different presentation surface; its profile can be null.                                        |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`TireFeedback API <uvs-api-events--tirefeedback>`.

.. _uvs-scripting-eventsreference--tiresmoke:

TireSmoke
~~~~~~~~~

+-------------------------+------+-------------------+--------------------------------------------------------+
| Event / callback        | Kind | Arguments         | When it fires / meaning                                |
+=========================+======+===================+========================================================+
| ``SmokeModeChanged``    | C#   | ``TireSmokeMode`` | After the smoke presentation mode changes.             |
+-------------------------+------+-------------------+--------------------------------------------------------+
| ``WheelBurnoutChanged`` | C#   | ``int, bool``     | When indexed wheel burnout-smoke presentation changes. |
+-------------------------+------+-------------------+--------------------------------------------------------+

Details: :ref:`TireSmoke API <uvs-api-presentation--tiresmoke>`.

.. _uvs-scripting-eventsreference--tractioncontrol:

TractionControl
~~~~~~~~~~~~~~~

+-------------------+------+-----------+------------------------------------------------------------------------------+
| Event / callback  | Kind | Arguments | When it fires / meaning                                                      |
+===================+======+===========+==============================================================================+
| ``ActiveChanged`` | C#   | ``bool``  | When resolved traction-control intervention changes between active/inactive. |
+-------------------+------+-----------+------------------------------------------------------------------------------+

Details: :ref:`TractionControl API <uvs-api-drivedynamics--tractioncontrol>`.

.. _uvs-scripting-eventsreference--trailer:

Trailer
~~~~~~~

+----------------------+------+-----------+----------------------------------------------------+
| Event / callback     | Kind | Arguments | When it fires / meaning                            |
+======================+======+===========+====================================================+
| ``ConnectionBroken`` | C#   | —         | When a trailer's active hitch relationship breaks. |
+----------------------+------+-----------+----------------------------------------------------+

Details: :ref:`Trailer API <uvs-api-towing--trailer>`.

.. _uvs-scripting-eventsreference--transmission:

Transmission
~~~~~~~~~~~~

+------------------+------+----------------------+------------------------------------------------------------------------+
| Event / callback | Kind | Arguments            | When it fires / meaning                                                |
+==================+======+======================+========================================================================+
| ``ModeChanged``  | C#   | ``TransmissionMode`` | After transmission mode changes and its gearbox connection is applied. |
+------------------+------+----------------------+------------------------------------------------------------------------+

Details: :ref:`Transmission API <uvs-api-drivedynamics--transmission>`.

.. _uvs-scripting-eventsreference--vehiclebodypart:

VehicleBodyPart
~~~~~~~~~~~~~~~

+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| Event / callback       | Kind | Arguments           | When it fires / meaning                                                                                                |
+========================+======+=====================+========================================================================================================================+
| ``ClosingCompleted``   | C#   | —                   | Once after the actual pose reaches the requested closing target.                                                       |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``ClosingStarted``     | C#   | —                   | Once before a closing operation moves the pose.                                                                        |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionAudioStopped`` | C#   | —                   | Requests stopping movement audio after interruption or disable.                                                        |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionOccurred``     | C#   | ``PartMotionEvent`` | Reports an admitted movement phase to optional presentation receivers.                                                 |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpenChanged``        | C#   | ``bool``            | When the part's requested open state changes.                                                                          |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpeningCompleted``   | C#   | —                   | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpeningStarted``     | C#   | —                   | Once before an opening operation moves the pose. No payload; interruptions never imply completion.                     |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``PhysicsChanged``     | C#   | ``bool``            | When the part's ``usePhysics`` policy changes.                                                                         |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``Released``           | C#   | —                   | After the body part is released from vehicle-owned motion.                                                             |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleBodyPart API <uvs-api-damage--vehiclebodypart>`.

.. _uvs-scripting-eventsreference--vehiclecargo:

VehicleCargo
~~~~~~~~~~~~

+----------------------+------+--------------------------+------------------------------------------------------------+
| Event                | Kind | Arguments                | Meaning                                                    |
+======================+======+==========================+============================================================+
| ``AttachmentBroken`` | C#   | ``CargoAttachmentBreak`` | After a manual or threshold break commits Free cargo mode. |
+----------------------+------+--------------------------+------------------------------------------------------------+
| ``ModeChanged``      | C#   | ``VehicleCargoMode``     | After an active cargo-mode transition.                     |
+----------------------+------+--------------------------+------------------------------------------------------------+
| ``Released``         | C#   | ``VehicleController``    | After ownership is cleared; carries the former vehicle.    |
+----------------------+------+--------------------------+------------------------------------------------------------+

.. _uvs-scripting-eventsreference--vehiclecontroller:

VehicleController
~~~~~~~~~~~~~~~~~

+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| Event / callback             | Kind | Arguments         | When it fires / meaning                                                                                     |
+==============================+======+===================+=============================================================================================================+
| ``AfterPhysicsStep``         | C#   | ``Telemetry``     | After the module pipeline and telemetry sampling; this is not a callback after native Physics.Simulate.     |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``Collided``                 | C#   | ``Collision``     | During Unity collision entry; Collision is live callback data, so copy values before deferring work.        |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``CommandSampled``           | C#   | ``Command``       | After the selected provider is sampled.                                                                     |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``ConfigurationChanged``     | C#   | —                 | After validated wheel/module configuration is applied.                                                      |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``ContactPersisted``         | C#   | ``Collision``     | During sustained native contact; copy values before retaining or deferring them.                            |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``DriveProfileChanged``      | C#   | ``DriveProfile``  | After an immediate profile change is configured successfully.                                               |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``Impacted``                 | C#   | ``Impact``        | After copying collision contact/velocity/impulse data; the Impact snapshot can be retained.                 |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``InputSourceChanged``       | C#   | ``MonoBehaviour`` | After assigning input ownership.                                                                            |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``ModuleRegistered``         | C#   | ``VehicleModule`` | After registration/configuration.                                                                           |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``ModuleUnregistered``       | C#   | ``VehicleModule`` | After removal from future pipeline membership; independent callbacks may still need disabling.              |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``Repaired``                 | C#   | —                 | After RepairAll finishes in-place repair and actuator cleanup; Teleport alone does not emit it.             |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``Teleported``               | C#   | ``Pose``          | After world pose and occupants have been synchronized.                                                      |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``WheelAttachmentChanged``   | C#   | ``Wheel, bool``   | Forwards an owned Wheel attachment change after its per-wheel notification; bool is the new attached state. |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``WheelAvailabilityChanged`` | C#   | ``int, bool``     | After a wheel availability change; arguments are configured wheel index and new availability.               |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleController API <uvs-api-core--vehiclecontroller>`.

.. _uvs-scripting-eventsreference--vehiclehandle:

VehicleHandle
~~~~~~~~~~~~~

+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind      | Arguments                | When it fires / meaning                                                                                                         |
+==========================+===========+==========================+=================================================================================================================================+
| ``ContactEnded``         | C#        | ``HandleContactContext`` | Once when contact is lost or released (including exit/disable/rebinding). Payload retains the original occupant identity.       |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ContactStarted``       | C#        | ``HandleContactContext`` | Once on a not-touching to touching transition; C# event runs before the matching UnityEvent.                                    |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ContactUpdated``       | C#        | ``HandleContactContext`` | Once per contact sample while touching, including its start sample. Payload identifies handle, seat, occupant, part and target. |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ControlModeChanged``   | C#        | ``HandleControlMode``    | After this handle changes its control mode and cancels the previous mode’s active requests.                                     |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ValueChangeStarted``   | C#        | ``HandleValueContext``   | Once when a significant value change or explicit BeginValueChange starts activity.                                              |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ValueChangeStopped``   | C#        | ``HandleValueContext``   | Once when the value settles for valueStopDelay, explicit EndValueChange runs or the handle is disabled/destroyed.               |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ValueChanging``        | C#        | ``HandleValueContext``   | Each active changed/manual sample; does not imply contact or commit a gameplay action.                                          |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onContactEnded``       | Inspector | ``HandleContactContext`` | Inspector-configurable counterpart of ContactEnded. Runs after the C# event for the same phase.                                 |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onContactStarted``     | Inspector | ``HandleContactContext`` | Inspector-configurable counterpart of ContactStarted. Runs after the C# event for the same phase.                               |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onContactUpdated``     | Inspector | ``HandleContactContext`` | Inspector-configurable counterpart of ContactUpdated. Runs after the C# event for the same phase.                               |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChangeStarted`` | Inspector | ``HandleValueContext``   | Inspector-configurable counterpart of ValueChangeStarted. Runs after the C# event for the same phase.                           |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChangeStopped`` | Inspector | ``HandleValueContext``   | Inspector-configurable counterpart of ValueChangeStopped. Runs after the C# event for the same phase.                           |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanging``      | Inspector | ``HandleValueContext``   | Inspector-configurable counterpart of ValueChanging. Runs after the C# event for the same phase.                                |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleHandle API <uvs-api-handles--vehiclehandle>`.

.. _uvs-scripting-eventsreference--vehiclemeshdeformation:

VehicleMeshDeformation
~~~~~~~~~~~~~~~~~~~~~~

+------------------------+------+-----------+------------------------------------------------------------------------------------------------------+
| Event / callback       | Kind | Arguments | When it fires / meaning                                                                              |
+========================+======+===========+======================================================================================================+
| ``DeformationChanged`` | C#   | —         | After pending deformation geometry is uploaded. No payload; inspect owned geometry at this boundary. |
+------------------------+------+-----------+------------------------------------------------------------------------------------------------------+
| ``Restored``           | C#   | —         | After deformable shape is restored to rest geometry.                                                 |
+------------------------+------+-----------+------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleMeshDeformation API <uvs-api-damage--vehiclemeshdeformation>`.

.. _uvs-scripting-eventsreference--vehiclemodule:

VehicleModule
~~~~~~~~~~~~~

+--------------------+------+---------------------------------------+-----------------------------------------------+
| Event / callback   | Kind | Arguments                             | When it fires / meaning                       |
+====================+======+=======================================+===============================================+
| ``Configured``     | C#   | ``VehicleController``                 | After controller-driven module configuration. |
+--------------------+------+---------------------------------------+-----------------------------------------------+
| ``EnabledChanged`` | C#   | ``bool``                              | After ``SetEnabled`` changes the module flag. |
+--------------------+------+---------------------------------------+-----------------------------------------------+
| ``Stepped``        | C#   | ``VehicleController, Command, float`` | After this registered module has stepped.     |
+--------------------+------+---------------------------------------+-----------------------------------------------+

Details: :ref:`VehicleModule API <uvs-api-modules--vehiclemodule>`.

.. _uvs-scripting-eventsreference--waterinteraction:

WaterInteraction
~~~~~~~~~~~~~~~~

+-------------------------------+------+-------------------+----------------------------------------------------------------------------+
| Event / callback              | Kind | Arguments         | When it fires / meaning                                                    |
+===============================+======+===================+============================================================================+
| ``InteractionEnabledChanged`` | C#   | ``bool``          | When the master water-interaction gate changes.                            |
+-------------------------------+------+-------------------+----------------------------------------------------------------------------+
| ``ProviderChanged``           | C#   | ``WaterProvider`` | When the assigned water provider changes; null means no assigned provider. |
+-------------------------------+------+-------------------+----------------------------------------------------------------------------+
| ``SubmergedChanged``          | C#   | ``bool``          | When sampled body-center submergence changes.                              |
+-------------------------------+------+-------------------+----------------------------------------------------------------------------+

Details: :ref:`WaterInteraction API <uvs-api-water--waterinteraction>`.

.. _uvs-scripting-eventsreference--weaponbarrel:

WeaponBarrel
~~~~~~~~~~~~

+--------------------------+------+---------------------------------+------------------------------------------------------------------+
| Event / callback         | Kind | Arguments                       | When it fires / meaning                                          |
+==========================+======+=================================+==================================================================+
| ``Fired``                | C#   | ``WeaponBarrel, MonoBehaviour`` | After an admitted shot creates/releases its projectile or store. |
+--------------------------+------+---------------------------------+------------------------------------------------------------------+
| ``FiringEnabledChanged`` | C#   | ``bool``                        | When weapon firing availability changes.                         |
+--------------------------+------+---------------------------------+------------------------------------------------------------------+
| ``TriggerChanged``       | C#   | ``bool``                        | When held trigger intent changes.                                |
+--------------------------+------+---------------------------------+------------------------------------------------------------------+

Details: :ref:`WeaponBarrel API <uvs-api-weapons--weaponbarrel>`.

.. _uvs-scripting-eventsreference--wheel:

Wheel
~~~~~

+-----------------------+------+-----------------+---------------------------------------------------------------------------------------------------+
| Event / callback      | Kind | Arguments       | When it fires / meaning                                                                           |
+=======================+======+=================+===================================================================================================+
| ``AttachmentChanged`` | C#   | ``Wheel, bool`` | After attachment state and collider/actuator availability update; bool is the new attached state. |
+-----------------------+------+-----------------+---------------------------------------------------------------------------------------------------+

Details: :ref:`Wheel API <uvs-api-wheelcontact--wheel>`.

.. _uvs-scripting-eventsreference--wheellift:

WheelLift
~~~~~~~~~

+----------------------+------+-----------+--------------------------------------------------------------------------------------------+
| Event / callback     | Kind | Arguments | When it fires / meaning                                                                    |
+======================+======+===========+============================================================================================+
| ``StateChanged``     | C#   | ``bool``  | New assistance state.                                                                      |
+----------------------+------+-----------+--------------------------------------------------------------------------------------------+
| ``WheelLiftStarted`` | C#   | —         | Assistance begins.                                                                         |
+----------------------+------+-----------+--------------------------------------------------------------------------------------------+
| ``WheelLiftStopped`` | C#   | —         | Assistance ends after controlled lowering, or immediately on reset/disable/excessive tilt. |
+----------------------+------+-----------+--------------------------------------------------------------------------------------------+

Details: :ref:`WheelLift API <uvs-api-wheellift--wheellift>`.

.. _uvs-scripting-eventsreference--wipers:

Wipers
~~~~~~

+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments              | When it fires / meaning                                                                                           |
+==========================+======+========================+===================================================================================================================+
| ``AudioStopped``         | C#   | —                      | Requests stopping wiper audio.                                                                                    |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``Parked``               | C#   | —                      | When wipers reach their parked state.                                                                             |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``RunningChanged``       | C#   | ``bool``               | When the wiper running request changes.                                                                           |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``SpeedChanged``         | C#   | ``float``              | After ``SetSpeed`` changes requested wiper speed.                                                                 |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``StrokeAudioRequested`` | C#   | ``Wiper, bool, float`` | Specific wiper, stroke direction and resolved cycles per minute for optional audio.                               |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``StrokeBatchStarted``   | C#   | —                      | Begins a mechanism tick; receivers can deduplicate shared voices within this batch.                               |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``StrokeStarted``        | C#   | ``bool``               | When a wiper stroke starts.                                                                                       |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperParked``          | C#   | ``string``             | When an entry reaches/is immediately placed at its parked pose; payload is its ID.                                |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperRemoved``         | C#   | ``Wiper``              | Reports an entry removed from the mechanism so optional receivers can release its resources.                      |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperRunningChanged``  | C#   | ``string, bool``       | After an API changes an entry's effective running request; payload is its ID and new bool request.                |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperSpeedChanged``    | C#   | ``string, float``      | After an API changes an entry's effective speed; payload is its ID and cycles per minute.                         |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperStrokeStarted``   | C#   | ``string, bool``       | Reports entry ID and stroke direction: false for outward, true for return. Entries have independent phase clocks. |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Wipers API <uvs-api-wipers--wipers>`.

.. _uvs-scripting-eventsreference--demo-and-example-classes:

Demo and example classes
------------------------

.. _uvs-scripting-eventsreference--camerarigdemo:

CameraRigDemo
~~~~~~~~~~~~~

+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind     | Arguments          | When it fires / meaning                                                                                                                             |
+==========================+==========+====================+=====================================================================================================================================================+
| ``ModeChanged``          | C#       | ``ViewMode``       | After a changed camera view mode is applied.                                                                                                        |
+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PointerCaptureFilter`` | C# query | ``Vector2 → bool`` | CanCaptureAt checks a screen position. Every invoked filter must allow capture; the first false vetoes it. This is not a state-change notification. |
+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``TargetChanged``        | C#       | ``Transform``      | After retargeting the demo camera; null releases the target.                                                                                        |
+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-eventsreference--projectiledemo:

ProjectileDemo
~~~~~~~~~~~~~~

+------------------+------+--------------------------------------+-----------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments                            | When it fires / meaning                                                                             |
+==================+======+======================================+=====================================================================================================+
| ``Impacted``     | C#   | ``ProjectileDemo, ProjectileImpact`` | Once on an accepted collision, after copying impact data and before application-owned hit handling. |
+------------------+------+--------------------------------------+-----------------------------------------------------------------------------------------------------+

.. _uvs-scripting-eventsreference--vehicleselectordemo:

VehicleSelectorDemo
~~~~~~~~~~~~~~~~~~~

+------------------+------+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments             | When it fires / meaning                                                                                          |
+==================+======+=======================+==================================================================================================================+
| ``Selected``     | C#   | ``VehicleController`` | After a valid selection updates input routing, camera target and HUD; selecting the same index can notify again. |
+------------------+------+-----------------------+------------------------------------------------------------------------------------------------------------------+
