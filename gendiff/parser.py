import json
from pathlib import Path

import yaml


def file_parser(path_to_file):
    file_path = Path(path_to_file)
    if file_path.suffix == '.json':
        data = json.load(open(file_path, 'r', encoding='utf-8'))
    elif file_path.suffix in ('.yaml', '.yml'):
        data = yaml.safe_load(open(file_path, 'r', encoding='utf-8'))
    return data
