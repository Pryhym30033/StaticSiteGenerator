import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_Nodes(self):
        testNode = HTMLNode("p", "tag test", None, {"href":"www.google.com", "target":"blank"})
        testNode1 = HTMLNode("a", "tag test", None, {"href":"www.ebay.com", "target":"blank"})
        testNode2 = HTMLNode("p", "tag test", "h1", {"href":"www.google.com", "target":"blank"})
        testNode3 = HTMLNode("p", "tag test", None)
        self.assertNotEqual(testNode.props, testNode1.props)
        self.assertIsNone(testNode3.props)
        self.assertIsNotNone(testNode2.children)
        self.assertNotEqual(testNode.tag, testNode1.tag)
if __name__ == "__main__":
    unittest.main()