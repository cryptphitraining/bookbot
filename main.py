# from os import chdir
# from pathlib import Path

# file_to_read = 'books/frankenstein.txt'
# current_dir = Path.cwd()
# path_to_file = current_dir / file_to_read

# def get_book_text(path_to_file):
#     with open(path_to_file) as f:
#         file_content = f.read()
#     print(file_content)

# def main():
#     get_book_text(path_to_file)

# main()

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)
#     # text_split = text.split()
#     # print(f"{(len(text_split))} words found in the document")



# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()
import sys
from stats import *

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     print(f"{num_words} words found in the document")

def main():
    book_path = sys.argv
    if len(book_path) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(book_path[1])
    num_words = get_num_words(text)
    chars_dict = count_char(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path[1], num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()