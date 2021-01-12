from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def user_output(self, info: any):
        pass

    @abstractmethod
    def user_input(self, question: str):
        pass


class ConsoleInterface(Interface):
    def user_output(self, info: any):
        print(info)

    def user_input(self, question: str):
        return input(question)

