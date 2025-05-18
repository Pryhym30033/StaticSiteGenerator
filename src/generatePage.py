import os
from markdownTohtml import *
from extractTitle import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}")

    markdown = ''
    template = ''

    with open(from_path, 'r') as file:
        markdown = file.read()

    with open(template_path, 'r') as file:
        template = file.read()

    node = markdown_to_html_node(markdown)

    html = node.to_html()
    title = extract_title(markdown)

    fullPage = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    
    fileName = "index.html"
    fullPath = os.path.join(dest_path, fileName)

    #os.makedirs(fullPath, exist_ok=True)

    with open(fullPath, 'w') as file:
        file.write(fullPage)

