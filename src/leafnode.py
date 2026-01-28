from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Error: leaf node have no value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"Leaf Node:\nTag: {self.tag}\nValue: {self.value}\nProps: {self.props}"
