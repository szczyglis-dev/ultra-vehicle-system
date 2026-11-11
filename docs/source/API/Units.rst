.. _uvs-api-units--units-api:

Units API
=========

Unit conversion and unit-aware Inspector authoring. Currently covers :doc:`speed units </SpeedUnits>`.

.. _uvs-api-units--types:

Types
-----

-  :ref:`SpeedAttribute <uvs-api-units--speedattribute>`
-  :ref:`SpeedUnit <uvs-api-units--speedunit>`
-  :ref:`SpeedUnits <uvs-api-units--speedunits>`

.. _uvs-api-units--speedattribute:

SpeedAttribute
--------------

**Runtime/Core/SpeedUnits.cs**

Marks a serialized float, float-array element or Vector2 speed range for the package Inspector drawer. Does not change runtime storage or serialization. Minimum applies in the storage unit; use it instead of combining Speed with a Min drawer.

**Inherits / implements:** ``PropertyAttribute``.

.. _uvs-api-units--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------+---------------------------------------------------------------+
| Member                                    | Meaning                                                       |
+===========================================+===============================================================+
| ``public float Minimum { get; }``         | Lower bound for numeric Inspector edits, in the storage unit. |
+-------------------------------------------+---------------------------------------------------------------+
| ``public SpeedUnit StorageUnit { get; }`` | Canonical serialized unit, default Kph.                       |
+-------------------------------------------+---------------------------------------------------------------+

.. _uvs-api-units--methods:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                                                | Role and behavior                                                                                   | Arguments and result |
+==========================================================================================================+=====================================================================================================+======================+
| ``public SpeedAttribute(SpeedUnit storageUnit = SpeedUnit.Kph, float minimum = float.NegativeInfinity)`` | Declares storage unit and optional minimum. Runtime assignments remain the caller's responsibility. | —                    |
+----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+----------------------+

.. _uvs-api-units--speedunit:

SpeedUnit
---------

**Runtime/Core/SpeedUnits.cs**

Supported linear-speed units. Default enum value is ``Kph`` for existing content.

+-----------------------------------------+------------------------------------+
| Value                                   | Meaning                            |
+=========================================+====================================+
| Kilometres per hour (``Kph``)           | Kilometres per hour, km/h.         |
+-----------------------------------------+------------------------------------+
| Miles per hour (``Mph``)                | International miles per hour, mph. |
+-----------------------------------------+------------------------------------+
| Metres per second (``MetresPerSecond``) | Metres per second, m/s.            |
+-----------------------------------------+------------------------------------+

.. _uvs-api-units--speedunits:

SpeedUnits
----------

**Runtime/Core/SpeedUnits.cs**

Stateless conversion; preserves signs. One international mile is exactly 1609.344 metres. Float conversions have normal floating-point rounding.

.. _uvs-api-units--methods-1:

Methods
~~~~~~~

+----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Signature                                                                  | Role and behavior                                                                                                                                                                     | Arguments and result |
+============================================================================+=======================================================================================================================================================================================+======================+
| ``public static float Convert(float value, SpeedUnit from, SpeedUnit to)`` | Converts a scalar linear speed between units. Identity conversion returns the original float. Invalid unit values throw ArgumentOutOfRangeException except on the identity fast path. | —                    |
+----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``public static string Symbol(SpeedUnit unit)``                            | Returns km/h, mph or m/s; invalid units throw ArgumentOutOfRangeException.                                                                                                            | —                    |
+----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
