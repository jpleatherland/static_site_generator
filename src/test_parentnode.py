from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if(not self.tag):
            raise ValueError('No tag provided')
        if(not self.children):
            raise ValueError('No children provided')
        pass
