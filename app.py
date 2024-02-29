from flask import Flask, render_template
from flask_mysqldb import MySQL
from routes import login, forgotpassword, register,interface,transfer,consignment,withdrawal,logOut
import secrets
import os

app = Flask(__name__)

IMG_FOLDER= os.path.join('static', 'IMG')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234567'
app.config['MYSQL_DB'] = 'banco'
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.static_url_path = '/static'
app.config['UPLOAD_FOLDER']= IMG_FOLDER

mysql = MySQL(app)

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')


@app.route('/gregistro', methods=['POST'])
def gregistro():
    return register.registro()


@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')

@app.route('/interfaz')
def interfaz():
    return interface.interfaz()


@app.route('/login', methods=['POST'])
def logIn():
    return login.login()    


@app.route('/tranferencia', methods=['POST'])
def transferencia():
    return transfer.transferencia()
    
@app.route('/consignacion', methods= ['POST'])
def consignacion():
    return consignment.consignacion()

@app.route('/retiro', methods= ['POST'])
def retiro():
    return withdrawal.retiro()
            
@app.route('/logout', methods= ['POST'])
def logout():
    return logOut.logout()

@app.route('/fpassword')
def fpassword():
    return render_template('forgotpassword.html')
    
@app.route('/forgot_password', methods= ['POST'])
def forgot_password():
    return forgotpassword.forgot_password()

    
if __name__ == '__main__':
    app.run(debug=True, port=3000)
