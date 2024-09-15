from abc import ABC, abstractmethod

class DBManagerInterface(ABC):

    @abstractmethod
    def connection(self):
        """
        Connects to Database.
        """

    @abstractmethod
    def disconnection(self):
        """
        Disconnects from Database.
        """
    
    def createTable(self):
        """
        Create the table if it not exists.
        """
        pass

    @abstractmethod
    def addAccount(self):
        """
        Adds an account to the 'Accounts.db' Databse
        """
        pass
    
    @abstractmethod
    def verifyAccount():
        """"
        Checks whether the account is registered.
        """
        pass

    @abstractmethod
    def _accountRegistration(self, email: str, password: str) -> bool:
        """
        Goes through all registered accounts and compares whether the email and password provided are registered.

        Args:
            email (str): the email provided;
            password (str): the password provided.

        Returns:
            bool: it returns True if the email and the password provided are related to an account, otherwise, it returns False.
        """
        pass