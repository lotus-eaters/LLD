# This principle is the first principle that applies to Interfaces instead of classes in SOLID and 
# it is similar to the single responsibility principle. It states that "do not force any client to "
# "implement an interface which is irrelevant to them". Here your main goal is to focus on avoiding 
# fat interface and give preference to many small client-specific interfaces. You should prefer many 
# client interfaces rather than one general interface and each interface should have a specific 
# responsibility.
from abc import ABC,abstractmethod
class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class Faxable(ABC):
    @abstractmethod
    def fax_document(self):
        pass


class AllInOnePrinter(Printable, Scannable, Faxable):
    def print_document(self):
        print("Printing...")
    
    def scan_document(self):
        print("Scanning...")
    
    def fax_document(self):
        print("Faxing...")


class SimplePrinter(Printable):
    """Only implements printing - honest about capabilities!"""
    def print_document(self):
        print("Printing...")
