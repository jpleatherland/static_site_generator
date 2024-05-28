from htmlnode import HTMLNode
import re

self_closing_tags = [
    "img",
    "br",
    "input",
    "hr"
]


class LeafNode(HTMLNode):
    ATTRIBUTE_REGEX = re.compile(r'^[a-zA-Z_:][-a-zA-Z0-9_:.]*$')

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value

        if self.tag in self_closing_tags:
            return self.self_closing_to_html()

        tag_prop = self.tag

        if (not self.value):
            raise ValueError('A leaf requires a value')
        if (self.props):
            tag_prop += f" {self.props_to_html()}"
        return f"<{tag_prop}>{self.value}</{self.tag}>"

    def self_closing_to_html(self):
        tag_prop = self.tag
        if (self.props):
            if not self.validate_props():
                raise ValueError("Invalid attributes found in properties")
            tag_prop += f" {self.props_to_html()}"
        return f"<{tag_prop} />"

    def validate_props(self):
        for key in self.props.keys():
            if not self.ATTRIBUTE_REGEX.match(key):
                return False
        return True
