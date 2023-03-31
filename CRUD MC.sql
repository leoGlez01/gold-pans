-- Creando la tabla clasificacion
CREATE TABLE clasificacion(
	id_clasificacion INTEGER,
	nombreChef VARCHAR(50) NOT NULL,
	apellido1 VARCHAR(50) NOT NULL,
	apellido2 VARCHAR(50) NOT NULL,
	plato_popular VARCHAR(50) NOT NULL,
	puesto_clasif VARCHAR(10) NOT NULL,
	CONSTRAINT "Clasificacion_pk" PRIMARY KEY (id_clasificacion)
);

-- CRUD con la tabla organizador 
SELECT * FROM organizador;
INSERT INTO organizador VALUES (3,'Yusimi','Espinosa','Fernandez','06/10/1966', 56, 'false');
UPDATE organizador SET nombre_org= 'Leandro' WHERE id_organizador=2;
DELETE FROM organizador WHERE id_organizador=4;


