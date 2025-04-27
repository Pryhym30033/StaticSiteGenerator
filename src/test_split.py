import unittest
from imgLinkSplit import *

class TestSplit(unittest.TestCase):
    def test_split(self):
        nodes = [TextNode('this is a test ![image](http://url.com) and ![image2](url.com) image node. now here\'s a link node [test link](img.com) and heres another [link2](img2.com) one ', TextType.TEXT)]
        node2 = [TextNode('![image](http://url.com) andimage node. now and heres another [link2](img2.com) one ', TextType.TEXT)]
        self.assertNotEqual(nodes, node2)
        newNodes = split_nodes_image(nodes)
        newNodes2 = split_nodes_link(node2)
        self.assertEqual(newNodes[0], TextNode('this is a test ' , TextType.TEXT))
        self.assertEqual(newNodes2[0], TextNode('![image](http://url.com) andimage node. now and heres another ', TextType.TEXT))

if __name__ == "__main__":
    unittest.main()