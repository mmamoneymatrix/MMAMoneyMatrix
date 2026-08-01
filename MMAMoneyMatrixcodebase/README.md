# MMAMoneyMatrix Codebase

This is the complete codebase for the MMAMoneyMatrix fight simulator, built according to the provided architecture specification.

## Project Structure

### Backend (Flask)
- `backend/app.py`: Main entry point and API route registration.
- `backend/engines/`: Core logic engines.
  - `matchup_engine.py`: Generates the "Fight Geometry Object".
  - `monte_carlo.py`: Runs thousands of fight simulations.
  - `scoring.py`: Implements round-by-round scoring and judge bias.
  - `bonuses.py`: Handles gym tier and underdog realism modifiers.
- `backend/models/`: Data structures for Fighters and Fights.
- `backend/routes/`: API endpoints for simulation and data management.

### Frontend (Next.js)
- `frontend/pages/`: Next.js page structure (Home, Import, Matchup).
- `frontend/components/`: Reusable UI components (MatchupRunner, FighterCard).
- `frontend/package.json`: Frontend dependencies and scripts.

### Database (Postgres)
- `database/schema.sql`: SQL definitions for fighters, fights, and styles tables.

## Setup Instructions

### Backend
1. Navigate to `backend/`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python app.py`

### Frontend
1. Navigate to `frontend/`
2. Install dependencies: `npm install`
3. Run development server: `npm run dev`

### Database
1. Execute `database/schema.sql` in your Postgres or Supabase instance.
2. Configure `.env` with your database credentials.
