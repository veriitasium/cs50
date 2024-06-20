"""
    * pip3 install pytest
    * pytest test_....
    * python3 -m pytest test_bank/test_bank.py (if above command not viable)
"""

from bank import value

def test_no_bank_greeting():
    assert value("What's happening?") == 100

def test_partially_bank_greeting():
    assert value("How you doing?") == 20

def test_bank_greeting():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0