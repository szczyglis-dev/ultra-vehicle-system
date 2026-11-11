.. _uvs-scripting-damage--body-opening-damage-and-repair:

Body opening, damage and repair
===============================

Body operation, damage accumulation and mesh deformation are separate layers. A body part can open around a hinge; a damage part can receive hits and detach; a deformation component can dent readable mesh geometry. Combining these layers produces a damaged vehicle without making every opening mechanism responsible for health or rendering.

Use the layer that matches the action. Open a door through ``Body``, report a gameplay impact through ``Damage``, and restore geometry through ``VehicleMeshDeformation``. VehicleController.RepairAll coordinates retained registered parts, wheel reconnection, body hinges and mesh restoration; ResetVehicle additionally teleports and resets passengers. Destroyed objects still need application respawning.

.. _uvs-scripting-damage--implementation-map:

Implementation map
------------------

+------------------------------+----------------------------------------------------------------------+
| Class                        | Responsibility                                                       |
+==============================+======================================================================+
| ``Body``                     | Finds and operates authored ``VehicleBodyPart`` entries.             |
+------------------------------+----------------------------------------------------------------------+
| ``Damage``                   | Accepts impacts and routes them to damage/deformation boundaries.    |
+------------------------------+----------------------------------------------------------------------+
| ``DamageCollisionRelay``     | Relays relevant native collisions into damage handling.              |
+------------------------------+----------------------------------------------------------------------+
| ``DamagePart``               | Tracks a part's damage and detachment behavior.                      |
+------------------------------+----------------------------------------------------------------------+
| ``ICollisionDamageResponse`` | Lets a target alter collision damage severity.                       |
+------------------------------+----------------------------------------------------------------------+
| ``VehicleBodyPart``          | Defines a named opening/moving body element.                         |
+------------------------------+----------------------------------------------------------------------+
| ``VehicleMeshDeformation``   | Owns readable mesh instances, dent buffers and geometry restoration. |
+------------------------------+----------------------------------------------------------------------+

.. _uvs-scripting-damage--independent-ownership:

Independent ownership
---------------------

Collision damage needs an impact measure rather than simply the vehicle's speed. Contact-normal relative motion distinguishes a head-on impact from moving quickly along a wall. Scripted damage already supplies an amount, so it should not be accidentally scaled again by a response intended only for native collisions.

Keep presentation and gameplay state separate in consumers too. A dent is a mesh change, a hit is an accepted damage event and detachment is an ownership change. A hit effect may happen before the mesh upload, while a repair screen may need to inspect the final geometry.

``Body`` operates ``VehicleBodyPart`` entries by case-sensitive ID. ``Damage`` routes copied collision/scripted impacts to ``DamagePart`` boundaries and optional ``VehicleMeshDeformation``. An opening hinge is not itself a health/detachment policy.

Collision severity uses contact-normal relative speed above threshold, not tangential travel speed. Scripted ``ApplyImpact`` supplies its own amount and does not pass through collision-only target response scaling. ``damageEnabled``, ``deformationEnabled`` and ``detachmentEnabled`` are independent policy gates for accepted hits.

.. _uvs-scripting-damage--open-a-named-part:

Open a named part
-----------------

Treat a part ID as an authored contract between the vehicle prefab and application interaction. The adapter returns the action result so a missing, disabled or released door does not appear to open successfully. Keep door-specific UI text and interaction selection outside the body mechanism.

When creating reusable prefabs, choose consistent IDs for equivalent parts. This lets the same application adapter operate several vehicles through configuration rather than searching transform names or hard-coding mesh hierarchy paths.

Assign the ``Body`` and the ID from **Vehicle Body Part > Part Id**, or resolve the module with ``vehicle.parts``. A missing Body/part, a disabled Body module or a released part returns ``false``; a directly addressed disabled VehicleBodyPart can retain its request until it resumes stepping. See :ref:`the vehicle entry points <uvs-scripting--what-is-available-directly-on-vehicle>` and :ref:`Body shortcut usage <uvs-movingparts--operate-it>`.

**Example:** ``BodyPartControl.cs``

.. raw:: html

   <!-- example: BodyPartControl.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class BodyPartControl : MonoBehaviour
       {
           public UltraVehicleSystem.Body body;
           public string partId = "Door";
           public bool Open() => body && body.Open(partId);
           public bool Close() => body && body.Close(partId);
       }
   }

.. _uvs-scripting-damage--read-requested-state-and-actual-position:

Read requested state and actual position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Call ``body.GetPart(partId)`` once for the operation, check the result, then read the returned ``VehicleBodyPart``. A successful Open/Close result means the request was accepted, not that the door has already arrived. ``Body`` is the ID-based controller; state and movement events belong to each individual part.

+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| State                              | Meaning                                                                                                                   |
+====================================+===========================================================================================================================+
| ``part.IsOpen``                    | Requested open endpoint, rather than actual clearance.                                                                    |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``part.IsOpening`` / ``IsClosing`` | Pending opening/closing operation. Use completion events to react to arrival.                                             |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``part.NormalizedPosition``        | Actual/reported travel in 0..1, including Translation, Animation and Custom.                                              |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``part.CurrentAngle``              | Measured hinge angle in degrees. Use it for a rotational hinge, not as the progress of a sliding window or skeletal clip. |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``part.IsReleased``                | Hinge ownership was released; ordinary open/close actions are no longer accepted.                                         |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``part.IsImpactUnlatched``         | Impact loosened the latch while the part may still be attached. This is separate from detachment.                         |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``part.usePhysics``                | Physical hinge policy, used in Rotation mode.                                                                             |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

For a gameplay action such as allowing boarding after a door opens, subscribe to ``OpeningCompleted`` rather than waiting a guessed duration or testing IsOpen immediately after Open. For a blocked physical door, the request and actual angle can remain different. See the :ref:`operation lifecycle <uvs-scripting-damage--body-part-operation-lifecycle>` and :ref:`subscription example <uvs-scripting-movingparts--subscribe-to-operation-events-and-configure-cues>`.

.. _uvs-scripting-damage--choose-the-impact-notification:

Choose the impact notification
------------------------------

+---------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Need                                                                | Observe                                                          | Interpretation                                                                                                                                                                 |
+=====================================================================+==================================================================+================================================================================================================================================================================+
| React to a vehicle root collision independently of built-in damage  | ``vehicle.Impacted`` (``Impact``)                                | Copied contact snapshot; available without a Damage module. It is not a promise that damage was applied.                                                                       |
+---------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Inspect every native contact of that root collision                 | ``vehicle.Collided`` (``Collision``)                             | Live Unity collision data, valid during the callback. Do not retain it for later work.                                                                                         |
+---------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| React to damage that passed the built-in policy and selected a part | ``Damage.Hit`` (``DamageHit``)                                   | Accepted amount and selected DamagePart, including scripted hits. One physical impact can produce several Hit callbacks if multiple parts are affected, or none when rejected. |
+---------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Observe the part's damage counter or detachment/repair              | ``DamagePart.Damaged``, ``Detached``, ``Repaired``, ``Restored`` | Part-specific state changes. Read ``DamagePart.Damage`` and ``IsDetached``.                                                                                                    |
+---------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Inspect uploaded dented mesh geometry                               | ``VehicleMeshDeformation.DeformationChanged``                    | Geometry update, which may occur later than Hit.                                                                                                                               |
+---------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

``Impacted`` and ``Collided`` are root ``OnCollisionEnter`` notifications, not continuous OnCollisionStay events. Separately simulated hinged parts may use ``DamageCollisionRelay`` to call ``Damage.ReceiveImpact`` directly; such relayed damage is visible through Damage.Hit, without another root Impacted event. Do not assume both events fire for every contact or use their subscription order as a damage-completion guarantee. See :ref:`event timing <uvs-scripting-events--choose-the-observation-point>`.

.. _uvs-scripting-damage--handle-a-physical-impact-in-your-own-script:

Handle a physical impact in your own script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Attach this observer to a gameplay/controller object, assign its Vehicle reference, and put your reaction in the accepted-impact branch. It records contact data and filters by speed into the surface normal. It does not change built-in damage or apply a second hit.

.. raw:: html

   <!-- example: VehicleImpactReaction.cs -->

.. code-block:: csharp

   using UltraVehicleSystem;
   using UnityEngine;

   public sealed class VehicleImpactReaction : MonoBehaviour
   {
       public VehicleController vehicle;
       [Min(0)] public float minimumNormalSpeed = 3;
       public Impact LastImpact { get; private set; }
       public float LastNormalSpeed { get; private set; }
       public int ReactionCount { get; private set; }
       private VehicleController subscribed;

       private void OnEnable()
       {
           subscribed = vehicle;
           if (subscribed) subscribed.Impacted += OnImpact;
       }

       private void OnDisable()
       {
           if (subscribed) subscribed.Impacted -= OnImpact;
           subscribed = null;
       }

       private void OnImpact(Impact impact)
       {
           if (!impact.HasContact) return;
           float speed = Mathf.Abs(Vector3.Dot(impact.RelativeVelocity, impact.Normal));
           if (speed < minimumNormalSpeed) return;
           LastImpact = impact;
           LastNormalSpeed = speed;
           ReactionCount++;
           // Your camera shake, gameplay notification or custom damage decision goes here.
           // Do not forward this same hit to Damage when its built-in listener already handles it.
       }
   }

``Impact.Point`` and ``Normal`` are world-space contact information; ``RelativeVelocity`` is in m/s, and ``Impulse`` is a vector in N·s. ``SelfCollider`` identifies the owned shape and ``OtherCollider`` the external shape. The copied numeric values can be retained; referenced colliders may later be destroyed, so check them before use. ``HasTelemetry`` guards the latest completed vehicle snapshot in ``Telemetry``; that snapshot is not a new measurement taken at the exact instant of contact. See :ref:`Impact API <uvs-api-events--impact>`.

This example counts root impact notifications, not damaged parts. It intentionally does not reproduce Damage's wheel-support, self-contact, threshold, radius or material rules. Add application-specific filters before using it as an alternative damage policy.

.. _uvs-scripting-damage--observe-accepted-damage:

Observe accepted damage
-----------------------

The sample captures the subscribed publisher separately from its editable reference and removes that exact subscription on disable. ``DamageHit`` supplies the accepted amount, so the observer does not attempt to recompute collision severity from vehicle speed.

Use ``Hit`` for gameplay notifications or accumulated statistics. Use the geometry-change notification when a consumer must inspect uploaded vertices. Keeping those consumers on the appropriate event avoids forcing an immediate mesh upload for every accepted collision.

``Damage.Hit`` provides ``DamageHit`` (part, point, direction and amount). It occurs when damage is accepted; a mesh upload can occur later in ``LateUpdate``. Use ``DeformationChanged`` when inspecting uploaded geometry. Subscribe with a named handler and release the same captured source.

**Example:** ``DamageObserver.cs``

.. raw:: html

   <!-- example: DamageObserver.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class DamageObserver : MonoBehaviour
       {
           public Damage damage;
           public float AcceptedDamage { get; private set; }
           private Damage subscribed;

           private void OnEnable()
           {
               subscribed = damage;
               if (subscribed) subscribed.Hit += OnHit;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.Hit -= OnHit;
               subscribed = null;
           }

           private void OnHit(DamageHit hit)
           {
               AcceptedDamage += hit.Amount;
               // hit.Part identifies the accepted boundary; hit.Point is a world position.
               // Use hit.Part.Damage / IsDetached for current part state after damage routing.
               // Place application-specific glass, health, UI or mechanical-failure logic here.
           }
       }
   }

.. _uvs-scripting-damage--use-accepted-damage-or-replace-the-policy:

Use accepted damage or replace the policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Add a reaction:** keep built-in Damage enabled and subscribe to Hit as above. ``hit.Amount`` is already scaled gameplay severity. Do not apply it again to the part from the observer. Hit runs after its part's counter update and the built-in detachment decision; visual mesh upload can still be pending.
-  **Read physical measurements:** test ``hit.HasPhysicalImpact`` before using ``ImpactSpeed`` (normal collision speed in m/s), ``Impulse`` (magnitude in N·s) or ``Force`` (average impulse/timestep in N). A simple scripted hit has no such metadata. Use ``HasTelemetry`` before reading its cached vehicle snapshot.
-  **Scale collisions against a particular target:** implement ``ICollisionDamageResponse`` on the external struck collider's hierarchy. Its ``CollisionDamageScale`` (0..1) scales collision speed before the built-in threshold. It does not change native collision forces, raw Impact notifications, or scripted ApplyImpact amounts. See :ref:`the response interface <uvs-api-damage--icollisiondamageresponse>`.
-  **Own the damage calculation:** disable/remove the built-in Damage module and handle root Impacted notifications yourself, to supply your complete policy. Root Impacted alone does not replace child-rigidbody relays; preserve the needed collision collection explicitly. To replace only the processing of already admitted hits, derive from Damage and override its protected virtual ``ApplyImpactCore(...)``; the built-in collision admission/thresholds still apply before this hook. Use protected ``RaiseHit`` when your replacement should publish Damage.Hit notifications. Keep one damage owner per impact.
-  **Inject a projectile/explosion hit:** call ``Damage.ApplyImpact(point, direction, amount)`` on the enabled registered Damage module. The amount is application severity, not an automatic force or speed. The module still applies its configured multiplier, radius/part admission and gates, so it may affect several parts or none. Use the physical-metadata overload only when those measurements are known. ``ReceiveImpact(Impact)`` instead runs the collision policy and thresholds. Do not forward a root collision that the built-in Damage subscription already receives.

Full signatures and repair operations remain in the :ref:`public index <uvs-scripting-damage--complete-public-method-and-event-index>`. Damage.Hit is a C# event; use a small observer such as DamageObserver to bridge it to your own Inspector UnityEvent when needed. The motion components' Inspector callbacks do not imply that Damage exposes the same serialized event fields.

.. _uvs-scripting-damage--geometry-and-restoration:

Geometry and restoration
------------------------

``VehicleMeshDeformation`` owns runtime copies of readable ``MeshFilter`` meshes and changes vertices around accepted impacts. It retains rest geometry so a dent is bounded relative to the original shape and can be restored later. This avoids progressively treating an already-dented mesh as a new unbounded baseline. Reused vertex buffers are uploaded in ``LateUpdate``; native collision proxies do not continuously deform with every visual vertex, and skinned meshes are outside this path.

Use ``Deform`` when supplying a custom local mesh impact and ``RestoreShape`` when resetting the owned geometry. A ``Damage`` integration normally routes accepted hits to it. ``DeformationChanged`` follows geometry update; ``Restored`` reports restoration. Choose these events when a renderer/tool must inspect shape rather than reacting merely to a hit.

Configure ``DamagePart.detachedVehicleColliders`` before startup to enable permanent chassis shapes when a panel releases. Keep those collider GameObjects active, their colliders disabled, and outside detachable groups, with one owner per collider. Activation precedes ``Detached``; full repair restores captured enabled states before ``Restored``. Parent-group release also activates nested parts' configured shapes. This performs work on release/repair only. See :ref:`exposed chassis setup <uvs-damage--protect-exposed-chassis-after-detachment>`.

``DamagePart`` owns the part's counter and detachment threshold. ``ReceiveDamage`` evaluates that counter, ``Repair(amount)`` removes damage and returns the actual repaired amount, and ``Detach`` changes object ownership. RepairFully coordinates remounting a retained object, restoring its part meshes and clearing damage. Destroyed objects still need an application reconstruction policy.

A restoration policy should state what “repair” includes. Resetting a counter makes a damage part eligible for future hits but does not recreate a missing object. Restoring vertices removes dents but does not reattach debris. Teleporting a vehicle changes pose without rebuilding its authored hierarchy.

For pooling, retain the required part instances and call RepairAll before returning the vehicle to play, or recreate destroyed objects through your pool. For a persistent world, the application may instead leave detached debris alive. Those are application lifetime choices; the local damage mechanic cannot infer them.

``DamagePart.Repair(amount)`` reduces an attached part’s counter and VehicleMeshDeformation.RestoreShape restores geometry only. Use RepairFully/RepairAll to remount retained debris, or VehicleController.ResetVehicle for repair plus a pose/passenger reset. Teleport alone remains pose-only.

Detached parts inherit motion and remain physical. Collision-clearance policy delays recontact with the former owner. ``ICollisionDamageResponse`` changes collision damage severity only; it does not change scripted amount, target mass or all physical contacts.

.. _uvs-scripting-damage--custom-impact-effect:

Custom impact effect
--------------------

Implement the callback interface on a component inside the profile's pooled prefab. The pool activates the object before PlayImpact and calls StopImpact before returning or replacing it. The lease is controlled by Effect Lifetime, not by your callback. Keep callbacks allocation-free and reset state for the next hit.

.. raw:: html

   <!-- example: ImpactLight.cs -->

.. code-block:: csharp

   using UltraVehicleSystem;
   using UnityEngine;

   public sealed class ImpactLight : MonoBehaviour, IDamageImpactEffect
   {
       [SerializeField] private Light flash;
       public void PlayImpact(DamageHit hit, float intensity)
       {
           if (flash) { flash.intensity = Mathf.Lerp(1f, 5f, intensity); flash.enabled = true; }
       }
       public void StopImpact()
       {
           if (flash) flash.enabled = false;
       }
   }

DamageHit keeps Part, Point, Direction and Amount and adds HasPhysicalImpact, ImpactSpeed (m/s), Impulse (N·s) and Force (N). The original constructor and ApplyImpact(point, direction, amount) create severity-only hits. The overload with physical values validates finite, nonnegative metadata. Force from Unity collisions is average impulse/timestep, not peak force. Use DamageFeedback.ResolveImpactProfile(hit) for threshold-aware selection; the part-only overload matches materials without evaluating severity.

On DamageFeedback, TryPlayEffect(hit) requests visuals without applying damage. EffectPlayed fires only for an accepted visual lease. ActiveEffectCount reports occupied slots; PlayedEffectCount counts starts and DroppedEffectCount counts requests rejected by the visual pool, including cooldown/capacity. Hit reports gameplay damage independently of whether a presentation response played. WarmUpEffects rebuilds capacity; ClearEffects returns current effects; SetImpactEffectsEnabled toggles presentation only.

.. _uvs-scripting-damage--body-part-opening-and-closing-curves:

Body-part opening and closing curves
------------------------------------

VehicleBodyPart.openingMotionCurve and closingMotionCurve independently shape normalized time-to-progress. Speed sets average commanded degrees/second. For animated doors the curve controls the pose; for physical doors it controls the spring target, leaving actual motion to the hinge solver. SetOpen restarts from the current actual angle only when the requested state changes. IsOpen remains the request flag, rather than an arrival notification. See :ref:`movement curves <uvs-movingparts--shape-movement-speed-with-curves>`.

.. _uvs-scripting-damage--body-part-operation-lifecycle:

Body-part operation lifecycle
-----------------------------

VehicleBodyPart exposes ``OpeningStarted``, ``OpeningCompleted``, ``ClosingStarted`` and ``ClosingCompleted`` as C# events and matching Inspector callbacks at the bottom of the component in this order: **Motion Events → Signals and callbacks → Gizmos**. See the existing :ref:`complete subscription example <uvs-scripting-movingparts--subscribe-to-operation-events-and-configure-cues>`, rather than installing another independent movement timer.

``OpenChanged(bool)`` reports the requested open/closed state, ``PhysicsChanged(bool)`` a physics-policy change, and ``Released`` the end of hinge ownership. ``MotionOccurred(PartMotionEvent)`` provides the four start/arrival cues through one event. ``Signals`` exposes the common lifecycle, including stop/cancel; its complete :ref:`callback table <uvs-movingparts--lifecycle-and-inspector-callbacks>` also covers Animation and Custom.

In Rotation, completion uses CurrentAngle and completionTolerance, so a physical hinge blocked by a collision does not publish success merely because its spring command finished. Translation/Animation use normalized arrival; Custom requires the external implementation to report progress and complete. Release cancels pending completion. See :ref:`the moving-parts guide <uvs-movingparts--motion-events-and-four-audio-cues>` for interruption, sound and source-ownership rules.

.. _uvs-scripting-damage--repair-a-wheel-or-reset-the-whole-vehicle:

Repair a wheel or reset the whole vehicle
-----------------------------------------

See :ref:`wheel setup and repair tutorials <uvs-damage--detachable-wheels>`. Repair methods operate on retained components and require no new damage admission. Use the ID on DamagePart/WheelPart, not a GameObject name or Wheel Setup label.

.. raw:: html

   <!-- example: VehicleRepairActions.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class VehicleRepairActions : MonoBehaviour
       {
           public VehicleController vehicle;
           public Transform respawn;
           public string wheelId = "WheelFrontLeft";

           public bool RepairWheel() => vehicle && vehicle.RepairPart(wheelId);
           public void RepairAll() { if (vehicle) vehicle.RepairAll(); }
           public void FullReset()
           {
               if (vehicle && respawn) vehicle.ResetVehicle(respawn.position, respawn.rotation);
           }
       }
   }

``WheelPart`` is a DamagePart subtype and belongs to the same Damage.Parts / Body.DamageParts registry. Its native Wheel adapter stays on the suspension mount. Read Wheel.Attached and subscribe to Wheel.AttachmentChanged or VehicleController.WheelAttachmentChanged to observe release/reconnection; use the part-level APIs to physically detach/remount it.

.. _uvs-scripting-damage--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed body operation and damage API </API/Damage>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _uvs-scripting-damage--body:

Body
~~~~

:ref:`Body <uvs-api-damage--body>` gives the full declared contract.

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Method                                                      | Role                                                                                                                             |
+=============================================================+==================================================================================================================================+
| ``public virtual VehicleBodyPart GetPart(string id)``       | Finds the authored body part by its case-sensitive ID.                                                                           |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Open(string id)``                     | Requests opening of this part or the body part selected by ID.                                                                   |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Close(string id)``                    | Requests closure of this part or the body part selected by ID.                                                                   |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Toggle(string id)``                   | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                              |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetPhysics(string id, bool enabled)`` | Looks up the case-sensitive part ID and requests that part's physics policy, returning ``false`` when no eligible target exists. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetOpen(string id, bool open)``       | Requests a body part's open/closed target.                                                                                       |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void OpenAll()``                           | Requests opening of every eligible authored body part.                                                                           |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CloseAll()``                          | Requests closure of every eligible authored body part.                                                                           |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-scripting-damage--damage:

Damage
~~~~~~

:ref:`Damage <uvs-api-damage--damage>` gives the full declared contract.

-  ``public event Action<DamageHit, float> DeformationRequested`` — Accepted hit and radius before part detachment; optional deformation receivers process it synchronously.
-  ``public event Action EffectsCleared`` — Requests clearing optional impact presentation.
-  ``public event Action FullyRepaired`` — Current fully repaired.
-  ``public event Action<DamageHit> Hit`` — // Reports each accepted copied damage hit after its target part and severity are resolved.
-  ``public event Action PartsChanged`` — Reports that the damage boundary list has been refreshed.
-  ``public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount)`` — Current apply impact.
-  ``public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount, float impactSpeed, float impulse, float force)`` — Current apply impact.
-  ``public virtual void ClearEffects()`` — Stops all pooled impact effects.
-  ``public override void Configure(VehicleController vehicle)`` — Binds the component to its configured owner and selected source.
-  ``public virtual DamagePart GetPart(string id)`` — Current get part.
-  ``public virtual void ReceiveImpact(Impact impact)`` — // Accepts a copied impact snapshot and routes it through this component's damage policy.
-  ``public virtual void RefreshParts()`` — Current refresh parts.
-  ``public virtual void RepairAll()`` — Current repair all.
-  ``public virtual bool RepairPart(DamagePart part)`` — Current repair part.
-  ``public virtual bool RepairPart(string id)`` — Current repair part.

.. _uvs-scripting-damage--damagefeedback:

DamageFeedback
~~~~~~~~~~~~~~

See :doc:`setup and examples </DamageFeedback>` and the :ref:`full API <uvs-api-damagefeedback--damagefeedback>`.

-  ``public event Action<DamageContact> Impacted``
-  ``public event Action<DamageContact> Scraped``
-  ``public event Action Cleared``
-  ``public event Action<DamageContact> Contacted``
-  ``public event Action<DamageHit, DamageImpactProfile> EffectPlayed``
-  ``public void SetImpactEffectsEnabled(bool value)``
-  ``public void WarmUpEffects()``
-  ``public DamageImpactProfile ResolveImpactProfile(DamagePart part)``
-  ``public DamageImpactProfile ResolveImpactProfile(DamageHit hit)``
-  ``public bool TryPlayEffect(DamageHit hit)``
-  ``public override void Configure(VehicleController owner)``
-  ``public void ClearEffects()``
-  ``public static DamageContact FromDamageHit(DamageHit hit)``
-  ``public void ResetVehicleState(VehicleResetReason reason)``
-  ``public void ClearState()``
-  ``public bool SubmitContact(DamageContact sample)``
-  ``public DamageSurfaceType ClassifyContact(DamageSurfaceQuery contact)``
-  ``public DamageFeedbackProfile ResolveContactResponse(DamageSurfaceQuery query)``
-  ``public override void Step(VehicleController owner, Command command, float dt)``

.. _uvs-scripting-damage--damageimpactprofile:

DamageImpactProfile
~~~~~~~~~~~~~~~~~~~

:ref:`DamageImpactProfile <uvs-api-damage--damageimpactprofile>` gives the full declared contract.

-  ``public virtual bool Matches(DamagePart part)`` — Current matches.
-  ``public virtual bool TryEvaluate(DamageHit hit, out float intensity)`` — Current try evaluate.

.. _uvs-scripting-damage--damagepart:

DamagePart
~~~~~~~~~~

:ref:`DamagePart <uvs-api-damage--damagepart>` gives the full declared contract.

-  ``public event Action<DamagePart, float> Damaged`` — Current damaged.
-  ``public event Action<DamagePart> Detached`` — // Reports this part after it becomes independent physical debris.
-  ``public event Action<DamagePart, float> Repaired`` — Current repaired.
-  ``public event Action<DamagePart> Restored`` — Current restored.
-  ``public virtual bool Detach(Rigidbody vehicleBody)`` — Current detach.
-  ``public virtual void ReceiveDamage(float amount)`` — // Accumulates finite positive damage only while the part is attached and then publishes the accepted amount.
-  ``public virtual float Repair(float amount)`` — Current repair.
-  ``public virtual bool RepairFully()`` — // Full repair is deliberately separate from incremental Repair(amount).

.. _uvs-scripting-damage--idamageimpacteffect:

IDamageImpactEffect
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+--------------------------------------------------------------------------+
| Signature                                           | Behavior                                                                 |
+=====================================================+==========================================================================+
| ``void PlayImpact(DamageHit hit, float intensity)`` | Initializes a leased effect using hit metadata and normalized intensity. |
+-----------------------------------------------------+--------------------------------------------------------------------------+
| ``void StopImpact()``                               | Resets a pooled effect before return or replacement.                     |
+-----------------------------------------------------+--------------------------------------------------------------------------+

.. _uvs-scripting-damage--ivehiclemodule:

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

.. _uvs-scripting-damage--vehiclebodypart:

VehicleBodyPart
~~~~~~~~~~~~~~~

:ref:`VehicleBodyPart <uvs-api-damage--vehiclebodypart>` gives the full declared contract.

-  ``public event System.Action ClosingCompleted`` — Current closing completed.
-  ``public event System.Action ClosingStarted`` — Current closing started.
-  ``public event System.Action MotionAudioStopped`` — Requests stopping movement audio after interruption or disable.
-  ``public event System.Action<PartMotionEvent> MotionOccurred`` — Reports an admitted movement phase to optional presentation receivers.
-  ``public event System.Action<bool> OpenChanged`` — // Reports a changed open/closed request rather than physical hinge arrival.
-  ``public event System.Action OpeningCompleted`` — Current opening completed.
-  ``public event System.Action OpeningStarted`` — Current opening started.
-  ``public event System.Action<bool> PhysicsChanged`` — Current physics changed.
-  ``public event System.Action Released`` — // Notifies observers after hinge ownership is permanently released.
-  ``public virtual void Close()`` — Current close.
-  ``public virtual void Open()`` — Current open.
-  ``public virtual void RefreshIgnoredCollisions()`` — Current refresh ignored collisions.
-  ``public virtual void Release()`` — Current release.
-  ``public virtual void RepairFully()`` — Current repair fully.
-  ``public virtual void SetOpen(bool value)`` — Current set open.
-  ``public virtual void SetPhysics(bool value)`` — Current set physics.
-  ``public virtual void StartMotion(float value)`` — Requests open for values at least 0.5, otherwise closed; BodyPart still has two requested endpoints.
-  ``public virtual void ReportProgress(float value)`` — Reports actual normalized Custom progress without writing the pose.
-  ``public virtual void CompleteCustomMotion()`` — Publishes successful Custom completion after the external implementation arrives.
-  ``public virtual void Stop()`` — Stops the current operation at its reported position, without completion.
-  ``public virtual void Cancel()`` — Cancels the current operation at its reported position, without completion.
-  ``public virtual void Tick(float deltaTime)`` — Owner-supplied motion step; do not add another Tick loop beside the component's normal FixedUpdate.
-  ``public virtual void GetTranslationFrame(out Vector3 origin, out Vector3 direction)`` — Returns the neutral world origin and axis used by translational body panels.
-  ``public virtual void Toggle()`` — Current toggle.
-  ``public virtual bool TryUnlatchFromImpact(float force, float speed)`` — // force: average contact force in N; speed: approach speed along the impact normal in m/s.

.. _uvs-scripting-damage--vehiclemeshdeformation:

VehicleMeshDeformation
~~~~~~~~~~~~~~~~~~~~~~

:ref:`VehicleMeshDeformation <uvs-api-damage--vehiclemeshdeformation>` gives the full declared contract.

-  ``public event System.Action DeformationChanged`` — // Notifies observers after accumulated vertex changes are uploaded.
-  ``public event System.Action Restored`` — // Notifies observers after original mesh shapes are restored.
-  ``public override void Configure(VehicleController owner)`` — Binds the component to its configured owner and selected source.
-  ``public virtual void Deform(DamageHit hit, float radius, float dentPerDamage, float maximumDent)`` — // Displaces vertices near the damage point, caps displacement from their rest positions and defers mesh upload.
-  ``public virtual void FlushPendingDeformation()`` — Current flush pending deformation.
-  ``public virtual void RestoreShape()`` — Current restore shape.
-  ``public virtual void RestoreShape(DamagePart part)`` — Current restore shape.

.. _uvs-scripting-damage--vehiclemodule:

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

.. _uvs-scripting-damage--wheelpart:

WheelPart
~~~~~~~~~

:ref:`WheelPart <uvs-api-damage--wheelpart>` gives the full declared contract.

-  ``public override bool Detach(Rigidbody vehicleBody)`` — Current detach.

``Damage.Hit`` and ``DeformationRequested`` include ``DamageHit.Telemetry``, the vehicle’s latest completed telemetry snapshot. Check ``HasTelemetry`` for manually constructed hits. Collision-time speed, force and impulse remain separate impact fields; the cached telemetry can precede the contact callback.
