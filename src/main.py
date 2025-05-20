from copyfunc import *
from generateSite import generate_pages_recursive

def main():
   
    CopyControlFunc()
    fromPath = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/content"
    template = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/template.html"
    dest = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/public"
    generate_pages_recursive(fromPath, template, dest)    

main()