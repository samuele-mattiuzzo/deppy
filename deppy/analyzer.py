import os
from deppy.utils import read_requirements_file, parse_requirements


def analyze_dependencies(requirements_path):
    """Analyze dependencies from a requirements file."""
    if not os.path.exists(requirements_path):
        raise FileNotFoundError(f"Requirements file not found: {requirements_path}")

    # Read the requirements file
    raw_dependencies = read_requirements_file(requirements_path)

    # Parse the dependencies
    dependencies = parse_requirements(raw_dependencies)

    # Count the number of dependencies
    num_dependencies = len(dependencies)
    print(f"Found {num_dependencies} dependencies in {requirements_path}.")

    # @TODO:
    # - check specific versions
    # - check outdated packages
    # - check conflicts
    # - report/summary of dependencies

    return dependencies
