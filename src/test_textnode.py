import unittest

from textnode import TextNode
from textnode import split_nodes_delimiter

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

    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", "text_type_text")
        new_nodes = split_nodes_delimiter([node], "`", "text_type_code")
        self.assertEqual(new_nodes, [TextNode("This is text with a ", "text_type_text"),TextNode("code block", "text_type_code"),TextNode(" word", "text_type_text"),])

if __name__ == "__main__":
    unittest.main()
