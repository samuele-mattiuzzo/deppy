import unittest
from deppy.report import generate_report


class TestReport(unittest.TestCase):
    def test_generate_report_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            generate_report("output/path/report.html")


if __name__ == '__main__':
    unittest.main()
