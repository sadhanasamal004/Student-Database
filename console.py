import psycopg2

def create_table():
    con=psycopg2.connect(dbname='studentdb',user='postgres',password='systemm',host='localhost',port='5432')
    cur=con.cursor()
    cur.execute('create table students(id serial primary key,name text,age int,number text);')
    print('Table created')
    con.commit()
    con.close()

def insert_data():
    con=psycopg2.connect(dbname='studentdb',user='postgres',password='systemm',host='localhost',port='5432')
    cur=con.cursor()
    name=input('Enter your name:')
    age=int(input('Enter your age:'))
    number=input('Enter your number:')
    cur.execute("insert into students(name,age,number) values (%s,%s,%s)",(name,age,number))
    print('Data inserted')
    con.commit()
    con.close()

def update_data_all():
    con=psycopg2.connect(dbname='studentdb',user='postgres',password='systemm',host='localhost',port='5432')
    cur=con.cursor()
    id=int(input('Enter the student id:'))
    name=input('Enter your name:')
    age=int(input('Enter your age:'))
    number=input('Enter your number:')
    cur.execute('update students set name=%s,age=%s,number=%s where id=%s',(name,age,number,id))
    print('Data updated')
    con.commit()
    con.close()
def update_data_single():
    con=psycopg2.connect(dbname='studentdb',user='postgres',password='systemm',host='localhost',port='5432')
    cur=con.cursor()
    id=int(input('Enter the student id:'))
    data={
        '1':('name','Enter the new name:'),
        '2':('age','Enter the new age:'),
        '3':('number','Enter the new number:')
    }
    for i in data:
        print(f'{i}:{data[i][0]}')
    choice=input('Enter your choice:')
    if choice in data:
        a,b=data[choice]
        new_value=input(b)
        command=f'update students set {a}=%s where id=%s'
        cur.execute(command,(new_value,id))
        print('Updated successfully')

    else:
        print('Invalid choice')
    con.commit()
    con.close()
def delete_data():
    id=input('Enter the student id:')
    con=psycopg2.connect(dbname='studentdb',user='postgres',password='systemm',host='localhost',port='5432')
    cur=con.cursor()
    cur.execute('select * from students where id=%s',(id))
    stud=cur.fetchone()
    if stud:
        print(f'Student to be deleted:\nName:{stud[0]}\nAge:{stud[1]}\nNumber:{stud[2]}')
        choice=input('Are you sure to delete the data(y/n)?')
        if choice=='y':
            cur.execute('delete from students where id=%s',(id))
            print('Data deleted')
        else:
            print('Deletion cancelled')
    else:
        print('Student not found')
    con.commit()
    con.close()    
def read_data():
    con=psycopg2.connect(dbname='studentdb',user='postgres',password='systemm',host='localhost',port='5432')
    cur=con.cursor()
    cur.execute('select * from students;')
    stud=cur.fetchall()
    print('The students are:')
    for s in stud:
        print(f'Student id:{s[0]}\tName:{s[1]}\tAge:{s[2]}\tNumber:{s[2]}')
    con.commit()
    con.close()
while True:
    print('\t\t-----------WELCOME TO THE DATABASE-----------')
    print('1.CREATE TABLE')
    print('2.INSERT DATA IN THE TABLE')
    print('3.UPDATE A SINGLE VALUE IN THE TABLE')
    print('4.UPDATE ALL THE VALUES IN THE TABLE')
    print('5.DELETE THE DATA IN THE TABLE')
    print('6.READ ALL THE DATA IN THE TABLE')
    print('7.EXIT')
    choice=int(input('Enter your choice:'))
    if choice==1:
        create_table()
    elif choice==2:
        insert_data()
    elif choice==3:
        update_data_single()
    elif choice==4:
        update_data_all()
    elif choice==5:
        delete_data()
    elif choice==6:
        read_data()
    elif(choice==7):
        print('\t\t-----------------THANK YOU-----------------')
        exit(0)
    else:
        print('Invalid choice')