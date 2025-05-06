# %%
from splitBlock import *
from blockType import *
from htmlnode import *
from textnode import *
from textToNode import *
import re

def text_to_children(text):
    textNodes = text_to_textnodes(text)
    htmlNodes = []
    for node in textNodes:
        htmlNode = TextNode.text_node_to_html_node(node)
        htmlNodes.append(htmlNode)

    return htmlNodes

def list_to_node(lines):
    lineHtml = []
    for line in lines:
        if line == "":
            continue
        li = text_to_children(line.strip())
        html = LeafNode("li", li)
        lineHtml.append(html)
    return lineHtml


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown.strip())
    children = []
    for block in blocks:
        type = blocks_to_block_type(block)
        if type == BlockType.PARAGRAPH:
            lines= block.split("\n")
            line = " ".join(lines)
            children.append(ParentNode("p", text_to_children(line)))

        elif type == BlockType.HEADING:
            int = 0
            striped = block.strip()
            for n in striped[:6]:
                if n == "#":
                    int +=1
            children.append(LeafNode(f"h{int}", text_to_children(striped[int:].strip())))

        elif type == BlockType.QUOTE:
            lines = block.split("\n")
            quoteLines = []
            for line in lines:
                if line.startswith(">"):
                    quoteLines.append(line[1:].strip())
                else:
                    quoteLines.append(line.strip())
            combine = " ".join(quoteLines)
            children.append(LeafNode("blockquote", text_to_children(combine)))

        elif type == BlockType.ORDERED:
            seperatedLines = block.split("\n")
            lines = []
            for line in seperatedLines:
                stripped = line.strip()
                digitsRemoved = re.sub(r"^\d+. ", "", stripped)
                lines.append(digitsRemoved.strip()) 
            children.append(LeafNode("ol", list_to_node(lines)))
        
        elif type == BlockType.UNORDERED:
            lines = block.splitlines()
            listLines = []
            for line in lines:
                if line.lstrip().startswith("-"):
                    leftstriped = line.lstrip()
                    dashRemoval = leftstriped[2:]
                    listLines.append(dashRemoval.strip())

            children.append(LeafNode("ul", list_to_node(listLines)))

        elif type == BlockType.CODE:
            codeBlock = block.split("\n")
            rejoin = "\n".join(codeBlock[1:-1])
            final = f"{rejoin}\n"
            codeNode = LeafNode("code", final)
            pre = ParentNode("pre", [codeNode])
            children.append(pre)

    parent = ParentNode("div", children)
    return parent

# %%
