import os, sys
sys.path.append(os.getcwd())

import json

from trie.core.trie_base import BaseTrie
from trie.core.node import *

from nltk.corpus import words
from random import randint, shuffle

class DictTrie(BaseTrie):
    def __init__(self, dict_path: str = None) -> None:
        super().__init__()
        
        self.__root = self.__get_node()
        
        if dict_path:
            self.__dict_path = dict_path
        else:
            self.__dict_path = os.getcwd() + "/dict/simple_english_dictionary.json"
        
        self.__en_dict = json.load(open(self.__dict_path, mode="r"))
        
        self.__load_dict_trie()
    
    def __get_node(self) -> DictNode:
        return DictNode()
        
    def get_dict(self) -> dict:
        return self.__en_dict
    
    def __load_dict_trie(self):
        for key in self.__en_dict:
            try:
                self(word = key, definition = self.__en_dict[key])
            except Exception as e:
                print(f"Error: {e}")
                print(f"Sample catched: {key}")
                continue
    
    def __getitem__(self, word: str = None):
        self._BaseTrie__check_word(word=word)
        pointer = self.__root
        
        base_len = len(word)
        
        for level in range(base_len):
            idx = self._BaseTrie__char2index(char=word[level].lower())
            
            if not pointer[idx]:
                return None
            pointer = pointer[idx]
        return pointer.get_def()
    
    def __call__(self, word: str = None, definition: str = None):
        self._BaseTrie__check_word(word=word)
        
        pointer = self.__root
        base_len = len(word)
        
        for level in range(base_len):
            idx  = self._BaseTrie__char2index(char=word[level].lower())
            
            if not pointer[idx]:
                pointer[idx] = self.__get_node()
            pointer = pointer[idx]
        pointer.set_term(term=True)
        pointer.set_def(definition=definition)
    
    def __contains__(self, word: str = None):
        self._BaseTrie__check_word(word=word)
        return self[word] is not None

if __name__ == "__main__":
    dict_trie = DictTrie(dict_path=os.getcwd() + "/dict/simple_english_dictionary.json")
    
    base_lst = [x for x in words.words() if len(x) > 1 and len(x.split(" ")) == 1 and "-" not in x]

    dict_lst = [x for x in list(dict_trie.get_dict().keys()) if " " not in x and "-" not in x]
    
    rand1 = randint(0, len(base_lst)-30)
    rand2 = randint(0, len(dict_lst)-30)
    
    sample_lst = base_lst[rand1:rand1+30] + dict_lst[rand2:rand2+30]
    
    shuffle(sample_lst)
    
    for sample in sample_lst:
        print(f"WORD: {sample}", end=" ")
        print(f"-- DEFINITION: {dict_trie[sample]}")