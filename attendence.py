import csv
import os
from tkinter import *
from tkinter import ttk, filedialog, messagebox

from PIL import Image,ImageTk

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1355x790+0+0")
        self.root.title("face Recognitoin System")

        # .......Variables.........
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attedence = StringVar()

        # first img
        img = Image.open(r"C:\SFDS\images\logo.png")
        img = img.resize((1350, 110), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1350, height=110)

        #  # second img
        # img1=Image.open(r"C:\SFDS\images\background.jpg")
        # img1=img.resize((800,200),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)
        #
        # f_lb1=Label(self.root,image=self.photoimg1)
        # f_lb1.place(x=0,y=0,width=800,height=200)
        #
        # bg img
        img3 = Image.open(r"C:\SFDS\images\background.jpg")
        img3 = img3.resize((1340, 600), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=110, width=1350, height=600)

        title_lbl = Label(bg_img, text="ATTENDENCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=8, y=50, width=1340, height=540)


        # left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Detail",font=("times new roman",20))
        Left_frame.place(x=10,y=10,width=650,height=520)

        img_left=Image.open(r"C:\SFDS\images\background.jpg")
        img_left=img_left.resize((650,130), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0,width=640, height=110)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=115,width=640,height=370)

        # Labeland entry
        # attendance id
        attendanceId_label=Label(left_inside_frame, text="AttendanceId: ", font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid (row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry=ttk. Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        #rollNo
        rollLabel=Label(left_inside_frame, text="Roll:", bg="white", font="comicsansns 12 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll, width=22, font="comicsansns 12 bold")
        atten_roll.grid (row=0, column=3, pady=8)

        # Name
        nameLabel=Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)


        atten_name=ttk.Entry (left_inside_frame,textvariable=self.var_atten_name, width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)



        #Department

        depLabel=Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)


        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep, width=22, font="comicsansns 11 bold")
        atten_dep.grid (row=1, column=3,pady=8)

        #time

        timeLabel=Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time, width=22, font="comicsansns 11 bold")
        atten_time.grid (row=2, column=1, pady=8)

        # Date

        dateLabel=Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=22, font="comicsansns 11 bold")
        atten_date.grid (row=2, column=3, pady=8)

        #attendance

        attendanceLabel=Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox (left_inside_frame,textvariable=self.var_atten_attedence,width=20, font="comicsanshs 11 bold",state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")

        self.atten_status.grid(row=3, column=1, pady=8)

        self.atten_status.current (0)

        #buttons frame

        btn_frame=Frame (left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300,width=632,height=35)


        save_btn=Button(btn_frame,command=self.importCsv, text="Import csv",width=15, font=("times new roman", 13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=8,column=0)


        update_btn=Button(btn_frame,command=self.exportCsv, text="Export csv",width=15, font=("times new roman", 13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=8, column=1)


        delete_btn=Button (btn_frame,command=self, text="Update",width=15,font=("times new roman",13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=8, column=2)

        reset_btn=Button(btn_frame,command=self.reset_data, text="Reset",width=15, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=8, column=3)

        #Right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Detail",font=("times new roman",20))
        Right_frame.place(x=670,y=10,width=650,height=520)

        table_frame=Frame (Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5,width=640,height=455)

        #======================scrool bar===========================

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)



        self.AttendaceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)


        self.AttendaceReportTable.heading("id", text="Attendance ID")

        self.AttendaceReportTable.heading ("roll", text="Roll")

        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")

        self.AttendaceReportTable.heading ("time", text="Time")

        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("attendence", text="Attendance")

        self.AttendaceReportTable [ "show"]="headings"

        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("roll",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("attendence",width=100)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>", self.get_cursor)

        # ..........Fetch data............
    def fetchData(self, rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("", END, values=i)

        # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                             filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

        # export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV file", "*.csv"), ("All File", "*.*")),parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported "+os.path.basename(fln) + "Successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendaceReportTable.focus()
        content = self.AttendaceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attedence.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attedence.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()

