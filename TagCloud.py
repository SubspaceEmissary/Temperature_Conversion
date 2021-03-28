from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty

class Stream(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read(self, streamtype):
        pass

class FileStream(Stream):
    pass 

class NetworkStream(Stream): 
    pass
