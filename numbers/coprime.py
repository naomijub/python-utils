import unittest

class Coprime:
    def __init__(self):
        pass

    def isCoprime(self, a, b):
        return False

class Test(unittest.TestCase):
    def setUp(self):
        self.cop = Coprime()

    def tearDown(self):
        pass

    def test_if_0_and_0_are_coprime(self):
        assert self.cop.isCoprime(0,0) == False

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
