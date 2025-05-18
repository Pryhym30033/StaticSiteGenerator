import unittest
from extractTitle import extract_title

class TestExtactTitle(unittest.TestCase):
    def test_TitleExtractor(self):   
        test1 = """#test header 1
            test line 2
            tesline 3
            test final line
            """   
        test2 = """     #test header 1
            test line 2
            tesline 3
            test final line
            """ 
        test3 = """test
            this line
            also..."""  
        self.assertEqual(extract_title(test1), "test header 1")
        self.assertEqual(extract_title(test2), "test header 1")
        with self.assertRaises(ValueError):
            extract_title(test3)


if __name__ == "__main__":
    unittest.main()