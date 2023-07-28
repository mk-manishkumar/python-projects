from tkinter import *
import speedtest


def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 2)) + " Mbps"
    up = str(round(sp.upload()/(10**6), 2)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="#8D3DAF")

lab_title = Label(sp, text="Internet Speed Test", font=(
    "Poppins", 30, "bold"), bg="#8D3DAF", fg="white")
lab_title.place(x=60, y=40, height=50, width=380)

lab_down_text = Label(sp, text="Download Speed", font=(
    "Poppins", 30, "bold"), bg="black", fg="white")
lab_down_text.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Poppins", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab_up_text = Label(sp, text="Upload Speed", font=(
    "Poppins", 30, "bold"), bg="black", fg="white")
lab_up_text.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Poppins", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=("Poppins", 30, "bold"),
                relief=RAISED, bg="#2827CC", fg="white", command=speedCheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
