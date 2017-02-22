import unittest

class Converter:
    def __init__(self):
        pass

    def convert(self, strg):
        return strg.encode('utf-8')

class Test(unittest.TestCase):
    def setUp(self):
        self.conv = Converter()

    def tearDown(self):
        pass

    def test_empty_str_return_empty_bytes(self):
        assert self.conv.convert(" ") == b' '

    def test_car_str_return_bytes(self):
        assert self.conv.convert("car") == b'car'

    def test_empty_bytes_return_empty_str(self):
        assert self.conv.convert(b' ') == " "

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
