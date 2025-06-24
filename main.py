from stats import get_num_words
import sys

def main():    
    print("Input path to book: ", sys.argv)

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        char_count = get_char_counts(text)    
        print_report(char_count, num_words)

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


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(char_count, word_total):
    print("--- Begin report of: ", sys.argv[1], "---")
    print(f"{word_total} words found in the document\n")

    sorted_chars = {}
    sorted_chars = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    for i in sorted_chars:
        if i.isalpha():
            print(f"{i}: {sorted_chars[i]}")

    print("\n--- End of Report ---")

main()