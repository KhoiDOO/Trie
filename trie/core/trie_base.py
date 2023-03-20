import os, sys
sys.path.append(os.getcwd())

from trie.core.node import *

class BaseTrie:
    def __init__(self) -> None:
        self.__root = self.__get_node()
    
    def __get_node(self):
        return StringLowerNode(size=26)
    
    def __call__(self, word: str = None):
        self.__check_word(word=word)
        
        pointer = self.__root
        base_len = len(word)
        
        for level in range(base_len):
            idx  = self.__char2index(char=word[level])
            
            if not pointer[idx]:
                pointer[idx] = self.__get_node()
            pointer = pointer[idx]
        pointer.set_term(term=True)
    
    def __getitem__(self, word: str = None):
        self.__check_word(word=word)
        pointer = self.__root
        
        base_len = len(word)
        
        for level in range(base_len):
            idx = self.__char2index(char=word[level])
            
            if not pointer[idx]:
                return False
            pointer = pointer[idx]
        return pointer.get_term()

    def __contains__(self, word: str = None):
        self.__check_word(word=word)
        return self[word]
    
    def __iter__(self):
        raise NotImplementedError
    
    def __char2index(self, char: str = None):
        self.__check_char(char=char)
        
        return ord(char)-ord('a')
        
    def __check_char(self, char: str = None):
        if char is None:
            raise Exception("char cannot be None")
        elif not isinstance(char, str):
            raise TypeError(f"exptected arg char with type of string but found {type(char)} instead")
        elif len(char) > 1:
            raise Exception(f"char must be a character but found length of {len(char)}")
    
    def __check_word(self, word: str = None):
        if word is None:
            raise Exception("char cannot be None")
        elif not isinstance(word, str):
            raise TypeError(f"exptected arg char with type of string but found {type(word)} instead")
        elif len(word) <= 1:
            raise Exception(f"word must be a single word not char but found length of {len(word)}")
        elif " " in word:
            raise Exception(f"word must be a single word not compund word")
        
if __name__ == "__main__":
    trie = BaseTrie()
    
    keys = ["the","there","anaswe","any",
            "by","their"]
    
    for key in keys:
        trie(key)
        
    print("{} ---- {}".format("the", "the" in trie))
    print("{} ---- {}".format("these", "these" in trie))
    print("{} ---- {}".format("their", "their" in trie))
    print("{} ---- {}".format("thaw", "thaw" in trie))