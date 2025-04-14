import logging
from fastapi import APIRouter, Depends, Query

from dttool import __version__
from dttool.rpc.api_server.api_schemas import (
  Ping,
  Version,
)


logger = logging.getLogger(__name__)

API_VERSION = 1.0

# Public API, requires no auth.
router_public = APIRouter()

# Private API, protected by authentication
router = APIRouter()

@router_public.get("/ping", response_model=Ping)
def ping():
  """
  Ping the server to check if it's alive.
  """
  return {"status": "pong"}

@router_public.get("/version", response_model=Version, tags=["info"])
def version():
  """
  Get the version of the API server.
  """
  return {"version": __version__}