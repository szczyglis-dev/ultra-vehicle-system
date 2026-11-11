.. _uvs-speedunits--speed-units-kmh-mph-and-ms:

Speed units: km/h, mph and m/s
==============================

Configure vehicle speeds in the unit you prefer without changing the physical meaning of existing values. The package keeps one canonical stored value per setting and converts only at the authoring or output boundary.

.. _uvs-speedunits--inspector-authoring:

Inspector authoring
-------------------

Speed fields have a unit selector beside the numeric value. Choose **kmh**, **mph** or **mps** (km/h, mph or m/s), then enter the speed. Changing the selector converts the displayed number; it does not change the stored speed, dirty the scene or retune the vehicle. Numeric edits use normal Unity serialization, Undo and prefab overrides.

The selector is an editor-wide preference saved on your computer, shared by marked speed fields. It is independent of HUD units and is not a runtime setting. For example, a stored top speed of 160.9344 km/h displays as approximately 100 mph; entering 60 mph stores approximately 96.56064 km/h.

This covers shared top speed, forward gear speed-limit array entries and reverse limit, automatic reverse threshold, engine limiter fade ranges, motorcycle rider thresholds, brake feedback and audio ranges, commercial audio movement thresholds, tire corner-squeal threshold and the demo waypoint driver's speed and overspeed thresholds. Selected m/s tuning fields also use this authoring interface: aircraft speed limits/takeoff/reverse/reference speeds, tracked pivot speed, launch/parking/lean thresholds, passenger access maximum speed, feedback speed thresholds, rolling-surface audio references and water audio/particle speed references. Coefficients, ratios and angular speeds retain their own units.

Minimum limits are applied after converting back into the field's canonical unit. Merely switching units never clamps or rewrites values. Array entries use the same unit selector as scalar speeds; brake speed ranges convert both endpoints.

.. _uvs-speedunits--hud-and-instrument-outputs:

HUD and instrument outputs
--------------------------

On **HudDemo**, set **Speed Unit** in the Inspector to choose the dashboard readout and its label. The selection remains in effect when switching vehicles. **CarHud → Speed Unit** selects the number and label on the generated cockpit display. A supplied custom dashboard texture remains authored content.

**SpeedValueSource → Speed Unit** selects the instrument value; **Signed** controls whether reverse motion is negative. Calibrate the receiving needle's range/curve in the selected output unit. The default is Kph for all three components. These output choices are serialized per component, included in builds and independent of the editor authoring preference.

.. _uvs-speedunits--code-and-telemetry:

Code and telemetry
------------------

``VehicleController.SpeedKph`` and ``Telemetry.SpeedKph`` keep their km/h contract. Both also expose ``SpeedMph`` and ``GetSpeed(SpeedUnit unit)``. ``DirectionSelectionSpeedMph`` accompanies ``DirectionSelectionSpeedKph`` and uses the same planar speed calculation, excluding suspension bounce. ``ForwardSpeed``, velocity vectors and airspeed retain m/s contracts.

Use ``Settings.TopSpeedMph`` for convenient read/write top-speed tuning in mph. For every other configuration field, convert into its declared storage unit with ``SpeedUnits.Convert``. A field ending in Kph always stores km/h regardless of Inspector preference. Fields expressed in m/s store metres per second. Changing engine/gearbox setup still follows the normal :ref:`configuration contract <uvs-configuration--controller-tabs>`.

.. raw:: html

   <!-- example: SpeedUnitsExample.cs -->

.. code-block:: csharp

   using UnityEngine;
   using UltraVehicleSystem;

   public sealed class SpeedUnitsExample : MonoBehaviour
   {
       public VehicleController vehicle;

       public void ConfigureRoadSpeeds()
       {
           vehicle.settings.TopSpeedMph = 100;
           var gearbox = vehicle.GetComponent<AutomaticGearbox>();
           if (gearbox) {
               gearbox.gearSpeedLimitsKph = new[] {
                   SpeedUnits.Convert(25, SpeedUnit.Mph, SpeedUnit.Kph),
                   SpeedUnits.Convert(50, SpeedUnit.Mph, SpeedUnit.Kph),
                   SpeedUnits.Convert(100, SpeedUnit.Mph, SpeedUnit.Kph)
               };
           }
           vehicle.ApplyConfiguration();
       }

       public float ReadMilesPerHour() => vehicle.SpeedMph;
       public float ReadSnapshotMilesPerHour(Telemetry snapshot) => snapshot.SpeedMph;
       public float ReadMetresPerSecond() => vehicle.GetSpeed(SpeedUnit.MetresPerSecond);

       // Custom speed setting: its serialized number remains km/h.
       [Speed(minimum: 0)] public float cruiseSpeedKph = 50;
   }

See :doc:`conversion API </API/Units>` for the attribute and conversion signatures. Conversion retains negative signs, so the same helper works for signed speed and speed differences.
