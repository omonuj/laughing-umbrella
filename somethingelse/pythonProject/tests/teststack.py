import unittest

from pythonProject.classwork import stack
from pythonProject.classwork.stack import Stack


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(3)


    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.append(10)
        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.append(5)
        self.stack.append(4)
        self.stack.append(67)
        self.assertEqual(3, self.stack.size())
        self.assertEqual(67, self.stack.pop())

    def test_peek(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.append(5)
        self.assertEqual(5, self.stack.peek())
        self.stack.append(4)
        self.assertEqual(4, self.stack.peek())

    def test_pop(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.append(5)
        self.stack.append(100)
        popped = self.stack.pop()
        self.assertEqual(100, popped)

    def test_is_full(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.append(5)
        self.stack.append(100)
        self.stack.append(200)
        self.assertTrue(self.stack.is_full())
        with self.assertRaises(Exception):
            self.stack.append(1000)

    def test_search(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.append(5)
        self.stack.append(100)
        self.stack.append(200)
        self.assertEqual(2, self.stack.search(200))

    # def test_search_not_found(self):
    #     self.assertFalse(self.stack.is_empty())
    #     self.stack.append(5)
    #     self.stack.append(100)
    #     self.stack.append(200)
    #     self.assertEqual(-1, self.stack.search(1))




if __name__ == '__main__':
    unittest.main()
