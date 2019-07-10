from connection import cur
while True:
    print("""welcome 2 'save platter' app
        [1] insert platter
        [2] remove platter
    """)
    a = input("==>")
    if a == "1":
        song_name = input("song name -->")
        singer = input("singer -->")
        song_type = input("song type -->")
        year = int(input("year -->"))
        connect.cursor()
        cur.execute('''INSERT INTO platter VALUES (?,?,?,?)''', (song_name, singer, song_type, year))
        cur.execute("select * from platter")
        for i in cur.fetchall():
            print(i)
        connect.commit()
        print("succes")
        cur.close()
        input("enter to homepage")
    elif a == "2":
        song_name = input("song name -->")
        singer = input("singer -->")
        song_type = input("song type -->")
        year = int(input("year -->"))
        ques = input("if u sure enter 1")
        if ques == "1":
            connect.cursor()
            cur.execute('''DELETE FROM platter WHERE songname = ? ''',(song_name,))
            connect.commit()
            print("succ")
            cur.close()
            input("enter to homepage")
        else:
            print("wrong!")
            input("enter to homepage")
    else:
        print("something went wrong")
        input("enter to homepage")
