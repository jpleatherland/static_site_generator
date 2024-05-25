from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

from extract_methods import (
    extract_markdown_images,
    extract_markdown_links
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if len(node.text) == 0:
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0 and len(node.text) > 0:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for i in range(0,len(images)):
            parts = remaining_text.split(f"![{images[i][0]}]({images[i][1]})")
            if len(parts[0]) > 0:
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(images[i][0], text_type_image, images[i][1]))
            if len(parts) > 1:
                remaining_text = parts[1]
        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, text_type_text))
    return new_nodes