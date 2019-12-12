# Tests for Syd_the_Bookworm Functions

from my_module.Syd_the_Bookworm_Functions import *
import string

compare_string = 'Hello, it\'s me'
compare_list = ['hello', 'its', 'me']

def test_prepare_text():
    """Tests prepare_text function"""
    
    assert ['Hello, it\'s me'] == prepare_text(compare_string)  
    assert isinstance(prepare_text(compare_string), list)
    assert callable(prepare_text)
    
def test_end_chat():
    """Tests end_chat function"""
    assert end_chat(compare_list) == False
    assert isinstance(end_chat(compare_list), bool)
    assert callable(end_chat)
    
def test_choose_book():
    """Tests choose_book function in few cases"""
    assert choose_book(['string']) == True
    assert isinstance(choose_book(['string']), bool)
    assert callable(choose_book)
    
def test_choose_author():
    """Test choose_author function in few cases"""
    assert choose_author(['string']) == True
    assert isinstance(choose_author(['string']), bool)
    assert callable(choose_author)
    
def test_all():
    """Tests all the test functions I created at once."""
    test_prepare_text()
    test_end_chat()
    test_choose_author()
    test_choose_book()