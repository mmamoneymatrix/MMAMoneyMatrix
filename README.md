# MMAMoneyMatrix

This commit reorganizes the repository to make the backend a proper Python package
and fixes imports and frontend wiring so the simulator works locally.

## What I changed

- Added package markers: `backend/__init__.py`, `backend/routes/__init__.py`, `backend/database/__init__.py`, `backend/engines/__init__.py`.
- Normalized backend imports to package-relative so `uvicorn backend.app:app` works.
- Exposed the simulation router under `/api/run_simulation` and added a health route `/`.
- Updated frontend `frontend/pages/matchup.tsx` to call the API at `/api/run_simulation` and use `NEXT_PUBLIC_API_URL` with a localhost fallback.
- Added `pyproject.toml` (Black config) and formatted updated files.

## How to run

Backend:

```bash
# From project root
pip install -r requirements.txt    # if you have a requirements file
uvicorn backend.app:app --reload --port 8000
```

If you prefer to run from the backend folder:

```bash
cd backend
uvicorn app:app --reload --port 8000
```

Frontend (Next.js):

```bash
cd frontend
npm install
NEXT_PUBLIC_API_URL=http://localhost:8000 npm run dev
```

## Test the API with curl

```bash
curl -X POST "http://localhost:8000/api/run_simulation" \
  -H "Content-Type: application/json" \
  -d '{"fighterA":"Fighter1","fighterB":"Fighter2","simulations":1000}'
```

## Notes / Follow-ups

- If you see `ModuleNotFoundError` for relative imports, ensure the `backend` folder is present in the repo root and has the `__init__.py` file (added here).
- If engine or database functions are `async`, update calls to `await` them and make sure the functions are async-compatible.
- Optional: add GitHub Actions for linting and testing.
