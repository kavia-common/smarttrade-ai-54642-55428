from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import auth, onboarding, dashboard, signals, portfolio, trade, notification, account

openapi_tags = [
    {"name": "Authentication", "description": "User login, signup, and auth flow."},
    {"name": "Onboarding & KYC", "description": "User onboarding and risk profiling."},
    {"name": "Dashboard", "description": "Portfolio overview, P&L, predictions."},
    {"name": "Signals & Sentiment", "description": "Signal explorer and sentiment endpoints."},
    {"name": "Portfolio Management", "description": "Manage target allocations, rebalances."},
    {"name": "Trade Execution", "description": "Trade placement and execution."},
    {"name": "Notifications", "description": "Alerting and notification system."},
    {"name": "Account & API Keys", "description": "Account settings and API key controls."},
    {"name": "WebSocket", "description": "Real-time push notification interfaces."},
]

app = FastAPI(
    title="SmartTrade.AI Backend API",
    description="API for authentication, onboarding, dashboard, signals, portfolio, trading, notifications, and integrations.",
    version="0.1.0",
    openapi_tags=openapi_tags
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router Registry
app.include_router(auth.router)
app.include_router(onboarding.router)
app.include_router(dashboard.router)
app.include_router(signals.router)
app.include_router(portfolio.router)
app.include_router(trade.router)
app.include_router(notification.router)
app.include_router(account.router)

@app.get("/", tags=["Health"])
def health_check():
    """Health check route."""
    return {"message": "Healthy"}
