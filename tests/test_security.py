import unittest
from deppy.security import check_security


class TestSecurity(unittest.TestCase):
    def test_check_security_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            check_security([])


if __name__ == '__main__':
    unittest.main()
