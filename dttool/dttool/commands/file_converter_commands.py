
from typing import Any
from dttool.file_converter.converter import Converter
from dttool.constants import Config

def convert_file(args: dict[str, Any]) -> None:
    """
    Convert files between different formats.
    :param args: The arguments passed to the command.
    :return: The return code of the command.
    """

    config: Config = {
        "file_converter_dir": "user_data/data/file_converter", 
        "source_filename": args["source"],  
        "destination_filename": args["destination"],
        "index": args.get("index", False),
    }

    print(f"Converting {args['source']} to {args['destination']}...")

    converter = Converter(config)
    operation = f"{args.from_format}_to_{args.to_format}"
    match operation:
        case "feather_to_excel":
            converter.feather_to_excel()
        case "excel_to_feather":
            converter.excel_to_feather()
        case "csv_to_feather":
            converter.csv_to_feather()
        case "feather_to_csv":
            converter.feather_to_csv()
        case _:
            raise ValueError(f"Unsupported operation: {operation}")