#Store all of the words into an array called, alg_word_set

def histogram():
    new_word_dict = {}
    for key_word in alg_word_set:
        if key_word in new_word_dict: #If that word exists in the set
            new_word_dict[key_word] += 1 #Increment the count value
        else:
            new_word_dict[key_word] = 1 #Initialize it with a value
    return new_word_dict

def unique_words(histogram_input):
    unique_total_count = 0
    return len(histogram_input.keys())

def specific_word_count(word, histogram_input):
    if word in histogram_input:
        return(histogram_input[word])
    else:
        raise ValueError, "Word not found"

#Average of the histogram

if __name__ == '__main__':
    # Reading text and making the word set
    alg = open('words_alg.txt', 'r')
    alg_text = alg.readlines()
    # word = str(raw_input()) This is if you want to find the number of times a specific word appears
    alg_word_set = []
    for line in alg_text:
        alg_word_set.extend(line.split())

    #Finding and printing the least frequent words
    sorted_set = sorted(histogram(), key=histogram().__getitem__)
    least_set = []
    for least in sorted_set:
        if histogram()[least] == histogram()[sorted_set[0]]:
            least_set.append(least)
    print("The least frequent words are " + str(least_set))

    #Finding and printing the  most frequent words
    most_set = []
    for most in sorted_set:
        if histogram()[most] == histogram()[sorted_set[-1]]:
            most_set.append(most)
    print("The most frequent words are " + str(most_set))

    #Printing the number of different words
    print("The number of distinct words are " + str(unique_words(histogram())))
