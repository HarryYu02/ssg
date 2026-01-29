from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Error: parent node have no tag")
        if self.children == None:
            raise ValueError("Error: parent node have no children")

        children_str = ""
        for child in self.children:
            children_str += child.to_html()
        return f"<{self.tag}{self.props_html()}>{children_str}</{self.tag}>"
