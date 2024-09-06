from tkinter import *  # type: ignore
from tkinter import ttk


class EntryPlaceHolder(Entry):

    def __init__(self, master=None, placeholder="INSERT YOUR PLACEHOLDER HERE", bg="#0D0D0D",
                 font=("Arial", 12, "bold"), fg="white", validate=None, validatecommand=None,
                 color="gray", bdwidth=0, highlightcolor="#8F00FF", highlightbg="white", 
                 highlightthick=1.7):
        super().__init__(master)

        self.estado = True

        self.placeholder = placeholder
        self.default_color = fg
        self.validate = validate
        self.validatecommand = validatecommand
        self.placeholder_color = color
        self["bg"] = bg
        self["font"] = font
        self["borderwidth"] = bdwidth
        self["highlightcolor"] = highlightcolor
        self["highlightbackground"] = highlightbg
        self["highlightthickness"] = highlightthick

        self.bind("<FocusIn>", self.foc_in, add="+")
        self.bind("<FocusOut>", self.foc_out, add="+")

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
        
