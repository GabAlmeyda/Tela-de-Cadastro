from tkinter import *
from .window_interface import WindowInterface

class AppWindow(WindowInterface):
    def screen(self) -> None:
        self.root.title("App Window")
        self.root.configure(bg="#0D0D0D")
        self.root.resizable(False, False)
        self.root.geometry("691x585+300+50")

    def widgets(self) -> None:
        pass

    def _createEntrys(self) -> None:
        pass

    def _createButtons(self) -> None:
        pass

    def _createLabels(self) -> None:
        pass


if __name__ == "__main__":
    AppWindow()