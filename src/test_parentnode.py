import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class ParentTestNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(tag="p", children=[LeafNode("b", "Bold Text")])
        self.assertEqual(node.to_html(), "<p><b>Bold Text</b></p>")

    def test_nested_parents(self):
        node = ParentNode(tag="p", 
                          children=[
                              ParentNode(
                                  tag="h1", 
                                  props={"test":"testval", "test2":"test2val"},
                                  children=[
                                      LeafNode("p", "Paragraph", {"testProp":"testVal"})
                                  ]
                              )
                          ]
                )
        self.assertEqual(node.to_html(), '<p><h1 test="testval" test2="test2val"><p testProp="testVal">Paragraph</p></h1></p>')


if __name__ == "__main__":
    unittest.main()
