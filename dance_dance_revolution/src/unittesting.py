#Unit tests for my game
import io
import unittest



"""
#create setUp and tearDown classes 
class Example_setUp_tearDown(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


# unit test interface 
class Test_ExampleClass(unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def test_example_method(self):
        self.assertEqual(1 + 1, 2)

    def tearDown(self):
        return super().tearDown()
"""    


import get_from_files as gff

class Test_get_from_file_module(unittest.TestCase):

    def setUp(self):
        self.search = list(["", " ", "config.txt", "styles.txt", "randomFile.txt"])
        self.results = list([Exception, Exception, io.IOBase, io.IOBase, Exception])
        return super().setUp()

    def test_open_File(self):
        for item_str in self.search:
            path = gff.top_level_path / "src" / item_str
            testfile = gff.open_file(path)
            self.assertIsInstance(testfile, self.results[self.search.index(item_str)])


    def test_get_line_by_keyword(self):
        self.search = list(["TestLength: ","TestWords: ", "", " ","TestWord_DoesNotExist" ])
        self.result = list(["1234", "Correct test words", ValueError, None, None])
        for item in self.search:
            testLine = gff.get_line_by_keyword("testFile.txt", item, second_level_path="tests/")
            print("searching for item: '", item, "' got ", testLine)
            self.assertEqual(testLine, self.result[self.search.index(item)])
    
    def test_get_line_by_keyword_button_style(self):   
        testLine = gff.get_line_by_keyword("styles.txt", "ButtonStyle:", second_level_path="src/")
        self.assertEqual(testLine, "TButton")

    def test_get_images_path(self):
        testLine = gff.get_line_by_keyword("config.txt", "ImagesPath:", second_level_path="src/")
        self.assertEqual(testLine, "assets/images/")

    def test_if_images_path_exists(self):
        testLine = gff.get_line_by_keyword("config.txt", "ImagesPath:", second_level_path="src/")
        full_path = gff.top_level_path / testLine
        print("Testing if path exists: ", full_path)
        self.assertTrue(full_path.exists())

    def tearDown(self):
        return super().tearDown()
"""
class test_get_line_by_keyword(unittest.TestCase):

    def setUp(self):
        self.search = list(["TestLength: ","TestWords: ", "", " ","TestWord_DoesNotExist" ])
        self.result = list(["1234", "Correct test words", Exception, Exception, Exception])
        return super().setUp()
    
    def test_get_line_by_keyword(self):
        for item in self.search:
            print("**********************",gff.top_level_path/"tests"/"testFile.txt")
            testLine = gff.get_line_by_keyword("testFile.txt", item, second_level_path="tests/")
            self.assertEqual(testLine, self.result[self.search.index(item)])


    def tearDown(self):
        return super().tearDown()
"""

if __name__ == '__main__':
    unittest.main()

