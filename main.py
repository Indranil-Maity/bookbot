from stats import get_book_text, book_word_count, book_stat, print_report
import sys

def main():
    
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = "".join(sys.argv[1:])

    print_report(file_path)
    
if __name__ == "__main__":
    main()
