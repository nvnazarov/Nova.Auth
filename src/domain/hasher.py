from abc import ABC, abstractmethod


class Hasher(ABC):
    @abstractmethod
    def hash(value: str) -> str:
        pass
    
    
    @abstractmethod
    def verify(value: str, value_hash: str) -> bool:
        pass