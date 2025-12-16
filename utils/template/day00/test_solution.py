import pytest
from pathlib import Path
from .solution import solve

testdata = [
    (Path(__file__).parent / "example.txt", 0),  # Change 0 to real number from task
    # (Path(__file__).parent / "input.txt", <solution>), # To optimize after first proper solution
]


@pytest.mark.parametrize("file_path, expected_number", testdata)
def test_solve(file_path, expected_number):
    assert solve(file_path) == expected_number
