import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Tkinter Application")

        # Create the entry window
        self.entry_window = tk.Entry(self.root)
        self.entry_window.pack()

        # Create the output window
        self.output_window = tk.Text(self.root)
        self.output_window.pack()

        # Create the button
        self.button = tk.Button(self.root, text="Press Me", command=self.display_text)
        self.button.pack()

        # Start the mainloop
        self.root.mainloop()

    def display_text(self):
        # Get the text from the entry window
        text = self.entry_window.get()

        # Display the text in the output window
        self.output_window.insert(tk.END, text + "\n")

if __name__ == "__main__":
    app = App()
