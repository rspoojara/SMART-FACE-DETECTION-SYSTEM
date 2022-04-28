from datetime import datetime
from time import strftime
from cgitb import text
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1355x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text = "FACE RECOGNITION", font = ("times new roman", 35, "bold"),bg="white", fg="green")
        title_lbl.place(x = 0,y = 0, width = 1355, height = 45)

    #1st image
        img_top = Image.open(r"C:\SFDS\images\background.jpg")
        img_top = img_top.resize((650,700), Image.ANTIALIAS)
        self.img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image= self.img_top)
        f_lbl.place(x = 0, y = 55, width = 650, height = 700)

    #2nd image
        img_bottom = Image.open(r"C:\SFDS\images\background.jpg")
        img_bottom = img_bottom.resize((950,700), Image.ANTIALIAS)
        self.img_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root,image= self.img_bottom)
        f_lbl.place(x = 650, y = 55, width = 950, height = 700)

    # button
        b1_1 = Button(f_lbl,command=self.face_recog, text = "Face Recognition", cursor = "hand2",font =("times new roman", 30, "bold"), bg = "darkgreen", fg = "white")
        b1_1.place(x =365, y = 500, width = 300, height = 40)

    def mark_attendance(self,i,r,n,d):
        with open("Dhruvil.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
                name_list.append(entry[5])
                print(name_list)
                today = datetime.now()
                t1 = today.strftime("%d/%m/%y")
            if((i not in name_list) and (t1 not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")


#================================= Face Recognition =========================================#

    def face_recog(self):
        def draw_boundry(img, claasifier, scaleFactor, minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = claasifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h,x:x+w])
                print(id)
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute(f"select Name from student where Student_id ={str(id)}")
                n = my_cursor.fetchone()
                print(n)
                n = "+".join(n)

                my_cursor.execute(f"select Roll from student where Student_id ={id}")
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(f"select Dep from student where Student_id = {id}")
                d = my_cursor.fetchone()
                d = "+".join(d)



                if confidence>77:
                    cv2.putText(img, f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8, (255,255,255),3 )
                    cv2.putText(img, f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8, (255,255,255),3 )
                    cv2.putText(img, f"Dep: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8, (255,255,255),3 )
                    self.mark_attendance(id,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, f"Unkown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8, (255,255,255),3 )

                coord = [x,y,w,y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
