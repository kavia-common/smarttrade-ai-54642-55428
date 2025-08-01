from fastapi import APIRouter
from src.schemas.portfolio import (
    PortfolioAllocationRequest, PortfolioAllocationResponse,
    ManualRebalanceRequest, ManualRebalanceResponse
)

router = APIRouter(
    prefix="/api/portfolio",
    tags=["Portfolio Management"]
)

# PUBLIC_INTERFACE
@router.post("/allocate", response_model=PortfolioAllocationResponse, summary="Set target allocations", description="Set or update portfolio allocations.")
async def allocate_portfolio(payload: PortfolioAllocationRequest):
    return PortfolioAllocationResponse(status="success", message="Allocation updated.")

# PUBLIC_INTERFACE
@router.post("/rebalance/manual", response_model=ManualRebalanceResponse, summary="Manual portfolio rebalance", description="Manually rebalance portfolio with provided trades.")
async def manual_rebalance(payload: ManualRebalanceRequest):
    return ManualRebalanceResponse(status="success", message="Rebalance processed.")
