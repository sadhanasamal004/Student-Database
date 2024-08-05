            # PROJECT 2: STUDENT DATABASE MANAGEMENT SYSTEM

from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox

def run_query(query,parameter=()):
    con=psycopg2.connect(dbname='studentdb',user='postgres',password='systemm',host='localhost',port='5432')
    cur=con.cursor()
    query_result=None
    try:
        cur.execute(query,parameter)
        if query.lower().startswith('select'):
            query_result=cur.fetchall()
        con.commit()
    except psycopg2.Error as e:
        messagebox.showerror('Database Error',str(e))
    finally:
        cur.close()
        con.close()
    return query_result

def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item)
    records=run_query('select * from students;')
    for record in records:
        tree.insert('',END,values=record)

def insert_data():
    query='insert into students(name,age,number) values (%s,%s,%s)'
    parameters=(name_entry.get(),age_entry.get(),number_entry.get())
    run_query(query,parameters)
    messagebox.showinfo('Information','Data inserted successfully')
    refresh_treeview()

def delete_data():
    selected_item=tree.selection()[0]
    student_id=tree.item(selected_item)['values'][0]
    query='delete from students where id=%s'
    parameter=(student_id,)
    run_query(query,parameter)
    messagebox.showinfo('Information','Data deleted successfully')
    refresh_treeview()

def update_data():
    selected_item=tree.selection()
    student_id=tree.item(selected_item)['values'][0]
    query='update students set name=%s,age=%s,number=%s where id=%s'
    parameter=(name_entry.get(),age_entry.get(),number_entry.get(),student_id)
    run_query(query,parameter)
    messagebox.showinfo('Information','Data updated successfully')
    refresh_treeview()

def create_table():
    query='create table if not exists students(id serial primary key,name text,age int,number text)'
    run_query(query)
    messagebox.showinfo("Information",'Table created')
    refresh_treeview()

root=Tk()
root.title('Student Manangement system')

frame=LabelFrame(root,text='STUDENT DATA',bd='10px',cursor='circle',font=('Algerian',20),bg='hotpink')
frame.grid(row=0,column=0,padx=10,pady=10,sticky='ew')

Label(frame,text='Name:',bg='peach puff',font=('Constantia',18),padx='10px',pady='5px').grid(row=0,column=0,padx=2,sticky='w')
name_entry=Entry(frame,font=('Sylfaen',20))
name_entry.grid(row=0,column=1,pady=2,sticky='ew')
Label(frame,text='Age:',bg='cornflower blue',font=('Constantia',18),padx='10px',pady='5px').grid(row=1,column=0,padx=2,sticky='w')
age_entry=Entry(frame,font=('Sylfaen',20))
age_entry.grid(row=1,column=1,pady=2,sticky='ew')
Label(frame,text='Phone Number:',bg='yellow',font=('Constantia',18),padx='10px',pady='5px').grid(row=2,column=0,padx=2,sticky='w')
number_entry=Entry(frame,font=('Sylfaen',20))
number_entry.grid(row=2,column=1,pady=2,sticky='ew')

button_frame=Frame(root)
button_frame.grid(row=1,column=0,pady=5,sticky='ew')

Button(button_frame,text='Create Table',command=create_table,bg='gold',activebackground='cyan',font=('Constantia',15)).grid(row=0,column=0,padx=50)
Button(button_frame,text='Add Data',command=insert_data,bg='gold',activebackground='cyan',font=('Constantia',15)).grid(row=0,column=1,padx=50)
Button(button_frame,text='Update Data',command=update_data,bg='gold',activebackground='cyan',font=('Constantia',15)).grid(row=0,column=2,padx=50)
Button(button_frame,text='Delete Data',command=delete_data,bg='gold',activebackground='cyan',font=('Constantia',15)).grid(row=0,column=3,padx=50)

tree_frame=Frame(root,bg='cyan')
tree_frame.grid(row=2,column=0,padx=10,sticky='nsew')

tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode='browse')
tree.pack()
tree_scroll.config(command=tree.yview)

style=ttk.Style()
style.configure('Treeview.Heading',font=('Constantia',18))
style.configure('Treeview',font=('Baskerville Old Face',13))

tree['columns']=('student_id','name','age','number')
tree.column('#0',width=0,stretch=NO)
tree.column('student_id',anchor=CENTER,width=80)
tree.column('name',anchor=CENTER,width=180)
tree.column('age',anchor=CENTER,width=80)
tree.column('number',anchor=CENTER,width=180)

tree.heading('student_id',text='ID',anchor=CENTER)
tree.heading('name',text='Name',anchor=CENTER)
tree.heading('age',text='Age',anchor=CENTER)
tree.heading('number',text='Phone Number',anchor=CENTER)

refresh_treeview()

root.mainloop()