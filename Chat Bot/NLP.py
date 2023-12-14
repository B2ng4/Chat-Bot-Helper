from transformers import AutoModel, AutoTokenizer
import torch
import numpy as np
from scipy.spatial.distance import cosine

# Initialize model and tokenizer once
model_name = "cointegrated/rubert-tiny"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


sem =[]
def compute_embeddings(sentences):
    encoded_input = tokenizer(sentences, padding=True, return_tensors='pt')
    with torch.no_grad():
        embeds = model(**encoded_input).last_hidden_state.mean(dim=1)
    return embeds.cpu().numpy()

sent = []
# Pre-compute embeddings for the sentences in data.txt
with open("data.txt") as f:
    sentences = f.readlines()
    for i in  sentences:
        sentence = i.split("%")[1]
        sent.append(sentence)

precomputed_embeddings = compute_embeddings(sent)

def bert_semantic_similarity(new_sentence, precomputed_embeddings=precomputed_embeddings):
    new_embed = compute_embeddings([new_sentence])[0]
    similarities = [1 - cosine(new_embed, pre_embed) for pre_embed in precomputed_embeddings]
    dictionary = {i: x for i, x in zip(sentences, similarities)}
    key_with_max_value = max(dictionary, key=dictionary.get)
    link = (str(key_with_max_value).split("%"))[2]
    return "https://www.xn----7sbab7amcgekn3b5j.xn--p1ai"+link





