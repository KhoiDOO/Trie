# from nltk.corpus import words
# from PyDictionary import PyDictionary
# import os
# import json
# from tqdm import tqdm

# word_lst = [x for x in words.words() if len(x) > 1]

# dictionary=PyDictionary()

# en_dict = {
    
# }

# for word in tqdm(word_lst):
#     try:
#         meaning = dictionary.meaning(word)
#         en_dict[word] = meaning
#     except Exception as e:
#         continue

# save_path = os.getcwd() + '/dict/data.json'

# with open(save_path, mode="w") as outfile:
#     outfile.write(json.dumps(en_dict, indent=4))