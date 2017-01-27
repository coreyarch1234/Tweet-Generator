#Store all of the words into an array called, alg_word_set
alg = open('words_alg.txt', 'r')
alg_text = alg.readlines()
alg_word_set = []
for line in alg_text:
    alg_word_set.extend(line.split())

def histogram():
    new_word_dict = {}
    for key_word in alg_word_set:
        if key_word in new_word_dict:
            new_word_dict[key_word] += 1
        else:
            new_word_dict[key_word] = 1
    return new_word_dict

def unique_words(histogram_input):
    unique_total_count = 0
    return len(histogram_input.keys())


if __name__ == '__main__':
    histogram()
    print(unique_words(histogram()))
