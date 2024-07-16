from tkinter import *
from tkinter import ttk


class StartWindow:

    def __init__(self) -> None:
        self.root = Tk()
        self.screen()
        self.widgets()
        self.root.mainloop()

    def screen(self) -> None:
        self.root.title("Nome da Empresa")
        self.root.geometry("691x585+300+50")
        self.root.resizable(False, False)
        self.root.configure(bg="#0D0D0D")

    def widgets(self) -> None:
        self.logo = Label(self.root, text="Empresa")
        self.logo.configure(
            fg="white", background="#0D0D0D", font=("verdana", 25, "bold"))
        self.logo.place(relx=0.4, rely=0.1, relwidth=0.24, relheight=0.1)



if __name__ == "__main__":
    StartWindow()
