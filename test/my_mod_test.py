#this is the my_mod_test file 

from app.my_mod import enlarge

def test_example():
    assert 1+1 == 2

def test_enlarge():
    assert enlarge(10) == 1000