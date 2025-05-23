
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props = ''
        for key in self.props:
             props = props+f" {key}=\"{self.props[key]}\""
        return props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children},{self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
       

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" 
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None: 
            raise ValueError("Tag is required for ParentNode")
        if self.children is None or len(self.children)<1:
            raise ValueError("Children are required for ParentNode")
        childrenHTML = ""
        for child in self.children:
            childrenHTML += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{childrenHTML}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


