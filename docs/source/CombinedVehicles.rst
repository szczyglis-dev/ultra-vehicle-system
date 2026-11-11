.. _uvs-combinedvehicles--combined-vehicles:

Combined vehicles
=================

Use separate registered drive configurations when one chassis can drive, hover, fly or move on water. This page owns profile registration, switching, transitions and input routing. Choose/configure each strategy in :doc:`Drive profiles </DriveProfiles>` and the corresponding vehicle-family guide before combining them.

.. _uvs-combinedvehicles--inspector-quick-start:

Inspector quick start
---------------------

1. Select the root and open **Modules > Controller > Profile Switcher**, adding it if absent. Keep the vehicle's Drive module enabled.
2. Expand **Profiles**, press **+** for each mode, give it a unique Id and choose/configure its drive profile in the entry. Configure supporting wheels, flight or water equipment before testing mode changes.
3. Check the current mode under **Setup > Drive mode** and its association with the switcher's active profile ID using the registration details below. Assign profile-pair transition components where needed. A transition reference supplies presentation; the profile still needs valid mechanics.
4. Configure the profile-switch action on the selected input source, apply/save, and test each mode separately followed by switching in both directions. Inspect wheel deployment/contact and camera/input state at each handover.

.. _uvs-combinedvehicles--set-up-a-profile-list:

Set up a profile list
---------------------

1. Add/enable registered ``ProfileSwitcher`` and keep an enabled registered ``Drive`` module.
2. Expand **Profiles** and create one slot per desired configuration.
3. Give every entry a unique, case-sensitive ID such as ``Drive``, ``Hover`` or ``Boat``, choose its profile and tune it.
4. Set **Active Profile Id** to the slot represented by the controller's current Drive mode, then apply vehicle configuration to reconnect that slot to the controller's strategy instance.
5. Test immediate switching without animation before adding transitions or multiple input sources.

Several slots can use the same profile class with independent settings. They are registrations of configuration instances, not merely labels in an enum. Keep references/IDs consistent when connecting switches and input routes.

``Toggle()`` advances in list order and wraps. ``SwitchTo(id)`` selects a named entry; a two-position control should normally select explicit IDs rather than rely on list order. Changing a registration list does not itself request a mode change.

.. _uvs-combinedvehicles--runtime-registry-operations:

Runtime registry operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``RegisterProfile``, ``UnregisterProfile``, ``SetProfiles`` and ``ClearProfiles`` rather than mutating an in-progress transition's list. Duplicate/invalid registrations and list changes during a transition are rejected. Removing an active registration leaves its current movement running; a later Toggle chooses the first remaining entry.

Do not use a successful registration result as proof a mode has started. Observe the switcher's/profile configuration state for the selected result. The :doc:`profile scripting guide </Scripting/DriveProfiles>` provides complete registry examples and lifecycle contracts.

.. _uvs-combinedvehicles--assign-transitions-to-profile-pairs:

Assign transitions to profile pairs
-----------------------------------

1. Add ``ProfileTransition`` or a suitable subclass to a helper object.
2. Set **From Profile Id** and **To Profile Id** to the exact registered IDs.
3. Add it to **ProfileSwitcher > Transitions**.
4. Enable **Bidirectional** if the same component handles the reverse pair.
5. Set **Duration**, optional **Forward Clip**/**Reverse Clip** and **Volume**.
6. Test both directions, then an unrelated pair that should not use this transition.

Exactly one enabled component may match a pair. Overlapping matches reject the switch; they are not combined in an arbitrary order. A pair without an enabled match switches immediately. A custom transition can reject admission through ``CanBegin``, for example when deployment would intersect another object.

The base transition can apply **Takeoff Velocity**, a world-up velocity change when leaving a wheel-based mode for a non-wheel mode. Set it to zero if that launch assistance is unwanted. Duration and sound are presentation/timing choices, not a reason to add a second movement controller writing the Rigidbody.

.. _uvs-combinedvehicles--road-and-hover-wheel-deployment:

Road and hover wheel deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``HoverDriveTransition`` for the folding/deployment sequence. Configure its model/wheel geometry, clearance and movement settings against the actual chassis. It coordinates wheel contact, folding and road restoration; do not separately enable the native wheel contacts halfway through its sequence.

The supplied Car/Porsche uses a bidirectional drive ↔ hover transition. That component does not imply every new profile pair should fold wheels. A separate boat/air configuration can have another transition or an immediate change.

Test a deployment on level ground, an incline and close to an obstacle, with enough space for the complete wheel path. Geometry that clears in the final pose can still intersect during folding. Save the neutral model/transition configuration outside Play Mode.

.. _uvs-combinedvehicles--route-controls:

Route controls
--------------

Use one input source that supplies all relevant channels, or an ``InputGate`` with routes keyed by registered **Profile Id**. Each route points to its compatible ``IVehicleInput`` component. Verify throttle/steering for the road mode and pitch/roll/lift/strafe channels where the other strategy uses them.

The gate changes the vehicle input source. It does not choose which network player owns the vehicle or which character camera should be active. Keep possession in the application, and avoid a second script continuously restoring the previous input source after each route change.

For a physical two-position selector, ``ProfileSwitchBinding`` maps explicit On/Off IDs. Its movement/interaction setup belongs to :ref:`Interior controls <uvs-interiorcontrols--bind-a-switch>`. Command sampling and keyboard/action mappings belong to :doc:`Input </Input>`.

.. _uvs-combinedvehicles--test-the-combined-vehicle:

Test the combined vehicle
-------------------------

+----------------------------------------------+------------------------------------------------------------------------+
| Symptom                                      | Check                                                                  |
+==============================================+========================================================================+
| Toggle selects the wrong mode                | Registration order versus explicit SwitchTo ID                         |
+----------------------------------------------+------------------------------------------------------------------------+
| Control switch springs back                  | Invalid ID, rejected transition or mechanic-state synchronization      |
+----------------------------------------------+------------------------------------------------------------------------+
| Switch fails only with animation installed   | Multiple matching transitions or CanBegin rejection                    |
+----------------------------------------------+------------------------------------------------------------------------+
| Correct profile but wrong controls           | InputGate route IDs, compatible source and competing source writer     |
+----------------------------------------------+------------------------------------------------------------------------+
| Wheels collide during folding                | Transition owns contacts; check geometry and duplicate contact control |
+----------------------------------------------+------------------------------------------------------------------------+
| Removing a profile leaves its motion running | Registry mutation is separate from selecting another strategy          |
+----------------------------------------------+------------------------------------------------------------------------+

For immediate versus animated switching and a multi-profile example, see :ref:`Profile scripting <uvs-scripting-driveprofiles--immediate-change-versus-animated-transition>` and :doc:`API </API/DriveProfiles>`.
