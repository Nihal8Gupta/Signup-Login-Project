from tkinter import *
r=Tk()
def getval():
    print('Successful submitted')
r.geometry('500x300')
#Headind
Label(r,text='-: Register Form :-',font='arial 15 bold').grid(row=0,column=5)
#Fields
name=Label(r,text='Full_Name:')
email=Label(r,text='Email:')
mobile=Label(r,text='Mobile:')
password=Label(r,text='Password:')
cpassword=Label(r,text='Confirm_Password:')
#Packing Fields
name.grid(row=1,column=3)
email.grid(row=2,column=3)
mobile.grid(row=3,column=3)
password.grid(row=4,column=3)
cpassword.grid(row=5,column=3)
#Variable for storing
namevalue=StringVar
emailvalue=StringVar
mobilevalue=StringVar
passwordvalue=StringVar
cpasswordvalue=StringVar
checkvalue=IntVar
#Create input Fields
nameentry=Entry(r,textvariable=namevalue)
emailentry=Entry(r,textvariable=emailvalue)
mobileentry=Entry(r,textvariable=mobilevalue)
passwordentry=Entry(r,textvariable=passwordvalue)
cpasswordentry=Entry(r,textvariable=cpasswordvalue)
#Packing input fields
nameentry.grid(row=1,column=5)
emailentry.grid(row=2,column=5)
mobileentry.grid(row=3,column=5)
passwordentry.grid(row=4,column=5)
cpasswordentry.grid(row=5,column=5)
#checkbox
checkbtn=Checkbutton(text='remember me ?',variable=checkvalue)
checkbtn.grid(row=6,column=5)
#submit button
Button(text='Submit',command=getval).grid(row=7,column=5)
r.mainloop()
