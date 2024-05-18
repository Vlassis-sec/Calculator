## IMPORT LIBRARIES
from tkinter import *
from tkinter import ttk, font
import re
root = Tk()
root.geometry("400x500")
root.rowconfigure(1, weight=1)
root.resizable(0,0)


## FUNCTIONS 

# This function inserts in entry the text of eache button.
def on_click(text) :
    
    return lambda : screen_entry.insert(END, text)

# This function is making pop-up windows 
def show_error_window(title,message) :
    newWindow = Toplevel(root)
    newWindow.title(title)
    label = ttk.Label(newWindow, text=message, justify="center", font="overstrike 11 bold").pack()
    destroy_button = ttk.Button(newWindow, text="OK", command=newWindow.destroy).pack()

# This function calculates the result 
equation_list = [] # | This list is made so i can use it in history function.
def show() :
    equation = entry_string.get()
    
    pattern = re.compile(r'\(*[0-9]*\.?[0-9]*\)*[\+\-\*\/]\(*[0-9]+\.?[0-9]*\)*') # | This pattern, makes sure the input is valid.
    pattern_division_with_zero = re.compile(r"\/[0]$") # | This pattern makes sure, you can't devide a number with 0.

    if pattern.match(equation) : # | If the input matches the pattern

        if pattern_division_with_zero.search(equation) : # | We have to check if there is a division with 0 | 
            show_error_window("Divsion with zero", "You can't divide a number\nwith zero.\nCheck your input!") # | If that's the case, this is the pop up window to warn you.
           

        else : # | If the input is valid, i calculate the result.
            var_x = str(equation)
            equation_list.append(var_x) ## | I append the equation to the list, so i can use it in history function.
            result = eval(equation) 
            entry_string.set(result)
            
    else : # | This else is here, to prevent the user from inserting a letter, a double opperator (e.g. ++) or didn't complete the equation (e.g 39+) | Anything but the pattern
        # i created, is not allowed.
        show_error_window("Invalid Input", "You either inserted a letter,\nor you didnt complete the\ncalculation.\nCheck your input!") # | This is again a pop up window to warn you.


# This function stores the calculations that has been made into a listbox.
def history() :
    newWindow = Toplevel(root)
    newWindow.title("History") 
    listbox = Listbox(newWindow, selectmode=SINGLE,width=40, height=20) # This is the listbox with the calculations.
    

    for i in equation_list :
        listbox.insert(0, i) # This for, inserts every calculation into the listbox.
 
    def get_element() : # This function, takes the calculation from the listbox, and set's it into the entry of the calculator.
        element = listbox.get(listbox.curselection())
        entry_string.set(element)
   


    insert_button = ttk.Button(newWindow,text="INSERT",command=get_element)
    listbox.pack()
    insert_button.pack()
    

# This function clears the screen
def clear() :
    
    screen_entry.delete(0,END)
    

# This function deletes the last number 
def delete() :
    the_calculation = entry_string.get()
    list_of_calculation = list(the_calculation)
    the_last_character = len(list_of_calculation) - 1
    screen_entry.delete(the_last_character)





## SCREEN | BUTTONS FRAME

frame1 = ttk.Frame(root, width=400, height=100, relief="solid")
frame2 = ttk.Frame(root, width=400, height=400, relief="solid")


## SCREEN | BUTOONS GRID
frame1.grid(column=0, row=0,sticky=(N,S,W,E))
frame2.grid(column=0, row=1,sticky=(N,S,W,E))

## DEFINE A GRID 

## FRAME 1 GRID 

frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)
frame1.rowconfigure(0,weight=1)
frame1.rowconfigure(1,weight=1)


## FRAME 2 GRID
frame2.columnconfigure(0,weight=1)
frame2.columnconfigure(1,weight=1)
frame2.columnconfigure(2,weight=1)
frame2.columnconfigure(3,weight=1)
frame2.columnconfigure(4,weight=1)


frame2.rowconfigure(0,weight=1)
frame2.rowconfigure(1,weight=1)
frame2.rowconfigure(2,weight=1)
frame2.rowconfigure(3,weight=1)

 


## BUTTONS

def setup_buttons(buttons_list, row) : # This function takes a list (with that buttons that has to be made), and the row (the row that the buttons will be inserted).
    
    for i, button_text in enumerate(buttons_list) : # This for iterates into the list, so the buttons can be made.

        # If and elif's check the buttons
        # This is happening, because some buttons are made for different purposes
        # Example : The "History" button, just pop up a list with the calculations.
        if button_text == "CE" :                                                                
            button = ttk.Button(frame2, text=button_text, command=clear)
            button.grid(column=i, row = row, sticky=(NSEW))
        elif button_text == "=" :
            button = ttk.Button(frame2, text=button_text, command=show)
            button.grid(column=i, row = row, sticky=(NSEW))
        elif button_text == "History" :
            button = ttk.Button(frame2, text=button_text, command=history)
            button.grid(columnspan=5, row = row, sticky=(NSEW))
        elif button_text == "Del" :
            button = ttk.Button(frame2, text=button_text, command=delete)
            button.grid(column=i, row = row, sticky=(NSEW))
        # This else, makes a button for every number
        else :
            button = ttk.Button(frame2, text=button_text, command=on_click(button_text))
            button.grid(column=i, row = row, sticky=(NSEW))


# LISTS AND FUNCTION CALLS 

# First row :
first_row = ["7", "8", "9", "/", "CE"]
setup_buttons(first_row,0)

# Second row :
second_row = ["4", "5", "6", "*", ")"]
setup_buttons(second_row,1)

# Third row :
third_row = ["1", "2", "3", "-", "("]
setup_buttons(third_row,2)

# Forth row :
forth_row = ["0", "Del", ".", "+", "="]
setup_buttons(forth_row, 3)

# Fifth row :
fifth_row = ["History"]
setup_buttons(fifth_row,4)


# The entry is the screen of the calculator.
entry_string = StringVar()
screen_entry = ttk.Entry(frame1,font=("claimcheck 30"),textvariable=entry_string, justify=RIGHT, validate="key")
screen_entry.place(width=400, height=100)


# RUN
root.mainloop()