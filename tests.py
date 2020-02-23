import unittest
import classroom_manager

class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, classroom_manager.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, classroom_manager.firstrun())

if __name__ == '__main__':
    unittest.main()
	