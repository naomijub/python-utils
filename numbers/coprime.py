import unittest

class Coprime:
    def __init__(self):
        pass

    def isCoprime(self, a, b):
        if a == 0 or b == 0 or a == 1 or b == 1:
            return False
        else:
            for i in range(2, min(a,b) + 1):
                if a % i == 0 and b % i == 0:
                    return False
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

    def test_if_4_and_9_are_coprime(self):
        assert self.cop.isCoprime(4, 9) == True

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
