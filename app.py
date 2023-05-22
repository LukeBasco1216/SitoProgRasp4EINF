from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('ProgettoRaspberry')

frame = Frame(root)
frame.grid()
LARGEFONT =("Verdana", 35)


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        Cognome = Label(root, text = 'Inserisci il tuo cognome: ').grid(row=0)

        Nome = Label(root, text = 'Inserisci il tuo nome: ').grid(row=1)

        Password = Label(root, text = 'Inserisci il tuo password: ').grid(row=2)

        EntryCognome = Entry(root)
        EntryNome = Entry(root)
        EntryPassword = Entry(root,show='*')
        EntryCognome.grid(row=0, column=1, padx=10, pady=5)
        EntryNome.grid(row=1, column=1, padx=10, pady=5)
        EntryPassword.grid(row=2, column=1, padx=10, pady=5)
        
        Hello_Label = Label(root, text = 'Good morning!' + EntryCognome.get() + ' ' + EntryNome.get())
        Hello_Label.grid()

        Button(root, text="Login", width=10, command=Hello_Label).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        Button(root, text="Close", width=10, command=root.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)

        






    







class UserEditPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Crea i campi di input per i dati dell'utente
        # Esempio: campo di input per il nome utente
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Crea un pulsante di salvataggio per aggiornare o inserire i dati dell'utente
        save_button = ttk.Button(self, text="Salva", command=self.save_user_data)
        save_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # ... Altri campi di input per gli altri dati dell'utente ...
        
    def save_user_data(self):
        # Ottieni i valori inseriti dall'utente
        username = self.username_entry.get()
        # ... Ottieni gli altri valori degli altri campi di input ...
        
        # Esegui la query SQL per aggiornare o inserire i dati dell'utente nel database
        query = "INSERT INTO utente (username) VALUES (%s)"
        values = (username,)
        execute_query = (query, values)
        
        # Mostra un messaggio di conferma all'utente
        messagebox.showinfo("Conferma", "Dati utente salvati con successo!")














root.mainloop()