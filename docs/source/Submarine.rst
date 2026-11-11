.. _uvs-submarine--submarine-setup:

Submarine setup
===============

Choose **Submarine** for wheel-free underwater displacement, powered forward/reverse thrust, yaw, pitch and vertical movement. This page owns hull/control/depth-hold behavior; use :doc:`Water </Water>` for provider/render setup and :doc:`Boat </Boat>` for surface-boat handling.

.. _uvs-submarine--build:

Build
-----

1. Prepare a correctly scaled +Z-forward vehicle root with Rigidbody and a suitable hull collider.
2. Choose **Tools > UltraVehicleSystem > Add Vehicle > Submarine**, or set the existing controller's Drive mode. Keep ``Drive`` enabled/registered.
3. Set mass, centre of mass and **Hull Half Height**.
4. Configure WaterInteraction with an explicit provider, or the profile's fallback plane/bounds through the :doc:`water guide </Water>`.
5. Select a compatible input source with forward/reverse, steering/yaw, Lift, Pitch and Brake.
6. Begin fully submerged in calm water with modest speeds; verify passive displacement/resistance before depth hold and effects.

The hull collider handles shore, seabed and obstacles. The sampled water has a surface height; it does not by itself supply seabed clearance or a safe depth limit. Add the application collision/navigation rules your simulation needs.

.. _uvs-submarine--immersion-and-passive-behavior:

Immersion and passive behavior
------------------------------

**Hull Half Height** defines the surface transition around the centre of mass. Fully submerged, the model supplies displacement that balances its own gravity; near the surface, that support fades with immersion. This is not a ballast-tank/flooding simulation or a computed watertight hull volume.

Buoyancy and resistance continue with the engine off while valid water is sampled. Powered forward/lift/yaw control stops when an installed Engine is disabled/stopped. As with other FreeProfile strategies, no registered engine means externally powered operation rather than an implicit stopped engine.

Outside provider/fallback bounds or when dry, the profile supplies neither water buoyancy nor water propulsion and clears its captured depth state. A visible water mesh elsewhere does not replace an explicit dry sample. See :ref:`water sampling ownership <uvs-water--enable-or-disable-interaction>`.

To suspend vehicle forces and assistance, see :ref:`Release and restore all vehicle forces <uvs-driveprofiles--release-and-restore-all-vehicle-forces>`.

.. _uvs-submarine--connect-the-control-channels:

Connect the control channels
----------------------------

+----------------+-------------------------------------------------------------------------+
| Command        | Use                                                                     |
+================+=========================================================================+
| Throttle       | Signed forward/reverse thrust                                           |
+----------------+-------------------------------------------------------------------------+
| Steering / Yaw | Combined yaw demand; avoid double-feeding the same axis unintentionally |
+----------------+-------------------------------------------------------------------------+
| Lift           | Ascend/dive command, −1 to +1                                           |
+----------------+-------------------------------------------------------------------------+
| Pitch          | Requested nose attitude within Maximum Pitch                            |
+----------------+-------------------------------------------------------------------------+
| Brake          | Powered velocity-opposing response, 0–1                                 |
+----------------+-------------------------------------------------------------------------+

Use ``KeyboardSubmarineInput`` for the supplied adapter, configured ActionInput, or your own ``IVehicleInput`` implementation. Check actual bindings in :doc:`Input </Input>` and :doc:`Demo </Demo>` rather than assuming aircraft keyboard mappings are identical.

The profile applies pitch/vertical demand directly to the hull policy. A cockpit yoke/propeller moving does not generate those commands. Mark analog/digital metadata correctly where the input system uses it, and send neutral values when an application-owned control is released.

.. _uvs-submarine--tune-propulsion-and-resistance:

Tune propulsion and resistance
------------------------------

**Acceleration** scales forward thrust. **Vertical Acceleration** sets powered vertical authority and bounds depth-hold correction. Tune forward motion separately from vertical ascent/descent so a strong forward engine does not conceal insufficient hold authority.

**Drag**, **Lateral Resistance** and **Vertical Resistance** act in hull axes. **Quadratic Resistance** grows with water-relative speed. Greater resistance shortens drift/coast but also demands more thrust at speed; do not tune every axis by changing the same scalar.

Provider horizontal currents remain part of the water-relative calculation underwater. Vertical surface-wave motion fades with depth rather than heaving a deep hull as strongly as one near the surface. Test a still provider first, then an intentional current so data errors are not mistaken for unstable damping.

.. _uvs-submarine--depth-and-attitude:

Depth and attitude
------------------

.. _uvs-submarine--hold-depth:

Hold depth
~~~~~~~~~~

With **Hold Depth** enabled, manual Lift or Pitch temporarily takes control of depth. Forward/reverse thrust follows the hull, so a pitched bow also changes the direction of travel; depth hold remains suspended while that thrust has a vertical component. After the maneuver ends, hold captures the current centre-of-mass world height and corrects toward it within the available authority. The target belongs to the vehicle, not a shared profile setting.

Despite the name, this holds a captured **world height**, not a constant distance below each passing wave or above the seabed. A depth display derived from current surface height can therefore change while world height remains steady. It is also not a horizontal position lock: currents can still carry the hull sideways/forward.

The hold correction accounts for water drag without opposing an intentional pitched-thrust maneuver. Tune Vertical Acceleration with current/load conditions in mind. A hold request does not guarantee the hull has already reached its target, and an obstacle can prevent the requested motion.

Power loss or leaving valid water clears the captured hold. Re-entering/configuration/reset can reacquire a target rather than preserving another vehicle's depth. With Hold Depth off, the model retains passive displacement/resistance and responds to manual Lift while powered.

.. _uvs-submarine--pitch-and-yaw:

Pitch and yaw
~~~~~~~~~~~~~

**Maximum Pitch** sets the commanded attitude range; **Leveling Strength** and Angular Damping shape pitch/roll settling. Neutral pitch returns toward level rather than preserving every arbitrary nose angle indefinitely.

**Yaw Rate** is requested yaw speed in rad/s, and **Turn Response** controls how it approaches that rate. Steering plus Yaw is clamped, so feeding the same full demand into both is not extra unlimited authority. Test sustained turn, release and countersteer while level, then with pitch/Lift input.

.. _uvs-submarine--propeller-presentation:

Propeller presentation
----------------------

1. Add/configure ``Propulsion``, assign Engine where used and add the visible shaft in **Propellers**.
2. Set the shaft's **Local Axis**, fixed **Degrees Per Second** or **Use Engine Rpm / Rpm Ratio**.
3. Enable **Only With Thrust** to gate/scale motion by demand; enable **Reverse With Thrust** if signed propulsion should reverse it.
4. Enable **Only In Water** to stop the shaft when the hull is dry.
5. Use **Spin With Steering**, **Spin With Lift** and **Spin With Pitch** only for actuators that should visibly respond to those maneuver commands. **Maneuver Speed** controls their contribution.
6. Choose Spin Up/Down response, or **Instant Thrust Response** when the demand-driven mesh should match immediate thrust intent.

These settings animate the mesh and its shared presentation/spool; physical thrust comes from the profile. Only In Water tests valid water and hull immersion, not whether a particular visual propeller tip crossed the surface. Use a custom actuator presentation if you need per-propeller wet/dry geometry.

Submarine support does not use the surface Boat wake/splash channels. Configure underwater-specific audio/bubbles in your application or an appropriate extension rather than expecting BoatWaterParticles to classify a submerged vessel as a surface boat.

.. _uvs-submarine--test-and-diagnose:

Test and diagnose
-----------------

+--------------------------------------------------------+---------------------------------------------------------------------+
| Symptom                                                | Inspect                                                             |
+========================================================+=====================================================================+
| Hull floats differently near the surface               | Hull Half Height, centre of mass and partial immersion              |
+--------------------------------------------------------+---------------------------------------------------------------------+
| Depth hold drifts despite power                        | Vertical authority, currents, hull pitch and actual captured target |
+--------------------------------------------------------+---------------------------------------------------------------------+
| Height is stable but indicated depth changes           | Hold is world-height based; surface waves can move                  |
+--------------------------------------------------------+---------------------------------------------------------------------+
| Powered movement continues without an engine component | Absent engine uses externally powered policy                        |
+--------------------------------------------------------+---------------------------------------------------------------------+
| Shaft spins but hull does not move                     | Valid water/power/input/profile, independent of presentation        |
+--------------------------------------------------------+---------------------------------------------------------------------+
| Lift moves visually but no vertical command            | Input source channels versus cockpit animator                       |
+--------------------------------------------------------+---------------------------------------------------------------------+
| No surface wake/spray                                  | Expected: shared boat effects only use Boat profile contact         |
+--------------------------------------------------------+---------------------------------------------------------------------+

Test engine-off drift, forward/reverse coast, manual ascent/descent, Lift release hold, pitch changes and dry-boundary transitions. For sampling/depth/propeller contracts, see :doc:`Water scripting </Scripting/Water>` and :doc:`API </API/Water>`.
