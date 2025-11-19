text = "hello world python"

words = []
word = ""

for ch in text:
    if ch != " ":
        word += ch
    else:
        words.append(word)
        word = ""
# append last word
words.append(word)

# reverse words
reversed_words = []
for i in range(len(words)-1, -1, -1):
    reversed_words.append(words[i])

result = ""

# join reversed words manually
for i in range(len(reversed_words)):
    result += reversed_words[i]
    if i != len(reversed_words) - 1:
        result += " "

print(result)
