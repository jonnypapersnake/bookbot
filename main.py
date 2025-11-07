## A function to take a file path, open it and convert it to text that can be read ##
import sys
from stats import count_words, number_of_characters, sort_dictionary

def get_book_text (filepath):
    with open (filepath) as f:
        text = f.read()
        return text
    

## After importing out functions from stats this main function takes a book, stores it as book text. It runs Count words and stores the number of words, it then figures out the number of characters, then sorts them out in the dictionary.
## A series of print statements run and list the total number of words. Then finally a for loop runs through the dictionary and stores each character as ch. We then loop through and if the character is not punctuation it is printed with the number of times
## it appears. Starting with the largest number ##

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath =sys.argv[1]
    book_text = get_book_text (filepath)

    num_words = count_words (book_text)
    num_characters = number_of_characters (book_text)
    sort_results = sort_dictionary (num_characters)

    print ("============ BOOKBOT ============")
    print ("Analyzing book found at ")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for item in sort_results:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print ("============= END ===============")



    
main()




