import json

def json_parsing(file_path):
    data = json.load(open(file_path, 'r', encoding='utf-8'))
    return data

def generate_diff(file_path1, file_path2):
    data1 = json_parsing(file_path1)
    data2 = json_parsing(file_path2)

    keys = data1.keys() | data2.keys()
    result = {}
    for key in keys:
        if key not in data1:
            result[f'+ {key}'] = data2[key]
        elif key not in data2:
            result[f'- {key}'] = data1[key]
        elif data1[key] == data2[key]:
            result[f'  {key}'] = data2[key]
        else:
            result[f'- {key}'] = data1[key]
            result[f'+ {key}'] = data2[key]
    str_result = '\n'.join(f'{k}: {v}' for k, v in result.items())
    return print(str_result)