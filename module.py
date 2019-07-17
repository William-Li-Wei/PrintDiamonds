import numpy as np


def make(character: str):

    FULL_EN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #  validate input
    if not isinstance(character, str):
        raise Exception('not a character')

    if len(character) != 1:
        raise Exception('too many characters')

    index = FULL_EN_ALPHABET.find(character.upper())
    if index == -1:
        raise Exception('not en character')

    # 'ABC' for input 'D'
    before_character = FULL_EN_ALPHABET[0: index]
    # 'CBA' for input 'D'
    after_charcter = before_character[::-1]
    # 'ABCDCBA' for input 'D'
    characters_all_lines = before_character + character + after_charcter

    #  init the result matrix
    diamond_size = index * 2 + 1
    result_matrix = init_result_matrix(diamond_size)
    print(result_matrix)

    # fill character into the correct position
    for idx, char in enumerate(characters_all_lines):
        pos = int(diamond_size / 2) - FULL_EN_ALPHABET.find(char)
        result_matrix[idx, pos] = char

        if char != 'A':
            second_pos = diamond_size - 1 - pos
            result_matrix[idx, second_pos] = char
    print(result_matrix)

    # turn result_matrix into string
    result_str = ''
    for i in range(0, diamond_size):
        for j in range(0, diamond_size):
            result_str = result_str + str(result_matrix[i, j])
        result_str = result_str + '\n'
    print(result_str)

    return result_str[:-1]


def init_result_matrix(size: int):
    return np.full((size, size), '_')
