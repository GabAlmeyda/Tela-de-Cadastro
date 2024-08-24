class AccountManager:

    def __init__(self) -> None:
        self.file = "accounts.txt"

        with open(self.file, "a") as _:
            pass

    def readAccounts(self):
        """
           Reads all registered accounts (email and password) in the 'accounts.txt' file
        """
        with open(self.file, "r") as file:
            print(file.read())

    def addAccount(self, email: str, password: str):
        """
            Add an account (email and password set) in the 'accounts.txt' file
        """
        with open(self.file, "a") as file:
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
            file.write("---\n")

    def verifyAccount(self, email: str, password: str) -> bool:
        """
            Checks whether the email and password provided fit in a registered account.
            Returns True if it has, returns False if it doens't.
        """
        with open(self.file, "r") as file:
            accounts = file.read().split("---\n")
            for acc in accounts:
                acc_info = acc.split("\n")
                if (acc_info[0])[7:] == email and (acc_info[1])[9:] == password:
                    return True
        return False
    
    def findAccount(self) -> bool:
        """
            Checks whether the provided email already exists in the registration.
            Return True if it has, returns False if it doens't.
        """
        with open(self.file, "r") as file:
            accounts = file.read().split("---\n")
            for acc in accounts:
                email = ((acc.split("\n"))[0]).replace("Email: ", "")
                if email == self.et_email.get():
                    return True
                else:
                    return False
