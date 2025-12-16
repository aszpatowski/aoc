import argparse
import shutil
from pathlib import Path


def generate_year_from_template(year: int, start_day: int, end_day: int):
    """Generate advent of code directory structure from template."""
    utils_dir = Path(__file__).parent
    template_dir = utils_dir / "template"
    output_dir = utils_dir.parent / str(year)

    # Create year directory, we dont want to overwrite existing years
    if output_dir.exists():
        raise FileExistsError(f"Directory {output_dir} already exists")
    output_dir.mkdir(exist_ok=False)

    # Copy __init__.py from template if it exists
    template_init = template_dir / "__init__.py"
    if template_init.exists():
        shutil.copy(template_init, output_dir / "__init__.py")

    # Generate day directories
    for day in range(start_day, end_day + 1):
        day_name = f"day{day:02d}"
        template_day_dir = template_dir / "day00"
        output_day_dir = output_dir / day_name

        # Copy entire day directory
        if output_day_dir.exists():
            raise FileExistsError(f"Directory {output_day_dir} already exists")
        shutil.copytree(template_day_dir, output_day_dir)

        print(f"Created {day_name}")

    print(
        f"Generated {year} from template (days {start_day}-{end_day}).\n Happy coding!"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Advent of Code year structure from template"
    )
    parser.add_argument("year", type=int, help="Year to generate")
    parser.add_argument(
        "--start-day", type=int, default=1, help="Start day (default: 1)"
    )
    parser.add_argument("--end-day", type=int, default=24, help="End day (default: 24)")

    args = parser.parse_args()
    generate_year_from_template(args.year, args.start_day, args.end_day)
