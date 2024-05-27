import unittest

from markdown_block import (
    markdown_to_blocks,
    block_types,
    block_to_block_type,
    markdown_to_html_node
)

from parentnode import ParentNode
from leafnode import LeafNode

class TestExtractMethods(unittest.TestCase):

    # Test markdown_to_blocks
    def test_markdown_to_blocks(self):
        markdown = "This is the first block.\n\nThis is the second block.\n\nThis is the third block."
        expected = ["This is the first block.", "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    def test_markdown_to_blocks_with_empty_lines(self):
        markdown = "This is the first block.\n\n\nThis is the second block.\n\n\n\nThis is the third block."
        expected = ["This is the first block.", "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    def test_markdown_to_blocks_with_whitespace(self):
        markdown = "   This is the first block.   \n\n   This is the second block.   \n\n   This is the third block.   "
        expected = ["This is the first block.", "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    def test_markdown_to_blocks_with_blank_lines(self):
        markdown = "This is the first block.\n\n\n\nThis is the second block.\n\n\n\n\n\nThis is the third block."
        expected = ["This is the first block.", "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)
    
    def test_markdown_to_blocks_with_single_new_lines(self):
        markdown = "This is the first line.\nThis is the second line.\nThis is the third line."
        expected = ["This is the first line.\nThis is the second line.\nThis is the third line."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    # Test block_to_block_type
    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph."
        expected = block_types["block_type_paragraph"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_h1(self):
        block = "# Heading 1"
        expected = block_types["block_type_h1"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_h2(self):
        block = "## Heading 2"
        expected = block_types["block_type_h2"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_h3(self):
        block = "### Heading 3"
        expected = block_types["block_type_h3"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_h4(self):
        block = "#### Heading 4"
        expected = block_types["block_type_h4"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_h5(self):
        block = "##### Heading 5"
        expected = block_types["block_type_h5"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_h6(self):
        block = "###### Heading 6"
        expected = block_types["block_type_h6"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello, World!')\n```"
        expected = block_types["block_type_code"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote."
        expected = block_types["block_type_quote"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_ul(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        expected = block_types["block_type_ul"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_type_ul_with_asterisk(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        expected = block_types["block_type_ul"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_block_to_block_type_ol(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        expected = block_types["block_type_ol"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
        
    def test_block_to_block_type_interrupted_ol(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3\nThis isn't an ordered list item.\n4. Item 4"
        expected = block_types["block_type_paragraph"]
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    # Test markdown_to_html_node
    def test_markdown_to_html_node_with_paragraph(self):
        markdown = "This is a paragraph."
        expected = ParentNode(tag="div", children=[LeafNode("paragraph", "This is a paragraph.")])
        result = markdown_to_html_node(markdown)
        self.assertEqual(expected, result)

    def test_markdown_to_html_node_with_headings(self):
        markdown = "# Heading 1\n\n## Heading 2\n\n### Heading 3"
        expected = ParentNode("div", children=[
            LeafNode("h1", "Heading 1"),
            LeafNode("h2", "Heading 2"),
            LeafNode("h3", "Heading 3")
        ])
        result = markdown_to_html_node(markdown)
        self.assertEqual(expected, result)

    def test_markdown_to_html_node_with_code_block(self):
        markdown = "```python\nprint('Hello, World!')\n```"
        expected = ParentNode("div", children=[
            LeafNode("code", "print('Hello, World!')")
        ])
        result = markdown_to_html_node(markdown)
        self.assertEqual(expected, result)

    def test_markdown_to_html_node_with_quote(self):
        markdown = "> This is a quote."
        expected = ParentNode("div", children=[
            LeafNode("quote", "This is a quote.")
        ])
        result = markdown_to_html_node(markdown)
        self.assertEqual(expected, result)

    def test_markdown_to_html_node_with_unordered_list(self):
        markdown = "- Item 1\n- Item 2\n- Item 3"
        expected = ParentNode("div", children=[
            LeafNode("unordered_list", "Item 1"),
            LeafNode("unordered_list", "Item 2"),
            LeafNode("unordered_list", "Item 3")
        ])
        result = markdown_to_html_node(markdown)
        self.assertEqual(expected, result)

    def test_markdown_to_html_node_with_ordered_list(self):
        markdown = "1. Item 1\n2. Item 2\n3. Item 3"
        expected = ParentNode("div", children=[
            LeafNode("ordered_list", "Item 1"),
            LeafNode("ordered_list", "Item 2"),
            LeafNode("ordered_list", "Item 3")
        ])
        result = markdown_to_html_node(markdown)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
