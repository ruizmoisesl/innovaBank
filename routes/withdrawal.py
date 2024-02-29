from flask import Flask,request, redirect, url_for,session
from flask_mysqldb import MySQL

app= Flask(__name__)
mysql= MySQL(app)

def retiro():
    if request.method == 'POST':
        pin = int(request.form['pin'])
        cursor = mysql.connection.cursor()
        id_usuario = session.get('id')
        cursor.execute('SELECT pin FROM usuario WHERE id= %s',(id_usuario,))
        pinb = int(cursor.fetchone()[0])
        if pin == pinb:
            cantidad_retiro= float(request.form['cantidad_retiro'])
            saldo_actual= float(session.get('saldo'))
            if cantidad_retiro <= saldo_actual:
                saldo_nuevo= saldo_actual-cantidad_retiro
                n_cuenta= session.get('numero_cuenta')
                cursor= mysql.connection.cursor()
                cursor.execute('UPDATE cuenta SET saldo = %s WHERE numero_cuenta = %s', (saldo_nuevo, n_cuenta,))
                mysql.connection.commit()
                session['saldo']= saldo_nuevo
                return redirect(url_for('interfaz'))
            else:
                return 'SALDO INSUFICIENTE'