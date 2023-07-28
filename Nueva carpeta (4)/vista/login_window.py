import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.font import Font
from main_window import MainWindow

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de Sesión")
        self.master.geometry("300x300")
        self.master.configure(bg='black')

        fuente_titulo = Font(family="Roboto", size=20, weight="bold")
        fuente_cuerpo = Font(family="Open Sans", size=12)

        label_usuario = ttk.Label(self.master, text="Usuario:", font=fuente_titulo)
        label_usuario.pack(pady=10)

        self.entry_usuario = ttk.Entry(self.master, font=fuente_cuerpo)
        self.entry_usuario.pack(pady=5)

        label_contraseña = ttk.Label(self.master, text="Contraseña:", font=fuente_titulo)
        label_contraseña.pack(pady=10)

        self.entry_contraseña = ttk.Entry(self.master, show="*", font=fuente_cuerpo)
        self.entry_contraseña.pack(pady=5)

        self.entry_usuario.bind("<Return>", self.verificar_credenciales)
        self.entry_contraseña.bind("<Return>", self.verificar_credenciales)

        boton_verificar = ttk.Button(self.master, text="Iniciar Sesión", command=self.verificar_credenciales)
        boton_verificar.pack(pady=20)

    def verificar_credenciales(self, event=None):
        usuario_valido = "123"
        contraseña_valida = "456"

        usuario_ingresado = self.entry_usuario.get()
        contraseña_ingresada = self.entry_contraseña.get()

        if usuario_ingresado == usuario_valido and contraseña_ingresada == contraseña_valida:
            self.master.destroy()
            root = tk.Tk()
            MainWindow(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos. Inténtalo de nuevo.")
