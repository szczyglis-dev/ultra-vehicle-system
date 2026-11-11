.. _uvs-scripting-examples-index--scripting-examples:

Scripting examples
==================

One hundred standalone examples in ten categories. Each example solves a small application task and includes setup, behavior, comments and a complete C# component. They complement the implementation chapters with UI adapters, policies, measurements and gameplay exercises.

.. _uvs-scripting-examples-index--before-using-an-example:

Before using an example
-----------------------

-  Save each component in the named ``.cs`` file under your own ``Assets`` scripts folder, outside the package. All examples use the ``VehicleDocumentationExamples.Cookbook`` namespace. If you use an assembly definition, reference ``UltraVehicleSystem.Runtime`` and the Unity modules your component needs.
-  Assign scene references before enabling a component. Event examples assume their source reference remains fixed while enabled: disable the component before replacing a source, then enable it again.
-  UI examples expose public methods for buttons, sliders or your own action system. They do not require a particular keyboard binding. Invoke Unity APIs on Unity's main thread.
-  Each script owns only the request or presentation property described in its setup. Combine scripts deliberately: two input writers, beam policies or FOV writers can overwrite each other. Ordinary MonoBehaviours are not vehicle modules; the custom-module category explains installation and physics timing.
-  Interior animators here are vehicle-system control components, distinct from Unity's skeletal Animator. Sources supply values; control animators move equipment; handles coordinate limbs.

.. _uvs-scripting-examples-index--categories:

Categories
----------

+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| Category                                                                | Examples | Focus                                                                                |
+=========================================================================+==========+======================================================================================+
| :doc:`Commands and input </Scripting/Examples/Input>`                   | 10       | Adapters for UI, remote control and repeatable driving tests.                        |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Configuration and recovery </Scripting/Examples/Lifecycle>`       | 10       | Runtime configuration, checkpoints and module availability.                          |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Custom vehicle modules </Scripting/Examples/Modules>`             | 10       | Install these components through Add Module or your normal module registration flow. |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Driving challenges and gameplay </Scripting/Examples/Gameplay>`   | 10       | Small challenge rules driven by authoritative telemetry.                             |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Engine, fuel and boost </Scripting/Examples/Powertrain>`          | 10       | Gameplay policies around the existing engine and boost modules.                      |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Exterior equipment </Scripting/Examples/Exterior>`                | 10       | Small policies for lights, wipers and moving model parts.                            |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Interior data sources </Scripting/Examples/Interior>`             | 10       | Custom scalar sources plug into an interior animator’s data source field.            |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Passengers and handle interactions </Scripting/Examples/Handles>` | 10       | Application-level gestures share HandleController ownership with normal controls.    |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Presentation and diagnostics </Scripting/Examples/Presentation>`  | 10       | Observers for camera effects, trails and development tools.                          |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+
| :doc:`Telemetry and measurements </Scripting/Examples/Telemetry>`       | 10       | Read completed physics snapshots for game rules and presentation.                    |
+-------------------------------------------------------------------------+----------+--------------------------------------------------------------------------------------+

.. toctree::
   :maxdepth: 1
   :caption: Example categories

   Exterior
   Gameplay
   Handles
   Input
   Interior
   Lifecycle
   Modules
   Powertrain
   Presentation
   Telemetry
