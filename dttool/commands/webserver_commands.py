from typing import Any

def start_webserver(args: dict[str, Any]) -> None:
  """
  Start the web server.

  :param args: The arguments passed to the command.
  :return: The return code of the command.
  """
  from dttool.rpc.api_server.webserver import ApiServer

  # Initialize the web server
  config = {            
    "api_server": {
      "enabled": True,
      "listen_ip_address": "127.0.0.1",
      "listen_port": 4096,
      "CORS_origins": ["http://localhost"],
      "username": "",
      "password": "",
    }
  }
  ApiServer(config, standalone=True)