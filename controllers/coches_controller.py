from models import coches_model
from views import coches_view


class CochesController:
    # ------------------.... Controlador o Controller del Sistema ....------------------
    def insertar_coche_controller(self):
        coches1=coches_model.CochesModel(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())                   
        respuesta=coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1    
       
    def eliminar_coche_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta=coches_model.CochesModel.eliminar(id)
        else:
            respuesta=False
        self.respuesta_sql(respuesta)
        
    def consultar_coche_controller(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in coches_model.CochesModel.consultar():
            self.tree.insert("", "end", values=row)
        
    def modificar_coche_controller(self):
        id=self.id.get()
        coches1=coches_model.CochesModel(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())  
        respuesta=coches1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coches1
    def buscar_controller(self,tipo_accion):
        id=self.id.get()      
        coche1=coches_model.CochesModel.buscar(id)
        #self.encontro(coche1,tipo_accion)
        coches_view.CochesView.encontro(self,coche1,tipo_accion)