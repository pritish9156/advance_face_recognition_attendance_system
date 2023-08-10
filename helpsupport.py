from tkinter import*
from PIL import Image,ImageTk
import webbrowser
from time import strftime
from datetime import datetime


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.wm_iconbitmap("face.ico")
        

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"college_images\banner.jpg")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=130)

        # backgorund image 
        bg1=Image.open(r"college_images\bg.jpg")
        bg1=bg1.resize((1530,710),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
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

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"college_images\web.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.Linkdin,image=self.std_img1,cursor="hand2")
        std_b1.place(x=310,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.Linkdin,text="Linkdin",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=310,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"college_images\fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=540,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=540,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"college_images\yt.png")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=770,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=770,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"college_images\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=1000,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1000,y=380,width=180,height=45)


        # create function for button 
    
    
    def Linkdin(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/pritish-pawar-02720319b/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/@pritishpawar4168/featured"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)



    def return_sud_data(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()