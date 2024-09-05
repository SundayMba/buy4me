from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def fetch_by_id(self):
        pass

    @abstractmethod
    def fetch_all(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass