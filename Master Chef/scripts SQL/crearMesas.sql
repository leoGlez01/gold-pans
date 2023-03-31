    def crearMesas(self):
        cursor = self.conexion.cursor()
        for i in range(1,15):
            sql= "CREATE TABLE MESA"+i+"(PRODUCTO VARCHAR(50) NOT NULL, CANTIDAD INT NOT NULL, PRECIO FLOAT NOT NULL)"
            cursor.execute(sql)
         
        self.conexion.commit()
        cursor.close()