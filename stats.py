def get_number_of_words(book_text):
    count_text = len(book_text.split())
    # print(f"{count_text} words found in the document")
    return count_text

def get_all_chars(book_text):
    count_of_each_char = {}
    all_chars = book_text.lower()
    for char in all_chars:
        if char in count_of_each_char:
            count_of_each_char[char] += 1
        else:
            count_of_each_char[char] = 1
    return count_of_each_char

def get_sorted_dict(chars_dict):
    chars_keys = list(chars_dict.keys())
    chars_keys.sort()
    sorted_chars_dict = {}
    for char in chars_keys:
        if char.isalpha():
            sorted_chars_dict[char] = chars_dict[char]
    return sorted_chars_dict