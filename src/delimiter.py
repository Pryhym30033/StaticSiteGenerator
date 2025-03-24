from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodeList = []
    for old_node in old_nodes:
        #if old node is not text type add to list and move on
        if old_node.text_type is not TextType.TEXT:
            newNodeList.append(old_node)
            continue

        #grab text from node
        text = old_node.text
        
        while delimiter in text:
            
            start = text.find(delimiter)
            #find starting point
            if start > 0:
                #Add segment to node list 
                newNodeList.append(TextNode(text[:start], TextType.TEXT))

            #Find endpoint
            end = text.find(delimiter, start+len(delimiter))
            if end == -1:
                raise Exception("No end Tag")
            
            #Add affected Node
            newNodeList.append(TextNode(text[start+len(delimiter):end], text_type))

            #adjust text
            text = text[end+len(delimiter):]

            
        #add end Node
        if text:
            newNodeList.append(TextNode(text, TextType.TEXT))
        

    return newNodeList

