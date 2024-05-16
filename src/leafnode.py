from htmlnode import HTMLNode 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)

    def to_html(self):
        if (!self.value):
            raise ValueError('A leaf requires a value')
        return self.props_to_html()

