

from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


def toxi(message):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    message = message
    results = model.predict(message, k = 2)[0]
    max_key = max(results, key=results.get)
    return str(max_key)
