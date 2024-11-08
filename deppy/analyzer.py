# deppy/analyzer.py

import os

from deppy.utils import (
    read_requirements_file, read_pipfile, read_pyproject_toml, read_setup_py,
    detect_dependency_file, parse_requirements
)


def analyze_dependencies(directory='.'):
    """Analyzes dependencies from various types of dependency files."""
    file_path, file_type = detect_dependency_file(directory)

    if not file_path:
        raise FileNotFoundError(
            "No supported dependency files found in the directory."
        )

    print(f"Analyzing dependencies from {file_type}...")

    # Read the appropriate file based on its type
    if file_type == 'requirements.txt':
        raw_lines = read_requirements_file(file_path)
        dependencies = parse_requirements(raw_lines)
    elif file_type == 'Pipfile':
        raw_lines = read_pipfile(file_path)
        dependencies = parse_requirements(raw_lines)
    elif file_type == 'pyproject.toml':
        raw_lines = read_pyproject_toml(file_path)
        # No need to parse again, `read_pyproject_toml`
        # returns dependency lists
        dependencies = [
            {'name': dep, 'version': None, 'extras': None} for dep in raw_lines
        ]
    elif file_type == 'setup.py':
        raw_lines = read_setup_py(file_path)
        dependencies = parse_requirements(raw_lines)

    return dependencies
