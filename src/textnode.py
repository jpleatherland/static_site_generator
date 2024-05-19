class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        return (self.text == other_node.text 
                and self.text_type == other_node.text_type 
                and self.url == other_node.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_nodes = []
    for node in old_nodes:
        current_text_string = '' 
        for char in node.text:
            print(current_text_string)
            if (char == delimiter):
                if(current_text_string.startswith(delimiter)):
                    result_nodes.append(TextNode(current_text_string[1:], text_type))
                    current_text_string = ''
                    continue
                else:
                    result_nodes.append(TextNode(current_text_string, 'text_type_text'))
                    current_text_string = char
            else:
                ''.join([current_text_string,char])
    return result_nodes
