import unittest
from string_dir import *


class Testing(unittest.TestCase):
    
    def test_running(self):
        self.assertTrue(return_list('/Users/akashrc/pytest'))

    def test_output_is_list(self):
        self.assertTrue(isinstance(return_list('/Users/akashrc/pytest'),list)) 

    def test_content_check(self):
        if "string_dir.py" in return_list('/Users/akashrc/pytest'):
            self.assertTrue(True)

        
if __name__ == "__main__":
    unittest.main()

    

              
        



    
        