from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import ast
w=Tk()
w.title('SignUp!')
w.geometry('850x531+200+60')
w.configure(bg='#fff')
width= w.winfo_screenwidth()
height= w.winfo_screenheight()
w.resizable(False,False)

def signup():
    user=username.get()
    passw=password.get()
    cpassw=cpassword.get()
    if passw==cpassw:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={user:passw}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w==file.write(str(r))

            messagebox.showinfo('Signup',f'Successful sign up {user}')

        except:
            file=open('datasheet.txt','w')
            pp=str({'user':'passw'})
            file.write(pp)
            file.close()
    else:
        messbox.showerror('Invalid',"Password and confirm password did't match")
def sign():
    w.destroy()
    
img=ImageTk.PhotoImage(file='sign-up.png')
Label(w,image=img,border=0,bg='white').place(x=0,y=50)

frame=Frame(w,width=350,height=400,bg='white')
frame.place(x=450,y=60)
heading=Label(frame,text='Sign up',fg='black',bg='white',font=('Microsoft YaHei UI Light',22,'bold'))
heading.place(x=120,y=30)
#username
def when_enter(u):
    username.delete(0,'end')
def when_leave(u):
    if username.get()=='':
        username.insert(0,'Username')
    
username=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',10,'bold'))
username.place(x=80,y=100)
username.insert(0,'Username')
username.bind('<FocusIn>',when_enter)
username.bind('<FocusOut>',when_leave)
Frame(frame,width=202,height=2,bg='black').place(x=80,y=120)
#password
def when_enter(u):
    password.delete(0,'end')
def when_leave(u):
    if password.get()=='':
        password.insert(0,'Password')
password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',10,'bold'))
password.place(x=80,y=160)
password.insert(0,'Password')
password.bind('<FocusIn>',when_enter)
password.bind('<FocusOut>',when_leave)
Frame(frame,width=202,height=2,bg='black').place(x=80,y=180)
#cpassword
def when_enter(u):
    cpassword.delete(0,'end')
def when_leave(u):
    if cpassword.get()=='':
        cpassword.insert(0,'Confirm Password')
cpassword=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',10,'bold'))
cpassword.place(x=80,y=220)
cpassword.insert(0,'Confirm Password')
cpassword.bind('<FocusIn>',when_enter)
cpassword.bind('<FocusOut>',when_leave)
Frame(frame,width=202,height=2,bg='black').place(x=80,y=240)
#button
Button(frame,width=30,pady=7,text='Sign up',cursor='hand2',bg='#57a1f8',fg='black',border=0,command=signup).place(x=72,y=260)
label=Label(frame,text="I have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',8,'bold'))
label.place(x=80,y=320)
signup=Button(frame,width=7,text='Sign in',bg='white',cursor='hand2',fg='#57a1f8',font=('Microsoft YaHei UI Light',8,'bold'),border=0,command=sign)
signup.place(x=200,y=320)
w.mainloop()
