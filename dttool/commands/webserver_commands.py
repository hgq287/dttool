from typing import Any

def start_webserver(args: dict[str, Any]) -> None:
  """
  Start the web server.

  :param args: The arguments passed to the command.
  :return: The return code of the command.
  """
  from dttool.rpc.api_server.webserver import ApiServer

  # Initialize the web server
  ApiServer(host='127.0.0.1', port=8080)