#Store all of the words into an array called, alg_word_set

def read_in(text):
    # Reading text and making the word set
    alg = open(text, 'r')
    alg_text = alg.readlines()
    # word = okstr(raw_input()) This is if you want to find the number of times a specific word appears
    alg_word_list = []
    for line in alg_text:
        alg_word_list.extend(line.split())
    return alg_word_list

def histogram(word_list):
    new_word_dict = {}
    for key_word in word_list:
        if key_word in new_word_dict: #If that word exists in the set
            new_word_dict[key_word] += 1 #Increment the count value
        else:
            new_word_dict[key_word] = 1 #Initialize it with a value
    return new_word_dict

def unique_words(histogram_input):
    return len(histogram_input.keys())

def specific_word_count(word, histogram_input):
    if word in histogram_input:
        return histogram_input[word]
    else:
        raise 0

#Average of the histogram. The mean is the sum of the number of all of the occurances divided by the number of unique words
def mean(histogram_input):
    sum = 0.0
    unique_count = unique_words(histogram_input)
    for key,value in histogram_input.iteritems():
        sum += value
    return (sum/unique_count)

#Find the median. First, sum all of the occurances, and then divide by 2, and then find the words that correspond with that frequency
def median(histogram_input):
    sum = mean(histogram_input) * unique_words(histogram_input)
    median_value = sum / 2.0
    count = 0 #keep track of the word values until it reaches the median
    print("The median value is " + str(median_value))
    median_array = []
    for key,value in histogram_input.iteritems():
        count += value
        if count == value :
            # print(count)
            median_array.append(key)
    return(median_array)


if __name__ == '__main__':
    histogram = histogram(read_in("words_alg.txt"))
    #Finding and printing the least frequent words
    sorted_set = sorted(histogram, key=histogram.__getitem__)
    least_set = []
    for least in sorted_set:
        if histogram[least] == histogram[sorted_set[0]]:
            least_set.append(least)
    print("The least frequent words are " + str(least_set))

    #Finding and printing the  most frequent words
    most_set = []
    for most in sorted_set:
        if histogram[most] == histogram[sorted_set[-1]]:
            most_set.append(most)
    print("The most frequent words and the modes are " + str(most_set))

    #Printing the number of different words
    print("The number of distinct words are " + str(unique_words(histogram)))

    #Printing the mean
    print("The mean of all of the words is " + str(mean(histogram)))

    #Printing the median of the words
    print("The median of all of the words is " + str(median(histogram)))
