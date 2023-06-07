def longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = longest_word(["ball", "applications", "packup"])
print("\nLongest word: ",result[1])
print("\nLength of the longest word: ",result[0])

