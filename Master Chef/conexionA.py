import psycopg2

class Comunicacion():

    def __init__(self):    
        self.conexion = psycopg2.connect("dbname=masterChef user = postgres password = XD")
                                            

    def insertar_productos(self, nombre, apeellido1, apellido2, nacimiento, edad, supervisor):
        cur = self.conexion.cursor()
        sql = ''' INSERT INTO organizador (NOMBRE_ORG, APELLIDO_1, APELLIDO_2, FECHA_NAC, EDAD_ORG, IS_SUPERVISOR)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(nombre, apeellido1, apellido2, nacimiento, edad, supervisor)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM premio"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def eliminar_productos(self,nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM inventario WHERE CODIGO or PRODUCTO = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

