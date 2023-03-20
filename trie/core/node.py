class BaseNode:
    def __init__(self, size: int = None) -> None:
        self.__size = size
        self.__check_size(size=size)
        self.__key = [None]*self.__size
        self.__terminal = False
        
    def __getitem__(self, index:int = None):
        raise NotImplementedError
    
    def __setitem__(self, index:int = None, node = None):
        raise NotImplementedError
    
    def __check_size(self, size:int):
        if size is None:
            raise Exception("size arg cannot be None")
        elif not isinstance(size, int):
            raise TypeError(f"size arg must be bool but found {type(size)} instead")

    def __check_term(self, term:bool):
        if term is None:
            raise Exception("term arg cnnot be None")
        elif not isinstance(term, bool):
            raise TypeError(f"term arg must be bool but found {type(term)} instead")
    
    def get_size(self) -> int:
        return self.__size
    
    def set_size(self, size: int = None):
        self.__check_size(size=size)
        self.__size = size
    
    def get_term(self) -> bool:
        return self.__terminal
    
    def set_term(self, term:bool = None):
        self.__check_term(term=term)
        self.__terminal = term

class Node(BaseNode):
    def __init__(self, size: int = None) -> BaseNode:
        super().__init__(size)
    
    def __getitem__(self, index:int = None) -> BaseNode or None:
        self.__check_index(index=index)
        return self._BaseNode__key[index]
    
    def __setitem__(self, index:int, node: BaseNode):
        self.__check_index(index=index)
        self.__check_node(node=node)
        self._BaseNode__key[index] = node
    
    def __check_node(self, node: BaseNode = None):
        if node is None:
            raise Exception("node arg cannot be None")
        elif not isinstance(node, Node):
            raise TypeError(f"node must have Node type but found {type(node)} instead")
    
    def __check_index(self, index):
        if index is None:
            raise Exception("index arg cannot be None")
        elif not isinstance(index, int):
            raise TypeError(f"index arg must be an integer but found {type(index)} instead")
        elif not 0 <= index <= len(self._BaseNode__key) - 1:
            raise IndexError("index is out of range")
        
        
class StringLowerNode(Node):
    def __init__(self, size: int = 26) -> None:
        self.__check_size(size=size)
        super().__init__(size)
    
    def __check_size(self, size: int):
        if size is None:
            raise Exception("size arg cannot be None")
        elif not isinstance(size, int):
            raise TypeError(f"size arg must be bool but found {type(size)} instead")
        elif size != 26:
            raise Exception("size must be 26 in StringLowerNode")

class StringNode(Node):
    def __init__(self, size: int = None) -> BaseNode:
        super().__init__(size)
        
        hash_char = {
            
        }
        
    def __check_size(self, size: int):
        if size is None:
            raise Exception("size arg cannot be None")
        elif not isinstance(size, int):
            raise TypeError(f"size arg must be bool but found {type(size)} instead")
        elif size != 26:
            raise Exception("size must be 26 in StringLowerNode")

class DictNode(StringLowerNode):
    def __init__(self, size: int = 26, definition:str = None) -> BaseNode:
        self.__definition = definition
        super().__init__(size)
    
    def __check_def(self, definition: str = None):
        if not isinstance(definition, str):
            raise TypeError(f"definition arg must be string object. but found {type(definition)} instead")
    
    def set_def(self, definition: str = None):
        self.__check_def(definition=definition)
        self.__definition = definition
    
    def get_def(self):
        return self.__definition