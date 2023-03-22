from tkinter import*
import random

root=Tk()

root.title("Who is your lucky friend in Class?")
root.geometry("700x700")
root.configure(background="#1C8FD3")

label = Label(root)
list1 = ["Harry", "Kevin", "Amelia", "Sarah", "Fionn", "Brooke", "Dáire", "Lauren", "Conall", "Robyn", "Samuel", "Evie", "Felix", "Áine", "Cillian", "Keelin", "Max", "Leah", "Zach", "Lena", "Adam", "Tara"]
print(list1)

def random_number():
    random_no = random.randint(0, 21)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("Your Lucky Friend is : " + random_lucky_friend)
    label["text"]="Your Lucky Friend is : " + random_lucky_friend

label.place(relx=0.5,rely=0.6, anchor=CENTER)
btn1 = Button(root)    
btn1 = Button(root, text="Click me to find out who your lucky friend is!", command = random_number, bg="#D31CCA", fg="white")
btn1.place(relx = 0.5,rely=0.5, anchor = CENTER)
root.mainloop()