## UV Installation

Install uv with our standalone installers:

### On macOS and Linux.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### On Windows.
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, from PyPI:

#### With pip.
```bash
pip install uv
```

If installed via the standalone installer, uv can update itself to the latest version:
```bash
uv self update
```

See the [installation documentation](https://docs.astral.sh/uv/getting-started/installation/) for details and alternative installation methods.

---

## Installing Python

If Python is already installed on your system, uv will detect and use it without configuration. However, uv can also install and manage Python versions. uv automatically installs missing Python versions as needed — you don't need to install Python to get started.

### Getting started

To install the latest Python version:
```bash
uv python install
```

**Note**

Python does not publish official distributable binaries. As such, uv uses distributions from the Astral python-build-standalone project. See the Python distributions documentation for more details.

Once Python is installed, it will be used by uv commands automatically.

**Important**

When Python is installed by uv, it will not be available globally (i.e. via the python command). Support for this feature is in preview. See Installing Python executables for details.

You can still use `uv run` or create and activate a virtual environment to use Python directly.

### Installing a specific version

To install a specific Python version:
```bash
uv python install 3.12
```