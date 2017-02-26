import unittest

class Converter:
    def __init__(self):
        pass

    def convert(self, strbt):
        if isinstance(strbt, str):
            return strbt.encode('utf-8')
        elif isinstance(strbt, bytes):
            return strbt.decode('utf-8')
        else:
            raise TypeError


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

    def test_5cars_bytes_return_empty_str(self):
        assert self.conv.convert(b'5cars') == "5cars"

    def test_number_raises_exception(self):
        with self.assertRaises(TypeError):
            self.conv.convert(1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
