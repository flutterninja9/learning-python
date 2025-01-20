poem = open("robert_frost_poem.txt", "r")
poem_lines = poem.readlines()
word_counter = {}

for line in poem_lines:
    words = line.split(" ")
    for word in words:
        clean_word = word.replace("\n", "").replace(",", "").replace(".", "").replace("!", "").replace(" ", "")
        if word_counter.__contains__(clean_word):
            count = word_counter[clean_word]
            word_counter[clean_word] =  count + 1
        else:
            word_counter[clean_word] = 1

for val in word_counter:
    print(val, word_counter[val])
poem.close()