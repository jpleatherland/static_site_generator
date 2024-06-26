import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "**test** This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("test", text_type_bold),
                TextNode(" This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode(
            "This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        result = split_nodes_image([node])
        self.assertListEqual(expected, result)

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "This is text with multiple images: ![image1](https://example.com/image1.png) and ![image2](https://example.com/image2.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with multiple images: ", text_type_text),
            TextNode("image1", text_type_image,
                     "https://example.com/image1.png"),
            TextNode(" and ", text_type_text),
            TextNode("image2", text_type_image,
                     "https://example.com/image2.png")
        ]
        result = split_nodes_image([node])
        self.assertListEqual(expected, result)

    def test_split_nodes_image_no_text(self):
        node = TextNode(
            "![](https://example.com/image.png)",
            text_type_text,
        )
        expected = [
            TextNode("", text_type_image, "https://example.com/image.png")
        ]
        result = split_nodes_image([node])
        self.assertListEqual(expected, result)

    def test_split_nodes_image_no_image(self):
        node = TextNode(
            "This is text without an image",
            text_type_text,
        )
        expected = [
            TextNode("This is text without an image", text_type_text)
        ]
        result = split_nodes_image([node])
        self.assertListEqual(expected, result)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example2.com)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://example.com"),
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://example2.com")
        ]
        result = split_nodes_link([node])
        self.assertListEqual(expected, result)

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "This is text with multiple links: [link1](https://example.com) and [link2](https://example2.com)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with multiple links: ", text_type_text),
            TextNode("link1", text_type_link, "https://example.com"),
            TextNode(" and ", text_type_text),
            TextNode("link2", text_type_link, "https://example2.com")
        ]
        result = split_nodes_link([node])
        self.assertListEqual(expected, result)

    def test_split_nodes_link_no_text(self):
        node = TextNode(
            "[](https://example.com)",
            text_type_text,
        )
        expected = [
            TextNode("", text_type_link, "https://example.com")
        ]
        result = split_nodes_link([node])
        self.assertListEqual(expected, result)

    def test_split_nodes_link_no_link(self):
        node = TextNode(
            "This is text without a link",
            text_type_text,
        )
        expected = [
            TextNode("This is text without a link", text_type_text)
        ]
        result = split_nodes_link([node])
        self.assertListEqual(expected, result)

    def test_text_to_textnodes_no_delimiters(self):
        text = "This is plain text without any delimiters"
        expected = [
            TextNode("This is plain text without any delimiters", text_type_text)
        ]
        result = text_to_textnodes(text)
        self.assertListEqual(expected, result)

    def test_text_to_textnodes_multiple_delimiters(self):
        text = "This is text with **multiple** *delimiters* and `code`"
        expected = [
            TextNode("This is text with ", text_type_text),
            TextNode("multiple", text_type_bold),
            TextNode(" ", text_type_text),
            TextNode("delimiters", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("code", text_type_code)
        ]
        result = text_to_textnodes(text)
        self.assertListEqual(expected, result)

    def test_text_to_textnodes_with_images_and_links(self):
        text = "This is text with an ![image](https://example.com/image.png) and a [link](https://example.com)"
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image,
                     "https://example.com/image.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://example.com")
        ]
        result = text_to_textnodes(text)
        self.assertListEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
