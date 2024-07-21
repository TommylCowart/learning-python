import tkinter as tk
from tkinter import messagebox

# Function to evaluate the code entered by the player
def evaluate_code():
    user_code = code_entry.get("1.0", tk.END).strip()
    if current_level == 5:
        # Check if the specified line is commented out
        if "# This line should be commented out" in user_code:
            messagebox.showinfo("Success", "Correct! The line was commented out.")
            next_level()  # Automatically move to the next level
        else:
            messagebox.showerror("Error", "Incorrect. Make sure to comment out the specified line.")
    else:
        try:
            # Capture and display output for debugging purposes
            from io import StringIO
            import sys
            
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout
            
            exec(user_code, globals())
            sys.stdout = old_stdout
            
            output = new_stdout.getvalue().strip()
            if current_level == 1:
                # Check if a variable was correctly created
                if 'x' in globals() and globals()['x'] == 10:
                    messagebox.showinfo("Success", "Correct! Variable was created.")
                    next_level()  # Automatically move to the next level
                else:
                    messagebox.showerror("Error", "Incorrect. Make sure the variable is defined as x = 10.")
            elif current_level == 2:
                # Ensure the loop runs and prints numbers 0 to 4
                if output == '0\n1\n2\n3\n4':
                    messagebox.showinfo("Success", "Correct! The for loop worked.")
                    next_level()  # Automatically move to the next level
                else:
                    messagebox.showerror("Error", "Incorrect. Make sure the loop prints numbers from 0 to 4.")
            elif current_level == 3:
                # Ensure the while loop runs and prints numbers 0 to 4
                if output == '0\n1\n2\n3\n4':
                    messagebox.showinfo("Success", "Correct! The while loop worked.")
                    next_level()  # Automatically move to the next level
                else:
                    messagebox.showerror("Error", "Incorrect. Make sure the while loop prints numbers from 0 to 4.")
            elif current_level == 4:
                # Check if the if-else statement works as intended
                if 'x' in globals():
                    if globals()['x'] > 5 and output == 'x is greater':
                        messagebox.showinfo("Success", "Correct! The if-else statement worked.")
                        next_level()  # Automatically move to the next level
                    elif globals()['x'] <= 5 and output == 'x is not greater':
                        messagebox.showinfo("Success", "Correct! The if-else statement worked.")
                        next_level()  # Automatically move to the next level
                    else:
                        messagebox.showerror("Error", "Incorrect. Make sure the if-else statement works as intended.")
            else:
                messagebox.showerror("Error", "Unknown level.")
        except Exception as e:
            messagebox.showerror("Error", f"Error in your code: {e}")

# Function to provide hints for the current challenge
def show_hint():
    if current_level == 1:
        hint_message = "Hint: A variable is used to store information. Example: `x = 10`."
    elif current_level == 2:
        hint_message = "Hint: A for loop iterates over a sequence. Example:\n`for i in range(5):\n    print(i)`."
    elif current_level == 3:
        hint_message = "Hint: A while loop runs as long as a condition is True. Example:\n`while i < 5:\n    print(i)`."
    elif current_level == 4:
        hint_message = "Hint: Use if-else to make decisions. Example:\n`if x > 5:\n    print('x is greater')\nelse:\n    print('x is not greater')`."
    elif current_level == 5:
        hint_message = "Hint: To comment out a line in Python, use `#` at the beginning of the line."
    messagebox.showinfo("Hint", hint_message)

# Function to show the answer for the current challenge
def show_answer():
    if current_level == 1:
        answer = """x = 10
"""
    elif current_level == 2:
        answer = """for i in range(5):
    print(i)
"""
    elif current_level == 3:
        answer = """i = 0
while i < 5:
    print(i)
    i += 1
"""
    elif current_level == 4:
        answer = """if x > 5:
    print("x is greater")
else:
    print("x is not greater")
"""
    elif current_level == 5:
        answer = """# This line should be commented out
print("Hello World")
"""
    messagebox.showinfo("Answer", answer)

# Function to provide instructions for the current challenge
def show_instructions():
    if current_level == 1:
        instructions = """Level 1: Creating a Variable
Objective: Declare a variable and assign it a value.

Instructions:
Write a line of code to create a variable and assign it a value.
Example:
x = 10
"""
    elif current_level == 2:
        instructions = """Level 2: Simple For Loop
Objective: Write a for loop to iterate over a range of numbers.

Instructions:
Write a for loop that prints numbers from 0 to 4.
Example:
for i in range(5):
    print(i)
"""
    elif current_level == 3:
        instructions = """Level 3: Simple While Loop
Objective: Write a while loop to print numbers.

Instructions:
Write a while loop that prints numbers from 0 to 4.
Example:
i = 0
while i < 5:
    print(i)
    i += 1
"""
    elif current_level == 4:
        instructions = """Level 4: Simple If-Else Statement
Objective: Use an if-else statement to compare values.

Instructions:
Write an if-else statement to check if a variable is greater than 5 and print a message.
Example:
if x > 5:
    print("x is greater")
else:
    print("x is not greater")
"""
    elif current_level == 5:
        instructions = """Level 5: Commenting Out a Line
Objective: Comment out a specific line of code.

Instructions:
The code below contains a line that should be commented out. Modify the code to comment out the line with the `#` symbol.

Example:
# This line should be commented out
print("Hello World")
"""
    instructions_text.set(instructions)

# Function to move on to the next level
def next_level():
    global current_level
    current_level += 1
    if current_level > 5:
        messagebox.showinfo("Congratulations!", "You've completed all levels!")
        root.quit()  # Exit the application
    else:
        update_level()

# Function to update the UI based on the current level
def update_level():
    global current_level
    show_instructions()  # Update instructions when changing levels
    if current_level == 5:
        code_label.config(text='# This line should be commented out\nprint("Hello World")')
        hint_button.config(command=show_hint)  # Re-enable hint button for level 5
    else:
        code_label.config(text='')
    next_level_button.config(state=tk.DISABLED)  # Initially disabled
    code_entry.delete("1.0", tk.END)

# Main application window
root = tk.Tk()
root.title("Python in Space: Loop Quest")

# Initialize the current level
current_level = 1

# Welcome message
welcome_label = tk.Label(root, text="Welcome to Python in Space: Loop Quest!", font=("Arial", 14))
welcome_label.grid(row=0, column=0, columnspan=5, pady=10)

# Instructions text
instructions_text = tk.StringVar()
instructions_label = tk.Label(root, textvariable=instructions_text, font=("Arial", 14))
instructions_label.grid(row=1, column=0, columnspan=5, pady=10)

# Code entry area
code_entry_label = tk.Label(root, text="Enter your code below:", font=("Arial", 14))
code_entry_label.grid(row=2, column=0, columnspan=5, pady=5)
code_entry = tk.Text(root, height=10, width=60, font=("Arial", 14))
code_entry.grid(row=3, column=0, columnspan=5, pady=5)

# Label for Level 5 code
code_label = tk.Label(root, text='', font=("Arial", 14))
code_label.grid(row=4, column=0, columnspan=5, pady=5)

# Buttons in the same row
buttons_frame = tk.Frame(root)
buttons_frame.grid(row=5, column=0, columnspan=5, pady=5)

instructions_button = tk.Button(buttons_frame, text="Show Instructions", command=show_instructions, font=("Arial", 14))
instructions_button.grid(row=0, column=0, padx=5)

evaluate_button = tk.Button(buttons_frame, text="Run Code", command=evaluate_code, font=("Arial", 14))
evaluate_button.grid(row=0, column=1, padx=5)

hint_button = tk.Button(buttons_frame, text="Show Hint", command=show_hint, font=("Arial", 14))
hint_button.grid(row=0, column=2, padx=5)

answer_button = tk.Button(buttons_frame, text="Show Answer", command=show_answer, font=("Arial", 14))
answer_button.grid(row=0, column=3, padx=5)

next_level_button = tk.Button(buttons_frame, text="Next Level", command=next_level, font=("Arial", 14))
next_level_button.grid(row=0, column=4, padx=5)
next_level_button.config(state=tk.DISABLED)  # Initially disabled

# Run the Tkinter event loop
root.mainloop()
