import sqlite3
import uuid
from tkinter import * 

conn =sqlite3.connect('test.db')
cur = conn.cursor()
print("Opened database successfully")

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS BOOKS(
        ID TEXT PRIMARY KEY,
        BOOK TEXT NOT NULL
    )''')

    print("Table created successfully")
except Exception as e:
    print(e)

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS HIGHLIGHTS(
        PARENTID TEXT,
        HIGHLIGHTS TEXT NOT NULL
    )''')

    print("Table created successfully")
except Exception as e:
    print(e)

def load_booklist():
    books_list.delete(0,END)
    cur.execute("SELECT BOOK FROM BOOKS")
    values = cur.fetchall()
    print(values)
    c=1
    for value in values:
        books_list.insert(END,str(c)+" "+value[0])
        c+=1
        

def insert_book():
    bookname = entry_bookname.get()
    bookid=str(uuid.uuid4())[:3]
    print(bookname)
    conn.execute("INSERT INTO BOOKS(ID,BOOK) VALUES(?,?)",(bookid,bookname,))
    conn.commit()
    print("Inserted ")
    load_booklist()
    # cur.execute("SELECT rowid,* FROM BOOKS")
    # rows = cur.fetchall()[-1]
    # print(rows)   
    # books_list.insert(END,str(rows[0])+". "+rows[2])

def delete_book():
    book_id=books_list.curselection()
    print(book_id)
    value = books_list.get(book_id).split()[1:]
    book_name=' '.join(map(str,value))
    sql = 'DELETE FROM BOOKS WHERE BOOK=?'
    cur.execute(sql, (book_name,))
    conn.commit()
    books_list.delete(ACTIVE)
    load_booklist()

def add_highlight(bookid, highlight,list):
    real_highlight = highlight.get()
    conn.execute("INSERT INTO HIGHLIGHTS(PARENTID,HIGHLIGHTS) VALUES(?,?)",(bookid,real_highlight,))
    conn.commit()
    print("Inserted highlight")
    cur.execute("SELECT HIGHLIGHTS FROM HIGHLIGHTS WHERE PARENTID=?",(bookid,))
    rows = cur.fetchall()[-1]
    print(rows)   
    list.insert(END,str(rows[0]))


def add_highlights_window():
    book_id=books_list.curselection()[0]
    real_book_id = books_list.get(book_id).split()[0][:-1]
    title = books_list.get(book_id).split()[1:]
    string_title = ' '.join([str(elem) for elem in title])
    new_highlights_window=Toplevel(master)
    new_highlights_window.title(title)
    new_highlights_window.geometry("500x350")
    new_highlights_window.resizable(False, False)
    new_highlights_window.grid_columnconfigure(0,weight=1)
    new_highlights_window.grid_rowconfigure(0,weight=1)

    intro_name = Label(new_highlights_window, text=f"Book Name: {string_title}")
    intro_id = Label(new_highlights_window, text=f"Book ID: {real_book_id}")

    hlts_entry = Entry(new_highlights_window)
   
    hlts_frame = LabelFrame(new_highlights_window, text="Highlights")
    hlts_list = Listbox(hlts_frame)
    add_highlight_button = Button(new_highlights_window, text = "Add Highlight", command=lambda: add_highlight(real_book_id, hlts_entry,hlts_list))
    scrollbar = Scrollbar(hlts_frame)   
    books_list.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = hlts_list.yview)
    
    intro_name.grid(row=0, column=0, sticky=NW)
    intro_id.grid(row=0, column=0, sticky=W)

    hlts_entry.grid(row=1, column=0, pady=0)
    add_highlight_button.grid(row=1, column=0, pady=0, sticky=E)

    hlts_frame.grid(row=2,column=0, columnspan=3, sticky=EW)
    hlts_frame.grid_columnconfigure(0,weight=1)
    hlts_frame.grid_rowconfigure(0,weight=1)
    hlts_list.grid(row=0,column=0, columnspan=3, sticky=EW)
    scrollbar.grid(sticky=E)
    cur.execute("SELECT HIGHLIGHTS FROM HIGHLIGHTS WHERE PARENTID=?",(real_book_id,))
    rows = cur.fetchall()
    for values in rows:
        hlts_list.insert(END,str(values[0]))





master = Tk()
master.grid_columnconfigure(0,weight=1)
master.grid_rowconfigure(0,weight=1)
master.title("TK Highlight")

master.geometry("500x350")
master.resizable(False, False)
label_bookname = Label(text="Enter your book name: ")
entry_bookname = Entry()
add_btn = Button(master, text="Add book", command=insert_book)


# cur.execute("SELECT rowid,* FROM BOOKS")
books_frame = LabelFrame(master, text="Books")
books_list = Listbox(books_frame)
scrollbar = Scrollbar(books_frame)
books_list.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = books_list.yview)
# rows = cur.fetchall()   
# for values in rows:
#     books_list.insert(END,str(values[0])+" "+values[2])

load_booklist()

del_btn = Button(books_frame, text="Delete Book", command=delete_book)
add_hlts_button = Button(books_frame, text="Add Highlights", command=add_highlights_window)

label_bookname.grid(row=0, column=0, pady=2)
entry_bookname.grid(row=0, column=1, pady=1)
add_btn.grid(row=0, column=2, pady=2)

books_frame.grid(row=2,column=0, columnspan=3, sticky=EW)
books_frame.grid_columnconfigure(0,weight=1)
books_frame.grid_rowconfigure(0,weight=1)
books_list.grid(row=0,column=0, columnspan=3, sticky=EW)
scrollbar.grid(sticky=E)
del_btn.grid(sticky=S)
add_hlts_button.grid(pady=10,sticky=S)


master.mainloop()
conn.close()
