# Advent of Code Solutions

[![AOC](https://github.com/aszpatowski/aoc/actions/workflows/python-app.yml/badge.svg)](https://github.com/aszpatowski/aoc/actions/workflows/python-app.yml)
[![Coverage Status](https://coveralls.io/repos/github/aszpatowski/aoc/badge.svg?branch=main)](https://coveralls.io/github/aszpatowski/aoc?branch=main)

A Python project containing solutions to the [Advent of Code](https://adventofcode.com/2025) challenges.

## Project Overview

This repository contains daily puzzle solutions for Advent of Code. Each day's solution is organized in its own directory with:

- **solution.py** - The main puzzle solving logic
- **test_solution.py** - Unit tests with example and actual inputs
- **example.txt** - Example input provided in the puzzle description
- **input.txt** - Actual puzzle input

## Project Structure

```
aoc/
├── main.py              # Entry point
├── pyproject.toml       # Project configuration and dependencies
├── README.md           # This file
└── <year>/
    ├── day01/
    ├── day02/
    ├── day03/
    ├── ...
    └── day24/
```

Each day directory contains the solution for that puzzle along with test cases.

## Installation

Install dependencies using [uv](https://docs.astral.sh/uv/):

```bash
# Using u
uv sync
```

## Running Tests

Run all tests across all days:

```bash
# Using uv
uv run pytest

# Using pytest directly
pytest
```

Run tests for a specific day:

```bash
uv run pytest 2025/day01/

# or using pytest directly
pytest 2025/day01/
```

Run tests with coverage:

```bash
uv run pytest --cov=2025 --cov-report=html
```

## Running Solutions

Run a specific day's solution:

```bash
uv run python -m 2025.day01.solution

# or using pytest directly
python -m 2025.day01.solution
```

## Code Quality

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and formatting.

Check for linting issues:

```bash
uv run ruff check ./2025/
```

Format code:

```bash
uv run ruff format ./2025/
```
