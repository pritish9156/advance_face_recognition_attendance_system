from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime
import webbrowser
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.wm_iconbitmap("face.ico")
        

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"college_images\banner1.jpg")
        img=img.resize((1540,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1540,height=130)

        # backgorund image 
        bg1=Image.open(r"college_images\bg.png")
        bg1=bg1.resize((1550,790),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1550,height=790)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1540,height=45)

        loginbtn=Button(title_lb1,command=self.return_sud_data,text="Back",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="red",bg="white")
        loginbtn.place(x=1310,y=4,width=200,height=35)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lb1, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1

        # Detect Face  button 2
        det_img_btn=Image.open(r"college_images\Screenshot_2023-03-25-19-27-14-42_e2d5b3f32b79de1d45acd1fad96fbb0f.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.Linkdin,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=500,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.Linkdin,text="Pritish Pawar",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=500,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"college_images\IMG_20200410_163923.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.Instagram,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=810,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.Instagram,text="Shubham bhosle",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=810,y=380,width=180,height=45)

        title_lb2 = Label(bg_img,text="“No matter how good or bad your life is, wake up each morning and be thankful you still have one.“",font=("verdana",15,"bold"),bg="white",fg="navyblue")
        title_lb2.place(x=0,y=662,width=1540,height=45)

         # Help  Support  button 4

    def Linkdin(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/pritish-pawar-02720319b/"
        webbrowser.open(self.url,new=self.new)   

    def Instagram(self):
        self.new = 1
        self.url = "https://www.instagram.com/shubham.bhosle007/"
        webbrowser.open(self.url,new=self.new)


    def return_sud_data(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()