def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_counts(text)    
    print_report(char_count, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_counts(text):
    lowered = text.lower()
    done = {}

    for word in lowered:
        working = word.split()

        for char in working:
            if char not in done:
                done[char] = 1
            else:
                done[char] += 1

    return done

def print_report(char_count, word_total):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_total} found in the document\n")

    sorted_chars = {}
    sorted_chars = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    for i in sorted_chars:
        if i.isalpha():
            print(f"the character {i} was found {sorted_chars[i]} times in the document")

    print("\n--- End of Report ---")

main()