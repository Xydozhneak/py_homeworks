import string

user_input = input("Enter your words: ")
words = user_input.split()
hashtag_words = [word.title() for word in words]
hashtag = "".join(hashtag_words)
hashtag = "#" + "".join(char for char in hashtag if char.isalnum())
hashtag = hashtag[:140]
print(hashtag)
