# Pull request: reorganize repo structure, fix imports, wire API, and format code

This PR makes the backend a proper Python package, normalizes imports, wires the FastAPI router under /api, and updates the frontend to call the API via NEXT_PUBLIC_API_URL with a localhost fallback.

Changes:
- Added package markers: backend/__init__.py, backend/routes/__init__.py, backend/database/__init__.py, backend/engines/__init__.py
- Updated backend/app.py and backend/routes/run_simulation.py
- Updated frontend/pages/matchup.tsx
- Added README.md and pyproject.toml with Black config

Run & test instructions are included in the README.
