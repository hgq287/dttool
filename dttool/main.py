import logging
import sys
from typing import Any, Optional

# check min. python version (>= 3.10 required)
if sys.version_info < (3, 10):  # pragma: no cover
  sys.exit("Dttool requires Python version >= 3.10")

from dttool.commands import Arguments

logger = logging.getLogger("dttool")
def main(sysargv: Optional[list[str]] = None) -> None:
  return_code: Any = 1
  try:
    arguments = Arguments(sysargv)
    args = arguments.get_parsed_arg()
    print(args)
  finally:
    sys.exit(return_code)
  
if __name__ == "__main__":  # pragma: no cover
  main()