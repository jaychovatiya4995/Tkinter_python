from tkinter import *
from tkinter import Message
from tkinter import ttk
from PIL import ImageTk, Image
from control import *
from control import l1


win = Tk()
win.title('Employee Management System')
win.geometry('650x650')
win.resizable(0,0)
# -----------------------functions----------------------------------------------------------
# sreach
#------ exit --------
def exit():
    win.destroy()
#----- onoff --------
def onoff(btn1):
    if btn1['text'] == 'On':
        identry.config(state=NORMAL)
        abtn.config(state=DISABLED)
        btn1['text'] = 'Off'
    elif btn1['text'] == 'Off':
        identry.config(state=DISABLED)
        abtn.config(state=NORMAL)
        btn1['text'] = 'On'
        

# ---- add ----------
def add():
    # e_id = eid.get()
    e_nm = enm.get()
    e_add = eadd.get()
    e_ct = ect.get()
    e_bd = ebd.get()
    e_ms = ems.get()
    e_d = ed.get()
    e_cls = ecls.get()
    e_g = eg.get()

    if e_nm == "" or e_add == "" or e_ct == "" or e_bd == "" or e_ms == "" or e_d == "" or e_cls == "" or e_g == "":
        messagebox.showwarning('Fill Data','Fill or the fileds to add new data')
    else:
        i_qu = '''insert into emplooye_data (empname,empaddress,empcity,empbdata,monthlysalary,classofemployee,gender,empdes)  
                values (%s,%s,%s,%s,%s,%s,%s,%s)''' 
        i_vl = (e_nm, e_add, e_ct, e_bd, e_ms, e_d, e_cls, e_g)
        mc.execute(i_qu,i_vl)
        mdb.commit()
        messagebox.showinfo('Insert','Data Save Successfully')
        
#------------------------ Title frame ------------------------------------------------------
f1 = Frame(win,width=650,height=200,bg='#c2bfd9')
f1.pack(side=TOP)   
i1 = Image.open('shop1.jpg')
i1 = i1.resize((665,200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(i1)
i1_lbl = Label(f1,image=img)
i1_lbl.place(x=0,y=0)
menu = Menu(f1,bg='#c2bfd9')
menu.add_command(label='Exit',command=exit)
#--------------------- Input frame -----------------------------------------------------------------
f2 = Frame(win,width=650,height=460,bg='#c2bfd9',highlightthickness=0,highlightcolor="#c2bfd9")
f2.pack()
#------------------- lable ---------------------------------------------------------------
Label(f2,text='Emplyooe Id',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=0,column=1,sticky='w')
Label(f2,text='Emplyooe Name',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=1,column=1,sticky='w')
Label(f2,text='Emplyooe Address',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=2,column=1,sticky='w')
Label(f2,text='City',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=3,column=1,sticky='w')
Label(f2,text='Brith Date',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=4,column=1,sticky='w')
Label(f2,text='Monthly Salary',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=5,column=1,sticky='w')
Label(f2,text='Designation',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=6,column=1,sticky='w')
Label(f2,text='Class',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=7,column=1,padx=0,pady=10,sticky='w')
Label(f2,text='Gender',font='Helvetica 12 bold',bg='#c2bfd9').grid(row=9,column=1,sticky='w')
Label(f2,text='Dsign and Devloped by \n Shahilsha',bg='#c2bfd9').grid(row=15,column=0)


#------------------------ entry -------------------------------------------------------
#----------- entry varible -----------------
eid = StringVar()
enm = StringVar()
eadd = StringVar()
ect = StringVar()
ebd = StringVar()
ems = StringVar()
ed = StringVar()
ecls = StringVar()
eg = StringVar()

#--------- Entry box ------------------------
identry = Entry(f2,textvariable=eid)
identry.grid(row=0, column=2,sticky='w')

Entry(f2,textvariable=enm).grid(row=1, column=2,sticky='w')
Entry(f2,textvariable=eadd).grid(row=2, column=2,sticky='w')
Entry(f2,textvariable=ect).grid(row=3,column=2,sticky='w')
Entry(f2,textvariable=ebd).grid(row=4,column=2,sticky='w')
Entry(f2,textvariable=ems).grid(row=5,column=2,sticky='w')

#---------- Combo box -------------------------
c1 = ttk.Combobox(f2,textvariable=ed)
# c1['values'] = ['Project Managere','Human Resources','Data Scenticest','Junior Devloper','Clark','Intern']
c1['values'] = l1
c1.grid(row=6,column=2,padx=0, pady=10,sticky='w')

#---------- Radiobutton -----------------------
Radiobutton(f2,text='Class I',variable=ecls,bg='#c2bfd9',value=1).place(x=280,y=265)
Radiobutton(f2,text='Class II',variable=ecls,bg='#c2bfd9',value=2).place(x=360,y=265)
Radiobutton(f2,text='Class III',variable=ecls,bg='#c2bfd9',value=3).place(x=440,y=265)
Radiobutton(f2,text='Male',variable=eg,bg='#c2bfd9',value=1).place(x=280,y=300)
Radiobutton(f2,text='Female',variable=eg,bg='#c2bfd9',value=2).place(x=360,y=300)
Radiobutton(f2,text='Other',variable=eg,bg='#c2bfd9',value=3).place(x=440,y=300)

#----------- Button -----------------------------

fbtn = Button(f2,text='First                 ',activeforeground='blue',bg='orange',fg='white',relief='solid')
fbtn.grid(row=1, column=5,padx=10, pady=10,sticky='w')

pbtn = Button(f2,text='< Previous     ',activeforeground='blue',bg='orange',fg='white',relief='solid')
pbtn.grid(row=3, column=5,padx=10, pady=10,sticky='w')

lbtn = Button(f2,text='Last                 ',activeforeground='blue',bg='orange',fg='white',relief='solid')
lbtn.grid(row=4, column=5,padx=10, pady=10,sticky='w')

nbtn = Button(f2,text='Next >            ',activeforeground='blue',bg='orange',fg='white',relief='solid')
nbtn.grid(row=2,column=5,padx=10, pady=0,sticky='w')

btn1 = StringVar()
btn = Button(f2,text='On',bg='silver',command=lambda : onoff(btn))
btn.grid(row=0,column=4)

sbtn = Button(f2,text='Search',activeforeground='green',bg='blue',fg='white',command=show)
sbtn.grid(row=0,column=5,sticky='s')

abtn = Button(f2,text='Add New',height=2,width=8,bg='blue',fg='white',relief='solid',command=add)
abtn.place(x=10,y=10)

dbtn = Button(f2,text='Delete',height=2,width=8,bg='red',fg='white',relief='solid')
dbtn.place(x=10,y=60)

ubtn = Button(f2,text='Update',height=2,width=8,bg='blue',fg='white',relief='solid')
ubtn.place(x=10,y=110)

cbtn = Button(f2,text='Clear',height=2,width=8,bg='red',fg='white',relief='solid')
cbtn.place(x=10,y=160)

win.config(menu=menu,bg='#c2bfd9')
win.mainloop()