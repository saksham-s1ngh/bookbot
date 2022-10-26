from itertools import count

with open("/Users/saksham_s1ngh/workspace/github.com/saksham-s1ngh/bookbot/books/frankenstein.txt") as f:
    data = f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_of_characters(book):
    lowercase_book = book.lower()
    character_count = {}
    for character in lowercase_book:
        if character in character_count.keys():
            character_count[character]+= 1
        else:
            character_count[character] = 1
    return character_count

def alphabet_counter(book):
    list_of_characters = list(count_of_characters(book).keys())
    list_of_characters.sort()
    char_count = count_of_characters(book)

    for character in list_of_characters:
        if character.isalpha():
            print(f"The \'{character}\' character was found {char_count[character]} times")


print("--- Begin report of books/frankenstein.txt ---")
print(count_words(data), "words found in the document\n")
alphabet_counter(data)
print("--- End report ---")