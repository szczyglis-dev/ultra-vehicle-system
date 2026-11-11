# Tire contact envelope

`ContactEnvelope` supplements Unity WheelCollider's centre-ray support by sampling the tire's rolling profile. It helps the lower tire surface negotiate small steps and edges while native suspension remains responsible for support forces. It is separate from the solid sidewall/obstacle volumes described in [Tire collision](TireCollision.md).

## Inspector quick start

1. Begin with a vehicle supported correctly on flat ground. Select its root and add/expand **Modules > Drive > Contact Envelope**.
2. Apply correct geometry from **Wheels > Wheel Setup** before tuning the envelope. Enable the module and review the sampling/correction limits below.
3. Apply/save, then compare the same low curb with the module on/off. Inspect chassis clearance too: an envelope cannot fix a bumper physically striking the ramp.
4. Use **Modules > Physics > Tire Collision** when solid sidewall/obstacle contacts are also needed; that helper has a separate purpose.

## Decide whether to use it

First establish a stable [native suspension](Suspension.md) on a smooth road. Add the envelope when the centre ray gives an abrupt result at curbs or narrow edges that a round tire should meet progressively. Compare identical runs with it enabled and disabled.

It is a finite sampling approximation, not tire deformation, a fully swept contact patch or a solver that can bridge an unsupported gap. Large obstacles still need suitable geometry, suspension clearance and solid collision handling.

## Configure

1. Add/register ContactEnvelope on the vehicle.
2. Set each wheel's physical radius and width in **Wheel Setup**, then apply configuration.
3. Set **Ground Layers** to eligible support geometry and **Minimum Ground Normal** for the permitted support slope.
4. Start with default longitudinal/width sampling and a moderate correction cap.
5. Test a low curb straight-on, an oblique curb, a ramp, a narrow edge, a gap and a landing.
6. Increase sampling/correction only when the test reveals a specific missed support case.

The layer mask should not include arbitrary helper geometry that must not support a tire. Support-normal filtering distinguishes a supporting face from a wall; it is not the same as allowing solid sidewall collision against that wall.

## Sampling and correction

| Setting | Meaning |
| --- | --- |
| Longitudinal Samples | Odd rolling-direction sample count, clamped to 3–15 |
| Width Samples | Across-tire sample count, 1–3 |
| Tire Half Width | Fallback when a wheel has no positive configured width; ordinary wheels use half their own width |
| Maximum Lift Radius | Maximum support correction as a fraction of physical tire radius |
| Ground Layers | Support-query layer mask |
| Minimum Ground Normal | Minimum upward component for eligible support |

More samples increase query cost per wheel. A long multi-axle vehicle multiplies that cost, so test representative vehicle counts rather than only one demonstration car. Width sampling can help at an oblique/narrow edge but does not make the tire infinitely wide.

**Maximum Correction** reports the largest current correction in metres. A cap of 0.5 on a 0.4 m radius permits at most 0.2 m of correction; it is not a 0.5 m world-space lift setting.

## What changes at runtime

The module adapts the native effective radius from its support estimate. The physical Wheel Setup radius remains the baseline; a live native radius can therefore differ from that baseline. Do not have another script repeatedly restore the native radius while the envelope is stepping.

It coordinates with suspension damping/force placement rather than adding an unrelated second spring. Disabling the module restores the configured wheel radii and clears its published correction. It does not undo the rest of the vehicle configuration.

The visual wheel pose and contact readings reflect the wheel/native/direct presentation contracts; a screenshot alone is insufficient to infer which face supported the tire. Check contact data and current correction when diagnosing an edge.

## Tune with a repeatable obstacle lane

Keep vehicle load, approach speed and throttle consistent. Establish the smallest obstacle that fails without correction, then inspect the wheel at low speed. If a wall face is treated as floor support, inspect normal/mask eligibility before increasing samples. If support rises more than intended, reduce the correction cap and inspect nearby overlapping geometry.

Use [solid tire contacts](TireCollision.md) for sidewall/unsupported obstacle interaction and [surfaces](Surfaces.md) for traction/effects. These modules complement one another but do not replace a suitable chassis collider.

## Troubleshoot

| Symptom | Check |
| --- | --- |
| No change at a curb | Registration, eligible layers/normals, wheel support and correction cap |
| Wheel radius keeps changing in Play | Expected envelope adaptation; inspect baseline versus effective radius |
| Contact looks too wide | Wheel Setup width and width-sample arrangement |
| Small gaps appear bridged | Sampling/correction limits and actual nearby support geometry |
| Excess query cost | Wheel count and longitudinal/width sample counts |
| Large obstacle still stops the vehicle | Tire/chassis collision and available suspension geometry |

For radius calculation, damping coordination and force placement, see [Wheel contact reference](Scripting/WheelContact.md) and [API](API/WheelContact.md).
