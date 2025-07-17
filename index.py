from pytubefix import YouTube
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import filedialog
from tkinter import ttk

def descargar_mp3():
    link = entrada_url.get()
    try:
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first()
        archivo_salida = audio.download(output_path=download_path.get())
        nombre_base, extension = os.path.splitext(archivo_salida)
        nuevo_archivo = nombre_base + '.mp3'
        os.rename(archivo_salida, nuevo_archivo)
        messagebox.showinfo("¡Descarga exitosa!", f"El vídeo: {yt.title}. Se ha descargado exitosamente como archivo MP3 en la ruta: {download_path.get()}")
    except Exception as e:
        print("Error al descargar MP3:", str(e))
        messagebox.showwarning("No es posible descargar", "¡Esto es una advertencia importante! \nHubo un error al descargar el MP3 del URL proporcionado: " + link)

def descargar_mp4():
    link = entrada_url.get()
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        archivo_salida = video.download(output_path=download_path.get())
        messagebox.showinfo("¡Descarga exitosa!", f"El vídeo: {yt.title}. Se ha descargado exitosamente como archivo MP4 en la ruta: {download_path.get()}")
    except Exception as e:
        print("Error al descargar MP4:", str(e))
        messagebox.showwarning("No es posible descargar", "¡Esto es una advertencia importante! \nHubo un error al descargar el MP4 del URL proporcionado: " + link)

# Crear una instancia de la ventana principal
ventana = tk.Tk()
ventana.title("PyTube")
ventana.resizable(width=False, height=False)
ventana.iconbitmap(os.path.abspath("favicon.ico"))
ventana.geometry("300x200")

download_path = tk.StringVar()
download_path.set("")

#FONT
font = ("Arial", 12, "bold")

estilo = ttk.Style()
estilo.configure("TButton", padding=(0, 0), font=font, background="white")


# Etiqueta e entrada para la URL
etiqueta_url = tk.Label(ventana, text="Ingresa la URL de YouTube:", font=("Arial", 12, "bold"))
etiqueta_url.pack()
# Crear un Frame para el campo de entrada
frame_entrada = tk.Frame(ventana, bg="white", highlightbackground="blue", highlightthickness=2)
frame_entrada.pack(pady=5)

entrada_url = tk.Entry(frame_entrada, font=font, bg="white")
entrada_url.pack()


# Botones para descargar en MP3 o MP4
boton_mp3 = tk.Button(ventana, text="Descargar MP3", command=descargar_mp3, font=font, relief="raised", background="white", borderwidth=2, highlightbackground="black")
boton_mp3.pack(pady=2)

boton_mp4 = tk.Button(ventana, text="Descargar MP4", command=descargar_mp4, font=font, relief="raised", background="white", borderwidth=2, highlightbackground="black")
boton_mp4.pack(pady=2)



# Etiqueta para mostrar el resultado de la descarga
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()

def seleccionar_carpeta_destino():
    carpeta_destino = filedialog.askdirectory()
    if carpeta_destino:
        download_path.set(carpeta_destino)

# Luego, puedes asociar esta función a un botón, por ejemplo:
boton_seleccionar_carpeta = ttk.Button(ventana, text="Seleccionar Carpeta de Destino", command=seleccionar_carpeta_destino, style="TButton")
boton_seleccionar_carpeta.pack(pady=1)

# Lanzar el bucle principal
ventana.mainloop()
