from tkinter import *
from tkinter import messagebox

import os
os.system('clear')

root = Tk()
root.title('ProgettoRaspberry')

frame = Frame(root)
frame.pack()


def SubmitCommand():
    Hello_Label = Label(root, text = 'Good morning!' + Cognome.get() + ' ' + Nome.get())
    Hello_Label.pack()



Cognome = Label(root, text = 'Inserisci il tuo cognome: ').grid(row=0)

Nome = Label(root, text = 'Inserisci il tuo nome').grid(row=1)

Password = Label(root, text = 'Inserisci il tuo password').grid(row=2)

EntryCognome = Entry(root)
EntryNome = Entry(root)
# 以 * 的形式显示密码
EntryPassword = Entry(root,show='*')
EntryCognome.grid(row=0, column=1, padx=10, pady=5)
EntryNome.grid(row=1, column=1, padx=10, pady=5)
EntryPassword.grid(row=2, column=1, padx=10, pady=5)


Button(root, text="Login", width=10, command=SubmitCommand).grid(row=3, column=0, sticky="w", padx=10, pady=5)
Button(root, text="Close", width=10, command=root.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)







root.mainloop()