from flask import Flask,render_template,request, redirect, url_for,session
from flask_mysqldb import MySQL
import locale

app= Flask(__name__)
mysql= MySQL(app)

try:
    locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
except locale.Error:
    pass

def interfaz():
    nombre = session.get('nombre', 'invitado').upper()
    saldo = int(session.get('saldo', None))
    saldo_formateado = locale.currency(saldo, grouping=True) 
    numero_cuenta = session.get('numero_cuenta', None)
    return render_template('interfaz.html', nombre= nombre, saldo=saldo_formateado, numero_cuenta= numero_cuenta)