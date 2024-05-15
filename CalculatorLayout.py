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



def history() :
    newWindow = Toplevel(root) 
    listbox = Listbox(newWindow, selectmode=SINGLE,width=40, height=20)
    

    for i in equation_list :
        listbox.insert(0, i)
 
    def get_element() :
        element = listbox.get(listbox.curselection())
        entry_string.set(element)
   


    insert_button = ttk.Button(newWindow,text="INSERT",command=lambda: get_element())
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

## STYLE 


## BUTTONS


button1 = ttk.Button(frame2, text="1", command= on_click("1"))
button2 = ttk.Button(frame2, text="2", command= on_click("2"))
button3 = ttk.Button(frame2, text="3", command= on_click("3"))
button4 = ttk.Button(frame2, text="4", command= on_click("4"))
button5 = ttk.Button(frame2, text="5", command= on_click("5"))
button6 = ttk.Button(frame2, text="6", command= on_click("6"))
button7 = ttk.Button(frame2, text="7", command= on_click("7"))
button8 = ttk.Button(frame2, text="8", command= on_click("8"))
button9 = ttk.Button(frame2, text="9", command= on_click("9"))
button0 = ttk.Button(frame2, text="0", command= on_click("0"))
button_plus = ttk.Button(frame2, text="+", command= on_click("+"))
button_minus = ttk.Button(frame2, text="-", command= on_click("-"))
button_div = ttk.Button(frame2, text="/", command= on_click("/"))
button_mult = ttk.Button(frame2, text="*", command= on_click("*"))
button_equal = ttk.Button(frame2, text="=", command=show)
button_dot = ttk.Button(frame2, text=".", command= on_click("."))
button_right_bracket = ttk.Button(frame2, text=")", command= on_click(")"))
button_left_bracket = ttk.Button(frame2, text="(", command= on_click("("))
button_clear = ttk.Button(frame2, text = "CE", command=clear)
button_del = ttk.Button(frame2, text= "Del", command=delete)
button_history = ttk.Button(frame2, text="History", command=history)

# FIRST ROW
button7.grid(column=0, row=0,sticky=(NSEW))
button8.grid(column=1, row=0,sticky=(NSEW))
button9.grid(column=2, row=0,sticky=(NSEW))
button_div.grid(column=3, row=0,sticky=(NSEW))

# SECOND ROW
button4.grid(column=0, row = 1,sticky=(NSEW))
button5.grid(column=1, row = 1,sticky=(NSEW))
button6.grid(column=2, row = 1,sticky=(NSEW))
button_mult.grid(column=3, row = 1,sticky=(NSEW))

# THIRD ROW
button1.grid(column=0, row=2,sticky=(NSEW))
button2.grid(column=1, row=2,sticky=(NSEW))
button3.grid(column=2, row=2,sticky=(NSEW))
button_minus.grid(column=3, row=2,sticky=(NSEW))

# FOURTH ROW
button0.grid(column=0, row =3,sticky=(NSEW))
button_dot.grid(column=2, row=3, sticky=(NSEW))
button_equal.grid(column=4, row=3,sticky=(NSEW))
button_plus.grid(column=3, row=3,sticky=(NSEW))

# BRACKETS | BACKSPACE | CLEAR | HISTORY
button_right_bracket.grid(column=4, row=1, sticky=(NSEW))
button_del.grid(column = 1, row = 3, sticky = (NSEW))
button_left_bracket.grid(column=4, row=2, sticky=(NSEW))
button_clear.grid(column=4, row= 0,sticky=(NSEW))
button_history.grid(columnspan=5, row=4, sticky=(NSEW))



entry_string = StringVar()
screen_entry = ttk.Entry(frame1,font=("claimcheck 30"),textvariable=entry_string, justify=RIGHT, validate="key")
screen_entry.place(width=400, height=100)






root.mainloop()