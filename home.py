import tkinter as tk


# Fatima Yupa
class HomeWindow:
    def __init__(self):
        self.home = tk.Tk()
        self.home.resizable(False, False)
        self.home.title("Home")

        wventana = 854
        hventana = 480
        pwidth = round(self.home.winfo_screenwidth() / 2 - wventana / 2)
        pheight = round(self.home.winfo_screenheight() / 2 - hventana / 2)

        self.home.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

        for i in range(3):
            self.home.rowconfigure(i, weight=1)
        for j in range(4):
            self.home.columnconfigure(j, weight=1)

        option_panel = tk.Frame(self.home)
        option_panel.grid(row=0, column=0, rowspan=3, sticky="nsew")

        lista_servicios = ["Esmaltado", "Semipermanente", "Gel", "Esculpidas"]
        pos = 0.1

        for servicio in lista_servicios:
            button = tk.Button(option_panel, text=servicio)
            button.place(relx=0.1, rely=pos, relwidth=0.8, relheight=0.1)
            pos += 0.15

        boton_reservaciones = tk.Button(option_panel, text="Reservaciones")
        boton_reservaciones.pack(side="bottom", fill="x", padx=10, pady=10)

        content_panel = tk.Frame(self.home)
        content_panel.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")

        self.home.mainloop()
