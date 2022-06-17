from tkinter import*
import sqlite3
from tkinter import messagebox
from venv import create

root=Tk()
root.title("Facebook")
root.iconbitmap('facebook.ico')
conn=sqlite3.connect("facebook.db")
c=conn.cursor()


#####create a table#####

# c.execute("""CREATE TABLE users(
#     first_name text,
#     last_name text,
#     age integer,
#     address text,
#     city text,
#     zipcode integer,
#     father_name text,
#     password text
#     )""")
# print("Table created")


#### create Entry box###
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
age=Entry(root,width=30)
age.grid(row=2,column=1)
address=Entry(root,width=30)
address.grid(row=3,column=1)
city=Entry(root,width=30)
city.grid(row=4,column=1)
zip_code=Entry(root,width=30)
zip_code.grid(row=5,column=1)
father_name=Entry(root,width=30)
father_name.grid(row=6,column=1)
password=Entry(root,width=30, show="*")
password.grid(row=7,column=1)

###### Create label#####
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
age_label=Label(root,text="Age")
age_label.grid(row=2,column=0)
address_label=Label(root,text="Address")
address_label.grid(row=3,column=0)
city_label=Label(root,text="City")
city_label.grid(row=4,column=0)
zip_code_label=Label(root,text="Zip Code")
zip_code_label.grid(row=5,column=0)
father_name_label=Label(root,text="Father Name")
father_name_label.grid(row=6,column=0)
password_label=Label(root,text="Password")
password_label.grid(row=7,column=0)


###### create submit button######
def submit():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("INSERT INTO users VALUES(:f_name,:l_name,:age,:address,:city,:zip_code,:father_name,:password)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'age':age.get(),
        'address':address.get(),
        'city':city.get(),
        'zip_code':zip_code.get(),
        'father_name':father_name.get(),
        'password':password.get()
    })

    messagebox.showinfo("Success","Record has been added")
    conn.commit()
    conn.close()
submit_btn=Button(root,text="Submit",command=submit)
submit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

def query():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("SELECT *,oid FROM users")
    records=c.fetchall()
    print_records=''
    for record in records:
        print_records+=str(record[8]) +':'+str(record)+"\n"
    query_label=Label(root,text=print_records)
    query_label.grid(row=9,column=0,columnspan=2)
    conn.commit()
    conn.close()

quary_btn=Button(root,text="Quary",command=query)
quary_btn.grid(row=18,column=0,columnspan=2,pady=10,padx=10,ipadx=100)



conn.commit
conn.close
mainloop()