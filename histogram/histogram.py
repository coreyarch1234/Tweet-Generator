#Store all of the words into an array called, alg_word_set
alg = open('words_alg.txt', 'r')
alg_text = alg.readlines()
alg_word_set = []
for line in alg_text:
    alg_word_set.extend(line.split())
print(alg_word_set)
