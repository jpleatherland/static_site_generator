from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_types = {
    "block_type_paragraph": "paragraph",
    "block_type_h1": "h1",
    "block_type_h2": "h2",
    "block_type_h3": "h3",
    "block_type_h4": "h4",
    "block_type_h5": "h5",
    "block_type_h6": "h6",
    "block_type_code": "code",
    "block_type_quote": "quote",
    "block_type_ul": "unordered_list",
    "block_type_ol": "ordered_list"
}


def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split("\n\n"):
        line = line.strip()
        if len(line) > 0:
            blocks.append(line)
    return blocks


def block_to_block_type(block):
    if block.startswith("# "):
        return block_types['block_type_h1']
    if block.startswith("## "):
        return block_types['block_type_h2']
    if block.startswith("### "):
        return block_types['block_type_h3']
    if block.startswith("#### "):
        return block_types['block_type_h4']
    if block.startswith("##### "):
        return block_types['block_type_h5']
    if block.startswith("###### "):
        return block_types['block_type_h6']
    if block.startswith("```") and block.endswith("```"):
        return block_types['block_type_code']
    if block.startswith("> "):
        return block_types['block_type_quote']
    if block.startswith("- ") or block.startswith("* "):
        return block_types['block_type_ul']
    if block.startswith("1. "):
        for i in range(0, len(block.split("\n"))):
            if not block.split("\n")[i].strip().startswith(f"{i+1}."):
                return block_types['block_type_paragraph']
        return block_types['block_type_ol']
    return block_types['block_type_paragraph']


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_content = block
        if block_type == block_types['block_type_h1']:
            block_content = block_content[2:]
            heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h2']:
            block_content = block_content[3:]
            heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h3']:
            block_content = block_content[4:]
            heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h4']:
            block_content = block_content[5:]
            heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h5']:
            block_content = block_content[6:]
            heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h6']:
            block_content = block_content[7:]
            heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_code']:
            block_content = block_content[3:-3]
        elif block_type == block_types['block_type_quote']:
            block_content = block_content[2:""" """  """ """]
        elif block_type == block_types['block_type_ul']:
            block_content = block_content[2:]
        elif block_type == block_types['block_type_ol']:
            block_content = block_content[3:]

    return ParentNode("div", children=children)
