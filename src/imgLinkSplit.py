# %%
from textnode import *
from extract import *

def split_nodes_image(oldNodes):
    newNodes = []
    for oldNode in oldNodes:
        if oldNode.text_type != TextType.TEXT:
            newNodes.append(oldNode)
            continue
        
        remains = oldNode.text
        while remains != "":

            images = extract_markdown_images(remains)
            if not images:
                newNodes.append(TextNode(remains, TextType.TEXT))
                break

            alt, url = images[0]
            imageLink = f"![{alt}]({url})"
            pieces = remains.split(imageLink, 1)
            

            if pieces[0]:
                newNodes.append(TextNode(pieces[0], TextType.TEXT))

            newNodes.append(TextNode(alt, TextType.IMAGE, url))

            if len(pieces) > 1:
                remains = pieces[1]
            else:
                remains = ""



    return newNodes

def split_nodes_link(oldNodes):
    #create container for nodes
    newNodes = []

    #process each node 
    for node in oldNodes:
        #if node is not text add it to container
        if node.text_type != TextType.TEXT:
            newNodes.append(node)
            continue

        #get text out of node 
        text = node.text

        #while text in node continue
        while text != "":

            #extract link out of text
            links = extract_markdown_links(text)
            
            #if no link in text then break
            if not links:
                newNodes.append(TextNode(text, TextType.TEXT))
                break

            #get first extracted link data
            alt, link = links[0]
            #create link text
            linkData = f"[{alt}]({link})"
            #split text by link 
            parts = text.split(linkData, 1)

            #if first piece exists create text node and add it to container
            if parts[0]:
                newNodes.append(TextNode(parts[0], TextType.TEXT))

            #create link node and append container
            newNodes.append(TextNode(alt, TextType.LINK, link))

            #if split results greater than 1 piece set second piece to node text
            if len(parts) > 1:
                text = parts[1]
            #else set node text to empty
            else:
                text = ""

    #return node
    return newNodes


# %%
