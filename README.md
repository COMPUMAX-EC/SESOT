# SESOT: Technical Support Expert System

> Rule-based Expert System for automated hardware diagnosis (CPUs and Printers), optimized for Edge environments (Raspberry Pi).

## Description

SESOT implements an inference engine (based on the Rete algorithm via `experta`) to guide users through a dynamic decision tree. The goal is to standardize first-level technical support, enabling fast and accurate diagnoses without the need for an internet connection.

## Installation and Setup

This project uses a modern structure managed by `uv`. Manual virtual environment creation is not required.

1. **Clone the repository:**

```bash
git clone https://github.com/COMPUMAX-EC/SESOT.git
cd SESOT
```

### Prerequisites

* **Python 3.10+**
* **[uv](https://github.com/astral-sh/uv):** High-performance package and project manager.

#### Installing `uv` (if not installed)
1. **Installing `uv` (if not installed)**

From PyPI:

```bash
pip install uv
```

2. **Sync the environment:**
This command reads `uv.lock`, creates the virtual environment (`.venv`), and automatically installs exact dependencies (`experta`, etc.).

```bash
uv sync
```

## Usage

To start the inference engine in the terminal:

```bash
uv run src/expert_system/main.py
```

The system will guide you by asking for the device type (cpu or printer) and observed symptoms.

## Development

To contribute or run tests:

```bash
# Run tests (requires pytest installed as a dev dependency)
uv run pytest
```

## Project Structure

We use `src` layout for robustness:

*   `src/expert_system/`: Package source code.
    *   `engine.py`: Inference engine logic (Rules and Facts).
    *   `main.py`: Entrypoint.
*   `pyproject.toml`: Project definition and dependencies.
*   `uv.lock`: Lock file for deterministic reproducibility.


## License

Distributed under the MIT License. See `LICENSE` for more information.
