import pytest
from roman_numerals import Numeral


TESTCASES = [
    (0, ''),
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X'),
    (11, 'XI'),
    (12, 'XII'),
    (13, 'XIII'),
    (14, 'XIV'),
    (15, 'XV'),
    (16, 'XVI'),
    (17, 'XVII'),
    (18, 'XVIII'),
    (19, 'XIX'),
    (20, 'XX'),
    (21, 'XXI'),
    (22, 'XXII'),
    (23, 'XXIII'),
    (24, 'XXIV'),
    (25, 'XXV'),
    (26, 'XXVI'),
    (27, 'XXVII'),
    (28, 'XXVIII'),
    (29, 'XXIX'),
    (30, 'XXX'),
    (31, 'XXXI'),
    (32, 'XXXII'),
    (33, 'XXXIII'),
    (34, 'XXXIV'),
    (35, 'XXXV'),
    (36, 'XXXVI'),
    (37, 'XXXVII'),
    (38, 'XXXVIII'),
    (39, 'XXXIX'),
    (40, 'XL'),
    (49, 'XLIX'),
    (50, 'L'),
    (60, 'LX'),
    (70, 'LXX'),
    (80, 'LXXX'),
    (90, 'XC'),
    (99, 'XCIX'),
    (100, 'C'),
    (101, 'CI'),
    (104, 'CIV'),
    (199, 'CXCIX'),
    (240, 'CCXL'),
    (250, 'CCL'),
    (400, 'CD'),
    (499, 'CDXCIX'),
    (500, 'D'),
    (600, 'DC'),
    (900, 'CM'),
    (999, 'CMXCIX'),
    (1000, 'M'),
    (1001, 'MI'),
    (2000, 'MM'),
    (3999, 'MMMCMXCIX'),
]

def test_it_generates_the_correct_roman_numeral():
    for n, x in TESTCASES:
        assert Numeral().generate(n) == x

def test_it_does_not_allow_a_list_to_be_passed():
    assert Numeral().generate([]) == None

def test_it_does_not_allow_a_dict_to_be_passed():
    assert Numeral().generate({}) == None

def test_it_does_not_allow_a_tuple_to_be_passed():
    assert Numeral().generate(()) == None

def test_it_does_not_allow_a_string_to_be_passed():
    assert Numeral().generate('foo') == None

def test_it_does_not_allow_None_to_be_passed():
    assert Numeral().generate(None) == None

def test_it_does_not_allow_a_float_to_be_passed():
    assert Numeral().generate(5.3) == None

def test_it_does_not_allow_a_bool_to_be_passed():
    assert Numeral().generate(True) == None
