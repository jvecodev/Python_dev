from abc import ABC, abstractmethod

class Animal(ABC):  
    """
        Serve como um contrato,
        toda subclasse tem que herdar
        este método e implementá-lo.
    """
    @abstractmethod #Decorator

    def fazer_som(self):  
        pass
