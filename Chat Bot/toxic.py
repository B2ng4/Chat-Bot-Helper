
from better_profanity import profanity

def insult():
    custom_bad_words = ["дурак", "badword2", "badword3"]
    profanity.load_censor_words(custom_bad_words)
    return profanity.load_censor_words(custom_bad_words)
