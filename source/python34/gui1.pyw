# Example 5-2 (gui1.pyw)
# A simple 'Hello World' GUI

import tkinter as tk

root = tk.Tk()
root.title('Simple GUI')

my_label = tk.Label(root, text='Hello World!')
my_label.pack()

quit_btn = tk.Button(root, text='Exit', command=quit)
quit_btn.pack()

root.mainloop()
