from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel


DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)


# engine = sqlalchemy.create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

