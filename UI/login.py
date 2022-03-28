from tkinter import *

root = Tk()
root.geometry()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.minsize((int(width/2)),(int(height/2)))

def registration():
    root.destroy()
    import registration

def homepage():
    print(f"{user_value.get(),pass_value.get()}")
    root.destroy()
    import homepage

user_value = StringVar()
pass_value = StringVar()
f1 = Frame(root ,borderwidth=3,relief=SUNKEN,padx=100,bg="#FFFFFF",width="1020",height="400")
f1.pack(pady=100,)
root.title("Login")
root.configure(bg="#CBC3E3")

Label(f1,text= "Login",font=("calibri", 25),bg="#FFFFFF").grid(columnspan=2,padx=16,pady=16)
user = Label(f1 , text="Username",font=1,bg="#FFFFFF").grid(row=2,column=0,padx=3,pady=3)
user_entry = Entry(f1 , textvariable=user_value).grid(row=2,column=1,padx=3,pady=3)
password = Label(f1 , text="Password",font=1,bg="#FFFFFF").grid(row=3,column=0,padx=3,pady=3)
pass_entry = Entry(f1 , textvariable=pass_value,show="*").grid(row=3,column=1,padx=3,pady=3)



Button(f1, text="Login", command=homepage,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(row=4,column=0,padx=3,pady=30)
Button(f1, text="Registration",height=1,width=14,padx=5,pady=3,command=registration,bg="#606060",fg="#FFFFFF").grid(row=4,column=1,padx=3,pady=30)


root.mainloop()