import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_delimiter(self):
        testTextNode = [TextNode("This is **bold** text", TextType.TEXT), TextNode("Bold Node", TextType.BOLD)]
        testDelimiter = split_nodes_delimiter(testTextNode, "**", TextType.BOLD)
        changeNode = [TextNode("This is a changed /Node/ text", TextType.TEXT)]
        changeDelimiter = split_nodes_delimiter(changeNode, "/", TextType.ITALIC)
        self.assertEqual(f"{testDelimiter}", "[TextNode(This is , text, None), TextNode(bold, bold, None), TextNode( text, text, None), TextNode(Bold Node, bold, None)]")
        self.assertEqual(f"{changeDelimiter}", "[TextNode(This is a changed , text, None), TextNode(Node, italic, None), TextNode( text, text, None)]")
        with self.assertRaises(Exception):
            errorNode = [TextNode("This is a error **Node", TextType.TEXT)]
            split_nodes_delimiter(errorNode, "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()

    
 