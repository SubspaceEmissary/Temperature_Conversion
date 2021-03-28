from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty

class Stream(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read(self, streamtype):
        pass

class FileStream(Stream):
    def __init__(self):
        super.__init__
        

class NetworkStream(Stream): 
    pass

dic1 = {}