import os
import unittest

from hyo2.abc.lib.helper import Helper
from hyo2.abc.lib.lib_info import LibInfo


class TestABCLibHelper(unittest.TestCase):

    def setUp(self):

        self.h = Helper(lib_info=LibInfo())

    @unittest.skipIf(Helper.is_linux(), "test not supported on Linux")
    def test_explore_folder(self):
        self.assertTrue(self.h.explore_folder(__file__))
        self.assertFalse(self.h.explore_folder(__file__ + ".fake"))
        self.assertTrue(self.h.explore_folder(os.path.dirname(__file__)))
        self.assertFalse(self.h.explore_folder(os.path.dirname(__file__) + "fake"))

    def test_is_64bit_os(self):
        self.assertIsInstance(self.h.is_64bit_os(), bool)

    def test_is_64bit_python(self):
        self.assertIsInstance(self.h.is_64bit_python(), bool)

    def test_is_darwin_linux_windows(self):
        self.assertIsInstance(self.h.is_darwin(), bool)
        self.assertIsInstance(self.h.is_linux(), bool)
        self.assertIsInstance(self.h.is_windows(), bool)

        self.assertTrue(any([self.h.is_linux(), self.h.is_darwin(), self.h.is_windows()]))

    def test_is_pydro(self):
        self.assertIsInstance(self.h.is_pydro(), bool)

    def test_is_url(self):
        self.assertTrue(self.h.is_url("https://www.hydroffice.org"))
        self.assertFalse(self.h.is_url("http://fake/url"))

    def test_python_path(self):
        self.assertTrue(os.path.exists(self.h.python_path()))

    def test_package_info(self):
        self.assertIsInstance(self.h.package_info(qt_html=True), str)
        self.assertIsInstance(self.h.package_info(qt_html=False), str)

    def test_package_folder(self):
        self.assertTrue(os.path.exists(self.h.package_folder()))


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibHelper))
    return s
