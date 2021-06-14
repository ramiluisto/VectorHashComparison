from array import array
import functools
import operator


class BaseVector:
    typecode = 'd'
    
    def __init__(self, iterable_input):
        self._components = array(self.typecode, iterable_input)

    def __iter__(self):
        return iter(self._components)

    def __eq__(self, other_vector):
        return tuple(self) == tuple(other_vector)

class SimpleVector(BaseVector):
    def __hash__(self):
        _ = hash(tuple(self._components))
        
        hash_collection = (hash(element) for element in self._components)
        return functools.reduce(operator.xor, hash_collection, 0)

    
class BetterVector(BaseVector):
    def __hash__(self):
        hash_collection = (hash(element) for element in self._components)
        _ = functools.reduce(operator.xor, hash_collection, 0)

        return hash(tuple(self._components))


    
