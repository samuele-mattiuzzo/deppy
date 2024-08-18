import re

VERSION_REGEX = r'^(?P<name>[a-zA-Z0-9_\-]+)(?:\[(?P<extras>[a-zA-Z0-9_,\-]+)\])?(?P<operator>==|>=)(?P<version>[a-zA-Z0-9_.\-]+)$'


def read_requirements_file(path):
    """Reads a requirements file and returns the content as a list of lines."""
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_requirements(lines):
    """
    Parses a list of lines from a requirements file and returns a structured
    list of dependencies. Each dependency is a dictionary with keys such as
    'name', 'version', and 'extras'.
    """
    dependencies = []
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # Skip empty lines and comments

        # Simple regex to parse 'package==version' or 'package[extras]==version'
        compiled = re.compile(VERSION_REGEX)
        match = compiled.match(line)
        if match:
            dependency = {
                'name': match.group('name'),
                'version': match.group('version'),
                'extras': match.group('extras').split(',') if match.group('extras') else None
            }
            dependencies.append(dependency)
        else:
            print(f"Warning: Could not parse line: {line}")

    return dependencies
