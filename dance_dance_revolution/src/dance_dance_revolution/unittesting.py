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

    def test_getFile(self):
        for path in self.search:
            testfile = gff.open_file(path)
            self.assertIsInstance(testfile, self.results[self.search.index(path)])

    def tearDown(self):
        return super().tearDown()
    
class test_  
    

if __name__ == '__main__':
    unittest.main()

