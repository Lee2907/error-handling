from tkinter import *
from tkinter import messagebox

money = Tk()
money.geometry("500x500")
money.title("Qualify For The Trip")
money.config(bg="salmon1")

def check():
    try:
        return 3000
    except e_1.get() > 3000:
        print("Please deposit more funds for this excursion.")
    except e_1.get() < 3000:
        print("You qualify for the Malaysia trip. Congratulations!")

l_1 = Label(money, text="Please enter money in your account: ")
l_1.place(x=5, y=5)

e_1 = Entry(money)
e_1.place(x=10, y=25)

qualify_btn = Button(money, text="Check qualification",bg="blanched almond",command=check)
qualify_btn.place(x=100, y=50)


money.mainloop()
