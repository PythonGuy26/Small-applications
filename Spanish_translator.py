def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    first_sentence = sentence.split(" ")
    new_sentence = []
    for word in first_sentence:
        for key in words:
            if key == word:
                new_sentence.append(words[key])
    return " ".join(new_sentence)


print(translate("el gato esta en la casa"))
# output: the cat is in the house
