from .window_interface import WindowInterface
from tkinter import *
from ..allFunctions.functions import Functions
from ..allFunctions.db_functions import DBManager
from ..custom_entrys import EntryPlaceHolder

class RegisterWindow(WindowInterface, Functions, DBManager):
    def screen(self) -> None:
        self.root.title("Empresa - Tela de Cadastro")
        self.root.configure(bg="#0D0D0D")
        self.root.resizable(False, False)
        self.root.geometry("691x585+300+50")

    def widgets(self) -> None:
        self._createButtons()
        self._createLabels()
        self._createEntrys()

    def _createButtons(self) -> None:
        self.bt_register = Button(self.root, text="Quero me inscrever!")
        self.bt_register.configure(bg="#FF003D", fg="white", font=("Arial", 15, "bold"), 
                                   activeforeground="white", activebackground="#ab022a", bd=0)
        self.bt_register.bind("<Enter>", self.focusIn)
        self.bt_register.bind("<Leave>", self.focusOut)
        self.bt_register.place(relx=0.25, rely=0.68, relwidth=0.5, relheight=0.07)

        self.bt_login = Button(self.root, text="Entrar com sua conta")
        self.bt_login.configure(bg="#8F00FF", fg="white", font=("Arial", 15, "bold"), 
                                activeforeground="white", activebackground="#530391", bd=0)
        self.bt_login.bind("<Enter>", self.focusIn)
        self.bt_login.bind("<Leave>", self.focusOut)
        self.bt_login.place(relx=0.325, rely=0.9, relwidth=0.35, relheight=0.07)

    def _createLabels(self) -> None:
        self.lb_logo = Label(self.root, text="Empresa")
        self.lb_logo.configure(bg="#0d0d0d", font=(
            "Times New Roman", 45, "bold"), fg="white")
        self.lb_logo.place(relx=0.05, rely=0.04, relwidth=0.35, relheight=0.13)

        terms = f"Se cadastrando na NOME-DA-EMPRESA, você está concordando \ncom os Termos de Serviço e os Termos de Coleta de Dados."
        self.lb_terms = Label(self.root, text=terms)
        self.lb_terms.configure(bg="#0d0d0d", font=(
            "Arial", 8, "bold"), fg="white")
        self.lb_terms.place(relx=0.25, rely=0.75, relwidth=0.5, relheight=0.07)

        self.lb_login = Label(self.root, text="Já tem uma conta?")
        self.lb_login.configure(bg="#0d0d0d", font=(
            "Arial", 13, "bold"), fg="white")
        self.lb_login.place(relx=0.373, rely=0.85, relwidth=0.27, relheight=0.05)

    def _createEntrys(self) -> None:
        self.et_name = EntryPlaceHolder(self.root, placeholder="Nome", highlightbg="white", highlightcolor="#FF003D")
        self.et_name.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.07)

        self.et_surname = EntryPlaceHolder(self.root, placeholder="sobrenome", highlightbg="white", highlightcolor="#FF003D")
        self.et_surname.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.07)

        self.et_email = EntryPlaceHolder(self.root, placeholder="email", highlightbg="white", highlightcolor="#FF003D")
        self.et_email.place(relx=0.1, rely=0.34, relwidth=0.8, relheight=0.07)

        self.et_password = EntryPlaceHolder(self.root, placeholder="senha", highlightbg="white", highlightcolor="#FF003D")
        self.et_password.bind("<FocusOut>", self.confirmPassword, add="+")
        self.et_password.place(relx=0.1, rely=0.47, relwidth=0.4, relheight=0.07)

        self.et_password2 = EntryPlaceHolder(self.root, placeholder="confirme sua senha", highlightbg="white", highlightcolor="#FF003D")
        self.et_password2.bind("<FocusOut>", self.confirmPassword, add="+")
        self.et_password2.place(relx=0.1, rely=0.56, relwidth=0.4, relheight=0.07)
