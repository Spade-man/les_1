import divisor_master

def test_is_simple1():
    assert divisor_master.is_simple(66431) == True

def test_is_simple2():
    assert divisor_master.is_simple(66432) == False

def test_all_simple_dividers():
    assert divisor_master.all_dividers(10123) == [1, 53, 191, 10123]

def test_biggest_simp_divder():
    assert divisor_master.biggest_simp_divder(10123) == 191

def test_canon():
    assert divisor_master.canon(10123) == [53, 191]

def test_biggest_divder():
    assert divisor_master.biggest_divder(66432) == 33216