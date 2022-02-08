import random
from tkinter import *
from PIL import Image, ImageTk 

root = Tk()
root.title("TechnoLord Programming")
root.geometry("500x400")

l = Label(root, text="Coin Toss", font=("Helvetica 18 bold"), fg="Red")
l.pack()

frame = Frame(root) 
Label(frame, text="Choose Heads/Tails: ", font=("Arial 16 bold")).pack(side=LEFT)
word = Entry(frame, font=("Arial 15 bold"))
word.pack()
frame.pack(pady=10)

#load heads
load = Image.open("tails.jpeg")
load = load.resize((200, 200))
heads = ImageTk.PhotoImage(load)
 
#load tails
load = Image.open("heads.jpeg")
load = load.resize((200, 200))
tails = ImageTk.PhotoImage(load)

load = Image.open("black.jpg")
load = load.resize((200, 200))
black = ImageTk.PhotoImage(load)

def tos():
    list1 = ["Heads", "Tails"]
    tossc = random.choice(list1)
    #num = random.randint(0,1)
    if tossc == "Heads":
        i.config(image=heads)
    else:
        i.config(image=tails)

b = Button(root, text="Flip Coin", bg='lightblue', fg='white', activebackground="lightgray", padx=10, pady=10, command=tos)
b.config(font=("Courier", 8))
b.pack()
 
i = Label(root, image=black)
i.pack()

e = Button(root, text="Exit", bg='gray', fg='white', activebackground="lightgray", padx=40, pady=20, command=exit)
e.config(font=("Courier", 14))
e.pack()

root.mainloop()




