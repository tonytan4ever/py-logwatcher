import os
import unittest

from logwatcher import log_file_watcher


class Test(unittest.TestCase):

    def make_test_dir(self):
        pass

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.make_test_dir()
        test_log_file_watcher_object = log_file_watcher.LogWatcher(

        )


    def testName(self):
        pass


    def tearDown(self):


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()