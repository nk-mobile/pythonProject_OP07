import tkinter as tk

def on_button_click():
    label2.config(text="Привет, " + str(entry.get() + "!!!" ))

root = tk.Tk()
root.title('Привет!!!')
root.geometry('300x100')

label = tk.Label(root, text='введите свое имя:')

entry = tk.Entry(root)

button = tk.Button(root, text="Дальше ->", command=on_button_click)

label2 = tk.Label(root, text='')
# label2.pack()

label.grid(column=0, row=0)
entry.grid(column=0, row=1)
button.grid(column=1, row=1)
label2.grid(column=0, row=2)
root.mainloop()
