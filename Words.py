#Liste des mots positifs et négatifs, respectivement positive_words et negative_words

from textblob import TextBlob

positive_words = TextBlob("Good healthy useful")
print(positive_words.words)



