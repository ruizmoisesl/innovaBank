from flask import Flask,request, redirect, url_for,session
from flask_mysqldb import MySQL

app= Flask(__name__)
mysql= MySQL(app)

def login():
    if request.method == 'POST':
        documento = request.form['Documento']
        n_documento = request.form['ndocumento']
        contraseña = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM usuario WHERE tipo_documento = %s AND numero_documento = %s AND contraseña = %s ',(documento,n_documento, contraseña))
        result = cursor.fetchall()
        if result:
            id_usuario = result[0][0]
            cursor.execute('SELECT * FROM cuenta WHERE id_usuario = %s ', (id_usuario,))
            cuenta = cursor.fetchall()
            if cuenta:
                session['id']= result[0][0]
                session['nombre'] = result[0][1]
                session['saldo'] = cuenta[0][2]
                session['numero_cuenta'] = cuenta[0][1]
                return redirect(url_for('interfaz'))
            else:
                return 'Usuario no encontrado.'
        else:
            return 'Usuario no existente'
