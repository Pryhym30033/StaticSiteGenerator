def markdown_to_blocks(text):
    lines = text.split("\n\n")
    newlines = []
    for line in lines:
        if "\n" in line:
            line = line.replace("\n\n", "")
        line = line.replace("    ", "")
        newlines.append(line.strip())
    return newlines
        