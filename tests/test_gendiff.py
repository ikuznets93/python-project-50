from pathlib import Path

from gendiff.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_gendiff():
    file1_path = get_test_data_path('testfile1.json')
    file2_path = get_test_data_path('testfile2.json')
    actual = generate_diff(file1_path, file2_path)
    expected = read_file('expected_result.txt')

    assert actual == expected

