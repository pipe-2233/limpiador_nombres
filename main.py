import os
import tkinter as tk
from tkinter import filedialog, messagebox

# ----- FUNCIONES -----

def seleccionar_carpeta():
    ruta = filedialog.askdirectory()
    if ruta:
        carpeta_var.set(ruta)
        listar_archivos(ruta)

def listar_archivos(ruta):
    lista_archivos.delete(0, tk.END)
    for archivo in os.listdir(ruta):
        if os.path.isfile(os.path.join(ruta, archivo)):
            lista_archivos.insert(tk.END, archivo)

def limpiar_nombre(nombre):
    nombre = nombre.strip().lower().replace(" ", "_")
    caracteres_invalidos = ['!', '#', '$', '%', '&', '(', ')', '@']
    for c in caracteres_invalidos:
        nombre = nombre.replace(c, "")
    return nombre

def renombrar_archivos():
    ruta = carpeta_var.get()
    if not ruta:
        messagebox.showerror("Error", "Selecciona una carpeta primero.")
        return

    renombrados = 0
    for archivo in os.listdir(ruta):
        ruta_actual = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_actual):
            nuevo_nombre = limpiar_nombre(archivo)
            nueva_ruta = os.path.join(ruta, nuevo_nombre)
            try:
                os.rename(ruta_actual, nueva_ruta)
                renombrados += 1
            except Exception as e:
                print(f"Error al renombrar {archivo}: {e}")

    listar_archivos(ruta)
    messagebox.showinfo("Renombrado", f"Se renombraron {renombrados} archivos.")

# ----- INTERFAZ GRÁFICA (GUI) -----

ventana = tk.Tk()
ventana.title("Renombrador Masivo de Archivos")
ventana.geometry("600x400")

carpeta_var = tk.StringVar()

tk.Label(ventana, text="Ruta de carpeta:").pack(pady=5)
tk.Entry(ventana, textvariable=carpeta_var, width=50).pack(pady=5)
tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta).pack(pady=5)

lista_archivos = tk.Listbox(ventana, width=80, height=15)
lista_archivos.pack(pady=10)

tk.Button(ventana, text="Renombrar archivos", bg="green", fg="white", command=renombrar_archivos).pack(pady=10)

ventana.mainloop()
