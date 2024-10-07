"""
Created on Wed Sep 25 19:53:56 2024
version 1
@author: Nadifa Aziza
Student ID: 20027521

This is is a unittest that will automatically check if the 'listfunction' works
"""
import unittest
from listfunction import add_value, sort_value, delete_value, search_value

class TestListFunctions(unittest.TestCase):
    def test_add_value(self): 
        test_list = []
        result = add_value(test_list, "Nadifa") 
#if its correct: 
        self.assertEqual(result, ["Nadifa"]) 
# check if its modified 
        self.assertEqual(test_list, ["Nadifa"]) 

    def test_sort_value(self): 
        test_list = ["Charlie", "Nadifa", "Alan"] 
        result = sort_value(test_list) 
#if its correct: 
        self.assertEqual(result, ["Alan", "Charlie", "Nadifa"]) 

    def test_delete_value(self): 
        test_list = ["Nadifa", "Charlie", "Alan"] 
        result = delete_value(test_list, "Alan") #alan will be deleted
#if its correct: 
        self.assertEqual(result, ["Nadifa", "Charlie"]) #list will change to this, as alan has been deleted

    def test_delete_not_found(self): 
        test_list = ["Hong", "Charlie", "Alan"] 
        delete_value(test_list, "Nadifa")
#check if the list remain unchanged
        self.assertEqual(test_list, ["Hong", "Charlie", "Alan"])
        
    def test_search_value(self):
        test_list = ["Nadifa", "Charlie"]
        result = search_value(test_list, "Nadifa")
        self.assertEqual(result, ["Nadifa", "Charlie"]) #Nadifa is in the list
#        self.assertNotEqual("Alan", test_list) #Alan is not in the list
        

if __name__ == '__main__':
    unittest.main()
