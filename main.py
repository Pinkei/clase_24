import sqlite3 

#creo una base de datos:
con = sqlite3.connect("prog2.db") #si no existe la base de dato la crea 
 
 #base de datos en una aplicacion, esta enbebida 
#guardamos los datos en una carpea, estan en diferentes archivos 
#si quiero guardar un usuario tengo que crear una tabla 
# extensiones

#creo un cursero para la base de datos

cur = con.cursor() #permite hacer cualquier cosa con esto

#creo una tabla:

#id integer primary key --> es para que no se pueda repetir 
cur.execute("CREATE TABLE IF NOT EXISTS personas_id(id integer primary key, nombre, apellido)") #ejecuta una instruccion sql, crea tabla
#va entre parentesis el nombre de las columnas, si ya exixstiera la tabla persona no hace anda. no la crea.abs

#hago una consulta para ver si esta creada. 
res = cur.execute("SELECT * FROM personas_id") #si tuviera muchas columnas pongo SELECT * FROM personas
#WHERE es como una condicion 

# cur.execute("""
# INSERT INTO personas VALUES
# ("juan", "Perez")
# ("Maria", "Garcia")
# """)

# personas = [("Dario", "costas"), ("Daniela", "Maria")]

# cur.executemany("INSERT INTO personas_id (nombre, apellido) VALUES (?, ?)", personas) #los signos de pregunta me dicen donde va cada tupla

# cur.execute("DELETE FROM personas_id WHERE id = 1") #borra toda la tabla si no le pongo el WHERE 

# cur.execute("""UPDATE personas_id SET nombre = "Walter" WHERE id = 5""")
# con.commit()



print(res.fetchall())
con.close()