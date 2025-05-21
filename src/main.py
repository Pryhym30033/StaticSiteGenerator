from copyfunc import *
from generateSite import generate_pages_recursive
import sys

basepath = ""
if sys.argv[1]:
    basepath += sys.argv[1]
else:
    basepath += "/"

def main():
   
    CopyControlFunc()
    fromPath = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/content"
    template = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/template.html"
    dest = "/home/pryhym/workspace/github.com/Pryhym30033/StaticSiteGenerator/docs"
    generate_pages_recursive(fromPath, template, dest, basepath)   

main()