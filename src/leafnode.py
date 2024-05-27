from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        tag_prop = self.tag
        if (not self.value):
            raise ValueError('A leaf requires a value')
        if (self.props):
            tag_prop += f" {self.props_to_html()}"
        return f"<{tag_prop}>{self.value}</{self.tag}>"
