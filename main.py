import tkinter as tk
from tkinter import messagebox

def login_user(email, password):
    if email == "user@example.com" and password == "123":
        print("Inicio sesion")
    else:
        messagebox.showerror("Error al iniciar sesion", "Email o contraseña incorrectos")

def on_login_button_click():
    email = emailText.get()
    password = passwordText.get()
    login_user(email, password)

login = tk.Tk()
login.resizable(False, False)
login.title("Login")

wventana = 854
hventana = 480
pwidth = round(login.winfo_screenwidth() / 2 - wventana / 2)
pheight = round(login.winfo_screenheight() / 2 - hventana / 2)

login.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

email = tk.Label(login, text="Ingrese su email:")
emailText = tk.Entry(login, width=40)
password = tk.Label(login, text="Ingrese su contraseña:")
passwordText = tk.Entry(login, show="*", width=40)
loginButton = tk.Button(login, text="Login", command=on_login_button_click)

email.place(relx=0.5, rely=0.3, anchor='center')
emailText.place(relx=0.5, rely=0.35, anchor='center')
password.place(relx=0.5, rely=0.4, anchor='center')
passwordText.place(relx=0.5, rely=0.45, anchor='center')
loginButton.place(relx=0.5, rely=0.55, anchor='center')

login.mainloop()