import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x300') # set specified window size

# create the strings for the timer
hours = StringVar()
minutes = StringVar()
seconds = StringVar()

# create the input fields and place them in the window
hours_entry = Entry(root, relief=FLAT, width=3, \
    font=("Calibri", 18, ""), textvariable=hours)
minutes_entry = Entry(root, relief=FLAT, width=3, \
    font=("Calibri", 18, ""), textvariable=minutes)
seconds_entry = Entry(root, relief=FLAT, width=3, \
    font=("Calibri", 18, ""), textvariable=seconds)

hours_entry.place(x=80, y=20)
minutes_entry.place(x=130, y=20)
seconds_entry.place(x=180, y=20)

# the countdown function
def letsgo():
    try:
        total_time = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())
    except:
        print("Please input a correct time value")
    
    while total_time > -1:

        # make sure time is in the correct format
        m, s = divmod(total_time, 60)
        h = 0

        if m > 60 : h, m = divmod(m, 60)
        
        # update the string variable with the new calculated time
        hours.set("{0:2d}".format(h))
        minutes.set("{0:2d}".format(m))
        seconds.set("{0:2d}".format(s))


        # update the tkinter window
        root.update() 

        # wait 1 second before decrementing the timer 
        time.sleep(1)

        # check if the timer finished
        if (total_time == 0):
            # print a message if it did
            messagebox.showinfo("Pomodoro", "Pomodoro has finished!")
            exit(1)

        total_time -=1 # decrement timer


start_button = Button(root, text='Start Timer', command=letsgo)
start_button.place(x=70, y=120)

root.mainloop()