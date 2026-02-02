import nltk
nltk.download('punkt')
text = "I Love Pizza!"
tokens = nltk.word_tokenize(text)
print(tokens)