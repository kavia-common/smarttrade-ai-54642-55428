from fastapi import APIRouter
from src.schemas.trade import TradeRequest, TradeResponse

router = APIRouter(
    prefix="/api/trades",
    tags=["Trade Execution"]
)

# PUBLIC_INTERFACE
@router.post("/execute", response_model=TradeResponse, summary="Execute trade", description="Place a new trade (buy/sell asset).")
async def execute_trade(payload: TradeRequest):
    return TradeResponse(status="accepted", trade_id="sample-trade-1", detail="Order placed.")
