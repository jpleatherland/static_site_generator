import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node")
        self.assertNotEqual(node, node2)

    def test_print(self):
        node = TextNode("This is a text node", "italic", "www.test.io")
        self.assertEqual(repr(node), "TextNode(This is a text node, italic, www.test.io)")

if __name__ == "__main__":
    unittest.main()
