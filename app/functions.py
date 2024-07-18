from tkinter import * # type: ignore

class Functions:

    def focusIn(self, event) -> None:
        color = self._selectColor(event.widget["bg"])
        event.widget["bg"] = color

    def focusOut(self, event) -> None:
        color = self._selectColor(event.widget["bg"])
        event.widget["bg"] = color

    def _selectColor(self, actual_color: str) -> str:
        colors: dict[str, tuple] = {
            "purple": ("#8F00FF", "#7202c9"),
            "pink": ("#FF003D", "#d40234")
        }

        for color_tuple in colors.values():
            if color_tuple[0] == actual_color:
                return color_tuple[1]
            elif color_tuple[1] == actual_color:
                return color_tuple[0]


