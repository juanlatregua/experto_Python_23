from abc import ABC
from abc import abstractmethod

class ReusableObject(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def reset(self):
        pass

class Pool:

    def __init__(self, slice_size, class_name, resizable = True):
        self.__slice = slice_size
        self.__class_name = class_name
        self.__resizable = resizable
        self.__pool = [self.__class_name() for _ in range(self.__slice)]

    def acquire(self):
        if len(self.__pool) <= 0:
            if self.__resizable:
                self.__pool += [self.__class_name() for _ in range(self.__slice)]
            else:
                raise Exception(f'Pool for {self.__class_name} exhausted')

        pool_object = self.__pool.pop()
        pool_object.reset()
        return pool_object

    def release(self, pool_object):
        self.__pool.append(pool_object)