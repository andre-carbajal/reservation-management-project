import sqlite3
import tkinter as tk
from datetime import date
from tkinter import messagebox, ttk

from tkcalendar import Calendar


# Kiara Tuesta y Mariela Ramos
class Ver_Reservation_Frame(tk.Frame):
    def __init__(self, master=None, reserva=None, lista_servicios=None):
        super().__init__(master, bg='white', bd=2, relief="groove")
        self.master = master
        self.reserva = reserva
        self.lista_servicios = lista_servicios
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
        self.edit_window.geometry("400x500")

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.edit_window.winfo_screenwidth()
        alto_pantalla = self.edit_window.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        ancho_ventana = 400
        alto_ventana = 400
        pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

        # Establecer la geometría con la posición calculada
        self.edit_window.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

        self.edit_window.configure(bg="#f7f9fc")

        header = tk.Label(self.edit_window, text="Editar Reserva", font=("Arial", 16, "bold"), bg="#f7f9fc", fg="#333")
        header.pack(pady=10)

        form_frame = tk.Frame(self.edit_window, bg="#f7f9fc")
        form_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Nombre
        validate_alpha = self.edit_window.register(lambda v: v.replace(" ", "").isalpha() or v == "")
        tk.Label(form_frame, text="Nombre:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=0, column=0,
                                                                                               sticky="w", pady=5)
        nombre_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, validate="key",
                                validatecommand=(validate_alpha, "%P"))
        nombre_entry.insert(0, self.reserva['nombre'])
        nombre_entry.grid(row=0, column=1, pady=5)

        def validate_telefono(P):
            return (P.isdigit() and len(P) <= 9) or P == ""

        # Teléfono
        vcmd = (self.register(validate_telefono), "%P")
        tk.Label(form_frame, text="Teléfono:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=1, column=0,
                                                                                                 sticky="w", pady=5)
        telefono_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, validate="key", validatecommand=vcmd)
        telefono_entry.insert(0, self.reserva['telefono'])
        telefono_entry.grid(row=1, column=1, pady=5)

        # Fecha
        tk.Label(form_frame, text="Fecha:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=2, column=0,
                                                                                              sticky="w", pady=5)
        fecha_button = tk.Button(form_frame, text=self.reserva['fecha'], font=("Arial", 12),
                                 command=lambda: self.seleccionar_fecha(fecha_button))
        fecha_button.grid(row=2, column=1, pady=5)

        # Hora
        tk.Label(form_frame, text="Hora:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=3, column=0,
                                                                                             sticky="w", pady=5)
        horas = [f"{h:02}:00" for h in range(8, 20)]
        hora_combo = ttk.Combobox(form_frame, values=horas, font=("Arial", 12))
        hora_combo.set(self.reserva['hora'])
        hora_combo.grid(row=3, column=1, pady=5)

        # Tipo de Uña
        tk.Label(form_frame, text="Tipo de Uña:", font=("Arial", 12), bg="#f7f9fc", fg="#333").grid(row=4, column=0,
                                                                                                    sticky="w", pady=5)
        tipos_una = [item[0] for item in self.lista_servicios]
        tipo_combo = ttk.Combobox(form_frame, values=tipos_una, font=("Arial", 12), state="readonly")
        tipo_combo.set(self.reserva['tipo_uña'])
        tipo_combo.grid(row=4, column=1, pady=5)

        # Botón Guardar
        save_button = tk.Button(
            self.edit_window, text="Guardar Cambios", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
            relief="flat",
            command=lambda: self.guardar_cambios(nombre_entry.get(), telefono_entry.get(), fecha_button['text'],
                                                 hora_combo.get(), tipo_combo.get())
        )
        save_button.pack(pady=20)

    def seleccionar_fecha(self, button):
        cal_window = tk.Toplevel(self.master)
        cal_window.title("Seleccionar Fecha")
        cal_window.resizable(False, False)

        ventana_ancho = 300
        ventana_alto = 300

        pantalla_ancho = cal_window.winfo_screenwidth()
        pantalla_alto = cal_window.winfo_screenheight()

        pos_x = (pantalla_ancho // 2) - (ventana_ancho // 2)
        pos_y = (pantalla_alto // 2) - (ventana_alto // 2)

        cal_window.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")

        cal = Calendar(cal_window, selectmode='day', mindate=date.today())
        cal.pack(pady=20)

        def seleccionar():
            button.config(text=cal.get_date())
            cal_window.destroy()

        tk.Button(cal_window, text="Seleccionar", command=seleccionar).pack(pady=10)

    # Andre Carbajal
    def guardar_cambios(self, nombre, telefono, fecha, hora, tipo, lista_servicios):
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
        actualizar_reservas(lista_servicios)

    # Andre Carbajal
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


# Andre Carbajal
def obtener_reservas():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, telefono, tipo, precio, fecha, hora FROM reservaciones WHERE terminado = 0')
    reservas = [
        {"nombre": row[0], "telefono": row[1], "tipo_uña": row[2], "precio": row[3], "fecha": row[4], "hora": row[5]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return reservas


reservas = obtener_reservas()


def actualizar_reservas(lista_servicios):
    global frame_canvas, canvas
    reservas = obtener_reservas()
    for widget in frame_canvas.winfo_children():
        widget.destroy()
    if not reservas:
        no_reservas_label = tk.Label(frame_canvas, text="No hay reservaciones pendientes", font=("Arial", 14),
                                     bg='#e6e6e6')
        no_reservas_label.pack(pady=20)
    else:
        for reserva in reservas:
            Ver_Reservation_Frame(master=frame_canvas, reserva=reserva, lista_servicios=lista_servicios)
    frame_canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def init_ver_reservaciones(lista_servicios):
    global frame_canvas, canvas
    root = tk.Tk()
    root.title("Reservación de Uñas")

    # Dimensiones de la ventana
    ancho_ventana = 600
    alto_ventana = 600

    # Obtener el tamaño de la pantalla
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    # Calcular posición para centrar la ventana
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Establecer geometría centrada
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    root.resizable(False, False)

    canvas = tk.Canvas(root, bg='#e6e6e6')
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    frame_canvas = tk.Frame(canvas, bg='#e6e6e6')
    canvas.create_window((0, 0), window=frame_canvas, anchor="nw")

    def ajustar_scroll(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_canvas.bind("<Configure>", ajustar_scroll)

    # Centrar el contenido dentro del Canvas
    def centrar_contenido(event=None):
        canvas_width = canvas.winfo_width()
        frame_width = frame_canvas.winfo_width()
        if frame_width < canvas_width:
            canvas.itemconfig("window", anchor="n", width=canvas_width)
        else:
            canvas.itemconfig("window", anchor="nw", width=frame_width)

    canvas.bind("<Configure>", centrar_contenido)

    actualizar_reservas(lista_servicios)

    root.mainloop()
