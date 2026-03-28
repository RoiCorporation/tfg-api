from datetime import datetime
import uuid
from typing import Optional
from sqlmodel import SQLModel, Field
from api.utils import now_utc


MAX_STATION_NAME_LENGTH = 50


class Station(SQLModel, table=True):
    __tablename__ = "stations_station"

    id: Optional[uuid.UUID] = Field(default=uuid.uuid4, primary_key=True, unique=True)
    name: str = Field(max_length=MAX_STATION_NAME_LENGTH, nullable=False)
    is_central_station: bool = Field(default=True, nullable=False)


class ConnectedStations(SQLModel, table=True):
    __tablename__ = "stations_connected_stations"

    central_station_id: uuid.UUID = Field(
        foreign_key="stations_station.id",
        primary_key=True,
        nullable=False,
    )
    wireless_station_id: uuid.UUID = Field(
        foreign_key="stations_station.id",
        primary_key=True,
        nullable=False,
        unique=True,  # equivalent to OneToOneField behavior
    )
    pairing_date: datetime = Field(default_factory=now_utc, nullable=False)


class EnvironmentalReadings(SQLModel, table=True):
    __tablename__ = "stations_environmental_readings"

    station_id: uuid.UUID = Field(
        foreign_key="stations_station.id",
        primary_key=True,
        nullable=False,
    )
    taken_at: datetime = Field(
        default_factory=now_utc,
        primary_key=True,
        nullable=False,
    )

    temperature: Optional[float] = Field(default=None)
    humidity: Optional[float] = Field(default=None)
    light_intensity: Optional[float] = Field(default=None)
    air_pressure: Optional[float] = Field(default=None)
    iaq: Optional[float] = Field(default=None)
    carbon_monoxide_concentration: Optional[float] = Field(default=None)
    methane_concentration: Optional[float] = Field(default=None)
    propane_concentration: Optional[float] = Field(default=None)
    alcohol_concentration: Optional[float] = Field(default=None)
    hydrogen_gas_concentration: Optional[float] = Field(default=None)
