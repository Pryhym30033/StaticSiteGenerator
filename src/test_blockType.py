import unittest
from blockType import *

class TestBlockType(unittest.TestCase):
    def test_blockType(self):
        code = "```test```"
        list = "- list"
        ordered = "1. first"
        quote = "> testing quote"
        para = "regular test"
        self.assertEqual(blocks_to_block_type(code), BlockType.CODE)
        self.assertEqual(blocks_to_block_type(list), BlockType.UNORDERED)
        self.assertEqual(blocks_to_block_type(ordered), BlockType.ORDERED)
        self.assertEqual(blocks_to_block_type(quote), BlockType.QUOTE)
        self.assertEqual(blocks_to_block_type(para), BlockType.PARAGRAPH)

if __name__ == "main":
    unittest.main()