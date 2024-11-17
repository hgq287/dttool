from dttool import __version__

class Arg:
  # Optional CLI arguments
  def __init__(self, *args, **kwargs):
    self.cli = args
    self.kwargs = kwargs


# List of available command line options
AVAILABLE_CLI_OPTIONS = {
  # Common options
  "logfile": Arg(
    "--logfile",
    "--log-file",
    help="Log to the file specified. Special values are: 'syslog', 'journald'. "
    "See the documentation for more details.",
    metavar="FILE",
  ),
  "version": Arg(
    "-V",
    "--version",
    action="version",
    version=f"%(prog)s {__version__}",
  ),
}