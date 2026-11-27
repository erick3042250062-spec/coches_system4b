import mysql.connector
from tkinter import messagebox
try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_coches'
    )   
    cursor=conexion.cursor(buffered=True) 
except:
    #print("...¡Por el momento no es posible conectarse con la BD, ... intentelo mas tarde ...")  
    messagebox.showinfo(title=":: !Sistema gestor de BD ::",message="...¡Por el momento no es posible conectarse con la BD, ... intentelo mas tarde ...")
  