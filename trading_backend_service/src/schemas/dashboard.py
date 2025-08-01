from typing import List, Dict, Any
from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class PortfolioSummary(BaseModel):
    """Summary of user's portfolio holdings."""
    total_value: float = Field(..., example=25000.00)
    positions: List[Dict[str, Any]] = Field(..., description="List of stock/crypto holdings")

# PUBLIC_INTERFACE
class PnLReport(BaseModel):
    """Profit & Loss over selectable intervals."""
    period: str = Field(..., example="1w")
    pnl: float
    breakdown: Dict[str, float]

# PUBLIC_INTERFACE
class PredictionsResponse(BaseModel):
    """ML model's market predictions for user dashboard."""
    recommendations: List[str]
    confidence: float
