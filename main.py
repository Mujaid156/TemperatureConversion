import tkinter
from tkinter import *

convert = Tk()
convert.geometry("800x500")

# name of application
convert.title("Temperature Converter")

cel = StringVar()
fahren = StringVar()
result = StringVar()

def convert_c():
    cel = int(celcius.get())
    fahren = (cel*9/5)+32
    return result.set(fahren)

def convert_f():
    fahren = int(fahrenheit.get())
    cel = (fahren-32)*5/9
    return result.set(cel)

def clear_inputs():
    celcius.delete(0, END)
    fahrenheit.delete(0, END)
    answer.config(state="normal")
    answer.delete(0, END)
    answer.config(state="readonly")

def exit_program():
    return convert.destroy()


# placing labels
label_celcius_to_fahrenheit = Label(convert, text="Celcius To Fahrenheit")
label_fahrenheit_to_celcius = Label(convert, text="Fahrenheit To Celcius")

# Entry text
celcius = Entry(convert, textvariable=cel)
fahrenheit = Entry(convert, textvariable=fahren)
answer = Entry(convert, textvariable=result, bg="lawn green")

# Adding buttons
activate_celcius = tkinter.Button(convert, text="Activate-Celcius to Fahrenheit", command=convert_c)
calculate_conversion = tkinter.Button(convert, text="Calculate Conversion", )
activate_fahrenheit = tkinter.Button(convert, text="Activate-Fahrenheit to Celcius", command=convert_f)
clear = tkinter.Button(convert, text="Clear", command=clear_inputs)
exit = tkinter.Button(convert, text="Exit Program", command=exit_program)

# labels
label_celcius_to_fahrenheit.place(x=100, y=80)
label_fahrenheit_to_celcius.place(x=450, y=80)

# entry
celcius.place(x=130, y=170)
fahrenheit.place(x=480, y=170)
answer.place(x=310, y=335, width=220, height=48)

# buttons
activate_celcius.place(x=130, y=250)
calculate_conversion.place(x=130, y=335)
activate_fahrenheit.place(x=480, y=250)
clear.place(x=580, y=325)
exit.place(x=580, y=380)


# runs program all the time
convert.mainloop()
