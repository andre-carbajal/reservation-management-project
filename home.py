import tkinter as tk

import ver_reservaciones
from reservation import ReservationFrame


# Fatima Yupa
class HomeWindow:
    def __init__(self):
        self.home = tk.Tk()
        self.home.resizable(False, False)
        self.home.title("Home")

        wventana = 854
        hventana = 580
        pwidth = round(self.home.winfo_screenwidth() / 2 - wventana / 2)
        pheight = round(self.home.winfo_screenheight() / 2 - hventana / 2)

        self.home.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

        for i in range(3):
            self.home.rowconfigure(i, weight=1)
        for j in range(4):
            self.home.columnconfigure(j, weight=1)

        option_panel = tk.Frame(self.home)
        option_panel.grid(row=0, column=0, rowspan=3, sticky="nsew")

        lista_servicios = [("Esmaltado", 25.0), ("Semipermanente", 35.0), ("Gel", 60.0), ("Esculpidas", 90.0)]
        pos = 0.1

        for servicio in lista_servicios:
            button = tk.Button(option_panel, text=servicio[0], command=lambda s=servicio: self.show_reservation_frame(s))
            button.place(relx=0.1, rely=pos, relwidth=0.8, relheight=0.1)
            pos += 0.15

        boton_reservaciones = tk.Button(option_panel, text="Reservaciones", command=ver_reservaciones.init_ver_reservaciones)
        boton_reservaciones.pack(side="bottom", fill="x", padx=10, pady=10)

        self.content_panel = tk.Frame(self.home)
        self.content_panel.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")

        self.home.mainloop()

    # Andre Carbajal
    def show_reservation_frame(self, servicio):
        for widget in self.content_panel.winfo_children():
            widget.destroy()
        reservation_frame = ReservationFrame(master=self.content_panel, servicio=servicio)
        reservation_frame.pack(fill="both", expand=True)