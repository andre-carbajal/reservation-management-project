import tkinter as tk

def inicioSesion():
    print("Inicio secion")
          
login = tk.Tk()
login.resizable(0,0)
login.title("Login")

wventana = 854
hventana = 480
pwidth = round(login.winfo_screenwidth()/2-wventana/2)
pheight = round(login.winfo_screenheight()/2-hventana/2)

login.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

email = tk.Label(login, text="Ingrese su email")
emailText = tk.Entry(login)
email.pack()
emailText.pack()

password = tk.Label(login, text="Ingrese su contraseña")
passwordText = tk.Entry(login)
password.pack()
passwordText.pack()

loginButton = tk.Button(login, text="Login")
loginButton.pack()

login.mainloop()