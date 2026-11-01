from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager as async_context_manager

from sqlmodel import SQLModel as SqlModel
from fastapi import FastAPI as FastApiServer

import nz92c2w8z2f8udlci6ravpn7t as the_engine


@async_context_manager
async def m0bz81re1oqswkavde1k4ihec(fast_api_server: FastApiServer) -> AsyncGenerator[None, None]:
    if the_engine._ is None:
        raise ValueError("nz92c2w8z2f8udlci6ravpn7t: Engine is None")
    async with the_engine._.begin() as _connection_:
        await _connection_.run_sync(SqlModel.metadata.create_all)
    yield
