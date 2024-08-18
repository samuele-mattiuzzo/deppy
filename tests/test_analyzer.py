import unittest
from deppy.analyzer import analyze_dependencies

class TestAnalyzer(unittest.TestCase):
    def test_analyze_dependencies_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            analyze_dependencies("path/to/requirements.txt")

if __name__ == '__main__':
    unittest.main()
