from argparse import ArgumentParser, Namespace, _ArgumentGroup
from functools import partial
from pathlib import Path
from typing import Any, Optional, Union

class Arguments:
  """
  Arguments Class. Manage the arguments received by the cli
  """

  def __init__(self, args: Optional[list[str]]) -> None:
    self.args = args
    self._parsed_arg: Optional[Namespace] = None