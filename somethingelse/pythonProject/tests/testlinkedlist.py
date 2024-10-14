import unittest

from pythonProject.classwork.linkedlist import LinkedList


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)
        self.list.append(50)
        self.assertEqual(4, self.list.size())

    def test_append(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)
        self.list.append(50)
        self.list.append(60)
        self.list.append(70)
        self.list.append(80)
        self.assertEqual(7, self.list.size())

    def test_print_list(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)
        self.list.append(50)
        self.list.append(60)
        self.list.print_list()

    def test_prepend(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)
        self.list.append(50)
        self.list.prepend(100)
        self.assertEqual(5, self.list.size())

    def test_delete(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)
        self.list.append(50)
        self.list.delete(1)
        self.assertEqual(4, self.list.size())

    def test_pop(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(20)
        self.list.append(30)
        self.list.append(40)
        self.list.append(50)
        self.list.append(60)
        popped = self.list.pop()
        self.assertEqual(4, self.list.size())
        self.assertEqual(60, popped)

    def test_reverse(self):






if __name__ == '__main__':
    unittest.main()
