import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox

def find_and_display_numbers():
    # Get user input
    user_input = text_widget.get("1.0", "end-1c").split('\n')
    
    matching_numbers = []
    for input_letter in user_input:
        # Find matching row in the DataFrame
        matching_row = df[df['letters'] == input_letter]
        
        if not matching_row.empty:
            matching_numbers.append(matching_row.iloc[0]['numbers'])
    
    if matching_numbers:
        result_text = "\n".join(map(str, matching_numbers))
        result_text_widget.delete("1.0", "end")
        result_text_widget.insert("1.0", result_text)
        copy_button.config(state=tk.NORMAL)
    else:
        messagebox.showinfo("No Matches", "No matching rows found.")
        result_text_widget.delete("1.0", "end")
        copy_button.config(state=tk.DISABLED)

def copy_to_clipboard():
    result_text = result_text_widget.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(result_text)
    root.update()

# Create the tkinter main window
root = tk.Tk()
root.title("Letter and Number Lookup")

# Load the Excel sheet into a DataFrame
file_path = r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\example_spreadsheet_for_translator.xlsx'

df = pd.read_excel(file_path)

# Create a text widget to input letters
text_widget = tk.Text(root, height=5, width=30)
text_widget.pack(padx=10, pady=5)

# Create a button to trigger the search
search_button = tk.Button(root, text="Search", command=find_and_display_numbers)
search_button.pack()

# Create a text widget to display results
result_text_widget = tk.Text(root, height=10, width=30)
result_text_widget.pack(padx=10, pady=5)

# Create a button to copy results to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack()

# Start the tkinter event loop
root.mainloop()
