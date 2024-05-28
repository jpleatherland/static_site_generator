import unittest

from htmlnode import HTMLNode


class HTMLTestNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "", "", "", {"href": "https://www.google.com", "target": "_blank"})
        stringNode = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), stringNode)

    def test_props_to_html2(self):
        node = HTMLNode(props={"test": "another test",
                        "another_prop": "prop the second"})
        stringNode = 'test="another test" another_prop="prop the second"'
        self.assertEqual(node.props_to_html(), stringNode)


if __name__ == "__main__":
    unittest.main()
