# DEPPY

## Overview

The Python Dependency Analyzer is be a tool that helps developers manage and optimize the dependencies of their Python projects.
The tool focuses on identifying outdated, insecure, or unnecessary packages and provide recommendations for upgrades or replacements.
It offers insights into dependency trees, compatibility issues, and license compliance.

## Key Features

*Dependency Analysis:*

- Parse requirements.txt, Pipfile, or poetry.lock to list all dependencies and their versions.
- Visualize the dependency tree, showing relationships between packages and their sub-dependencies.
- Detect and highlight outdated dependencies with available updates.
- Identify insecure packages by cross-referencing known vulnerability databases (like the Python Package Advisory Database).

*Compatibility Checks:*

- Ensure compatibility between the Python version and dependencies.
- Detect conflicting dependencies that could cause runtime errors or failures during installation.

*License Compliance:*

- Analyze the licenses of all dependencies and ensure compliance with the project's licensing policy.
- Highlight any packages with restrictive or incompatible licenses.


*Upgrade Recommendations:*

- Suggest safe upgrades for dependencies with minimal risk of breaking changes.
- Optionally, recommend alternatives to packages that are no longer maintained.

*Report Generation:*

- Generate detailed reports of the dependency analysis, including security risks, outdated packages, and license compliance issues.
- Provide actionable insights to improve dependency health.
