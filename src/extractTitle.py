# %%
def extract_title(markdown):
    if "#" not in markdown:
        raise ValueError('No header in Markdown!!!')
    
    lines = list(filter(None, markdown.split("\n")))
    header = ""

    for line in lines:
      
        line = line.strip()
        if "#" not in line[:1]:
            continue
        header += line.strip()
        break

    return header[1:]
# %%
