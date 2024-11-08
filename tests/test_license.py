import unittest
from deppy.license import check_license_compliance


class TestLicense(unittest.TestCase):
    def test_check_license_compliance_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            check_license_compliance([])  # Pass an empty list of dependencies for now


if __name__ == '__main__':
    unittest.main()
