from tkinter import*
from datetime import date
root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')
Label1 = Label(text = "hi there",fg = "white",bg = "blue", height = 1, width = 300)
name_label1 = Label(text = "full name", bg = "green")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = "welcome to the application. \n todays date is:"
    greet = "hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height = 3)
btn = Button(text = "begin",command = display, height = 1, bg = "grey", fg = "white")
Label1.pack()
name_label1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()