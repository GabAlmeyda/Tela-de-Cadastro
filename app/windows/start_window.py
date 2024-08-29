from tkinter import *  # type: ignore
from tkinter import ttk
from .window_interface import WindowInterface
from ..allFunctions.functions import Functions


class StartWindow(WindowInterface, Functions):

    def screen(self) -> None:
        self.root.title("NOME DA EMPRESA")
        self.root.configure(bg="#0d0d0d")
        self.root.resizable(False, False)
        self.root.geometry("691x585+300+50")

    def widgets(self) -> None:
        self._createButtons()
        self._createEntrys()
        self._createLabels()

    def _createButtons(self) -> None:
        self.enter_bt = Button(self.root, text="Entrar com sua conta")
        self.enter_bt.configure(bg="#8F00FF", font=(
            "Arial", 15, "bold"), fg="white", activebackground="#530391",
            activeforeground="white", bd=0)
        self.enter_bt.bind("<Enter>", self.focusIn)
        self.enter_bt.bind("<Leave>", self.focusOut)
        self.enter_bt.place(relx=0.2, rely=0.57, relwidth=0.6, relheight=0.1)

        self.enter_bt = Button(self.root, text="Cadastrar uma nova conta")
        self.enter_bt.configure(bg="#FF003D", font=(
            "Arial", 15, "bold"), fg="white", activebackground="#ab022a",
            activeforeground="white", bd=0)
        self.enter_bt.bind("<Enter>", self.focusIn)
        self.enter_bt.bind("<Leave>", self.focusOut)
        self.enter_bt.place(relx=0.2, rely=0.81, relwidth=0.6, relheight=0.1)

    def _createEntrys(self) -> None:
        pass

    def _createLabels(self) -> None:
        self.logo_lb = Label(self.root, text="Empresa")
        self.logo_lb.configure(bg="#0D0D0D", font=(
            "Times New Roman", 45, "bold"), fg="white")
        self.logo_lb.place(relx=0.325, rely=0.08, relwidth=0.35, relheight=0.13)

        self.enter_lb = Label(self.root, text="Já tem uma conta na Empresa?")
        self.enter_lb.configure(bg="#0d0d0d", font=(
            "Arial", 15, "bold"), fg="white")
        self.enter_lb.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.06)

        self.line_lb = Label(
            self.root, text="____________________________________________________________________________________________")
        self.line_lb.configure(bg="#0d0d0d", fg="white",
                               font=("verdana", 15, "bold"))
        self.line_lb.place(relx=0.15, rely=0.67, relwidth=0.7, relheight=0.05)

        self.enter_lb = Label(self.root, text="Ainda não fez sua conta?")
        self.enter_lb.configure(bg="#0d0d0d", font=(
            "Arial", 15, "bold"), fg="white")
        self.enter_lb.place(relx=0.25, rely=0.74, relwidth=0.5, relheight=0.06)
