import sqlite3
import sys
import tkinter as tk
from tkinter import messagebox

from home import HomeWindow

INTENTOS_MAXIMO = 3


# Andre Carbajal
def login_user(email, password, login_instance):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email=? AND password=?", (email, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        login_instance.intentos = 0
        login_instance.login.destroy()
        HomeWindow()
    else:
        login_instance.intentos += 1
        remaining_attempts = INTENTOS_MAXIMO - login_instance.intentos
        if login_instance.intentos >= INTENTOS_MAXIMO:
            messagebox.showerror("Error al iniciar sesión", "Demasiados intentos fallidos. El programa se cerrará.")
            login_instance.login.destroy()
            sys.exit()
        else:
            messagebox.showerror("Error al iniciar sesión",
                                 f"Email o contraseña incorrectos. Intentos restantes: {remaining_attempts}")


# Fatima Yupa
class LoginWindow:
    def __init__(self):
        self.intentos = 0
        self.login = tk.Tk()
        self.login.resizable(False, False)
        self.login.title("Login")

        wventana = 854
        hventana = 480
        pwidth = round(self.login.winfo_screenwidth() / 2 - wventana / 2)
        pheight = round(self.login.winfo_screenheight() / 2 - hventana / 2)

        self.login.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

        self.login.configure(bg="#EDE7F6")

        title = tk.Label(self.login, text="Bienvenido", font=("Arial", 20, "bold"), bg="#EDE7F6", fg="#5E35B1")
        title.place(relx=0.5, rely=0.2, anchor='center')

        email_label = tk.Label(self.login, text="Email", font=("Arial", 12), bg="#EDE7F6", fg="#5E35B1")
        email_label.place(relx=0.5, rely=0.35, anchor='center')
        self.emailText = tk.Entry(self.login, width=30, font=("Arial", 12))
        self.emailText.place(relx=0.5, rely=0.4, anchor='center')

        password_label = tk.Label(self.login, text="Contraseña", font=("Arial", 12), bg="#EDE7F6", fg="#5E35B1")
        password_label.place(relx=0.5, rely=0.5, anchor='center')
        self.passwordText = tk.Entry(self.login, show="*", width=30, font=("Arial", 12))
        self.passwordText.place(relx=0.5, rely=0.55, anchor='center')

        loginButton = tk.Button(self.login, text="Login", command=self.on_login_button_click,
                                font=("Arial", 12, "bold"),
                                bg="#7E57C2", fg="white", width=15, relief="flat", cursor="hand2")
        loginButton.place(relx=0.5, rely=0.7, anchor='center')

        self.login.bind('<Return>', self.on_login_button_click)
        self.login.mainloop()

    def on_login_button_click(self, event=None):
        email = self.emailText.get()
        password = self.passwordText.get()
        login_user(email, password, self)


if __name__ == "__main__":
    LoginWindow()
