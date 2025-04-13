import logging
from typing import Any

import orjson
import uvicorn
from fastapi import Depends, FastAPI

from starlette.responses import JSONResponse 


class FTJSONResponse(JSONResponse):
  media_type = "application/json"

  def render(self, content: Any) -> bytes:
    """
    Render the content to JSON format using orjson.

    :param content: The content to be rendered.
    :return: The rendered JSON bytes.
    """
    return orjson.dumps(content, option=orjson.OPT_SERIALIZE_NUMPY)

class ApiServer:
  """
  A class to represent an API web server.
  """

  def __init__(self, host: str, port: int) -> None:
    """
    Initialize the ApiServer instance.

    :param host: The host of the web server.
    :param port: The port of the web server.
    """
    self.host = host
    self.port = port
    print(f"ApiServer initialized at {self.host}:{self.port}")

    self.app = FastAPI(
      title="Dttool API",
      description="API for dttool",
      version="0.1.0",
      default_response_class=FTJSONResponse,
    )

    self.start_api()

  def start_api(self):
    """
    Start the API server.
    """
    print(f"Starting API server at {self.host}:{self.port}")
    
    uvconfig = uvicorn.Config(
      self.app,
      port=4096,
      host='127.0.0.1',
      use_colors=False,
      log_config=None,
    )
    
    try:
      server = uvicorn.Server(uvconfig)
      server.run()
    except Exception as e:
      logging.error(f"Error starting server: {e}")
      raise
    finally:
      logging.info("Server stopped")