import pytest
import random
import string
import session6
import os
import inspect
import re
import math
import time
from session6 import doc_string_checker
# from session6 import next_fibonacci
# from session6 import dec_factory_calculator

README_CONTENT_CHECK_FOR = [
    'doc_string_checker',
    'next_fibonacci',
    'dec_factory_calculator',
    'closure',
    'decorator'
]

def test_session6_readme_exists():
    """ Test that checks if README.md file exists
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session6_readme_200_words():
    """ Test that checks if README.md file contains 200 words 
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add atleast 200 words"


def test_session6_readme_proper_description():
    """ Test to check if the README.md file has all relevant description. 
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    """ Test to check header formatting of README.md file. \
        File should contain minimum og 10 '#' 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10



def test_session6_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).       
    """
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session6_function_name_had_cap_letter():
    """ Test that checks for usage of Capital letter(s) in function names        
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

############################## Assignment Validations###########################

def test_session6_doc_string_checker_50Words():
    """ Test doc_string_checker function. Function passed should have more than 50 words description
        failure: 0 return value
        success: 1 return value   
    """
    def fn_with_50_words():
        """This is a dummy function with more than 50 characters in description
        and I am just repeating the same text to get to the count of 50
        This is a dummy function with more than 50 characters in description
        and I am just repeating the same text to get to the count of 50 """
        pass

   
    assert doc_string_checker()(fn_with_50_words) == True, "doc_string_checker should return true as there are more than 50 words in fn desc"
    

def test_session6_doc_string_checker_lt50Words():
    """ Test doc_string_checker function. Function passed should have more than 50 words description
        failure: 0 return value
        success: 1 return value   
    """
    def fn_with_less_than_50_words():
        """This is a dummy function with less than than 50 characters in description"""
        pass
    
    assert doc_string_checker()(fn_with_less_than_50_words) == False, "doc_string_checker should return false as there are less than 50 words in fn desc"
    
