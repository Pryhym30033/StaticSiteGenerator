import unittest
from extract import *

class TestExtract(unittest.TestCase):
    def test_Extractor(self):
        text = "This is text with a [rick roll](https://i.imgur.com/link/) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        pictureCapture = extract_markdown_images(text)
        linkCapture = extract_markdown_links(text) 
        self.assertEqual(f"{pictureCapture}", "[('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]")
        self.assertEqual(f"{linkCapture}", "[('rick roll', 'https://i.imgur.com/link/')]")

if __name__ == "__main__":
     unittest.main()