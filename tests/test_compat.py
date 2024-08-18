import unittest
from deppy.compat import check_compatibility

class TestCompatibility(unittest.TestCase):
    def test_check_compatibility_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            check_compatibility([], "3.8")  # Pass an empty list and Python version for now

if __name__ == '__main__':
    unittest.main()
