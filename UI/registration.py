from tkinter import *

win = Tk()

win.geometry()
width, height = win.winfo_screenwidth(), win.winfo_screenheight()
win.geometry('%dx%d+0+0' % (width,height))
win.minsize((int(width/2)),(int(height)))
win.configure(bg="#CBC3E3")


def login():
    win.destroy()
    print(f"{name_value.get(),employeeId_value.get(),email_value.get(),mobileNo_value.get(),dateOfBirth_value.get(),age_value.get(),gender_value.get(),bloogGroup_value.get(),department_value.get()}")
    import login
def homepage():
    win.destroy()
    import homepage



Button(win , text="<--", command=homepage,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(sticky="w")
frame = Frame(win ,borderwidth=3,relief=SUNKEN,padx=130,pady=80,bg="#FFFFFF",height="1020",width="400")
frame.grid(padx="400")
win.title("Add User")
name_value = StringVar()
employeeId_value = StringVar()
email_value = StringVar()
mobileNo_value = StringVar()
dateOfBirth_value = StringVar()
age_value = StringVar()
gender_value = IntVar()
bloogGroup_value = StringVar()
department_value = StringVar()


Label(frame,text="Add User",font=("calibri", 20),bg="#FFFFFF").grid(columnspan=2,padx=30,pady=30)

name = Label(frame , text="Name",font=("calibri", 14),bg="#FFFFFF").grid(row=2,column=0,padx=3,pady=3,sticky="w")
name_entry = Entry(frame , textvariable= name_value).grid(row=2,column=1,padx=3,pady=3)

employeeId = Label(frame , text="Employee ID ",font=("calibri", 14),bg="#FFFFFF").grid(row=3,column=0,padx=3,pady=3,sticky="w")
employeeid_entry = Entry(frame , textvariable=employeeId_value).grid(row=3,column=1,padx=3,pady=3)

email=Label(frame, text="Email ", font=("calibri", 14),bg="#FFFFFF").grid(row=4,column=0,padx=3,pady=3,sticky="w")
email_entry = Entry(frame , textvariable=email_value).grid(row=4,column=1,padx=3,pady=3)

mobileNo=Label(frame,text="Mobile No. ",font=("calibri", 14),bg="#FFFFFF").grid(row=5,column=0,padx=3,pady=3,sticky="w")
mobileno_entry = Entry(frame , textvariable=mobileNo_value).grid(row=5,column=1,padx=3,pady=3)

dateOfBirth=Label(frame,text="Birth Date ",font=("calibri", 14),bg="#FFFFFF").grid(row=6,column=0,padx=3,pady=3,sticky="w")
dateofbirth_entry = Entry(frame , textvariable=dateOfBirth_value).grid(row=6,column=1,padx=3,pady=3)

age=Label(frame,text="Age ", font=("calibri", 14),bg="#FFFFFF").grid(row=7,column=0,padx=3,pady=3,sticky="w")
age_entry = Entry(frame , textvariable=age_value).grid(row=7,column=1,padx=3,pady=3)

gender=Label(frame,text="Gender ",font=("calibri", 14),bg="#FFFFFF").grid(row=8,column=0,padx=6,pady=3,sticky="w")

Radiobutton(frame, text='Male',variable=gender_value,value=1,bg="#FFFFFF").grid(row=8,column=1)
Radiobutton(frame, text='Female',variable=gender_value,value=2,bg="#FFFFFF").grid(row=8,columnspan=2)

bloodGroup=Label(frame,text="Blood Group ",font=("calibri", 14),bg="#FFFFFF").grid(row=9,column=0,padx=3,pady=3,sticky="w")
bloodgroup_entry = Entry(frame , textvariable=bloogGroup_value).grid(row=9,column=1,padx=3,pady=3)

department=Label(frame,text="Department ",font=("calibri", 14),bg="#FFFFFF").grid(row=10,column=0,padx=3,pady=3,sticky="w")
department_entry = Entry(frame , textvariable=department_value).grid(row=10,column=1,padx=3,pady=3)



Button(frame, text="submit", command=login,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(columnspan=2,padx=3,pady=30)




win.mainloop()