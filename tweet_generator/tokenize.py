# module for creating lists of tokens from a text
import sys

def read_in(text):
    text_file = open(text, 'r') #Read text file
    word_list = [] #Create empty list to store words
    for line in text_file.readlines(): #Loop through line of words
        word_list.extend(line.split()) #Split words by white space and store as one huge list of individual words
    return word_list

if __name__ == '__main__':
    input_text = sys.argv[1] #Takes in text file as input
    text_list = read_in(input_text) #Create list
    print(text_list)
