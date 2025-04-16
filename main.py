from stats import get_num_words, get_num_of_char, sort_dic_of_chars
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def print_report(file_contents):
    words_count = get_num_words(file_contents)
    sorted_list_char_info = sort_dic_of_chars(get_num_of_char(file_contents))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char_info in sorted_list_char_info:
        char = char_info["char"]
        if char.isalpha():
            count = char_info["count"]
            print(f"{char}: {count}")
    print("============= END ===============")
    

def main():
   if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   path_to_file = sys.argv[1] 
   file_contents =  get_book_text(path_to_file)
   print_report(file_contents)
main()