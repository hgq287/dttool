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
        help="show program's version number and exit",
        action="store_true",
    ),
    "version_main": Arg(
        # Copy of version - used to have -V available with and without subcommand.
        "-V",
        "--version",
        help="show program's version number and exit",
        action="store_true",
    ),
    "reset": Arg(
        "--reset",
        help="Reset sample files to their original state.",
        action="store_true",
    ),
    "print_json": Arg(
        "--print-json",
        help="Print output in JSON format.",
        action="store_true",
        default=False,
    ),
    "export_csv": Arg(
        "--export-csv",
        help="Export to CSV-File."
        " This will disable table print."
        " Example: --export-csv hyperopt.csv",
        metavar="FILE",
    ),
    "convert_to_csv": Arg(
        "--convert-to-csv",
        help="Convert to CSV-File."
        " This will disable table print."
        " Example: -convert-to-csv import-file.feather export-file.csv",
        metavar="FILE",
    ),
}