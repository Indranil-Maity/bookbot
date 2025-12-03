def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def book_word_count(book):
    num_words = len(book.split())
    return f"Found {num_words} total words"

def book_stat(book):
    res = {}
    for l in book.lower():
        if l.isalpha():
            if l in res:
                res[l] += 1
            else:
                res[l] = 1

    return [{"char": x, "count": y} for x, y in res.items()]

def print_report(file_path):
    book = get_book_text(file_path)
    num_words = book_word_count(book)
    stat = book_stat(book)
    stat.sort(reverse=True, key=lambda x: x["count"])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for s in stat:
        print(f"{s['char']}: {s['count']}")
    print("============= END ===============")

