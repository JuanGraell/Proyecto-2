import tkinter as tk
from tkinter import ttk,messagebox
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import pandas as pd

class Canal:
    def __init__(self, canal, categoria="No categorizado"):
        self.canal = canal
        self.categoria = categoria
        
def indicate(lb,page):
    hide_indicate()
    lb.config(bg="#158aff")
    limpiarFrame()
    page()

def hide_indicate():
    home_button_indicate.config(bg="#c3c3c3")
    canales_button_indicate.config(bg="#c3c3c3")
    suscribirse_button_indicate.config(bg="#c3c3c3")
    cerrar_button_indicate.config(bg="#c3c3c3")

def home():
    home_frame = tk.Frame(main_frame)
    lb=tk.Label(home_frame,text="Apartado Home",font=("Bold",30))
    lb.pack()
    home_frame.pack(pady=20)


def canales():
    def obtener_canales_suscritos(yt):
        # Obtener los canales a los que está suscrito el usuario
        canales = []
        request = yt.subscriptions().list(part="snippet", mine=True, maxResults=50)
        print(request)
        
        while request is not None:
            response = request.execute()
            for item in response['items']:
                canal = item['snippet']['title']
                canales.append(Canal(canal))
            request = yt.subscriptions().list_next(request, response)
        return canales

    canales_frame = tk.Frame(main_frame)
    lb = tk.Label(canales_frame, text="Apartado Canales", font=("Bold", 30))
    lb.pack()

    # Obtener los canales a los que está suscrito el usuario como objetos Canal
    canales = obtener_canales_suscritos(youtube)

    # Crear una tabla para mostrar los canales
    tabla = ttk.Treeview(canales_frame, columns=("Canal", "Categoría"), show="headings")
    tabla.heading("Canal", text="Canal")
    tabla.heading("Categoría", text="Categoría")
    tabla.pack()

    # Recorrer la lista de objetos Canal y mostrarlos en la tabla
    for i, canal in enumerate(canales):
        tabla.insert("", "end", values=(canal.canal, canal.categoria))

    canales_frame.pack(pady=20)

'''
def canales():
    def obtener_canales_suscritos(yt):
        # Obtener los canales a los que está suscrito el usuario
        canales = []
        request = yt.subscriptions().list(part="snippet", mine=True, maxResults=50)
        print(request)
        
        while request is not None:
            response = request.execute()
            for item in response['items']:
                canal = item['snippet']['title']
                canales.append(Canal(canal))
            request = yt.subscriptions().list_next(request, response)
        return canales

    canales_frame = tk.Frame(main_frame)
    lb=tk.Label(canales_frame,text="Apartado Canales",font=("Bold",30))
    lb.pack()

    # Obtener los canales a los que está suscrito el usuario como objetos Canal
    canales = obtener_canales_suscritos(youtube)

    # Crear una tabla para mostrar los canales
    tabla_canvas = tk.Canvas(canales_frame,width=400, height=350)
    tabla_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(canales_frame, orient=tk.VERTICAL, command=tabla_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tabla_canvas.configure(yscrollcommand=scrollbar.set)

    tabla = tk.Frame(tabla_canvas)
    tabla_canvas.create_window((0,0), window=tabla, anchor='nw')

    # Crear encabezados de la tabla
    tk.Label(tabla, text="Canal", font=("bold", 15)).grid(row=0, column=0, padx=10, sticky='w')
    tk.Label(tabla, text="Categoría", font=("bold", 15)).grid(row=0, column=1, padx=10, sticky='w')

    # Recorrer la lista de objetos Canal y mostrarlos en la tabla
    for i, canal in enumerate(canales):
        tk.Label(tabla, text=canal.canal, anchor='w').grid(row=i+1, column=0, padx=10, sticky='w')
        tk.Label(tabla, text=canal.categoria, anchor='w').grid(row=i+1, column=1, padx=10, sticky='w')

    tabla.update_idletasks()

    tabla_canvas.config(scrollregion=tabla_canvas.bbox('all'))

    canales_frame.pack(pady=20)
'''

'''
def suscribirse():
    def search_channels(query):
        request = youtube.search().list(
            part='id,snippet',
            q=query,
            type='channel',
            maxResults=5
        )
        response = request.execute()

        # Extrae la información relevante de la respuesta de la API de YouTube
        channels = []
        for item in response['items']:
            channel_id = item['id']['channelId']
            channel_title = item['snippet']['title']
            channel_description = item['snippet']['description']
            channels.append({'Título': channel_title, 'Descripción': channel_description, 'ID':channel_id})

        # Devuelve los resultados de búsqueda en forma de DataFrame de pandas
        return pd.DataFrame(channels)
    
    def create_table(parent, df):
        tree = ttk.Treeview(parent, columns=list(df.columns), show="headings")
        for col in df.columns:
            tree.heading(col, text=col)
        for row in df.to_numpy().tolist():
            tree.insert("", "end", values=row)
        tree.pack(side='left', fill='both', expand=True,pady=20)
        return tree
    
    def on_search():
        query = search_entry.get()
        df = search_channels(query)
        create_table(table_frame, df)

    suscribirse_frame=tk.Frame(main_frame)
    lb=tk.Label(suscribirse_frame,text="Apartado suscribirse",font=("Bold",30))
    lb.pack()

    search_label = tk.Label(suscribirse_frame, text="Término de búsqueda:")
    search_label.pack(side= 'left',padx=5, pady=20)

    search_entry = tk.Entry(suscribirse_frame)
    search_entry.pack(side='left', fill='x', padx=5, pady=20, expand=True)

    search_button = tk.Button(suscribirse_frame, text="Buscar", command=on_search)
    search_button.pack(side='left', padx=5, pady=20)

    table_frame = tk.Frame(suscribirse_frame)
    table_frame.pack(fill='both', expand=True,pady=20)

    suscribirse_frame.pack(pady=20)
'''

def suscribirse():
    def agregar_datos_busqueda():
        tabla.delete(*tabla.get_children())

        query = search_entry.get()
        busqueda = youtube.search().list(
            q=query,
            type='channel',
            part='id,snippet',
            maxResults=5
        ).execute()

        for item in busqueda['items']:
            id_canal = item['id']['channelId']
            nombre_canal = item['snippet']['title']
            descripcion_canal = item['snippet']['description']
            tabla.insert("",tk.END,text=str(nombre_canal), values=(str(descripcion_canal),str(id_canal)))
    def suscribirse_acc():
        text = tabla.item(tabla.selection())['text']
        values = tabla.item(tabla.selection())['values']
        print(values)
        messagebox.showinfo("Título del mensaje", f"El nombre del canal seleccionado es: {text}\nEl ID del canal seleccionado es: {values[1]}")
        
    suscribirse_frame=tk.Frame(main_frame)
    lb=tk.Label(suscribirse_frame,text="Apartado suscribirse",font=("Bold",30))
    lb.pack()

    search_label = tk.Label(suscribirse_frame, text="Término de búsqueda:")
    search_label.place(x=40,y=65)

    search_entry = tk.Entry(suscribirse_frame)
    search_entry.place(x=165,y=65)

    search_button = tk.Button(suscribirse_frame, text="Buscar",command=agregar_datos_busqueda)
    search_button.place(x=300,y=60)

    tabla=ttk.Treeview(suscribirse_frame,columns=("col1","col2"))

    tabla.column("#0",width=130)
    tabla.column("col1",width=200)
    tabla.column("col2",width=170)

    tabla.heading("#0",text="Nombre",anchor=tk.CENTER)
    tabla.heading("col1",text="Descripcion",anchor=tk.CENTER)
    tabla.heading("col2",text="ID",anchor=tk.CENTER)
                
    tabla.pack(pady=60)

    subscribe_button = tk.Button(suscribirse_frame, text="Suscribirse",command=suscribirse_acc)#command=on_subscribe)
    subscribe_button.pack(side=tk.BOTTOM)

    suscribirse_frame.pack(pady=20)

def limpiarFrame():
    for frame in main_frame.winfo_children():
        frame.destroy()

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

# Autorización del flujo OAuth2 del usuario
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_local_server(port=0)

# Construcción de la instancia del servicio de la API de YouTube
youtube = build('youtube', 'v3', credentials=credentials)

root = tk.Tk()
root.geometry("700x600")
root.title("Nombre app")


options_frame = tk.Frame(root, bg="#c3c3c3")

home_button=tk.Button(options_frame,text="Home",font=("bold",15),fg="#158aff",bd=0,bg="#c3c3c3",command=lambda: indicate(home_button_indicate,home))
home_button.place(x=8,y=50)
home_button_indicate=tk.Label(options_frame,text="",bg="#158aff")
home_button_indicate.place(x=3,y=50,width=5,height=40)

canales_button=tk.Button(options_frame,text="Canales",font=("bold",15),fg="#158aff",bd=0,bg="#c3c3c3",command=lambda: indicate(canales_button_indicate,canales))
canales_button.place(x=8,y=100)
canales_button_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
canales_button_indicate.place(x=3,y=100,width=5,height=40)

suscribirse_button=tk.Button(options_frame,text="Suscribir",font=("bold",15),fg="#158aff",bd=0,bg="#c3c3c3",command=lambda: indicate(suscribirse_button_indicate,suscribirse))
suscribirse_button.place(x=8,y=150)
suscribirse_button_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
suscribirse_button_indicate.place(x=3,y=150,width=5,height=40)

cerrar_button=tk.Button(options_frame,text="Cerrar",font=("bold",15),fg="#158aff",bd=0,bg="#c3c3c3",command=root.quit)
cerrar_button.place(x=8,y=200)
cerrar_button_indicate=tk.Label(options_frame,text="",bg="#c3c3c3")
cerrar_button_indicate.place(x=3,y=200,width=5,height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=600)

main_frame = tk.Frame(root,highlightbackground="black", highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=600, height=700)
home()

root.mainloop()