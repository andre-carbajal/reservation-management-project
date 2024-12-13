import sqlite3
import tkinter as tk
from tkinter import messagebox

# Define global variables
frame_canvas = None
canvas = None


class Reservation_Frame(tk.Frame):
    def __init__(self, master=None, reserva=None):
        super().__init__(master, bg='white', bd=2, relief="groove")
        self.master = master
        self.reserva = reserva
        self.pack(pady=0, fill=tk.X)
        self.create_widgets()

    def create_widgets(self):
        # Contenedor principal
        container_frame = tk.Frame(self, bg='#f0f0f0', padx=150, pady=20)
        container_frame.pack(fill=tk.X, padx=20, pady=20)

        # Mostrar los datos de la reserva
        tk.Label(container_frame, text=f"{self.reserva['tipo_uña']}", font=("Arial", 14, "bold"), bg='#f0f0f0').pack(
            anchor="w", pady=5)
        tk.Label(container_frame, text=f"Teléfono: {self.reserva['telefono']}", bg='#f0f0f0', font=("Arial", 12)).pack(
            anchor="w", pady=2)
        tk.Label(container_frame, text=f"Fecha: {self.reserva['fecha']} - Hora: {self.reserva['hora']}", bg='#f0f0f0',
                 font=("Arial", 12)).pack(anchor="w", pady=2)
        tk.Label(container_frame, text=f"Nombre: {self.reserva['nombre']}", bg='#f0f0f0', font=("Arial", 12)).pack(
            anchor="w", pady=2)

        # Botones para acciones
        btn_frame = tk.Frame(container_frame, bg='#f0f0f0')
        btn_frame.pack(fill=tk.X, pady=5)
        tk.Button(btn_frame, text="Editar", bg="orange", fg="white", font=("Arial", 10, "bold"), relief="flat",
                  command=self.editar).pack(side=tk.RIGHT, padx=5)
        tk.Button(btn_frame, text="Cancelar", bg="red", fg="white", font=("Arial", 10, "bold"), relief="flat",
                  command=self.cancelar).pack(side=tk.RIGHT, padx=5)

    def editar(self):
        self.edit_window = tk.Toplevel(self.master)
        self.edit_window.title("Editar Reserva")
        self.edit_window.geometry("400x400")
        self.edit_window.configure(bg="#f7f9fc")

        header = tk.Label(self.edit_window, text="Editar Reserva", font=("Arial", 16, "bold"), bg="#f7f9fc", fg="#333")
        header.pack(pady=10)

        form_frame = tk.Frame(self.edit_window, bg="#f7f9fc")
        form_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Nombre
        tk.Label(form_frame, text="Nombre:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=0, column=0,
                                                                                               sticky="w", pady=5)
        nombre_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        nombre_entry.insert(0, self.reserva['nombre'])
        nombre_entry.grid(row=0, column=1, pady=5)

        # Teléfono
        tk.Label(form_frame, text="Teléfono:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=1, column=0,
                                                                                                 sticky="w", pady=5)
        telefono_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        telefono_entry.insert(0, self.reserva['telefono'])
        telefono_entry.grid(row=1, column=1, pady=5)

        # Fecha
        tk.Label(form_frame, text="Fecha:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=2, column=0,
                                                                                              sticky="w", pady=5)
        fecha_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        fecha_entry.insert(0, self.reserva['fecha'])
        fecha_entry.grid(row=2, column=1, pady=5)

        # Hora
        tk.Label(form_frame, text="Hora:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=3, column=0,
                                                                                             sticky="w", pady=5)
        hora_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        hora_entry.insert(0, self.reserva['hora'])
        hora_entry.grid(row=3, column=1, pady=5)

        # Tipo de Uña
        tk.Label(form_frame, text="Tipo de Uña:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=4, column=0,
                                                                                                    sticky="w", pady=5)
        tipo_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        tipo_entry.insert(0, self.reserva['tipo_uña'])
        tipo_entry.grid(row=4, column=1, pady=5)

        # Botón Guardar
        save_button = tk.Button(self.edit_window, text="Guardar Cambios", font=("Arial", 12, "bold"), bg="#4CAF50",
                                fg="white", relief="flat",
                                command=lambda: self.guardar_cambios(nombre_entry.get(), telefono_entry.get(),
                                                                     fecha_entry.get(), hora_entry.get(),
                                                                     tipo_entry.get()))
        save_button.pack(pady=20)

    def guardar_cambios(self, nombre, telefono, fecha, hora, tipo):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE reservaciones
            SET nombre = ?, telefono = ?, fecha = ?, hora = ?, tipo = ?
            WHERE nombre = ? AND telefono = ? AND fecha = ? AND hora = ? AND tipo = ?
        ''', (
            nombre, telefono, fecha, hora, tipo, self.reserva['nombre'], self.reserva['telefono'],
            self.reserva['fecha'],
            self.reserva['hora'], self.reserva['tipo_uña']))
        conn.commit()
        conn.close()

        self.reserva['nombre'] = nombre
        self.reserva['telefono'] = telefono
        self.reserva['fecha'] = fecha
        self.reserva['hora'] = hora
        self.reserva['tipo_uña'] = tipo
        self.edit_window.destroy()
        actualizar_reservas()

    def cancelar(self):
        response = messagebox.askyesno("Cancelar",
                                       f"¿Está seguro de que desea cancelar la cita de {self.reserva['nombre']}?")
        if response:
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE reservaciones
                SET terminado = ?
                WHERE nombre = ? AND telefono = ? AND fecha = ? AND hora = ? AND tipo = ?
            ''', (True, self.reserva['nombre'], self.reserva['telefono'], self.reserva['fecha'], self.reserva['hora'],
                  self.reserva['tipo_uña']))
            conn.commit()
            conn.close()
            actualizar_reservas()


def obtener_reservas():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, telefono, tipo, precio, fecha, hora FROM reservaciones')
    reservas = [
        {"nombre": row[0], "telefono": row[1], "tipo_uña": row[2], "precio": row[3], "fecha": row[4], "hora": row[5]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return reservas


reservas = obtener_reservas()


def actualizar_reservas():
    global frame_canvas, canvas
    for widget in frame_canvas.winfo_children():
        widget.destroy()
    for reserva in reservas:
        Reservation_Frame(master=frame_canvas, reserva=reserva)
    frame_canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def init_ver_reservaciones():
    global frame_canvas, canvas
    root = tk.Tk()
    root.title("Reservación de Uñas")
    root.geometry("600x600")

    canvas = tk.Canvas(root, bg='#e6e6e6')
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    frame_canvas = tk.Frame(canvas, bg='#e6e6e6')
    canvas.create_window((0, 0), window=frame_canvas, anchor="nw")

    actualizar_reservas()

    root.mainloop()
