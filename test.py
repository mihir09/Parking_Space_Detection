import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='testdatabase',
)

mycursor = db.cursor()

users = [("mihir", "mj1"),
         ("prutha", "pp1")]

user_scores = [(45, 100),
               (75, 100)]

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50), passwd VARCHAR(50))"
Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id),game1 int DEFAULT 0, game2 int DEFAULT 0)"

# mycursor.execute(Q1)
# mycursor.execute(Q2)

Q3= "Insert Into Users (name,passwd) VALUES (%s,%s)"
Q4= "Insert Into Scores (userId, game1, game2) VALUES (%s,%s,%s)"

for x,user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[x])
db.commit()
mycursor.execute("SELECT * FROM Users")

for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Scores")

for x in mycursor:
    print(x)


# mycursor.execute("CREATE DATABASE testdatabase")

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("DESCRIBE Person")
#
# for x in mycursor:
#     print(x)

# st = ('prutha',21)
# mycursor.execute("INSERT INTO Person(name, age) VAlUES (%s,%s)", st)
# db.commit()
#
# mycursor.execute("SELECT * FROM Person")
#
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE Test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Prutha",datetime.now(),"F"))
# db.commit()

# mycursor.execute("SELECT id,name FROM Test WHERE gender='M' ORDER BY id ASC")
#
# for x in mycursor:
#     print(x)

# mycursor.execute("alter TABLE Test ADD COLUMN food varchar(50) NOT NULL")
# mycursor.execute("alter TABLE Test DROP food")
# mycursor.execute("alter TABLE Test CHANGE first_name first_name varchar(30)")
# mycursor.execute("Describe Test")
#
# for x in mycursor:
#     print(x)

