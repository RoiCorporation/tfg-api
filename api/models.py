from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from api.utils import now_utc


MAX_STATION_NAME_LENGTH = 50


class Station(SQLModel, table=True):
    __tablename__ = "stations_station"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=MAX_STATION_NAME_LENGTH, nullable=False)
    is_central_station: bool = Field(default=True, nullable=False)


class ConnectedStations(SQLModel, table=True):
    __tablename__ = "stations_connected_stations"

    central_station_id: int = Field(
        foreign_key="stations_station.id",
        primary_key=True,
        nullable=False,
    )
    wireless_station_id: int = Field(
        foreign_key="stations_station.id",
        primary_key=True,
        nullable=False,
        unique=True,  # equivalent to OneToOneField behavior
    )
    pairing_date: datetime = Field(default_factory=now_utc, nullable=False)


class EnvironmentalReadings(SQLModel, table=True):
    __tablename__ = "stations_environmental_readings"

    station_id: int = Field(
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
    co_concentration: Optional[float] = Field(default=None)
    ch4_concentration: Optional[float] = Field(default=None)
    c3h8_concentration: Optional[float] = Field(default=None)
    oh_concentration: Optional[float] = Field(default=None)
    h2_concentration: Optional[float] = Field(default=None)
