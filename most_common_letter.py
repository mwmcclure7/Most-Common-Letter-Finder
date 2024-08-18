from pprint import pprint

file = open(input("Enter the file name: "), 'r')
words = file.read().splitlines()
file.close()
connected_words = ''
alphabit_count = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

for word in words:
    connected_words += word
connected_words = connected_words.lower()

for letter in alphabit_count:
    alphabit_count[letter] = connected_words.count(letter)

sorted_alphabit = sorted(alphabit_count.items(), key=lambda x: x[1], reverse=True)
pprint(sorted_alphabit)