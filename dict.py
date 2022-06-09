import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="connectdb",
   user="marcus",
   password="abc123"
)
##reads the dict
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
##add words to translate
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
#deletes words from the dictionary
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
#saves the dictionary
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()
commands = [

     '\n',

    ' ADD:      Add a name to the, list',

    ' LIST:     Print the list of names',

    ' DELETE:   Delete phone',

    ' QUIT:     End the program by pressing ctrl +c',

    '\n']


for x in commands:

    print(x)
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
