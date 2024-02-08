import sys
import logo
from turtle import width 
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexion import Comunicacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('Master Chef/Master Chef.ui', self)

        self.boton_menu.clicked.connect(self.mover_menu)
        self.database = Comunicacion()

        #oculta el boton minSize
        self.boton_minSize.hide()
    

        #funciones de los botones de la ventana
        #self.boton_minimizar.clicked.connect(self.control_boton_minimizar)
        self.boton_minSize.clicked.connect(self.control_boton_minSize)
        self.boton_maxSize.clicked.connect(self.control_boton_maxSize)
        self.boton_cerrar.clicked.connect(lambda: self.close())

        #elimina barra de titulo -opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover la ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #funciones botones del menu lateral

        self.boton_organizador.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_organizador))
        self.boton_registro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_registro))
        self.boton_chef.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_chef))
        self.boton_patrocinador.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_patrocinador))
        self.boton_asistente.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_asistente))
        self.boton_Menu.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_menu))
        self.boton_recetas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_receta))
        self.boton_ingrediente.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_ingredientes))
        self.boton_clasificacion.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_clasificacion))
        self.boton_contacto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_contacto))
        self.boton_premio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_premio))

        # self.boton_organizador.clicked.connect(self.mostrar_elementos)
        # self.boton_registro.clicked.connect(self.mostrar_elementos)
        # self.boton_chef.clicked.connect(self.mostrar_elementos)
        # self.boton_patrocinador.clicked.connect(self.mostrar_elementos)
        # self.boton_asistente.clicked.connect(self.mostrar_elementos)
        # self.boton_Menu.clicked.connect(self.mostrar_elementos)
        # self.boton_recetas.clicked.connect(self.mostrar_elementos)
        # self.boton_ingrediente.clicked.connect(self.mostrar_elementos)
        # self.boton_clasificacion.clicked.connect(self.mostrar_elementos)
        # self.boton_contacto.clicked.connect(self.mostrar_elementos)
        self.boton_premio.clicked.connect(self.mostrar_elementos)


        #funciones de los botones de registrar de las paginas
        # self.btn_registrarOrg.clicked.connect(self.insertar_elementos)
        # self.btn_registrarReg.clicked.connect(self.insertar_elementos)
        # self.btn_registrarChef.clicked.connect(self.insertar_elementos)
        # self.btn_registrarPatroc.clicked.connect(self.insertar_elementos)
        # self.btn_registrarAsist.clicked.connect(self.insertar_elementos)
        # self.btn_registrarMenu.clicked.connect(self.insertar_elementos)
        # self.btn_registrarReceta.clicked.connect(self.insertar_elementos)
        # self.btn_registrarIngred.clicked.connect(self.insertar_elementos)
        # self.btn_registrarClasif.clicked.connect(self.insertar_elementos)
        # self.btn_registrarContac.clicked.connect(self.insertar_elementos)

        # # Botones de Eliminar de las paginas
        # self.btn_eliminarOrg.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarReg.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarChef.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarPatroc.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarAsist.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarMenu.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarReceta.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarIngred.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarClasif.clicked.connect(self.eliminar_elemento)
        # self.btn_eliminarContac.clicked.connect(self.eliminar_elemento)

    #     #ancho de columna adaptable
        self.tabla_organizador.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_registro.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_chef.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_patrocinador.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_asistentes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_Menu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_receta.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_ingredientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_clasificacion.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_contacto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_premio.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    
    def control_boton_minSize(self):
        self.showNormal()
        self.boton_minSize.hide()
        self.boton_maxSize.show()

    def control_boton_maxSize(self):
        self.showMaximized()
        self.boton_maxSize.hide()
        self.boton_minSize.show()

    #mover ventana
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons()== QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()
                event.accept()
        
        if event.globalPos().y() <=10:
            self.showMaximized()
            self.boton_maxSize.hide()
            self.boton_minSize.show()
        else:
            self.showNormal()
            self.boton_minSize.hide()
            self.boton_maxSize.show()

    #mover el menu lateral izquierdo
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width == 0:
                extender = 300
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    # FUNCIONES 

    def mostrar_elementos(self):
        datos = self.database.mostrar_productos()
        i = len(datos)
        self.tabla_premio.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.codigo = row[0]
            self.tabla_premio.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1])) 
            self.tabla_premio.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2])) 
            self.tabla_premio.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3])) 
            self.tabla_premio.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4])) 
            
            tablerow +=1
            

    # def insertar_elementos(self):
    #     nombre = self.entry_nombreOrg.text().upper()
    #     apellido1 = self.entry_apellidoOrg.text().upper()
    #     apellido2 = self.entry_apellido2Org.text().upper()
    #     nacimiento = self.entry_fechaOrg.text().upper()
    #     edad = self.entry_edadOrg.text().upper()
    #     supervisor = self.entry_supervOrg.text().upper()

    #     if nombre != '' and apellido1 != '' and apellido2 != '' and nacimiento != '' and edad != '' and supervisor != '' :
    #         self.naodatabase.insertar_productos(nombre, apellido1, apellido2, nacimiento, edad, supervisor)
    #         self.entry_nombreOrg.clear()            
    #         self.entry_apellidoOrg.clear()
    #         self.entry_apellido2Org.clear()
    #         self.entry_fechaOrg.clear()
    #         self.entry_edadOrg.clear()
    #         self.entry_supervOrg.clear()
            
    #     else:
    #         self.signal_registro.setText('Hay espacios vacios')



    # def eliminar_elemento(self):
    #     self.row_flag = self.tabla_eliminar.currentRow()
    #     if self.row_flag == 0:
    #         self.tabla_eliminar.removeRow(0)
    #         self.naodatabase.eliminar_productos("'"+ self.producto_a_borrar +"'")
    #         self.signal_eliminar.setText('Producto Eliminado')            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
    