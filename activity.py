import tkinter as tk
from tkinter import messagebox

# GROUP: Calculation process
def calculate(firstNumber, operand, secondNumber):
	result = "Something went wrong. Please try again."
	try:
		first = float(firstNumber)
		second = float(secondNumber)	
		operator = operand.strip()
		if operator == "+":
			result = f"{first} + {second} = {first + second}"
		elif operator == "-":
			result = f"{first} - {second} = {first - second}"
		elif operator == "*":
			result = f"{first} * {second} = {first * second}"
		elif operator == "/":
			result = f"{first} / {second} = {first / second}"
	except:
		result = "Something went wrong. Please try again."

	return result

# GROUP: Setup views
window = tk.Tk()

# GROUP: Create label and entry for first number
firstNumberLabel = tk.Label(text="First Number:")
firstNumberEntry = tk.Entry()

# GROUP: Create label and entry for operand
operandLabel = tk.Label(text="Operand: ")
operandEntry = tk.Entry()

# GROUP: Create label and entry for second number
secondNumberLabel = tk.Label(text="Second Number:")
secondNumberEntry = tk.Entry()

# SUB-GROUP: Execution of calculation 
def executeCalculation():
	firstNumberArg = firstNumberEntry.get()
	arithmeticOperator = operandEntry.get()
	secondNumberArg = secondNumberEntry.get()
	output = calculate(firstNumberArg,arithmeticOperator,secondNumberArg)
	if output != "Something went wrong. Please try again.":
		messagebox.showinfo(title="Result",message=f"{output}")
	else:
		messagebox.showerror(title="Error",message=f"{output}")

calculateButton = tk.Button(master=window,text="Calculate",command=executeCalculation)

# GROUP: Pack all visual elements in order
usedWidgets = [
	firstNumberLabel,
	firstNumberEntry,
	operandLabel,
	operandEntry,
	secondNumberLabel,
	secondNumberEntry,
	calculateButton
]

for widget in usedWidgets:
	widget.pack()



window.mainloop()