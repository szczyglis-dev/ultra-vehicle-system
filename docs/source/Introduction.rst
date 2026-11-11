.. _uvs-introduction--introduction-and-quick-start:

Introduction and quick start
============================

Build a vehicle from reusable mechanics, model controls and presentation components. Start with a drive mode, configure the model and wheels, then add the systems your game needs.

.. _uvs-introduction--first-vehicle:

First vehicle
-------------

1. :doc:`Install and create a working car </GettingStarted>`.
2. :doc:`Check the model hierarchy and pivots </VehicleModelConvention>`.
3. :doc:`Connect your controls </Input>`.
4. :doc:`Tune mass, suspension and handling </VehicleTuning>`.
5. :doc:`Choose optional systems </ChoosingSystems>`.

For a working example, open the supplied :doc:`Demo scene </Demo>`. If something does not work, use :doc:`Troubleshooting </Troubleshooting>`.

.. _uvs-introduction--setup-guides:

Setup guides
------------

+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Task                                            | Guides                                                                                                                                                                                                                                                                                           |
+=================================================+==================================================================================================================================================================================================================================================================================================+
| Configure the Inspector and prefab              | :doc:`Vehicle configuration </Configuration>`, :doc:`Inspector options </InspectorConfiguration>`                                                                                                                                                                                                |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Understand the controller and module categories | :doc:`Modules and architecture </ModulesAndArchitecture>`                                                                                                                                                                                                                                        |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Choose speed authoring and display units        | :doc:`Speed units </SpeedUnits>`                                                                                                                                                                                                                                                                 |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Choose movement and change modes                | :doc:`Drive profiles </DriveProfiles>`, :doc:`Combined vehicles </CombinedVehicles>`                                                                                                                                                                                                             |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configure a drivetrain                          | :doc:`Gearbox </Gearbox>`, :doc:`Clutch </Clutch>`, :doc:`Differential </Differential>`, :doc:`Traction control </TractionControl>`                                                                                                                                                              |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configure wheels and ground contact             | :doc:`Suspension </Suspension>`, :doc:`Contact envelope </ContactEnvelope>`, :doc:`Solid tire contacts </TireCollision>`, :doc:`Ground surfaces </Surfaces>`, :doc:`Tracked vehicles </Tracked>`                                                                                                 |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Build aircraft or water vehicles                | :doc:`Aircraft </Aircraft>`, :doc:`Boat </Boat>`, :doc:`Submarine </Submarine>`, :doc:`Water </Water>`                                                                                                                                                                                           |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Add orbit and cabin views                       | :doc:`Cameras and anchors </Cameras>`                                                                                                                                                                                                                                                            |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Add characters                                  | :doc:`Passengers </Passengers>`, :doc:`Seats </Seats>`, :doc:`Handles </Handles>`, :doc:`Hand grips </SteeringHandGrip>`, :doc:`Reusable hand positions </HandPositions>`, :doc:`Anatomical setup </HumanAnatomy>`, :doc:`Entry and exit </PassengerAccess>`                                     |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Add controls and displays                       | :doc:`Interior overview </Interior>`, :doc:`Control animators and instruments </InteriorControls>`, :doc:`Interaction gestures </ControlInteractions>`, :doc:`Custom animation and IK </HandleAnimation>`, :doc:`Mirrors, fuel and assists </InteriorSystems>`, :doc:`Exterior wipers </Wipers>` |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collisions and stabilization                    | :doc:`Collisions and stabilization </CollisionsAndStabilization>`                                                                                                                                                                                                                                |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Add body systems                                | :doc:`Moving parts </MovingParts>`, :doc:`Lights </Lights>`, :doc:`Damage </Damage>`, :doc:`Towing </Towing>`                                                                                                                                                                                    |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Add effects and weapons                         | :doc:`Audio </Audio>`, :doc:`Particles </Particles>`, :doc:`Tire marks </Decals>`, :doc:`Weapons </Weapons>`                                                                                                                                                                                     |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Plan deployment and performance                 | :doc:`Installation layouts </Distribution>`, :doc:`Performance </Performance>`, :doc:`Physics scope </Physics>`                                                                                                                                                                                  |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _uvs-introduction--programming:

Programming
-----------

Use the :doc:`Scripting Reference </Scripting/index>` for implementation contracts and complete C# examples. :doc:`Architecture </Architecture>` explains ownership and the execution pipeline; :doc:`Scripting </Scripting>` explains extension choices; :doc:`API </API>` is the public API map.

.. _uvs-introduction--supplied-content:

Supplied content
----------------

Vehicle names such as Car, Boat and Jet refer to example configurations in **Demo**. See :doc:`Demo resources </DemoResources>` for asset references and :doc:`Third-party credits </ThirdParty>` for attribution.

.. _uvs-introduction--reference-and-support:

Reference and support
---------------------

:ref:`Modules list <uvs-modulesandarchitecture--modules-list>` groups all runtime components by responsibility, with brief purposes and collaborators. Continue with :doc:`Performance </Performance>`, :doc:`Troubleshooting </Troubleshooting>` and the :doc:`Inspector reference </InspectorReference>` for tuning and individual settings.
