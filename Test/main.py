# main.py
import tkinter as tk
import subprocess

def open_calculator():
    subprocess.run(["python", "calculator.py"])

# Create the main Tkinter window
root = tk.Tk()
root.title("Calculator Opener")

# Create a button to open the calculator
start_button = tk.Button(root, text="Start", command=open_calculator)
start_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
