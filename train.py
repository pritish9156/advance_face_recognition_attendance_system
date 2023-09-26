from tkinter import *
from tkinter import ttk #stylish tool kits
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        

        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        loginbtn=Button(title_lbl,command=self.return_sud_data,text="Back",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="red",bg="white")
        loginbtn.place(x=1310,y=4,width=200,height=35)    

        lbl = Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

        img_top=Image.open(r"college_images\facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] 

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

    def return_sud_data(self):
        self.root.destroy()    



if __name__ == "__main__":
    root = Tk()
    obj=Train(root)
    root.mainloop()         