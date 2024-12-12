import sqlite3
import tkinter as tk
from tkinter import messagebox

from home import HomeWindow


# Andre Carbajal
def login_user(email, password, login_instance):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email=? AND password=?", (email, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        login_instance.login.destroy()
        HomeWindow()
    else:
        messagebox.showerror("Error al iniciar sesion", "Email o contraseña incorrectos")


# Fatima Yupa
class LoginWindow:
    def __init__(self):
        self.login = tk.Tk()
        self.login.resizable(False, False)
        self.login.title("Login")

        wventana = 854
        hventana = 480
        pwidth = round(self.login.winfo_screenwidth() / 2 - wventana / 2)
        pheight = round(self.login.winfo_screenheight() / 2 - hventana / 2)

        self.login.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

        email = tk.Label(self.login, text="Ingrese su email:")
        self.emailText = tk.Entry(self.login, width=40)
        password = tk.Label(self.login, text="Ingrese su contraseña:")
        self.passwordText = tk.Entry(self.login, show="*", width=40)
        loginButton = tk.Button(self.login, text="Login", command=self.on_login_button_click)

        email.place(relx=0.5, rely=0.3, anchor='center')
        self.emailText.place(relx=0.5, rely=0.35, anchor='center')
        password.place(relx=0.5, rely=0.4, anchor='center')
        self.passwordText.place(relx=0.5, rely=0.45, anchor='center')
        loginButton.place(relx=0.5, rely=0.55, anchor='center')

        self.login.bind('<Return>', self.on_login_button_click)
        self.login.mainloop()

    def on_login_button_click(self, event=None):
        email = self.emailText.get()
        password = self.passwordText.get()
        login_user(email, password, self)
