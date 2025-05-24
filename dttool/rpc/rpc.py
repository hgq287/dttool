class RPC:
  def __init__(self, host: str, port: int) -> None:
    """
    Initialize the RPC instance.

    :param host: The host of the RPC server.
    :param port: The port of the RPC server.
    """
    self.host = host
    self.port = port
    print(f"RPC initialized at {self.host}:{self.port}")