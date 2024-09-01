from app import StartWindow, LoginWindow, AppWindow
from tkinter import *

while True:
    print("\033[1;36m"+"[1] para Start Window\n[2] para Login Window\n[3] para Register Window\n[4] para App Window\n[5] para Sair\n")
    opcao = int(input("Digite uma opção: \033[0m"))

    match opcao:
        case 1:
            print("\033[1;32mStart Window")
            start = StartWindow()
            start.run()
        case 2:
            print("\033[1;33mLogin Window")
            login = LoginWindow()
            login.run()
        case 3:
            print("\033[1;34mRegister Window")
            pass
        case 4:
            print("\033[1;35mApp Window")
            app = AppWindow()
            app.run()
        case 5:
            break
        case _:
            print("Invalid Option!")

    print("_" * 50)






