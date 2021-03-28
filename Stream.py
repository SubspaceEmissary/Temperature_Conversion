from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod

class Stream(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def __init__(self):
        super().__init__()
        self._stream_type = "Filestream"
    
    def str_type(self):
        return self._stream_type
    
    def read(self):
        print("Reading filestream.")

class NetworkStream(Stream):
    def __init__(self):
        super().__init__()
        self._stream_type = "Networkstream"
    
    def str_type(self):
        return self._stream_type

    def read(self):
        print("Reading networkstream.")


stri = "w3resource"
dict1 = {item: stri.index(item) + 1 for item in stri}
print(dict1)

letters1 = "tqwreryuwfksdghjoerweiuqopwosmvmbsjfhqoiqwrpqwoumcvxwqriuiosm"
subletters1 = "er"

def func(letters, subletters):
    for item in letters:
        if subletters[0] == item:
            match1 = letters.index(item)
    if letters[match1 + 1] == subletters[1]:
        return f"Match at index {match1} to {match1 + 1}"
    else:
        return "No matches"

print(func(letters1, subletters1))

    




    
 