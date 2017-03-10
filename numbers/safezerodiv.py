import unittest

def sdiv(num, div, as_inf):
    try:
        return num / div
    except ZeroDivisionError:
        if as_inf:
            return float('inf')
        else:
            raise

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_if_3_sdiv_2_is_1(self):
        assert sdiv(3,2, False) == 1.5

    def test_if_5_sdiv_2_is_1(self):
        assert sdiv(5,2, True) == 2.5

    def test_if_3_sdiv_0_is_inf(self):
        with self.assertRaises(ZeroDivisionError):
            assert sdiv(3,0, False)

    def test_if_return_inf_for_zerodivisionerror(self):
        assert sdiv(3,0, True) == float('inf')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
