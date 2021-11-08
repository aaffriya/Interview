import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0000",
  database = "student"
)

mycursor = mydb.cursor()

def insert():
    id = input("Enter Studnet ID :")
    name = input("Enter Student name :")
    city = input("Enter Student City :")
    id_list = id.split(",")
    name_list = name.split(",")
    city_list = city.split(",")
    i = 0
    while i != min(len(id_list),len(name_list),len(city_list)):
        query = f"insert into students(id, name, city) values({id_list[i]}, '{name_list[i]}', '{city_list[i]}')"
        mycursor.execute(query)
        mydb.commit()
        print(query)
        print(mycursor.rowcount, "was inserted.")
        i += 1

def delete():
    id = input("Enter Student ID : ")
    id_list = id.split()
    i = 0
    while i != len(id_list):
        query = f"delete from students where id = {id_list[i]}"
        mycursor.execute(query)
        mydb.commit()
        print(query)
        print(mycursor.rowcount, "record(s) deleted")
        i += 1

def update():
    try:
        id = int(input("Enter Student ID : "))
        type = input("Enter update to value : Name, City : ")
        Newval = input("Enter New Value: ")
        query = f"UPDATE students SET {type} = '{Newval}' WHERE id = {id}"
        mycursor.execute(query)
        mydb.commit()
        print(query)
        print(mycursor.rowcount, "record(s) affected")
    except:
        print("Enter Correct Data")

while True:
    print('''
    -> Press 1 for Insert.
    -> Press 2 for Delete.
    -> Press 3 for Update.
    -> Press 4 for Exit Program''')

    try:
        choice = int(input("Enter :"))
        if choice == 1:
            insert()
        elif choice == 2:
            delete()
        elif choice == 3:
            update()
        elif choice == 4:
            break
        
    except:
        pass
