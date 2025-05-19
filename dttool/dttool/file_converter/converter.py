import pandas as pd
from pathlib import Path
from dttool.constants import Config


class Converter:
    """
    A class to convert files between different formats.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

        basedir = Path(config["file_converter_dir"])
        source_filename = config["source_filename"]
        destination_filename = config["destination_filename"]

        self.input_path = basedir / "input" / source_filename
        self.output_path = basedir / "output" / destination_filename
        self.index = config.get("index", False)

    def feather_to_excel(self):
        df = pd.read_feather(self.input_path)
        df.to_excel(self.output_path, index=self.index)
        print(f"Converted '{self.input_path}' to '{self.output_path}'")

    def excel_to_feather(self):
        df = pd.read_excel(self.input_path)
        df.to_feather(self.output_path)
        print(f"Converted '{self.input_path}' to '{self.output_path}'")

    def csv_to_feather(self):
        df = pd.read_csv(self.input_path)
        df.to_feather(self.output_path)
        print(f"Converted '{self.input_path}' to '{self.output_path}'")

    def feather_to_csv(self):
        df = pd.read_feather(self.input_path)
        df.to_csv(self.output_path, index=False)
        print(f"Converted '{self.input_path}' to '{self.output_path}'")