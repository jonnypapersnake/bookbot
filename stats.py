## Function to count words. Takes the parameter of book text and splits whatever book text is into individual strings stored as words. It then returns the length of words, giving the number of words in a book ##
   
def count_words (book_text):
    words = book_text.split()
    return len(words)

## Function to take the book text and figure out how many times each character appears including punctuation. It creates an empty dictionary, takes the book text and makes it all lower case, which is then stored as a variable.
## For each character in number it then loops through and checks if it is already in the dictionary. If it isn't it adds it, if it is it adds 1 to the tally. Then it returns the dictionary at the end ##

def number_of_characters (book_text):
    list_of_characters = {}
    number = book_text.lower()
    for i in number:
        if i in list_of_characters:
            list_of_characters[i] +=1
        else:
            list_of_characters[i] = 1
    return list_of_characters

## Function to sort the dictionary. It creates an empty list, then loops through the list of characters dictionary looking at each key (character) and each value (number of times they appear).
## A second function then sorts those figures numerically ##
 
def sort_dictionary (list_of_characters):
    results = []
    for key, value in list_of_characters.items():
        results.append({"char":key, "num": value})

    def sort_on(item):
        return item["num"]
    
    results.sort(reverse=True, key=sort_on)
    return results
    


