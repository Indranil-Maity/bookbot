#!usr/bin/python3

def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        word_lst = content.split()
        return word_count(word_lst), count_character(content) 

def word_count(lst):
    count = 0 
    for l in lst:
        count += 1
    return count

def count_character(content):
    content = content.lower()
    content_dict = {}
    for c in content:
        if c.isalpha() == True:
            if c not in content_dict:
                content_dict[c] = 1
            else:
                content_dict[c] += 1
    return content_dict


def print_report(word_count, count_character):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(" ")
    for count in count_character:
        print(f"The {count} character was found {count_character.get(count, 0)} times")
    print("--- End report ---")


word, char = main()
print_report(word, char)
