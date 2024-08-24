class AccountManager:

    def __init__(self) -> None:
        self.file = "accounts.txt"

        with open(self.file, "a") as _:
            pass

    def readAccounts(self):
        with open(self.file, "r") as file:
            print(file.read())

    def addAccount(self, email: str, password: str):
        with open(self.file, "a") as file:
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
            file.write("---\n")

    def verifyAccount(self, email: str, password: str) -> bool:
        with open(self.file, "r") as file:
            accounts = file.read().split("---\n")
            for acc in accounts:
                acc_info = acc.split("\n")
                if (acc_info[0])[7:] == email and (acc_info[1])[9:] == password:
                    return True
        return False
