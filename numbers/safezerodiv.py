import unittest

def sdiv(num, div):
    return num / div

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_if_3_sdiv_2_is_1(self):
        assert sdiv(3,2) == 1.5

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
