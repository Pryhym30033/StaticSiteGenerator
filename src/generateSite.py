import os
from generatePage import generate_page

def generate_pages_recursive(dirPathContent, templatePath, destDirPath):
    
    if not os.path.exists(destDirPath):
        os.mkdir(destDirPath)

    contents = os.listdir(dirPathContent)

    for content in contents:
        source = os.path.join(dirPathContent, content)
        destination = os.path.join(destDirPath, content)

        if os.path.isfile(source):
            generate_page(source, templatePath, destDirPath)
          
        else:
            generate_pages_recursive(source, templatePath, destination)
            