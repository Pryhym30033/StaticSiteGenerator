# %%
def markdown_to_blocks(text):
    lines = text.split("\n\n")
    newlines = []
    for line in lines:
        if "\n" in line:
            line = line.replace("\n\n", "")
        line = line.replace("    ", "")
        newlines.append(line.strip())
    return newlines
        

blocks = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
