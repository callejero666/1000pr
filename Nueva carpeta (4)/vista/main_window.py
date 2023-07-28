import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
import json

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana Principal")
        self.master.geometry("600x600")
        self.master.configure(bg='black')

        estilo = ttk.Style(self.master)
        estilo.configure('TLabel', background='black', foreground='red', font=('Roboto', 16, 'bold'))
        estilo.configure('TButton', background='dark grey', font=('Open Sans', 12, 'bold'))

        contenedor_imagenes_botones = ttk.Frame(self.master, style='My.TFrame')
        contenedor_imagenes_botones.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        estilo.configure('My.TFrame', background='black')

        self.add_image_button(contenedor_imagenes_botones, "bart.png", "historial", 1)
        self.add_image_button(contenedor_imagenes_botones, "bart.png", "new evento", 2)
        self.add_image_button(contenedor_imagenes_botones, "bart.png", "mapa", 3)

        contenedor_imagenes_botones.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def add_image_button(self, container, image_path, text, num_cuadro):
        imagen = tk.PhotoImage(file=image_path)
        boton_cuadro = ttk.Button(container, text=text, command=lambda: self.abrir_ventana_nueva_json() if num_cuadro == 1 else self.abrir_ventana_nueva(num_cuadro), compound=tk.BOTTOM)
        cuadro = ttk.Label(container, image=imagen, text=text, style='TLabel', compound=tk.BOTTOM)
        cuadro.image = imagen

        cuadro.grid(row=0, column=num_cuadro - 1, padx=15, pady=15)
        boton_cuadro.grid(row=1, column=num_cuadro - 1, padx=15, pady=5)

    def abrir_ventana_nueva_json(self):
        ventana_nueva = tk.Toplevel()
        ventana_nueva.title("Cuadro 1")
        ventana_nueva.geometry("400x300")

        estilo = ttk.Style(ventana_nueva)
        ventana_nueva.configure(bg='black')
        estilo.configure('TLabel', background='black', foreground='red', font=('Roboto', 16, 'bold'))
        estilo.configure('TButton', background='dark grey', font=('Open Sans', 12, 'bold'))

        label = ttk.Label(ventana_nueva, text="Contenido del Cuadro 1 con JSON", style='TLabel')
        label.pack(padx=15, pady=15)

        # Cargar datos desde el archivo JSON ('historial_eventos.json')
        with open('historial_eventos.json', 'r') as file:
            historial_eventos = json.load(file)

        tabla = ttk.Treeview(ventana_nueva)

        # Definir las columnas de la tabla
        tabla["columns"] = ("Nombre", "Artista", "Género", "Ubicación", "Hora Inicio", "Hora Fin", "Descripción")

        # Configurar encabezados de columna
        tabla.heading("#0", text="ID")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Artista", text="Artista")
        tabla.heading("Género", text="Género")
        tabla.heading("Ubicación", text="Ubicación")
        tabla.heading("Hora Inicio", text="Hora Inicio")
        tabla.heading("Hora Fin", text="Hora Fin")
        tabla.heading("Descripción", text="Descripción")

        # Configurar las columnas
        tabla.column("#0", width=50)
        tabla.column("Nombre", width=150)
        tabla.column("Artista", width=150)
        tabla.column("Género", width=100)
        tabla.column("Ubicación", width=150)
        tabla.column("Hora Inicio", width=150)
        tabla.column("Hora Fin", width=150)
        tabla.column("Descripción", width=200)

        # Insertar datos en la tabla
        for evento in historial_eventos:
            tabla.insert("", "end", text=evento["id"], values=(
                evento["nombre"],
                evento["artista"],
                evento["genero"],
                evento["id_ubicacion"],
                evento["hora_inicio"],
                evento["hora_fin"],
                evento["descripcion"]
            ))

        tabla.pack(padx=15, pady=15)

    def abrir_ventana_nueva(self, numero_cuadro):
        ventana_nueva = tk.Toplevel()
        ventana_nueva.title(f"Cuadro {numero_cuadro}")
        ventana_nueva.geometry("400x300")

        estilo = ttk.Style(ventana_nueva)
        ventana_nueva.configure(bg='black')
        estilo.configure('TLabel', background='black', foreground='red', font=('Roboto', 16, 'bold'))
        estilo.configure('TButton', background='dark grey', font=('Open Sans', 12, 'bold'))

        label = ttk.Label(ventana_nueva, text=f"Contenido del Cuadro {numero_cuadro}", style='TLabel')
        label.pack(padx=15, pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")

    # Create an instance of MainWindow
    main_window = MainWindow(root)

    root.mainloop()
