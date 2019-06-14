""" Singleton metaclass"""
from abc import ABCMeta, abstractmethod

class Singleton(type):
    _instances_ = {}
    def __call__(cls, *args, **kwargs):
        """
        overrides instance creation.
        if a instance was created before, this instance is returned instead of creating a new one.
        """
        if cls not in cls._instances_:
            cls._instances_[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances_[cls]


class Repository(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        raise NotImplementedError
    @abstractmethod
    def remove(self, entity):
        raise NotImplementedError
    @abstractmethod
    def update(self, entity):
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError
    @abstractmethod
    def list_all(self):
        raise NotImplementedError

