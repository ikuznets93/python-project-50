import json

def json_parsing(file_path):
    data = json.load(open(file_path, 'r', encoding='utf-8'))
    return data

# json.load(open('/home/dragoongo/files_for_project/file2.json'))



def generate_diff(file_path1, file_path2):
    data1 = json_parsing(file_path1)
    data2 = json_parsing(file_path2)
    pass


def gen_diff(data1, data2):
    keys = data1.keys() | data2.keys()  # https://youtu.be/vkUTX1hruF8?t=929
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = 'added'
        elif key not in data2:
            result[key] = 'deleted'
        elif data1[key] == data2[key]:
            result[key] = 'unchanged'
        else:
            result[key] = 'changed'
    return result   