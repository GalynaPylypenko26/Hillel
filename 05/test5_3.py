import string
input_string = input("Будь ласка, введіть рядок: ")
# Видаляємо всі знаки пунктуації
cleaned_string = ""
for symbol in input_string:
    if symbol not in string.punctuation:
        cleaned_string += symbol
words = cleaned_string.split()
capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())
hashtag = '#' + ''.join(capitalized_words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)