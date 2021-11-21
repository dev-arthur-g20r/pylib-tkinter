import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x500") # Set window's dimensions to 500x500

# GROUP: Set up and display label of name
nameLabel = tk.Label(
	text = "Name:"
)
nameLabel.pack()

# GROUP: Set up and display entry of name
nameEntry = tk.Entry()
nameEntry.pack()

# GROUP: Display alert of name from the entry
def displayName():
	name = nameEntry.get()
	tk.messagebox.showinfo(
		title = "What is Your Name?",
		message = f"Your name is {name}."
	)

# GROUP: Set up and display the button
displayButton = tk.Button(
	master = window,
	text = "Display my name",
	command = displayName
)
displayButton.pack()

window.mainloop()