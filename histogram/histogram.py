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

if __name__ == '__main__':
    # histogram()
    # print(unique_words(histogram()))
    alg = open('words_alg.txt', 'r')
    alg_text = alg.readlines()
    word = str(raw_input())
    alg_word_set = []
    
    for line in alg_text:
        alg_word_set.extend(line.split())
    print specific_word_count(word, histogram())
