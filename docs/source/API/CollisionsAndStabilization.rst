.. _uvs-api-collisionsandstabilization--collisions-and-stabilization-api:

Collisions and stabilization API
================================

.. _uvs-api-collisionsandstabilization--types:

Types
-----

-  :ref:`CargoAttachmentAxes <uvs-api-collisionsandstabilization--cargoattachmentaxes>`
-  :ref:`CargoAttachmentBreak <uvs-api-collisionsandstabilization--cargoattachmentbreak>`
-  :ref:`CargoAttachmentBreakReason <uvs-api-collisionsandstabilization--cargoattachmentbreakreason>`
-  :ref:`CargoAttachmentSettings <uvs-api-collisionsandstabilization--cargoattachmentsettings>`
-  :ref:`CargoCollisionExclusions <uvs-api-collisionsandstabilization--cargocollisionexclusions>`
-  :ref:`CargoCollisionSettings <uvs-api-collisionsandstabilization--cargocollisionsettings>`
-  :ref:`Collisions <uvs-api-collisionsandstabilization--collisions>`
-  :ref:`DynamicObstacle <uvs-api-collisionsandstabilization--dynamicobstacle>`
-  :ref:`Stabilization <uvs-api-collisionsandstabilization--stabilization>`
-  :ref:`VehicleCargo <uvs-api-collisionsandstabilization--vehiclecargo>`
-  :ref:`VehicleCargoMode <uvs-api-collisionsandstabilization--vehiclecargomode>`
-  :ref:`VehicleCollisionHandler <uvs-api-collisionsandstabilization--vehiclecollisionhandler>`
-  :ref:`VehicleCollisionHooks <uvs-api-collisionsandstabilization--vehiclecollisionhooks>`

.. _uvs-api-collisionsandstabilization--cargoattachmentaxes:

CargoAttachmentAxes
-------------------

**Runtime/World/Cargo/Settings/CargoAttachmentSettings.cs**

Flags selecting axes in the attachment frame. Linear axes apply to Spring; angular axes apply when Align Rotation is enabled.

-  ``None = 0``
-  ``X = 1``
-  ``Y = 2``
-  ``Z = 4``
-  ``All = X | Y | Z``

.. _uvs-api-collisionsandstabilization--cargoattachmentbreak:

CargoAttachmentBreak
--------------------

**Runtime/World/Cargo/Settings/CargoAttachmentSettings.cs**

Copied break notification. Reported after mode becomes Dynamic and optional ownership release completes. Force/torque are requested values before caps; distance is point-to-target separation.

.. _uvs-api-collisionsandstabilization--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+---------------------------------------------------------------+
| Member                                                | Meaning                                                       |
+=======================================================+===============================================================+
| ``public readonly VehicleCargo Cargo``                | Cargo helper that broke its attachment.                       |
+-------------------------------------------------------+---------------------------------------------------------------+
| ``public readonly float Distance``                    | Point-to-target separation at the break, in metres.           |
+-------------------------------------------------------+---------------------------------------------------------------+
| ``public readonly Vector3 Force``                     | Requested world-space force before the force cap, in newtons. |
+-------------------------------------------------------+---------------------------------------------------------------+
| ``public readonly VehicleCargoMode Mode``             | Attachment mode before breaking.                              |
+-------------------------------------------------------+---------------------------------------------------------------+
| ``public readonly CargoAttachmentBreakReason Reason`` | Condition that broke the attachment.                          |
+-------------------------------------------------------+---------------------------------------------------------------+
| ``public readonly Vector3 Torque``                    | Requested world-space torque before the torque cap, in N*m.   |
+-------------------------------------------------------+---------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--methods:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+--------------------------------------------------------------------------------+
| Signature                                                                                                                                                    | Role and behavior                       | Arguments and result                                                           |
+==============================================================================================================================================================+=========================================+================================================================================+
| ``public CargoAttachmentBreak(VehicleCargo cargo, VehicleCargoMode mode, CargoAttachmentBreakReason reason, Vector3 force, Vector3 torque, float distance)`` | Constructs the immutable break context. | cargo, prior mode, reason, requested world force/torque, separation in metres. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+--------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--cargoattachmentbreakreason:

CargoAttachmentBreakReason
--------------------------

**Runtime/World/Cargo/Settings/CargoAttachmentSettings.cs**

Manual API release or the first enabled distance, force or torque break condition.

-  ``Manual``
-  ``Distance``
-  ``Force``
-  ``Torque``

.. _uvs-api-collisionsandstabilization--cargoattachmentsettings:

CargoAttachmentSettings
-----------------------

**Runtime/World/Cargo/Settings/CargoAttachmentSettings.cs**

Attachment-frame, elastic-force, slack-rope and break tuning. Ignored for Free simulation. Secured is kinematic and follows rotation directly; force/torque limits and force/torque breaks apply to Spring/Tethered. Distance break also applies to Secured. No mode introduces world-upright correction.

.. _uvs-api-collisionsandstabilization--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                     | Meaning                                                                                                                                                                         |
+============================================+=================================================================================================================================================================================+
| ``public bool alignRotation``              | Optional rotational spring for Spring/Tethered. Off allows free tumbling; it never aligns cargo to world up. Secured always follows the target rotation.                        |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform anchor``                | Optional attachment frame. Empty uses the captured placement on the carrier, or the captured world pose without a carrier. Never used to attract free cargo.                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 anchorOffset``            | Target point offset in the anchor's local axes. Without an anchor, offsets the captured placement.                                                                              |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public CargoAttachmentAxes angularAxes`` | Rotational spring axes in the target frame; used only with Align Rotation.                                                                                                      |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float angularDamper``             | Relative angular-velocity damping in N\ *m*\ s/radian.                                                                                                                          |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float angularSpring``             | Rotational spring stiffness in N*m/radian.                                                                                                                                      |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float breakDistance``             | Break the attachment above this point-to-target separation in metres. Zero disables this condition.                                                                             |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float breakForce``                | Break above this requested attachment force in newtons, before Maximum Force is applied. Zero disables this condition.                                                          |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float breakTorque``               | Break above this requested attachment torque in N*m, before Maximum Torque is applied. Zero disables this condition.                                                            |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public CargoAttachmentAxes linearAxes``  | Spring translation axes in the target frame. Tethered uses a radial rope and ignores this selection.                                                                            |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAttachmentPoint``    | Attachment point in the cargo's local coordinates. An off-centre point lets spring/rope forces swing and rotate the item naturally.                                             |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumForce``              | Maximum translational attachment force in newtons. Zero disables the force.                                                                                                     |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumTorque``             | Maximum rotational attachment torque in N*m. Zero disables the torque.                                                                                                          |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float positionDamper``            | Relative point-velocity damping in N*s/m. Uses an implicit step to remain stable for light items.                                                                               |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float positionSpring``            | Translational spring stiffness in N/m. Tethered applies it only beyond Tether Length.                                                                                           |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float reactionScale``             | Attachment force/torque reaction applied to the anchor Rigidbody. Zero affects only cargo; one gives the anchor the opposite reaction. Independent of contact Vehicle Response. |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool releaseOnBreak``             | Also clear vehicle ownership on break. Off leaves a free, protected cargo item; on restores ordinary collisions with the former carrier.                                        |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 rotationOffset``          | Desired cargo rotation relative to the anchor/captured placement, in degrees. Spring and Tethered use it only when Align Rotation is enabled.                                   |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tetherLength``              | Slack rope length in metres for Tethered mode. No translational force is applied inside this radius; a taut rope only pulls.                                                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--cargocollisionexclusions:

CargoCollisionExclusions
------------------------

**Runtime/World/Cargo/Settings/CargoCollisionSettings.cs**

Flags selecting carrier-owned collision groups. None restores all contacts unless layers or custom exclusions still suppress them.

-  ``None = 0``
-  ``CarrierWheels = 1``
-  ``CarrierBody = 2``
-  ``CarrierPassengers = 4``
-  ``CarrierCargo = 8``

.. _uvs-api-collisionsandstabilization--cargocollisionsettings:

CargoCollisionSettings
----------------------

**Runtime/World/Cargo/Settings/CargoCollisionSettings.cs**

Additional collision exclusions, combined with existing collider layer exclusions. Pair exclusions are reference counted and restore their prior state when their last owner releases them. Refresh after changing individual array entries or hierarchy contents directly.

.. _uvs-api-collisionsandstabilization--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Member                                         | Meaning                                                                                                                             |
+================================================+=====================================================================================================================================+
| ``public LayerMask excludedLayers``            | Additional collision layers excluded on cargo colliders. Existing per-collider exclusions are preserved and restored on disable.    |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public CargoCollisionExclusions exclusions`` | Contact groups ignored by this cargo. Body excludes passengers, wheels and other cargo so each group can be selected independently. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public Collider[] ignoredColliders``         | Additional individual colliders to ignore. Existing ignored pairs and exclusions owned by other cargo helpers are preserved.        |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform[] ignoredRoots``            | Ignore colliders under these optional hierarchies. Call RefreshCollisionFilters after adding shapes to these roots at runtime.      |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--collisions:

Collisions
----------

**Runtime/Physics/Stability/Collisions.cs**

See :doc:`the handling guide </CollisionsAndStabilization>`. Component enable/disable controls participation; direct control is excluded.

**Inherits / implements:** :ref:`PhysicsModule <uvs-api-modules--physicsmodule>`, :ref:`IVehicleResetHandler <uvs-api-modules--ivehicleresethandler>`.

.. _uvs-api-collisionsandstabilization--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                                                                                                                                                                                   |
+========================================================+===========================================================================================================================================================================================================================================================+
| ``public float bodyFriction``                          | Additional body friction coefficient, limited by the normal contact impulse.                                                                                                                                                                              |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool coordinateLandingResponse``              | Coordinate grip loss and sway with active smooth suspension landing: retain the impact speed before absorption and wait briefly for all tires to carry load. When suspension landing is disabled, use the ordinary immediate response. Default: ``true``. |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashAttackTime``                       | Seconds to peak crash force; zero begins immediately on the next physics step. Default: ``0``.                                                                                                                                                            |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashCentredYaw``                       | Optional yaw target in degrees/s for severe near-centred impacts; alternates sides. Zero disables this presentation effect. Default: ``12``.                                                                                                              |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashDamperMultiplier``                 | Fraction of normal suspension damping retained just after a hard crash. Recovers smoothly through the suspension response window. Default: ``.25f``.                                                                                                      |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashEnergyFraction``                   | Maximum fraction of normal impact energy for the additional rotation/lift, including a movable partner. Default: ``.08f``.                                                                                                                                |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool crashFromWheelImpacts``                  | Opt in to supported tire impacts against near-vertical obstacles. Requires ``crashWeightTransfer``; excludes landings and leaves native tire restitution unchanged. Default: ``false``.                                                                   |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashGroundPivot``                      | Blend severe-crash direction toward the struck-end ground pivot; zero follows the real contact lever. Default: ``.8f``.                                                                                                                                   |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashMaximumLiftSpeed``                 | Maximum additional upward chassis speed in m/s; zero disables lift. Default: ``2``.                                                                                                                                                                       |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashMaximumRotation``                  | Maximum additional chassis rotation rate in degrees/s per crash. Default: ``100``.                                                                                                                                                                        |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashMinimumLeverage``                  | Minimum effective pitch/roll leverage in severe supported impacts. Default: ``.6f``.                                                                                                                                                                      |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashMinimumSpeed``                     | Normal collision speed in m/s required for chassis weight transfer. Default: ``6``.                                                                                                                                                                       |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashReleaseTime``                      | Seconds for crash force to fade from its peak; preserves the bounded impulse budget. Default: ``.14f``.                                                                                                                                                   |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashRotationPerSpeed``                 | Pitch/roll speed change in degrees/s per m/s of closing speed. Scaled by actual collision impulse so light debris cannot kick the car. Default: ``4``.                                                                                                    |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashSuspensionRecovery``               | Seconds for suspension damping to recover after the impact. Default: ``.7f``.                                                                                                                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool crashWeightTransfer``                    | Deliver a short, bounded pitch/roll impulse through the chassis after a hard body impact. Direction follows the contact normal and gravity. Default: ``true``.                                                                                            |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float crashYawVariation``                     | Maximum small yaw-rate variation in degrees/s after a hard crash. Its sign follows the real contact lever; zero disables it. Default: ``3``.                                                                                                              |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``        | Default local order 100.                                                                                                                                                                                                                                  |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float impactCooldown``                        | Minimum seconds between additional crash impulses.                                                                                                                                                                                                        |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool impactResponse``                         | Supply missing collision restitution after the native solver resolves the impact. Default: ``true``.                                                                                                                                                      |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingContactHoldTime``                | Maximum seconds after first tire contact to hold grip recovery and defer the sway while the remaining tires acquire load. Zero disables the contact wait; pre-absorption impact strength is still retained. Default: ``.45f``.                            |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingForwardGrip``                    | Forward grip retained at full landing response, before other grip modifiers. Initial value: ``.45f``.                                                                                                                                                     |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float LandingForwardGripScale { get; }``      | Current forward tire-grip multiplier before other grip policies.                                                                                                                                                                                          |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingFullResponseSpeed``              | Normal landing speed producing full grip loss and sway, in m/s. Initial value: ``4.5f``.                                                                                                                                                                  |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float LandingGripLoss { get; private set; }`` | Current 0–1 grip-loss envelope; smooth recovery, zero when inactive.                                                                                                                                                                                      |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingGripRecoveryTime``               | Seconds for tire grip and stability assistance to smoothly recover. Initial value: ``.85f``.                                                                                                                                                              |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingLateralSway``                    | Maximum added sideways speed in m/s at a directional landing. Delivered over a short ground-contact push. Initial value: ``.45f``.                                                                                                                        |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingMinimumAirTime``                 | Minimum unsupported flight time before a wheel landing is eligible, in seconds. Initial value: ``.15f``.                                                                                                                                                  |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingMinimumSpeed``                   | Minimum normal landing speed relative to the surface, in m/s. Initial value: ``1.5f``.                                                                                                                                                                    |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingRearGripBias``                   | Additional sideways grip reduction on wheels behind the centre of mass during recovery. Initial value: ``.2f``.                                                                                                                                           |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingSidewaysGrip``                   | Sideways grip retained at full landing response, before other grip modifiers. Initial value: ``.3f``.                                                                                                                                                     |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float LandingSidewaysGripScale { get; }``     | Current base lateral grip and stability-authority multiplier; rear wheel bias is applied separately.                                                                                                                                                      |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool landingTractionLoss``                    | Briefly reduce tire grip after an airborne wheel landing and allow a small directional sway. Initial value: ``true``.                                                                                                                                     |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingYawSway``                        | Maximum additional yaw-rate change in degrees/s. Direction follows the landing's lateral motion, bank and first wheel contacts. Initial value: ``7``.                                                                                                     |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngularKick``                    | Maximum angular speed change per impact, in degrees/s. Off-centre contacts naturally pitch, yaw or roll.                                                                                                                                                  |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumReboundSpeed``                   | Maximum additional separation speed, in m/s.                                                                                                                                                                                                              |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumBodyTilt``                       | Minimum gravity-relative tilt for additional body sliding friction.                                                                                                                                                                                       |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumImpactSpeed``                    | Normal closing speed required for an additional response, in m/s.                                                                                                                                                                                         |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``      | Contact phase: updates landing grip loss before steering, friction and stability assistance.                                                                                                                                                              |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restitution``                           | Target separation speed as a fraction of normal closing speed. Existing PhysX bounce is counted.                                                                                                                                                          |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--methods-1:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                           | Role and behavior                                                                                                                                                        | Arguments and result |
+=====================================================================================+==========================================================================================================================================================================+======================+
| ``public override void Configure(VehicleController vehicle)``                       | Clears transient state, binds the configured vehicle and refreshes owned native settings. Called by vehicle configuration.                                               | —                    |
+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public virtual void ResetVehicleState(VehicleResetReason reason)``                | Clears transient state for the supplied reset reason without changing persistent configuration.                                                                          | —                    |
+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float dt)`` | Detects grounded-profile wheel landings, updates recovery and distributes the bounded directional sway while wheels touch ground. No direct-control or kinematic forces. | —                    |
+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-collisionsandstabilization--dynamicobstacle:

DynamicObstacle
---------------

**Runtime/Physics/Stability/DynamicObstacle.cs**

Opt-in native settings for movable world props pushed by heavier vehicles. Enabled on the five Demo/Samples dynamic crates. No forces, velocity clamps, pose corrections or per-frame updates. Disabling restores captured Rigidbody settings; re-enable captures fresh ownership. Reapply after editing fields or switching kinematic mode.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-collisionsandstabilization--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                                                                                          |
+======================================================+==================================================================================================================================================================================+
| ``public CollisionDetectionMode collisionDetection`` | Native collision detection mode. Default ContinuousSpeculative covers angular motion and dynamic panels; kinematic bodies use Speculative when a non-Discrete mode is requested. |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public RigidbodyInterpolation interpolation``      | Native display interpolation. Default Interpolate matches the default vehicle.                                                                                                   |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDepenetrationSpeed``           | Maximum native overlap-separation speed in m/s, retains a lower original cap. Does not cap physical impact speed. Default: ``2``.                                                |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverIterations``                      | Minimum position solver passes; retains higher original settings. Default: ``0``. Zero preserves original.                                                                       |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverVelocityIterations``              | Minimum velocity solver passes; retains higher original settings. Default: ``0``. Zero preserves original.                                                                       |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--methods-2:

Methods
~~~~~~~

+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
| Signature                               | Role and behavior                                                                                                                                               | Arguments and result           |
+=========================================+=================================================================================================================================================================+================================+
| ``public virtual void ApplySettings()`` | Captures settings on first active application and configures the owned Rigidbody. Reapplication never overwrites the restoration snapshot. No-op when disabled. | No arguments; no return value. |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+

.. _uvs-api-collisionsandstabilization--stabilization:

Stabilization
-------------

**Runtime/Physics/Stability/Stabilization.cs**

See :doc:`the handling guide </CollisionsAndStabilization>`. Component enable/disable controls participation; direct control is excluded.

**Inherits / implements:** :ref:`PhysicsModule <uvs-api-modules--physicsmodule>`.

.. _uvs-api-collisionsandstabilization--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                      |
+======================================================+==============================================================================================================+
| ``public event System.Action<Telemetry> Overturned`` | Raised once when sustained tilt qualifies; carries the telemetry snapshot at that transition.                |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<Telemetry> Recovered``  | Raised once when tilt falls below the recovery threshold; carries the telemetry snapshot at that transition. |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                                                                                                                                            |
+====================================================+====================================================================================================================================================================================================================+
| ``public bool affectOtherProfiles``                | Opt in for air/water/hover profiles. Normally only grounded profiles are supported.                                                                                                                                |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 airborneDamping``                 | Local pitch/yaw/roll damping rates in 1/s while airborne.                                                                                                                                                          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float airborneDelay``                     | Delay before airborne damping in seconds; airborne leveling instead builds smoothly through this interval.                                                                                                         |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float airborneLevelDamping``              | Airborne roll-leveling damping in 1/s. Initial value: ``8``.                                                                                                                                                       |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float airborneLevelMaximumAcceleration``  | Airborne leveling acceleration cap in degrees/s squared. Initial value: ``360``.                                                                                                                                   |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float airborneLevelMaximumTilt``          | Largest eligible bank angle relative to gravity in degrees. Initial value: ``170``.                                                                                                                                |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float airborneLevelStrength``             | Airborne angular spring strength in 1/s squared. Initial value: ``16``.                                                                                                                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool autoLevelAirborne``                  | Opt in to gravity-relative local-Z roll recovery during free flight. Initial value: ``false``.                                                                                                                     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool autoRighting``                       | Smoothly push a slow vehicle on its side back onto its wheels using torque while the body touches the ground.                                                                                                      |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool detectOverturn``                     | When checked, detect overturn is active; when unchecked the owning system skips that optional policy. Initial value: ``true``.                                                                                     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``    | Default order 760 in the balance phase, after normal motorcycle riding balance.                                                                                                                                    |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsAirborne { get; private set; }``   | Whether the last module step found no wheel support or fresh body contact.                                                                                                                                         |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsOverturned { get; private set; }`` | Current is overturned.                                                                                                                                                                                             |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsRighting { get; }``                | Whether optional assisted recovery is currently active.                                                                                                                                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDeceleration``               | Maximum angular deceleration in degrees/s squared.                                                                                                                                                                 |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumSpin``                       | Soft angular speed threshold in degrees/s; does not hard-clamp velocity.                                                                                                                                           |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float overspeedDamping``                  | Additional damping above Maximum Spin, in 1/s.                                                                                                                                                                     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float overturnAngle``                     | Overturn angle in degrees, relative to the owning mechanism's reference frame. Initial value: ``70``.                                                                                                              |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float overturnDelay``                     | Time continuously tilted before reporting overturn, in seconds.                                                                                                                                                    |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``  | Balance phase. Ground recovery yields when Motorcycle Balance applies supported roll control in the same physics step.                                                                                             |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool preventOutwardAirRoll``              | With airborne leveling enabled, block rider roll input away from upright and retain automatic recovery during corrective input. Pitch remains available; the restriction can be disabled. Initial value: ``true``. |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float recoveryAngle``                     | Tilt below which an overturned vehicle is considered recovered. Initial value: ``40``.                                                                                                                             |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingBuildTime``                 | Seconds for recovery torque to build smoothly after Righting Delay. Zero preserves immediate full-strength assistance.                                                                                             |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingContactGrace``              | Seconds to continue an already active recovery across brief support gaps while lifting off the chassis onto the wheels. Longer gaps stop recovery and restart its delay and buildup.                               |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingDamping``                   | Angular damping in 1/s during recovery.                                                                                                                                                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingDelay``                     | Seconds continuously overturned and touching the ground before recovery starts.                                                                                                                                    |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingMaximumAcceleration``       | Recovery angular acceleration limit in degrees/s squared.                                                                                                                                                          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingMaximumSpeed``              | Maximum chassis speed in m/s during assisted recovery.                                                                                                                                                             |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingMaximumTilt``               | Maximum eligible tilt for side recovery; roof recovery is excluded. Default: ``125``, range 90–135 degrees.                                                                                                        |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingMinimumTilt``               | Tilt in degrees required to begin recovery.                                                                                                                                                                        |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool rightingOnWheelSupport``             | Allow recovery from excessive lean while usable wheels still touch the ground. Wall/ceiling tire contact is not standing support.                                                                                  |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool rightingRollOnly``                   | Recover only sideways bank around the vehicle's longitudinal Z axis. Does not correct wheelies, nose pitch or heading.                                                                                             |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightingStrength``                  | Angular spring strength in 1/s squared.                                                                                                                                                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--methods-3:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                  | Role and behavior                                                                                                                              | Arguments and result |
+============================================================================================+================================================================================================================================================+======================+
| ``public override void Configure(VehicleController vehicle)``                              | Clears transient state, binds the configured vehicle and refreshes owned native settings. Called by vehicle configuration.                     | —                    |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Runs passive airborne damping and optional grounded recovery for this fixed step. Ignores missing/kinematic bodies and non-positive timesteps. | —                    |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Allows grounded profiles by default; affectOtherProfiles opts into other media.                                                                | —                    |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-collisionsandstabilization--vehiclecargo:

VehicleCargo
------------

**Runtime/World/Cargo/VehicleCargo.cs**

Optional per-item helper with independent contact ownership, collision filters and opt-in attachments. Free mode never corrects pose or applies attachment forces. Compound colliders on its body are supported; separate child bodies need their own helper. Disabling restores original body settings, collider flags/layer masks and owned collision pairs. Parent hierarchy restoration is deferred until the next frame, outside native activation/deactivation callbacks; reenabling or explicitly releasing the cargo cancels stale requests. Initially nested cargo is detached at runtime; explicitly released cargo stays detached.

.. _uvs-api-collisionsandstabilization--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Member                                                         | Meaning                                                                                                 |
+================================================================+=========================================================================================================+
| ``public event Action<CargoAttachmentBreak> AttachmentBroken`` | Raised after manual/threshold break commits Free mode and optional carrier release.                     |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public event Action<VehicleCargoMode> ModeChanged``          | Raised after an active mode transition is applied; initial enable is not a transition.                  |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public event Action<VehicleController> Released``            | Raised once ownership is cleared, carrying the former vehicle. Repeated unowned releases do not notify. |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                                                                                 |
+======================================================+=========================================================================================================================================================================+
| ``public CargoAttachmentSettings attachment``        | Optional anchor, spring/rope tuning and break thresholds. Free mode never uses these settings to move the body.                                                         |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float AttachmentDistance { get; }``         | Last solved world-space point-to-target separation in metres.                                                                                                           |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 AttachmentForce { get; }``          | Last applied attachment force in newtons, zero in Free or after a break.                                                                                                |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 AttachmentTorque { get; }``         | Last applied attachment torque in N*m, zero when rotation alignment is disabled.                                                                                        |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float autoReleaseDistance``                 | Automatically Release when farther than this distance from the captured placement moving with the carrier. Zero disables automatic release; it never attracts the item. |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Rigidbody Body { get; }``                   | Independent cargo Rigidbody, never the chassis.                                                                                                                         |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController Carrier { get; }``        | Currently bound carrier, including after cargo unparents.                                                                                                               |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float carrierBounciness``                   | Carrier-contact restitution when Override Carrier Material is enabled.                                                                                                  |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float carrierDynamicFriction``              | Sliding carrier-contact friction when Override Carrier Material is enabled.                                                                                             |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float carrierFriction``                     | Static carrier-contact friction when Override Carrier Material is enabled. Other contacts keep their own physics materials.                                             |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public CollisionDetectionMode collisionDetection`` | Collision detection for loose cargo. Speculative contacts cover translation and rotation without making carrier sweeps stop on their own load.                          |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public CargoCollisionSettings collisions``         | Collision groups, layers and individually ignored shapes. Changes through the public setters apply immediately.                                                         |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool followVehicleTeleport``                | Reset cargo to its captured placement when the carrier teleports, including vehicle reset.                                                                              |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool HasAttachment { get; }``               | True while enabled in an attached mode with a usable target frame.                                                                                                      |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public RigidbodyInterpolation interpolation``      | Presentation interpolation while the helper is enabled. Original body settings are restored on disable.                                                                 |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDepenetrationSpeed``           | Maximum overlap recovery speed in m/s. Limits initial placement kicks without capping ordinary motion.                                                                  |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleCargoMode mode``                     | Free/Dynamic has no attachment forces or rotation correction. Secured fixes the pose; Spring is elastic; Tethered pulls only after rope slack is used.                  |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool overrideCarrierMaterial``              | Override carrier-contact material values. Off preserves normal physics materials, including friction and bounce; no glue or upright force is added.                     |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverIterations``                      | Minimum native position solver iterations while this helper is enabled.                                                                                                 |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverVelocityIterations``              | Minimum native velocity solver iterations while this helper is enabled.                                                                                                 |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle``                 | Vehicle carrying this object. Initially resolves from the parent hierarchy when empty. Release removes this ownership and restores ordinary contacts with that vehicle. |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float vehicleResponse``                     | Carrier response to loose cargo contacts only. Zero prevents cargo pushing or tipping its vehicle; one restores the normal two-way solver response.                     |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--methods-4:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Signature                                                                                                      | Role and behavior                                                                                                                    | Arguments and result                                                                               |
+================================================================================================================+======================================================================================================================================+====================================================================================================+
| ``public virtual void ApplySettings()``                                                                        | Reapplies owned native tuning and contact policy without changing carrier mass/velocity. Reads current attachment tuning.            | Call after direct configuration edits when an immediate update is needed.                          |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual bool BreakAttachment(CargoAttachmentBreakReason reason = CargoAttachmentBreakReason.Manual)`` | Switches to Free, optionally clears ownership, then raises copied AttachmentBroken context.                                          | reason defaults Manual; returns false if already Free.                                             |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual bool CaptureAnchorOffset()``                                                                  | Captures current attachment-point and rotation offsets relative to the explicit anchor.                                              | Returns false without a valid explicit anchor.                                                     |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void CapturePlacement()``                                                                     | Stores current cargo pose in carrier physics coordinates, or world coordinates without a carrier. Resets attachment sampling.        | No arguments or result.                                                                            |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshBinding()``                                                                       | Rescans cargo shapes and carrier bodies, reconnects events and refreshes filters. Same-carrier refresh preserves captured placement. | Call after adding/removing native shapes or carrier parts.                                         |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCollisionFilters()``                                                              | Reconciles groups, layers and custom exclusions without recapturing placement or moving cargo.                                       | Use after editing list entries or changing excluded hierarchies.                                   |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void Release()``                                                                              | Switches to Free and clears carrier ownership, restoring ordinary former-carrier contacts and retaining momentum.                    | No arguments or result. Does not clear authored anchor settings.                                   |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void ResetPlacement()``                                                                       | Restores captured cargo pose with carrier point/angular velocity, or zero without a carrier.                                         | No arguments or result.                                                                            |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual bool SetAnchor(Transform value, bool preserveWorldPose = true)``                              | Assigns optional frame. Pose preservation captures offsets; clearing with preservation captures current placement. Never teleports.  | value: target or null; preserveWorldPose defaults true. Returns false for self/descendant anchors. |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void SetCollisionExclusions(CargoCollisionExclusions value)``                                 | Changes carrier-group exclusion flags and refreshes native pairs immediately.                                                        | value: combinable CargoCollisionExclusions flags.                                                  |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void SetExcludedLayers(LayerMask value)``                                                     | Combines additional layer exclusions with the collider masks captured on binding.                                                    | value: layer mask; zero removes only helper additions.                                             |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void SetIgnoredColliders(Collider[] value)``                                                  | Replaces custom excluded collider list and immediately reconciles pairs.                                                             | value: collider array; null clears the list.                                                       |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void SetIgnoredRoots(Transform[] value)``                                                     | Replaces excluded hierarchies and collects their current descendant colliders.                                                       | value: Transform array; null clears the list.                                                      |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void SetMode(VehicleCargoMode value)``                                                        | Applies the selected mode immediately while enabled. Leaving Secured inherits target point/angular velocity.                         | value: Dynamic, Secured, Spring or Tethered.                                                       |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual void SetVehicle(VehicleController value)``                                                    | Rebinds carrier ownership and captures placement only when the carrier changes; does not move cargo.                                 | value: carrier, or null to clear ownership.                                                        |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual bool SnapToAnchor()``                                                                         | Explicitly places cargo at its target, including configured point/rotation offsets; inherits target momentum.                        | Returns false if disabled or frame invalid. This is an explicit teleport, even in Free mode.       |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--vehiclecargomode:

VehicleCargoMode
----------------

**Runtime/World/Cargo/VehicleCargo.cs**

Simulation mode. Existing numeric values remain Dynamic = 0 and Secured = 1; Spring = 2 and Tethered = 3. Free is the Inspector label of Dynamic.

-  ``Dynamic``
-  ``Secured``
-  ``Spring``
-  ``Tethered``

.. _uvs-api-collisionsandstabilization--vehiclecollisionhandler:

VehicleCollisionHandler
-----------------------

**Runtime/Physics/Core/VehicleCollisionHandler.cs**

Target-side collision extension. Attach a derived component above the target colliders. See :ref:`wheel and body hook example <uvs-collisionsandstabilization--custom-wheel-and-body-collision-handling>`.

**Inherits / implements:** ``MonoBehaviour``.

.. _uvs-api-collisionsandstabilization--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-----------------------------------------------------------------------------+
| Member                                            | Meaning                                                                     |
+===================================================+=============================================================================+
| ``public virtual int CollisionPriority { get; }`` | Higher values dispatch first; default zero. Ties retain registration order. |
+---------------------------------------------------+-----------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--methods-5:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Signature                                                                                                  | Role and behavior                                                      | Arguments and result                                                                               |
+============================================================================================================+========================================================================+====================================================================================================+
| ``public virtual bool ExcludeWheelSupport(Collider target)``                                               | Defines native and supplemental wheel-support admission.               | True excludes target for all UVS wheels; default false. Sampled at registration.                   |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual bool HandleBodyCollision(VehicleController vehicle, Collision collision, bool entering)`` | Handles a native body contact before package processing.               | True claims the pair; false continues. Main thread, after physics. ``entering`` is false for stay. |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public void RefreshCollisionColliders()``                                                                | Rebuilds owned target registrations and wheel-support rules.           | Call after collider/rule/priority changes.                                                         |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public void RefreshWheelSupport()``                                                                      | Resamples support admission without rebuilding collider registrations. | Call when only wheel-support rules change.                                                         |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. _uvs-api-collisionsandstabilization--vehiclecollisionhooks:

VehicleCollisionHooks
---------------------

**Runtime/Physics/Core/VehicleCollisionHooks.cs**

Main-thread target registry and prioritized body-contact dispatcher. Normally use VehicleCollisionHandler's automatic lifecycle registration.

.. _uvs-api-collisionsandstabilization--methods-6:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------+
| Signature                                                                                                 | Role and behavior                                                     | Arguments and result                                                |
+===========================================================================================================+=======================================================================+=====================================================================+
| ``public static bool HandleBodyCollision(VehicleController vehicle, Collision collision, bool entering)`` | Dispatches once per vehicle/self-target pair/phase/fixed step.        | True skips standard package logic; native physical impulse remains. |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public static void Register(Collider target, VehicleCollisionHandler handler)``                         | Adds one enabled handler for this collider and its support exclusion. | Repeated registration is idempotent.                                |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public static void Unregister(Collider target, VehicleCollisionHandler handler)``                       | Releases only this owner's target registration and exclusion lease.   | Final release restores the original wheel ignore states.            |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------+
