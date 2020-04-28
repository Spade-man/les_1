import home_work_les_4
import random

def test_F_len():
    assert len(home_work_les_4.F(['a', 'b', 'c'], 10)) == 10

def test_F_element():
    lst = ['a', 'b', 'c', 'd', 'e']
    a = home_work_les_4.F(lst, 3)
    i = random.choice(a)
    assert i in lst


