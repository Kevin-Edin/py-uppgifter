import tkinter as tk

root = tk.Tk()
root.title('Counting Seconds')
tk.Label(root, text='Name').grid(row=0)
tk.Label(root, text='Password').grid(row=1)
user = tk.Entry(root)
password = tk.Entry(root)
user.grid(row=0, column=1)
password.grid(row=1, column=1)

result_label = tk.Label(root, text='')
result_label.grid(row=4, columnspan=2)

def show():
    print('User:', user.get())
    print('Password:', password.get())
    result_label.config(text=f'User: {user.get()}\nPassword: {password.get()}')

tk.Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Show', command=show).grid(row=3, column=1, sticky=tk.W, pady=4) 
root.mainloop()