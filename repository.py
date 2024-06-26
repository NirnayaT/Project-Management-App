from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    Adding Repository Layer between database interface and main interface
    """

    @abstractmethod
    def get(self):
        raise NotImplementedError()

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def remove(self, unique_id: int):
        raise NotImplementedError()


class AbstractRepositoryForUser(ABC):
    """
    Adding Repository Layer between user interface and main interface
    """

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError()
