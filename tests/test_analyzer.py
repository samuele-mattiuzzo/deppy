import unittest
from unittest.mock import patch, mock_open
from deppy.analyzer import analyze_dependencies


class TestAnalyzer(unittest.TestCase):

    @patch("deppy.analyzer.os.path.exists")
    @patch("deppy.analyzer.read_requirements_file")
    @patch("deppy.analyzer.parse_requirements")
    def test_analyze_dependencies_success(self, mock_parse, mock_read, mock_exists):
        # Mock the file exists check to return True
        mock_exists.return_value = True

        # Mock the reading and parsing functions
        mock_read.return_value = ["pkg==1.2.3", "pkg[extras]==1.2.3"]
        mock_parse.return_value = [
            {'name': 'pkg', 'version': '1.2.3', 'extras': None},
            {'name': 'pkg', 'version': '1.2.3', 'extras': ['extras']}
        ]

        # Call the function
        result = analyze_dependencies("requirements.txt")

        # Check the results
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'pkg')
        self.assertEqual(result[1]['extras'], ['extras'])

        # Ensure mocks were called
        mock_exists.assert_called_once_with("requirements.txt")
        mock_read.assert_called_once_with("requirements.txt")
        mock_parse.assert_called_once_with(["pkg==1.2.3", "pkg[extras]==1.2.3"])

    @patch("deppy.analyzer.os.path.exists")
    def test_analyze_dependencies_file_not_found(self, mock_exists):
        # Mock the file exists check to return False
        mock_exists.return_value = False

        # Expect FileNotFoundError to be raised
        with self.assertRaises(FileNotFoundError):
            analyze_dependencies("requirements.txt")

        # Ensure the mock was called
        mock_exists.assert_called_once_with("requirements.txt")


if __name__ == '__main__':
    unittest.main()
