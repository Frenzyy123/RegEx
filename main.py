import re

sentence = "I love python"
print(re.match("^[a-zA-Z ]+$",sentence))
importantSentence = "Today will rain"
if re.match(r"^[A-Z]",importantSentence):
    print("Recenica pocinje velikim slovom")
else:
    print("Recenica ne pocinje velikim slovom")
