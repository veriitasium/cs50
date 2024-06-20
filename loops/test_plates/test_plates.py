"""
    * pip3 install pytest
    * pytest test_....
    * python3 -m pytest test_plates/test_plates.py (if above command not viable)
"""

from plates import is_valid

def test_least_characters():
    assert is_valid("H") == False

def test_max_characters():
    assert is_valid("OUTATIME") == False

def test_first_two_letters():
    assert is_valid("50CS") == False
    
def test_zero_not_first_number():
    assert is_valid("CS05") == False

def test_no_numbers_in_middle():
    assert is_valid("AAA22A") == False

def test_no_periods_spaces_punctuations():
    assert is_valid("PI3.14") == False

def test_met_requirements():
    assert is_valid("CS50") == True