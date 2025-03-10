import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.ITALIC, "google.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertIsNone(node3.url)
        self.assertIsNotNone(node4.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        with self.assertRaises(AttributeError):
            failure = TextNode("Should Fail", TextType.IMG)

if __name__ == "__main__":
    unittest.main()