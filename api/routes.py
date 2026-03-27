from fastapi import APIRouter
from api.config import SessionDep
from api.models import EnvironmentalReadings


router = APIRouter(prefix="/tfg/api", tags=["api"])


@router.post("/insert_station_readings/")
def insert_station_readings(readings: EnvironmentalReadings, session: SessionDep):
    session.add(readings)
    session.commit()
    session.refresh(readings)
    return readings
