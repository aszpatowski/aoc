import pytest
from pathlib import Path
from .solution import solve

testdata = [
    (Path(__file__).parent / "example.txt", 357),
    (Path(__file__).parent / "input.txt", 17383),
]


@pytest.mark.parametrize("file_path, expected_number", testdata)
def test_calculate(file_path, expected_number):
    assert solve(file_path) == expected_number
