import sys
from stats import get_number_of_words, get_all_chars, get_sorted_dict

def main():
    if sys.argv.__len__() == 2:
        book_path = sys.argv[1]
        book_content = get_book_text(book_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {get_number_of_words(book_content)} total words")
        print("--------- Character Count -------")
        sorted_dict = get_sorted_dict(get_all_chars(book_content))
        sorted_keys = sorted_dict.keys()
        for key in sorted_keys:
            print(f"{key}: {sorted_dict[key]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents



main()