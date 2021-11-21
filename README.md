
# Tkinter Guide
This is a documentation of the use of Tkinter in a **calculator** wherein you input your numbers and an operator to their *entries* then tap a *button* to calculate between two numbers then display the result using a *message box* created by Arthur Tristan M. Ramos to present in the 2021 Mini Workshop Series: Into Coding: Introduction to Python Libraries.

## Tkinter
Tkinter is the standard cross-platform Graphical User Interface (GUI) framework of Python. The display of its visual elements are native so it's dependent on the operating system of the computer.

## Import Tkinter
Import the Tkinter library to your program. Most commonly name it *tk*.

```
import tkinter as tk
```

## f-Strings
f-Strings are a cleaner and new way of formatted strings in Python 3 where it starts with **f** the followed by a string literal enclosed in quotation marks ("") wherein interpolated literals, variables or expressions are enclosed in curly braces (**{}**) 

```
name = "Joshua"
string1 = f"My name is {name}."
string2 = f"My jeepney fare always amounts to Php {3 + 5}"

print(string1)
print(string2)

# Output:
# My name is Joshua.
# My jeepney fare always amounts to Php 8.
```

## Set up Window
The *window* is an instance of the Tk class. Here, you will set up and display the visual elements.

```
window = tk.Tk()
```

## Run the Event Loop
This is where the window accepts events like button clicks and keypresses. This method below blocks code after this until the window is closed. This is always written in the last part of the program.

```
window.mainloop()
```


## Widgets
Widgets are the visual elements of the application where the user interacts to make the solutions to his/her problems happen easier and faster.

## widget.pack()
 This is used to organize widgets before placing them in the parent widget.
 
## 1. Label
This is a widget that displays text serving as a placeholder on top of an entry or text field showing what data the user inputs. In this example, the function needs a **text** which is a string that will label that the data to input is *name*.
```
nameLabel = tk.Label(text="Name:")
nameLabel.pack()
```

## 2. Entry
This is a widget where you *enter text* to input data that will be processed. This only accepts single line of text. This block of code shows you how to create and display an entry text box.

```
nameEntry = tk.Entry()
nameEntry.pack()

# Get value of entry. This returns a string. User inputs "Juan Dela Cruz".
name = nameEntry.get()
print(name)

# Output:
# Juan Dela Cruz
```

## 3. Button
This is a widget that executes a command when the user clicks it. It has 3 parameters:

 - *master* - The parent window where the button is displayed
 - *text* - The text that displays what the button does when clicked
 - *command* - This is the callback function or method that the button executes when clicked

```
# This is the function to execute.
def displayMessage():
	print("Welcome! How are you?")

messageButton = tk.Button(
	master = window,
	text = "Display Message",
	command = displayMessage
)
```

## Functions vs. Methods
*Functions* return a value, it may be an string, integer, list or any data type.
*Methods* do not return anything. They just execute lines of code.

**Function**
```
def sum(first, second):
   return first + second

myVariable = sum(2,3)
print(myVariable)

# Output:
# 5
```

**Method**
```
def displayMessage():
	print("Hello World!")

displayMessage()

# Output:
# Hello World!
```

## 4. Message Box
This is a window that displays a message from the system to deliver a response to a user after a user has done something like usually clicking a button. Each of its methods (e.g. showinfo and showerror) usually have 2 parameters:

 - *title* - Title of the message box
 - *message* - The message itself

## Information Message Box
A message box displaying information
```
tk.messagebox.showinfo(
	title="Information", 
	message="You have clicked this button to show some information."
)
```

## Error Message Box
A message box displaying error
```
tk.messagebox.showerror(
	title="Information", 
	message="There is no Internet. Please try again."
)
```

## Display Name
![Display Name for Lesson](https://github.com/dev-arthur-g20r/pylib-tkinter/blob/main/images/DisplayName.jpg)

## Calculator
![Calculator for Activity](https://github.com/dev-arthur-g20r/pylib-tkinter/blob/main/images/Calculator.jpg)


> Written with [StackEdit](https://stackedit.io/).
