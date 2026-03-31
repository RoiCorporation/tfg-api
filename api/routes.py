from fastapi import APIRouter, HTTPException, Header, Depends
from api.config import API_KEY, SessionDep
from api.models import EnvironmentalReadings


router = APIRouter(prefix="/api", tags=["api"])


def get_api_key(x_api_key: str = Header()):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key


@router.post("/insert-station-readings/")
def insert_station_readings(
    readings: EnvironmentalReadings,
    session: SessionDep,
    api_key: str = Depends(get_api_key)
):
    db_reading = EnvironmentalReadings.model_validate(readings)
    session.add(db_reading)
    session.commit()
    session.refresh(db_reading)
    return db_reading
