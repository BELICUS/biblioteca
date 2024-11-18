#Importando  flask y algunos paquetes
from flask import Flask, render_template, request, redirect, url_for
from confiDB import *  #Importando conexion BD

#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

app.secret_key = '97110c78ae51a45afcb3380af008f90b23a5d1616bf19bc29098105da20fe'


#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/index.html')
      
      
#Buscar empleado
@app.route('/buscar_empleado', methods=['GET','POST'])
def buscar_empleado():
    if request.method    == "POST":
        search           = request.form['buscar']
        conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
        cur      = conexion_MySQLdb.cursor(dictionary=True)
        querySQL = cur.execute("SELECT * FROM trabajadores WHERE nombre='%s' " % (search,))
        resultadoBusqueda = cur.fetchone()  
        cur.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        return render_template('public/resultadoBusqueda.html', miData = resultadoBusqueda, busqueda = search)
    return redirect(url_for('inicio'))  
   
#agregar datos
@app.route('/agregar_libro', methods=['GET', 'POST'])
def agregar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['autor']
        url = request.form['anio']
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor()
        cur.execute("INSERT INTO trabajadores (nombre, email, fecha_ingreso) VALUES (%s, %s, %s)", (titulo, descripcion, url))
        conexion_MySQLdb.commit()
        cur.close()
        conexion_MySQLdb.close()
        return redirect(url_for('inicio'))
    return render_template('public/resultadoBusqueda.html')
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    
    

if __name__ == "__main__":
    app.run(debug=True, port=8000)
