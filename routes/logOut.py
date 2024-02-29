from flask import Flask,request, redirect, url_for,session
from flask_mysqldb import MySQL

app= Flask(__name__)

def logout():
    if 'id' and 'nombre' and 'numero_cuenta' and 'saldo' in session:
        session.clear()
        return redirect(url_for('principal'))