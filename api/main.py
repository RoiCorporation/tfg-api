from fastapi import FastAPI
from api.config import create_db_and_tables
from api.routes import router


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
