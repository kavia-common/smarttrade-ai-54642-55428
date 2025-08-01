from typing import List
from pydantic import BaseModel

# PUBLIC_INTERFACE
class PortfolioAllocationRequest(BaseModel):
    allocations: List[dict]

# PUBLIC_INTERFACE
class PortfolioAllocationResponse(BaseModel):
    status: str
    message: str

# PUBLIC_INTERFACE
class ManualRebalanceRequest(BaseModel):
    actions: List[dict]

# PUBLIC_INTERFACE
class ManualRebalanceResponse(BaseModel):
    status: str
    message: str
