"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""
#Dana funkcja
def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

#Moj kod
words = generate_words()
with open("utf8.txt", 'w', encoding ="UTF-8") as file1:
    utf8_words = ([word for word in words])
    text1 = "\n".join(utf8_words)
    file1.write(text1)

with open("CP1252.txt", 'w', encoding ="CP1252") as file2:
    cp_words = ([word for word in reversed(words)])
    text2 = ",".join(cp_words)
    file2.write(text2)