from tkinter import *
import calendar

text = calendar.calendar(2023)
root = Tk()

root.geometry("550x600")
root.title("CALENDAR")

label = Label(root, text="CALENDAR", bg="dark gray",
              font=("Poppins", 28, 'bold'))

label.grid(row=1, column=1)
root.config(background="white")

label2 = Label(root, text=text, font="consolas 10 bold", justify="left")
label2.grid(row=2, column=1, padx=20, pady=10)

root.mainloop()
