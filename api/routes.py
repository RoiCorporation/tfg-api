from fastapi import APIRouter
from api.config import SessionDep
from api.models import EnvironmentalReadings


router = APIRouter(prefix="/api", tags=["api"])


@router.post("/insert-station-readings/")
def insert_station_readings(readings: EnvironmentalReadings, session: SessionDep):
    session.add(readings)
    session.commit()
    session.refresh(readings)
    return readings
