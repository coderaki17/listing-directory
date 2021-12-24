import unittest
from string_dir import *


class Testing(unittest.TestCase):
    
    def test_running(self):
        self.assertTrue(return_list(directory))

    def test_output_is_list(self):
        self.assertTrue(isinstance(return_list(directory),list))  

    def test_content_check(self):
        if "string_dir.py" in return_list(directory):
            self.assertTrue(True)

        
if __name__ == "__main__":
    unittest.main()

    

              
        



    
        