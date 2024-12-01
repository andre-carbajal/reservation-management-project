import tkinter as tk

def loginUser():
    print("Inicio sesion")

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
loginButton = tk.Button(login, text="Login", command=loginUser)

# Centering the content
email.place(relx=0.5, rely=0.3, anchor='center')
emailText.place(relx=0.5, rely=0.35, anchor='center')
password.place(relx=0.5, rely=0.4, anchor='center')
passwordText.place(relx=0.5, rely=0.45, anchor='center')
loginButton.place(relx=0.5, rely=0.55, anchor='center')

login.mainloop()