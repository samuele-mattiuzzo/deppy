# tests/test_analyzer.py

import os
import pytest
from unittest import mock
from deppy.analyzer import analyze_dependencies


class TestAnalyzer:
    @pytest.fixture
    def sample_requirements_file(self, tmp_path):
        """Creates a sample requirements.txt file for testing."""
        content = """
        requests==2.26.0
        flask[async]==2.0.1
        pytest>=6.2.5
        black
        """
        file_path = tmp_path / "requirements.txt"
        file_path.write_text(content)
        return str(file_path)

    @pytest.fixture
    def sample_pipfile(self, tmp_path):
        """Creates a sample Pipfile for testing."""
        content = """
        [packages]
        requests = "==2.26.0"
        flask = {version = "==2.0.1", extras = ["async"]}

        [dev-packages]
        pytest = ">=6.2.5"
        black = "*"
        """
        file_path = tmp_path / "Pipfile"
        file_path.write_text(content)
        return str(file_path)

    @pytest.fixture
    def sample_pyproject_toml(self, tmp_path):
        """Creates a sample pyproject.toml file for testing."""
        content = """
        [project]
        dependencies = [
            "requests==2.26.0",
            "flask[async]==2.0.1",
            "pytest>=6.2.5",
            "black"
        ]
        optional-dependencies = {
            test = ["pytest", "mock"]
        }
        """
        file_path = tmp_path / "pyproject.toml"
        file_path.write_text(content)
        return str(file_path)

    def test_analyze_dependencies_requirements(self, tmp_path, sample_requirements_file):
        """Test analyzing dependencies from requirements.txt."""
        dependencies = analyze_dependencies(tmp_path)
        expected_dependencies = [
            {'name': 'requests', 'version': '2.26.0', 'extras': None},
            {'name': 'flask', 'version': '2.0.1', 'extras': ['async']},
            {'name': 'pytest', 'version': None, 'extras': None},
            {'name': 'black', 'version': None, 'extras': None},
        ]
        assert dependencies == expected_dependencies

    def test_analyze_dependencies_pipfile(self, tmp_path, sample_pipfile):
        """Test analyzing dependencies from Pipfile."""
        dependencies = analyze_dependencies(tmp_path)
        expected_dependencies = [
            {'name': 'requests', 'version': '2.26.0', 'extras': None},
            {'name': 'flask', 'version': '2.0.1', 'extras': ['async']},
            {'name': 'pytest', 'version': None, 'extras': None},
            {'name': 'black', 'version': None, 'extras': None},
        ]
        assert dependencies == expected_dependencies

    def test_analyze_dependencies_pyproject_toml(self, tmp_path, sample_pyproject_toml):
        """Test analyzing dependencies from pyproject.toml."""
        dependencies = analyze_dependencies(tmp_path)
        expected_dependencies = [
            {'name': 'requests', 'version': '2.26.0', 'extras': None},
            {'name': 'flask', 'version': '2.0.1', 'extras': ['async']},
            {'name': 'pytest', 'version': None, 'extras': None},
            {'name': 'black', 'version': None, 'extras': None},
        ]
        assert dependencies == expected_dependencies
