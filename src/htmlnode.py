class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_string = list(map(lambda x: f'{x[0]}="{x[1]}"', self.props.items()))
        return " ".join(props_string)
    
    def text_node_to_html_node(text_node):
        match text_node['text_type']:
            case "text_type_text":
                pass
            case "text_type_bold":
                pass
            case "text_type_italic":
                pass
            case "text_type_code":
                pass
            case "text_type_link":
                pass
            case "text_type_image":
                pass
            case _:
                raise Exception('invalid text_type')

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
