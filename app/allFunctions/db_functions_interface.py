from abc import ABC, abstractmethod

class DBManagerInterface(ABC):

    @abstractmethod
    def connection(self):
        """
        Connects to Database.

        Raises:
            NotImplementedError: raises an error if the method isn't implemented.
        """
        raise NotImplementedError("'connection' method needs to be implemented!")

    @abstractmethod
    def disconnection(self):
        """
        Disconnects from Database.

        Raises:
            NotImplementedError: raises an error if the method isn't implemented.
        """
        raise NotImplementedError("'disconnection' method needs to be implemented!")
    
    def createTable(self):
        """
        Create the table if it not exists.

        Raises:
            NotImplementedError: raises an error if the method isn't implemented.
        """
        raise NotImplementedError("'createTable' method needs to be implemented!")

    @abstractmethod
    def addAccount(self):
        """
        Adds an account to the 'Accounts.db' Databse

        Raises:
            NotImplementedError: raises an error if the method isn't implemented.
        """
        raise NotImplementedError("'AddAccount' method needs to be implemented!")
    
    @abstractmethod
    def verifyAccount():
        """"'AddAccount' method needs to be implemented!"

        Raises:
            NotImplementedError: raises an error if the method isn't implemented.
        """
        raise NotImplementedError("'verifyAccount' method needs to be implemented!")

    @abstractmethod
    def _accountRegistration(self, email: str, password: str) -> bool:
        """
        Goes through all registered accounts and compares whether the email and password provided are registered.

        Args:
            email (str): the email provided;
            password (str): the password provided.

        Raises:
            NotImplementedError: raises an error if the method isn't implemented.

        Returns:
            bool: it returns True if the email and the password provided are related to an account, otherwise, it returns False.
        """
        raise NotImplementedError("'verifyAccount' method needs to be implemented!")