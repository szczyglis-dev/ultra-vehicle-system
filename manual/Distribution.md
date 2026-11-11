# Installation and included content

## Install from the Asset Store

1. Open a Unity **6000.0.84f1** or newer project and sign in with the Unity account used to acquire Ultra Vehicle System from the Asset Store.
2. Open **Window → Package Management → Package Manager** and select **My Assets**.
3. Select **Ultra Vehicle System**, click **Download** if needed, then **Import**.
4. In the **Import Unity Package** window, keep the package files selected. Keep **Documentation** for the manual and **Demo** for the example scene and vehicles, then click **Import**.
5. Find the imported content under `Assets/Szczyglis/UltraVehicleSystem`. The manual is in `Documentation/Markdown`; the example scene is `Demo/Demo.unity`.

## Installed folders

The Asset Store release is a `.unitypackage`. All selected content is imported into the project's `Assets` folder:

```text
Assets/Szczyglis/UltraVehicleSystem/
├── Runtime/
├── Editor/
├── Resources/
├── Demo/
├── Documentation/
│   ├── Markdown/
│   ├── RTF/
│   └── UltraVehicleSystem.pdf
├── README.md
├── LICENSE.md
└── CHANGELOG.md
```

`Runtime`, `Editor` and `Resources` contain the vehicle system. `Demo` contains the optional example scene, vehicles and sample scripts; it can be deselected in the import window. `Documentation/Markdown` contains the editable manual. `Documentation/RTF` contains standard `.rtf` documents for Word, LibreOffice and other RTF readers. `Documentation/UltraVehicleSystem.pdf` contains the complete manual with a table of contents and bookmarks. The three root Markdown files come from the package source root. In the imported README, local documentation references are plain `Documentation/…` paths; the source README retains its package-relative links.

## Updates and custom vehicles

Install updates through Package Manager → My Assets by downloading and importing the new release. Keep your own vehicles, prefab variants and scripts outside `Assets/Szczyglis/UltraVehicleSystem` so package updates do not overwrite them. Prefer prefab variants and public APIs over editing the supplied files directly. Consult the changelog for removed or relocated files that need cleanup after an update.

## Requirements and rendering

Use Unity 6000.0.84f1 or newer with Input System 1.19.0 installed. The supplied demo uses URP materials and URP camera/light components; install Universal RP for the complete demo. For another render pipeline, provide suitable vehicle, water and effect materials; runtime mechanics do not depend on URP.

Installation does not replace your project's render pipeline or input settings. Configure input handling for the Input System and review your own project layers/collision matrix.

## License and credits

Read the package LICENSE and the supplied art/audio credits before redistribution. Original package code and third-party content have separate license terms. Third-party attribution and license files accompany the distributed assets; see [Third-party credits](ThirdParty.md).

## Release version

`UltraVehicleSystem.PackageVersion.Current` is the shared version label for runtime UI and the vehicle Inspector, including Asset Store imports and player builds. When releasing, update `Runtime/Core/PackageVersion.cs` and the development package’s `package.json` version together. `Tools/build_distribution.py` validates that these values match before writing distribution files. The demo footer uses the shared value rather than its own version string.

## Building the release

Run `python3 Tools/build_distribution.py` from the development repository. It writes `Releases/UltraVehicleSystem-<version>.unitypackage`, a SHA-256 checksum and a release manifest. Local development scripts under `Demo/Scripts/Dev` are excluded automatically; they are not required by the shipped scenes or prefabs. It preserves source asset GUIDs and does not copy runtime assemblies into the development project's Assets folder. It does not create a UPM archive or modify the source README, Demo or Samples snapshots.

Validate the archive with `python3 Tools/verify_distribution.py Releases/UltraVehicleSystem-<version>.unitypackage`. Before submission, import it into a separate Unity project and run the Asset Store Publishing Tools validator. Local archive generation does not upload or submit a release.
