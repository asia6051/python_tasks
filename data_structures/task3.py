# Task 3 - Python Basics

from typing import Iterable

def build_from_unique_words(*lines: Iterable[str], word_number: int):
    result = ""
    for line in lines:
        words_counter = dict()
        words = line.split(' ')

        for word in words:
            if word not in words_counter.keys():
                words_counter[word] = 1
            else:
                words_counter[word] += 1

        unique_not_found = 1

        for word in words[word_number:]:    # find unique words starting from given word_number
            if (words_counter[word] == 1) and unique_not_found:
                unique_not_found = 0
                result = result + " " + word
    return result

# TESTS
print("Result:", build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1))
print("Result:",build_from_unique_words('a b c', '', 'cat dog milk', word_number=0))
print("Result:",build_from_unique_words('1 2', '1 2 3', word_number=10))
print("Result:",build_from_unique_words(word_number=10))
