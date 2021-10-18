import sqlite3


class BookHighlightsDB:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('db/book-highlights.db')
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
        self.cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS email_index ON users (email_id)")

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
                    page INTEGER NOT NULL,
                    book INTEGER NOT NULL,
                    FOREIGN KEY (book) REFERENCES books(id)
                )""")

            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def addUser(self, name, email_id, password):
        self.cursor.execute("INSERT INTO users (name, email_id, password) VALUES (?, ?, ?)",
                            (name, email_id, password))
        self.connection.commit()

    def userExists(self, email_id):
        self.cursor.execute(
            "SELECT EXISTS(SELECT 1 FROM users WHERE email_id = ?)", (email_id,))
        exists = self.cursor.fetchone()[0]
        return exists

    def getPassword(self, email_id):
        self.cursor.execute(
            "SELECT password FROM users WHERE email_id = ?", (email_id, ))
        password = self.cursor.fetchone()

        if password:
            return password[0]
        else:
            return None

    def addBook(self, title, author, user):
        self.cursor.execute("INSERT INTO books (title, author, user) VALUES (?, ?, ?)",
                            (title, author, user))
        self.connection.commit()

    def getBooks(self, user):
        self.cursor.execute(
            f"SELECT id, title, author FROM books WHERE user = ?", (user,))
        return self.cursor.fetchall()

    def deleteBook(self, book):
        self.cursor.execute('DELETE FROM highlights WHERE book = ?', (book,))
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book,))
        self.connection.commit()

    def addHighlight(self, highlight, page, book):
        self.cursor.execute(
            'INSERT INTO highlights (highlight, page, book) VALUES (?, ?, ?)', (highlight, page, book))
        self.connection.commit()

    def getHighlights(self, book):
        self.cursor.execute(
            'SELECT id, highlight, page FROM highlights WHERE book = ?', (book,))
        return self.cursor.fetchall()

    def deleteHighlight(self, highlight):
        self.cursor.execute(
            'DELETE FROM highlights WHERE id = ?', (highlight,))
        self.connection.commit()

    def getUserID(self, email):
        self.cursor.execute(
            f"SELECT id FROM users WHERE email_id = ?", (email,))
        return self.cursor.fetchone()[0]

    def getUserName(self, email):
        self.cursor.execute(
            f"SELECT name FROM users WHERE email_id = ?", (email,))
        return self.cursor.fetchone()[0]

    def updateHighlight(self, new_value, highlight_id):
        self.cursor.execute(
            "UPDATE highlights SET highlight = ? WHERE id = ?", (new_value, highlight_id))
        self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()


if __name__ == '__main__':
    db = BookHighlightsDB()
    # db.addUser('Rushabh Javeri', 'javeri.rushabh45@gmail.com', 'Mpstme@123')
    # db.addUser('Om Kamath', 'om.kamath43@nmims.edu.in', 'ilovetech')
    # db.addUser('Varun Nair', 'varunanil03@gmail.com', 'animeop')

    # print(db.getPassword('javeri.rushabh45@gmail.com'))
    # print(db.getPassword('javeri.rushabh45'))

    # db.addBook('Sapiens', 'Yuval Harari', 2)
    # db.addBook('Why We Sleep', 'Matthew Walker', 2)
    # db.addBook('The Ninth Pawn of the White', 'Vijay Fafat', 2)
    # db.addBook('Atomic Habits', 'James Clear', 2)

    # db.addBook('Ikigai', 'Hector Garcia', 2)
    # db.addBook('Man\'s search for Meaning', 'Victor Frankl', 2)

    # db.addBook('To Kill a Mockingbird', 'Harper Lee', 3)

    # db.addHighlight('Wow awesome', 2, 2)
    # db.addHighlight('Wow superb', 3, 2)
    # db.addHighlight('Wow too good', 17, 2)

    # print(db.getUserName('javeri.rushabh45@gmail.com'))
    # print(db.getUserName('om@gmail.com'))

    # db.updateHighlight('Best book ever', 3)

    # print(db.getBooks(1))

    # print(db.userExists('javeri.rushabh45@gmail.com'))
    # print(db.userExists('om@gmail.com'))
    # print(db.userExists('varun@gmail.com'))
    # print(db.userExists('hello moto'))
