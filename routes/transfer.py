from flask import Flask,request, redirect, url_for,session
from flask_mysqldb import MySQL

app= Flask(__name__)
mysql= MySQL(app)

def transferencia():
    if request.method == 'POST':
        pin = int(request.form['pin'])
        cursor = mysql.connection.cursor()
        id_usuario = session.get('id')
        cursor.execute('SELECT pin FROM usuario WHERE id= %s',(id_usuario,))
        pinb = int(cursor.fetchone()[0])
        if pin == pinb:
             cuenta_origen= session.get('numero_cuenta')
             saldo_origen= float(session.get('saldo'))
             vtransferenca = float(request.form['vtransferencia'])
             if saldo_origen>= vtransferenca:
                n_saldo_origen= saldo_origen-vtransferenca
                cursor.execute('UPDATE cuenta SET saldo = %s WHERE numero_cuenta = %s', (n_saldo_origen, cuenta_origen))
                n_cuenta = request.form['numero_cuenta']
                vtransferenca = float(request.form['vtransferencia'])
                cursor.execute('SELECT saldo FROM cuenta WHERE numero_cuenta = %s', (n_cuenta,))
                saldo_actual = float(cursor.fetchone()[0])
                nuevo_saldo= saldo_actual+vtransferenca
                cursor.execute('UPDATE cuenta SET saldo = %s WHERE numero_cuenta = %s', (nuevo_saldo, n_cuenta))
                mysql.connection.commit()
                session['saldo'] = n_saldo_origen
                return redirect(url_for('interfaz'))
             else:
                 return 'SALDO INSUFICIENTE'
        else: 
            return 'PIN incorrecto'