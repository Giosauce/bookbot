import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print("Arguments are valid! Continuing...")

from stats import count_words, count_chars, sort_char_counts

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = count_words(book_text)

    char_counts = count_chars(book_text)
    sorted_chars = sort_char_counts(char_counts)

    print_report(path, num_words, sorted_chars)
     
main()