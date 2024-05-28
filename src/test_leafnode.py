import unittest

from leafnode import LeafNode


class LeafTestNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_result = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_result)

    def missing_value(self):
        node = LeafNode("p")
        expected_result = ValueError('A leaf requires a value')
        self.assertEqual(node.to_html(), expected_result)


if __name__ == "__main__":
    unittest.main()
