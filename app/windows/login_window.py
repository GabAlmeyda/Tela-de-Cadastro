from tkinter import *  # type: ignore
from .window_interface import WindowInterface
from ..allFunctions.functions import Functions
from ..allFunctions.db_functions import DBManager
from ..custom_entrys import EntryPlaceHolder


class LoginWindow(WindowInterface, Functions, DBManager):

    def screen(self) -> None:
        self.root.title("Empresa - Tela de Login")
        self.root.configure(bg="#0D0D0D")
        self.root.resizable(False, False)
        self.root.geometry("691x585+300+50")

    def widgets(self) -> None:
        self._createLabels()
        self._createEntrys()
        self._createButtons()
        
    def _createLabels(self):
        self.logo_lb = Label(self.root, text="Empresa")
        self.logo_lb.configure(bg="#0d0d0d", font=(
            "Times New Roman", 45, "bold"), fg="white")
        self.logo_lb.place(relx=0.05, rely=0.04, relwidth=0.35, relheight=0.13)

    def _createButtons(self) -> None:
        self.bt_continue = Button(self.root, text="Continuar", command=self.loginAction)
        self._releaseButtonLogin()
        self.bt_continue.configure(font=("Arial", 15, "bold"), fg="white", )
        self.bt_continue.bind("<Enter>", self.focusIn)
        self.bt_continue.bind("<Leave>", self.focusOut)
        self.bt_continue.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.07)
    
    def _createEntrys(self) -> None:
        self.et_email = EntryPlaceHolder(self.root, placeholder="Digite seu email")
        self.et_email.bind("<KeyRelease>", self._releaseButtonLogin)
        self.et_email.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.07)

        self.et_password = EntryPlaceHolder(self.root,  placeholder="Digite sua senha")
        self.et_password.bind("<KeyRelease>", self._releaseButtonLogin)
        self.et_password.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.07)


if __name__ == "__main__":
    LoginWindow()
