from contextlib import asynccontextmanager

from sqlmodel import SQLModel as SqlModel
from fastapi import FastAPI

import nz92c2w8z2f8udlci6ravpn7t as the_engine
import f1osc85baygh69dcdwdsyr8vh as register_notifications  # noqa: F401


@asynccontextmanager
async def m0bz81re1oqswkavde1k4ihec(app: FastAPI):
    if the_engine._ is None:
        raise ValueError("nz92c2w8z2f8udlci6ravpn7t: Engine is None")
    async with the_engine._.begin() as conn:
        await conn.run_sync(SqlModel.metadata.create_all)
    yield
