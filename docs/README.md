Browse the [Markdown manual](../manual/README.md) directly on GitHub.

# Build the documentation

The manual is written in reStructuredText under `source/`. Its entry point is `source/index.rst`.

From the repository root, install the documentation dependencies and build HTML:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r docs/requirements.txt
python -m sphinx -W --keep-going -b html docs/source docs/build/html
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

Open `docs/build/html/index.html` to read the local build. The repository's `.readthedocs.yaml` uses the same Sphinx configuration to build the hosted manual.
