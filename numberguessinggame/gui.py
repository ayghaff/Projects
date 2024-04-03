import tkinter as tk
import sys
import random


def check_guess(random_num, user_guess, new_window, rangemin, rangemax):
    try:
        user_guess = int(user_guess.strip())
    except ValueError:
        check_error_label = tk.Label(new_window, text = "Error. Please input a valid integer.")
        check_error_label.pack()
    print(random_num, user_guess)
    print(random_num == user_guess)
    try:
        if user_guess < rangemin:
            under_range_label = tk.Label(new_window, text = f"Please enter a number greater than {rangemin}")
            under_range_label.pack()
        elif user_guess > rangemax:
            over_range_lavel = tk.Label(new_window, text = f"Please enter a number lower than {rangemax}")
            over_range_lavel.pack()
        elif user_guess == random_num:
            print("won")
            winning_window = tk.Tk()
            winning_window.title("You won!")
            winning_label = tk.Label(winning_window, text = "Congratulations!")
            winning_label.pack()
            winning_label_the_sequel = tk.Label(winning_window, text = "You guessed the number correctly!")
            winning_label_the_sequel.pack()
            winning_label_the_trequel = tk.Label(winning_label, text = "To exit the game, close the program.")
            winning_label_the_trequel.pack()
        elif not user_guess == random_num:
            print("wrong")
            try:
                print(previous_guess)
            except UnboundLocalError:
                it_exists = False
            if it_exists:
                if abs(random_num - previous_guess) > abs(random_num - user_guess):
                    close_or_far = "closer"
                    wrong_label = tk.Label(new_window, text = f"Incorrect, you're getting {close_or_far}!")
                    previous_guess = user_guess
                    it_exists = True
                elif abs(random_num - previous_guess) < abs(random_num - user_guess):
                    close_or_far = "farther"
                    wrong_label = tk.Label(new_window, text = f"Incorrect, you're getting {close_or_far}!")
                    previous_guess = user_guess
                    it_exists = True
            else:
                previous_guess = user_guess
                wrong_label = tk.Label(new_window, text = "Incorrect, try again!")
            wrong_label.pack()
            previous_guess = user_guess
            it_exists = True
            print(it_exists)
    except TypeError:
        typeerror_error_label = tk.Label(new_window, text = "Error. Please enter a valid integer.")
        typeerror_error_label.pack()

def check_guess_init(random_num, user_guess, new_window, rangemin, rangemax):
    check_guess(random_num, user_guess, new_window, rangemin, rangemax)

def error_checking():
    try:
        errormin = int(minentry.get())
        errormax = int(maxentry.get())
        
        if errormin >= errormax:
            errorcheck = False
            error_label = tk.Label(window, text = "Error, make sure your minimum value is lower than the maximum value.")
        if errormin.is_integer() and errormax.is_integer():
            errorcheck = True
        else:
            errorcheck = False
            error_label = tk.Label(window, text = "Error, please input an integer.")
            error_label.pack()
    except ValueError:
        errorcheck = False
        error_label = tk.Label(window, text = "Error, please input an integer.")
        error_label.pack()
        
    if errorcheck == True:
        open_new_window(errormin, errormax)


def open_new_window(rangemin, rangemax):
    random_num = random.randint(rangemin, rangemax)

    new_window = tk.Tk()
    new_window.title("Guess the number")

    guesslabel = tk.Label(new_window, text = f"Guess a number between {rangemin} and {rangemax}.")
    guesslabel.pack()
    guessentry = tk.Entry(new_window)
    guessentry.pack()
    guessbutton = tk.Button(new_window, text = "Guess", command = lambda: check_guess_init(random_num, user_guess = guessentry.get(), new_window = new_window, rangemin = rangemin, rangemax = rangemax))
    guessbutton.pack()

    window.destroy()

window = tk.Tk()
window.title("Set the range")

minlabel = tk.Label(window, text = "How low would you like your guess to go?")
minlabel.pack()
minentry = tk.Entry(window)
minentry.pack()

maxlabel = tk.Label(window, text = "How high would you like your guess to go?")
maxlabel.pack()
maxentry = tk.Entry(window)
maxentry.pack()

minmaxbutton = tk.Button(window, text = "Enter", command = error_checking)
minmaxbutton.pack()

infolabel = tk.Label(window, text = "If you would like to use the Command Line Interface (CLI), please close this window and run the 'main.py' file again.")
infolabel.pack()

window.mainloop()
