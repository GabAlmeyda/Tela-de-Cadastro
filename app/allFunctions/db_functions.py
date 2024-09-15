from cgitb import text
from .db_functions_interface import DBManagerInterface
import sqlite3

class DBManager(DBManagerInterface):

    def __init__(self) -> None:
        self.createTable()

    def verifyAccount(self) -> bool:
        self.email = self.et_email.get()
        self.password = self.et_password.get()
        registration = self._accountRegistration(self.email, self.password)
        if registration:
            return True
        else:
            return False

    def addAccount(self) -> bool:
        self.name = self.et_name.get()
        self.surname = self.et_surname.get()
        self.email = self.et_email.get()
        self.password = self.et_password.get()
        registration = self._accountRegistration(self.email, self.password)
        if not registration:
            self.connection()
            self.cursor.execute("""
                INSERT INTO Accounts(name, surname, email, password) VALUES(?, ?, ?, ?)
            """, (self.name, self.surname, self.email, self.password))
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
        accounts: list[str, str] = self.cursor.fetchall()
        self.disconnection()
        for reg_email, reg_password in accounts:
            if reg_email == email and reg_password == password:
                return True
        return False
        