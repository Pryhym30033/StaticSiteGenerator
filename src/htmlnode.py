

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        keys = self.props.keys()
        props = ''
        for key in keys:
             props = props+f" {key}=\"{self.props[key]}\""
        return props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children},{self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if value is None:
            raise ValueError
        else:
            self.value = value

    def to_html(self):
    
        if self.tag is None:
            return f"{self.value}"
        else:
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                htmlProp = self.props_to_html()
                return f"<{self.tag}{htmlProp}>{self.value}</{self.tag}>" 
        
    