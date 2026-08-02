from typing import Any, Dict

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ..engines.matchup_engine import build_matchup
from ..engines.monte_carlo import run_monte_carlo
from ..database.db import get_fighter_by_name

router = APIRouter()


class SimulationRequest(BaseModel):
    fighterA: str
    fighterB: str
    simulations: int = 5000


@router.post("/run_simulation", response_model=Dict[str, Any])
async def run_simulation(req: SimulationRequest):
    # Load fighters (these helper functions are assumed synchronous)
    f1 = get_fighter_by_name(req.fighterA)
    f2 = get_fighter_by_name(req.fighterB)

    if not f1 or not f2:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="One or both fighters not found",
        )

    matchup = build_matchup(f1, f2)
    results = run_monte_carlo(matchup, req.simulations)

    return {
        "fighterA": req.fighterA,
        "fighterB": req.fighterB,
        "results": results,
    }
