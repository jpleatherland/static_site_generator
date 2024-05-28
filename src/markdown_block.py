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


def heading_to_html_node(block_type, block_content):
    block_content.strip()
    text_nodes = text_to_textnodes(block_content)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return ParentNode(block_type, children=children)


def code_to_html_node(block_content):
    block_content = block_content.strip()
    text_nodes = text_to_textnodes(block_content)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    code = ParentNode(tag="code", children=children)
    return ParentNode(tag="pre", children=[code])


def paragraph_to_html_node(block_content):
    block_content.strip()
    block_content = block_content.replace("\n", " ")
    text_nodes = text_to_textnodes(block_content)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return ParentNode("p", children=children)


def quote_to_html_node(block_content):
    block_content.strip()
    lines = block_content.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip("> "))
    content = " ".join(new_lines)
    text_nodes = text_to_textnodes(content)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return ParentNode("blockquote", children=children)


def ol_to_html_node(block_content):
    block_content.strip()
    lines = block_content.split("\n")
    children = []
    for line in lines:
        line = line[3:]
        text_nodes = text_to_textnodes(line)
        li_children = []
        for text_node in text_nodes:
            li_children.append(text_node_to_html_node(text_node))
        children.append(ParentNode("li", children=li_children))
    return ParentNode("ol", children=children)


def ul_to_html_node(block_content):
    block_content.strip()
    lines = block_content.split("\n")
    children = []
    for line in lines:
        line = line[2:]
        text_nodes = text_to_textnodes(line)
        li_children = []
        for text_node in text_nodes:
            li_children.append(text_node_to_html_node(text_node))
        children.append(ParentNode("li", children=li_children))
    return ParentNode("ul", children=children)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_content = block
        block_content = block_content.lstrip("\n")
        block_content = block_content.rstrip("\n")
        if block_type == block_types['block_type_h1']:
            block_content = block_content[2:]
            node = heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h2']:
            block_content = block_content[3:]
            node = heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h3']:
            block_content = block_content[4:]
            node = heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h4']:
            block_content = block_content[5:]
            node = heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h5']:
            block_content = block_content[6:]
            node = heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_h6']:
            block_content = block_content[7:]
            node = heading_to_html_node(block_type, block_content)
        elif block_type == block_types['block_type_code']:
            block_content = block_content[3:-3]
            node = code_to_html_node(block_content)
        elif block_type == block_types['block_type_quote']:
            block_content = block_content[2:]
            node = quote_to_html_node(block_content)
        elif block_type == block_types['block_type_ul']:
            node = ul_to_html_node(block_content)
        elif block_type == block_types['block_type_ol']:
            node = ol_to_html_node(block_content)
        elif block_type == block_types['block_type_paragraph']:
            node = paragraph_to_html_node(block_content)
        children.append(node.to_html())

    return ''.join(children)

#    return ParentNode("div", children=children)
