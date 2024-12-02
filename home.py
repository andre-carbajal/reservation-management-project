import tkinter as tk

#Fatima Yupa 
def show_home():
    global home

    home = tk.Tk()
    home.resizable(False, False)
    home.title("Home")

    wventana = 854
    hventana = 480
    pwidth = round(home.winfo_screenwidth() / 2 - wventana / 2)
    pheight = round(home.winfo_screenheight() / 2 - hventana / 2)

    home.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

    menu_frame = tk.Frame(home)
    menu_frame.pack(side="left", fill=tk.Y, padx=15, pady=15)

    lista_servicios = ["Esmaltado", "Semipermanente", "Gel", "Esculpidas"]
    pos = 0.3
    for servicio in lista_servicios:
        label = tk.Button(menu_frame, text=servicio)
        label.place(rely=pos)
        pos += 0.08

    boton_reservas = tk.Button(menu_frame, text="Ver Reservaciones")
    boton_reservas.pack(side=tk.BOTTOM)

    home.mainloop()