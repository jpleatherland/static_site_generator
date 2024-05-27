import unittest

from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode


class ParentTestNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(tag="p", children=[LeafNode("b", "Bold Text")])
        self.assertEqual(node.to_html(), "<p><b>Bold Text</b></p>")

    def test_nested_parents(self):
        node = ParentNode(tag="p",
                          children=[
                              ParentNode(
                                  tag="h1",
                                  props={"test": "testval",
                                         "test2": "test2val"},
                                  children=[
                                      LeafNode("p", "Paragraph", {
                                               "testProp": "testVal"})
                                  ]
                              )
                          ]
                          )
        self.assertEqual(node.to_html(
        ), '<p><h1 test="testval" test2="test2val"><p testProp="testVal">Paragraph</p></h1></p>')

    def test_empty_parent(self):
        node = ParentNode(tag="div", children=[])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("No children provided" in str(context.exception))

    def test_multiple_children(self):
        node = ParentNode(tag="ul",
                          children=[
                              LeafNode("li", "Item 1"),
                              LeafNode("li", "Item 2"),
                              LeafNode("li", "Item 3")
                          ]
                          )
        self.assertEqual(
            node.to_html(), '<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>')

    def test_nested_empty_parents(self):
        node = ParentNode(tag="div",
                          children=[
                              ParentNode(tag="span", children=[]),
                              ParentNode(tag="div", children=[
                                  ParentNode(tag="p", children=[])
                              ])
                          ]
                          )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("No children provided" in str(context.exception))

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            'class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
