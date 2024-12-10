import tkinter as tk
from tkinter import messagebox


class ReservationFrame(tk.Frame):
    # Andre Carbajal
    def __init__(self, master=None, servicio=None):
        super().__init__(master, bg='red')
        self.entradas = []
        self.master = master
        self.servicio = servicio
        self.pack()
        self.create_widgets()

    # Mariela Ramos
    def create_widgets(self):
        campo_frame = tk.Frame(self, bg='red')
        campo_frame.pack()

        campos = ["Nombre", "Teléfono", "Fecha", "Hora"]
        for campo in campos:
            etiqueta = tk.Label(campo_frame, text=campo)
            etiqueta.pack(fill=tk.X, pady=5)
            entrada = tk.Entry(campo_frame, width=40)
            entrada.pack(fill=tk.X, pady=5)
            self.entradas.append(entrada)

        boton_agendar = tk.Button(campo_frame, text="Agendar", command=self.verificar_casillas)
        boton_agendar.pack(pady=20)

    # Mariela Ramos
    def verificar_casillas(self):
        for entry in self.entradas:
            if not entry.get().strip():
                messagebox.showwarning("Advertencia", "Debe completar todas las casillas para continuar.")
                return
