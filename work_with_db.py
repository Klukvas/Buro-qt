import sqlite3


def login(log, pas):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    [req] = curso.execute("SELECT * FROM Logging WHERE Username = ? AND Password = ?",(log, pas))
    connee.close()
    return req

def register(log, pas, typef):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    curso.execute("INSERT INTO Logging VALUES (?,?,?)",(log, pas, typef))
    connee.commit()
    connee.close()


def delete(username):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    [req] = curso.execute("SELECT Password FROM Logging WHERE Username = ?",(str(username),))
    connee.close()
    return req

def del_acc(pas):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    curso.execute("DELETE  FROM Logging WHERE Password = ?",[pas])
    connee.commit()
    connee.close()


def change_pass(pas, username):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    curso.execute("UPDATE Logging SET Password = ? WHERE Username = ?",(pas,username))
    connee.commit()
    connee.close()


def change_name(username, pas):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    curso.execute("UPDATE Logging SET Username = ? WHERE Password = ?",(username,pas))
    connee.commit()
    connee.close()

def create_emp(head, salary, city, body, image, author):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    curso.execute("INSERT INTO vacS VALUES (?,?,?,?,?,?)",(head, salary, city, body, image, author))
    connee.commit()
    connee.close()

def create_res(post, salary, city, deck, image, author):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    curso.execute("INSERT INTO rezumS VALUES (?,?,?,?,?,?)",(post, salary, city, deck, image, author))
    connee.commit()
    connee.close()

def getAllRes(author):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    req = []
    for item in curso.execute("SELECT * from rezumS where author = ?",(str(author),)):
        req.append(item)
    connee.close()
    return req

def getAllEmp(author):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    req = []
    for item in curso.execute("SELECT * from vacS where author = ?",(str(author),)):
        req.append(item)
    connee.close()
    return req

def getFiltered(salary, city):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    req = []
    for item in curso.execute("SELECT head, salary, city, body, author from vacS where salary >= ? and city like ?",(salary, city,)):
        req.append(item)
    connee.close()
    return req

def getFilteredForEmp(salary, city):
    connee = sqlite3.connect('LOG.db')
    curso = connee.cursor()
    req = []
    for item in curso.execute("SELECT posy, salary, city, description, author from rezumS where salary >= ? and city like ?",(salary, city,)):
        req.append(item)
    connee.close()
    return req

