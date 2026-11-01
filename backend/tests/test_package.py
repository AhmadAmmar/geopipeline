"""
Purpose:
This file contains a minimal smoke test for the Phase 1 scaffold.

What it verifies:
- the backend package can be imported
- the package exposes the expected version string

What it does not verify yet:
- no FastAPI routes
- no geospatial logic
- no CLI behavior
"""

# Purpose:
# Import the package version from the installable backend package.
from geopipeline import __version__


# Purpose:
# Smoke-test the package import and version constant.
def test_package_version() -> None:
    assert __version__ == "0.1.0"