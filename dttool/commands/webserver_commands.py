from typing import Any

def start_webserver(args: dict[str, Any]) -> None:
  """
  Start the web server.

  :param args: The arguments passed to the command.
  :return: The return code of the command.
  """
  from dttool.rpc.api_server.webserver import ApiServer

  print("Starting web server...")

  # Initialize the web server
  ApiServer(host=args.host, port=args.port)