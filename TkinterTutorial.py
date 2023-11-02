import tkinter as tk

window = tk.Tk()
#greeting = tk.Label(
#    text="Hello, Tkinter",
#    foreground="white", # Set the text color to white
#    bg="#34A2FE", #set the background color to light blue while using the abbreviated for backgroud bg. 
#    width=10,
#    height=10
#)
#greeting.pack()

#button = tk.Button(
#    text = "Click Me!",
#    width=25,
#    height=5,
#    bg="blue",
#    fg="yellow"
#)
#button.pack()

label = tk.Label(text='Name')
entry = tk.Entry()
label.pack()
entry.pack()

name = entry.insert(0, "Python")

window.mainloop()


