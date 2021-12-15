#Jeremy Klein
#CS345
#The database below is a database of all of the ninjutsus used in the show Naruto (Shonen Jump)
#I created one large table that contains all of the basic information about each jutsu and created smaller tables for
#the different characters that use the jutsus and a table that holds every jutsu for each type of jutsu
#I also created smaller tables based on the range of each ninjutsu
#In all of these tables the name of the ninjutsu is not null since there can't be two ninjutsus that have the same name
#I also required an entry for the character that uses the jutsu since you can't have a ninjutsu without a user, made
#sure there could not be two characters with same first and last name, and linked the character first name from the
#character table and the character name in the main ninjutsus table

#The following code was written using the python ide editor (version 3.9)

#importing sqlite3 to use in the pythonfile

import sqlite3

import os

#removing the data saved in the database so that it does not recreate the database everytime you run it

os.remove("ninjutsus.db")

#connection to the database so that you can actually edit the tables, attributes, etc. inside the database

connect = sqlite3.connect("ninjutsus.db")

jutsu = connect.cursor();

########################################################################################################################

#creating a large table that holds all of the ninjutsus and each ninjutsus name, type (e.g. offensive)

jutsu.execute('''CREATE TABLE ninjutsus
            (name  text NOT NULL PRIMARY KEY,
             type  text NOT NULL,
             character  text NOT NULL,
             range int,
             rank  text,
             FOREIGN KEY (character) REFERENCES character(firstname) )''')

#creating a table of all of the characters that use a jutsu in the big table that holds the characters first name, last
#name, and the village they come from
         
jutsu.execute('''CREATE TABLE character
            (firstname text NOT NULL,
             lastname  text,
             village   text NOT NULL,
             PRIMARY KEY(firstname, lastname)) ''')

#the next four tables created are tables that contain the rank, users full name, and range of each jutsu based on the
#four different types of jutsu: Offensive, Defensive, Hiden, Supplementary, and all four types

jutsu.execute('''CREATE TABLE offensivejutsus
            (name text NOT NULL,
             rank text,
             userf text,
             userl text,
             range int)''')

jutsu.execute('''CREATE TABLE defensivejutsus
            (name text NOT NULL,
             rank text,
             characterf text,
             characterl text,
             range int)''')

jutsu.execute('''CREATE TABLE supplementaryjutsus
            (name text NOT NULL,
             rank text,
             userf text,
             userl text,
             range int)''')

jutsu.execute('''CREATE TABLE hidenjutsus
            (name text NOT NULL,
             rank text,
             userf text,
             userl text,
             range int)''')

jutsu.execute('''CREATE TABLE allfourjutsutypes
            (name text NOT NULL,
             rank text,
             userf text,
             userl text,
             range int) ''')

#the next four tables created are tables that contain the name and type of attack based on the four different ranges that
#jutsus can have: long, medium, short, and no range

jutsu.execute('''CREATE TABLE shortrange
        (name text NOT NULL,
         type text NOT NULL) ''')

jutsu.execute('''CREATE TABLE midrange
        (name text NOT NULL,
         type text NOT NULL) ''')

jutsu.execute('''CREATE TABLE longrange
        (name text NOT NULL,
         type text NOT NULL) ''')

jutsu.execute('''CREATE TABLE norange
        (name text NOT NULL,
         type text NOT NULL) ''')
         
########################################################################################################################

#inserting values into the ninjutsus table

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Amagumo', 'Offensive', 'Kidoumaru', 100, 'B')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Amaterasu', 'Offensive', 'Itachi', 5, NULL)''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Baika no Jutsu', 'Hiden', 'Chouji', NULL, '')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Bubun Baika no Jutsu', 'Hiden', 'Chouji', NULL, NULL)''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Bunshin Daibakuha', 'Defensive', 'Itachi', NULL, 'A')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Bunshin no Jutsu', 'Supplementary', 'Naruto', NULL, 'E')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Chakura Kyuin Jutsu', 'Supplementary', 'Akadou', 5, NULL)''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Chidori', 'Offensive', 'Kakashi', 5, 'A')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES('Chikatsu Saisei no Jutsu', 'Supplementary', 'Shizune', 5, 'A')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Chobaika no Jutsu', 'Hiden', 'Chouji', NULL, NULL)''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Daikamaitachi no Jutsu', 'Defensive', 'Temari', 100, 'B')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Diason no Me', 'Supplementary', 'Gaara', NULL, NULL)''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Dokugiri', 'Offensive', 'Shizune', 10, 'B') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Dokumeki no Jutsu', 'Supplementary', 'Sakura', 5, NULL) ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Fushi Tensei', 'Supplementary', 'Orochimaru', NULL, 'S') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Gokusamaiso', 'Offensive', 'Gaara', 10, NULL) ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Hari Jizo', 'Offensive, Defensive', 'Jiraiya', 5, 'B') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Henge no Jutsu', 'Supplementary', 'Iruka', NULL, 'E') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Hiraishin no Jutsu', 'Supplementary', 'Minato', 100, 'S') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Inyu Shometsu', 'Supplementary', 'Kabuto', NULL, 'A') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Jinju Konbi Henge: Sotoro', 'Supplementary', 'Kiba', NULL, 'B') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Jujin Bunshin', 'Supplementary', 'Akamaru', NULL, 'B') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kage Bunshin no Jutsu', 'Supplementary', 'Naruto', NULL, 'B') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kage Kubi Shibari no Jutsu', 'Hiden', 'Shikamaru', 10, NULL) ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kage Shuriken no Jutsu', 'Offensive', 'Sasuke', 100, 'D') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kagemane no Jutsu', 'Hiden, Supplementary', 'Shikamaru', 10, NULL) ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kage Nui', 'Offensive, Hiden', 'Shikamaru', 10, NULL) ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kakuremino no Jutsu', 'Supplementary', 'Konohamaru', NULL, 'E') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kamaitachi no Jutsu', 'Offensive', 'Temari', 10, 'C') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kanashibari no Jutsu', 'Supplementary', 'Orochimaru', 10, 'D') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Katon: Gokakyu', 'Offensive', 'Jiraiya', 100, 'B') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Katon: Gokakyu no Jutsu', 'Offensive', 'Fugaku', 5, 'C') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Katon: Hosenka no Jutsu', 'Offensive', 'Sasuke', 5, 'C') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Katon: Karyu Endan', 'Offensive', 'Hiruzen', 10, 'B') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Katon: Ryuka no Jutsu', 'Offensive', 'Sasuke', 10, 'C') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Katsuyu Daibunretsu', 'Supplementary', 'Katsuyu', NULL, NULL) ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kawarimi no Jutsu', 'Supplementary', 'Naruto', NULL, 'E') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kaze no Yaiba', 'Offensive', 'Baki', 5, 'A') ''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kikaichu no Jutsu', 'All types', 'Shino', 100, NULL)''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kiri Gakura no Jutsu', 'Supplementary', 'Zabuza', NULL, 'D')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Konbi Henge', 'Supplementary', 'Naruto', NULL, 'B')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kuchiyose: Doton: Tsuiga no Jutsu', 'Offensive', 'Kakashi', 100, 'B')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kuchiyose: Edo Tensei', 'Supplementary', 'Orochimaru', NULL, 'S')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kuchiyose: Gamaguchi Shibari', 'Offensive', 'Jiraiya', 100, 'A')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kiri no Sneeze', 'Supplementary', 'Orochimaru', 0, 'S')''')

jutsu.execute('''INSERT INTO ninjutsus
                 VALUES ('Kuchiyose: Kirikiri Mai', 'Offensive', 'Temari', 100, 'B')''')

########################################################################################################################

#inserting values in the character table

jutsu.execute('''INSERT INTO character
                 VALUES ('Naruto', 'Uzumaki', 'Leaf')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Sakura', 'Haruno', 'Leaf')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Gaara', NULL, 'Sand')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Kidoumaru', 'Chiba', 'Sound')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Chouji', 'Akimichi', 'Leaf')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Itachi', 'Uchiha', 'Leaf')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Akadou', 'Yoroi', 'Sea')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Kakashi', 'Hatake', 'Leaf')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Shizune', NULL, 'Leaf')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Temari', 'Nara', 'Sand')''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Orochimaru', NULL, 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Jiraiya', NULL, 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Iruka', 'Umino', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Minato', 'Namikaze', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Kabuto', 'Takushi', 'None') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Kiba', 'Inuzuka', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Akamaru', NULL, 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Shikamaru', 'Nara', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Fred', 'Fake', 'Ohio') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Konohamaru', 'Sarutobi', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Fugaku', 'Uchiha', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Hiruzen', 'Sarutobi', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Katsuyu', 'Unknown', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Baki', 'Unknown', 'Sand') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Shino', 'Aburame', 'Leaf') ''')

jutsu.execute('''INSERT INTO character
                 VALUES ('Zabuza', 'Momochi', 'Mist') ''')

########################################################################################################################

#updating the nijutsu and character table to either change values so they are correct or changing null values to unknown

jutsu.execute('''UPDATE ninjutsus
                 SET type = 'Offensive', range = 5
                 WHERE name = 'Bunshin Daibakuha' ''')

jutsu.execute('''UPDATE character
                 SET lastname = 'Unknown'
                 WHERE firstname = 'Gaara' ''')

jutsu.execute('''UPDATE character
                 SET lastname = 'Unknown'
                 WHERE firstname = 'Shizune' ''')

jutsu.execute('''UPDATE character
                 SET lastname = 'Unknown'
                 WHERE firstname = 'Orochimaru' ''')

jutsu.execute('''UPDATE character
                 SET lastname = 'Unknown'
                 WHERE firstname = 'Jiraiya' ''')

jutsu.execute('''UPDATE character
                 SET lastname = 'Unknown'
                 WHERE firstname = 'Akamaru' ''')

########################################################################################################################

#deleting jutsus and characters from tables to ensure they contain the right info

jutsu.execute('''DELETE FROM character
                 WHERE lastname = 'Fake' ''')

jutsu.execute('''DELETE FROM ninjutsus
                 WHERE name = 'Kiri no Sneeze' ''')

#inserting jutsus into the offensivejutsus table based on the type columns of the jutsus table
#the query also uses a join to pull attributes from both ninjutsus and charater to give this table more info on the
#character that is using the jutsu

offensivejutsu = '''INSERT INTO offensivejutsus
                    SELECT n.name, n.rank, c.firstname, c.lastname, n.range 
                    FROM ninjutsus AS n
                    JOIN character AS c
                    ON n.character = c.firstname
                    WHERE type = 'Offensive' OR type = 'Offensive, Defensive' OR type = 'Offensive, Hiden' '''

jutsu.execute(offensivejutsu)

#inserting jutsus into the defensivejutsus table based on the type columns of the jutsus table
#the query also uses a join to pull attributes from both ninjutsus and charater to give this table more info on the
#character that is using the jutsu

defensivejutsu = '''INSERT INTO defensivejutsus
                    SELECT n.name, n.rank, c.firstname, c.lastname, n.range 
                    FROM ninjutsus AS n
                    JOIN character AS c
                    ON n.character = c.firstname
                    WHERE type = 'Defensive' OR type = 'Offensive, Defensive' '''

jutsu.execute(defensivejutsu)

#inserting jutsus into the supplementaryjutsus table based on the type columns of the jutsus table
#the query also uses a join to pull attributes from both ninjutsus and charater to give this table more info on the
#character that is using the jutsu

supplementaryjutsu = '''INSERT INTO supplementaryjutsus
                        SELECT n.name, n.rank, c.firstname, c.lastname, n.range 
                        FROM ninjutsus AS n
                        JOIN character AS c
                        ON n.character = c.firstname
                        WHERE type = 'Supplementary' OR type = 'Hiden, Supplementary' '''

jutsu.execute(supplementaryjutsu)

#inserting jutsus into the hidenjutsus table based on the type columns of the jutsus table
#the query also uses a join to pull attributes from both ninjutsus and charater to give this table more info on the
#character that is using the jutsu

hidenjutsu = '''INSERT INTO hidenjutsus
                SELECT n.name, n.rank, c.firstname, c.lastname, n.range 
                FROM ninjutsus AS n
                JOIN character AS c
                ON n.character = c.firstname
                WHERE type = 'Hiden' OR type = 'Hiden, Supplementary' '''

jutsu.execute(hidenjutsu)

#inserting jutsus into the allfourjutsutypes table based on the type columns of the jutsus table
#the query also uses a join to pull attributes from both ninjutsus and charater to give this table more info on the
#character that is using the jutsu

allfourjutsu = '''INSERT INTO allfourjutsutypes
                   SELECT n.name, n.rank, c.firstname, c.lastname, n.range 
                   FROM ninjutsus AS n
                   JOIN character AS c
                   ON n.character = c.firstname
                   WHERE type = 'All types' '''

jutsu.execute(allfourjutsu)

shortrange = '''INSERT INTO shortrange
                SELECT name, type
                FROM ninjutsus
                WHERE range = 5 '''

jutsu.execute(shortrange)

midrange = '''INSERT INTO midrange
              SELECT name, type
              FROM ninjutsus
              WHERE range = 10 '''

jutsu.execute(midrange)

longrange = '''INSERT INTO longrange
               SELECT name, type
               FROM ninjutsus
               WHERE range = 100 '''

jutsu.execute(longrange)

norange = '''INSERT INTO norange
             SELECT name, type
             FROM ninjutsus
             WHERE range = NULL '''

jutsu.execute(norange)

########################################################################################################################

#printing the offensivejutsus table created by the insert query

offensivejutsu = '''SELECT * FROM offensivejutsus'''

jutsu.execute(offensivejutsu)

#printing out the query that is being used
print("QUERY:", offensivejutsu)
print()
print("RESULT:")
print()
#initializing and defining a variable to iterate through the result of the query
iterator = jutsu.fetchone()
#while loop that iterates through the result query until it hits a null row
while iterator is not None:
    print(iterator)
    print()
    iterator = jutsu.fetchone()
print()
print("*" * 50)

########################################################################################################################

#printing the defensivejutsus table created by the insert query

defensivejutsu = '''SELECT * FROM defensivejutsus'''

jutsu.execute(defensivejutsu)

#printing out the query that is being used
print("QUERY:", defensivejutsu)
print()
print("RESULT:")
print()
#initializing and defining a variable to iterate through the result of the query
iterator = jutsu.fetchone()
#while loop that iterates through the result query until it hits a null row
while iterator is not None:
    print(iterator)
    print()
    iterator = jutsu.fetchone()
print()
print("*" * 50)

########################################################################################################################

#printing the supplementaryjutsus table created by the insert query

supplementaryjutsu = '''SELECT * FROM supplementaryjutsus'''

jutsu.execute(supplementaryjutsu)

#printing out the query that is being used
print("QUERY:", supplementaryjutsu)
print()
print("RESULT:")
print()
#initializing and defining a variable to iterate through the result of the query
iterator = jutsu.fetchone()
#while loop that iterates through the result query until it hits a null row
while iterator is not None:
    print(iterator)
    print()
    iterator = jutsu.fetchone()
print()
print("*" * 50)

########################################################################################################################

#printing the hidenjutsus table created by the insert query

hidenjutsu = '''SELECT * FROM hidenjutsus'''

jutsu.execute(hidenjutsu)

#printing out the query that is being used
print("QUERY:", hidenjutsu)
print()
print("RESULT:")
print()
#initializing and defining a variable to iterate through the result of the query
iterator = jutsu.fetchone()
#while loop that iterates through the result query until it hits a null row
while iterator is not None:
    print(iterator)
    print()
    iterator = jutsu.fetchone()
print()
print("*" * 50)

########################################################################################################################

allfourjutsutypes = '''SELECT * FROM allfourjutsutypes'''

jutsu.execute(allfourjutsutypes)

#printing out the query that is being used
print("QUERY:", allfourjutsutypes)
print()
print("RESULT:")
print()
#initializing and defining a variable to iterate through the result of the query
iterator = jutsu.fetchone()
#while loop that iterates through the result query until it hits a null row
while iterator is not None:
    print(iterator)
    print()
    iterator = jutsu.fetchone()
print()
print("*" * 50)

########################################################################################################################

#command line prompt asking the user what table they would like to see between the tables character, shortrange jutsus,
#midrange jutsus, longrange jutsus, and jutsus that have no range 

userinput = ""
output = ""

print("What Table would you like to see?")
print()
print("Enter c for characters, s for short range jutsus, m for medium range jutsus, l for long range jutsus, and n for ")
print("jutsus that don't have a range.")
print()

userinput = input()

#if statements that select the table based on what the user inputs by editing the string output

if userinput == "c":
    output = ('''SELECT *
                 FROM character ''')
elif userinput == "s":
    output = ('''SELECT *
                 FROM shortrange ''')
elif userinput == "m":
    output = ('''SELECT *
                 FROM midrange ''')
elif userinput == "n":
    output = ('''SELECT *
                 FROM shortrange ''')
#else block catches when a user inputs an incorrect value
else:
    print("Invalid Entry, please reboot or run again :( ")

jutsu.execute(output)

#printing out the query that is being used
print("QUERY: ", output)
print()
print("RESULT:")
print()
#initializing and defining a variable to iterate through the result of the query using a while loop
iterator = jutsu.fetchone()
#while loop that iterates through the result query until it hits a null row
while iterator is not None:
    print(iterator)
    print()
    iterator = jutsu.fetchone()
print()
print("*" * 50)
print()
print("ALL DONE")







