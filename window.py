import tkinter as tk

window = tk.Tk()
ent_start_date = tk.Entry(width=40)
ent_start_date.insert(0, 'What is your name?')
ent_start_date.pack()
window.mainloop()