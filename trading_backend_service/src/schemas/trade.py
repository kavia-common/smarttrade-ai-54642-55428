from pydantic import BaseModel, Field
from typing import Optional

# PUBLIC_INTERFACE
class TradeRequest(BaseModel):
    symbol: str = Field(..., example="AAPL")
    action: str = Field(..., example="buy")
    quantity: float = Field(..., gt=0)
    price: Optional[float] = Field(None, description="Limit price if applicable")

# PUBLIC_INTERFACE
class TradeResponse(BaseModel):
    status: str
    trade_id: Optional[str]
    detail: Optional[str]
