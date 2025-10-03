# test_ajvjson.py
"""
Tests for AjvJSON module.
"""

import unittest
from ajvjson import AjvJSON

class TestAjvJSON(unittest.TestCase):
    """Test cases for AjvJSON class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AjvJSON()
        self.assertIsInstance(instance, AjvJSON)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AjvJSON()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
