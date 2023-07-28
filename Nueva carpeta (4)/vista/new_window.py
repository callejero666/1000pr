import tkinter as tk
import tkinter.ttk as ttk
import json

class NewWindow:
    def __init__(self, master, numero_cuadro):
        self.master = master
        self.master.title(f"Cuadro {numero_cuadro}")
        self.master.geometry("800x600")

        estilo = ttk.Style(self.master)
        self.master.configure(bg='black')
        estilo.configure('TLabel', background='black', foreground='red', font=('Roboto', 16, 'bold'))
        estilo.configure('TButton', background='dark grey', font=('Open Sans', 12, 'bold'))

        label = ttk.Label(self.master, text=f"Contenido del Cuadro {numero_cuadro}", style='TLabel')
        label.pack(padx=15, pady=15)

        # Cargar datos desde el archivo JSON ('historial_eventos.json')
        with open('J:\copia de seguridad\Desktop\tpintegrador\historial_eventos.json', 'r') as file:
            historial_eventos = json.load(file)

        # Crear una instancia de ttk.Treeview
        tabla = ttk.Treeview(self.master)

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

# Ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")

    btn_open_window = ttk.Button(root, text="Abrir Ventana de Historial", command=lambda: NewWindow(tk.Toplevel(root), 1))
    btn_open_window.pack(pady=20)

    root.mainloop()
