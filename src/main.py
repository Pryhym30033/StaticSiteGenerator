from copyfunc import *
from generatePage import generate_page

def main():
   
    CopyControlFunc()
    fromPath = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/content/index.md"
    template = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/template.html"
    dest = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/public"
    generate_page(fromPath, template, dest)    

main()