import tkinter as tk 

def convert_temperature():
    try:
        fahrenheit = float(Entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{celsius:.2f} degrees celsius")
    except ValueError:
        result_label.config(text= "Enter a number" )
#Create the main window.
root = tk.Tk()
root.title ("Temperature Converter")
#Create the Frame.
Frame = tk.Frame (root)
Frame.pack(padx=20, pady=20)
#Create an Entry for F.
Entry = tk.Entry(Frame, width = 10)
Entry.grid(row= 0, column = 0, padx = 5)
#Create a button to convert temperature.
convert_button = tk.Button(Frame, text = "Convert", command = convert_temperature)
convert_button.grid(row = 0, column = 1, padx = 5)
#Create a label to show the result.
result_label = tk.Label (Frame, text = "")
result_label.grid (row = 0, column = 2, padx = 5)

root.mainloop()