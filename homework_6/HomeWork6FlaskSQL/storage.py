# -*- coding: utf-8 -*-
import datetime
import sqlite3


def make_db():
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS entries (title text, text text, created_at text, comments text);""")
    # cursor.execute('DELETE FROM entries')

    BLOG_ENTRIES = [("It's first entry",
      'The term normalisation comes from the database world. It refers to transforming the schema of a \n        database to remove redundant information. Also, redundant information means the same data that is stored in more \n        than one place.',
      '21:19:19 - Nov 24 2019', 'Julius Koronci;Nice article - Alexander Shirokov;Thanks for good article'
      ),
     ("It's second entry",
      'The term normalisation comes from the database world. It refers to transforming the schema of a \n        database to remove redundant information. Also, redundant information means the same data that is stored in more \n        than one place.',
      '21:19:19 - Nov 24 2019',
      "")]

    cursor.execute("SELECT rowid, * FROM entries")
    a = cursor.fetchall()
    if len(a) < 2:
        cursor.executemany("INSERT INTO entries (title, text, created_at, comments) values (?, ?, ?, ?)", BLOG_ENTRIES)
        conn.commit()


def read_db():
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM entries")
    a = cursor.fetchall()
    d = []
    for now in a:
        s = now[4]
        c = []
        if s == '':
            c.append([])
        else:
            for w in s.split(' - '):
                name, text = w.split(';')
                c.append({'name': name, 'text': text})
        d.append({'key': now[0],
                  'title': now[1],
                  'text': now[2],
                  'created_at': now[3],
                  'comments': c})
    return d


def addto_db(title, text, created_at):
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO entries (title, text, created_at, comments) values (?, ?, ?, ?)", (title, text, created_at, ''))
    conn.commit()


def getlast_key():
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid FROM entries")
    return (cursor.fetchall())[-1][0]


def add_comment(key, name, text):
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute("SELECT comments FROM entries WHERE rowid = ?", (key, ))
    old_com = cursor.fetchall()[0][0]
    if old_com == '':
        add = name + ';' + text
    else:
        add = ' - ' + name + ';' + text
    new_com = old_com + add
    cursor.execute("""UPDATE entries SET comments = ? WHERE rowid = ?""", (new_com, key))
    conn.commit()

