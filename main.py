from stats import word_count, character_count, sort_char_counts
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 


filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():

    my_book = get_book_text(filepath)
    words_total = word_count(my_book)
    # print(f"Found {words_total} total words")
    character_total = character_count(my_book)
    # print(f"{character_total}")
    sorted_chars = sort_char_counts(character_total)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_total} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()