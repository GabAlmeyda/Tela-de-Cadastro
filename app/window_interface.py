from abc import ABC, abstractmethod
from tkinter import Tk

class WindowInterface(ABC):
    def __init__(self) -> None:
        self.root = Tk()

    @abstractmethod
    def screen(self) -> None:
        """
        It should contain commands for screen settings, such as size, background, title etc.
        """
        pass
    
    @abstractmethod
    def widgets(self) -> None:
        """
        Must bring together all commands for screen widgets, such as labels, entrys, buttons etc. Preferably, this method should just run the methods ""_createLabels", "_createButtons" and "_createEntrys".  
        """
        pass
    
    @abstractmethod
    def _createLabels(self) -> None:
        """
        This method brings together all the labels that the window will have.
        """
        pass
    
    @abstractmethod
    def _createEntrys(self) -> None:
        """
        This method brings together all the entrys that the window will have.
        """
    pass

    @abstractmethod
    def _createButtons(self) -> None:
        """
        This method brings together all the buttons that the window will have.
        """
    pass  

    def run(self) -> None:
        self.root.mainloop()
    
