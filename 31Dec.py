import tkinter as tk

def convert():
    # Implement conversion logic here
    print("Conversion in progress...")

def analyze():
    # Implement analysis logic here
    print("Analyzing data...")

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Tkinter Buttons Example")

# Create Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Create Analyze button
analyze_button = tk.Button(root, text="Analyze", command=analyze)
analyze_button.pack()

# Create Exit button
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack()

# Start the Tkinter event loop
root.mainloop()
