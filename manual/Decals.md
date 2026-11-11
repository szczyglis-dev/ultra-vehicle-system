# Tire marks

`Skidmarks` draws bounded world-space tire ribbons from TireFeedback. It is a trail renderer with a managed segment pool, not a general-purpose projected decal system. Physical friction, tire particles and mesh damage are independent.

## Inspector quick start

1. Select the root and open **Effects**. Add **Tire Feedback** and **Skidmarks** through **Modules > Add module...** if absent, then assign Skidmarks' **Tire Feedback** reference.
2. Assign the bundled Tire Skid material or a compatible project material. Set Width to fit the tires, then choose an intensity gate and bounded segment pool below.
3. Apply/save and perform a supported braking/steering skid. Inspect the road's TireSurface profile if it suppresses marks; ordinary rolling need not leave a black ribbon.
4. Check the result from an external camera before raising density. The module generates world-space ribbons; no separate decal projector is required on each tire.

## Configure

1. Add/register `TireFeedback` and `Skidmarks` and assign **TireFeedback**.
2. Assign the bundled **Tire Skid** material from `Resources/Effects` or a compatible transparent vertex-color material. Vehicle creation normally fills the bundled default.
3. Set **Width**, **Minimum Intensity**, **Minimum Distance** and **Ground Offset**.
4. Set **Max Segments** and **Lifetime** for the visible history budget.
5. Add ground effect profiles through [Surfaces](Surfaces.md) when colors, loose-soil appearance or mark activity differ.
6. Test a skid, ordinary rolling, wheel lift, teleport and crossing between ground surfaces.

Use the package skidmark shader or implement its supported vertex/color/fade contract in your material. Assigning an arbitrary opaque material can hide intensity/fade or show a solid strip even when the underlying trail data is valid.

## Tune geometry and continuity

| Setting | Meaning |
| --- | --- |
| Width | Base trail width in metres |
| Minimum Intensity | Activity required before emitting a segment |
| Minimum Distance | Minimum wheel travel between useful trail points |
| Maximum Gap | Largest spacing that can be joined into one continuous trail |
| Ground Offset | Small offset above the supporting surface to reduce depth fighting |
| Max Segments | Bounded history capacity |
| Lifetime | Base fading time |

Smaller point spacing gives smoother curves but consumes the pool sooner. Large spacing can make tight turns angular. A large Maximum Gap can stretch a strip across discontinuous motion; it is not a substitute for enough sampling at the intended speed.

Ground Offset should be only enough to avoid z-fighting. Too large an offset makes the trail hover, especially on slopes. Test from a low camera angle as well as from above.

## Surface profiles and activity

Surface profiles select their mark style/color/activity where supported. **Rolling Marks** can produce a trail on loose ground without a strong skid; ordinary rubber-road marks generally keep that contribution low/zero. **Marks Enabled** can suppress a profile's output.

Classify the ground in [Surfaces](Surfaces.md) and configure particles/audio in their own guides. A dark tire mark does not itself lower grip, create a physical rut or apply damage. Several presentation consumers can read the same contact without each providing its own unrelated surface lookup.

## Pool size and lifetime

`SegmentCount` reports the buffer's segment use. Capacity bounds history even if the requested lifetime is long. Increasing lifetime does not guarantee every old segment survives when new marks reuse a finite pool.

Choose the budget for the number of emitting wheels and vehicles. Halving spacing can roughly double segment demand for the same driving distance. Test repeated tight skids and normal driving, not only one short straight trail.

`ClearMarks()` clears trail history and raises Cleared. Use it deliberately for a fresh race/session or pooling policy; a vehicle teleport does not necessarily mean every old world-space mark should be erased. For a complete clearing example, see [Presentation scripting](Scripting/Presentation.md#clear-a-vehicles-trail-history).

## World-space ownership

Trails break when contact/surface continuity is lost or spacing exceeds the gap policy. This avoids connecting an airborne wheel to its later landing with one long strip. A surface/profile change can begin another trail segment rather than blending unrelated output indefinitely.

Existing marks remain in world space. They do not follow a moving platform after emission, so use static ground for stable marks or implement a platform-relative alternative. Moving the vehicle does not drag all its previous marks behind it.

Disabling the module stops new sampling and clears retained continuity state; it is not the same as destroying every old mark immediately. The module owns its generated mesh/host and releases those resources on destruction. Do not save or attach the runtime host as a new independent trail system.

## Troubleshoot

| Symptom | Inspect |
| --- | --- |
| No marks but tire smoke works | Material, minimum intensity and profile Marks Enabled |
| Black/opaque rectangular ribbon | Material's transparency, vertex color and fade support |
| Trail flickers into the road | Ground Offset and supporting geometry |
| Long line after discontinuous motion | Continuity/gap policy and application teleport handling |
| Marks disappear early | Finite segment capacity, spacing and total emitting wheels |
| Marks float after a platform moves | World-space output is not attached to the platform |
| Loose dirt has no rolling tracks | Surface Rolling Marks and speed thresholds |

For buffer uploads, fading/ownership and exact methods, see [Presentation reference](Scripting/Presentation.md) and [API](API/Presentation.md).
