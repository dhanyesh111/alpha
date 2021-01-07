import mysql.connector
import mysql.connector.errorcode
import population_load


def load_db():
    con = mysql.connector.connect(host="localhost", user="root", password="heisenberg")
    cur = con.cursor()
    create_query = "create database if not exists cal"
    cur.execute(create_query)
    cur.execute("use cal")
    table_query = "create table if not exists population (name varchar(60), populations varchar(60), currency varchar(60))"
    cur.execute(table_query)
    con.commit()
    cur.close()
    con.close()
    print("data collected")


def insert():
    con = mysql.connector.connect(host="localhost", user="root", password="heisenberg")
    cur = con.cursor()
    cur.execute("use cal")
    data = population_load.load()

    for i in data:
        val = (i["name"], i["population"], i["currency"])
        insert_query = "insert into population (name,populations,currency) values (%s,%s,%s)"
        cur.execute(insert_query, val)
    con.commit()
    cur.close()
    con.close()
    print("data inserted into database")

def clear():
    con = mysql.connector.connect(host="localhost", user="root", password="heisenberg")
    cur = con.cursor()
    cur.execute("use cal")
    delete_query="drop table population"
    cur.execute(delete_query)
    con.commit()
    cur.close()
    con.close()
    print("database cleared")

def select(name):
    con = mysql.connector.connect(host="localhost", user="root", password="heisenberg")
    cur = con.cursor()
    cur.execute("use cal")
    try:
        if name=="all":
            select_query = f"select * from population "
            cur.execute(select_query)
            for i in cur.fetchall():
             x,y,z=i
             print("<----------------------->")
             print(f"{x}:{y}:{z}")
        else :
            select_query = f"select populations,currency from population where name='{name}'"
            cur.execute(select_query)
            z = cur.fetchall()
            x, y = z[0]
            print(z)
            print(f"{name}'s population is {x} and currency is {y}")
    except:
        print("searching failed")
    con.commit()
    cur.close()
    con.close()




