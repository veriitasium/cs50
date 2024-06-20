"""
    * pip3 install pytest
    * pytest test_....
    * python3 -m pytest test_fuel/test_fuel.py (if above command not viable)
"""

from fuel import convert

def test_empty():
    assert convert("0/4") == "E"
    assert convert("1/100") == "E"

def test_full():
    assert convert("99/100") == "F"
    assert convert("4/4") == "F"