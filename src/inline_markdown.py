from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     result_nodes = []
#     for node in old_nodes:
#         current_text_string = '' 
#         for char in node.text:
#             if (char == delimiter):
#                 if(current_text_string.startswith(delimiter)):
#                     result_nodes.append(TextNode(current_text_string[1:], text_type))
#                     current_text_string = ''
#                     continue
#                 else:
#                     result_nodes.append(TextNode(current_text_string, text_type_text))
#                     current_text_string = char
#             else:
#                current_text_string = ''.join([current_text_string,char])
#         result_nodes.append(TextNode(current_text_string, text_type_text))
#     return result_nodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
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