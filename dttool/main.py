import logging
import sys
from typing import Any, Optional

from dttool import __version__
from dttool.exceptions import OperationalException

# check min. python version (>= 3.10 required)
if sys.version_info < (3, 10):  # pragma: no cover
  sys.exit("Dttool requires Python version >= 3.10")

from dttool.commands import Arguments

logger = logging.getLogger("dttool")

def main(sysargv: Optional[list[str]] = None) -> None:
  return_code: Any = 1
  try:
    print("Dttool CLI")
    arguments = Arguments(sysargv)
    args = arguments.get_parsed_arg()

    # Call subcommand.
    if "func" in args:
        logger.info(f"dttool {__version__}")
        return_code = args["func"](args)
    else:
        # No subcommand was issued.
        raise OperationalException(
            "Usage of Dttool requires a subcommand to be specified.\n"
            "To see the full list of options available, please use "
            "`dttool --help` or `dttool <command> --help`."
        )
  finally:
    print("Exiting dttool")
    sys.exit(return_code)
  
if __name__ == "__main__":  # pragma: no cover
  main()