# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:33:36 2024
version 1
@author: Nadifa Aziza
Student ID: 20027521
This is is a unittest that will automatically check if the 'dictfunction' works
"""
import unittest
from dictfunction import add_dict, delete_dict, sort_dict, search_dict

class TestDictFunctions(unittest.TestCase):
    def test_add_dict(self):
        test_dict = {}
        add_dict(test_dict, "tom holland", 2000)  # Assuming the date should be an integer
        self.assertEqual(test_dict, {"tom holland": 2000})  # Use a dictionary with a key-value pair

    def test_delete_dict(self): 
        test_dict = {"tom holland": 2000, "charlie chaplin": 1950, "timothee": 2002} 
        result = delete_dict(test_dict, "tom holland") #tom holland will be deleted
#if its correct: 
        self.assertEqual(result, {"charlie chaplin": 1950, "timothee": 2002} ) #list will change to this, as alan has been deleted

    def test_delete_not_found(self):
        test_dict = {"charlie chaplin": 1950, "timothee": 2002} #dictionary doe not include tom holland
        result = delete_dict(test_dict, "tom holland")  # Attempt to delete a non-existent entry 
        self.assertEqual(result, {'charlie chaplin': 1950, 'timothee': 2002})  # Verify that the dictionary remains unchanged

    def test_sort_dict(self):
        test_dict = {"timothee": 2002, "charlie chaplin": 1950, "tom holland": 2000} #dictionary is not in order
        result = sort_dict(test_dict)
        self.assertEqual(result, [('charlie chaplin', 1950), ('timothee', 2002), ('tom holland', 2000)]) #sort in ascending order
   

    def test_search_dict_found(self):
        test_dict = {"tom holland": 2000, "charlie chaplin": 1950} #tom holland is in the dictionary
        result = search_dict(test_dict, "tom holland") #input tom holland
        self.assertEqual(result, {'tom holland': 2000, 'charlie chaplin': 1950})  # Should return the entry for "tom holland"
        
    def test_search_dict_not_found(self):
        test_dict = {"tom holland": 2000, "charlie chaplin": 1950} #dictionary does not contain timothee
        result = search_dict(test_dict, "timothee") #input timothee
        self.assertEqual(result, {"tom holland": 2000, "charlie chaplin": 1950}) #timothee will not be found

        
if __name__ == '__main__':
    unittest.main()