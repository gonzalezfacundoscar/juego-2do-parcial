import sqlite3


def crear_base_de_datos(text, puntuacion):
    with sqlite3.connect("db_ranking.db") as conexion:

        try:
            sentencia = ''' create table puntajes
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )           
            '''
            conexion.execute(sentencia)
            print("se creo la tabla de puntajes")
        except sqlite3.OperationalError:
            print("La tabla puntajes ya existe")

        try:
            conexion.execute("insert into puntajes(nombre, puntaje) values (?,?)", (text, puntuacion))
            conexion.commit()
        except:
            print("error")

        cursor = conexion.execute("SELECT * FROM puntajes")
        for fila in cursor:
            print(fila)

"""

def guardar_puntuacion(nombre, puntuacion):
    conexion = sqlite3.connect('puntuaciones.db')
    cursor = conexion.cursor()

    # Crear la tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS puntuaciones (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        puntuacion INTEGER
                    )''')

    # Insertar los datos del jugador
    cursor.execute("INSERT INTO puntuaciones (nombre, puntuacion) VALUES (?, ?)", (nombre, puntuacion))

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
"""
def obtener_puntuaciones():
    conexion = sqlite3.connect("db_ranking.db")
    cursor = conexion.cursor()

    # Obtener los datos de los jugadores ordenados por puntuación descendente
    cursor.execute("SELECT nombre, puntaje FROM puntajes ORDER BY puntaje DESC")
    puntuaciones = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    return puntuaciones

