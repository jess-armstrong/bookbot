import sys
from stats import get_num_words, get_chars_dict, sort_dict

def main():
    books = get_argv(sys.argv)
    #print(books)
    text = get_book_text(books)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_dict(chars_dict)
    print_report(books, num_words, sorted_chars)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_argv(argv):
    if len(argv) <=1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return argv[1]
        
        
        

def print_report(book_path, num_words, sorted_chars):   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        print(i["char"]+": "+ str(i["num"]))
    print("============= END ===============")
    

main()