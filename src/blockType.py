# %%
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def blocks_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    elif block[0] == "`" and block[1]=="`" and block[2] == "`":
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif block[0] == "-" and block[1] == " ":
        return BlockType.UNORDERED
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED
    else:
        return BlockType.PARAGRAPH
