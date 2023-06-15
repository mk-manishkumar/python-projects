from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title('Rock Paper Scissor')
root.geometry("500x600")

root.config(bg="#2874f0")

# label for computer choice
computer_choice = Label(root, text="Computer Choice:",
                        font=("Helvetica", 18), bg="#2874f0", fg="white")
computer_choice.pack(pady=(30, 10))

rock = PhotoImage(file='images/rock.png')
paper = PhotoImage(file='images/paper.png')
scissors = PhotoImage(file='images/scissors.png')

# Add images to a list
image_list = [rock, paper, scissors]

# Pick random no. between 0 and 2
random_number = randint(0, 2)

# Throw up an image when the program starts
image_label = Label(root, image=image_list[random_number], bd=0, bg="#2874f0")
image_label.pack(pady=20)

# create spin function


def spin():
    random_number = randint(0, 2)
    image_label.config(image=image_list[random_number])

    # convert dropdown choice to a number
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    # Determine the outcome
    if user_choice_value == 0:
        if random_number == 0:
            result_label.config(text="It's a Tie!")
        elif random_number == 1:
            result_label.config(text="Paper beats Rock! You Lose :(")
        else:
            result_label.config(text="Rock beats Scissors! You Win! :)")
    elif user_choice_value == 1:
        if random_number == 0:
            result_label.config(text="Paper beats Rock! You Win! :)")
        elif random_number == 1:
            result_label.config(text="It's a Tie!")
        else:
            result_label.config(text="Scissors beat Paper! You Lose :(")
    else:
        if random_number == 0:
            result_label.config(text="Rock beats Scissors! You Lose :(")
        elif random_number == 1:
            result_label.config(text="Scissors beat Paper! You Win! :)")
        else:
            result_label.config(text="It's a Tie!")


# user choice label
your_choice = Label(root, text="Choose Yours:",
                    font=("Helvetica", 18), bg="#2874f0", fg="white")
your_choice.pack(pady=(30, 10))

# Make our choice
user_choice = ttk.Combobox(root, value=(
    "Rock", "Paper", "Scissors"), font=("Helvetica", 16))
user_choice.current(0)
user_choice.pack(pady=20)

# create spin button
spin_button = Button(root, text='Spin!', font=("Helvetica", 16), command=spin)
spin_button.pack(pady=10)

# Label for result
result_label = Label(root, text="", font=(
    "Helvetica", 18), bg="#2874f0", fg="white")
result_label.pack(pady=50)

root.mainloop()
