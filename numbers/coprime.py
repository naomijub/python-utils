import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_if_0_and_0_are_coprime(self):
        assert self.coprime.isCoprime(0, 0) == false

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
