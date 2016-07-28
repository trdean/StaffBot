import json,random

word_list = "words.json"
word_file = open(word_list)
j = json.load(word_file)

def pick_word(node_type):
    return random.choice(j[node_type])
