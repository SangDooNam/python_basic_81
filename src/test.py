from text import to_upper, to_word_list_isupper
import unittest

class TestText(unittest.TestCase):
    
    def setUp(self) -> None:
        self.upper = to_upper("abcdef")
        self.result_upper = "ABCDEF"
        self.isupper_arg_1 = ['I', 'LOVE', 'YOU']
        self.isupper_arg_2 = ['i', 'LOVE', 'YOU']
        self.isupper_1 = to_word_list_isupper(self.isupper_arg_1)
        self.isupper_2 = to_word_list_isupper(self.isupper_arg_2)
        
    #Task1
    def test_to_upper(self):
        self.assertEqual(self.upper, self.result_upper)
    #Task2
    def test_to_word_list_isupper_1(self):
        self.assertTrue(self.isupper_1)
    #Task3
    def test_to_word_list_isupper_2(self):
        self.assertFalse(self.isupper_2)
        
    #Task4 it won't raise TypeError but AttributeError unless it is not modified to raise TypeError
    def test_to_upper_type_error(self):
        with self.assertRaises(TypeError):
            to_upper(1234)
            to_upper([1,2,3,4])
    
    def test_to_word_list_isupper_type_error(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper('Hello Error')
            to_word_list_isupper(1234567890)
    
    






if __name__ == '__main__':
    unittest.main()