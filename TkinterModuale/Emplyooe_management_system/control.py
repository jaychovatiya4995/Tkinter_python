import mysql.connector as con
# from model import *
# from model import  enm, eadd, ect, ebd, ems, ed, ecls, eg
from tkinter import messagebox

mdb = con.connect(host='localhost',user='root',password='password',database='employee_master')

mc = mdb.cursor()

# feach designation 
l1 = []
mc.execute('select destination from emp_des')
re = mc.fetchall()
for i in re:
    l1.append(i)

def show():
    mc.execute('show tables')

    for i in mc:
        print(i)   


# def add():
#     # e_id = eid.get()
#     e_nm = enm.get()
#     e_add = eadd.get()
#     e_ct = ect.get()
#     e_bd = ebd.get()
#     e_ms = ems.get()
#     e_d = ed.get()
#     e_cls = ecls.get()
#     e_g = eg.get()

#     i_qu = '''insert into emplooye_data (empname,empaddress,empcity,empbdata,monthlysalary,classofemployee,gender,empdes)  
#               values (%s,%s,%s,%s,%s,%s,%s,%s)''' 
#     i_vl = (e_nm, e_add, e_ct, e_bd, e_ms, e_d, e_cls, e_g)
#     mc.execute(i_qu,i_vl)
#     mdb.commit()
#     messagebox.showinfo('Insert','Data Save Successfully')