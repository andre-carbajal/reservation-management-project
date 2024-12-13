import re
import sqlite3
import tkinter as tk
from datetime import date
from tkinter import messagebox

from tkcalendar import Calendar


# Mariela Ramos
class ReservationFrame(tk.Frame):
    def __init__(self, master=None, servicio=None):
        super().__init__(master, bg='#F0E6F6')
        self.master = master
        self.servicio = servicio
        self.entradas = []
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        campo_frame = tk.Frame(self, bg='#F0E6F6')
        campo_frame.pack()

        tk.Label(campo_frame, text="Tipo de Uña:", font=("Arial", 12), bg="#F0E6F6", fg="#6A3D9A").pack(pady=(20, 5))
        self.tipo_uña_label = tk.Label(campo_frame, text=f"{self.servicio[0]} - S/{self.servicio[1]:.2f}",
                                       font=("Arial", 12), bg="white", fg="#6A3D9A")
        self.tipo_uña_label.pack(pady=(0, 10))

        tk.Label(campo_frame, text="Nombre:", font=("Arial", 12), bg="#F0E6F6", fg="#6A3D9A").pack(pady=(10, 5))
        entry_nombre = tk.Entry(campo_frame, font=("Arial", 12), width=30)
        entry_nombre.pack(pady=(0, 10))
        self.entradas.append(entry_nombre)

        def validate_telefono(P):
            return (P.isdigit() and len(P) <= 9) or P == ""

        vcmd = (self.register(validate_telefono), "%P")
        tk.Label(campo_frame, text="Teléfono:", font=("Arial", 12), bg="#F0E6F6", fg="#6A3D9A").pack(pady=(10, 5))
        entry_telefono = tk.Entry(campo_frame, font=("Arial", 12), width=30, validate="key", validatecommand=vcmd)
        entry_telefono.pack(pady=(0, 10))
        self.entradas.append(entry_telefono)

        def seleccionar_fecha():
            def guardar_fecha():
                entry_fecha.config(state="normal")
                entry_fecha.delete(0, tk.END)
                entry_fecha.insert(0, calendario.get_date())
                entry_fecha.config(state="readonly")
                ventana_fecha.destroy()

            ventana_fecha = tk.Toplevel(self.master)
            ventana_fecha.title("Seleccionar Fecha")
            ventana_ancho = 300
            ventana_alto = 250

            pantalla_ancho = ventana_fecha.winfo_screenwidth()
            pantalla_alto = ventana_fecha.winfo_screenheight()

            pos_x = (pantalla_ancho // 2) - (ventana_ancho // 2)
            pos_y = (pantalla_alto // 2) - (ventana_alto // 2)

            ventana_fecha.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")
            calendario = Calendar(ventana_fecha, selectmode="day", date_pattern="yyyy-mm-dd", mindate=date.today())
            calendario.pack(pady=10)
            tk.Button(ventana_fecha, text="Guardar", command=guardar_fecha, bg="#6A3D9A", fg="white").pack(
                pady=5)  # Purple button

        tk.Label(campo_frame, text="Fecha:", font=("Arial", 12), bg="#F0E6F6", fg="#6A3D9A").pack(pady=(10, 5))
        entry_fecha = tk.Entry(campo_frame, font=("Arial", 12), width=30, state="readonly")
        entry_fecha.pack(pady=(0, 5))
        tk.Button(campo_frame, text="Seleccionar Fecha", command=seleccionar_fecha, bg="#6A3D9A", fg="white").pack(
            pady=(0, 10))  # Purple button
        self.entradas.append(entry_fecha)

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
            ventana_hora.resizable(False, False)

            ventana_ancho = 270
            ventana_alto = 80

            pantalla_ancho = ventana_hora.winfo_screenwidth()
            pantalla_alto = ventana_hora.winfo_screenheight()

            pos_x = (pantalla_ancho // 2) - (ventana_ancho // 2)
            pos_y = (pantalla_alto // 2) - (ventana_alto // 2)

            tk.Label(ventana_hora, text="Hora:", font=("Arial", 12), bg="#F0E6F6", fg="#6A3D9A").pack(
                pady=(10, 5))
            ventana_hora.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")
            spin_hora = tk.Spinbox(ventana_hora, from_=1, to=12, width=5, wrap=True)
            spin_hora.pack(side=tk.LEFT, padx=5)

            tk.Label(ventana_hora, text=":", font=("Arial", 12), bg="#F0E6F6", fg="#6A3D9A").pack(side=tk.LEFT)

            spin_minuto = tk.Spinbox(ventana_hora, from_=0, to=59, width=5, wrap=True, format="%02.0f")
            spin_minuto.pack(side=tk.LEFT, padx=5)

            am_pm = tk.StringVar(value="AM")
            tk.OptionMenu(ventana_hora, am_pm, "AM", "PM").pack(side=tk.LEFT, padx=5)

            tk.Button(ventana_hora, text="Guardar", command=guardar_hora, bg="#6A3D9A", fg="white").pack(
                pady=10)  # Purple button

        tk.Label(campo_frame, text="Hora:", font=("Arial", 12), bg="#F0E6F6", fg="#6A3D9A").pack(pady=(10, 5))
        entry_hora = tk.Entry(campo_frame, font=("Arial", 12), width=30, state="readonly")
        entry_hora.pack(pady=(0, 5))
        tk.Button(campo_frame, text="Seleccionar Hora", command=seleccionar_hora, bg="#6A3D9A", fg="white").pack(
            pady=(0, 10))  # Purple button
        self.entradas.append(entry_hora)

        btn_agendar = tk.Button(campo_frame, text="Agendar", font=("Arial", 12), bg="#9C4F96", fg="white",
                                # Dark purple button
                                command=lambda s=self.servicio: self.agendar_cita(s))
        btn_agendar.pack(pady=(20, 20))

    # Andre Carbajal
    def agendar_cita(self, servicio):
        nombre = self.entradas[0].get()
        telefono = self.entradas[1].get()
        tipo = servicio[0]
        precio = servicio[1]
        fecha = self.entradas[2].get()
        hora = self.entradas[3].get()

        if not nombre or not telefono or not fecha or not hora:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        if not re.fullmatch(r"\d{9}", telefono):
            messagebox.showwarning("Teléfono inválido", "Por favor, ingresa un número de teléfono válido (9 dígitos).")
            return

        hora_reservacion = int(hora.split(":")[0]) * 60 + int(hora.split(":")[1].split(" ")[0])
        if "PM" in hora and int(hora.split(":")[0]) != 12:
            hora_reservacion += 12 * 60
        elif "AM" in hora and int(hora.split(":")[0]) == 12:
            hora_reservacion -= 12 * 60

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT hora FROM reservaciones WHERE fecha = ?
        ''', (fecha,))
        reservaciones = cursor.fetchall()

        for reservacion in reservaciones:
            hora_existente = reservacion[0]
            hora_existente_minutos = int(hora_existente.split(":")[0]) * 60 + int(
                hora_existente.split(":")[1].split(" ")[0])
            if "PM" in hora_existente and int(hora_existente.split(":")[0]) != 12:
                hora_existente_minutos += 12 * 60
            elif "AM" in hora_existente and int(hora_existente.split(":")[0]) == 12:
                hora_existente_minutos -= 12 * 60

            if abs(hora_reservacion - hora_existente_minutos) < 45:
                messagebox.showwarning("Conflicto de horario", "Ya existe una reservación en el mismo rango de tiempo.")
                conn.close()
                return

        cursor.execute('''
        INSERT INTO reservaciones (nombre, telefono, tipo, precio, fecha, hora, terminado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, telefono, tipo, precio, fecha, hora, False))
        conn.commit()
        conn.close()

        messagebox.showinfo("Éxito", "La cita ha sido agendada correctamente.")
