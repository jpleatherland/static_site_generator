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
        expected = ["This is the first block.",
                    "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    def test_markdown_to_blocks_with_empty_lines(self):
        markdown = "This is the first block.\n\n\nThis is the second block.\n\n\n\nThis is the third block."
        expected = ["This is the first block.",
                    "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    def test_markdown_to_blocks_with_whitespace(self):
        markdown = "   This is the first block.   \n\n   This is the second block.   \n\n   This is the third block.   "
        expected = ["This is the first block.",
                    "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    def test_markdown_to_blocks_with_blank_lines(self):
        markdown = "This is the first block.\n\n\n\nThis is the second block.\n\n\n\n\n\nThis is the third block."
        expected = ["This is the first block.",
                    "This is the second block.", "This is the third block."]
        result = markdown_to_blocks(markdown)
        self.assertListEqual(expected, result)

    def test_markdown_to_blocks_with_single_new_lines(self):
        markdown = "This is the first line.\nThis is the second line.\nThis is the third line."
        expected = [
            "This is the first line.\nThis is the second line.\nThis is the third line."]
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


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block),
                         block_types['block_type_h1'])
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block),
                         block_types['block_type_code'])
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block),
                         block_types['block_type_quote'])
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block),
                         block_types['block_type_ul'])
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block),
                         block_types['block_type_ol'])
        block = "paragraph"
        self.assertEqual(block_to_block_type(block),
                         block_types['block_type_paragraph'])

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
