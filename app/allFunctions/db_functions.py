from cgitb import text
from .db_functions_interface import DBManagerInterface
import sqlite3

class DBManager(DBManagerInterface):

    def verifyAccount(self) -> bool:
        email = self.et_email.get()
        password = self.et_password.get()
        registration = self._accountRegistration(email, password)
        if registration:
            return True
        else:
            return False

    def addAccount(self) -> bool:
        name = self.et_name.get()
        surname = self.et_surname.get()
        email = self.et_email.get()
        password = self.et_password.get()
        registration = self._accountRegistration(email, password)
        if not registration:
            self.connection()
            self.cursor.execute("""
                INSERT INTO Accounts(name, surname, email, password) VALUES(?, ?, ?, ?)
            """, (name, surname, email, password))
            self.conn.commit()
            self.disconnection()
            return True
        else:
            return False

    def connection(self):
        self.conn = sqlite3.connect("Accounts.db")
        self.cursor = self.conn.cursor()

    def disconnection(self):
        self.conn.close()

    def createTable(self):
        self.connection()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Accounts(
                email CHAR(40) NOT NULL,
                password CHAR(40) NOT NULL,
                name CHAR(15) NOT NULL,
                surname Char(30) NOT NULL
            );
        """)
        self.conn.commit()
        self.disconnection()

    def _accountRegistration(self, email: str, password: str) -> bool:
        self.connection()
        self.cursor.execute(f"""
            SELECT email, password FROM Accounts WHERE email = ?
        """, (email,))

        accounts = self.cursor.fetchone()
        if accounts is not None:
            reg_email, reg_password = accounts

            if reg_email == email and reg_password == password:
                self.disconnection()
                return True
        self.disconnection()
        return False
    
if __name__ != "__main__":
    manager = DBManager()
    manager.createTable()
        