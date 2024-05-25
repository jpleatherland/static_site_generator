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
        self.assertEqual(node.to_html(), '<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>')
    
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

if __name__ == "__main__":
    unittest.main()
