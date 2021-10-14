import sqlite3


class BookHighlightsDB:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('book-highlights.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('PRAGMA foreign_keys=on')

        # Creating tables if they don't exist (for safety)
        try:
            self.cursor.execute("""\
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email_id TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )""")

            self.connection.commit()
        except sqlite3.OperationalError:
            pass

        # To make accessing data using email faster
        self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS email_index ON users (email_id)")

        try:
            self.cursor.execute("""\
                CREATE TABLE books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    user INTEGER NOT NULL,
                    FOREIGN KEY (user) REFERENCES users(id)
                )""")

            self.connection.commit()
        except sqlite3.OperationalError:
            pass

        try:
            self.cursor.execute("""\
                CREATE TABLE highlights (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    highlight TEXT NOT NULL,
                    book INTEGER NOT NULL,
                    FOREIGN KEY (book) REFERENCES books(id)
                )""")

            self.connection.commit()
        except sqlite3.OperationalError:
            pass
    
    
    def addUser(self, name, email_id, password):
        self.cursor.execute("INSERT INTO users (name, email_id, password) VALUES (?, ?, ?)", \
                                               (name, email_id, password))
        self.connection.commit()
    

    def getPassword(self, email_id):
        self.cursor.execute("SELECT password FROM users WHERE email_id = ?", (email_id, ))
        password = self.cursor.fetchone()
        
        if password:
            return password[0]
        else:
            return None


    def __del__(self) -> None:
        self.connection.close()

if __name__ == '__main__':
    db = BookHighlightsDB()
    # db.addUser('Rushabh Javeri', 'javeri.rushabh45@gmail.com', 'secret123')
    # db.addUser('Om Kamath', 'om.kamath43@nmims.edu.in', 'ilovetech')
    # db.addUser('Varun Nair', 'varunanil03@gmail.com', 'animeop')

    # print(db.getPassword('javeri.rushabh45@gmail.com'))
    # print(db.getPassword('javeri.rushabh45'))