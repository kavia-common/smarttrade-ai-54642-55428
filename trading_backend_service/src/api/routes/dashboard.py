from fastapi import APIRouter
from src.schemas.dashboard import PortfolioSummary, PnLReport, PredictionsResponse

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)

# PUBLIC_INTERFACE
@router.get("/portfolio", response_model=PortfolioSummary, summary="Get user portfolio", description="Get the user's current portfolio and holdings summary.")
async def get_portfolio():
    return PortfolioSummary(total_value=10000.0, positions=[{"symbol": "AAPL", "amount": 50}])

# PUBLIC_INTERFACE
@router.get("/pnl", response_model=PnLReport, summary="Get user P&L", description="Profit and loss breakdown over period.")
async def get_pnl(period: str = "1w"):
    return PnLReport(period=period, pnl=123.45, breakdown={"AAPL": 80, "GOOG": 40})

# PUBLIC_INTERFACE
@router.get("/predictions", response_model=PredictionsResponse, summary="Get predictions", description="Get ML-based market predictions.")
async def get_predictions():
    return PredictionsResponse(recommendations=["AAPL Buy", "GOOG Hold"], confidence=0.87)
