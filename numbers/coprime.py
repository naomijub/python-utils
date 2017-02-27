import unittest

class Coprime:
    def __init__(self):
        pass

    def isCoprime(self, a, b):
        if a == 0 or b == 0 or a == 1 or b == 1:
            return False
        else:
            return True

class Test(unittest.TestCase):
    def setUp(self):
        self.cop = Coprime()

    def tearDown(self):
        pass

    def test_if_0_and_0_are_coprime(self):
        assert self.cop.isCoprime(0,0) == False

    def test_if_1_and_0_are_coprime(self):
        assert self.cop.isCoprime(1,0) == False

    def test_if_2_and_3_are_coprime(self):
        assert self.cop.isCoprime(2,3) == True

    def test_if_2_and_8_are_coprime(self):
        assert self.cop.isCoprime(2,8) == False

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
