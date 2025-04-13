import logging

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