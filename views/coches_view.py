#from controllers import coches_controller
from controllers.coches_controller import CochesController
from tkinter import Tk,Label,Entry,Button,messagebox, StringVar,Menu,Frame,ttk


class CochesView:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()
    def borrarPantalla(self):
      for widget in self.ventana.winfo_children():
          widget.destroy()
 
    def barraMenu(self):
            #Menu de Opciones
            menuBar = Menu(self.ventana)
            self.ventana.config(menu=menuBar)


            menuPrincipal = Menu(menuBar , tearoff=False)
            menuBar.add_cascade(label="Principal" , menu=menuPrincipal)
            menuPrincipal.add_command(label="Menu Principal",command=self.main)
            menuPrincipal.add_command(label="Menu Acciones",command=self.menu_acciones)
            menuPrincipal.add_separator()
            menuPrincipal.add_command(label="Salir",command=self.ventana.quit)
                    
            accionesMenu = Menu(menuBar , tearoff=False)
            menuBar.add_cascade(label="Acciones" , menu=accionesMenu)
            accionesMenu.add_command(label="Agregar",command=self.insertar_coche_view)
            accionesMenu.add_command(label="Borrar",command=self.eliminar_coche_view)
            accionesMenu.add_command(label="Modificar",command=self.modificar_coche_view)
            accionesMenu.add_command(label="Mostrar",command=self.consultar_coche_view)
            accionesMenu.add_separator()
            accionesMenu.add_command(label="Regresar",command=self.main) 
    
    def main(self):
       self.borrarPantalla()
       self.barraMenu()
       Label(self.ventana,text="::: MENU PRINCIPAL :::").pack(pady=20)
       self.frame=Frame(self.ventana)
       self.frame.pack(pady=10)
       
       Button(self.frame,text="Coches",width=10,height=3,command=self.menu_acciones).grid(row=0,column=0,pady=10,padx=10,sticky="e")
       Button(self.frame,text="Salir",width=10,height=3,command=self.ventana.quit).grid(row=0,column=1,pady=10,padx=10,sticky="e")
    
    def menu_acciones(self):
        self.borrarPantalla()
        self.barraMenu()
        tipo="Coche"
        Label(self.ventana,text=f"...::: Menu de {tipo} :::...").pack(pady=10)
        
        self.frame=Frame(self.ventana)
        self.frame.pack(pady=10)
        Button(self.frame,text="Agregar",width=10,height=3,command=self.insertar_coche_view).grid(row=0,column=0,pady=10,padx=10,sticky="e")
        Button(self.frame,text="Borrar",width=10,height=3,command=self.eliminar_coche_view).grid(row=0,column=1,pady=10,padx=10,sticky="w")
        Button(self.frame,text="Modificar",width=10,height=3,command=self.modificar_coche_view).grid(row=1,column=0,pady=10,padx=10,sticky="e")
        Button(self.frame,text="Mostrar",width=10,height=3,command=self.consultar_coche_view).grid(row=1,column=1,pady=10,padx=10,sticky="w")
        Button(self.frame,text="Regresar",width=10,height=3,command=self.main).grid(row=2,column=0,pady=10,padx=10,columnspan=2)
        
    def insertar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="...Ingresar los datos del Coche").pack(pady=10)
        
        self.frame=Frame(self.ventana)
        self.frame.pack(pady=10)
        
        Label(self.frame,text="Marca: ").grid(row=0,column=0,pady=5,padx=5, sticky="e")
        self.marca=Entry(self.frame)
        self.marca.focus()
        self.marca.grid(row=0,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame,text="Color: ").grid(row=1,column=0,pady=5,padx=5, sticky="e")
        self.color=Entry(self.frame)
        self.color.grid(row=1,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame,text="Modelo: ").grid(row=2,column=0,pady=5,padx=5, sticky="e")
        self.modelo=Entry(self.frame)
        self.modelo.grid(row=2,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame,text="Velocidad: ").grid(row=3,column=0,pady=5,padx=5, sticky="e")
        self.velocidad=Entry(self.frame)
        self.velocidad.grid(row=3,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame,text="Potencia: ").grid(row=4,column=0,pady=5,padx=5, sticky="e")
        self.potencia=Entry(self.frame)
        self.potencia.grid(row=4,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame,text="# de Asientos: ").grid(row=5,column=0,pady=5,padx=5, sticky="e")
        self.asientos=Entry(self.frame)
        self.asientos.grid(row=5,column=1,pady=5,padx=5, sticky="w")
        
        Button(self.frame,text=":: Agregar ::",command=lambda:{CochesController.insertar_coche_controller(self),self.insertar_coche_view()}).grid(row=6,column=0,pady=10,padx=5,sticky="e")
        Button(self.frame,text=":: Regresar ::",command=self.menu_acciones).grid(row=6,column=1,pady=10,padx=5,sticky="w")
       
    def eliminar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="...Ingresar el ID del coche a eliminar").pack(pady=10)
        
        self.frame=Frame(self.ventana)
        self.frame.pack(pady=10)        
        
        Label(self.frame,text="ID: ").grid(row=0,column=0,pady=5,padx=5, sticky="e")
        self.id=Entry(self.frame)
        self.id.focus()
        self.id.grid(row=0,column=1,pady=5,padx=5,sticky="w")
        
        self.btn_buscar=Button(self.frame,text=":: Buscar ::",command= lambda:CochesController.buscar_controller(self,"eliminar"))
        self.btn_buscar.grid(row=1,column=0,padx=5,pady=5,columnspan=2)
        self.btn_eliminar=Button(self.frame,text=":: Eliminar ::",state="disabled",command=lambda:{CochesController.eliminar_coche_controller(self),self.eliminar_coche_view()})
        self.btn_eliminar.grid(row=2,column=0,padx=5,pady=5)
        Button(self.frame,text=":: Regresar ::",command=self.menu_acciones).grid(row=2,column=1,pady=5, padx=5)
        
    def consultar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="..:: Consultar Coches ::..").pack(pady=10)
        # Tabla
        self.tree =ttk.Treeview(self.ventana, columns=("ID", "Marca", "Color", "Modelo","Velocidad","Potencia","Asientos"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.column("ID", width=40, anchor="w")
        self.tree.heading("Marca", text="Marca")
        self.tree.column("Marca", width=60, anchor="w")
        self.tree.heading("Color", text="Color")
        self.tree.column("Color", width=60, anchor="w")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.column("Modelo", width=60, anchor="w")
        self.tree.heading("Velocidad", text="Velocidad")
        self.tree.column("Velocidad", width=60, anchor="w")
        self.tree.heading("Potencia", text="Potencia")
        self.tree.column("Potencia", width=60, anchor="w")
        self.tree.heading("Asientos", text="Asientos")
        self.tree.column("Asientos", width=60, anchor="w")
        self.tree.pack(fill="both", expand=False)
        CochesController.consultar_coche_controller(self)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
    
    def modificar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)    
        self.frame2=Frame(self.ventana)
        self.frame2.pack(pady=10)
        
        Label(self.frame1,text="...Ingresar el ID del coche a modificar").grid(row=0,column=0,pady=5,padx=5, columnspan=2)
        
        Label(self.frame1,text="ID: ").grid(row=1,column=0,pady=5,padx=5, sticky="e")
        self.id=Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        self.btn_buscar=Button(self.frame1,text=":: Buscar ::",command= lambda:CochesController.buscar_controller(self,"modificar"))
        self.btn_buscar.grid(row=2,column=0,padx=5,pady=5,columnspan=2)
        
        Label(self.frame2,text="...Datos del Coche").grid(row=0,column=0,pady=5,padx=5, columnspan=2)
        
        # Variables asociadas a los campos
        self.var_marca = StringVar()
        self.var_color = StringVar()
        self.var_modelo = StringVar()
        self.var_velocidad = StringVar()
        self.var_potencia = StringVar()
        self.var_asientos = StringVar()
        
        Label(self.frame2,text="Marca: ").grid(row=1,column=0,pady=5,padx=5, sticky="e")
        self.marca=Entry(self.frame2,textvariable=self.var_marca)
        self.marca.grid(row=1,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame2,text="Color: ").grid(row=2,column=0,pady=5,padx=5, sticky="e")
        self.color=Entry(self.frame2,textvariable=self.var_color)
        self.color.grid(row=2,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame2,text="Modelo: ").grid(row=3,column=0,pady=5,padx=5, sticky="e")
        self.modelo=Entry(self.frame2,textvariable=self.var_modelo)
        self.modelo.grid(row=3,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame2,text="Velocidad: ").grid(row=4,column=0,pady=5,padx=5, sticky="e")
        self.velocidad=Entry(self.frame2,textvariable=self.var_velocidad)
        self.velocidad.grid(row=4,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame2,text="Potencia: ").grid(row=5,column=0,pady=5,padx=5, sticky="e")
        self.potencia=Entry(self.frame2,textvariable=self.var_potencia)
        self.potencia.grid(row=5,column=1,pady=5,padx=5, sticky="w")
        
        Label(self.frame2,text="# de Asientos: ").grid(row=6,column=0,pady=5,padx=5, sticky="e")
        self.asientos=Entry(self.frame2,textvariable=self.var_asientos)
        self.asientos.grid(row=6,column=1,pady=5,padx=5, sticky="w")
        
        self.btn_modificar=Button(self.frame2,text=":: Modificar ::",state="disabled",command=lambda: {CochesController.modificar_coche_controller(self),self.modificar_coche_view()})
        self.btn_modificar.grid(row=7,column=0,pady=5,padx=5, sticky="e")
        
        Button(self.frame2,text=":: Regresar ::",command=self.menu_acciones).grid(row=7,column=1,pady=5,padx=5, sticky="w")
        
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
        if resp==True:
            return True
        else:
            return False

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::",message="...¡Accion Realizada con Exito!...")
        else:
            messagebox.showerror(title=":: Verifique por favor ::",message="...¡Esta Accion no pudo realizarse en este momento!...")

    def encontro(self,coche1,tipo_accion):
        if len(coche1)>0:
            messagebox.showinfo(title="...!REGISTRO ENCONTRADO!...", message=f"El regitro fue encontrado con exito, puedes {tipo_accion}")
            self.cambiar_estado_btn(True, tipo_accion)
            if tipo_accion=="modificar":
                self.var_marca.set(coche1[0][1])
                self.var_color.set(coche1[0][2])
                self.var_modelo.set(coche1[0][3])
                self.var_velocidad.set(coche1[0][4])
                self.var_potencia.set(coche1[0][5])
                self.var_asientos.set(coche1[0][6])
        else:
                messagebox.showerror(title="...!REGISTRO NO ENCONTRADO!...", message=f"El regitro no fue encontrado, no puedes {tipo_accion}")
                self.cambiar_estado_btn(False, tipo_accion) 