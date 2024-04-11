import pymysql as mysql
from tkinter import*
def buttonClick():
 u=e1.get()
 f=e2.get()
 if u=="mohit" and f=="kuk":
    l1['text']='valid user'
 else:
    l1['text']='Invalid user'
def buttonClick2():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)
def buttonclick():
   
   con = mysql.connect(host="localhost", user="root", password="root", database="test1")
   p = con.cursor()
   sql = "INSERT INTO student VALUES (2, 'tttt')"
   p.execute(sql)
   con.commit()
   p.close()
   con.close()


rate=Tk()
rate.geometry("400x400")
rate.title("registration form")
t1=Frame(rate,height=400,width=400,bg='light pink')
t1.pack(fill=BOTH,expand=True)
e1=Entry(t1,width=20,bg='white',fg='black')
e1.pack()
e1.place(x=600,y=200)
e2=Entry(t1,width=20,bg='white',fg='black')
e2.pack()
e2.place(x=600,y=220)
e3=Entry(t1,width=20,bg='white',fg='black')
e3.pack()
e3.place(x=600,y=240)
e4=Entry(t1,width=20,bg='white',fg='black',show='*')
e4.pack()
e4.place(x=600,y=260)
b1=Button(t1,text="save",width=15,fg='black',bg='white',command=buttonClick)
b1.pack()
b1.place(x=600,y=280)
b2=Button(t1,text="clear",width=15,fg='black',bg='white',command=buttonclick)
b2.pack()
b2.place(x=600,y=330)
l1=Label(t1,text='result here ...',width=15)
l1.pack()
l1.place(x=600,y=306)
rate.mainloop()
   