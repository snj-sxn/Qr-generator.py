from tkinter import* 
import qrcode
from PIL import Image,ImageTk 
from resizeimage import resizeimage                                                                                                                                                                                                                                                                                                                                              
class Qr_generator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("700x500+400+100")
        self.root.title("QR Generator||Sanjana Saxena")
        self.root.resizable(False,False)

        title = Label(self.root,text="QR CODE GENERATOR",font=("times new roman",30),bg='#ffb3b3',fg='Black',anchor=W).place(x=0,y=0,relwidth=1)
        #...Student Details window ...
        #...Variables ...to fetch details
        self.var_stu_code=StringVar()
        self.var_stu_name=StringVar()
        self.var_stu_Branch=StringVar()
        self.var_stu_college=StringVar()
        self.var_stu_City=StringVar()

        stu_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        stu_Frame.place(x=30,y=80,width=350,height =370)
        stu_title = Label(stu_Frame,text="STUDENT DETAILS",font=("goudy old style",15),bg='#ff0080',fg='Black').place(x=0,y=0,relwidth=1)
        lbl_stu_code=Label(stu_Frame,text="Student ID",font=("times new roman",12,'bold'),bg='white').place(x=20,y=50)
        lbl_name=Label(stu_Frame,text="Name",font=("times new roman",12,'bold'),bg='white').place(x=20,y=90)
        lbl_Branch=Label(stu_Frame,text="Branch",font=("times new roman",12,'bold'),bg='white').place(x=20,y=130)
        lbl_college=Label(stu_Frame,text="College",font=("times new roman",12,'bold'),bg='white').place(x=20,y=170)
        lbl_City=Label(stu_Frame,text="City",font=("times new roman",12,'bold'),bg='white').place(x=20,y=210)

        txt_stu_code=Entry(stu_Frame,font=("times new roman",12),textvariable=self.var_stu_code,bg='lightyellow').place(x=150,y=50)
        txt_name=Entry(stu_Frame,font=("times new roman",12),textvariable=self.var_stu_name,bg='lightyellow').place(x=150,y=90)
        txt_Branch=Entry(stu_Frame,font=("times new roman",12),textvariable=self.var_stu_Branch,bg='lightyellow').place(x=150,y=130)
        txt_college=Entry(stu_Frame,font=("times new roman",12),textvariable=self.var_stu_college,bg='lightyellow').place(x=150,y=170)
        txt_City=Entry(stu_Frame,font=("times new roman",12),textvariable=self.var_stu_City,bg='lightyellow').place(x=150,y=210)

        btn_generate = Button(stu_Frame,text='Generate QR',command=self.generate,font=("times new roman",12,'bold'),bg='#ffb3b3',fg='black',anchor=W).place(x=40,y=260,width=120,height=20)
        btn_clear = Button(stu_Frame,text='Clear',command=self.clear,font=("times new roman",12,'bold'),bg='#ff0080',fg='black').place(x=180,y=260,width=120,height=20)

        self.msg = ''
        self.lbl_msg=Label(stu_Frame,text=self.msg,font=("times new roman",15,'bold'),bg='white',fg='Dark Green')
        self.lbl_msg.place(x=0,y=303,relwidth=1)

        #...Window of QR code
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=450,y=80,width=220,height =370)
        qr_title = Label(qr_Frame,text="Student QR Code",font=("goudy old style",15),bg='#ff0080',fg='Black').place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text='No Qr\n Available',font=('times new roman',15),bg='#ffb3b3',fg='black',bd=1,relief=RIDGE)
        self.qr_code.place(x=27,y=100,width=160,height=180)
    def clear(self):
        self.var_stu_code.set('')
        self.var_stu_name.set('')
        self.var_stu_Branch.set('')
        self.var_stu_college.set('')
        self.var_stu_City.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')



    def generate(self):
        if self.var_stu_code.get()==''or self.var_stu_name.get()==''or self.var_stu_Branch.get()==''or self.var_stu_college.get()==''or self.var_stu_City.get()=='':
           self.msg='All Fields are Required!!'
           self.lbl_msg.config(text=self.msg,fg='Red')
        else:
            qr_data=(f"Student ID:{self.var_stu_code.get()}\n"
                     f"Student Name:{self.var_stu_name.get()}\n"
                     f"Branch:{self.var_stu_Branch.get()}\n"
                     f"college:{self.var_stu_college.get()}\n"
                     f"City:{self.var_stu_City.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[160,160])
            qr_code.save("student_qr/Stu_"+str(self.var_stu_code.get())+'.png')
            #...QR code image update...
            self.im=ImageTk.PhotoImage(file="student_qr/Stu_"+str(self.var_stu_code.get())+'.png')
            self.qr_code.config(image=self.im)

            #.....updating notification
            self.msg='QR Generated succesfully !!'
            self.lbl_msg.config(text=self.msg,fg='Dark Green')




root = Tk()
object = Qr_generator(root)
root.mainloop()