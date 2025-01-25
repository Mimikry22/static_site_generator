
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_str = ""
        for prop in self.props:
            html_str += f' {prop}="{self.props[prop]}"'
        return html_str