import tkinter.messagebox
from tkinter import*
import os
from tkinter import ttk
from PIL import Image,ImageTk

from attendence import Attendence
from student import Student
from train import Train
from face_rocognition import Face_Recognition



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1355x720+0+0")
        self.root.title("Face Recognition System")

        #First Image
        img=Image.open(r"C:\SFDS\images\logo.png")
        img=img.resize((1350,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1350,height=130)

        #Background Image
        img3=Image.open(r"C:\SFDS\images\background.jpg")
        img3=img3.resize((1340,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1350,height=520)

        title_lbl=Label(bg_img ,text="Face Recognition Attedence System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)


        #Student Button

        img4=Image.open(r"C:\SFDS\images\student.jpg")
        img4=img4.resize((190,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=75,width=190,height=190)

        b1_1=Button(bg_img,text="student details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=240,width=190,height=40)



        # Detect face Button
        img5=Image.open(r"C:\SFDS\images\facedetector.jpg")
        img5=img5.resize((190,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,command=self.face_data,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=75,width=190,height=190)

        b1_1=Button(bg_img,command=self.face_data,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=240,width=190,height=40)


        #Attedence face button

        img6=Image.open(r"C:\SFDS\images\attendence.png")
        img6=img6.resize((190,190),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,command=self.attendance,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=75,width=190,height=190)

        b1_1=Button(bg_img,command=self.attendance,text="Attedence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=240,width=190,height=40)


        # #Help  face Button
        # img7=Image.open(r"C:\Users\ASUS\Desktop\FRDS\Images\  .....       ")
        # img7=img.resize((500,130),Image.ANTIALIAS)
        # self.photoimg7=ImageTk.PhotoImage(img7)
        #
        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        # b1.place(x=175,y=75,width=190,height=190)
        #
        # b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        # b1_1.place(x=175,y=75,width=190,height=40)
        #
        #
        #Train face Button

        img8=Image.open(r"C:\SFDS\images\train.jpg")
        img8=img8.resize((190,190),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=310,width=190,height=190)

        b1_1=Button(bg_img,command=self.train_data,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=475,width=190,height=40)


        #Photos Face Button
        img9=Image.open(r"C:\SFDS\images\photo.png")
        img9=img9.resize((190,190),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=310,width=190,height=190)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=500,y=475,width=190,height=40)



        #Developer Face Button
        # img10=Image.open(r"C:\SFDS\images\logo.png")
        # img10=img.resize((190,190),Image.ANTIALIAS)
        # self.photoimg10=ImageTk.PhotoImage(img10)
        #
        # b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        # b1.place(x=800,y=310,width=190,height=190)
        #
        # b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        # b1_1.place(x=800,y=475,width=190,height=40)


        # #Exit Face Button
        img11=Image.open(r"C:\SFDS\images\exit.jpg")
        img11=img11.resize((190,190),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,command=self.iExit,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=310,width=190,height=190)

        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=800,y=475,width=190,height=40)

    def open_img(self):
        os.startfile("data")

        #========================Functions buttons======================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this window",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()