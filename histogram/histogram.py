#Store all of the words into an array called, alg_word_set
alg = open('words_alg.txt', 'r')
alg_text = alg.readlines()
alg_word_set = []
for line in alg_text:
    alg_word_set.extend(line.split())

def give_default_value():
    word_dict = {}
    for key_word in alg_word_set:
        word_dict[key_word] = 0
    return word_dict

def histogram():
    new_word_dict = give_default_value()
    for key_word in alg_word_set:
        new_word_dict[key_word] += 1
    return new_word_dict

def unique_words(histogram_input):
    unique_total_count = 0
    for key,value in histogram_input.items():
        # print("Key : {0}, Value : {1}".format(key, value))
        if value == 1:
            # print("HOORAYYYYYYY")
            unique_total_count += 1
    return unique_total_count


if __name__ == '__main__':
    histogram()
    print(unique_words(histogram()))
