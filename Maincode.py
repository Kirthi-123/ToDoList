from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('350x530')
window.title('To-Do List')
window.resizable(0,0)

def addTask():
    task = my_entry.get()
    if task != "":
        box.insert(END, task)
        task_list.append(task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("WARNING", "Please enter some task.")

def editTask():
    selected=box.curselection()
    edit_Task=box.get(selected) 
    my_entry.delete(0, END)
    my_entry.insert(0, edit_Task)
    box.delete(ANCHOR)

def deleteTask():
    if box.curselection() != "":
        box.delete(ANCHOR)
    else:
        messagebox.showerror("ERROR",'No Task Selected,Cannot Delete.')

def close():   
    window.destroy()  
  
label=Label(window,text="TO DO LIST",fg='black',font=('ariel',20))
label.grid(row=1,column=1)

box = Listbox(window,width=25,height=8,font=('Times', 18),bd=0,fg='#464646',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none",)
box.grid(row=4,column=1,padx=15,pady=10)

task_list = list()

my_entry = Entry(window,font=('times', 24))
my_entry.grid(row=2,column=1,padx=15,pady=10)

addTask_btn = Button(window,text=' Add Task ',font=('times 14'),bg='#c5f776',command=addTask)
addTask_btn.grid(row=5,column=1,pady=5)

editTask_btn = Button(window,text='  Edit Task ',font=('times 14'),bg='light blue',command=editTask)
editTask_btn.grid(row=6,column=1,pady=5)

delTask_btn = Button(window,text='Delete Task',font=('times 14'),bg='#ff8b61',command=deleteTask)
delTask_btn.grid(row=7,column=1,pady=5)

exit_btn = Button(window,text='      Exit      ',font=('times 14'),bg='grey',command=close)
exit_btn.grid(row=8,column=1,pady=5)

window.mainloop()
