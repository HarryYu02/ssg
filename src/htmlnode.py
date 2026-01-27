class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Error: not implemented")

    def props_html(self):
        attrs = ""
        for attr in self.props:
            attrs += f' {attr}="{self.props[attr]}"'
        return attrs

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
