from tkinter import * # type: ignore
from ..custom_entrys import EntryPlaceHolder

class Functions:

    def __init__(self) -> None:
        self.et_email: EntryPlaceHolder
        self.et_password: EntryPlaceHolder
        self.bt_continue: Button

    # Key: color's name, values order: lighter color; darker color.
    colors: dict[str, tuple] = {
            "purple": ("#8F00FF", "#7202c9"),
            "pink": ("#FF003D", "#d40234")
        }

    def focusIn(self, event) -> None:
        """
        Changes the background color's of the button when it receives focus, based on the color tuple from the color dictionary.
        """
        color = self._selectColor(event.widget["bg"])
        event.widget["bg"] = color

    def focusOut(self, event) -> None:
        """
        Changes the background color's of the button when it loses focus, based on the color tuple from the color dictionary.
        """
        color = self._selectColor(event.widget["bg"])
        event.widget["bg"] = color

    def validPassword(self, password: str):
        """
        Validates the entered password to create an account. A good password has more than four characters.

        Args:
            password (str): the entered password
        """
        if len(password) < 4:
            self.et_password["highlightcolor"] = self.et_password["highlightbackground"] = self.et_password["fg"] = "red"
        else:
            self.et_password["highlightcolor"] = "#8F00FF"
            self.et_password["highlightbackground"] = "white"
            self.et_password["fg"] = "white"

    def _releaseButtonLogin(self, event=None):
        """
        Activate the button when the email and password field are not empty
        """

        email = self.et_email.get()
        password = self.et_password.get()
        if (email and password) and not (self.et_email.estado or self.et_password.estado):
            self.bt_continue.configure(bg="#8F00FF", activebackground="#530391", activeforeground="white", bd=0,
                                       state="normal")
        else:
            self.bt_continue.configure(bg="#0D0D0D", state="disabled", bd=3)

    def _selectColor(self, actual_color: str) -> str:
        """
        Changes the color between a lightest or a darker color, based on the colors registered in the color dictionary.

        Args:
            actual_color (str): the actual color of the widget

        Raises:
            Exception: if the color pair does not exists, raises a exception

        Returns:
            str: the other color from the color pair of the color dictionary
        """
        for color_tuple in self.colors.values():
            if color_tuple[0] == actual_color:
                return color_tuple[1]
            elif color_tuple[1] == actual_color:
                return color_tuple[0]
        raise Exception(f"A cor {actual_color} não foi adicionada ao dicionário local de cores!")
