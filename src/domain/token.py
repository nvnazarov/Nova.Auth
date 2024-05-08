from abc import ABC, abstractmethod

from . import entities


class AccessTokenContext(ABC):
    @abstractmethod
    def generate(self, user: entities.User) -> str:
        raise NotImplementedError
    

class RefreshTokenContext(ABC):
    @abstractmethod
    def generate(self, user: entities.User) -> str:
        raise NotImplementedError