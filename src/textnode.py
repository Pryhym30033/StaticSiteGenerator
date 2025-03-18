from enum import Enum
from htmlnode import *

class TextType(Enum):
        TEXT = "text"
        BOLD = "bold"
        ITALIC = "italic"
        CODE = "code"
        LINK = "link"
        IMAGE = "image"

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if other == None:
             return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url  

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

    def text_node_to_html_node(self):
        if self.text_type not in TextType:
            raise ValueError("Not a TextNode")
        elif self.text_type == TextType.TEXT:
             textLeaf = LeafNode(None, self.text)
             return textLeaf
        elif self.text_type ==TextType.BOLD:
             boldLeaf = LeafNode("b", self.text)
             return boldLeaf
        elif self.text_type == TextType.ITALIC:
             italicLeaf = LeafNode("i", self.text)
             return italicLeaf
        elif self.text_type == TextType.CODE:
             codeLeaf = LeafNode("code", self.text)
             return codeLeaf
        elif self.text_type == TextType.LINK:
             linkLeaf = LeafNode("a", self.text, "href")
             return linkLeaf
        elif self.text_type == TextType.IMAGE:
             imageLeaf = LeafNode("img", "", ["src", "alt"])
             return imageLeaf
 