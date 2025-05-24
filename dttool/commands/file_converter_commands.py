
from typing import Any
from dttool.file_converter.converter import Converter
from dttool.constants import Config

def convert_file(args: dict[str, Any]) -> None:
    """
    Convert files between different formats.
    :param args: The arguments passed to the command.
    :return: The return code of the command.
    """

    convert_arg = args["convert_to_csv"].split(" ")
    config: Config = {
        "file_converter_dir": "user_data/data/file_converter", 
        "input_filename": convert_arg[0],  
        "output_filename": convert_arg[1],
        "include_index": args.get("index", False),
    }


    print(f"Input file: {config['input_filename']}")
    print(f"Output file: {config['output_filename']}")

    converter = Converter(config)
    input_ext = config['input_filename'].split('.')[-1].lower()
    output_ext = config['output_filename'].split('.')[-1].lower()

    operation = f"{input_ext}_to_{output_ext}"
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