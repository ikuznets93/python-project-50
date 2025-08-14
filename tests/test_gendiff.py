from pathlib import Path

from gendiff.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_json():
    file1_path = get_test_data_path('testfile1.json')
    file2_path = get_test_data_path('testfile2.json')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_result.txt')

    assert actual == expected


'''
def test_json_one_empty():
    file1_path = get_test_data_path('testfile1.json')
    file2_path = get_test_data_path('testfile_empty1.json')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_one_empty.txt')

    assert actual == expected


def test_json_empty():
    file1_path = get_test_data_path('testfile_empty1.json')
    file2_path = get_test_data_path('testfile_empty2.json')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_empty.txt')

    assert actual == expected
'''


def test_yaml():
    file1_path = get_test_data_path('testfile1.yml')
    file2_path = get_test_data_path('testfile2.yaml')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_result.txt')

    assert actual == expected


'''
def test_yaml_one_empty():
    file1_path = get_test_data_path('testfile1.yml')
    file2_path = get_test_data_path('testfile_empty1.yml')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_one_empty.txt')

    assert actual == expected


def test_yaml_empty():
    file1_path = get_test_data_path('testfile_empty1.yml')
    file2_path = get_test_data_path('testfile_empty2.yml')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_empty.txt')

    assert actual == expected
'''


def test_json_yaml():
    file1_path = get_test_data_path('testfile1.yml')
    file2_path = get_test_data_path('testfile2.json')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_result.txt')

    assert actual == expected