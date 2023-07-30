from tkinter import *

window = Tk()
window.geometry("700x500")
window.title("Billing System")

# function


def calculateBill():
    aloo_paratha = int(e1.get() or 0)
    samosa = int(e2.get() or 0)
    fried_rice = int(e3.get() or 0)
    tea = int(e4.get() or 0)

    total = (aloo_paratha * 30) + (samosa * 15) + \
        (fried_rice * 45) + (tea * 10)

    displayTotal = Label(
        window, text=f"Total Bill Amount: Rs {total}", font="Poppins 30 bold")

    displayTotal.place(x=350, y=380, anchor="center")


# ----------------------------- Main Layout------------------------------


labelBrand = Label(window, text="Mohan Ka Melaram Dhaba",
                   font="Poppins 30 bold")
labelBrand.place(x=350, y=20, anchor="center")

labelMenu = Label(window, text="MENU", font="Poppins 28 bold")
labelMenu.place(x=550, y=70)

label1 = Label(window, text="Aloo Paratha     Rs30", font="Poppins 18")
label1.place(x=450, y=120)

label2 = Label(window, text="Samosa            Rs15", font="Poppins 18")
label2.place(x=450, y=150)

label3 = Label(window, text="Fried Rice         Rs45", font="Poppins 18")
label3.place(x=450, y=180)

label4 = Label(window, text="Tea                   Rs10", font="Poppins 18")
label4.place(x=450, y=210)

# ------------------- Billing Section -------------------

labelSelectItems = Label(
    window, text="Select the Items", font="Poppins 20 bold")
labelSelectItems.place(x=70, y=70)

label5 = Label(window, text="Aloo Paratha", font="Poppins 18")
label5.place(x=20, y=120)

e1 = Entry(window)
e1.place(x=20, y=160)

label6 = Label(window, text="Samosa", font="Poppins 18")
label6.place(x=250, y=120)

e2 = Entry(window)
e2.place(x=250, y=160)

label7 = Label(window, text="Fried Rice", font="Poppins 18")
label7.place(x=20, y=200)

e3 = Entry(window)
e3.place(x=20, y=240)

label8 = Label(window, text="Tea", font="Poppins 18")
label8.place(x=250, y=200)

e4 = Entry(window)
e4.place(x=250, y=240)

# ------------------------------ Button Section---------------------------------

billButton = Button(window, text="BILL", width=20, command=calculateBill)
billButton.place(x=100, y=300)


window.mainloop()
