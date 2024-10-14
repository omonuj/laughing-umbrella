import unittest

from pythonProject.classwork.queue import Queue


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()


    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.queue.enqueue(50)
        self.assertEqual(4, self.queue.size())
        self.assertFalse(self.queue.is_empty())

    def test_enqueue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.queue.enqueue(50)
        self.queue.enqueue(60)
        self.queue.enqueue(70)
        self.assertEqual(6, self.queue.size())

    def test_dequeue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.queue.enqueue(50)
        self.queue.enqueue(60)
        self.queue.enqueue(70)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(4, self.queue.size())

    def test_peek(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.queue.enqueue(50)
        self.queue.enqueue(60)
        peeked = self.queue.peek()
        self.assertEqual(20, peeked)

    def test_size(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.queue.enqueue(50)
        self.queue.enqueue(60)
        self.assertEqual(5, self.queue.size())

    def test_print_queue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.queue.enqueue(50)
        self.queue.enqueue(60)
        self.queue.print_queue()




if __name__ == '__main__':
    unittest.main()
