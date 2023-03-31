-- Funciones

-- Creando una tabla con una funcion
create or replace function crearTabla()
returns text
as $$

declare
sql text;

begin

	if exists(select tablename from pg_tables where tablename = 'prueba')
		then
			sql:= 'DROP TABLE prueba;' ;
			execute sql;
			raise notice 'La Tabla prueba ha sido eliminada';
	end if;
	if not exists(select tablename from pg_tables where tablename = 'prueba')
		then
			sql:= 'CREATE TABLE prueba(
				NOMBRE VARCHAR(50),
				EDAD INTEGER,
				PAIS VARCHAR(50)
			);' ;
			execute sql;
			raise notice 'La Tabla prueba ha sido creada con exito';

	end if;
	
	insert into prueba (nombre, edad, pais) values ('Leo', 21, 'Cuba');
	raise notice 'Datos incertados en la tabla prueba';
	
return 'Tabla creada con exito';

end;
$$ language plpgsql;

select crearTabla();


-- Insertando datos a una tabla
create or replace function registra_asistente(id_asistente integer, nombre_asistente varchar(50),
							apellido_1 varchar(50), apellido_2 varchar(50), edad_asistente integer,
											 is_confirm boolean)
returns text
as $$
declare
sql text;

begin
	
	if exists(select tablename from pg_tables where tablename ='asistente')
	then
		raise notice 'La tabla asistente ya existe';
		insert into asistente (id_asistente, nombre_asistente, apellido_1, apellido_2, edad_asistente,
							  is_confirm) values (id_asistente, nombre_asistente, apellido_1, apellido_2, edad_asistente,
							  is_confirm);
		
		raise notice 'Los datos han sido insertados correctamente';
	end if;
	
return 'Se Acabo! XD';

end;
$$ language plpgsql;

select registra_asistente(1, 'Pedro', 'Soto', 'Vila', 21, 'True')
select * from asistente;

-- Funcion Bucle

create or replace function bucle(numero integer)
returns integer
as $$
declare
add integer:= 0;
result integer:= 5;

begin
	while add < 5
	loop
	
	result:= result + numero;
	add:= add + 1;
	
	end loop;
	
	return result;
end;
$$ language plpgsql;

select bucle(20);
