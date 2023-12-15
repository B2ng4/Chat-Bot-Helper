
from better_profanity import profanity

def insult(text_to_check):
    with open('DATA_INSULT.txt', 'r') as file:
        custom_bad_words = file.read().splitlines()
    profanity.load_censor_words(custom_bad_words)
    return profanity.contains_profanity(text_to_check)