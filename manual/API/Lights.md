# Vehicle lighting API

Read [the system explanation](../Scripting/Lights.md) for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from `MonoBehaviour`, `Object` or `ScriptableObject` are documented by Unity.

## Types

- [BeamMode](Lights.md#beammode)
- [CustomLightGroup](Lights.md#customlightgroup)
- [IndicatorState](Lights.md#indicatorstate)
- [LightChannel](Lights.md#lightchannel)
- [Lights](Lights.md#lights)
- [VehicleLampGlow](Lights.md#vehiclelampglow)
- [VehicleLightType](Lights.md#vehiclelighttype)

## BeamMode

**Runtime/Exterior/Lights/Lights.cs**

Defines the allowed beam mode choices used by this topic.

### Values

- `Off`
- `Low`
- `High`

## CustomLightGroup

**Runtime/Exterior/Lights/CustomLightGroup.cs**

An independently requested/blinking custom lighting group. Inherits all physical light and emission parameters and `LitChanged` from [LightChannel](Lights.md#lightchannel).

**Inherits / implements:** [LightChannel](Lights.md#lightchannel).

### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool blinking` | Enables the group's independent blink clock; a newly enabled request begins in the lit phase. |
| `public float blinkInterval` | Duration of each on/off phase in seconds, clamped to at least 0.05. |
| `public string id` | Unique, nonblank, case-sensitive ID within the owning list. Duplicate authored IDs cannot be addressed individually. |
| `public bool on` | Requested custom light state, independent of availability and the current blink phase. |

## IndicatorState

**Runtime/Exterior/Lights/Lights.cs**

Defines the allowed indicator state choices used by this topic.

### Values

- `Off`
- `Left`
- `Right`
- `Hazard`

## LightChannel

**Runtime/Exterior/Lights/LightChannel.cs**

One lamp/emission output channel, including lit output state and its output notification.

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event Action<bool> LitChanged` | When a `LightChannel`'s actual lit output changes. Payload: bool. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public Color color` | Color and alpha used to render color. Initial value: `Color.white`. |
| `public float emission` | Emission multiplier applied to the channel lens materials when active. Initial value: `2`. |
| `public bool enabled` | Includes this entry in its owning system's configured behavior. Initial value: `true`. |
| `public float intensity` | Light intensity applied to the channel light sources when active. Initial value: `4`. |
| `public virtual bool IsLit { get; protected set; }` | Current is lit predicate; read it instead of maintaining a second application flag. |
| `public Renderer[] lenses` | Assign the lenses references used by LightChannel. Entries are processed in list order. Initial value: `Array.Empty<Renderer>()`. |
| `public VehicleLampGlow[] glows` | Saved lens halos following this channel, independently of illumination intensity. Initial value: `Array.Empty<VehicleLampGlow>()`. |
| `public Light[] lights` | Assign the lights references used by LightChannel. Entries are processed in list order. Initial value: `Array.Empty<Light>()`. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void RefreshConfiguration()` | Reapplies appearance/output references with the last requested lit state. No blink reset or unchanged-state event. | — |
| `public virtual void Apply(bool requested)` | Applies requested lit state/intensity to configured native lights and emission outputs, publishing `LitChanged` on output changes. | `requested` — Requested, interpreted by this operation in the declared type. |

## Lights

**Runtime/Exterior/Lights/Lights.cs**

Owns beam/indicator requests, automatic outputs and timing.

**Inherits / implements:** [ExteriorModule](Modules.md#exteriormodule).

### Events and Inspector callbacks

| Member | Meaning |
| --- | --- |
| `public event System.Action<BeamMode> BeamModeChanged` | When requested beam mode changes. Payload: `BeamMode`. |
| `public event System.Action<bool> IndicatorPhaseChanged` | When the shared flashing output phase changes. Payload: lit bool; hazards share one phase. |
| `public event System.Action<IndicatorState> IndicatorsChanged` | When requested direction/hazard state changes. Payload: `IndicatorState`, not blink phase. |


### State and configuration

| Member | Meaning |
| --- | --- |
| `public bool automaticBrakeLights` | Derives brake-light activation from the vehicle brake request unless overridden through the light API. Initial value: `true`. |
| `public bool automaticReverseLights` | Derives reverse-light activation from the vehicle drivetrain direction unless overridden through the light API. Initial value: `true`. |
| `public virtual BeamMode BeamMode { get; }` | Read-only/resolved beam mode for Lights. |
| `public float blinkInterval` | Time in seconds used for blink interval. Larger values make this phase/wait last longer. Initial value: `.45f`. |
| `public LightChannel brakeLights` | Optional Light sources and emissive renderers for the service brake. |
| `public virtual bool BrakeLightsOn { get; }` | Read-only/resolved brake lights on for Lights. |
| `public float brakeLightThreshold` | Minimum applied service brake that turns on stop lamps. Includes progressive and analog braking. |
| `public List<CustomLightGroup> customLights` | Optional custom light groups. Each group has the same Light sources, emissive lenses, color, intensity, emission and availability controls as a built-in channel. |
| `public Engine engine` | Assign the engine Engine component/asset used by Lights. |
| `public override int ExecutionOrder { get; }` | Default local priority within phase/category. |
| `public bool handbrakeActivatesBrakeLights` | Includes an applied handbrake in the automatic brake-light request. Initial value: `false`. |
| `public LightChannel headlights` | Configuration for headlights. Expand this field; its settings are described under LightChannel. Initial value: `new LightChannel()`. |
| `public virtual bool HeadlightsOn { get; }` | Read-only/resolved headlights on for Lights. |
| `public LightChannel highBeams` | Configuration for high beams. Expand this field; its settings are described under LightChannel. Initial value: `new LightChannel()`. |
| `public virtual bool HighBeamsOn { get; }` | Read-only/resolved high beams on for Lights. |
| `public virtual bool IndicatorFlashOn { get; }` | Read-only/resolved indicator flash on for Lights. |
| `public virtual IndicatorState Indicators { get; }` | Read-only/resolved indicators for Lights. |
| `public LightChannel leftIndicators` | Configuration for left indicators. Expand this field; its settings are described under LightChannel. Initial value: `new LightChannel { color = new Color(1, .4f, 0), intensity = .1f }`. |
| `public virtual bool LeftIndicatorsOn { get; }` | Read-only/resolved left indicators on for Lights. |
| `public override ExecutionPhase Phase { get; }` | Cross-category execution barrier used by the module pipeline. |
| `public LightChannel reverseLights` | Optional Light sources and emissive renderers for selected reverse gear / direct reverse drive. |
| `public virtual bool ReverseLightsOn { get; }` | Read-only/resolved reverse lights on for Lights. |
| `public LightChannel rightIndicators` | Configuration for right indicators. Expand this field; its settings are described under LightChannel. Initial value: `new LightChannel { color = new Color(1, .4f, 0), intensity = .1f }`. |
| `public virtual bool RightIndicatorsOn { get; }` | Read-only/resolved right indicators on for Lights. |
| `public LightChannel tailLights` | Rear position-lamp channel following headlights unless overridden. |
| `public virtual bool TailLightsOn { get; }` | Read-only/resolved tail lights on for Lights. |


### Methods

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public virtual void RefreshLightingConfiguration()` | Reapplies standard/custom lamp appearance and bindings, preserving requested states and blink timing. | — |
| `public override void Configure(VehicleController vehicle)` | Resolves missing Engine/Events references without replacing explicit assignments. | `vehicle` — Vehicle context/owner receiving the operation. |
| `public virtual LightChannel GetChannel(VehicleLightType type)` | Returns the configured lighting channel for the selected light role. | `type` — Type, interpreted by this operation in the declared type. **Returns:** Returned `LightChannel`; ownership remains as specified by the creating/lookup operation. |
| `public virtual CustomLightGroup GetCustomLight(string id)` | Finds a custom group by its exact ID. Returns null for blank, missing or ambiguous duplicate IDs. | — |
| `public virtual void RefreshCustomLights()` | Applies custom requests and changed configuration immediately without advancing blink clocks. Removed list entries are extinguished. | — |
| `public virtual bool RegisterCustomLight(CustomLightGroup group)` | Adds a nonnull group with a unique, nonblank ID, then applies its current request. Returns false for invalid or duplicate registrations. | — |
| `public virtual void RestoreAutomaticLights()` | Clears forced lighting overrides so automatic mechanic-following resumes. | No arguments; no returned value. |
| `public virtual void SetAllCustomLights(bool on)` | Sets the requested on state of every custom group without changing built-in lighting channels. | — |
| `public virtual void SetBeamMode(BeamMode mode)` | Requests Off, Low or High beam policy through the lighting state machine. | `mode` — Mode, interpreted by this operation in the declared type. |
| `public virtual void SetBrakeOverride(bool? on)` | Forces brake output on/off; `null` restores mechanic-following. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetChannelEnabled(VehicleLightType type, bool available)` | Changes availability of a selected lighting channel independently of its requested state. | `type` — Type, interpreted by this operation in the declared type. `available` — Requested availability, distinct from mesh detachment. |
| `public virtual bool SetCustomLight(string id, bool on)` | Sets the identified group's on request and refreshes outputs. Returns false for an unresolved ID. A disabled module or group remains dark. | — |
| `public virtual bool SetCustomLightEnabled(string id, bool available)` | Changes group availability while retaining its on request. Returns false for an unresolved ID. | — |
| `public virtual void SetHazards(bool on)` | Requests synchronized left/right hazard indicators. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetHeadlights(bool on)` | Requests the headlight on/off policy through the lighting state machine. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetHighBeams(bool on)` | Requests or releases high beams using the component's low-beam return policy. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetIndicators(IndicatorState value)` | Requests the selected direction/hazard indicator state. | `value` — Requested state/value in this operation's domain; use its configured range/unit. |
| `public virtual void SetLeftIndicator(bool on)` | Requests or clears the left turn-indicator state. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetLowBeams(bool on)` | Requests low-beam availability/state through normal beam policy. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetReverseOverride(bool? on)` | Forces reverse lamp output on/off; `null` resumes mechanic-following. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetRightIndicator(bool on)` | Requests or clears the right turn-indicator state. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetTailLights(bool on)` | Changes the tail-light request/availability policy. | `on` — On, interpreted by this operation in the declared type. |
| `public virtual void SetTailOverride(bool? on)` | Forces tail output on/off; `null` resumes normal beam-following. | `on` — On, interpreted by this operation in the declared type. |
| `public override void Step(VehicleController vehicle, Command command, float dt)` | Consumes light/indicator commands, advances the shared blink clock and applies resolved lamp/emission output. | `vehicle` — Vehicle context/owner receiving the operation. `command` — Command sampled for this tick; use its channel metadata as well as axes. `dt` — Elapsed time in seconds. |
| `public virtual bool ToggleCustomLight(string id)` | Toggles the identified group's requested on state; returns false for an unresolved ID. | — |
| `public virtual bool UnregisterCustomLight(string id)` | Turns the identified group off and removes it. Returns false for an unresolved ID. | — |

## VehicleLampGlow

**Runtime/Exterior/Lights/VehicleLampGlow.cs**

**Inherits / implements:** `MonoBehaviour`.

A depth-tested lens halo, controlled by a LightChannel and rendered with the bundled Lamp Glow material. Use the Lights component menu's **Add lamp glows** command to create saved sources at assigned lamps.

| Member | Meaning |
| --- | --- |
| `public Renderer glowRenderer` | Renderer using the Lamp Glow material, oriented outward along local Z. |
| `public float radius` | Halo radius in metres; default 0.12, range 0.005–0.5. |
| `public float brightness` | Lens brightness independent of road illumination; default 2. |
| `public bool directional` | Fade behind the lens; default true. |

| Signature | Role and behavior | Arguments and result |
| --- | --- | --- |
| `public void Apply(bool lit, Color color)` | Set halo visibility and color; the owning channel normally calls this automatically. | `lit` — Requested light state. `color` — Lens color. |

## VehicleLightType

**Runtime/Exterior/Lights/Lights.cs**

Defines the allowed light type choices used by this topic.

### Values

- `Headlights`
- `HighBeams`
- `Tail`
- `Brake`
- `Reverse`
- `LeftIndicator`
- `RightIndicator`
