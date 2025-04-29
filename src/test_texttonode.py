import unittest
from textToNode import *
from textnode import *


class TestTextToNode(unittest.TestCase):
    def test_text_to_node(self):
        
        result = text_to_textnodes('This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')
        self.assertTrue(TextNode('This is ', TextType.TEXT) in result)
        self.assertTrue(TextNode(' word and a ', TextType.TEXT) in result)
        self.assertTrue(TextNode('code block', TextType.CODE) in result)
        self.assertTrue(TextNode('obi wan image', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg') in result)
        self.assertTrue(TextNode(' and a ', TextType.TEXT) in result)

if __name__ == "__main__":
    unittest.main()