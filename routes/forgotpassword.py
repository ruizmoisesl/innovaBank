from flask import Flask,request, redirect, url_for
from flask_mysqldb import MySQL

app= Flask(__name__)
mysql= MySQL(app)

def forgot_password():
    if request.method == 'POST':
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero']
        fecha_ingreso = request.form['ingreso']
        pin = request.form['pin']  
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id,pin, fecha_ingreso FROM usuario WHERE tipo_documento =%s AND numero_documento =%s',(tipo_documento,numero_documento))
        datos = cursor.fetchall()
        if datos:
            id = datos[0][0]  
            cursor.execute('SELECT contraseña FROM usuario WHERE id = %s ', (id,))
            contraseña = cursor.fetchone()[0]  
            return f'SU CONTRASEÑA ES {contraseña}'
        else:
            return 'NO HAY DATOS VALIDOS'