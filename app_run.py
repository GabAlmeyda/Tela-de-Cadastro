from tkinter import *
from app import WindowInterface
from app import EntryPlaceHolder
from app.allFunctions.functions import Functions
from app.allFunctions.db_functions import DBManager


class AppManager:
    def __init__(self) -> None:
        start = StartWindow()
        start.run()

    @staticmethod
    def changeWindow(actual_window: WindowInterface, new_window: WindowInterface):
        actual_window.destroy()
        new_window.run()


# start of the class "StartWindow"
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
        self.bt_login = Button(self.root, text="Entrar com sua conta",
                               command=lambda: AppManager.changeWindow(
                                   actual_window=self.root, new_window=LoginWindow()))
        self.bt_login.configure(bg="#8F00FF", font=(
            "Arial", 15, "bold"), fg="white", activebackground="#530391",
            activeforeground="white", bd=0)
        self.bt_login.bind("<Enter>", self.focusIn)
        self.bt_login.bind("<Leave>", self.focusOut)
        self.bt_login.place(relx=0.2, rely=0.57, relwidth=0.6, relheight=0.1)

        self.bt_register = Button(self.root, text="Cadastrar uma nova conta",
                                  command=AppManager.changeWindow(
                                      actual_window=self.root, new_window=RegisterWindow()))
        self.bt_register.configure(bg="#FF003D", font=(
            "Arial", 15, "bold"), fg="white", activebackground="#ab022a",
            activeforeground="white", bd=0)
        self.bt_register.bind("<Enter>", self.focusIn)
        self.bt_register.bind("<Leave>", self.focusOut)
        self.bt_register.place(relx=0.2, rely=0.81,
                               relwidth=0.6, relheight=0.1)

    def _createEntrys(self) -> None:
        pass

    def _createLabels(self) -> None:
        self.lb_logo = Label(self.root, text="Empresa")
        self.lb_logo.configure(bg="#0D0D0D", font=(
            "Times New Roman", 45, "bold"), fg="white")
        self.lb_logo.place(relx=0.325, rely=0.08,
                           relwidth=0.35, relheight=0.13)

        self.lb_enter = Label(self.root, text="Já tem uma conta na Empresa?")
        self.lb_enter.configure(bg="#0d0d0d", font=(
            "Arial", 15, "bold"), fg="white")
        self.lb_enter.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.06)

        self.lb_line = Label(
            self.root, text=("_" * 92))
        self.lb_line.configure(bg="#0d0d0d", fg="white",
                               font=("verdana", 15, "bold"))
        self.lb_line.place(relx=0.15, rely=0.67, relwidth=0.7, relheight=0.05)

        self.lb_register = Label(self.root, text="Ainda não fez sua conta?")
        self.lb_register.configure(bg="#0d0d0d", font=(
            "Arial", 15, "bold"), fg="white")
        self.lb_register.place(relx=0.25, rely=0.74,
                               relwidth=0.5, relheight=0.06)
# End of the class "StartWindow"


# Start of the class "RegisterWindow"
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
        self.bt_register = Button(
        # TODO: colocar o comando de trocar de janela
            self.root, text="Quero me inscrever!", command=self.registerAction)
        self.bt_register.configure(bg="#FF003D", fg="white", font=("Arial", 15, "bold"),
                                   activeforeground="white", activebackground="#ab022a", bd=0)
        self.bt_register.bind("<Enter>", self.focusIn)
        self.bt_register.bind("<Leave>", self.focusOut)
        self.bt_register.place(relx=0.25, rely=0.68,
                               relwidth=0.5, relheight=0.07)

        self.bt_login = Button(self.root, text="Entrar com sua conta", 
                               command=AppManager.changeWindow(
                                actual_window=self.root, new_window=LoginWindow()))
        self.bt_login.configure(bg="#8F00FF", fg="white", font=("Arial", 15, "bold"),
                                activeforeground="white", activebackground="#530391", bd=0)
        self.bt_login.bind("<Enter>", self.focusIn)
        self.bt_login.bind("<Leave>", self.focusOut)
        self.bt_login.place(relx=0.325, rely=0.9,
                            relwidth=0.35, relheight=0.07)

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
        self.lb_login.place(relx=0.373, rely=0.85,
                            relwidth=0.27, relheight=0.05)

    def _createEntrys(self) -> None:
        self.et_name = EntryPlaceHolder(
            self.root, placeholder="Nome", highlightbg="white", highlightcolor="#FF003D")
        self.et_name.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.07)

        self.et_surname = EntryPlaceHolder(
            self.root, placeholder="sobrenome", highlightbg="white", highlightcolor="#FF003D")
        self.et_surname.place(relx=0.5, rely=0.25,
                              relwidth=0.4, relheight=0.07)

        self.et_email = EntryPlaceHolder(
            self.root, placeholder="email", highlightbg="white", highlightcolor="#FF003D")
        self.et_email.place(relx=0.1, rely=0.34, relwidth=0.8, relheight=0.07)

        self.et_password = EntryPlaceHolder(
            self.root, placeholder="senha", highlightbg="white", highlightcolor="#FF003D")
        self.et_password.bind("<FocusOut>", self.confirmPassword, add="+")
        self.et_password.place(relx=0.1, rely=0.47,
                               relwidth=0.4, relheight=0.07)

        self.et_password2 = EntryPlaceHolder(
            self.root, placeholder="confirme sua senha", highlightbg="white", highlightcolor="#FF003D")
        self.et_password2.bind("<FocusOut>", self.confirmPassword, add="+")
        self.et_password2.place(relx=0.1, rely=0.56,
                                relwidth=0.4, relheight=0.07)
# End of the class "RegisterWindow"


# Start of the class "LoginWindow"
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
        self.lb_logo = Label(self.root, text="Empresa")
        self.lb_logo.configure(bg="#0d0d0d", font=(
            "Times New Roman", 45, "bold"), fg="white")
        self.lb_logo.place(relx=0.05, rely=0.04, relwidth=0.35, relheight=0.13)

    def _createButtons(self) -> None:
        self.bt_continue = Button(
        # TODO: colocar o comando de mudar a janela
            self.root, text="Continuar", command=self.loginAction)
        self._releaseButtonLogin()
        self.bt_continue.configure(font=("Arial", 15, "bold"), fg="white", )
        self.bt_continue.bind("<Enter>", self.focusIn)
        self.bt_continue.bind("<Leave>", self.focusOut)
        self.bt_continue.place(relx=0.25, rely=0.6,
                               relwidth=0.5, relheight=0.07)

    def _createEntrys(self) -> None:
        self.et_email = EntryPlaceHolder(
            self.root, placeholder="Digite seu email")
        self.et_email.bind("<KeyRelease>", self._releaseButtonLogin)
        self.et_email.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.07)

        self.et_password = EntryPlaceHolder(
            self.root,  placeholder="Digite sua senha")
        self.et_password.bind("<KeyRelease>", self._releaseButtonLogin)
        self.et_password.place(relx=0.25, rely=0.4,
                               relwidth=0.5, relheight=0.07)
# End of the class "LoginWindow"


# Start of the class "AppWindow"
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
# End of the class "AppWindow"


if __name__ == "__main__":
    AppManager()
