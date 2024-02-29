from flask import Flask,request, redirect, url_for,session
from flask_mysqldb import MySQL

app= Flask(__name__)
mysql= MySQL(app)

def consignacion():
    if request.method== 'POST':
        pin = int(request.form['pin'])
        cursor = mysql.connection.cursor()
        id_usuario = session.get('id')
        cursor.execute('SELECT pin FROM usuario WHERE id= %s',(id_usuario,))
        pinb = int(cursor.fetchone()[0])
        if pin == pinb:
            cantidad=float (request.form['cantidad'])
            saldo_actual= float(session.get('saldo'))
            saldo_nuevo= saldo_actual+cantidad
            n_cuenta= session.get('numero_cuenta')
            cursor.execute('UPDATE cuenta SET saldo = %s WHERE numero_cuenta = %s', (saldo_nuevo, n_cuenta))
            mysql.connection.commit()
            session['saldo']= saldo_nuevo
            return redirect(url_for('interfaz'))
        else:
            return 'PIN INCORRECTO'
