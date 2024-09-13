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
<<<<<<< HEAD
        pass
=======
        pass
>>>>>>> cc2897fa456fcb43ea70282428f49afbf6a9314d
