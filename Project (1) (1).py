#[project]

"""
a) Build a Temperature Conversion Application
Build a temperature conversion application that converts temperature from
degree Fahrenheit to degree Celcius and vice versa, using the python tkinter module.
""" 
import tkinter as tk

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert():
    temperature = float(entry.get())
    if var.get() == 0:  # Fahrenheit to Celsius
        result_label.config(text=f"{temperature}°F = {fahrenheit_to_celsius(temperature):.2f}°C")
    else:  # Celsius to Fahrenheit
        result_label.config(text=f"{temperature}°C = {celsius_to_fahrenheit(temperature):.2f}°F")

root = tk.Tk()
root.title("Temperature Converter")

var = tk.IntVar()

label = tk.Label(root, text="Enter temperature:")
label.pack()

entry = tk.Entry(root)
entry.pack()

radio_frame = tk.Frame(root)
radio_frame.pack()

fahrenheit_radio = tk.Radiobutton(radio_frame, text="Fahrenheit to Celsius", variable=var, value=0)
fahrenheit_radio.pack(side="left")

celsius_radio = tk.Radiobutton(radio_frame, text="Celsius to Fahrenheit", variable=var, value=1)
celsius_radio.pack(side="right")

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()