from abc import ABC, abstractmethod
from tkinter import Tk

class WindowInterface(ABC):
    def __init__(self) -> None:
        self.root = Tk()
        self.screen()
        self.widgets()

    @abstractmethod
    def screen(self) -> None:
        """
            Deve conter os comandos para configurações da tela, como tamanho, fundo, título etc.
        """
        raise Exception("Deve ser implementado o método 'screen'")
    
    @abstractmethod
    def widgets(self) -> None:
        """
            Deve reunir todos os comandos para os widgets da tela, com labels, entrys, botões etc. Preferencialmente, esse método deve
        apenas executar os métodos "createLabels", "createButtons" e "createEntrys".
        """
        self._createButtons()
        self._createEntrys()
        self._createLabels()
        raise Exception("Deve ser implementado o método 'widgets'")
    
    @abstractmethod
    def _createLabels(self) -> None:
        """
            Este método reúne toda a criação de labels que a janela terá.
        """
        raise Exception("Deve ser implementado o método 'createLabels'")
    
    @abstractmethod
    def _createEntrys(self) -> None:
        """
            Este método reúne toda a criação de entrys que a janela terá.
        """
        raise Exception("Deve ser implementado o método 'createEntrys'")
    
    @abstractmethod
    def _createButtons(self) -> None:
        """
            Este método reúne toda a criação de botões que a janela terá.
        """
        raise Exception("Deve ser implementado o método 'createButtons'")
    
    def run(self) -> None:
        self.root.mainloop()
    
