input_text = input("Enter your sentence")


def correct_sentence(text: str):
    text_by_words = text.split()

    first_word = text_by_words[0].capitalize()

    rest_of_sentence = ' '.join(text_by_words[1:])

    if not text.endswith('.'):
        corrected_sentence = f"{first_word} {rest_of_sentence}."
    else:
        corrected_sentence = f"{first_word} {rest_of_sentence}"

    return corrected_sentence


result = correct_sentence(input_text)
print(result)
