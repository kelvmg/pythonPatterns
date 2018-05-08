#Prototype_1 class
from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass

#Concrete class
class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)
