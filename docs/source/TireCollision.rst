.. _uvs-tirecollision--solid-tire-contacts:

Solid tire contacts
===================

``TireCollision`` adds solid tire volumes for sidewalls, obstacles and unsupported tread contact. The native WheelCollider still supplies normal suspension/road traction where its centre contact is available. For smoother lower rolling support over curbs, use the complementary :doc:`ContactEnvelope </ContactEnvelope>`.

.. _uvs-tirecollision--inspector-quick-start:

Inspector quick start
---------------------

1. Select the root, configure radius/width/mass in **Wheels > Wheel Setup**, and apply configuration so the adapters/native contacts match.
2. Add/expand **Modules > Physics > Tire Collision**. Choose its geometry and supplemental-contact policies below. Let it own generated proxies rather than adding duplicate solid tires manually.
3. Check wheel-arch/chassis clearance at both steering locks and through suspension travel. Apply/save, then test side contact and an obstacle approach.
4. Compare native road support with supplemental contacts. For rolling-profile curb assistance, configure **Drive > Contact Envelope** separately.

.. _uvs-tirecollision--configure:

Configure
---------

1. Configure wheel radius, width and mass through **Wheel Setup** and apply the vehicle configuration.
2. Add/register TireCollision on the vehicle.
3. Inspect chassis and wheel-arch colliders at centred steering, both locks and full suspension travel. Leave real clearance for each tire volume.
4. Start with the default cylinder geometry/contact settings below.
5. Test slow curb/sidewall contact before landings and high-speed impacts.
6. Compare native road contact, supplemental tread contact and chassis collision in diagnostics.

Generated tire proxies are runtime helpers owned by the module. Configure the source module/wheel geometry rather than editing or saving generated proxy objects as a second independent wheel system.

.. _uvs-tirecollision--choose-the-collision-geometry:

Choose the collision geometry
-----------------------------

+--------------------------+----------------------------------------------------------------------+
| Setting                  | Purpose                                                              |
+==========================+======================================================================+
| Radius Scale             | Slightly reduces the supplemental volume relative to physical radius |
+--------------------------+----------------------------------------------------------------------+
| Cylinder Sides           | Number of sides in the generated convex tire approximation           |
+--------------------------+----------------------------------------------------------------------+
| Support Normal Threshold | Distinguishes supporting tread faces from other obstacle contacts    |
+--------------------------+----------------------------------------------------------------------+
| Tread Friction           | Friction used for supplemental loaded tread interaction              |
+--------------------------+----------------------------------------------------------------------+

A higher cylinder count smooths the approximation but increases geometry/contact cost. It is not a tread-block or tire-deformation model. Width comes from the wheel configuration, not from scaling a visual tire mesh during playback.

A small radius reduction helps avoid redundant supported-road contacts. Do not shrink it so far that the sidewall no longer matches the tire, or enlarge the tire to compensate for a wheel mount placed incorrectly.

.. _uvs-tirecollision--chassis-clearance-matters:

Chassis clearance matters
-------------------------

Use compound hull/body colliders that leave the wheel openings empty. A single box/convex hull can fill a visually open arch. The tire then collides with bodywork through normal travel even though the rendered meshes do not touch.

Check all steering/suspension extremes and moving gear states. TireCollision does not articulate a separate unsprung Rigidbody for each wheel; the wheel volume supplements the vehicle's existing physics arrangement. Do not add an independent dynamic tire body simply because a generated contact volume exists.

.. _uvs-tirecollision--road-support-versus-supplemental-contact:

Road support versus supplemental contact
----------------------------------------

The module avoids duplicating native/envelope-supported floor contact while retaining relevant obstacle/sidewall behavior. With ContactEnvelope enabled, solid tire extension also respects the remaining off-centre tread support at a ledge, including when the centre ray has no ground hit or already sees the lower road. This prevents the proxy from dropping through the upper lip and injecting a rigid depenetration impulse into the chassis. Supplemental tread friction/load is not another complete native wheel solver running in parallel.

``Wheel.Grounded`` includes recent loaded supplemental tread support. A true Grounded reading does not guarantee a detailed native ``WheelHit`` for every consumer. Automatic gearbox forward shifts still require loaded native road contact, so a supplemental-only edge touch need not trigger a shift.

Use **Tread Contact Count** and **Tread Impulse** for the module's published supplemental diagnostics, plus the vehicle's :ref:`per-wheel telemetry <uvs-scripting-events--diagnostic-snapshot>`. Contact count/impulse is not a direct tire-slip curve or a general damage-force threshold.

In direct pose control, the module supports the mode so it can suspend its physical proxies; commanded movement should not be interpreted as a physically solved obstacle response. See :doc:`Input </Input>` for direct-mode ownership.

.. _uvs-tirecollision--test-high-speed-contact-separately:

Test high-speed contact separately
----------------------------------

First eliminate overlap and incorrect dimensions. Then test the intended fixed timestep, collision detection and solver setup at representative speeds. A configuration that negotiates a slow curb does not guarantee reliable contact with a thin obstacle at every speed.

Avoid masking a bad chassis overlap by changing traction, engine torque or tire friction. Test an obstacle with no drive demand too, so a propulsion force does not obscure the collision response.

.. _uvs-tirecollision--troubleshoot:

Troubleshoot
------------

+-------------------------------------------+---------------------------------------------------------------------------+
| Symptom                                   | Inspect                                                                   |
+===========================================+===========================================================================+
| Vehicle jitters with no input             | Tire/chassis overlap and duplicate native/supplemental support            |
+-------------------------------------------+---------------------------------------------------------------------------+
| Sidewall hits before the visible tire     | Wheel width/radius, proxy scale and collider mount                        |
+-------------------------------------------+---------------------------------------------------------------------------+
| Visual wheel clips but no solid collision | Registered/enabled module, wheel availability and actual proxy dimensions |
+-------------------------------------------+---------------------------------------------------------------------------+
| Grounded true but no automatic shift      | Supplemental support is not loaded native road-speed evidence             |
+-------------------------------------------+---------------------------------------------------------------------------+
| Tire looks polygonal at obstacles         | Cylinder approximation versus performance budget                          |
+-------------------------------------------+---------------------------------------------------------------------------+
| Thin obstacles fail only at high speed    | Scene timestep/collision settings and obstacle geometry                   |
+-------------------------------------------+---------------------------------------------------------------------------+

For contact filtering, self-collision exclusions and supplemental force resolution, see :doc:`Wheel contact reference </Scripting/WheelContact>` and :doc:`API </API/WheelContact>`.
