import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALICS)
        node4 = TextNode("This is a text node", TextType.ITALICS, "google.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertIsNone(node3.url)
        self.assertIsNotNone(node4.url)
if __name__ == "__main__":
    unittest.main()