from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if (not self.tag):
            raise ValueError('No tag provided')
        if (not self.children):
            raise ValueError('No children provided')

        tag_prop = self.tag
        if (self.props):
            tag_prop += f" {self.props_to_html()}"
        return f"<{tag_prop}>{self.__children_to_html__()}</{self.tag}>"

    def __children_to_html__(self):
        children_string = list(map(lambda x: x.to_html(), self.children))
        return ''.join(children_string)
