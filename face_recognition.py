# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Pannel")
        self.root.wm_iconbitmap("face.ico")
        

        #title section
        title_lb1 = Label(self.root,text="Welcome to Face Recognition Pannel",font=("verdana",35,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        loginbtn=Button(title_lb1,command=self.return_sud_data,text="Back",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="red",bg="white")
        loginbtn.place(x=1310,y=4,width=200,height=35)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lb1, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"college_images\face_detector1.jpg")
        img=img.resize((650,700),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=55,width=650,height=700)

        # second header image
        bg1=Image.open(r"college_images\facial_recognition.jpg")
        bg1=bg1.resize((950,700),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=650,y=55,width=950,height=700)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        
        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="red",fg="white")
        std_b1_1.place(x=365,y=620,width=200,height=40)
    #=====================Attendance===================

    def mark_attendance(self,i,r,n):
        with open("attendance_report/attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",user="root",password="root123",database="face_recognizer")
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select Roll from student where Student_ID="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=cursor.fetchone()
                i="+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll-No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()

    def return_sud_data(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()