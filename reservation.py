import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import re

class ReservationFrame(tk.Frame):
    def __init__(self, master=None, servicio=None):
        super().__init__(master, bg='lightgray')
        self.master = master
        self.servicio = servicio
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        campo_frame = tk.Frame(self, bg='lightgray')
        campo_frame.pack()

        # Tipo de Uña (fijo)
        tk.Label(campo_frame, text="Tipo de Uña:", font=("Arial", 12), bg="lightgray").pack(pady=(20, 5))
        tipo_uña_label = tk.Label(campo_frame, text="Manicura Gel - S/50.00", font=("Arial", 12), bg="white")
        tipo_uña_label.pack(pady=(0, 10))

        # Campo para Nombre
        tk.Label(campo_frame, text="Nombre:", font=("Arial", 12), bg="lightgray").pack(pady=(10, 5))
        entry_nombre = tk.Entry(campo_frame, font=("Arial", 12), width=30)
        entry_nombre.pack(pady=(0, 10))
        self.entradas.append(entry_nombre)

        # Campo para Teléfono
        def validate_telefono(P):
            return (P.isdigit() and len(P) <= 9) or P == ""

        vcmd = (self.register(validate_telefono), "%P")
        tk.Label(campo_frame, text="Teléfono:", font=("Arial", 12), bg="lightgray").pack(pady=(10, 5))
        entry_telefono = tk.Entry(campo_frame, font=("Arial", 12), width=30, validate="key", validatecommand=vcmd)
        entry_telefono.pack(pady=(0, 10))
        self.entradas.append(entry_telefono)

        # Campo para Fecha
        def seleccionar_fecha():
            def guardar_fecha():
                entry_fecha.config(state="normal")
                entry_fecha.delete(0, tk.END)
                entry_fecha.insert(0, calendario.get_date())
                entry_fecha.config(state="readonly")
                ventana_fecha.destroy()

            ventana_fecha = tk.Toplevel(self.master)
            ventana_fecha.title("Seleccionar Fecha")
            calendario = Calendar(ventana_fecha, selectmode="day", date_pattern="yyyy-mm-dd")
            calendario.pack(pady=10)
            tk.Button(ventana_fecha, text="Guardar", command=guardar_fecha).pack(pady=5)

        tk.Label(campo_frame, text="Fecha:", font=("Arial", 12), bg="lightgray").pack(pady=(10, 5))
        entry_fecha = tk.Entry(campo_frame, font=("Arial", 12), width=30, state="readonly")
        entry_fecha.pack(pady=(0, 5))
        tk.Button(campo_frame, text="Seleccionar Fecha", command=seleccionar_fecha).pack(pady=(0, 10))
        self.entradas.append(entry_fecha)

        # Campo para Hora
        def seleccionar_hora():
            def guardar_hora():
                horas = spin_hora.get()
                minutos = spin_minuto.get()
                periodo = am_pm.get()
                entry_hora.config(state="normal")
                entry_hora.delete(0, tk.END)
                entry_hora.insert(0, f"{horas}:{minutos} {periodo}")
                entry_hora.config(state="readonly")
                ventana_hora.destroy()

            ventana_hora = tk.Toplevel(self.master)
            ventana_hora.title("Seleccionar Hora")

            tk.Label(ventana_hora, text="Hora:").pack(pady=(10, 5))
            spin_hora = tk.Spinbox(ventana_hora, from_=1, to=12, width=5, wrap=True)
            spin_hora.pack(side=tk.LEFT, padx=5)

            tk.Label(ventana_hora, text=":").pack(side=tk.LEFT)

            spin_minuto = tk.Spinbox(ventana_hora, from_=0, to=59, width=5, wrap=True, format="%02.0f")
            spin_minuto.pack(side=tk.LEFT, padx=5)

            am_pm = tk.StringVar(value="AM")
            tk.OptionMenu(ventana_hora, am_pm, "AM", "PM").pack(side=tk.LEFT, padx=5)

            tk.Button(ventana_hora, text="Guardar", command=guardar_hora).pack(pady=10)

        tk.Label(campo_frame, text="Hora:", font=("Arial", 12), bg="lightgray").pack(pady=(10, 5))
        entry_hora = tk.Entry(campo_frame, font=("Arial", 12), width=30, state="readonly")
        entry_hora.pack(pady=(0, 5))
        tk.Button(campo_frame, text="Seleccionar Hora", command=seleccionar_hora).pack(pady=(0, 10))
        self.entradas.append(entry_hora)

        # Botón para Agendar
        btn_agendar = tk.Button(campo_frame, text="Agendar", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.agendar_cita)
        btn_agendar.pack(pady=(20, 20))

    def agendar_cita(self):
        tipo_uña = "Manicura Gel - S/50.00"
        nombre = self.entradas[0].get()
        telefono = self.entradas[1].get()
        fecha = self.entradas[2].get()
        hora = self.entradas[3].get()

        if not nombre or not telefono or not fecha or not hora:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        if not re.fullmatch(r"\d{9}", telefono):
            messagebox.showwarning("Teléfono inválido", "Por favor, ingresa un número de teléfono válido (9 dígitos).")
            return

        messagebox.showinfo(
            "Cita Agendada",
            f"Cita agendada con éxito:\n\nTipo de Uña: {tipo_uña}\nNombre: {nombre}\nTeléfono: {telefono}\nFecha: {fecha}\nHora: {hora}"
        )