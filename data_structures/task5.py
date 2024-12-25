# Task 5 Python Basics

def remove_duplicated_words(line: str):
    unique_words = list()
    words = line.split(' ')     # dissect words from line

    for word in words:
        if word not in unique_words:
            unique_words.append(word)       # add unique elements to list

        result = " ".join(unique_words)     # turn list elements into string
    return result

# TESTS
print(remove_duplicated_words('cat cat dog 1 dog 2'))
print(remove_duplicated_words('cat cat cat'))
print(remove_duplicated_words('1 2 3'))