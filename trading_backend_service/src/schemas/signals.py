from typing import List, Dict
from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class SignalExplorerQuery(BaseModel):
    asset: str
    timeframe: str

# PUBLIC_INTERFACE
class SignalExplorerResponse(BaseModel):
    signals: List[Dict[str, str]]
    sentiment: float = Field(..., description="Market sentiment score [-1,1]")
