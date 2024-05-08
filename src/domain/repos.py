from abc import ABC, abstractmethod

from . import entities
from . import dtos


class UserRepo(ABC):
    @abstractmethod
    async def add(self, user: dtos.UserAdd) -> entities.User:
        raise NotImplementedError
    
    
    @abstractmethod
    async def find_by_email(self, email: str) -> entities.User | None:
        raise NotImplementedError