from stats import *    
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]    
    file_contents = get_book_text(book_path)
    total_words = count_words(file_contents)
    word_counts = char_count(file_contents)
    new_dict = num_char_count(word_counts)
    print(f"{'='*15} BOOKBOT {'='*15}")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"{'='*13} Word Count {'='*13}")
    print(f"Found {total_words} total words")
    print(f"{'='*10} Character Count {'='*10}")
    for dct in new_dict:
        if dct["char"].isalpha():
            print(f"{dct["char"]}: {dct["num"]}")
    print(f"{'=' * 10} END {'=' * 10}")            
main()
