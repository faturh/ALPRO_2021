import tkinter as tk

# Create the first Tkinter window
window1 = tk.Tk()
window1.title("Window 1")

# Function to open a new window and close the current window
def open_new_window():
    # Close the current window
    window1.destroy()

    # Create the new Tkinter window
    window2 = tk.Tk()
    window2.title("Window 2")

# Create a button to open the new window
open_button = tk.Button(window1, text="Open New Window", command=open_new_window)
open_button.pack()

# Run the Tkinter event loop
window1.mainloop()
