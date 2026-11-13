from coches import coches
from tkinter import Tk,Label,Entry,Button,messagebox


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()
    
    # .... Vistas o Views del Sistema ....
    def borrarPantalla(self):
      for widget in self.ventana.winfo_children():
          widget.destroy()
    
    def main(self):
       self.borrarPantalla()
       Label(self.ventana,text="::: MENU PRINCIPAL :::").pack(pady=20)
       Button(self.ventana,text="1.- Coches",command=self.menu_acciones).pack(pady=10)
       Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=10)
    
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coche"
        Label(self.ventana,text=f"...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_coche_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_coche_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_coche_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_coche_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=10)
        
    def insertar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos del Coche").pack(pady=10)
        
        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)
        
        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana,text="# de Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)
        
        Button(self.ventana,text=":: Agregar ::",command=lambda:{self.insertar_coche_controller(),self.insertar_coche_view()}).pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
       
    def eliminar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del coche a eliminare").pack(pady=10)
        
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        
        self.btn_buscar=Button(self.ventana,text=":: Buscar ::",command= lambda:self.busca_controller("eliminar"))
        self.btn_buscar.pack(pady=5)
        
        self.btn_eliminar=Button(self.ventana,text=":: Eliminar ::",state="disabled",command=lambda:{self.eliminar_coche_controller(),self.eliminar_coche_view()})
        self.btn_eliminar.pack(pady=5)
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
        
    def consultar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="..:: Consultar Coches ::..").pack(pady=10)
        filas=""
        filas=self.consultar_coche_controller(filas)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
    
    def modificar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del coche a modificar").pack(pady=10)
        
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        
        Label(self.ventana,text="...Datos del Coche").pack(pady=10)
        
        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.pack(pady=5)
        
        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana,text="# de Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)
        
        Button(self.ventana,text=":: Modificar ::",command=lambda:{self.modificar_coche_controller(),self.modificar_coche_view()}).pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
        
    def cambiar_estado_btn(self,estado,tipo_accion):
        if estado:
            if tipo_accion == "eliminar":
                self.btn_eliminar.config(state="normal")
            elif tipo_accion == "modificar":
                self.btn_modificar.config(state="normal")   
        else:
            if tipo_accion == "eliminar":
                self.btn_eliminar.config(state="disabled")
            elif tipo_accion == "modificar":
                self.btn_modificar.config(state="disabled")
                
    def confirmacion_eliminar(self,tipo_accion):
        resp=messagebox.askyesno(title=":: Confirmar Accion ::",message=f"...¿Esta seguro de que desea {tipo_accion} este registro?...")
        if resp=="yes":
            return True
        else:
            return False
        
    # .... Controlador o Controller del Sistema ....
    def respuesta_sql(self,respuesta):
            if respuesta:
                messagebox.showinfo(title=":: Exitoso ::",message="...¡Accion Realizada con Exito!...")
            else:
                messagebox.showerror(title=":: Verifique por favor ::",message="...¡Esta Accion no pudo realizarse en este momento!...")
    
    def insertar_coche_controller(self):
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())                   
        respuesta=coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1    
       
    def eliminar_coche_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta=coches.Coches.eliminar(id)
        else:
            respuesta=False
        self.respuesta_sql(respuesta)
        
    def consultar_coche_controller(self,filas):
        registros=coches.Coches.consultar()
        num_coche=1
        if len(registros)>0:
           for fila in registros:
             filas=filas+(f"\n\tCoche #: {num_coche}\nID: {fila[0]}\tMarca: {fila[1]}\n\tColor: {fila[2]}\tModelo: {fila[3]}\n\tVelocidad: {fila[4]}\tPotencia: {fila[5]}\tAsientos: {fila[6]}")
             num_coche+=1
        else:
            filas="¡No se encontro informacion en la BD!..."
        return filas    
      
    def modificar_coche_controller(self):
        id=self.id.get()
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())  
        respuesta=coches1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coches1
    def busca_controller(self,tipo_accion):
        id=self.id.get()      
        coche1=coches.Coches.buscar(id)
        if len(coche1)>0:
            messagebox.showinfo(title="...!REGISTRO ENCONTRADO!...", message=f"El regitro fue encontrado con exito, puedes {tipo_accion}")
            self.cambiar_estado_btn(True, tipo_accion)
        else:
            messagebox.showerror(title="...!REGISTRO NO ENCONTRADO!...", message=f"El regitro no fue encontrado, no puedes {tipo_accion}")
            self.cambiar_estado_btn(False, tipo_accion)
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
