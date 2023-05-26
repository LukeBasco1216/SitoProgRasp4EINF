from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import pymssql

LARGEFONT =("Verdana", 35)


class tkinterApp(tk.Tk):
     
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.grid(row=5,column=5)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Sign_Up, Page3):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, Sign_Up respectively with
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
		command = lambda : controller.show_frame(Sign_Up))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

		button3 = ttk.Button(self, text ="Page 3",
		command = lambda : controller.show_frame(Page3))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)
		


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
							command = lambda : controller.show_frame(Sign_Up))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
		
		button3 = ttk.Button(self, text ="Page 3",
		command = lambda : controller.show_frame(Page3))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame Sign_Up
class Sign_Up(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Inserzione", font = LARGEFONT)
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
	
        button3 = ttk.Button(self, text ="Page 3",
		                    command = lambda : controller.show_frame(Page3))
	
		# putting the button in its place by
		# using grid
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)

        Email = Label(self, text='Insert Email: ')
        Email.grid(row=0, column=0, padx=10, pady=5)

        Nome = Label(self, text='Insert name: ')
        Nome.grid(row=1, column=0, padx=10, pady=5)

        Password = Label(self, text='Insert password: ')
        Password.grid(row=2, column=0, padx=10, pady=5)

        EntryEmail = Entry(self)
        EntryEmail.grid(row=0, column=1, padx=10, pady=5)

        EntryNome = Entry(self)
        EntryNome.grid(row=1, column=1, padx=10, pady=5)

        EntryPassword = Entry(self, show='*')
        EntryPassword.grid(row=2, column=1, padx=10, pady=5)

        Button(self, text="registra", width=20, command=lambda: self.insert(EntryEmail.get(), EntryNome.get(), EntryPassword.get())).grid(row=6, column=0, sticky="w", padx=10, pady=10)

    def insert(self, Email, Nome, Password):
        conn = pymssql.connect(server='5.172.64.20\SQLEXPRESS', database='cilibeanu.nicolae', user='cilibeanu.nicolae', password='xxx123##')
        cursor = conn.cursor()
        Str_Email = str(Email)
        Str_Nome = str(Nome)
        Str_Password = str(Password)

        print("Email:", Str_Email)
        print("Nome:", Str_Nome)
        print("Password:", Str_Password)

        insert_q = "insert into Utente(nome_utente, email, passw) VALUES (%s, %s, %s)"
        vals = (Str_Email, Str_Nome, Str_Password)
        cursor.execute(insert_q, vals)
        conn.commit()
        conn.close()

	# def execute_query(self, Email, Nome, Password):
	#     conn = pymssql.connect(server='5.172.64.20\SQLEXPRESS', database='cilibeanu.nicolae', user='cilibeanu.nicolae', password='xxx123##') #dacasa: 5.172.64.20
	#     cursor = conn.cursor()
	#     Str_Email = str(Email)
	#     Str_Nome = str(Nome)
	#     Str_Password = str(Password)
	#     cursor.execute(f"INSERT INTO Utente (nome_utente, email, passw) VALUES ('{Str_Email}', '{Str_Nome}', '{Str_Password}')")
	#     conn.commit()

		
		
        


class Page3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 3", font = LARGEFONT)
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
		
		button3 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Sign_Up))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)



    







# class UserEditPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
        
#         # Crea i campi di input per i dati dell'utente
#         # Esempio: campo di input per il nome utente
#         self.username_entry = ttk.Entry(self)
#         self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
#         # Crea un pulsante di salvataggio per aggiornare o inserire i dati dell'utente
#         save_button = ttk.Button(self, text="Salva", command=self.save_user_data)
#         save_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
#         # ... Altri campi di input per gli altri dati dell'utente ...
        
#     def save_user_data(self):
#         # Ottieni i valori inseriti dall'utente
#         username = self.username_entry.get()
#         # ... Ottieni gli altri valori degli altri campi di input ...
        
#         # Esegui la query SQL per aggiornare o inserire i dati dell'utente nel database
#         query = "INSERT INTO utente (username) VALUES (%s)"
#         values = (username,)
#         execute_query = (query, values)
        
#         # Mostra un messaggio di conferma all'utente
#         messagebox.showinfo("Conferma", "Dati utente salvati con successo!")











app = tkinterApp()



app.mainloop()