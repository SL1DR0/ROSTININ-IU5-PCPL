from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def square(self):
        """Виртуальный метод для вычисления площади"""
        pass
