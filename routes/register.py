from flask import Flask, url_for, request, redirect, session
from flask_mysqldb import MySQL
from routes import generarcuenta
from datetime import datetime

fecha_actual = datetime.now().date()
app = Flask(__name__)
mysql = MySQL(app)



def registro():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        fecha = request.form['fecha']
        documento = request.form['Documento']
        ndocuento = request.form['numero']
        pin = request.form['pin']
        contraseña = request.form['password']
        rcontraseña = request.form['rpassword']
        if contraseña == rcontraseña:
            cursor = mysql.connection.cursor()
            cursor.execute(
                'INSERT INTO usuario (nombre,fecha_nacimiento, tipo_documento,numero_documento,pin,contraseña,fecha_ingreso) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                (nombre, fecha, documento, ndocuento, pin, contraseña, fecha_actual))
            mysql.connection.commit()
            cursor.execute('SELECT id FROM usuario WHERE numero_documento = %s', (ndocuento,))
            result = cursor.fetchone()
            if result:
                user_id = result[0]
                numero_cuenta = generarcuenta.generar_numero_cuenta()
                saldo_inicial = 0
                cursor.execute('INSERT INTO cuenta(numero_cuenta, saldo, id_usuario) VALUES (%s, %s, %s)',
                               (numero_cuenta, saldo_inicial, user_id))
                mysql.connection.commit()
                return redirect(url_for('interfaz'))
            else:
                return 'Usuario no encontrado.'
        else:
            return 'Contraseñas no coinciden, Intente de nuevo'