from operation import Operation
import unittest

class TestOperation(unittest.TestCase):
    def setUp(self):
        self.operation = Operation(price=1.2345, type_of_operation="buy", stop_loss=1.15, stop_gain=1.35, pip_value=0.0001, lot_size=10000, leverage=10)

    def test_stop_loss(self):
        self.operation.stop_loss()
        self.assertAlmostEqual(self.operation.stop_loss, 1.19845, places=4)

    def test_stop_gain(self):
        self.operation.stop_gain()
        self.assertAlmostEqual(self.operation.stop_gain, 1.3503, places=4)

    def test_reached_stop_gain(self):
        actual_price = 1.3503
        result = self.operation.reached_stop_gain(actual_price)
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    unittest.main()