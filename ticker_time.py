from tkinter import*
import time
import datetime
#stiveckamash@gmail.com
def tickertime():

	#create a variable to store the time and format it
	clock_time=time.strftime("%A  %H:%M:%S")#A means full day name
	clock.config(text=clock_time)
	#set the number of ticks the clock to recall function 
	clock.after(1000,tickertime)
window=Tk()
window.title("steve clock_time")
#create an object for the gui
clock=Label(window,bg="blue",font=("times",100,"bold"))
clock.grid(row=0,column=2)
tickertime()
#call the function
window.mainloop()