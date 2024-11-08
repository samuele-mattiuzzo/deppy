# deppy/utils.py

import os
import re
import toml


def read_requirements_file(file_path):
    """Reads dependencies from a requirements.txt-style file."""
    with open(file_path, 'r') as f:
        return f.readlines()


def read_pipfile(file_path):
    """Reads dependencies from Pipfile."""
    with open(file_path, 'r') as f:
        return f.readlines()


def read_pyproject_toml(file_path):
    """Reads dependencies from pyproject.toml."""
    data = toml.load(file_path)
    dependencies = data.get('project', {}).get('dependencies', [])
    optional_dependencies = data.get('project', {}).get('optional-dependencies', {}).values()
    all_dependencies = dependencies + [dep for optional in optional_dependencies for dep in optional]
    return all_dependencies


def read_setup_py(file_path):
    """Extracts dependencies from setup.py by reading `install_requires`."""
    # Here we'll use regex or manual parsing to extract install_requires list.
    dependencies = []
    with open(file_path, 'r') as f:
        content = f.read()
        install_requires_match = re.search(r'install_requires\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if install_requires_match:
            # Extract individual dependencies from the list
            raw_deps = install_requires_match.group(1)
            dependencies = [dep.strip().strip("'").strip('"') for dep in raw_deps.split(',')]
    return dependencies


def detect_dependency_file(directory):
    """Detects the type of dependency file present in a directory."""
    supported_files = ['requirements.txt', 'Pipfile', 'pyproject.toml', 'setup.py']
    for file in supported_files:
        file_path = os.path.join(directory, file)
        if os.path.exists(file_path):
            return file_path, file
    return None, None


def parse_requirements(lines):
    """Parses a list of lines from a requirements-style file."""
    dependencies = []
    package_pattern = re.compile(
        r'^(?P<name>[a-zA-Z0-9_\-]+)(?:\[(?P<extras>[a-zA-Z0-9_,\-]+)\])?(?P<operator>==|>=)?(?P<version>[a-zA-Z0-9_.\-]+)?$'
    )

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        match = package_pattern.match(line)
        if match:
            dependencies.append({
                'name': match.group('name'),
                'version': match.group('version'),
                'extras': match.group('extras').split(',') if match.group('extras') else None,
            })
        else:
            print(f"Warning: Could not parse line: {line}")

    return dependencies
