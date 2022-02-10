import json
from pathlib import Path


def read_tmp_file(filepath: Path):
    """
    Reads data provided with tmp file.
    :return dict if tmp file is json-formatted
    else plain text
    """
    if filepath.name.endswith('.json'):
        return json.load(filepath.open())
    else:
        return filepath.read_text()


class Converter:
    @staticmethod
    def bytes_to_mbytes(val: int):
        return val >> 20

    @staticmethod
    def bits_to_mbits(val):
        return val / 1_000_000
