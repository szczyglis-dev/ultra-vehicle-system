# Vehicle model hierarchy

Use a unit-scale vehicle root facing local +Z, with local +Y up. Put the chassis Rigidbody, VehicleController and vehicle modules on the root or explicitly registered child objects. Keep import scale and orientation corrections on mesh children.

A practical hierarchy is:

```text
Vehicle
  Body
    Exterior
    Interior
      Interior Camera
      Controls
      Passengers
  Wheels
    WheelFL
    WheelFR
    WheelRL
    WheelRR
```

This is an authoring convention, not a runtime name lookup contract. Assign the actual Body, wheels, controls, seats and camera references in their inspectors. Custom hierarchies are supported through those references.

Wheel pivots should sit at the tire centers. Keep imported mesh offsets beneath the pivots. Assign steering, drive, service-brake and handbrake roles per wheel instead of inferring them from names. A separate caliper pivot can follow suspension and steering without tire spin.

Place steering-wheel, yoke, stick, pedal and instrument pivots at their real axes. Parent hand/foot targets to the corresponding moving controls. A seat origin represents the seated pelvis; entry, exit and foot-rest anchors serve separate purposes. See [interior controls](InteriorControls.md), [passengers](Passengers.md) and [seat access](PassengerAccess.md).

Use a suitable chassis collision envelope. A convex MeshCollider on a dynamic Rigidbody provides an outer hull; it does not reproduce a walkable concave cabin. Keep the rendered water surface free of solid support colliders when buoyancy supplies support.

Example hierarchies are available in the [demo prefabs](Demo.md).
