def popular_words():
    text = input("Enter your text: ")

    words_input = input("Enter words for search separate by space: ").lower().split()

    text_words = text.lower().split()

    word_count = {word: text_words.count(word) for word in words_input}

    return word_count


result = popular_words()

print(result)
