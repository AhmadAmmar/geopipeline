# GeoPipeline

GeoPipeline is an open-source full-stack geospatial processing platform.

Planned capabilities include:

- vector upload and validation
- raster upload and validation
- CRS inspection
- reprojection
- buffering
- AOI intersection
- raster clipping
- summary metrics and statistics
- output downloads through an API, web UI, and CLI

## Current status

This repository is in the early bootstrap stage.

Completed so far:

- repository initialization
- Python package scaffold
- frontend scaffold
- code quality tooling
- editor settings
- pre-commit hooks

## Repository layout

- `src/geopipeline/` — Python package for backend and shared domain logic
- `frontend/` — React + TypeScript + Vite frontend
- `tests/` — Python tests
- `.vscode/` — recommended editor settings
- `pyproject.toml` — Python packaging and tool configuration

## Quick start

### Backend / Python toolchain

```bash
python -m pip install -e ".[dev]"
pre-commit install