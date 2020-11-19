from tkinter import*
from tkinter.ttk import*
from sqlite3 import*
from tkinter import messagebox
import home


class LoginWindow(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)

        self.title("Login")
        self.geometry("300x300")

        style=Style()
        style.configure("hf.TFrame",background="blue")


        hf=Frame(self,height=60,style="hf.TFrame")
        hf.pack(fill=X)

        style.configure("lb.TLabel",background="blue",foreground="white",font=(NONE,20))
        lb=Label(hf,text="My Contact Book",style="lb.TLabel")
        lb.pack(pady=10)

        style.configure("cf.TFrame",background="white")
        cf=Frame(self,style="cf.TFrame")
        cf.pack(fill=BOTH,expand=TRUE)
        
        style.configure("lf.TFrame",background="white")
        lf=Frame(cf,style="lf.TFrame")
        lf.place(relx=.5,rely=.5,anchor=CENTER)

        style.configure("lf.TLabel",background="White",font=(NONE,10))

        userlabel=Label(lf,text="Username:",style="lf.TLabel")
        userlabel.grid(row=0,column=0)
        
        self.e1=Entry(lf,font=(NONE,10),width=15)
        self.e1.grid(row=0,column=1,pady=5)
        
        passlabel=Label(lf,text="Password:",style="lf.TLabel")
        passlabel.grid(row=1,column=0)

        self.e2=Entry(lf,font=(NONE,10),show="*",width=15)
        self.e2.grid(row=1,column=1,pady=5)

        style.configure("lf.TButton",font=(NONE ,10))
        b=Button(lf,text="Login",style="lf.TButton",width=15,command=self.login_button_click)
        b.grid(row=2,column=1,pady=5)
        b.bind('<Return>', self.login_button_click)
        

    def login_button_click(self,event=None):
        con=connect('mycontact.db')
        cur=con.cursor()
        cur.execute("select *from Login where Username=? and Password=?",( self.e1.get(),self.e2.get()))
        row=cur.fetchone()
        if row is not None:
           self.destroy()
           home.HomeWindow()
        else:
                messagebox.showerror("Error message","Inavlid username/password")

if __name__=='__main__':
    lw=LoginWindow()
    lw.mainloop()

