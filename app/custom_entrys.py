from tkinter import *
from tkinter import ttk

class PlaceHolder(Entry):

    def __ini__(self, master=None, placeholder="INSERT YOUR PLACEHOLDER HERE", bg="#0D0D0D", 
                font=("verdana", 8, "bold"), fg="white", validate="key", validatecommand="", 
                color="light gray"):
        super().__init__(master)
        self.placeholder = placeholder
        self.default_color = fg
        self.validate = validate
        self.validatecommand = validatecommand
        self.placeholder_color = color
        self["bg"] = bg
        self["font"] = font
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()
        self.estado = True

    def foc_in(self) -> None:
        if self.estado:
            self.delete(0, END)
            self["fg"] = self.default_color
            self["validate"] = self.validate
            self["validatecommand"] = self.validatecommand
            self.estado = False

    def foc_out(self) -> None:
        if not self.get():
            self.put_placeholder()
            self.estado = True

    def put_placeholder(self) -> None:
        self["validate"] = None
        self["validatecommand"] = None
        self["fg"] = self.placeholder_color
        self.insert(0, self.placeholder)
        self.estado = True
