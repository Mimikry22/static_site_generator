
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props 

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html_str = ""
        for prop in self.props:
            html_str += f' {prop}="{self.props[prop]}"'
        return html_str

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if(self.value==None):
            raise ValueError("All leaf nodes must have a value")
        if(self.tag == None):
            return self.value
        html_str = ""
        if(self.props==None):
            html_str = f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            html_str = f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return html_str
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
