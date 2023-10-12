from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import ast
r=Tk()
r.title('Login!')
r.geometry('850x531+100+50')
r.configure(bg='#fff')
r.resizable(False,False)

def signin():
    user=username.get()
    passw=password.get()

    file=open('datasheet.txt','r')
    d=file.read()
    k=ast.literal_eval(d)
    file.close()
    
    if user in k.keys() and k[user]==passw:
        messagebox.showinfo('Signin',f'Signin Successful')
        screen=Toplevel(r)
        screen.title('App')
        screen.geometry('850x531+100+50')
        screen.configure(bg='#FF4040')
        Label(screen,text=f'Welcome {user}!',bg='#FF4040',font=('Calibri(Body)',40,'bold')).pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror('Invalid',f"Invalid username {user} or password {passw}")
        
#####################################################
def signup_page():
    window=Toplevel(r)
    window.title('SignUp!')
    window.geometry('850x531+200+60')
    window.configure(bg='#fff')
    width= window.winfo_screenwidth()
    height= window.winfo_screenheight()
    window.resizable(False,False)

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
                window==file.write(str(r))
                messagebox.showinfo('Signup',f'Successful sign up {user}')
                window.destroy()
            except:
                file=open('datasheet.txt','w')
                pp=str({'user':'passw'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid',"Username or Password or confirm password did't match")
    def sign():
        window.destroy()
        
    img=ImageTk.PhotoImage(file='sign-up.png')
    Label(window,image=img,border=0,bg='white').place(x=0,y=50)

    frame=Frame(window,width=350,height=400,bg='white')
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
    window.mainloop()


#####################################################
img=PhotoImage(file='back11.png')
Label(r,image=img,bg='white').place(x=0,y=0)
frame=Frame(r,width=350,height=350,bg='#3D3D3D')
frame.place(x=480,y=70)
heading=Label(frame,text='Sign in',fg='#57a1f8',bg='#3D3D3D',font=('Microsoft YaHei UI Light',24,'bold'))
heading.place(x=100,y=30)
#username
def when_enter(u):
    username.delete(0,'end')
def when_leave(u):
    if username.get()=="":
        username.insert(0,'Username')
username=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#3D3D3D',font=('Microsoft YaHei UI Light',10,'bold'))
username.place(x=80,y=100)
username.insert(0,'Username')
username.bind('<FocusIn>',when_enter)
username.bind('<FocusOut>',when_leave)

Frame(frame,width=202,height=2,bg='#57a1f8').place(x=80,y=120)
#password
def when_enter(u):
    password.delete(0,'end')
def when_leave(u):
    passw=password.get()
    if passw=="":
        password.insert(0,'Password')
    
password=Entry(frame,width=25,fg='#57a1f8',border=0,bg='#3D3D3D',font=('Microsoft YaHei UI Light',10,'bold'))
password.place(x=80,y=140)
password.insert(0,'Password')
password.bind('<FocusIn>',when_enter)
password.bind('<FocusOut>',when_leave)

Frame(frame,width=202,height=2,bg='#57a1f8').place(x=80,y=160)
#button
Button(frame,width=30,pady=7,text='Sign in',cursor='hand2',bg='#57a1f8',fg='black',border=0,command=signin).place(x=72,y=210)
label=Label(frame,text="Don't have an account?",fg='black',bg='#3D3D3D',font=('Microsoft YaHei UI Light',7,'bold'))
label.place(x=75,y=180)
signup=Button(frame,width=7,text='Sign up',bg='#3D3D3D',cursor='hand2',fg='#57a1f8',font=('Microsoft YaHei UI Light',7,'bold'),border=0,command=signup_page)
signup.place(x=190,y=180)
r.mainloop()
