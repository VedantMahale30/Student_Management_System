from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

import matplotlib.pyplot as plt
from matplotlib import pyplot
import requests

def f1():
	mw.withdraw()
	aw.deiconify()


def f2():
	aw.withdraw()
	mw.deiconify()


def f3():
	mw.withdraw()
	uw.deiconify()


def f4():
	vw.withdraw()
	mw.deiconify()


def f5():
	con = None
	try:
		con = connect("pro.db")
		cursor = con.cursor()
		sql = "insert into employee values('%d', '%s', '%d')"

		aw_ent_eid.focus()
		id = aw_ent_eid.get()
		tid = int(aw_ent_eid.get())
		if  tid < 0:
			showwarning("Notice", "Id Cannot be Negative")
			eid = int(aw_ent_sal.get())
			raise Exception("Id Cannot be Negative.")

		elif tid == 0:
			showwarning("Notice", "Id Cannot be 0")
			eid = int(aw_ent_sal.get())
			raise Exception("Id Cannot be 0.")

		elif not (id.isdigit()):
			showwarning("Notice", "Id Should Contain Numbers Only")
			eid = int(aw_ent_sal.get())

		else:
			eid = int(aw_ent_eid.get())



		name = aw_ent_name.get()
		if not (name.isalpha()):
			showwarning("Notice", "Name should contain letters only.")
			raise Exception("Name should contain letters only.")

		elif not len(name) > 2:
			showwarning("Notiice", "Name should contain at least 2 letters.")
			raise Exception("Name should contain letters only.")
		else:
			name = aw_ent_name.get()


		sal = aw_ent_sal.get()
		if not (sal.isdigit()):
			showwarning("Notice", "Salary Should Contain Numbers Only")
		else:
			sal = int(aw_ent_sal.get())

			if sal < 12000 :
				showwarning("Notice", "Salary should be greater than 12000")
				raise Exception("Salary should be greater than 12000.")


		cursor.execute(sql % (eid, name, sal))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Done", "Record Added")
		else:
			showwarning("OOPS", "Id does not exist")

	except IntegrityError:
		showerror("Mistake", "Id Already Exists")

	except ValueError:
		showerror("Mistake", "No field should be empty")


	finally:
		aw_ent_eid.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_sal.delete(0, END)
		aw_ent_eid.focus()
		if con is not None:
			con.close()


def f6():
	mw.withdraw()
	vw.deiconify()
	con = None
	vw_st_data.delete(1.0, END)

	try:
		con = connect("pro.db")
		cursor = con.cursor()
		sql = "select * from employee "
		cursor.execute(sql)
		data = cursor.fetchall()		
		info = ""
		for d in data:
			info += "ID " +str(d[0]) + " Name " +str(d[1]) + " Salary " +str(d[2]) + "\n"		
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showrerror("Mistake", e)
	finally:
		aw_ent_eid.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_sal.delete(0, END)
		aw_ent_eid.focus()
	if con is not None:
		con.close()

def f7():
	vw.withdraw()
	aw.deiconify()

def f8():
	uw.withdraw()
	mw.deiconify()

def v_back():
	pass


def u_save():
	con = None
	try:
		con = connect("pro.db")
		sql = "update employee set name='%s', sal=%d where eid='%d'"
		cursor = con.cursor()

		id = uw_ent_eid.get()
		if not (id.isdigit()):
			showwarning("Notice", "Id Should Contain Positive Numbers Only")
			eid = int(uw_ent_sal.get())


		else:
			eid = int(uw_ent_eid.get())

		name = uw_ent_name.get()
		if not (name.isalpha()):
			showwarning("Notiice", "Name should contain letters only.")
			raise Exception("Name should contain letters only.")
		elif not len(name) > 2:
			showwarning("Notiice", "Name should contain at least 2 letters.")
			raise Exception("Name should contain at least 2 letters.")

		else:
			name = uw_ent_name.get()

		sal = uw_ent_sal.get()
		if not (sal.isdigit()):
			showinfo("Notice", "Salary Should Contain Numbers Only")
		else:
			sal = int(uw_ent_sal.get())
			if sal < 12000 :
				showwarning("Notice", "Salary should be greater than 12000")
				raise Exception("Salary should be greater than 12000.")


		cursor.execute(sql%(name, sal, eid))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Done", "Record Updated")
		else:
			showwarning("OOPS", "Id does not exist")

	except IntegrityError:
		showerror("Mistake", "Id Already Exists")

	except ValueError:
		showerror("Mistake", "No field should be empty")

	except Exception as e:
		con.rollback()
		showerror("issue ",e)

	finally:
		uw_ent_eid.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_sal.delete(0, END)
		uw_ent_eid.focus()

		if con is not None:
			con.close()

def dw_back():
	dw.withdraw()
	mw.deiconify()
	
def dw_open():
	mw.withdraw()
	dw.deiconify()

def delete():
	con = None
	try:
		con = connect("pro.db")
		sql = "delete from employee where eid='%d'"
		cursor = con.cursor()

		dw_ent_eid.focus()
		eid = int(dw_ent_eid.get())
		cursor.execute(sql%(eid))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Notice","Employee Record Deleted")
		else:
			showwarning("Error","Id does not exist")

	except ValueError:
		showerror("Error", "Id Should Contain Positive Numbers Only")

	except Exception as e:
		con.rollback()
		showerror("issue ",e)
	finally:
		dw_ent_eid.delete(0, END)
		if con is not None:
			con.close()


def addlabels(x, y):
	for i in range(len(x)):
		plt.text(i,y[i],y[i])


def chart():
	con = None
	try:
		con=connect("pro.db")
		cursor=con.cursor()
		sql = "select name, sal from employee order by sal desc limit 5"
		cursor.execute(sql)
		data=cursor.fetchall()
		name=[]
		salary=[]
		for d in data:
			name.append(d[0])
			salary.append(d[1])

		plt.bar(name, salary, color=["yellow", "green", "red"],width=0.5)
		addlabels(name, salary)			

		plt.xlabel("Name")
		plt.ylabel("Salary")
		plt.title("Salary Of Top 5 Employees")
		plt.show()

	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()

mw = Tk()
mw.title("E.M.S")
mw.geometry("700x600+90+90")
mw.configure(bg="black")

f=("Arial" ,23 , "bold")
fs=("Arial" ,12 )
y = 10
	
try:

	wa = "https://ipinfo.io"
	res = requests.get(wa)
#	print(res)
	data = res.json()
#	print(data)
	city = data["city"]
#	print(data)
	city = data["city"]
	print("city = ", city)
	state = data["region"]
#	print("state = ", state)
	loc = data["loc"]
	latlong = loc.split(",")
	lat = latlong[0]
	lng = latlong[1]
#	print("Lattitude = ", lat)
#	print("Longitude = ", lng)

	a1 = "https://api.openweathermap.org/data/2.5/weather"
	a2="?q=" + city
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units="+"metric"

	wa = a1 + a2+ a3 + a4
	res = requests.get(wa)
#	print(res)
	data = res.json()
#	print(data)
	temp = data["main"]["temp"]
#	print("Temprature of ", city, " is = ", temp)

except Exception as e:
	print("issue",e)


mw_btn_add = Button(mw, text="Add Employees", font=f, width=15, bg="khaki1", command=f1)
mw_btn_view = Button(mw, text="View Employees", font=f, width=15, command=f6, bg="SeaGreen1")
mw_btn_add.pack(pady=y)
mw_btn_view.pack(pady=y)
mw_btn_update = Button(mw, text="Update Employees", font=f, width=15, bg = "LightBlue1" , command=f3)
mw_btn_delete = Button(mw, text="Delete Employees", font=f, width=15, command=dw_open, bg="OrangeRed2")
mw_btn_charts = Button(mw, text="Charts", font=f, width=15, command=chart)
mw_btn_update.pack(pady=y)
mw_btn_delete.pack(pady=y)
mw_btn_charts.pack(pady=y)

lab_cintro = Label(mw, text="You Are In ", bg="black" , fg="white" , font = fs)
lab_cintro.place(x = 20, y = 500)
lab_city = Label(mw, text= city, fg="white" , bg="black" , font = fs )
lab_city.place(x = 125, y = 500)
lab_temp = Label(mw, text= "Temprature ", fg="white" ,bg="black" , font = fs )
lab_temp.place(x = 380, y = 500)
lab_temp = Label(mw, text= temp, fg="white", bg="black", font=fs)
lab_temp.place(x = 500, y = 500)


aw = Toplevel(mw)
aw.title("Add Employee")
aw.geometry("700x600+90+90")
aw.configure(bg="khaki1")

aw_lab_eid = Label(aw, text="Enter Employee ID ", bg="khaki1",font=f)
aw_lab_eid1 = Label(aw, text="Numbers only ", bg="khaki1",font=fs)
aw_ent_eid = Entry(aw, font=f)
aw_lab_eid2 = Label(aw, text="Letters Only ", bg="khaki1",font=fs)
aw_lab_name = Label(aw, text="Enter Name",  bg="khaki1",font=f)
aw_ent_name = Entry(aw, font=f)
aw_lab_sal = Label(aw, text="Enter Salary",  bg="khaki1",font=f)
aw_lab_eid3 = Label(aw, text="Numbers only ", bg="khaki1",font=fs)
aw_ent_sal = Entry(aw, font=f)
aw_btn_save = Button(aw, text="Save", font=f,  bg="khaki1" , command=f5)
aw_btn_back = Button(aw, text="Back", font=f, command = f2,  bg="khaki1")

aw_lab_eid.pack(pady=y)
aw_lab_eid1.pack()
aw_ent_eid.pack(pady=y)
aw_lab_name.pack(pady=y)
aw_lab_eid2.pack()
aw_ent_name.pack(pady=y)
aw_lab_sal.pack(pady=y)
aw_lab_eid3.pack()
aw_ent_sal.pack(pady=y)
aw_btn_save.pack(pady=y)
aw_btn_back.pack(pady=y)
aw.withdraw()


uw = Toplevel(mw)
uw.title("Update Employee")
uw.geometry("700x600+90+90")
uw.configure(bg="LightBlue1")

uw_lab_eid = Label(uw, text="Enter Employee ID", bg = "LightBlue1",font=f)
uw_ent_eid = Entry(uw, font=f)
uw_lab_name = Label(uw, text="Enter Name",  bg="LightBlue1",font=f)
uw_ent_name = Entry(uw, font=f)
uw_lab_sal = Label(uw, text="Enter Salary",  bg="LightBlue1",font=f)
uw_ent_sal = Entry(uw, font=f)
uw_btn_save = Button(uw, text="Save", font=f,  bg="LightBlue1", command=u_save)
uw_btn_back = Button(uw, text="Back", font=f, command = f8,  bg="LightBlue1")

uw_lab_eid.pack(pady=y)
uw_ent_eid.pack(pady=y)
uw_lab_name.pack(pady=y)
uw_ent_name.pack(pady=y)
uw_lab_sal.pack(pady=y)
uw_ent_sal.pack(pady=y)
uw_btn_save.pack(pady=y)
uw_btn_back.pack(pady=y)
uw.withdraw()

vw = Toplevel(mw)
vw.title("View Employees")
vw.geometry("700x600+90+90")
vw.configure(bg="SeaGreen1")


vw_st_data = ScrolledText(vw, width=36, height=11, font=f, bg="SeaGreen1")
vw_btn_back = Button(vw, text="Back", font=f, command=f4, bg="SeaGreen1")
vw_st_data.pack(pady=y)
vw_btn_back.pack(pady=y)
vw.withdraw()

dw = Toplevel(mw)
dw.title("Delete Employees")
dw.geometry("700x600+90+90")
dw.configure(bg="OrangeRed2")

dw_lab_name = Label(dw, text="Enter Employee ID",  bg="OrangeRed2",font=f)
dw_ent_eid = Entry(dw, font=f)
dw_btn_delete = Button(dw, text="Delete", font=f, width=15, command=delete, bg="OrangeRed2")
dw_btn_back = Button(dw, text=" Back ", font=f, command=dw_back, bg="OrangeRed2")
dw_lab_name.pack(pady=y)
dw_ent_eid.pack(pady=y)
dw_btn_delete.pack(pady=y)
dw_btn_back.pack(pady=y)
dw.withdraw()


def confirmExit():
	if askokcancel('exit', 'do you want to exit?'):
		mw.destroy()
mw.protocol('WM_DELETE_WINDOW', confirmExit)


mw.mainloop() 




















