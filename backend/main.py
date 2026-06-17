from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from battery import get_battery_info
from system import get_system_info
from status import get_system_status
from insights import generate_insights
from events import get_events


app = FastAPI(
    title="PowerGuard API",
    description="Backend API for PowerGuard",
    version="1.0.0"
)

# CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "status": "online",
        "message": "PowerGuard API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/metrics")
def metrics():

    battery_data = get_battery_info()
    system_data = get_system_info()

    status_data = get_system_status(
        battery_data["percent"],
        system_data["cpu"],
        system_data["ram"]
    )

    insights_data = generate_insights(
        battery_data["percent"],
        system_data["cpu"],
        system_data["ram"],
        battery_data["charging"]
    )

    return {
        "battery": battery_data,
        "system": system_data,
        "status": status_data,
        "insights": insights_data,
        "events": get_events()
    }