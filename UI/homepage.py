from http.client import OK
from tkinter import *

def registration():
    root.destroy()
    import registration
def login():
    root.destroy()
    import login
def Logout():
    root.destroy()
# class main_button:
# def registration_button():
# def recognize_button():
# def sentiment_button():
# def login_button():
# def exit_button():


root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.minsize((int(width)),(int(height)))
root.title("Home Page")
canvas2 = Canvas( root, width = 800,
                 height = 50,bg="#ffcaaf")
                 
canvas2.pack(fill = "both", expand = True,side=TOP) 

Button(canvas2, text="Add User", command=registration,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(row=0,column=2,padx=3,pady=6)
# registration_button()
Button(canvas2, text="Recognize", command=OK,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(row=0,column=3,padx=3,pady=6)
# recognize_button()
Button(canvas2, text="Sentiment", command=OK,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(row=0,column=4,padx=3,pady=6)
# sentiment_button()
Button(canvas2, text="Login", command=login,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(row=0,column=5,padx=3,pady=6)
# login_button()
Button(canvas2, text="Exit", command=Logout,height=1,width=8,padx=5,pady=3,bg="#606060",fg="#FFFFFF").grid(row=0,column=6,padx=3,pady=6)
# exit_button()

bg = PhotoImage(file = "recog.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 1200,
                 height = 1200 )
  
canvas1.pack(fill = "both", expand = True,side=TOP)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw" )

root.mainloop()