# Deppy: Dependency Analyzer for Python

![GitHub Tag](https://img.shields.io/github/v/tag/samuele-mattiuzzo/deppy) ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/samuele-mattiuzzo/deppy/run_tests.yml) ![GitHub License](https://img.shields.io/github/license/samuele-mattiuzzo/deppy)

Deppy is a powerful tool designed to help Python developers manage and optimize the dependencies in their projects. It provides insights into outdated, insecure, or unnecessary packages and offers recommendations for upgrades or replacements. Deppy also ensures compatibility, license compliance, and overall dependency health.

## Key Features

- **Dependency Analysis**
  - Parse `requirements.txt`, `Pipfile`, and `poetry.lock` files.
  - Visualize dependency trees and identify outdated packages.
  - Cross-reference with known vulnerability databases for insecure packages.

- **Compatibility Checks**
  - Verify compatibility between Python versions and dependencies.
  - Detect conflicts that could lead to runtime errors.

- **License Compliance**
  - Analyze licenses and ensure compatibility with your project’s licensing policies.
  - Highlight packages with restrictive or incompatible licenses.

- **Upgrade Recommendations**
  - Suggest safe upgrades and alternative packages.
  
- **Report Generation**
  - Generate detailed reports in JSON, HTML, and PDF formats.

## Installation

Install Deppy using pip:

```bash
pip install deppy
```

## Usage

Please refer to the [usage document](/docs/USAGE.md) for instructions on how to use the tool

## Contributing

We welcome contributions! Please read our [contributing guidelines](/docs/CONTRIBUTING.md) before making a pull request

## Other links

- [Development roadmap](/docs/ROADMAP.md)

- [Known issues](/docs/ISSUES.md)
