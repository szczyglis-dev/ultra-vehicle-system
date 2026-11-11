# Lighting state and timing

Vehicle lighting separates requested state from actual channel output. A driver requests low beams, high beams or indicators; the lighting component combines that request with channel availability and mechanical signals such as braking or reverse.

Use this state layer for gameplay and UI rather than manipulating individual Unity lights directly. A custom renderer or lamp model can then present the same vehicle lighting behavior without becoming a second owner of the beam or indicator state.

## Configure in the Inspector first

Use [Add one headlight pair](../Lights.md#inspector-quick-start-add-one-headlight-pair) to add Lights, create Unity Light objects and assign channel Lights/Lenses. Apply/save and test the Live lighting actions before using the API below. Custom application policies build on that working output setup.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `IndicatorAudio` | Observes the indicator phase and presents clicks. |
| `LightChannel` | Describes the physical light/emission output for a channel. |
| `Lights` | Owns beam/indicator requests, automatic outputs and timing. |

## Requested versus output state

An unavailable channel can suppress an otherwise valid request. That distinction supports vehicles with different lamp configurations and application damage rules. A dashboard may show the requested beam mode while another display reports whether a particular channel actually produces output.

Nullable overrides make ownership explicit. A brake-light override of `true` forces a request on; `false` forces it off; `null` returns control to the normal mechanic. Restore `null` when the cutscene or override ends instead of guessing the current brake state and writing it once.

`Lights` owns independent channel availability, beam request, overrides and the indicator clock. Tail normally follows beam mode. Brake/reverse output can follow mechanics or a nullable override; a `false` availability gate can suppress any channel.

`SetBeamMode` selects Off/Low/High. `SetHighBeams`(`false`) returns toward low-beam policy. Tail/brake/reverse overrides accept `null` to resume automatic following. Lens emission uses property blocks; materials must support emission and independently controlled renderers must not overwrite each other's channel output.

## Changing lamp appearance

Beam requests, brake/reverse following, availability and blink timing remain immediate through the existing public actions. Lamp appearance and assigned outputs are configuration: changing `color`, `intensity`, `emission`, `lights`, `lenses`, `glows` or glow radius/brightness requires one refresh. The same applies after Play Mode Inspector edits. A standalone `LightChannel` has `RefreshConfiguration()`; a vehicle `Lights` component has `RefreshLightingConfiguration()`. Refresh preserves requests and blink timing and does not invent `LitChanged` events when illumination is unchanged.

**Example: `LampAppearanceControl.cs`**

<!-- example: LampAppearanceControl.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public sealed class LampAppearanceControl : MonoBehaviour
    {
        public Lights lights;
        public void ChangeHeadlightColor(Color color)
        {
            if (!lights) return;
            lights.headlights.color = color;
            lights.RefreshLightingConfiguration();
        }
    }
}
```

Avoid writing the same native Light or lens emission from another controller every frame. Make a configuration edit and refresh, or use a custom LightChannel implementation. Shared outputs within one Lights core retain their authored channel order; use independent outputs for independently visible channels.

## Indicator events

Indicators have a requested direction and a flashing output clock. `SetIndicators` changes direction; the clock turns output on/off while that request remains active. A stalk animation needs direction, while a click and lamp emission need output phase.

`IndicatorsChanged` reports a changed direction request. `IndicatorPhaseChanged(bool)` reports the clock's lit/unlit phase. Use one phase listener for a shared hazard click, since left and right are synchronized. Beam state has its own `BeamModeChanged` notification and does not share the indicator timer.

When replacing lamp rendering, retain the state machine and supply output through the configured channels or a deliberate derived implementation. When replacing only click audio, subscribe to phase and leave lamp rendering alone. This keeps two independent extensions from each restarting their own flashing clock.

Subscribe to output phase when synchronizing a click or another phase-sensitive effect. Subscribe/read requested direction when showing the selected stalk state. Restarting the phase on every repeated input would keep a held indicator from following a stable clock, so unchanged requests deliberately preserve timing.

Emission requires compatible material properties as well as channel state. If several systems write a renderer's property block, coordinate their ownership; correct indicator logic cannot prevent a later writer from replacing the rendered output.

A newly selected direction starts a lit phase; repeating that state does not restart its clock. Hazards share one phase. `IndicatorPhaseChanged` reports actual output phase transitions. `IndicatorAudio` follows that phase, so hazards do not create one click per side.

Optional `tickOn`/`tickOff` replace generated defaults independently. Disabling the channel/core suspends playback and removes its active subscription. The channel owns generated clips/sources, not assigned assets.

## Bind a day/night action

The sample sends one state request when the application changes night mode. It leaves lamp intensity, emission and output availability under the lighting component's configuration. This is also a useful boundary for replacing the visual implementation: the game can keep the same night action while the lamps change.

Attach this beside game lighting controls and assign vehicle `Lights`. It uses one public action per change rather than writing Unity Light intensities directly.

**Example: `VehicleNightLights.cs`**

<!-- example: VehicleNightLights.cs -->
```csharp
using UnityEngine;
using UltraVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class VehicleNightLights : MonoBehaviour
    {
        public Lights lights;
        public void SetNight(bool night)
        {
            if (lights) lights.SetBeamMode(night ? BeamMode.Low : BeamMode.Off);
        }
    }
}
```

Read `BeamMode` and actual channel output properties for UI. For Inspector setup see [Lights](../Lights.md).

## Custom lighting groups

`customLights` contains `CustomLightGroup` entries with the same light/emission parameters as `LightChannel`, plus an ID, independent on request and optional blink clock. IDs are nonblank and ordinal case-sensitive; ambiguous authored duplicates cannot be addressed. One entry can drive one source or an entire group.

Use `RegisterCustomLight`, `UnregisterCustomLight`, `GetCustomLight`, `SetCustomLight`, `ToggleCustomLight`, `SetCustomLightEnabled`, `SetAllCustomLights` and `RefreshCustomLights`. Registration rejects duplicate IDs. Removal extinguishes the group. Disabled modules/groups remain dark while retaining their on requests. Custom groups do not follow the built-in beam, brake or indicator requests. They advance from `Lights.Step`; do not run a second custom blink loop.

Inherited `LitChanged` reports actual illumination, including blinking and availability. An on request differs from `IsLit` while a blink phase or gate is off. `RefreshCustomLights` reapplies custom configuration without advancing time. The regular step follows live on/blink requests and cleans removed list entries; appearance or output-assignment edits require refresh. Use separate physical Light components/renderers for independently controlled channels so they do not overwrite one another's output.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed vehicle lighting API](../API/Lights.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### CustomLightGroup

[CustomLightGroup](../API/Lights.md#customlightgroup) gives the full declared contract.

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### LightChannel

[LightChannel](../API/Lights.md#lightchannel) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void Apply(bool requested)` | Applies requested lit state/intensity to configured native lights and emission outputs, publishing `LitChanged` on output changes. |
| `public virtual void RefreshConfiguration()` | Reapplies this channel's configured appearance and outputs while retaining its last request. |

| Event / callback | Role |
| --- | --- |
| `public event Action<bool> LitChanged` | When a `LightChannel`'s actual lit output changes. Payload: bool. |

### Lights

[Lights](../API/Lights.md#lights) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public override void Configure(VehicleController vehicle)` | Resolves missing Engine/Events references without replacing explicit assignments. |
| `public override void Step(VehicleController vehicle, Command command, float dt)` | Consumes light/indicator commands, advances the shared blink clock and applies resolved lamp/emission output. |
| `public virtual LightChannel GetChannel(VehicleLightType type)` | Returns the configured lighting channel for the selected light role. |
| `public virtual void RestoreAutomaticLights()` | Clears forced lighting overrides so automatic mechanic-following resumes. |
| `public virtual void SetBeamMode(BeamMode mode)` | Requests Off, Low or High beam policy through the lighting state machine. |
| `public virtual void SetLowBeams(bool on)` | Requests low-beam availability/state through normal beam policy. |
| `public virtual void SetTailLights(bool on)` | Changes the tail-light request/availability policy. |
| `public virtual void SetTailOverride(bool? on)` | Forces tail output on/off; `null` resumes normal beam-following. |
| `public virtual void SetHazards(bool on)` | Requests synchronized left/right hazard indicators. |
| `public virtual void SetLeftIndicator(bool on)` | Requests or clears the left turn-indicator state. |
| `public virtual void SetRightIndicator(bool on)` | Requests or clears the right turn-indicator state. |
| `public virtual void SetHeadlights(bool on)` | Requests the headlight on/off policy through the lighting state machine. |
| `public virtual void SetHighBeams(bool on)` | Requests or releases high beams using the component's low-beam return policy. |
| `public virtual void SetIndicators(IndicatorState value)` | Requests the selected direction/hazard indicator state. |
| `public virtual void SetBrakeOverride(bool? on)` | Forces brake output on/off; `null` restores mechanic-following. |
| `public virtual void SetReverseOverride(bool? on)` | Forces reverse lamp output on/off; `null` resumes mechanic-following. |
| `public virtual void SetChannelEnabled(VehicleLightType type, bool available)` | Changes availability of a selected lighting channel independently of its requested state. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> IndicatorPhaseChanged` | When the shared flashing output phase changes. Payload: lit bool; hazards share one phase. |
| `public event System.Action<BeamMode> BeamModeChanged` | When requested beam mode changes. Payload: `BeamMode`. |
| `public event System.Action<IndicatorState> IndicatorsChanged` | When requested direction/hazard state changes. Payload: `IndicatorState`, not blink phase. |

| Declaration | Behavior |
| --- | --- |
| `public virtual CustomLightGroup GetCustomLight(string id)` | Finds a custom group by its exact ID. Returns null for blank, missing or ambiguous duplicate IDs. |
| `public virtual bool RegisterCustomLight(CustomLightGroup group)` | Adds a nonnull group with a unique, nonblank ID, then applies its current request. Returns false for invalid or duplicate registrations. |
| `public virtual bool UnregisterCustomLight(string id)` | Turns the identified group off and removes it. Returns false for an unresolved ID. |
| `public virtual bool SetCustomLight(string id, bool on)` | Sets the identified group's on request and refreshes outputs. Returns false for an unresolved ID. A disabled module or group remains dark. |
| `public virtual bool ToggleCustomLight(string id)` | Toggles the identified group's requested on state; returns false for an unresolved ID. |
| `public virtual bool SetCustomLightEnabled(string id, bool available)` | Changes group availability while retaining its on request. Returns false for an unresolved ID. |
| `public virtual void SetAllCustomLights(bool on)` | Sets the requested on state of every custom group without changing built-in lighting channels. |
| `public virtual void RefreshCustomLights()` | Applies custom requests and changed configuration immediately without advancing blink clocks. Removed list entries are extinguished. |
| `public virtual void RefreshLightingConfiguration()` | Reapplies standard/custom lamp appearance and bindings while preserving requested states and blink clocks. |

### VehicleModule

[VehicleModule](../API/Modules.md#vehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void Configure(VehicleController vehicle)` | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
| `public virtual void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it. |
| `public virtual void SetEnabled(bool value)` | Changes module enabled state and publishes an actual requested-flag change. |
| `public virtual bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> EnabledChanged` | After `SetEnabled` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
| `public event System.Action<VehicleController> Configured` | After controller-driven module configuration. Payload: the owning `VehicleController`. |
| `public event System.Action<VehicleController, Command, float> Stepped` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds. |

### VehicleLampGlow

| Signature | Role |
| --- | --- |
| `public void Apply(bool lit, Color color)` | Set a lens halo directly when implementing a custom lighting backend; LightChannel normally calls it. |
