from tkinter import *
import scripts.webget as webget

root=Tk()
root.title("Dictionary")
root.geometry("365x584+400+100")
root.resizable(False,False)
def track():
    enter_number=entry.get()
    result = webget.get(enter_number,["def_text"])
    if result != None:meaning.config(text=result,wraplength = root.winfo_width())
    else:meaning.config(text="Cant Find Answer")


logo=PhotoImage(file="assets/logo image.png")
Label(root,image=logo).place(x=250,y=80)

Heading=Label(root,text="Dictionary",font=("arial",15,"bold"))
Heading.place(x=90,y=110)

Entry_back=PhotoImage(file="assets/search png.png")
Label(root,image=Entry_back).place(x=20,y="190")

entry=StringVar()
enter_number=Entry(root,textvariable=entry, width=17, bd=0, font=("arial",20),justify="center")
enter_number.place(x=50,y=220)

Search_image=PhotoImage(file="assets/search.png")   
search=Button(image=Search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=35,y=300)

Box=PhotoImage(file="assets/bottom png.png")
Label(root, image=Box).place(x=-2,y=355)

meaning = Label(root, text="Meaning",bg="#5770A9",fg="black",font=("arial",10,"bold"))
meaning.place(x=30,y=400)

root.mainloop()