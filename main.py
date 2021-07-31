import tkinter
from tkinter import *

convert = Tk()
convert.geometry("800x500")

# name of application
convert.title("Temperature Converter")
convert.configure(bg="skyblue")

cel = StringVar()
fahren = StringVar()
result = StringVar()


def convert_c():
    cel = int(celsius.get())
    fahren = (cel*9/5)+32
    final = round(fahren, 2)
    return result.set(final)


def convert_f():
    fahren = int(fahrenheit.get())
    cel = (fahren-32)*5/9
    final = round(cel, 2)
    return result.set(final)


def clear_inputs():
    celsius.delete(0, END)
    fahrenheit.delete(0, END)
    answer.config(state="normal")
    answer.delete(0, END)
    answer.config(state="readonly")


def exit_program():
    return convert.destroy()


# placing labels
label_celsius_to_fahrenheit = Label(convert, text="Celsius To Fahrenheit", font="arial 20 italic", bg="skyblue")
label_fahrenheit_to_celsius = Label(convert, text="Fahrenheit To Celsius", font="arial 20 italic", bg="skyblue")

# Entry text
celsius = Entry(convert, textvariable=cel)
fahrenheit = Entry(convert, textvariable=fahren)
answer = Entry(convert, textvariable=result, bg="lawn green")

# Adding buttons
activate_celsius = tkinter.Button(convert, text="Activate-Celsius to Fahrenheit", command=convert_c)
calculate_conversion = tkinter.Button(convert, text="Calculate Conversion", )
activate_fahrenheit = tkinter.Button(convert, text="Activate-Fahrenheit to Celsius", command=convert_f)
clear = tkinter.Button(convert, text="Clear", command=clear_inputs)
exit = tkinter.Button(convert, text="Exit Program", command=exit_program)

# labels
label_celsius_to_fahrenheit.place(x=110, y=80)
label_fahrenheit_to_celsius.place(x=460, y=80)

# entry
celsius.place(x=110, y=170)
fahrenheit.place(x=460, y=170)
answer.place(x=310, y=335, width=220, height=48)

# buttons
activate_celsius.place(x=110, y=250)
calculate_conversion.place(x=110, y=335)
activate_fahrenheit.place(x=460, y=250)
clear.place(x=580, y=325)
exit.place(x=580, y=380)


# runs program all the time
convert.mainloop()
