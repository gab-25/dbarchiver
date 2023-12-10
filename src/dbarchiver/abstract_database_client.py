from abc import ABC, abstractmethod


class AbstractDatabseClient(ABC):
    def __init__(self):
        self.check_dependencies()

    @abstractmethod
    def check_dependencies(self):
        pass

    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def restore(self):
        pass
