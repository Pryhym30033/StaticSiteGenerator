import unittest
from splitBlock import markdown_to_blocks

class TestBlockSplit(unittest.TestCase):
    def test_splitblock(self):
        blocks = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        lines = markdown_to_blocks(blocks)
        self.assertEqual(lines, 
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            )