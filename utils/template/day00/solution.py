"""
<task>
"""

from pathlib import Path

file_path = Path(__file__).parent / "input.txt"


def solve(file_path: str) -> int:
    return 0


def main():
    print(solve(file_path))


if __name__ == "__main__":
    main()
