def word_freq(sentence):
    sentence = sentence.lower()

    words = sentence.split()


    freq = {}

    for word in words:
        if word not in freq:
            freq[word]=1
        else:
            freq[word]+=1

    return freq

input = "the car and the hat"

ans = word_freq(input)
print(ans)