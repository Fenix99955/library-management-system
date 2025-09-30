from tkinter import *
root=Tk()
root.title("Library Management System")
root.geometry("1200x880")
root.maxsize(1200,880)
root.background="#B2D7FD"


#mainframe

df=Frame(root,width=900,height=900,bg="white",background="#B2D7FD")
df.place(x=300,y=0)


def issue_books(frame):
        for widget in frame.winfo_children():
            widget.destroy()
        Label0=Label(df,text=("Issue Books"),font=("arial",30,"bold"),background="#B2D7FD")
        Label0.place(x=50,y=10)
        data1=Frame(df,width=800,height=700,bg="white")
        data1.place(x=50,y=100)

        label12=Label(data1,text="Issued Books",font=("arial",20,"bold"),bg="white")
        label12.place(x=50,y=0)



def members(frame):
        for widget in frame.winfo_children():
            widget.destroy()
        Label0=Label(df,text=("Members"),font=("arial",30,"bold"),background="#B2D7FD")
        Label0.place(x=50,y=10)
        data2=Frame(df,width=800,height=700,bg="white")
        data2.place(x=50,y=100)

        button1members=Button(df,text="+ Add Member",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=15,height=2)
        button1members.place(x=700,y=10)

        searchmembers=Entry(df,font=("arial",31),width=10)
        searchmembers.place(x=300,y=10)

        button2members=Button(df,text="Search",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=15,height=2)
        button2members.place(x=535,y=10)




def books(frame):
        for widget in frame.winfo_children():
            widget.destroy()
        Label0=Label(df,text=("Books"),font=("arial",30,"bold"),background="#B2D7FD")
        Label0.place(x=50,y=10)

        button1=Button(df,text="+ Add Book",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=15,height=2)
        button1.place(x=700,y=10)

        data=Frame(df,width=800,height=700,bg="white")
        data.place(x=50,y=100)

        searchbook=Entry(df,font=("arial",31),width=10)
        searchbook.place(x=300,y=10)

        buttonbook2=Button(df,text="Search",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=15,height=2)
        buttonbook2.place(x=535,y=10)




def dashboard(frame):
    for widget in frame.winfo_children():
        widget.destroy()    

    Label0=Label(df,text=("Dashboard"),font=("arial",30,"bold"),background="#B2D7FD")
    Label0.place(x=50,y=10)

    Label1=Label(df,text=("BOOKS"),font=("arial",20,"bold"),width=10,height=7,bg="white")
    Label1.place(x=50,y=100)

    Label1=Label(df,text=("BOOKS"),font=("arial",20,"bold"),width=10,height=7,bg="white")
    Label1.place(x=250,y=100)

    Label1=Label(df,text=("BOOKS"),font=("arial",20,"bold"),width=10,height=7,bg="white")
    Label1.place(x=450,y=100)

    Label1=Label(df,text=("BOOKS"),font=("arial",20,"bold"),width=10,height=7,bg="white")
    Label1.place(x=650,y=100)

    #mainframe
    mainframe=Frame(df,width=778,height=400,bg="white")
    mainframe.place(x=50,y=400)

    abel5=Label(mainframe,text="Recent Activities",font=("arial",20,"bold"),bg="white")
    abel5.place(x=50,y=0)

    


#aside bar
right=Frame(root,background="#1E3A8A",width=300,height=900)
right.place(x=0,y=0)

button1=Button(right,text="Dashboard",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=30,height=3,command=lambda: dashboard(df))
button1.place(x=0,y=0)

button2=Button(right,text="Books",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=30,height=3,command=lambda: books(df))
button2.place(x=0,y=70)

button3=Button(right,text="Members",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=30,height=3,command=lambda: members(df))
button3.place(x=0,y=130)

button4=Button(right,text="Issue Books",font=("arial",12,"bold"),background="#1E3A8A",fg="white",width=30,height=3,command=lambda: issue_books(df))
button4.place(x=0,y=190)





dashboard(df)





root.mainloop()