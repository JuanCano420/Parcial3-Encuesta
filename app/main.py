import tkinter as tk
from gestor_encuestas import GestorEncuestas
from encuesta import Encuesta
from pregunta import Pregunta

# Crear una nueva encuesta
def crear_encuesta():
    titulo = entrada_titulo.get()
    if titulo:
        encuesta_actual = gestor.crear_encuesta(titulo)
        mostrar_interfaz_seleccion_preguntas(encuesta_actual)
    else:
        tk.messagebox.showerror("Error", "El título de la encuesta no puede estar vacío.")

# Mostrar la interfaz para seleccionar preguntas
def mostrar_interfaz_seleccion_preguntas(encuesta):
    ventana_preguntas = tk.Toplevel(root)
    ventana_preguntas.title(f"Seleccionar Preguntas para '{encuesta.titulo}'")

    tk.Label(ventana_preguntas, text="Preguntas disponibles:").pack()
    preguntas_disponibles = Pregunta.obtener_preguntas_predeterminadas()
    seleccionadas = []

    for pregunta in preguntas_disponibles:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(ventana_preguntas, text=pregunta.texto, variable=var)
        chk.pack(anchor='w')
        seleccionadas.append((pregunta, var))

    def guardar_preguntas():
        for pregunta, var in seleccionadas:
            if var.get():
                encuesta.agregar_pregunta(pregunta.texto)
        ventana_preguntas.destroy()
        tk.messagebox.showinfo("Éxito", f"Preguntas agregadas a '{encuesta.titulo}'")

    tk.Button(ventana_preguntas, text="Guardar", command=guardar_preguntas).pack()

# Visualizar todas las encuestas creadas
def visualizar_encuestas():
    ventana_visualizacion = tk.Toplevel(root)
    ventana_visualizacion.title("Visualizar Encuestas")
    encuestas = gestor.listar_encuestas()

    for i, encuesta in enumerate(encuestas):
        tk.Button(
            ventana_visualizacion,
            text=encuesta.titulo,
            command=lambda i=i: mostrar_detalles_encuesta(i),
        ).pack()

# Mostrar detalles de una encuesta específica
def mostrar_detalles_encuesta(indice):
    encuesta = gestor.obtener_encuesta(indice)
    ventana_detalles = tk.Toplevel(root)
    ventana_detalles.title(f"Detalles de '{encuesta.titulo}'")

    tk.Label(ventana_detalles, text=f"Título: {encuesta.titulo}").pack()
    tk.Label(ventana_detalles, text="Preguntas:").pack()
    for pregunta in encuesta.preguntas:
        tk.Label(ventana_detalles, text=f"- {pregunta}").pack()

# Ver y editar preguntas
def gestionar_preguntas():
    ventana_preguntas = tk.Toplevel(root)
    ventana_preguntas.title("Gestión de Preguntas")

    # Mostrar preguntas existentes
    tk.Label(ventana_preguntas, text="Preguntas existentes:").pack()
    lista_preguntas = tk.Listbox(ventana_preguntas, height=10)
    lista_preguntas.pack()

    preguntas = Pregunta.obtener_preguntas_predeterminadas()
    for pregunta in preguntas:
        lista_preguntas.insert(tk.END, pregunta.texto)

    # Campo para editar o agregar preguntas
    tk.Label(ventana_preguntas, text="Texto de la pregunta:").pack()
    entrada_pregunta = tk.Entry(ventana_preguntas)
    entrada_pregunta.pack()

    def agregar_pregunta():
        texto = entrada_pregunta.get()
        if texto:
            nueva_pregunta = Pregunta(texto)
            Pregunta.agregar_pregunta(nueva_pregunta)
            lista_preguntas.insert(tk.END, texto)
            entrada_pregunta.delete(0, tk.END)
            tk.messagebox.showinfo("Éxito", "Pregunta agregada exitosamente.")
        else:
            tk.messagebox.showerror("Error", "El texto de la pregunta no puede estar vacío.")

    # En el método editar_pregunta dentro de gestionar_preguntas:
    def editar_pregunta():
        seleccion = lista_preguntas.curselection()
        if seleccion:
            indice = seleccion[0]
            nuevo_texto = entrada_pregunta.get()
            if nuevo_texto:
                # Actualizar el banco de preguntas
                Pregunta.editar_pregunta(indice, nuevo_texto)
                # Actualizar la lista visible
                lista_preguntas.delete(indice)
                lista_preguntas.insert(indice, nuevo_texto)
                entrada_pregunta.delete(0, tk.END)
                tk.messagebox.showinfo("Éxito", "Pregunta editada exitosamente.")
            else:
                tk.messagebox.showerror("Error", "El texto de la pregunta no puede estar vacío.")
        else:
            tk.messagebox.showerror("Error", "Por favor selecciona una pregunta para editar.")


    # Botones de gestión
    tk.Button(ventana_preguntas, text="Agregar Pregunta", command=agregar_pregunta).pack()
    tk.Button(ventana_preguntas, text="Editar Pregunta", command=editar_pregunta).pack()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión de Encuestas")

gestor = GestorEncuestas()

# Elementos de la interfaz gráfica
tk.Label(root, text="Título de la Encuesta:").pack()
entrada_titulo = tk.Entry(root)
entrada_titulo.pack()

btn_crear_encuesta = tk.Button(root, text="Crear Encuesta", command=crear_encuesta)
btn_crear_encuesta.pack()

btn_visualizar_encuestas = tk.Button(root, text="Visualizar Encuestas", command=visualizar_encuestas)
btn_visualizar_encuestas.pack()

btn_gestionar_preguntas = tk.Button(root, text="Gestionar Preguntas", command=gestionar_preguntas)
btn_gestionar_preguntas.pack()

root.mainloop()
