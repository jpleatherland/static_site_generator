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

    def split_nodes_delimiters(old_nodes, delimiter, text_type):
        split_nodes = old_nodes.split(delimiter)
        match text_type:
            case "text_type_bold":

        pass
