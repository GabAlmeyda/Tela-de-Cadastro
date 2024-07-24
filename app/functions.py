from tkinter import * # type: ignore

class Functions:

    # key: color's name, values order: lighter color ; darker color
    colors: dict[str, tuple] = {
            "purple": ("#8F00FF", "#7202c9"),
            "pink": ("#FF003D", "#d40234")
        }

    def focusIn(self, event) -> None:
        color = self._selectColor(event.widget["bg"])
        event.widget["bg"] = color

    def focusOut(self, event) -> None:
        color = self._selectColor(event.widget["bg"])
        event.widget["bg"] = color

    def _selectColor(self, actual_color: str) -> str:

        for color_tuple in self.colors.values():
            if color_tuple[0] == actual_color:
                return color_tuple[1]
            elif color_tuple[1] == actual_color:
                return color_tuple[0]
        raise Exception(f"A cor {actual_color} não foi adicionada ao dicionário local de cores!")


