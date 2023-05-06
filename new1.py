from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import ttk, messagebox
import pymysql
win=Tk()
win.geometry("1200x720")
win.resizable(False,False)
img1=ImageTk.PhotoImage(file=r"C:\Users\admin\PycharmProjects\pythonProject1\frame2updated.png")
img_label=Label(win,image=img1)
img_label.place(x=0,y=0,relwidth=1,relheight=1)

# variables
items_var=StringVar()
model_var=StringVar()
type_var=StringVar()
search_by_var=StringVar()
search_entry_var=StringVar()

# combobox them
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'grey',
                                       'fieldbackground': 'gray',
                                       'background': 'brown'
                                       }}}
                         )
combostyle.theme_use('combostyle')
# combo1
item_combo=ttk.Combobox(win,justify='center',font='georgia',width=22,textvariable=items_var)
item_combo['value']=('Glass','Cover','Headphone','Databable')
item_combo.set('Select options ')
item_combo.place(x=160,y=95)
# combo2
model_combo=ttk.Combobox(win,justify='center',font='georgia',width=20,textvariable=model_var)
model_combo['value']=('SAM a12','note 9pro max','Realme c31','Vivo v21')
model_combo.set('Select options ')
model_combo.place(x=190,y=157)
# combo3
type_combo=ttk.Combobox(win,justify='center',font='georgia',width=20,textvariable=type_var)
type_combo['value']=('11D','Super D','Normal','Antiblue','Matt',)
type_combo.set('Select options ')
type_combo.place(x=160,y=225)

# functions
def uplod_data():
    if items_var.get()==""or model_var.get()==""or type_var.get()=="":
        messagebox.showerror("Error","All fields are required to fill")
    else:
        con=pymysql.connect(host="localhost",user="root",password="saurav123",database="saurav")
        cur=con.cursor()
        cur.execute("insert into shop values(%s,%s,%s)",(items_var.get(),model_var.get(),type_var.get(),))


        con.commit()
        fatch_data()
        clear()
        con.close()
        messagebox.showinfo("Success","Recored has be upload")
def fatch_data():
    con=con=pymysql.connect(host="localhost",user="root",password="saurav123",database="saurav")
    cur = con.cursor()
    cur.execute("select * from shop")
    rows=cur.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
        for row in rows:
            table.insert('',END,values=row)
        con.commit()
    con.close()
def get_cuser(ev):
    cur_row=table.focus()
    contents=table.item(cur_row)
    row=contents['values']
    items_var.set(row[0])
    model_var.set(row[1])
    type_var.set(row[2])
    # type_var.delete("1.0", END)
    # type_var.insert(END,row[3])
    # type_var.delete("1.0",END)
    # type_var.insert(END,row[3])

def clear():
    items_var.set('')
    model_var.set('')
    type_var.set('')
def update_data():
    if items_var.get() == "" or model_var.get() == "" or type_var.get() == "":
        messagebox.showerror("Error", "All fields are required to fill")
    else:

        con = pymysql.connect(host="localhost", user="root", password="saurav123", database="saurav")
        cur = con.cursor()
        cur.execute("update shop set items=%s,model=%s where type=%s",(
                items_var.get(), model_var.get(), type_var.get(),))

        con.commit()
        fatch_data()
        clear()
        con.close()
        messagebox.showinfo("Success", "Recored has be Update")

def delete_data():
    if items_var.get() == "" or model_var.get() == "" or type_var.get() == "":
        messagebox.showerror("Error", "All fields are required to fill")
    else:
        con = pymysql.connect(host="localhost", user="root", password="saurav123", database="saurav")
        cur = con.cursor()
        cur.execute("delete from shop where type=%s",(type_var.get(),))
        con.commit()
        con.close()
        fatch_data()
        clear()
def search_data():
    if search_by_var.get() == "" or search_entry_var.get() == "":
        messagebox.showerror("Error","Field are required")
    else:

        con = pymysql.connect(host="localhost", user="root", password="saurav123", database="saurav")
        cur = con.cursor()
        cur.execute("select * from shop where "+str(search_by_var.get())+" LIKE '%"+str(search_entry_var.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            table.delete(*table.get_children())
            for row in rows:
                table.insert('', END, values=row)
            con.commit()
        con.close()


# buttons1
bt1=Button(win,text="Upload",bg="grey",fg="black",width=10,bd=1,font='georgia 10',command=uplod_data)
bt1.place(x=70,y=400,height=19)
# buttons2
bt2=Button(win,text="Update",command=update_data,bg="grey",fg="black",width=10,bd=1,font='georgia 10')
bt2.place(x=250,y=400,height=19)
# buttons3
bt3=Button(win,command=clear,text="Clear",bg="grey",fg="black",width=10,bd=1,font='georgia 10')
bt3.place(x=90,y=470,height=19)
# # buttons4
bt4=Button(win,text="Delete",command=delete_data,bg="grey",fg="black",width=10,bd=1,font='georgia 10')
bt4.place(x=270,y=470,height=19)

# showall_bt=Button(table_frame,text="Show all",font='georgia 8',width=14,height=1,bg="gray")
# showall_bt.place(x=612,y=8,height=19)

# table frame

table_frame=Frame(win,bd=4,relief=RIDGE,bg="black")
table_frame.place(x=430,y=55,width=760,height=600)

search_label=Label(table_frame,text="Search by",fg="black",bg='gray',font="georgia 9",)
search_label.place(x=20,y=10,width=85,height=16)

search_combo=ttk.Combobox(table_frame,font='georgia 8',width=22,justify='center',textvariable=search_by_var)
search_combo['value']=("type","Model","11D",)
# search_combo.set("select opting")
search_combo.place(x=120,y=8,height=18)
search_entry=Entry(table_frame,font="georgia 8",bg="gray",textvariable=search_entry_var)
search_entry.place(x=330,y=8)
# button2
search_bt=Button(table_frame,text="Search",command=search_data,font='georgia 8',width=14,height=1,bg="gray")
search_bt.place(x=500,y=8,height=19)

showall_bt=Button(table_frame,text="Show all",font='georgia 8',width=14,height=1,bg="gray",command=fatch_data)
showall_bt.place(x=612,y=8,height=19)
# treeview

table_frame2=Frame(win,bd=4,relief=RIDGE,bg="black")
table_frame2.place(x=430,y=120,width=760,height=540)
scroll_x=Scrollbar(table_frame2,orient=HORIZONTAL)
scroll_y=Scrollbar(table_frame2,orient=VERTICAL)
table=ttk.Treeview(table_frame2,columns=("items","model","types"),xscrollcommand=scroll_x,yscrollcommand=scroll_y,)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config()
scroll_y.config()

# style2 = ttk.Style(table_frame2)
# style2.theme_use("clam")
# style2.configure("Treeview", background="grey",
#                 fieldbackground="black", foreground="gray")

table.heading("items",text="Items")
table.heading("model",text="Model")
table.heading("types",text="Types")

table['show']='headings'
table.column("items",width=100)
table.column("model",width=100)
table.column("types",width=100)
table.pack(fill=BOTH,expand=1,)
table.bind("<ButtonRelease-1>",get_cuser)
fatch_data()
#

win.mainloop()