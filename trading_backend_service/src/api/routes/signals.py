from fastapi import APIRouter
from src.schemas.signals import SignalExplorerQuery, SignalExplorerResponse

router = APIRouter(
    prefix="/api/signals",
    tags=["Signals & Sentiment"]
)

# PUBLIC_INTERFACE
@router.post("/explore", response_model=SignalExplorerResponse, summary="Explore signals", description="Query algorithmic signals and market sentiment.")
async def explore_signals(payload: SignalExplorerQuery):
    return SignalExplorerResponse(signals=[{"name": "rsi", "signal": "buy"}], sentiment=0.3)
