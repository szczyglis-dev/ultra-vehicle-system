.. _uvs-scripting-weapons--weapon-and-payload-contracts:

Weapon and payload contracts
============================

Vehicle weapons separate firing admission, projectile behavior and presentation. A barrel validates a request and spawns a projectile. The projectile owns its flight, impact and lifetime. Effects and recoil observe the shot. Rockets and dropped objects use related but distinct ownership rules for mounted stores.

This makes it possible to use the same barrel with a custom projectile or replace the visual effects without changing cooldown and trigger behavior. Game damage, scoring, inventory and rearming belong to the application or projectile implementation rather than being inferred from a muzzle flash.

.. _uvs-scripting-weapons--implementation-map:

Implementation map
------------------

+---------------------+-------------------------------------------------------------------------------+
| Class               | Responsibility                                                                |
+=====================+===============================================================================+
| ``DroppableObject`` | Detaches the actual payload and establishes released physics.                 |
+---------------------+-------------------------------------------------------------------------------+
| ``ObjectDropper``   | Validates selected payload release and cooldown.                              |
+---------------------+-------------------------------------------------------------------------------+
| ``Rocket``          | Owns launched-rocket motor, collision and lifetime behavior.                  |
+---------------------+-------------------------------------------------------------------------------+
| ``RocketLauncher``  | Selects and launches configured mounted rocket stores.                        |
+---------------------+-------------------------------------------------------------------------------+
| ``WeaponBarrel``    | Owns muzzle aiming, trigger/cooldown admission and projectile initialization. |
+---------------------+-------------------------------------------------------------------------------+
| ``WeaponEffects``   | Presents shot sound, flash and smoke.                                         |
+---------------------+-------------------------------------------------------------------------------+
| ``WeaponRecoil``    | Presents configured visual/hull recoil.                                       |
+---------------------+-------------------------------------------------------------------------------+

.. _uvs-scripting-weapons--firing-admission:

Firing admission
----------------

Choose the firing API from the input semantics. ``TryFire`` requests one shot now; ``SetTrigger`` supplies held intent for the configured Single/Automatic policy. Automatic cadence is bounded by physics ticks, so a requested rate higher than the tick frequency does not produce arbitrarily many shots inside one tick.

Keep the muzzle's local +Z axis aligned with firing direction. Aiming/elevation and projectile ballistics are separate: ``AimAt`` points the configured barrel, while lead, gravity compensation and target selection require an application aiming policy. Refresh the collision filter after changing the owner's colliders so a new projectile receives the current exclusion set.

``WeaponBarrel`` requires an enabled owner, muzzle and ``projectilePrefab`` implementing ``IWeaponProjectile``. ``TryFire`` respects the enable/cooldown policy. ``SetTrigger`` supplies held Single/Automatic intent; automatic fire emits at most one round per physics tick. ``RefreshCollisionFilter`` after owned collider changes.

Initialize receives owner, initial velocity, impulse, lifetime and ignored owner colliders. The projectile owns applying those values, collision/impact rules and cleanup. Fired supplies the spawned component. Barrel ``AimAt`` controls its configured elevation; a separate ``MovingPart`` can control turret yaw. Supply ballistic compensation externally.

.. _uvs-scripting-weapons--a-minimal-custom-projectile:

A minimal custom projectile
---------------------------

``IWeaponProjectile.Initialize`` is the handover from the barrel to the projectile. Apply the supplied initial velocity, impact impulse, lifetime and ignored-collider list in the implementation. A custom projectile can instead implement penetration, area effects or another flight model, but it must still own cleanup and respect its intended owner-contact policy.

The example records an initial impact direction before native contact response can change velocity. Its ``hit`` guard ensures multiple collision callbacks do not apply the gameplay impulse repeatedly. The one-shot impulse is deliberately separate from a health/damage system; connect that application rule at the same accepted-impact boundary.

Put this on a prefab with ``Rigidbody`` and a collider, then assign that component as ProjectileDemo Prefab. It applies an impulse once to a hit ``Rigidbody`` and destroys itself. Add game damage/scoring in the same impact path as needed.

**Example:** ``SimpleVehicleProjectile.cs``

.. raw:: html

   <!-- example: SimpleVehicleProjectile.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       [RequireComponent(typeof(Rigidbody), typeof(Collider))]
       public class SimpleVehicleProjectile : MonoBehaviour, IWeaponProjectile
       {
           private float impactImpulse;
           private Vector3 impactDirection;
           private bool hit;

           public void Initialize(VehicleController owner, Vector3 velocity, float impulse,
               float lifetime, Collider[] ignoredColliders)
           {
               impactImpulse = impulse;
               impactDirection = velocity.normalized;
               var body = GetComponent<Rigidbody>();
               body.useGravity = true;
               body.collisionDetectionMode = CollisionDetectionMode.ContinuousDynamic;
               body.linearVelocity = velocity;
               foreach (var own in GetComponentsInChildren<Collider>())
                   foreach (var ignored in ignoredColliders)
                       if (own && ignored) UnityEngine.Physics.IgnoreCollision(own, ignored);
               Destroy(gameObject, Mathf.Max(.01f, lifetime));
           }

           private void OnCollisionEnter(Collision collision)
           {
               if (hit) return;
               hit = true;
               if (collision.rigidbody)
                   collision.rigidbody.AddForce(impactDirection * impactImpulse, ForceMode.Impulse);
               Destroy(gameObject);
           }
       }
   }

.. _uvs-scripting-weapons--rocket-and-presentation-ownership:

Rocket and presentation ownership
---------------------------------

``RocketLauncher`` chooses a configured mounted store and admits a shot according to enable/trigger/cooldown policy. ``Rocket`` owns the launched object's motion and impact behavior. The launcher publishes ``Fired`` with the launched rocket so application scoring or tracking can associate that object with the shot.

A rocket's ``Launch`` boundary establishes carrier velocity and flight configuration. Its motor can stop before its lifetime ends. ``StopMotor`` therefore stops force/audio/emission while ``Detonate`` ends it through the explosion path. Use ``Exploded`` for explosion-specific rules instead of treating every motor stop or object destruction as a hit.

``WeaponEffects`` and ``WeaponRecoil`` observe accepted shots. They can be replaced independently: an effect adapter owns its generated flash/audio/particles, while recoil owns the configured part motion and optional hull impulse. Keep the barrel's aiming transform and recoil transform arranged so both systems do not overwrite the same pivot.

Mounted and launched stores have different lifetimes. The launcher disables the mounted original and creates the detached rocket copy; rearming therefore needs an explicit application rule to restore available stores. Stopping the motor ends its force and owned presentation, not necessarily the entire projectile lifetime.

Presentation should follow accepted shots. Playing a muzzle effect from raw input could show firing even when cooldown or missing ammunition rejected the action. Recoil likewise belongs to the shot result, and its visual travel should not become a competing writer of the hull's rotation.

``RocketLauncher`` chooses the next active store from its explicit list. Launch creates a detached physical copy and disables the mounted original. The copy inherits carrier point velocity, motor/gravity policy and configured lifetime. Native collision detonates once; base rockets have no seeker. Rearm belongs to the application.

``StopMotor`` stops force, loop and emission. Burnout/impact/despawn perform the same owned cleanup. ``WeaponEffects`` supplies separately enabled sound, flash and smoke; ``WeaponRecoil`` supplies visual travel/hull impulse without assigning hull rotation.

.. _uvs-scripting-weapons--drop-a-selected-object:

Drop a selected object
----------------------

A dropper is an admission/control layer, not an inventory selector. The application decides which payload is selected and passes that exact object. The object itself detaches, so repeated release cannot be treated as spawning another identical item.

For a payload with a fuse, impact effect or lifetime, place that behavior on the released object or an application component. The drop event only establishes release; it cannot imply when the object will collide or whether that collision should count as a successful delivery.

``ObjectDropper`` does not own an inventory. ``TryDrop`` accepts one eligible owned payload and starts its cooldown. ``DroppableObject`` detaches the actual object, creates/reuses a ``Rigidbody`` and applies inherited/separation velocity. It does not clone a replacement or auto-expire.

**Example:** ``PayloadReleaseControl.cs``

.. raw:: html

   <!-- example: PayloadReleaseControl.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class PayloadReleaseControl : MonoBehaviour
       {
           public ObjectDropper dropper;
           public DroppableObject payload;
           public bool Release() => dropper && payload && dropper.TryDrop(payload);
       }
   }

The payload must belong to the configured owner and remain active/undropped. Direct Drop bypasses the dropper's cooldown. A release event does not imply an impact or explosion; add those rules separately.

.. _uvs-scripting-weapons--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed weapons and payloads API </API/Weapons>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-weapons--droppableobject:

DroppableObject
~~~~~~~~~~~~~~~

:ref:`DroppableObject <uvs-api-weapons--droppableobject>` gives the full declared contract.

+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Method                                                | Role                                                                                      |
+=======================================================+===========================================================================================+
| ``public virtual bool Drop(VehicleController owner)`` | Detaches this actual payload, establishes released-body motion and publishes its release. |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------+

+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                 | Role                                                                                                                     |
+==================================================+==========================================================================================================================+
| ``public event Action<DroppableObject> Dropped`` | After accepted payload release. Payload: released ``DroppableObject``; ``ObjectDropper`` also includes its own instance. |
+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-weapons--ivehiclemodule:

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

.. _uvs-scripting-weapons--iweaponprojectile:

IWeaponProjectile
~~~~~~~~~~~~~~~~~

:ref:`IWeaponProjectile <uvs-api-weapons--iweaponprojectile>` gives the full declared contract.

+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                                     | Role                                                                                                                  |
+============================================================================================================================+=======================================================================================================================+
| ``void Initialize(VehicleController owner, Vector3 velocity, float impulse, float lifetime, Collider[] ignoredColliders)`` | Accepts the projectile handover: owner, initial world velocity, impact impulse, lifetime and ignored owner colliders. |
+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-weapons--objectdropper:

ObjectDropper
~~~~~~~~~~~~~

:ref:`ObjectDropper <uvs-api-weapons--objectdropper>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                             |
+============================================================================================+==================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Assigns the vehicle owner used to validate payload release.                                      |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Decrements payload-release cooldown; selection and release remain explicit ``TryDrop`` requests. |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual void SetDroppingEnabled(bool value)``                                     | Changes payload-release availability through the dropper's action/event path.                    |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual bool TryDrop(DroppableObject item)``                                      | Requests release of a selected eligible payload, respecting owner, enable and cooldown policy.   |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                | Role                                                                                                                     |
+=================================================================+==========================================================================================================================+
| ``public event Action<ObjectDropper, DroppableObject> Dropped`` | After accepted payload release. Payload: released ``DroppableObject``; ``ObjectDropper`` also includes its own instance. |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> DroppingEnabledChanged``            | When dropper availability changes. Payload: bool.                                                                        |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-weapons--rocket:

Rocket
~~~~~~

:ref:`Rocket <uvs-api-weapons--rocket>` gives the full declared contract.

+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Method                                                    | Role                                                                                                  |
+===========================================================+=======================================================================================================+
| ``public virtual Rocket Launch(VehicleController owner)`` | Creates/initializes launched-rocket behavior from the mounted store and carrier state.                |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual void StopMotor()``                       | Stops the rocket motor and its owned loop/emission without implying immediate projectile destruction. |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual void Detonate(Vector3 point)``           | Ends the rocket through its explosion path at the supplied world point.                               |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

+---------------------------------------------------+--------------------------------------------------------------------------------+
| Event / callback                                  | Role                                                                           |
+===================================================+================================================================================+
| ``public event Action<Rocket, Vector3> Exploded`` | At the rocket's explosion boundary. Payload: Rocket and world explosion point. |
+---------------------------------------------------+--------------------------------------------------------------------------------+

.. _uvs-scripting-weapons--rocketlauncher:

RocketLauncher
~~~~~~~~~~~~~~

:ref:`RocketLauncher <uvs-api-weapons--rocketlauncher>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                |
+============================================================================================+=====================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Assigns the vehicle owner used by launched stores.                                                  |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Decrements launcher cooldown and requests another shot while automatic held-trigger policy applies. |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public virtual void SetFiringEnabled(bool value)``                                       | Changes weapon firing availability and publishes its state transition.                              |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public virtual void SetTrigger(bool held)``                                              | Supplies held trigger intent; firing mode/cooldown determine actual shots.                          |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public virtual bool TryFire()``                                                          | Requests one shot/store release subject to enable, valid setup and cooldown policy.                 |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Event / callback                                      | Role                                                                                                                  |
+=======================================================+=======================================================================================================================+
| ``public event Action<bool> TriggerChanged``          | When held trigger intent changes. Payload: bool; a ``true`` trigger does not guarantee a shot.                        |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> FiringEnabledChanged``    | When weapon firing availability changes. Payload: bool.                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<RocketLauncher, Rocket> Fired`` | After an admitted shot creates/releases its projectile. Payload: weapon owner and spawned projectile/store component. |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-weapons--vehiclemodule:

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

.. _uvs-scripting-weapons--weaponbarrel:

WeaponBarrel
~~~~~~~~~~~~

:ref:`WeaponBarrel <uvs-api-weapons--weaponbarrel>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                                          |
+============================================================================================+===============================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Assigns the vehicle owner and rebuilds owner-collider exclusions for spawned projectiles.                                     |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCollisionFilter()``                                           | Rebuilds the owner-collider exclusion set supplied to subsequently spawned projectiles.                                       |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Attempts at most one automatic shot for a positive timestep while the trigger is held.                                        |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFiringEnabled(bool value)``                                       | Changes weapon firing availability and publishes its state transition.                                                        |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMovementInput(float input)``                                      | Supplies barrel elevation rate input rather than a fixed aim target.                                                          |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAimAngle(float angle)``                                           | Requests a bounded barrel elevation angle in degrees.                                                                         |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AimAt(Vector3 point)``                                               | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AimAt(Transform target)``                                            | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StopAiming()``                                                       | Releases barrel target tracking without inventing a new aim target.                                                           |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFireMode(WeaponFireMode mode)``                                   | Chooses single/automatic firing policy for subsequent trigger input.                                                          |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTrigger(bool held)``                                              | Supplies held trigger intent; firing mode/cooldown determine actual shots.                                                    |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryFire()``                                                          | Requests one shot/store release subject to enable, valid setup and cooldown policy.                                           |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Event / callback                                           | Role                                                                                                                  |
+============================================================+=======================================================================================================================+
| ``public event Action<bool> TriggerChanged``               | When held trigger intent changes. Payload: bool; a ``true`` trigger does not guarantee a shot.                        |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> FiringEnabledChanged``         | When weapon firing availability changes. Payload: bool.                                                               |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<WeaponBarrel, MonoBehaviour> Fired`` | After an admitted shot creates/releases its projectile. Payload: weapon owner and spawned projectile/store component. |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-weapons--weaponeffects:

WeaponEffects
~~~~~~~~~~~~~

:ref:`WeaponEffects <uvs-api-weapons--weaponeffects>` gives the full declared contract.

+---------------------------------------------------------------+----------------------------------------------------------------+
| Method                                                        | Role                                                           |
+===============================================================+================================================================+
| ``public override void Configure(VehicleController vehicle)`` | Refreshes accepted-shot bindings while this effect is enabled. |
+---------------------------------------------------------------+----------------------------------------------------------------+

.. _uvs-scripting-weapons--weaponrecoil:

WeaponRecoil
~~~~~~~~~~~~

:ref:`WeaponRecoil <uvs-api-weapons--weaponrecoil>` gives the full declared contract.

+---------------------------------------------------------------+-----------------------------------------------------------------------------+
| Method                                                        | Role                                                                        |
+===============================================================+=============================================================================+
| ``public override void Configure(VehicleController vehicle)`` | Refreshes accepted-shot bindings while this recoil presentation is enabled. |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+
