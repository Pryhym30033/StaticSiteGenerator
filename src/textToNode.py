from delimiter import *
from imgLinkSplit import *
from textnode import *

def text_to_textnodes(text):
    
    textNode = [TextNode(text, TextType.TEXT)]
    imageNodes = split_nodes_image(textNode)
    linkNodes = split_nodes_link(imageNodes)
    bold = split_nodes_delimiter(linkNodes, '**', TextType.BOLD)
    italic = split_nodes_delimiter(bold, '_', TextType.ITALIC)
    code = split_nodes_delimiter(italic, '`', TextType.CODE)


    return code
    



