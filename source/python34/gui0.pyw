# Example 5-1 (gui0.py)
# A simple 'Hello World' GUI

import tkinter as tk

root = tk.Tk()
root.title('Simple GUI')

my_label = tk.Label(root, text='Hello World!')
my_label.pack()

root.mainloop()
