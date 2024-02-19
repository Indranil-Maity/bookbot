def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_count = count_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{len(text.split())} words found in the document\n")

    for char, count in chars_count.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def count_characters(text):
    chars_count = {}
    for char in text:
        lowered = char.lower()
        if lowered.isalpha():
            chars_count[lowered] = chars_count.get(lowered, 0) + 1
    return chars_count


def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    main()
