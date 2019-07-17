import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '/'))
sys.path.insert(0, root_path)

import pytest

import module


def test_make_throws_on_number_input():
    one_number = 123

    with pytest.raises(Exception):
        module.make(one_number)


def test_make_throws_on_too_many_characters():
    too_many_characters = 'AAA'

    with pytest.raises(Exception):
        module.make(too_many_characters)


def test_make_throws_on_none_en_characters():
    none_en_character = "Ü"

    with pytest.raises(Exception):
        module.make(none_en_character)


def test_make_returns_A_on_A():
    input_character = 'A'

    result = module.make(input_character)

    assert result == 'A'


def test_make_gives_diamonds():
    input_character = 'C'
    expected = \
        '__A__\n' + \
        '_B_B_\n' + \
        'C___C\n' + \
        '_B_B_\n' + \
        '__A__'

    result = module.make(input_character)

    assert result == expected
    assert False
