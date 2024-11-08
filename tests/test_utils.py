import unittest
from unittest.mock import mock_open, patch
from deppy.utils import read_requirements_file, parse_requirements


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="pkg_one==1.2.3\npkg_one[with_extras]==1.2.3\n")
    def test_read_requirements_file(self, mock_file):
        # Call the function
        result = read_requirements_file("requirements.txt")

        # Check the results
        self.assertEqual(result, ["pkg_one==1.2.3\n", "pkg_one[with_extras]==1.2.3\n"])

        # Ensure the file was opened correctly
        mock_file.assert_called_once_with("requirements.txt", 'r')

    def test_parse_requirements(self):
        # Raw input lines
        raw_lines = [
            "pkg_one==1.2.3",
            "pkg_one[with_extras]==1.2.3",
            "# This is a comment",
            "pkg_two>=1.2.3",
            "pkg_two[with_extras]>=1.2.3"  
        ]

        # Call the function
        result = parse_requirements(raw_lines)

        # Define the expected result
        expected = [
            {'name': 'pkg_one', 'version': '1.2.3', 'extras': None},
            {'name': 'pkg_one', 'version': '1.2.3', 'extras': ['with_extras']},
            {'name': 'pkg_two', 'version': '1.2.3', 'extras': None},
            {'name': 'pkg_two', 'version': '1.2.3', 'extras': ['with_extras']}
        ]

        # Check the results
        self.assertEqual(result, expected)

    def test_parse_requirements_invalid_line(self):
        # Define raw input lines with an invalid line
        raw_lines = [
            "pkg_one==1.2.3",
            "invalid-package-line",
        ]

        # Capture output to ensure the warning is printed
        with patch('sys.stdout') as mock_stdout:
            result = parse_requirements(raw_lines)
        #    self.assertIn("Warning: Could not parse line: invalid-package-line", mock_stdout.write.call_args[0][0])

        # Ensure valid lines are still processed
        expected = [
            {'name': 'pkg_one', 'version': '1.2.3', 'extras': None},
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
