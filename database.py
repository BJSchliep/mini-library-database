import sqlite3 as sq
import sys
con = sq.connect("miniLibrary.db") # Need to create a connection
cur = con.cursor()

try:
    cur.execute('''
        CREATE TABLE miniLibrary(
        Title TEXT,
        Author TEXT,
        Genre TEXT,
        Year INTERGER
        )''')
except Exception as e:
    pass

def displaylibrary():
    library = cur.execute(f"SELECT Title, Author, Genre, Year FROM miniLibrary ORDER BY Title ASC").fetchall()
    for book in library:
        print(f'{book[0]} | {book[1]} | {book[2]} | {book[3]}')

def insert_book():
    title = input("Enter Title: ")
    author = input("Enter author(First/Last name): ")
    genre = input("Enter genre: ")
    year = int(input("Enter year: "))
    cur.execute(f'''INSERT INTO miniLibrary VALUES
                (
                    '{title}',
                    '{author}',
                    '{genre}',
                    '{year}'
                )''')
    con.commit()

def delete_book():
    category = input('Enter categroy: (Title/Author/Genre/Year)')
    name = input("Enter name:")
    con.execute(f'''DELETE FROM miniLibrary WHERE {category} = '{name}' ''')
    con.commit()
    print("user deleted")

def filter_library():
    filter = input(f"Filter library by(Title, Author, Genre, Year): ")
    library = cur.execute(f"SELECT Title, Author, Genre, Year FROM miniLibrary ORDER BY {filter} ASC").fetchall()
    for book in library:
        print(f'{book[0]} | {book[1]} | {book[2]} | {book[3]}')


print("Hello Welcome to the Schliep Household Mini Library!")
task = 0
while(task != '6'):
    print("What would you like to do?")
    print('1) Display\n2) Filter\n3) Insert\n4) Delete\n5) Quit')
    task = input("#:")
    if (task == '1'):
        displaylibrary()
    elif (task == '2' ):
        filter_library()
    elif (task == '3' ):
        insert_book()
    elif (task == '4' ):
        delete_book()    
    elif(task == '5'):
        con.commit() #Saves the file
        con.close() # Closes the file
        sys.exit()

