from tkinter import *  # type: ignore
from tkinter import ttk


class EntryPlaceHolder(Entry):

    def __init__(self, master=None, placeholder="INSERT YOUR PLACEHOLDER HERE", bg="white",
                 font=("verdana", 8, "bold"), fg="black", validate=None, validatecommand=None,
                 color="gray"):
        super().__init__(master)
        self.estado = True
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
        

    def foc_in(self, *args) -> None:
        if self.estado:
            self.estado = False
            self.delete(0, END)
            self["fg"] = self.default_color
            self["validate"] = self.validate
            self["validatecommand"] = self.validatecommand
            

    def foc_out(self, *args) -> None:
        if not self.get():
            self.put_placeholder()

    def put_placeholder(self) -> None:
        self.estado = True
        self["validate"] = None
        self["validatecommand"] = None
        self["fg"] = self.placeholder_color
        self.insert(0, self.placeholder)
        
