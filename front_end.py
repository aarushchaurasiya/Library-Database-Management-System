from tkinter import *
import back_end

def view_fun():
    list1.delete(0,END)
    for i in back_end.printing():
        list1.insert(END,i)


def search_fun():
    for i in back_end.searching(e_t.get(),e_a.get(),e_y.get(),e_i.get()):
        list1.insert(END,i)
        

def add_fun():
    back_end.inserting(e_t.get(),e_a.get(),e_y.get(),e_i.get())
    list1.delete(0,END) 
    list1.insert(END,(e_t.get(),e_a.get(),e_y.get(),e_i.get()))

def select_row(event):
    global t
    index = list1.curselection()[0]
    t = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,t[1])
    e2.delete(0,END)
    e2.insert(END,t[2])
    e3.delete(0,END)
    e3.insert(END,t[3])
    e4.delete(0,END)
    e4.insert(END,t[4])

def dlt_fun():
    back_end.deleting(t[0])

def update_fun():
    back_end.updaitng(t[0],e_t.get(),e_a.get(),e_y.get(),e_i.get())


win = Tk()
win.wm_title("Library")


l_1 = Label(win,text='Title')
l_1.grid(row=0,column=0)

l_2 = Label(win,text='Year')
l_2.grid(row=1,column=0)

l_3 = Label(win,text='Author')
l_3.grid(row=0,column=2)

l_4 = Label(win,text='Book Number')
l_4.grid(row=1,column=2)


e_t = StringVar()
e1 = Entry(win,textvariable=e_t)
e1.grid(row=0,column=1)

e_y = StringVar()
e2 = Entry(win,textvariable=e_y)
e2.grid(row=1,column=1)

e_a = StringVar()
e3 = Entry(win,textvariable=e_a)
e3.grid(row=0,column=3)

e_i = StringVar()
e4 = Entry(win,textvariable=e_i)
e4.grid(row=1,column=3)

list1 = Listbox(win,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

s_b1 = Scrollbar(win)
s_b1.grid(rowspan=6,row=2,column=2)

list1.configure(yscrollcommand=s_b1.set)
s_b1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',select_row)

b1 = Button(win,text='View All',width=12,command=view_fun)
b1.grid(row=2,column=3)

b2 = Button(win,text='Search Entry',width=12,command=search_fun)
b2.grid(row=3,column=3)

b3 = Button(win,text='Add Entry',width=12,command=add_fun)
b3.grid(row=4,column=3)

b4 = Button(win,text='Update',width=12,command=update_fun)
b4.grid(row=5,column=3)

b4 = Button(win,text='Delete',width=12,command=dlt_fun)
b4.grid(row=6,column=3)

b4 = Button(win,text='Close' ,width=12,command=win.destroy)
b4.grid(row=7,column=3)

win.mainloop()