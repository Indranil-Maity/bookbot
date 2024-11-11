with open("/home/indranil/workspace/github.com/Indranil-Maity/bookbot/books/frankenstein.txt", "r") as f:
    contents = f.read()
    words = contents.split()
    word_counts = {}
    for word in words:
        for letter in word:
            if letter.isalpha() == True:
                lower_letter = letter.lower()
                if lower_letter not in word_counts:
                    word_counts[lower_letter] = 1
                else:
                    word_counts[lower_letter] += 1
            
    print("--- STARTING BOOK ANALYSIS ---")
    print(f"Your book contains {len(word)} words")
    for a, b in word_counts.items():
        print(f"The character {a} was found {b}")
    print("--- THE END ---")